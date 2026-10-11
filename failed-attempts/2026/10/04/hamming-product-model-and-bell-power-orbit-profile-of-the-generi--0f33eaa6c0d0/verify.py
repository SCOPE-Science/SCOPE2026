#!/usr/bin/env python3
import itertools
def bell(N):
 S=[[0]*(N+1) for _ in range(N+1)]; S[0][0]=1
 for n in range(1,N+1):
  for k in range(1,n+1): S[n][k]=S[n-1][k-1]+k*S[n-1][k]
 return [sum(S[n]) for n in range(N+1)],S
def stir1(N):
 s=[[0]*(N+1) for _ in range(N+1)]; s[0][0]=1
 for n in range(1,N+1):
  for k in range(1,n+1): s[n][k]=s[n-1][k-1]-(n-1)*s[n-1][k]
 return s
def parts(n):
 def rec(a,m):
  if len(a)==n: yield tuple(a); return
  for v in range(m+2):
   a.append(v); yield from rec(a,max(m,v)); a.pop()
 if n: yield from rec([0],0)
 else: yield ()
def discrete(ps):
 sig=[tuple(p[j] for p in ps) for j in range(len(ps[0]))]
 return len(sig)==len(set(sig))
N=10; B,S=bell(N); s=stir1(N)
A={}
for d in (1,2,3,4):
 A[d]=[0]+[sum(s[n][k]*B[k]**d for k in range(1,n+1)) for n in range(1,N+1)]
 for n in range(1,N+1): assert B[n]**d==sum(S[n][k]*A[d][k] for k in range(1,n+1))
for d in (1,2,3):
 for n in range(1,6):
  P=list(parts(n)); brute=sum(discrete(ps) for ps in itertools.product(P,repeat=d))
  assert brute==A[d][n],(d,n,brute,A[d][n])
exp=[1,3,15,113,1153,15125,245829,4815403]
assert A[2][1:9]==exp
print('d=2 injective:',A[2][1:9]); print('d=2 all:',[B[n]**2 for n in range(1,9)])
print('d=3 injective:',A[3][1:9]); print('VERIFY_OK')
