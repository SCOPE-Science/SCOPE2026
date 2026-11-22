"""Independent finite-degree algebra and spherical-design checks for harmonic-energy cumulants.
Run: python3 check_harmonic.py. Standard library only.
"""
from fractions import Fraction as F
from math import factorial, sqrt
from itertools import product

assertions = 0

def check(b, message):
    global assertions
    assertions += 1
    if not b:
        raise AssertionError(message)

def add(a,b):
    out=[F(0)]*max(len(a),len(b))
    for j,v in enumerate(a):out[j]+=v
    for j,v in enumerate(b):out[j]+=v
    return out

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]+=v*w
    return out

def scale(a,c):return [c*v for v in a]

def legendre(deg):
    if deg==0:return [F(1)]
    a,b=[F(1)],[F(0),F(1)]
    for j in range(1,deg):
        c=scale(add(scale([F(0)]+b,F(2*j+1)),scale(a,-F(j))),F(1,j+1))
        a,b=b,c
    return b

def integral_half(poly):
    return sum(v/F(i+1) for i,v in enumerate(poly) if i%2==0)

def gaunt_by_integration(l,m,k):
    a=mul(mul(legendre(l),legendre(m)),legendre(k))
    return F((2*l+1)*(2*m+1)*(2*k+1))*integral_half(a)

def gaunt_by_factorials(l,m,k):
    if (l+m+k)%2 or l>m+k or m>l+k or k>l+m:return F(0)
    s=(l+m+k)//2
    return F((2*l+1)*(2*m+1)*(2*k+1))*F(factorial(2*s-2*l)*factorial(2*s-2*m)*factorial(2*s-2*k),factorial(2*s+1))*F(factorial(s),factorial(s-l)*factorial(s-m)*factorial(s-k))**2

def exact_cumulant(n,l,m,k):
    a=gaunt_by_factorials(l,m,k)
    out=F(4*(n-1),n*n)*a
    if l==m==k:
        out += F(8*(n-1)*(n-2)*(2*l+1),n*n)
    return out

for l in range(1,9):
    for m in range(1,9):
        for k in range(1,9):
            v=gaunt_by_integration(l,m,k)
            w=gaunt_by_factorials(l,m,k)
            check(v==w,('Gaunt',l,m,k,v,w))
            check(w>=0,('Gaunt sign',l,m,k))
            expect=((l+m+k)%2==0 and l<=m+k and m<=l+k and k<=l+m)
            check((w>0)==expect,('selection rule',l,m,k))
check(gaunt_by_factorials(1,1,2)==6,'dipole-quadrupole Gaunt')
check(gaunt_by_factorials(1,2,3)==9,'three distinct coupling')
check(gaunt_by_factorials(2,2,4)==F(90,7),'quadrupole hexadecapole')
check(gaunt_by_factorials(2,2,2)==F(50,7),'pure quadrupole')

# Icosahedron vertices form an equal-weight spherical 5-design; each term in
# the mixed (1,1,2) and pure (1,1,1) products have degree <=4
# at each integration vertex, so the exhaustive design average equals the
# continuous spherical expectation, not an approximate Monte Carlo moment.
phi=(1+sqrt(5))/2
raw=[]
for a in (-1,1):
    for b in (-1,1):
        raw.extend([(0.,float(a),float(b)*phi),(float(a),float(b)*phi,0.),(float(b)*phi,0.,float(a))])
scale_s=sqrt(1+phi*phi)
vertices=[tuple(z/scale_s for z in v) for v in raw]
check(len(vertices)==12 and len(set(vertices))==12,'icosahedron cardinality')

def kernel(degree,u):
    if degree==1:return 3*u
    if degree==2:return F(5,2)*(3*u*u-1)
    raise ValueError('design checker handles degree 1 or 2 only')

for n in (2,3,4):
    tot=12**n
    sums=[0.0]*7 # mean T1, mean T2, var1, var2, cov12, third112, third111
    for inds in product(range(12), repeat=n):
        dots=[[sum(a*b for a,b in zip(vertices[inds[i]],vertices[inds[j]])) for j in range(n)] for i in range(n)]
        v1=sum(3*dots[i][j] for i in range(n) for j in range(n))/n-3
        v2=sum(float(kernel(2,dots[i][j])) for i in range(n) for j in range(n))/n-5
        terms=(v1,v2,v1*v1,v2*v2,v1*v2,v1*v1*v2,v1*v1*v1)
        for i,v in enumerate(terms):sums[i]+=v
    sums=[x/tot for x in sums]
    goal=(0.,0.,float(F(2*(n-1)*3,n)),float(F(2*(n-1)*5,n)),0.,
          float(exact_cumulant(n,1,1,2)),float(exact_cumulant(n,1,1,1)))
    for idx,(v,g) in enumerate(zip(sums,goal)):
        check(abs(v-g)<2e-9,('icosahedron quadrature',n,idx,v,g))
    print('icosahedron n=',n,'third(1,1,2)=',sums[5], 'target=',goal[5])

print('PASS',assertions,'assertions; exact Gaunt and independent icosahedral design checks')
