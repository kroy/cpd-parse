import pandas as pd

def slice_by_date(df: pd.DataFrame, start: str, end: str, date_time_col: str = "date_time") -> pd.DataFrame:
  df.set_index(date_time_col).loc[pd.date_range(start=start, end=end)]