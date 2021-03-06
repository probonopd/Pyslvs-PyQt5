# -*- coding: utf-8 -*-
##Pyslvs - Open Source Planar Linkage Mechanism Simulation and Mechanical Synthesis System. 
##Copyright (C) 2016-2018 Yuan Chang [pyslvs@gmail.com]

"""
"info" module contains Pyslvs program informations.
"""

from .info import (
    INFO,
    ARGUMENTS,
    VERSION,
    check_update
)
from .about import (
    Pyslvs_Splash,
    Pyslvs_About,
    html
)

__all__ = [
    'INFO',
    'ARGUMENTS',
    'VERSION',
    'check_update',
    'Pyslvs_Splash',
    'Pyslvs_About',
    'html'
]
