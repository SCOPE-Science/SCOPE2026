#!/usr/bin/env python3
"""Finite-field recurrence tests for sparse-cylinder trace dimensions."""
from math import comb,gcd

def rank_modp(a,p):
    if not a:return 0
    a=[r[:] for r in a];rows=len(a); cols=len(a[0]); piv=0
    for j in range(cols):
        z=next((i for i in range(piv,rows) if a[i][j]%p),None)
        if z is None:continue
        a[piv],a[z]=a[z],a[piv]; inv=pow(a[piv][j],-1,p)
        a[piv]=[(v*inv)%p for v in a[piv]]
        for i in range(rows):
            if i!=piv and a[i][j]%p:
                t=a[i][j]
                a[i]=[(v-t*w)%p for v,w in zip(a[i],a[piv])]
        piv+=1
        if piv==rows:break
    return piv

def measured_rank(p,k,N,m,t,a,b):
    # Solve (a+b Shift)^t f=0 on each residue class modulo k
    c=[comb(t,j)*pow(a,t-j,p)*pow(b,j,p)%p for j in range(t+1)]
    inv=pow(c[-1],-1,p)
    sites=[j*N for j in range(m)]
    basis=[]
    for r in range(k):
        js=[(site-r)//k if site%k==r else None for site in sites]
        horizon=max((j for j in js if j is not None),default=-1)
        if horizon<0:continue
        for seed in range(t):
            vals=[int(j==seed) for j in range(t)]
            while len(vals)<=horizon:
                next_val=-inv*sum(c[j]*vals[len(vals)-t+j] for j in range(t))
                vals.append(next_val%p)
            basis.append([vals[j] if j is not None else 0 for j in js])
    return rank_modp(basis,p)

def predicted(p,k,N,m,t):
    g=gcd(k,N);R=k//g;h=N//g;v=1
    while h%p==0:v*=p;h//=p
    q=(t+v-1)//v
    sizes=[max(0,(m-1-c)//R+1) for c in range(R)]
    return sum(min(s,q) for s in sizes)

def run():
    tested=0
    for p in (2,3,5):
      for k in (1,2,3,4):
        for N in (1,2,3,4,5,6,8,9,12):
          for m in (2,3,4,5):
            for t in (1,2,3,4,5,6,8,9,12,17):
              a=1; b=(p-1)
              x=measured_rank(p,k,N,m,t,a,b)
              y=predicted(p,k,N,m,t)
              assert x==y,(p,k,N,m,t,x,y)
              tested+=1
    for p,k,N,m,t in ((2,1,8,3,8),(2,1,8,3,9),(2,1,8,3,16),(2,1,8,3,17),(3,2,9,5,4),(5,1,25,3,26)):
      x=measured_rank(p,k,N,m,t,1,1)
      y=predicted(p,k,N,m,t)
      assert x==y,(p,k,N,m,t,x,y)
      tested+=1
    print(f'PASS: {tested} exact recurrence-matrix rank comparisons; no exhaustive infinite claim')
if __name__=='__main__':run()
