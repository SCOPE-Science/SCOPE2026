"""Exact finite-characteristic cross-checks for the two quartic Hasse invariants.
No external dependencies. This checks examples; the all-prime proof is mathematical.
"""
from math import factorial

def add(a,b,p):
    z=[0]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]=(z[i]+v)%p
    for i,v in enumerate(b):z[i]=(z[i]+v)%p
    while len(z)>1 and z[-1]==0:z.pop()
    return z

def mul(a,b,p):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):z[i+j]=(z[i+j]+v*w)%p
    while len(z)>1 and z[-1]==0:z.pop()
    return z

def sc(a,k,p):return [(v*k)%p for v in a]

def legendre_half(d,p):
    a,b=[1],[0,pow(2,-1,p)]
    if d==0:return a
    for k in range(1,d):
        nxt=add(sc(mul(b,[0,1],p),(2*k+1)*pow(2*(k+1),-1,p),p),sc(a,-k*pow(k+1,-1,p),p),p)
        a,b=b,nxt
    return b

def hasse_E1(p):
    n=(p-1)//2; m=n//2
    out=[0]*(m+1)
    for j in range(m+1):
        coef=factorial(n)//(factorial(j)**2*factorial(n-2*j))*(-4)**(n-2*j)
        for k in range(j+1):
            out[k]=(out[k]+coef*factorial(j)//(factorial(k)*factorial(j-k))*2**(j-k))%p
    return out

def hasse_E0(p):
    n=(p-1)//2; out=[0]*(n+1)
    for j in range(n//2+1):
        out[n-2*j]=(factorial(n)//(factorial(j)**2*factorial(n-2*j)))%p
    return out

def polyval(a,c,p):
    v=0
    for x in reversed(a):v=(v*c+x)%p
    return v

def norm(a,p):
    return sc(a,pow(a[-1],-1,p),p)

def primes(limit):
    return [n for n in range(3,limit) if all(n%d for d in range(2,int(n**0.5)+1))]

def hwt_direct(p,c):
    # Direct sparse expansion of (x^8+c*x^4+1)^((p-1)/2).
    n=(p-1)//2; coefs={}
    for i in range(n+1):
        for j in range(n-i+1):
            exponent=8*i+4*j
            coefs[exponent]=(coefs.get(exponent,0)+factorial(n)//(factorial(i)*factorial(j)*factorial(n-i-j))*c**j)%p
    return [[coefs.get(p*i-j,0) for j in (1,2,3)] for i in (1,2,3)]

def rank3(mat,p):
    a=[r[:] for r in mat]; r=0
    for col in range(3):
        pivot=next((i for i in range(r,3) if a[i][col]%p),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]; inv=pow(a[r][col],-1,p)
        a[r]=[v*inv%p for v in a[r]]
        for i in range(3):
            if i!=r:
                z=a[i][col];a[i]=[(v-z*w)%p for v,w in zip(a[i],a[r])]
        r+=1
    return r

for p in primes(110):
    m=(p-1)//4;n=(p-1)//2
    A=hasse_E1(p);B=hasse_E0(p)
    PA=legendre_half(m,p);PB=legendre_half(n,p)
    assert norm(A,p)==norm(PA,p),('E1',p,A,PA)
    assert norm(B,p)==norm(PB,p),('E0',p,B,PB)
    assert polyval(A,2,p) and polyval(A,-2,p)
    assert polyval(B,2,p) and polyval(B,-2,p)
    assert len(A)-1==m and len(B)-1==n
    # The curve's direct 3x3 Cartier matrix must have predicted rank.
    for c in range(p):
        if (c*c-4)%p==0:continue
        mat=hwt_direct(p,c)
        assert rank3(mat,p)==2*(polyval(A,c,p)!=0)+(polyval(B,c,p)!=0),(p,c,mat,A,B)
    print(f'p={p}: Prym Hasse degree {m}, elliptic Hasse degree {n}; Cartier cross-check OK')
print('VERIFY_OK')
