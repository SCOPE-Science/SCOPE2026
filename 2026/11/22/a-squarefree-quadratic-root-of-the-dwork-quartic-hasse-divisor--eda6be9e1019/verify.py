"""Exact modular coefficient, squarefreeness, and smooth-base checks for Dwork quartics."""
from math import comb, factorial

def trim(a):
    while a and a[-1]==0: a.pop()
    return a

def mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    return trim(c)

def divrem(a,b,p):
    a=trim(a[:]); b=trim(b[:]); assert b
    while len(a)>=len(b):
        c=a[-1]*pow(b[-1],-1,p)%p
        s=len(a)-len(b)
        for i,v in enumerate(b):a[i+s]=(a[i+s]-c*v)%p
        trim(a)
    return a

def pgcd(a,b,p):
    while b: a,b=b,divrem(a,b,p)
    return len(a)-1

def check(p):
    k=(p-1)//8; delta=int(p%8 in (5,7));d=(p-1-4*delta)//2
    aa,bb=(1,3) if not delta else (5,7)
    a=aa*pow(8,-1,p)%p;b=bb*pow(8,-1,p)%p
    Q=[0]*(d+1);coeff=1
    for j in range(k+1):
        Q[d-4*j]=coeff
        if j<k:coeff=coeff*(a+j)*(b+j)*pow((j+1)**2,-1,p)%p
    P=mul(Q,Q,p)
    if delta:
        P=mul(P,[(p-1)%p,0,0,0,1],p)
    H=[0]*p
    for j in range((p-1)//4+1):
        expo=p-1-4*j
        c=factorial(p-1)//(factorial(p-1-4*j)*factorial(j)**4)*(-4)**expo
        H[expo]=c%p
    trim(H)
    assert P==H,(p,'identity',P,H)
    assert pgcd(Q,[(i*v)%p for i,v in enumerate(Q)][1:],p)==0,(p,'squarefree')
    assert pgcd(Q,[(p-1),0,0,0,1],p)==0,(p,'smooth')
    return d,Q

for p in range(5,212):
    if all(p%i for i in range(2,int(p**.5)+1)):
        d,q=check(p)
        if p in (5,7,11,13,17,19,23,29):print(p,d,[(i,c) for i,c in enumerate(q) if c])
print('DWORK_HASSE_SQUAREFREE_FAMILY_EXACT_FINITE_CHECK_VERIFIED')
