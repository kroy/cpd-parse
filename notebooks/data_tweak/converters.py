from collections.abc import Callable
import pandas as pd
from data_tweak.normalizers import normalize_race, normalize_sex

def convert_datetime(df: pd.DataFrame, datetime_col: str = "date_time") -> None:
  df[datetime_col] = pd.to_datetime(df[datetime_col])

def convert_race(df: pd.DataFrame, race_cols: list[str]) -> None:
  convert_cols(df, race_cols, normalize_race)

def convert_sex(df: pd.DataFrame, sex_cols: list[str]) -> None:
  convert_cols(df, sex_cols, normalize_sex)

def convert_cols(df: pd.DataFrame, cols: list[str], converter: Callable[[str], str]) -> None:
  for col in cols:
    df[col] = df[col].transform(converter)
  # df[[*cols]] = df[[*cols]].transform(converter)
