file = open("input", "r")

values = list(map(lambda line: line.replace("\n", ""), file.readlines()))
frequencies = [0]

def solve():
  for freq in values:
    newFreq = frequencies[-1] + (int(freq[1:]) if freq.startswith("+") else -int(freq[1:]))
    if newFreq in frequencies:
      return frequencies[len(values)], newFreq
    frequencies.append(newFreq)
  return solve()

print("Solutions: ", solve())