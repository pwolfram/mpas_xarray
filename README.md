mpas_xarray.py
===============================================================================
Wrapper to handle importing MPAS files into xarray (https://github.com/pydata/xarray)

 Module does
 1. Converts MPAS "xtime" to xarray time dimension is assigned via
    `preprocess_mpas`.
 2. Provides capability to remove redundant time entries from
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

