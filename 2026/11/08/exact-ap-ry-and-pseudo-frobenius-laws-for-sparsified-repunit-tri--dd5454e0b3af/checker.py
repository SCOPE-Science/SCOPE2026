#!/usr/bin/env python3
"""Exact integer verification for sparse repunit triple theorem.
No scientific result depends on finite checks: this tests worked cases only.
"""
import heapq

def rep(b,n): return (b**n-1)//(b-1)

def expected(b,n):
 assert b>=2 and n>=3 and n%2
 a=rep(b,n);u=b**n*(b+1); m=1+b*b+b**4
 k,r=divmod(a,m)
 assert r== {1:1,3:1+b+b*b,5:b**3+b}[n%6]
 c=lambda t: t//m+t%m
 L=a-1 if n%6 !=1 else a-2
 if n==3: L=a-1
 W=lambda t:a*c(t)+u*t
 F=W(L)-a
 C=k*m*(k+m-2)//2 +r*k+r*(r-1)//2
 genus=C+(u-1)*(a-1)//2
 T=[a-1] if n==3 else [a-1,k*m-1]
 PF=sorted({W(t)-a for t in T})
 assert len(PF)==(1 if n==3 else 2)
 return a,u,m,F,genus,PF,W

def dijkstra(a,gens):
 d=[None]*a;d[0]=0
 q=[(0,0)]
 while q:
  val,j=heapq.heappop(q)
  if d[j]!=val:continue
  for g in gens:
   jj=(j+g)%a; vv=val+g
   if d[jj] is None or vv<d[jj]:
    d[jj]=vv;heapq.heappush(q,(vv,jj))
 return d

def check(b,n):
 a,u,m,F,g,PF,W=expected(b,n)
 gens=[a,rep(b,n+2),rep(b,n+6)]
 assert gens == [a,a+u,a+m*u]
 d=dijkstra(a,gens)
 assert sorted(d)==sorted(W(t) for t in range(a)), (b,n,'apery mismatch')
 assert max(d)-a==F
 assert (sum(d)-a*(a-1)//2)//a==g
 S=lambda value:(value>=0 and value>=d[value%a])
 found=sorted(z-a for z in d if all(S(z+h-a) for h in gens) and z>=a)
 assert found==PF,(b,n,found,PF)
 assert (2*g==F+1)==(n==3)
 return f'b={b} n={n} a={a} F={F} genus={g} type={len(PF)} PF={PF}'

if __name__=='__main__':
 for b,nmax in [(2,15),(3,11),(4,9),(5,7)]:
  for n in range(3,nmax+1,2):
   print(check(b,n))
 print('ALL CHECKS PASSED')
