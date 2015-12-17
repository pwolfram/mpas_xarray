mpas_xray.py                                                                                   
==============================================================
Wrapper to handle importing MPAS files into xray.

 Module does
 1. Converts MPAS "xtime" to xray-understood time dimension via
    `preprocess_mpas`.
 2. Provides capability to remove redundant time entries from
    reading of multiple netCDF datasets via 
    `remove_repeated_time_index`.
    
 Example Usage:

``` 
from mpas_xray import preprocess_mpas, remove_repeated_time_index

ds = xray.open_mfdataset('globalStats*nc', preprocess=preprocess_mpas)
ds = remove_repeated_time_index(ds)
```

To test:

```
tar xzvf globalStatsShort.tgz
python mpas_xray.py -f "globalStats*nc"
```

This outputs a simple time-series plot of Time vs. Time to test functionality.

