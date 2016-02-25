#!/usr/bin/env python
"""
mpas_xarray.py
==============================================================
Wrapper to handle importing MPAS files into xarray.

 Module does
 1. Converts MPAS "xtime" to xarray-understood time dimension via
    'preprocess_mpas'.
 2. Provides capability to remove redundant time entries from
    reading of multiple netCDF datasets via
    'remove_repeated_time_index'.

 Example Usage:

>>> from mpas_xarray import preprocess_mpas, remove_repeated_time_index
>>>
>>> ds = xarray.open_mfdataset('globalStats*nc', preprocess=preprocess_mpas)
>>> ds = remove_repeated_time_index(ds)

Phillip J. Wolfram
12/01/2015
"""

import matplotlib.pyplot as plt
import numpy as np
import datetime
import pandas as pd
import xarray as xr

def preprocess_mpas(ds, yearoffset=1700): #{{{
    """
    Builds corret time specification for MPAS, allowing a year offset because the
    time must be betwee 1678 and 2262 based on the xarray library.

    Phillip J. Wolfram
    12/01/2015
    """

    time = np.array([''.join(atime).strip() for atime in ds.xtime.values])
    datetimes = [datetime.datetime(yearoffset + int(x[:4]), int(x[5:7]), \
            int(x[8:10]), int(x[11:13]), int(x[14:16]), int(x[17:19])) for x in time]
    # make sure  date times are set up properly
    assert datetimes[0].year > 1678, 'ERROR: yearoffset=%s'%(yearoffset) + \
            ' must be large enough to ensure datetimes larger than year 1678'
    assert datetimes[-1].year < 2262, 'ERROR: yearoffset=%s'%(yearoffset) + \
            ' must be large enough to ensure datetimes larger than year 2262'

    # append the corret time information
    ds.coords['Time'] = pd.to_datetime(datetimes)

    # record the yroffset
    ds.attrs.__setitem__('time_yearoffset',str(yearoffset))

    return ds #}}}

def remove_repeated_time_index(ds): #{{{
    """
    Remove repeated times from xarray dataset.

    Phillip J. Wolfram
    12/01/2015
    """
    # get repeated indices
    time = ds.Time.values
    index = range(len(time))
    uniquetime = set()
    remove = []
    for id, atime in enumerate(time):
        if atime not in uniquetime:
            uniquetime.add(atime)
        else:
            remove.append(id)

    remove.reverse()
    for id in remove:
        index.pop(id)

    # remove repeated indices
    ds = ds.isel(Time=index)

    return ds #}}}

def test_load_mpas_xarray_datasets(path):
    ds = xr.open_mfdataset(path, preprocess=preprocess_mpas)
    ds = remove_repeated_time_index(ds)

    # make a simple plot from the data
    ds.Time.plot()
    plt.show()

    return


if __name__=="__main__":
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-f", "--file", dest="inputfilename", help="files to be opened with xarray, could be of form 'output*.nc'", metavar="FILE")

    options, args = parser.parse_args()
    if not options.inputfilename:
        parser.error("Input filename or expression ('-f') is a required input... e.g., -f 'output*.npz'")

    test_load_mpas_xarray_datasets(options.inputfilename)

