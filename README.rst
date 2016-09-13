mpas\_xarray.py
===============

Wrapper to handle importing MPAS files into xarray
(https://github.com/pydata/xarray).  Module can be installed via

::

    pip -v install git+ssh://git@github.com/pwolfram/mpas_xarray

The module does the following:

1. Converts MPAS "xtime" to xarray time. Time dimension is
   assigned via ``preprocess_mpas``.
2. Converts MPAS "timeSinceStartOfSim"
   to xarray time for MPAS fields coming from the timeSeriesStatsAM. Time
   dimension is assigned via ``preprocess_mpas(...,timeSeriesStats=True)``.
3. Allows generalized selection of variables via ``preprocess_mpas(..., onlyvars=['var1','var2'])``
   and slicing via ``preprocess_mpas(..., iselvals={'nVertLevels':1})`` and
   ``preprocess_mpas(..., selvals={'lonCell':180.0})``.
4. Provides capability to remove redundant time entries from reading of
   multiple netCDF datasets via ``remove_repeated_time_index``.

Example Usage:

::

    import xarray
    from mpas_xarray import preprocess_mpas, remove_repeated_time_index

    ds = xarray.open_mfdataset('globalStats*nc', preprocess=preprocess_mpas)
    ds = remove_repeated_time_index(ds)

To test:

::

    tar xzvf globalStatsShort.tgz
    python mpas_xarray.py -f "globalStats*nc"

This outputs a simple time-series plot of Time vs. Time to test
functionality.

Example Usage for timeSeriesStatsAM fields:

::

    import xarray
    from mpas_xarray import preprocess_mpas, remove_repeated_time_index

    def preprocess(x, timestr='timeSeriesStatsMonthly_avg_daysSinceStartOfSim_1'):
      return preprocess_mpas(x, timeSeriesStats=True, timestr=timestr)

    ds = xarray.open_mfdataset('am.mpas-cice*nc', preprocess=preprocess)
    ds = remove_repeated_time_index(ds)

To test:

::

    tar xzvf am.mpas-ciceShort.tgz
    python mpas_xarray.py -f "am.mpas-cice*nc" --istimeavg "true"

This plots a short time series of global average ice concentration,
showing the correctly centered curve (derived using
preprocess\_mpas\_timeSeriesStats) and the curve incorrectly shifted
toward the end of the time averaging period (derived using
preprocess\_mpas).
