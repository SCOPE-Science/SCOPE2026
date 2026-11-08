#!/usr/bin/env python3
"""Reproduce the finite checks for the periodic two-run distinct-subsequence theorem.
Uses only the Python standard library. No finite check replaces the proof.
"""

def plus(*polys):
    n=max((len(p) for p in polys), default=0)
    out=[0]*n
    for p in polys:
        for i,x in enumerate(p):out[i]+=x
    return out

def neg(p): return [-x for x in p]

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def power(k):return [0]*k+[1]

def geos(k):return [0]+[1]*k

def expand(a,b,m):
    a0=geos(a);b0=geos(b)
    X=power(a);Y=power(b)
    u=[0];v=[0]
    for _ in range(m):
        u0=plus(mul(X,u),mul(a0,plus(v,[1])))
        v0=plus(mul(Y,v),mul(b0,plus(u0,[1])))
        u,v=u0,v0
    return plus([1],u,v)

def generating_recurrence(a,b,top):
    A=geos(a);B=geos(b);X=power(a);Y=power(b)
    K=plus(X,Y,mul(A,B));XY=mul(X,Y)
    C=plus(A,neg(X));D=plus(B,neg(Y))
    numer={0:[1],1:plus(C,D),2:mul(C,D)}
    fs=[]
    for m in range(top+1):
        f=numer.get(m,[0])
        if m>=1:f=plus(f,mul(plus(K,[1]),fs[m-1]))
        if m>=2:f=plus(f,neg(mul(plus(K,XY),fs[m-2])))
        if m>=3:f=plus(f,mul(XY,fs[m-3]))
        fs.append(f)
    return fs

def brute(a,b,m):
    found={''}
    for c in ('0'*a+'1'*b)*m:
        found |= {v+c for v in found}
    out=[0]*(m*(a+b)+1)
    for v in found:out[len(v)]+=1
    return out

def equivalent(a,b):
    p,q=a[:],b[:]
    p.extend([0]*max(0,len(q)-len(p)))
    q.extend([0]*max(0,len(p)-len(q)))
    return p==q

if __name__=='__main__':
    c1=c2=c3=0
    for a in range(1,5):
      for b in range(1,5):
       fm=generating_recurrence(a,b,6)
       for m in range(7):
        assert equivalent(expand(a,b,m),fm[m]),('transfer vs GF',a,b,m)
        c1+=1
        if m*(a+b)<=19:
            assert equivalent(brute(a,b,m),fm[m]),('brute vs GF',a,b,m)
            c2+=1
    for s in range(2,21):
      for m in range(1,11):
        values=[]
        for a in range(1,s):
          b=s-a
          values.append((sum(expand(a,b,m)),a,b))
        peak=max(x for x,a,b in values)
        assert all((x==peak)==(abs(a-b)<=1) for x,a,b in values),('balance',s,m)
        c3+=1
    print(f'PASS transfer/GF={c1}; independent distinct-word enumeration={c2}; finite balance={c3}')
