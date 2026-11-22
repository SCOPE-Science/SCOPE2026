#!/usr/bin/env python3
"""Exact independent verification of global Roman labelling enumerator on wheel graphs."""
from collections import Counter
from itertools import product, combinations
from math import comb

def add(P,Q,scalar=1):
  out=Counter(P)
  for k,v in Q.items():out[k]+=scalar*v
  return +out if all(z>=0 for z in out.values()) else {k:v for k,v in out.items() if v}
def term_fixed(n,k,base,free):
  # k denotes rim twos; base total weight on rim excluding hub.
  return {(base+j,k):comb(free,j) for j in range(free+1)}
def polygon_nbr(i,j,n):return (i-j)%n in (1,n-1)
def subsets(n):return list(combinations(range(n),2))
def roman_good(seq):
  n=len(seq)
  return all(seq[i]!=0 or seq[(i-1)%n]==2 or seq[(i+1)%n]==2 for i in range(n))
def global_good(seq,h):
  n=len(seq)
  return all(seq[i]!=0 or ((h==2 or seq[(i-1)%n]==2 or seq[(i+1)%n]==2) and any(seq[j]==2 and j!=i and not polygon_nbr(i,j,n) for j in range(n))) for i in range(n))
def direct(n):
  B=Counter();H1=Counter();H2=Counter()
  for seq in product(range(3),repeat=n):
    k=seq.count(2); w=sum(seq)
    if roman_good(seq): B[(w,k)]+=1
    if global_good(seq,1):H1[(w,k)]+=1
    if global_good(seq,2):H2[(w,k)]+=1
  return B,H1,H2

def formula(n,B):
  # Hub-1 starts as cycle Roman, corrected only for one and two twos.
  H1=Counter(B)
  H1=add(H1,term_fixed(n,1,n-1,2),-n)
  H1[(n+1,1)]+=n
  H2=Counter({(n,0):1})
  H2=add(H2,term_fixed(n,1,4, n-3),n)
  for i,j in subsets(n):
    S={i,j}
    qu=sum(1 for v in range(n) if v not in S and (polygon_nbr(v,i,n) or polygon_nbr(v,j,n)))
    qx=sum(1 for v in range(n) if v not in S and (polygon_nbr(v,i,n) != polygon_nbr(v,j,n)))
    H1=add(H1,term_fixed(n,2,4+n-2-qx,qx))
    H1=add(H1,term_fixed(n,2,4+n-2-qu,qu),-1)
    bad=sum(1 for v in range(n) if v not in S and polygon_nbr(v,i,n) and polygon_nbr(v,j,n))
    H2=add(H2,term_fixed(n,2,4+bad,n-2-bad))
  for k in range(3,n+1):H2=add(H2,term_fixed(n,k,2*k,n-k),comb(n,k))
  return H1,H2

def trace_coeff(n):
  states=list(product(range(3),repeat=2))
  total=Counter()
  for start in states:
    D={(start,0,0):1}
    for step in range(n):
      E=Counter()
      for ((a,b),w,k),v in D.items():
        for c in range(3):
          if b!=0 or a==2 or c==2:
            E[((b,c),w+b,k+(b==2))]+=v
      D=E
    for (state,w,k),v in D.items():
      if state==start:total[w,k]+=v
  return total

def trace_eval(n,x,y):
  V=list(product(range(3),repeat=2));idx={v:i for i,v in enumerate(V)}
  M=[[0]*9 for _ in V]
  for a,b in V:
    for c in range(3):
      if b!=0 or a==2 or c==2: M[idx[a,b]][idx[b,c]]+= x**b * (y if b==2 else 1)
  def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(9)) for j in range(9)] for i in range(9)]
  P=[[int(i==j) for j in range(9)] for i in range(9)]
  for _ in range(n):P=mul(P,M)
  return sum(P[i][i] for i in range(9))

def census(H1,H2):
  combined=Counter()
  for (w,k),c in H1.items():combined[w+1]+=c
  for (w,k),c in H2.items():combined[w+2]+=c
  low=min(combined)
  return low,combined[low]

def main():
 for n in range(3,10):
  B,A,C=direct(n);F1,F2=formula(n,trace_coeff(n))
  assert B==trace_coeff(n),(n,"transfer polynomial mismatch")
  assert A==F1,(n,'hub1',A-F1,F1-A)
  assert C==F2,(n,'hub2',C-F2,F2-C)
  for x,y in ((2,3),(3,2)):
   assert trace_eval(n,x,y)==sum(c*x**w*y**k for (w,k),c in B.items()),(n,'transfer')
  m,ct=census(A,C)
  expected={3:(4,1),4:(5,5),5:(6,21),6:(5,3),7:(6,28)}.get(n,(6,comb(n,2)))
  assert (m,ct)==expected,(n,m,ct,expected)
  print(f'n={n} FULL_WEIGHT_AND_TWO_COUNT_POLYNOMIAL_MATCH; TRANSFER_MATCH; optimum={m}; optimizers={ct}')
 print('ALL_EXACT_CHECKS_PASS')
if __name__=='__main__':main()
