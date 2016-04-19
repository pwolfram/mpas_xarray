mpas_xarray.py
===============================================================================
Wrapper to handle importing MPAS files into xarray (https://github.com/pydata/xarray)

 Module does
 1. Converts MPAS "xtime" to xarray time.  Time dimension is assigned via
    `preprocess_mpas`.
 2. Converts MPAS "timeSinceStartOfSim" to xarray time optionally for MPAS fields coming from the
    timeSeriesStatsAM.  Time dimension is assigned via 
    `preprocess_mpas_timeSeriesStats`.
 3. Provides capability to remove redundant time entries from
    reading of multiple netCDF datasets via
    `remove_repeated_time_index`.

 Example Usage:

```
from mpas_xarray import preprocess_mpas, remove_repeated_time_index

ds = xarray.open_mfdataset('globalStats*nc', preprocess=preprocess_mpas)
ds = remove_repeated_time_index(ds)
```

To test:

```
tar xzvf globalStatsShort.tgz
python mpas_xarray.py -f "globalStats*nc"
```

This outputs a simple time-series plot of Time vs. Time to test functionality.

 Example Usage for timeSeriesStatsAM fields:

```
from mpas_xarray import preprocess_mpas_timeSeriesStats, remove_repeated_time_index

ds = xarray.open_mfdataset('am.mpas-cice*nc', preprocess=preprocess_mpas_timeSeriesStats)
ds = remove_repeated_time_index(ds)
```

To test:

```
tar xzvf am.mpas-ciceShort.tgz
python mpas_xarray.py -f "am.mpas-cice*nc" --istimeavg "true"
```

This plots a short time series of global average ice concentration, showing the correctly centered curve
(derived using preprocess_mpas_timeSeriesStats) and the curve incorrectly shifted toward the end of the 
time averaging period (derived using preprocess_mpas).

