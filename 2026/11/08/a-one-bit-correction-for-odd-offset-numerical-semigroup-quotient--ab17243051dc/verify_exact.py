"""Standalone exact-integer verification of odd-offset quotient Frobenius formula."""
from math import gcd
from heapq import heappush,heappop

def coin_cost(x,q):
    if x==0:return 0
    s,t=divmod(x-1,q)
    return s+1+(t%2)

def formula(a,p,h,d,q):
    m=a//p; assert m>=2 and a%p==0 and 3<=q<a and q%2
    s,t=divmod(a-p-1,q);t+=1
    terminal=h*m*(s+1+(t%2==0))+d*(m-1)-m
    correction=max(0,h*m-d) if (p%2 and t%2 and t>p) else 0
    return terminal+correction

def direct(a,p,h,d,q):
    gens=[h*a+d*j for j in range(1,q+1,2)]
    dist=[10**30]*a;dist[0]=0;todo=[(0,0)]
    while todo:
        cost,r=heappop(todo)
        if cost!=dist[r]:continue
        for g in gens:
            nr=(r+g)%a;nc=cost+g
            if nc<dist[nr]:dist[nr]=nc;heappush(todo,(nc,nr))
    return max(dist[r]//p for r in range(0,a,p))-a//p

if __name__=='__main__':
    cases=0; odd_gap=0; corrections=0; even_gap=0; samples=[]
    for a in range(4,145):
      for p in range(1,a):
       if a%p or a//p<2:continue
       for q in range(3,a,2):
        for h in (1,2,3):
         for d in (1,2,3):
          if gcd(a,d)!=1:continue
          x=formula(a,p,h,d,q);y=direct(a,p,h,d,q)
          if x!=y:raise AssertionError((a,p,h,d,q,x,y))
          cases+=1
          t=(a-p-1)%q+1
          if t%2:
           odd_gap+=1
           if p%2 and t>p and h*(a//p)>d:
            corrections+=1
            if len(samples)<12:samples.append((a,p,h,d,q,x))
          else:even_gap+=1
    print('PASS:',cases,'parameter tuples;',odd_gap,'odd remainders;',even_gap,'even remainders;',corrections,'nonzero corrections')
    print('Sample correction cases:',samples)
