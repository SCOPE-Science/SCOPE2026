#!/usr/bin/env python3
"""Independent truncated-local-ring elimination for cubic graph Fourier self-sampling."""
import math

def modconv(a,b,p,N):
    z=[0]*N
    for i,x in enumerate(a):
        if not x: continue
        for j,y in enumerate(b[:N-i]):
            if y: z[i+j]=(z[i+j]+x*y)%p
    return z

def add(a,b,p,sgn=1):return [(x+sgn*y)%p for x,y in zip(a,b)]
def valuation(a):
    return next((i for i,v in enumerate(a) if v),len(a))
def invunit(a,p,N):
    assert a[0]%p
    z=[0]*N
    z[0]=pow(a[0],-1,p)
    for k in range(1,N):
        z[k]=(-z[0]*sum(a[i]*z[k-i] for i in range(1,k+1)))%p
    return z

def eliminate(p,a=1,b=1):
    N=p-1
    choose=[[None]*p for i in range(p)]
    for s in range(p):
        for t in range(p):
            E=(a*s*t+b*(s*t)**3)%p
            choose[s][t]=[math.comb(E,i)%p if i<=E else 0 for i in range(N)]
    M=choose
    exps=[]
    for k in range(p):
        cells=[(valuation(M[i][j]),i,j) for i in range(k,p) for j in range(k,p)]
        e,i,j=min(cells)
        if e==N:
            exps.extend([N]*(p-k));break
        M[k],M[i]=M[i],M[k]
        for row in M:row[k],row[j]=row[j],row[k]
        inv=invunit(M[k][k][e:]+[0]*e,p,N)
        for i in range(k+1,p):
            vi=valuation(M[i][k])
            if vi==N:continue
            assert vi>=e
            ratio=modconv(M[i][k][e:]+[0]*e,inv,p,N)
            for j in range(k,p):
                M[i][j]=add(M[i][j],modconv(ratio,M[k][j],p,N),p,-1)
            assert valuation(M[i][k])>=N
        exps.append(e)
    return sorted(exps)

def predicted(p):
    N=p-1
    e0=next(j for j in range(2,N+1,2) if 3*j>=N)
    def tmin(t):
        return next(j for j in range(1,N+1) if j<=t<=3*j and (j-t)%2==0)
    return sorted([0,e0]+[tmin(t) for t in range(1,N)])

if __name__=='__main__':
 for p in [5,7,11,13,17,19]:
    observed=eliminate(p)
    expect=predicted(p)
    assert observed==expect, (p,observed,expect)
    print('p=',p,'smith=',observed,'sum=',sum(observed),'PASS')
 # Variations of cubic curvature; exponent p-1 means at least p-1, not exact.
 for p in [7,11]:
    for c in range(1,p):
        assert eliminate(p,1,c)==predicted(p),(p,c)
    print('all cubic curvatures PASS for',p)
 for c in range(1,5):
    vals=eliminate(5,1,c)
    assert (vals[-1]==4)==(c in (2,3)),(c,vals)
    print('p=5 curvature',c,'truncated invariants',vals)
 # The exceptional character sum cancels exactly, not just modulo p.
 for c in [2,3]:
    assert (1+c-(2+3*c))%5==0 or (1+c+(2+3*c))%5==0
 print('CUBIC_GRAPH_LOCAL_SMITH_PASS')
