import math

def calculateStats(numbers):
  computedStats = {}
  
  if(numbers==[]):
    computedStats["min"] = float("nan")
    computedStats["max"] = float("nan")
    computedStats["avg"] = float("nan")
  else:
    computedStats["min"] = min(numbers)
    computedStats["max"] = max(numbers)
    computedStats["avg"] = (sum(numbers)/len(numbers))    
  
  return computedStats
