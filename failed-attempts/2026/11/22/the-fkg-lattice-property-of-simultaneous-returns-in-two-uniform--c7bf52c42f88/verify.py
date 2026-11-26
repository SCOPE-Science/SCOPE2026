#!/usr/bin/env python3
"""Standalone exact checker for the common-return FKG property of pairs of Dyck paths."""
from math import comb
from collections import Counter

def cat(n):return comb(2*n,n)//(n+1)

def paths(n):
 def rec(s,up,down,height,returns):
  if up==down==n:
   yield frozenset(returns)
   return
  if up<n:yield from rec(s+'U',up+1,down,height+1,returns)
  if down<up:
   new=returns+([down+1] if height==1 and down+1<n else [])
   yield from rec(s+'D',up,down+1,height-1,new)
 return list(rec('',0,0,0,[]))

def block(n):
 a=[cat(i)**2 for i in range(n+1)]; b=[0]*(n+1)
 for i in range(1,n+1):b[i]=a[i]-sum(b[j]*a[i-j] for j in range(1,i))
 return a,b

def test():
 assertions=0
 for n in range(2,9):
  a,b=block(n)
  assert all(b[i]>0 for i in range(1,n+1)); assertions+=n
  for i in range(2,n):
   assert b[i-1]*b[i+1]>b[i]**2,(n,i)
   assertions+=1
  pw=paths(n); cnt=Counter(frozenset(x & y) for x in pw for y in pw)
  assert sum(cnt.values())==cat(n)**2; assertions+=1
  for mask in range(1<<(n-1)):
   S=frozenset(i for i in range(1,n) if mask>>(i-1)&1)
   gaps=[0,*sorted(S),n]
   w=1
   for u,v in zip(gaps,gaps[1:]):w*=b[v-u]
   assert cnt[S]==w,(n,S,cnt[S],w)
   assertions+=1
   for i in range(1,n):
    if i in S:continue
    for j in range(i+1,n):
     if j in S:continue
     Si=S|{i};Sj=S|{j};Sij=Si|{j}
     assert cnt[Sij]*cnt[S]>=cnt[Si]*cnt[Sj],(n,S,i,j)
     assertions+=1
  print('semilength',n,'paths',len(pw),'pairs',len(pw)**2,'all exact weights & lattice inequalities verified')
 print('PASS',assertions,'exact assertions')
if __name__=='__main__':test()
