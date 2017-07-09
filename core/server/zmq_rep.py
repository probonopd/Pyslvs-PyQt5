# -*- coding: utf-8 -*-

def startRep(PORT):
    import os, timeit
    import zmq
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.connect(PORT) #tcp://localhost:8000
    print(PORT)
    print("Worker {} is awaiting orders...".format(os.getpid()))
    while True:
        type_num, mechanismParams, GenerateData, algorithmPrams = socket.recv_multipart()
        t0 = timeit.default_timer()
        t1 = timeit.default_timer()
        print('total cost time: {:.4f} [s]'.format(t1-t0))
        socket.send()
