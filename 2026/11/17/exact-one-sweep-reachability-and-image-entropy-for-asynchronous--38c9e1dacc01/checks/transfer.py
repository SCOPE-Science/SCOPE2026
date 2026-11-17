#!/usr/bin/env python3
# Reproduce the four-state cyclic-word transfer and the rational count.
from fractions import Fraction
states=((0,0),(0,1),(1,0),(1,1))
T=[[0]*4 for _ in range(4)]
for i,(a,b) in enumerate(states):
  for c in (0,1):
    if (a,b,c)!=(1,0,1):T[i][states.index((b,c))]+=1

def mul(A,B):
  return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
I=[[int(i==j) for j in range(4)] for i in range(4)]
powers=[I]
for n in range(1,40):powers.append(mul(powers[-1],T))
counts=[0,2,2]
for n in range(3,35):
  A=sum(powers[n][i][i] for i in range(4))
  B=powers[n][2][2]
  C=powers[n-2][1][2]
  counts.append(A-B-C)
assert counts[3:13]==[3,7,13,22,38,67,118,207,363,637]
for n in range(5,35):assert counts[n]==2*counts[n-1]-counts[n-2]+counts[n-3]
print('transfer_states',states)
print('T',T)
print('count n=3..20',counts[3:21])
print('PASS: transfer identity and third-order recurrence through n=34')
