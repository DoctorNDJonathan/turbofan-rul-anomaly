"""Data helpers for the C-MAPSS FD001 turbofan dataset."""

import pandas as pd

INDEX_COLS = ["unit", "cycle"]
SETTING_COLS = [f"setting_{i}" for i in range(1, 4)]
SENSOR_COLS = [f"s_{i}" for i in range(1, 22)]
ALL_COLS = INDEX_COLS + SETTING_COLS + SENSOR_COLS  # 26 columns

RUL_CAP = 125  # common ceiling in the literature; kept as a parameter


def load_cmapss(path: str) -> pd.DataFrame:
    """Read a space-separated C-MAPSS file and name its 26 columns."""
    df = pd.read_csv(path, sep=r"\s+", header=None, engine="python")
    df = df.iloc[:, : len(ALL_COLS)]  # drop empty trailing columns if present
    df.columns = ALL_COLS
    return df


def add_rul(df: pd.DataFrame, cap: int = RUL_CAP) -> pd.DataFrame:
    """Add RUL = (last cycle of the engine) - (current cycle), capped at `cap`."""
    out = df.copy()
    last_cycle = out.groupby("unit")["cycle"].transform("max")
    out["rul"] = (last_cycle - out["cycle"]).clip(upper=cap)
    return out


def near_constant_sensors(df: pd.DataFrame, tol: float = 1e-6) -> list:
    """Return sensor/setting columns whose standard deviation is (almost) zero."""
    cols = SETTING_COLS + SENSOR_COLS
    stds = df[cols].std()
    return stds[stds <= tol].index.tolist()
