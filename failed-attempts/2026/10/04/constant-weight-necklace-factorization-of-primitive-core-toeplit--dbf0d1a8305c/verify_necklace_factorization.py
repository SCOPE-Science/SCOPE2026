#!/usr/bin/env python3
from math import comb, gcd

# GF(2)[x] bit-polynomial utilities.
def deg(f):
    return f.bit_length()-1

def pmul(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
    return r

def pmod(a,m):
    dm=deg(m)
    while a and deg(a)>=dm:
        a ^= m << (deg(a)-dm)
    return a

def pgcd(a,b):
    while b:
        a,b=b,pmod(a,b)
    return a

def mulmod(a,b,m):
    return pmod(pmul(a,b),m)

def powmod(a,n,m):
    r=1
    while n:
        if n&1:r=mulmod(r,a,m)
        a=mulmod(a,a,m);n//=2
    return r

def prime_divisors(n):
    out=[];p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:out.append(n)
    return out

def irreducible(f,d):
    x=2
    # x^(2^d)=x mod f
    if powmod(x,1<<d,f)!=x:
        return False
    for p in prime_divisors(d):
        g = powmod(x,1<<(d//p),f) ^ x
        if pgcd(g,f)!=1:
            return False
    return True

def primitive(f,d):
    if not irreducible(f,d): return False
    x=2; N=(1<<d)-1
    return all(powmod(x,N//p,f)!=1 for p in prime_divisors(N))

def first_primitive(d):
    for mid in range(1<<(d-1)):
        f=(1<<d) | (mid<<1) | 1
        if primitive(f,d): return f
    raise RuntimeError(d)

# Field polynomial in T, low-to-high coefficients, each a GF(2^d) element.
def t_mul(A,B,f):
    C=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):
            C[i+j] ^= mulmod(a,b,f)
    return C

def alpha_pow(e,f,d):
    return powmod(2,e % ((1<<d)-1),f)

def minpoly_from_exponents(exps,f,d):
    P=[1]
    for e in exps:
        P=t_mul(P,[alpha_pow(e,f,d),1],f)  # T + alpha^e in char 2
    if any(c not in (0,1) for c in P):
        raise AssertionError(('not base-field coefficients',P))
    bits=sum((c&1)<<i for i,c in enumerate(P))
    return bits

def poly_str(bits,var='T'):
    if bits==0:return '0'
    ts=[]
    for i in range(deg(bits),-1,-1):
        if not ((bits>>i)&1):continue
        ts.append('1' if i==0 else var if i==1 else f'{var}^{i}')
    return ' + '.join(ts)

def rotations_orbits(d,k):
    subs=[sum(1<<i for i in I) for I in __import__('itertools').combinations(range(d),k)]
    S=set(subs);orbs=[]
    def rot(mask):
        return ((mask<<1)&((1<<d)-1)) | ((mask>>(d-1))&1)
    while S:
        a=min(S);o=[];b=a
        while b not in o:
            o.append(b);b=rot(b)
        for z in o:S.remove(z)
        orbs.append(o)
    return orbs

def exponent(mask,d):
    return sum((1<<i) for i in range(d) if (mask>>i)&1)  # Q=2, so same numeric digits

def mobius(n):
    m=n;cnt=0;p=2
    while p*p<=m:
        if m%p==0:
            m//=p;cnt+=1
            if m%p==0:return 0
            while m%p==0:m//=p
        p+=1
    if m>1:cnt+=1
    return -1 if cnt%2 else 1

def exact_orbit_count_formula(d,k,e):
    if d%e:return 0
    h=d//e
    if k%h:return 0
    w=k//h
    s=0
    for r in range(1,gcd(e,w)+1):
        if gcd(e,w)%r==0:
            s += mobius(r)*comb(e//r,w//r)
    return s//e

# Global necklace formula checks.
for d in range(2,11):
    for k in range(1,d):
        obs={}
        for o in rotations_orbits(d,k): obs[len(o)]=obs.get(len(o),0)+1
        pred={e:exact_orbit_count_formula(d,k,e) for e in range(1,d+1) if exact_orbit_count_formula(d,k,e)}
        assert obs==pred,(d,k,obs,pred)
        assert sum(e*n for e,n in obs.items())==comb(d,k)
        if gcd(d,k)==1:
            assert obs=={d:comb(d,k)//d}

# Exact finite-field checks for several primitive cores.
for d,k in [(4,2),(5,2),(6,2),(6,3)]:
    f=first_primitive(d)
    orbs=rotations_orbits(d,k)
    facs=[]
    for o in orbs:
        exps=[exponent(mask,d) for mask in o]
        fac=minpoly_from_exponents(exps,f,d)
        assert deg(fac)==len(o)
        facs.append((len(o),fac,exps))
    print(f'd={d} k={k} primitive_core={poly_str(f,"x")} factor_degrees={[x[0] for x in facs]}')
    for sz,fac,exps in facs:
        print('  ',sz,poly_str(fac),'exponents=',exps)

print('CHECK_OK')
