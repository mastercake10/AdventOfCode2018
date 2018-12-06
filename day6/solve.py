import operator
from collections import Counter

file = open("input", "r")

values = [line.replace("\n", "") for line in file]

arr = {}
startingP = []

i = ord('A')
for line in values:
  arr[chr(i)] = list(map(int, line.split(", ")))
  startingP.append(map(int, line.split(", ")))
  i += 1

def dist(x1, x2, y1, y2):
  return abs(x1 - x2) + abs(y1 - y2)

xmax = arr[max(arr.keys(), key=(lambda k: arr[k][0]))][0]
ymax = arr[max(arr.keys(), key=(lambda k: arr[k][1]))][1]

infAreas = set()
areas = {}
for x in range(xmax):
  for y in range(ymax):
    dists = {}
    for pkey in arr:
      if [x, y] not in startingP:
        distance = dist(x, arr[pkey][0], y, arr[pkey][1])
        if distance == 0:
          continue
        dists[pkey] = distance 
      else:
        continue
    if dists:
      idClosest = min(dists, key=lambda k: dists[k])
      closestDist = dists[idClosest]
      found = False
      dup = False
      for id in dists:
        if closestDist == dists[id]:
          if found:
            dup = True
          found = True
      if not dup:
        if idClosest not in areas:
          areas[idClosest] = 2
        else:
          areas[idClosest] += 1
        if x == 0 or y == 0 or x == xmax or y == ymax:
          infAreas.add(idClosest)
          
for key in arr:
  p = arr[key]
  if p[0] == 0 or p[1] == 0 or p[0] == xmax or p[1] == ymax:
    infAreas.add(key)
print(areas)
print(infAreas)

for key in infAreas:
  del areas[key]

ar = 0
for x in range(xmax):
  for y in range(ymax):
    total = 0
    for pkey in arr:
      total += dist(x, arr[pkey][0], y, arr[pkey][1])
    if total < 10000:
      ar += 1
print(ar)

print(areas[max(areas, key=lambda k: areas[k])])