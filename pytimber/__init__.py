# -*- coding: utf-8 -*-

from .pytimber import LoggingDB
from .dataquery import (DataQuery, parsedate, dumpdate,
                        flattenoverlap, set_xaxis_date,
                        set_xaxis_utctime, set_xlim_date, get_xlim_date)
from . import timberdata

__version__ = "2.2.5"

cmmnbuild_deps = [
    "accsoft-cals-extr-client",
    "accsoft-cals-extr-domain",
    "slf4j-log4j12",
    "slf4j-api",
    "log4j"
]
