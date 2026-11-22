"""Reproduce exact six-character permutation moment identities; standard library only.
Run: python check.py
"""
from functools import lru_cache
from itertools import permutations
from math import factorial, pi, cos, sin

@lru_cache(None)
def partitions(n):
    if n == 0: return ((),)
    out=[]
    for p in partitions(n-1):
        out.append(p+((n-1,),))
        for j in range(len(p)):
            q=list(p); q[j]=q[j]+(n-1,); out.append(tuple(q))
    return tuple(out)

# Polynomials with integer coefficients ordered by ascending power.
def norm(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return tuple(a)
def add(a,b): return norm([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return norm(z)
def scale(a,c):return norm([c*x for x in a])
def product(ps):
    z=(1,)
    for p in ps:z=mul(z,p)
    return z
def poly_sub(a,b):return add(a,scale(b,-1))
def ev(a,n):return sum(c*n**i for i,c in enumerate(a))
N=(0,1)
SIGNS=(1,1,1,-1,-1,-1)

def injective_character_sum(p,order):
    # For a block partition p of six positions, use partition-lattice Mobius inversion.
    blockweights=[sum(SIGNS[i] for i in block) for block in p]
    val=(0,)
    for coarsening in partitions(len(p)):
        if any(sum(blockweights[i] for i in block)%order for block in coarsening):continue
        mu=1
        for block in coarsening:mu*=(-1)**(len(block)-1)*factorial(len(block)-1)
        val=add(val,scale((0,)*len(coarsening)+(1,),mu))
    return val

def claimed_raw_numerator(kind):
    if kind == (7,7):
        q=(-20,34,-27,6)
        return product(((0,0,0,1),q,(0,1),(-4,1),(-5,1)))
    if kind == (3,7):
        q=(2,-3,2)
        return product(((0,0,0,3),q,(0,1),(-3,1),(-4,1),(-5,1)))
    if kind == (3,3):
        q=(108,-225,201,-62,6)
        return product(((0,0,0,1),q,(0,1),(-3,1)))
    raise ValueError(kind)

def poly_certificate(kind):
    # Common denominator (n)_6, each term indexed by equality partition of 6.
    numer=(0,)
    sum_by_m=[(0,) for _ in range(7)]
    for p in partitions(6):
        f=injective_character_sum(p,kind[0]);g=injective_character_sum(p,kind[1])
        sum_by_m[len(p)]=add(sum_by_m[len(p)],mul(f,g))
    for m in range(1,7):
        numer=add(numer,mul(sum_by_m[m],product(tuple((-j,1) for j in range(m,6)))))
    expected=claimed_raw_numerator(kind)
    assert numer == expected,(kind,numer,expected)
    return len(partitions(6)),sum(len(p)>0 for p in partitions(6))

def theoretical(n,k,l):
    mu=n/(n-1)
    var=n*(n*n-3*n+3)/((n-2)*(n-1)**2)
    r=int((3*k)%n==0)+int((3*l)%n==0)
    K0=2*(n**4-6*n**3+14*n**2-16*n+5)/((n-3)*(n-1)**3)
    K1=(2*n**3-6*n*n+9*n-3)/(n-1)**3
    K2=(n-3)*(2*n**5-21*n**4+80*n**3-148*n*n+135*n-36)/((n-5)*(n-4)*(n-2)*(n-1)**3)
    return mu,var,(K0,K1,K2)[r]

def enumerative_check(n,pairs):
    # Full enumeration independent of the partition algebra (no Monte Carlo).
    root=[complex(cos(2*pi*j/n),sin(2*pi*j/n)) for j in range(n)]
    sums=[[0.0,0.0,0.0] for _ in pairs]
    count=0
    for perm in permutations(range(n)):
        count+=1
        for index,(k,l) in enumerate(pairs):
            a=sum(root[(k*j+l*perm[j])%n] for j in range(n))
            z=(a.real*a.real+a.imag*a.imag)/n
            sums[index][0]+=z
            sums[index][1]+=z*z
            sums[index][2]+=z*z*z
    for (k,l),(s1,s2,s3) in zip(pairs,sums):
        m=s1/count
        v=s2/count-m*m
        third=s3/count-3*m*s2/count+2*m**3
        em,ev,et=theoretical(n,k,l)
        for measured,expected in ((m,em),(v,ev),(third,et)):
            assert abs(measured-expected)<3e-9,(n,k,l,measured,expected)
    return count*len(pairs)*3

if __name__=='__main__':
    checks=0
    for kind in ((7,7),(3,7),(3,3)):
        n,m=poly_certificate(kind);checks+=1;print('exact polynomial identity passed for',kind,':',n,'equality partitions')
    checks+=enumerative_check(7,[(1,1),(2,3)])
    checks+=enumerative_check(9,[(1,1),(3,1),(3,3)])
    print('PASS: all symbolic identities and exhaustive n=7,9 moments;',checks,'enumerated moment contributions plus three exact polynomial identities')
