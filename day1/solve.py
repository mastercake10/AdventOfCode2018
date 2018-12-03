file = open("input", "r")

values = map(int, [line.replace("\n", "") for line in file])
frequencies = set()

def solve(newFreq):
  for freq in values:
    newFreq += freq
    if newFreq in frequencies:
      return newFreq
    frequencies.add(newFreq)
  return solve(newFreq)

print("part #1: %d part #2: %d" % (sum(values), solve(0)))
