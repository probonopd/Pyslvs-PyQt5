# -*- coding: utf-8 -*-
##Pyslvs - Open Source Planar Linkage Mechanism Simulation and Dimensional Synthesis System.
##Copyright (C) 2016-2017 Yuan Chang
##E-mail: pyslvs@gmail.com
##
##This program is free software; you can redistribute it and/or modify
##it under the terms of the GNU Affero General Public License as published by
##the Free Software Foundation; either version 3 of the License, or
##(at your option) any later version.
##
##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Affero General Public License for more details.
##
##You should have received a copy of the GNU Affero General Public License
##along with this program; if not, write to the Free Software
##Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

from ...libs.pyslvs_topologic.topologic import topo
from networkx import (
    triangles,
    is_connected,
    is_isomorphic
)

class TestError(Exception):
    pass

def testT(G, degenerate):
    if degenerate:
        if not all(n==0 for n in triangles(G).values()):
            raise TestError("has triangle")

def testG(G, answer):
    if not is_connected(G):
        raise TestError("is not connected")
    for G_ in answer:
        if is_isomorphic(G, G_):
            raise TestError("is isomorphic")
