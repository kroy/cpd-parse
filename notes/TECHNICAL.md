Technique for slicing a date range using string bounds:

```
df.loc["2012-01-01T00:01:00Z":"2012-01-01T00:05:00Z"]
```

Maybe use a list comprehension and concatenate dataframes when processing big files
eg from https://pandas.pydata.org/docs/user_guide/merging.html#concatenating-objects

Note

It is worth noting that concat() (and therefore append()) makes a full copy of the data, and that constantly reusing this function can create a significant performance hit. If you need to use the operation over several datasets, use a list comprehension.

frames = [ process_your_file(f) for f in files ]
result = pd.concat(frames)


