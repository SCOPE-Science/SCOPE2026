"""Exact truncated cyclotomic Smith tests for parabolic Fourier restriction.

Run with python3 verify.py. Requires only the Python standard library.
The truncated ring F_p[pi]/(pi^(m+1)) agrees with the cyclotomic
valuation quotient at this precision because v_pi(p)=p-1 >= m+1.
Finite tests corroborate, but do not prove, the all-prime theorem.
"""
from math import comb

def sv(a):
    return next((i for i,x in enumerate(a) if x),len(a))

def add(a,b,p):return [(x+y)%p for x,y in zip(a,b)]
def sub(a,b,p):return [(x-y)%p for x,y in zip(a,b)]
def mul(a,b,p):
    n=len(a);o=[0]*n
    for i,x in enumerate(a):
        if not x:continue
        for j in range(n-i):
            if b[j]:o[i+j]=(o[i+j]+x*b[j])%p
    return o

def quotient(a,b,p):
    n=len(a);v=sv(b)
    assert v<n and sv(a)>=v
    o=[0]*n
    iv=pow(b[v],-1,p)
    for t in range(n-v):
        val=(a[v+t]-sum(o[j]*b[v+t-j] for j in range(t)))%p
        o[t]=val*iv%p
    assert mul(o,b,p)==a,(a,b,o)
    return o

def smith(p,c):
    m=(p-1)//2;T=m+1
    a=[[[comb((s*t+c*(s*t)**2)%p,k)%p if k<=((s*t+c*(s*t)**2)%p) else 0 for k in range(T)] for t in range(p)] for s in range(p)]
    vs=[]
    for i in range(p):
        v,j,k=min((sv(a[j][k]),j,k) for j in range(i,p) for k in range(i,p))
        assert v<T, (p,c,i,'zero')
        a[i],a[j]=a[j],a[i]
        for row in a:row[i],row[k]=row[k],row[i]
        vs.append(v)
        for j in range(i+1,p):
            q=quotient(a[j][i],a[i][i],p)
            a[j]=[sub(x,mul(q,y,p),p) for x,y in zip(a[j],a[i])]
        for k in range(i+1,p):
            q=quotient(a[i][k],a[i][i],p)
            for j in range(i,p):
                a[j][k]=sub(a[j][k],mul(q,a[j][i],p),p)
        assert all(sv(a[i][j])==T for j in range(i+1,p))
        assert all(sv(a[j][i])==T for j in range(i+1,p))
    return sorted(vs)

for p in [3,5,7,11,13,17,19]:
    expected=[0]+[r for r in range(1,(p+1)//2) for _ in range(2)]
    for c in sorted(set([1,2,p-1])):
        s=smith(p,c)
        assert s==expected,(p,c,s,expected)
    print('SMITH_CONFIRMED',p,expected)
print('PARABOLIC_LOCAL_SMITH_PASS')
