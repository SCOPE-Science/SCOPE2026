"""Exact reproducibility checks for two-landmark screening on wheels.

Python 3.9 or later; standard library only. Finite certificates and
matrix calculations do not replace the written proof for all wheel sizes.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial
from pathlib import Path
import json

checks = 0

def check(b, msg='exact identity'):
    global checks
    assert b, msg
    checks += 1

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def der(p):return trim([i*p[i] for i in range(1,len(p))] or [0])

def sub(a,b):return add(a,[-x for x in b])

def ev(p,x):
    z=0
    for c in p[::-1]:z=z*x+c
    return z

def interp(vals):
    """Newton finite-difference interpolation at x=0,1,...,d."""
    temp=[F(v) for v in vals]; result=[F(0)];basis=[F(1)]
    for k in range(len(vals)):
        result=add(result,[v*temp[0] for v in basis])
        if k+1==len(vals):break
        temp=[temp[i+1]-temp[i] for i in range(len(temp)-1)]
        basis=mul(basis,[F(-k,k+1),F(1,k+1)])
    check(all(ev(result,i)==v for i,v in enumerate(vals)))
    return result

def det(M):
    a=[list(map(int,row)) for row in M]
    n=len(a)
    if not n:return 1
    prev=1;sgn=1
    for k in range(n-1):
        if a[k][k]==0:
            for i in range(k+1,n):
                if a[i][k]:a[k],a[i]=a[i],a[k];sgn=-sgn;break
            else:return 0
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*p-a[i][k]*a[k][j]
                check(z%prev==0,'Bareiss exact divisibility')
                a[i][j]=z//prev
        for i in range(k+1,n):a[i][k]=0
        prev=p
    return sgn*a[-1][-1]

def full(m,mu):
    n=m+1;A=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):A[i][i]=mu+(m if i==0 else 3)
    for i in range(1,n):
        j=1+(i%m)
        for u,v in [(0,i),(i,j)]:A[u][v]-=1;A[v][u]-=1
    return A

def minor(m,S,mu):
    A=full(m,mu);u=[i for i in range(m+1) if i not in S]
    return [[A[i][j] for j in u] for i in u]

def inverse(M):
    n=len(M);a=[list(map(F,row))+[F(int(i==j)) for j in range(n)] for i,row in enumerate(M)]
    for j in range(n):
        p=next(i for i in range(j,n) if a[i][j]!=0)
        a[j],a[p]=a[p],a[j];fac=a[j][j]
        a[j]=[z/fac for z in a[j]]
        for i in range(n):
            if i!=j:
                f=a[i][j];a[i]=[v-f*w for v,w in zip(a[i],a[j])]
    return [row[n:] for row in a]

def trace_inv(M):
    B=inverse(M);return sum(B[i][i] for i in range(len(B)))

def orbit_poly(m,S):
    d=m-1
    values=[det(minor(m,S,F(k))) for k in range(d+1)]
    p=interp(values)
    check(all(int(c)==c for c in p),'integer determinant coefficients')
    check(len(p)==d+1 and p[-1]==1,'monic characteristic polynomial')
    return p

# Independently match the supplied readable coefficient certificate if available.
cert_path = Path(__file__).with_name('certificates.json')
certs = json.loads(cert_path.read_text(encoding='utf-8'))['wheel_sizes'] if cert_path.exists() else None

# Direct integer determinant reconstruction, one representative per orbit.
for m in range(3,8):
    H=orbit_poly(m,(0,1))
    R={d:orbit_poly(m,(1,1+d)) for d in range(1,m//2+1)}
    star=R[m//2]
    if certs is not None:
        saved=certs[str(m)]['principal_determinant_coefficients_ascending']
        check(saved['H']==[int(t) for t in H])
        for d,p in R.items():check(saved['R'+str(d)]==[int(t) for t in p])
        comp=certs[str(m)]['comparison_numerator_coefficients_ascending']
        for name,p in [('H',H)]+[('R'+str(d),p) for d,p in R.items() if d!=m//2]:
            q=sub(mul(der(p),star),mul(p,der(star)))
            check(comp[name+'-R'+str(m//2)]==[int(t) for t in q])
    if m==3:
        check(H==star)
    else:
        for d in R:
            if d==m//2:continue
            q=sub(mul(der(R[d]),star),mul(R[d],der(star)))
            check(all(c>0 for c in q),'strict rim-distance order')
        q=sub(mul(der(H),star),mul(H,der(star)))
        if m<=6:check(all(c>0 for c in q),'smaller wheels never favor hub')
        else:
            want=[-6931,17226,95916,153158,130255,68172,23107,5106,712,57,2]
            check(q==[2*F(z) for z in want], 'degree-ten exact crossover certificate')
            check(ev(want,F(1753547088,10**10))<0)
            check(ev(want,F(1753547089,10**10))>0)
            check(all(z>0 for z in want[1:]) and want[0]<0)
    for x in [F(1,100),F(1,10),F(1,4),F(1),F(4),F(30)]:
        for S in [(0,1)]+[(1,1+d) for d in R]:
            p=H if S==(0,1) else R[S[1]-1]
            direct=trace_inv(minor(m,S,x))
            check(der(p) and direct==ev(der(p),x)/ev(p,x),'Jacobi trace identity')
        vals={S:trace_inv(minor(m,S,x)) for S in combinations(range(m+1),2)}
        minimum=min(vals.values()); opt={S for S,v in vals.items() if v==minimum}
        if m==3:expect=set(vals)
        elif m<7:expect={S for S in vals if S[0]>0 and min(abs(S[1]-S[0]),m-abs(S[1]-S[0]))==m//2}
        elif x<F(1,5):expect={S for S in vals if 0 in S}
        else:expect={S for S in vals if S[0]>0 and min(abs(S[1]-S[0]),m-abs(S[1]-S[0]))==3}
        check(opt==expect,f'global minimizers m={m},mu={x}')

# The eight-rim zero-screening orbit table is independently checked.
expected_H = F(2939,987)
expected_R = [F(4927,1218),F(1451,420),F(425,132),F(221,70)]
check(trace_inv(minor(8,(0,1),F(0)))==expected_H)
for d,c in enumerate(expected_R,1):
    check(trace_inv(minor(8,(1,1+d),F(0)))==c)
    check(c>expected_H)

# The positive-root interval is strict, and a derivative with positive
# coefficients ensures unique crossing on (0,infinity).
print('PASSED:',checks,'exact integer/rational assertions')
