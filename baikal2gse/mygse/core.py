# -*- coding: utf-8 -*-
"""
GSE2/GSE1 bindings
"""
from __future__ import division
import numpy as np


from mygse.obspycore.stream import Stream
from mygse.obspycore.trace import Trace
#from mygse.libgse2 import isGse2 as _isGse2
#from mygse.libgse2 import readHeader as _readHeader
#from mygse.libgse2 import read as _readGSE2
from mygse.libgse2 import write as _writeGSE2

'''
def isGSE2(filename):
    """
    Checks whether a file is GSE2 or not.
    """
    # Open file.
    try:
        with open(filename, 'rb') as f:
            _isGse2(f)
    except:
        return False
    return True

def readGSE2(filename, headonly=False, verify_chksum=True):
    """ Reads a GSE2 file and returns a Stream object """
    traces = []
    with open(filename, 'rb') as f:
        # reading multiple gse2 parts
        while True:
            try:
                if headonly:
                    header = _readHeader(f)
                    traces.append(Trace(header=header))
                else:
                    header, data = _readGSE2(f, verify_chksum=verify_chksum)
                    traces.append(Trace(header=header, data=data))
            except EOFError:
                break
    return Stream(traces=traces)
'''

def writeGSE2(stream, filename, inplace=False):
    """ Write GSE2 file from a Stream object """
    # Translate the common (renamed) entries
    with open(filename, 'wb') as f:
        # write multiple gse2 parts
        for trace in stream:
            dt = np.dtype(np.int32)
            if trace.data.dtype.name == dt.name:
                trace.data = np.ascontiguousarray(trace.data, dt)
            else:
                msg = "GSE2 data must be of type %s, but are of type %s" % \
                    (dt.name, trace.data.dtype)
                raise Exception(msg)
            _writeGSE2(trace.stats, trace.data, f, inplace)
