# -*- coding: utf-8 -*-
from libc.math cimport sqrt, exp, log10
from cpython cimport bool
from array import array
import numpy as np
cimport numpy as np
from libc.stdlib cimport rand, RAND_MAX, srand
#from libc.time cimport time
from time import time

# make true it is random everytime
srand(int(time()))

cdef double randV():
    return rand()/(RAND_MAX*1.01)

cdef class Chromosome(object):
    cdef public int n
    cdef public double f
    cdef public np.ndarray v
    
    def __cinit__(self, n):
        self.n = n
        #self.v = <double *>malloc(n*cython.sizeof(double))
        self.v = np.zeros(n)
        # the light intensity
        self.f = 0
    
    cdef double distance(self, Chromosome obj):
        cdef double dist
        dist = 0
        for i in range(self.n):
            dist += (self.v[i] - obj.v[i])**2
        return sqrt(dist)
    
    cdef void assign(self, Chromosome obj):
        self.n = obj.n
        self.v[:] = obj.v
        self.f = obj.f

cdef class Firefly(object):
    cdef int D, n, maxGen, rp, gen
    cdef double alpha, alpha0, betaMin, beta0, gamma, timeS, timeE
    cdef object func, progress_fun, interrupt_fun
    cdef np.ndarray lb, ub
    cdef np.ndarray fireflys
    cdef Chromosome genbest, bestFirefly
    cdef object fitnessTime, fitnessParameter
    
    def __init__(self, object func, object settings, object progress_fun=None, object interrupt_fun=None):
        """
        settings = {
            'n',
            'alpha',
            'betaMin',
            'beta0',
            'gamma',
            'maxGen',
            'report'
        }
        """
        # object function
        self.func = func
        # D, the dimension of question and each firefly will random place position in this landscape
        self.D = self.func.get_nParm()
        # n, the population size of fireflies
        self.n = settings['n']
        # alpha, the step size
        self.alpha = settings['alpha']
        # alpha0, use to calculate_new_alpha
        self.alpha0 = settings['alpha']
        # betamin, the minimal attraction, must not less than this
        self.betaMin = settings['betaMin']
        # beta0, the attraction of two firefly in 0 distance
        self.beta0 = settings['beta0']
        # gamma
        self.gamma = settings['gamma']
        # low bound
        self.lb = np.array(self.func.get_lower())
        # up bound
        self.ub = np.array(self.func.get_upper())
        # all fireflies, depend on population n
        self.fireflys = np.ndarray((self.n,), dtype=np.object)
        for i in range(self.n):
            self.fireflys[i] = Chromosome(self.D)
        # maxima generation, report: how many generation report status once
        self.maxGen = settings['maxGen']
        self.rp = settings['report']
        self.progress_fun = progress_fun
        self.interrupt_fun = interrupt_fun
        # generation of current
        self.gen = 0
        # best firefly of geneation
        self.genbest = Chromosome(self.D)
        # best firefly so far
        self.bestFirefly = Chromosome(self.D)
        
        # setup benchmark
        self.timeS = time()
        self.timeE = 0
        self.fitnessTime = ''
        self.fitnessParameter = ''
    
    cdef void init(self):
        cdef int i, j
        for i in range(self.n):
            # init the Chromosome
            for j in range(self.D):
                self.fireflys[i].v[j]=randV()*(self.ub[j]-self.lb[j])+self.lb[j];
    
    cdef void movefireflies(self):
        cdef int i, j, k
        cdef bool is_move
        for i in range(self.n):
            is_move = False
            for j in range(self.n):
                is_move |= self.movefly(self.fireflys[i], self.fireflys[j])
            if not is_move:
                for k in range(self.D):
                    scale = self.ub[k] - self.lb[k]
                    self.fireflys[i].v[k] += self.alpha * (randV() - 0.5) * scale
                    self.fireflys[i].v[k] = self.check(k, self.fireflys[i].v[k])
    
    cdef void evaluate(self):
        cdef Chromosome firefly
        for firefly in self.fireflys:
            firefly.f = self.func(firefly.v)
    
    cdef bool movefly(self, Chromosome me, Chromosome she):
        cdef double r, beta
        cdef int i
        if me.f > she.f:
            r = me.distance(she)
            beta = (self.beta0-self.betaMin)*exp(-self.gamma*(r**2))+self.betaMin
            for i in range(me.n):
                scale = self.ub[i] - self.lb[i]
                me.v[i] += beta * (she.v[i] - me.v[i]) + self.alpha*(randV()-0.5) * scale
                me.v[i] = self.check(i, me.v[i])
            return True
        return False
    
    cdef double check(self, int i, double v):
        if v > self.ub[i]:
            return self.ub[i]
        elif v < self.lb[i]:
            return self.lb[i]
        else:
            return v
    
    cdef Chromosome findFirefly(self):
        return min(self.fireflys, key=lambda chrom:chrom.f)
    
    cdef void report(self):
        self.timeE = time()
        self.fitnessTime += '%d,%.4f,%.2f;'%(self.gen, self.bestFirefly.f, self.timeE - self.timeS)
    
    cdef void calculate_new_alpha(self):
        self.alpha = self.alpha0 * log10(self.genbest.f + 1)
    
    cdef void generation_process(self):
        self.movefireflies()
        self.evaluate()
        # adjust alpha, depend on fitness value
        # if fitness value is larger, then alpha should larger
        # if fitness value is small, then alpha should smaller
        self.genbest.assign(self.findFirefly())
        if self.bestFirefly.f > self.genbest.f:
            self.bestFirefly.assign(self.genbest)
        # self.bestFirefly.assign(gen_best)
        self.calculate_new_alpha()
        if self.rp != 0:
            if self.gen % self.rp == 0:
                self.report()
        else:
            if self.gen % 10 == 0:
                self.report()
        #progress
        if self.progress_fun is not None:
            self.progress_fun(self.gen, '%.4f'%self.bestFirefly.f)
    
    cpdef run(self):
        self.init()
        self.evaluate()
        self.bestFirefly.assign(self.fireflys[0])
        self.report()
        if self.maxGen>0:
            for self.gen in range(1, self.maxGen+1):
                self.generation_process()
                #interrupt
                if self.interrupt_fun is not None:
                    if self.interrupt_fun():
                        break
        else:
            while True:
                self.generation_process()
                self.gen += 1
                #interrupt
                if self.interrupt_fun is not None:
                    if self.interrupt_fun():
                        break
        self.report()
        return self.func.get_coordinates(self.bestFirefly.v), self.fitnessTime
