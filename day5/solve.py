#!/usr/bin/env python2

file = open("input", "r")
polymer = map(ord, file.readline())

def react(polymer):
  newPolymer = []
  for e in polymer:
    if len(newPolymer) > 0 and abs(newPolymer[-1] - e) == 32:
      newPolymer.pop()
    else:
      newPolymer.append(e)
  return newPolymer

polymerLenghts = [len(react(list(filter(lambda a: a != i and a != i + 32, polymer)))) for i in range(ord('A'), ord('Z') + 1)]

print("part #1: %d\npart #2: %d" % (len(react(polymer)), min(polymerLenghts)))
  