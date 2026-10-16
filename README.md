# Turbofan Engine Anomaly Detection and RUL Prediction on Databricks

> Learning project on public data: detect abnormal engine behaviour early and predict remaining useful life (RUL) using NASA C-MAPSS FD001, Databricks, Delta Lake and MLflow.

**Status:** in progress (replace with "v1.0 complete" when done)

## Results

<!-- TODO: fill in after Sprint 2. Report only numbers you produced. -->

| Model | Test RMSE (cycles) | NASA score |
|---|---|---|
| Ridge baseline | TODO | TODO |
| Gradient boosting (final) | TODO | TODO |

Median alert lead time before failure: TODO cycles

![Predicted vs actual RUL](reports/figures/pred_vs_actual.png)

## Problem

Unplanned engine failure is costly. Using run-to-failure sensor data, this project (1) flags engines whose behaviour drifts away from healthy operation and (2) predicts how many cycles remain before failure.

## Data

NASA C-MAPSS turbofan engine degradation simulation, subset FD001 (one operating condition, one fault mode). Download from the NASA Prognostics Data Repository and place the files as described in [`data/README.md`](data/README.md). Raw data is not stored in this repository.

Citation: Saxena, A., Goebel, K., Simon, D., & Eklund, N. (2008). Damage propagation modeling for aircraft engine run-to-failure simulation. *IEEE International Conference on Prognostics and Health Management.*

## Approach

1. **Bronze to gold pipeline on Delta Lake:** raw files, then cleaned data with RUL labels, then rolling-window features built in PySpark.
2. **Anomaly detection:** Isolation Forest fitted on early (healthy) cycles; anomaly score tracked per cycle; alert threshold taken from a percentile of healthy scores.
3. **RUL prediction:** ridge baseline versus gradient boosting; train and validation split by engine ID to avoid leakage; RUL capped at a fixed ceiling.
4. **Tracking and registry:** experiments logged with MLflow; best model registered and used for batch scoring.
5. **Evaluation:** official FD001 test set at each engine's last cycle; RMSE and the NASA asymmetric score.

## Repository layout

```
notebooks/   01_eda, 02_anomaly_detection, 03_rul_model
src/         data.py, features.py, evaluate.py
data/        download instructions only
reports/     figures used in this README
```

## How to run

1. Clone the repository and add it as a Git folder in Databricks (or run locally with `pip install -r requirements.txt`).
2. Download the FD001 files as described in `data/README.md`.
3. Run the notebooks in order: `01_eda`, `02_anomaly_detection`, `03_rul_model`.

Random seeds are set in each notebook so results can be reproduced.

## Limitations and next steps

- Only FD001 is used; FD002 to FD004 (multiple operating conditions and fault modes) are future work.
- Simulated data; results do not transfer directly to real engines.
- Next: SHAP explanations, then a retrieval-based assistant over maintenance documents (separate project).

## Licence

MIT, see [LICENSE](LICENSE).

## Author

Nikhil D Jonathan
