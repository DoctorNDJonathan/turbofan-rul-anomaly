# Data

Raw data is not stored in this repository.

## Source

NASA Prognostics Data Repository, "Turbofan Engine Degradation Simulation Data Set" (C-MAPSS):
https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/

## Files used (subset FD001)

- `train_FD001.txt`: run-to-failure sensor data for 100 training engines
- `test_FD001.txt`: sensor data for 100 test engines, stopped before failure
- `RUL_FD001.txt`: true remaining useful life at the last cycle of each test engine

## Columns (26, space-separated, no header)

`unit`, `cycle`, `setting_1`, `setting_2`, `setting_3`, then `s_1` to `s_21` (sensor readings).

## Where to put them

- Local run: copy the three files into this `data/` folder.
- Databricks: upload them to a Unity Catalog volume and load them as Delta tables (bronze layer).

###FILE = "/Volumes/turbofan/cmapss/raw"

Citation for data:
A. Saxena and K. Goebel (2008). “Turbofan Engine Degradation Simulation Data Set”, NASA Prognostics Data Repository, NASA Ames Research Center, Moffett Field, CA.
