"""Numerical spot checks for path-variation estimates of three-sample p-means.
Run: python check_pmean.py. Finite tests do not certify universal inequalities.
"""
import random

def pmean(vals,p):
    if p==2: return sum(vals)/3.0
    lo=min(vals); hi=max(vals)
    if hi==lo: return lo
    q=p-1
    for _ in range(66):
        z=(lo+hi)/2
        s=sum((abs(x-z)**q)*(1 if x>z else -1 if x<z else 0) for x in vals)
        if s>0: lo=z
        else: hi=z
    return (lo+hi)/2

def transform(x,p):
    return [pmean(x[i:i+3],p) for i in range(len(x)-2)]

def var(x): return sum(abs(a-b) for a,b in zip(x,x[1:]))

def bound(n,p):
    if n==3: return 0
    if p<2: return min(n-3,3)
    if p==2: return min((n-3)/3,1)
    return 1

def checks():
    rng=random.Random(12031991)
    count=0
    for p in (1.25,1.5,1.75,2,2.1,3,4,8):
      for n in (3,4,5,6,7,8,12):
       B=bound(n,p)
       for _ in range(80):
        x=[rng.uniform(-3,3) for i in range(n)]
        y=[rng.uniform(-3,3) for i in range(n)]
        vin=var([a-b for a,b in zip(x,y)])
        vout=var([a-b for a,b in zip(transform(x,p),transform(y,p))])
        assert vout <= B*vin + 3e-11,(n,p,vin,vout,B)
        count+=1
    print('RANDOM_TWO_INPUT_INEQUALITIES_PASS',count)
    # First-order extremizers: 3, 4 or 5 output coordinates anchored around (-1,1,0,2).
    for p in (1.25,1.5,1.75,3,4,8):
      for n in (4,5,6,9):
        if n==4: x=[-1,1,0,2]; k=2
        elif n==5: x=[-1,1,0,2,0]; k=2
        else: x=[0,-1,1,0,2]+[0]*(n-5); k=3
        h=[0]*k+[1]*(n-k)
        eps=1e-7 if p>=2 else 1e-9
        y=[xi+eps*hi for xi,hi in zip(x,h)]
        vi=var([a-b for a,b in zip(x,y)])
        vo=var([a-b for a,b in zip(transform(x,p),transform(y,p))])
        ratio=vo/vi
        target=bound(n,p)
        assert abs(ratio-target)<(0.03 if p<2 else 0.002),(n,p,ratio,target)
        print('SHARPNESS_LIMIT',p,n,round(ratio,8),'target',target)
    print('ALL_THREE_SAMPLE_P_MEAN_CHECKS_PASS')

if __name__=='__main__':checks()
