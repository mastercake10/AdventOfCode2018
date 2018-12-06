import time
from collections import Counter

file = open("input", "r")
values = [line.replace("\n", "") for line in file]

# excluding the year 1518 since it isn't relevant
values.sort(key=lambda x:time.mktime(time.strptime(x.split("]")[0].split("1518-")[1], '%m-%d %H:%M')))

cId = 0
peaces = {}
fallsAt = 0

for entry in values:
  curMinute = int(entry.split(":")[1].split("]")[0])
  if "Guard" in entry:
    cId = int(entry.split(" ")[3].replace("#", ""))
  elif "falls" in entry:
    fallsAt = curMinute
  elif "wakes" in entry:
    if cId in peaces:
      peaces[cId]["sleeptimes"].append([fallsAt, curMinute])
      peaces[cId]["total"] += curMinute - fallsAt
    else:
      peaces[cId] = {}
      peaces[cId]["sleeptimes"] = [[fallsAt, curMinute]]
      peaces[cId]["total"] = curMinute - fallsAt

idMax = max(peaces, key=lambda k: peaces[k]["total"])

# gets the most slept minute and the most overlaps
def getMaxSleepMinutes(guardId, peaces):
  minutes = []

  # some lazy intersection checkings
  for timeSpan in peaces[guardId]["sleeptimes"]:
    for i in range(timeSpan[0], timeSpan[1]):
      minutes.append(i)

  # get the actual intersecting minute
  counted = dict(Counter(minutes))
  minMaxAsleep = max(counted, key=lambda k: counted[k])
  return {"atMinute": minMaxAsleep, "overLaps": counted[minMaxAsleep]}

maxAsleep = getMaxSleepMinutes(idMax, peaces)
part1 = idMax * maxAsleep["atMinute"]

maxAsleepDict = {cId: getMaxSleepMinutes(cId, peaces) for cId in peaces}

guardMostSlept = max(maxAsleepDict, key=lambda k: maxAsleepDict[k]["overLaps"])

part2 = guardMostSlept * maxAsleepDict[guardMostSlept]["atMinute"]

print("part #1: %d\npart #2: %d" % (part1, part2))
  