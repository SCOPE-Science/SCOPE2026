"""Independent exact Euclidean checks of the geometric superspecial intersections."""
from math import comb

def trim(a,p):
    a=[v%p for v in a]
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def legendre_poly(n,p):
    # Coefficient formula in powers of c for the degree-n Legendre P_n(c/2).
    a=[0]*(n+1)
    for k in range(n//2+1):
        # (-1)^k * (2n-2k)! / (2^(2n-2k) k!(n-k)!(n-2k)!)
        # = (-1)^k * comb(n,k)*comb(2n-2k,n) / 2^(2n-2k)
        j=n-2*k
        a[j]=(-1)**k*comb(n,k)*comb(2*n-2*k,n)*pow(2,-(2*n-2*k),p)%p
    return trim(a,p)

def rem(a,b,p):
    a=trim(a,p);b=trim(b,p)
    while len(a)>=len(b) and a!=[0]:
        h=a[-1]*pow(b[-1],-1,p)%p
        d=len(a)-len(b)
        for i,v in enumerate(b):a[d+i]=(a[d+i]-h*v)%p
        a=trim(a,p)
    return a

def gcd(a,b,p):
    while b!=[0]:a,b=b,rem(a,b,p)
    return trim([(x*pow(a[-1],-1,p))%p for x in a],p)

expected={3:0,5:0,7:1,11:0,13:0,17:2,19:0,23:1,31:3,47:7,73:6,97:2}
for p,degree in expected.items():
    m=(p-1)//4;n=(p-1)//2
    A=legendre_poly(m,p);B=legendre_poly(n,p)
    g=gcd(A,B,p)
    assert len(g)-1==degree,(p,len(g)-1,degree)
    assert rem(A,g,p)==[0] and rem(B,g,p)==[0]
    print(f'p={p}: m={m}, n={n}, gcd-degree={degree}')
print('VERIFY_OK')
