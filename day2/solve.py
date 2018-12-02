import itertools
import collections

file = open("input", "r")

values = [line.replace("\n", "") for line in file]

# part 1
cnts = []
for word in values:
  cnts.extend(set(word.count(i) for i in word))

# part 2
# since we're working with ascii, we can simply use the Hamming distance!
def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

dists = {hamming_distance(boxes[0], boxes[1]):boxes for boxes in itertools.combinations(values , 2)}

print("part #1: %d\npart #2: %s" % (cnts.count(2) * cnts.count(3), dists[1][0].replace(list(set(dists[1][0]) - set(dists[1][1]))[0], "")))