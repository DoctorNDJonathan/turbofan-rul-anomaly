"""Rolling-window feature helpers (pandas version; the Databricks notebook uses PySpark windows)."""

import pandas as pd


def add_rolling_features(df: pd.DataFrame, sensor_cols, windows=(5, 15, 30)) -> pd.DataFrame:
    """Add rolling mean and std per engine using only current and past rows.

    `rolling(...)` looks backwards, so no future rows are used (no leakage).
    """
    out = df.sort_values(["unit", "cycle"]).copy()
    grouped = out.groupby("unit")
    for w in windows:
        for col in sensor_cols:
            out[f"{col}_mean_{w}"] = grouped[col].transform(lambda s: s.rolling(w, min_periods=1).mean())
            out[f"{col}_std_{w}"] = grouped[col].transform(lambda s: s.rolling(w, min_periods=2).std()).fillna(0.0)
    return out
