from numpy import sign
import pandas as pd

def matches(df: pd.DataFrame, signifier: str | list[str], merged_on: list[str] = []) -> pd.DataFrame:
  matches = df[df[signifier].notna()]
  print("Based on the join key [" + ", ".join(merged_on) + "]:")
  print("\tNumber of matches:", matches.shape[0])
  return matches

def unmatched(df: pd.DataFrame, signifier: str | list[str], merged_on: list[str] = []) -> pd.DataFrame:
  if type("signifier") is str: signifier = [signifier]
  unmatched = df[df[signifier].isna().any(axis=1)]
  print("Based on the join key [" + ", ".join(merged_on) + "]:")
  print("\tNumber of unmatched records:", unmatched.shape[0])
  return unmatched

def dupes(df: pd.DataFrame, signifier: str | list[str], merged_on: list[str] = []) -> pd.DataFrame:
  grouped = df.groupby(by=signifier, dropna=False).size().sort_values(ascending=False).to_frame("size")
  dupes = grouped[grouped["size"] > 1]
  print("Based on the join key [" + ", ".join(merged_on) + "]:")
  print("\tNumber of records with more than one match:", dupes.shape[0])
  return dupes
