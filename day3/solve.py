from collections import Counter
from itertools import combinations
import re


file = open("input", "r")
values = [line.replace("\n", "") for line in file]

fields, claims = [], []

for value in values:
  id, x, y, dimx, dimy = map(int, re.split(r"[#,@:x]", value.replace(" ", ""))[1:])
  claims.append({"x": x, "y": y, "width": dimx, "height": dimy, "id": id, "laps": 0})

  for cx in range(0, dimx):
    for cy in range(0, dimy):
      fields.append(str(cx + x) + "." + str(cy + y))

# counting occurrences of duplicates
part1 = len([k for k, v in Counter(dict(Counter(fields))).iteritems() if v > 1])

def overlap(r1, r2):
  return not (r1["x"] + r1["width"] < r2["x"] or r1["y"] + r1["height"] < r2["y"] or r1["x"] > r2["x"] + r2["width"] or r1["y"] > r2["y"] + r2["height"])

# finding overlaps
for comb in combinations(claims, 2):
  if overlap(comb[0], comb[1]):
    comb[0]["laps"] += 1
    comb[1]["laps"] += 1

part2 = sorted(claims, key=lambda k: k["laps"])[0]["id"]

print("part #1: %d\npart #2: %d" % (part1, part2))