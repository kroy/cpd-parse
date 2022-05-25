def normalize_sex(sex: str) -> str:
  if (sex == "M" or sex == "MALE"):
    return "MALE"
  elif (sex == "F" or sex == "FEMALE"):
    return "FEMALE"
  else:
    return "NA"

def normalize_race(race: str) -> str:
  if race in ["WHITE", "BLACK", "HISPANIC", "ASIAN/PACIFIC ISLANDER", "NATIVE AMERICAN/ALASKAN NATIVE"]:
    return race
  elif race == "WHITE HISPANIC":
    return "HISPANIC"
  elif race in ["AMER IND/ALASKAN NATIVE", "NATIVE AMERICAN"]:
    return "NATIVE AMERICAN/ALASKAN NATIVE"
  else:
    return race