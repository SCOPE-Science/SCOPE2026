#!/usr/bin/env python3
"""Independent exact checks of majority periodic-state classification on wheel graphs."""
from collections import defaultdict
from math import comb

def choose(n,k): return comb(n,k) if 0<=k<=n else 0

def poly_component(L):
    assert L>=2
    d={(0,0):1,(L,L):1}
    for m in range(2,L):
        for b in range(1,min(L-m,m//2)+1):
            count=L*choose(m-b-1,b-1)*choose(L-m-1,b-1)//b
            assert (L*choose(m-b-1,b-1)*choose(L-m-1,b-1))%b==0
            d[m,m-b]=d.get((m,m-b),0)+count
    return d

def conv(p,q):
    r=defaultdict(int)
    for (m,e),v in p.items():
      for (mm,ee),vv in q.items(): r[m+mm,e+ee]+=v*vv
    return dict(r)

def transfer_component(L):
    # Circular four-state automaton, independently of run-count compositions.
    def mul(a,b):
      out=defaultdict(int)
      for i,j,m,e,v in a:
        for k,l,mm,ee,vv in b:
          if j==k:out[i,l,m+mm,e+ee]+=v*vv
      return [(i,j,m,e,v) for (i,j,m,e),v in out.items()]
    edges=[]
    for a in (0,1):
      for b in (0,1):
        for c in (0,1):
          if b and not (a or c):continue
          edges.append((2*a+b,2*b+c,b,b*c,1))
    acc=[(i,i,0,0,1) for i in range(4)]
    for _ in range(L):acc=mul(acc,edges)
    result=defaultdict(int)
    for i,j,m,e,w in acc:
      if i==j:result[m,e]+=w
    return dict(result)

def analytic(n):
    p=poly_component(n) if n%2 else conv(poly_component(n//2),poly_component(n//2))
    S=sum(v for (m,e),v in p.items() if 2*m>n and 2*e<n)
    return (2+4*(n%2==0)+2*S,S)

def upd(n,state):
    mask=(1<<n)-1
    ring=state&mask;c=(state>>n)&1
    x=[(ring>>i)&1 for i in range(n)]
    y=[int(x[(i-1)%n]+x[(i+1)%n]+c>=2) for i in range(n)]
    new_c=int(2*sum(x)>n or (2*sum(x)==n and c==1))
    return sum(bit<<i for i,bit in enumerate(y))|(new_c<<n)

def brute(n):
    count=0; center_change=0; fixed=0
    for s in range(1<<(n+1)):
      y=upd(n,s)
      if upd(n,y)==s:
        count+=1
        if ((s^y)>>n)&1:center_change+=1
        if s==y:fixed+=1
    return count,center_change,fixed

def run():
    for L in range(2,29):
      a=poly_component(L);b=transfer_component(L)
      assert a==b,(L,a,b)
    for n in range(3,16):
      tot,S=analytic(n)
      b,b_h,b_f=brute(n)
      assert (tot,2*S,2)==(b,b_h,b_f),(n,(tot,S),(b,b_h,b_f))
    known={3:(8,3),4:(6,0),5:(12,5),6:(24,9),7:(44,21),8:(70,32),9:(134,66),10:(156,75),11:(442,220),12:(456,225),13:(1432,715),14:(1672,833)}
    for n,ans in known.items():assert analytic(n)==ans,(n,analytic(n),ans)
    for n in range(3,61):
      t,s=analytic(n)
      assert (t-2)%2==0 and t<=1<<(n+1)
      if n%2: assert t==2+2*s
      else: assert t==6+2*s
    print('PASS: 27 independent polynomial/transfer comparisons; 13 full-state enumerations; 58 all-size exact integer audits; 12 reference counts')
    for n in range(3,15):
      t,s=analytic(n)
      print(n,t,2, (t-2)//2,s)
if __name__=='__main__':run()
