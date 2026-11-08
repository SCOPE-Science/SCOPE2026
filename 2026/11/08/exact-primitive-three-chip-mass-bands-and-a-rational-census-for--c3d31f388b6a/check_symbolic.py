"""Exact 9-state transfer test and independent explicit firing-phase enumerations."""
from collections import defaultdict
from itertools import product
import sympy as sp

x,t=sp.symbols('x t')
states=list(product(range(3),repeat=2))
idx={a:i for i,a in enumerate(states)}
def weight(a,b,c):
    return int(b==1)+int(a==(b-1)%3)+int(c==(b-1)%3)
T=sp.zeros(9); L=sp.zeros(1,9); R=sp.zeros(9,1)
for a,b in states:
    i=idx[a,b]
    L[i]=(int(a==1)+int(b==(a-1)%3))*t**int(a==2)
    R[i]=(int(b==1)+int(a==(b-1)%3))*t**int(b==2)
    for c in range(3): T[i,idx[b,c]]=weight(a,b,c)*t**int(b==2)
Q=(L*(sp.eye(9)-x*T).inv()*R)[0]
f=sp.factor(sp.diff(Q,t).subs(t,1))
target=2*(1-x)/((1-3*x+x*x)**2*(1+x+x*x))
assert sp.cancel(f-target)==0
print('RATIONAL_IDENTITY=PASS')

# General degree-dependent local polynomial for one firing in three rounds.
def chip_options(phase,degree,nphase):
    z0,z1,z2=nphase
    if phase==0: return range(degree, degree+z2)
    if phase==1: return range(degree-z0,degree)
    return range(z2,z2+z1)

def low_poly(n):
    ans=defaultdict(int)
    for colors in product(range(3), repeat=n):
        hcount=colors.count(2)
        if not hcount:continue
        path_poly={0:1}
        for i,phase in enumerate(colors):
            nphase=[int(j==0)+sum(int(colors[k]==j) for k in (i-1,i+1) if 0<=k<n) for j in range(3)]
            degree=2 if i in (0,n-1) else 3
            options=chip_options(phase,degree,nphase)
            if not options:
                path_poly={};break
            next_poly=defaultdict(int)
            for m,cnt in path_poly.items():
                for z in options:next_poly[m+z]+=cnt
            path_poly=next_poly
        for hm in range(n,n+hcount):
            for m,v in path_poly.items():ans[m+hm]+=3*v
    return dict(ans)

def q_value(n):
    a=L*T**(n-2)*R
    return sp.expand(a[0])
for n in range(2,9):
    lo=low_poly(n)
    expected=3*int(sp.diff(q_value(n),t).subs(t,1))
    assert sum(lo.values())==expected,(n,sum(lo.values()),expected)
    support=sorted(k for k,v in lo.items() if v)
    assert support==list(range(2*n-1,3*n-2)),(n,support)
    assert lo[2*n-1]==6
    assert sum(lo.values())*2==[12,48,168,564,1788,5496,16536][n-2]
    print(f'n={n} low={sum(lo.values())} full={2*sum(lo.values())} band={support[0]}..{support[-1]}')
print('PHASE_ENUMERATION=PASS')

# Independently test all mass coefficients of the displayed bivariate matrix.
z=sp.symbols('z')
def S(j): return sum(z**r for r in range(j))
def W(phase,d,nn):
    c0,c1,c2=nn
    if phase==0:return z**d*S(c2)
    if phase==1:return z**(d-c0)*S(c0)
    return z**c2*S(c1)
LL=sp.zeros(1,9); RR=sp.zeros(9,1); MM=sp.zeros(9)
for a,b in states:
    i=idx[a,b]
    LL[i]=t**int(a==2)*W(a,2,[1+int(b==0),int(b==1),int(b==2)])
    RR[i]=t**int(b==2)*W(b,2,[1+int(a==0),int(a==1),int(a==2)])
    for c in range(3):
        MM[i,idx[b,c]]=t**int(b==2)*W(b,3,[1+int(a==0)+int(c==0),int(a==1)+int(c==1),int(a==2)+int(c==2)])
for n in range(2,6):
    QQ=sp.expand((LL*MM**(n-2)*RR)[0])
    poly=sp.cancel(3*z**n*(QQ.subs(t,1)-QQ.subs(t,z))/(1-z))
    co=low_poly(n)
    expected=sum(v*z**k for k,v in co.items())
    assert sp.expand(poly-expected)==0,(n,poly,expected)
    print(f'n={n} BIVARIATE_COEFFICIENTS=PASS')
print('BIVARIATE_TRANSFER=PASS')
