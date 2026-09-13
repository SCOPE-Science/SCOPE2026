"""Step 1: enumerate primary primes, pairwise cubic symbols."""
import math, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1560/output/artifacts')
from eisen import *

def e_round_div(alpha, beta):
    # alpha/beta in Q(w): alpha*conj(beta)/N
    N = enorm(beta)
    num = emul(alpha, econj(beta))
    p, q = num
    # candidates around p/N, q/N
    import math as m
    p0 = m.floor(p/N); q0 = m.floor(q/N)
    best=None
    for da in (0,1):
        for db in (0,1):
            qu=(p0+da,q0+db)
            r=esub(alpha, emul(qu,beta))
            n=enorm(r)
            if best is None or n<best[0]:
                best=(n,qu,r)
    return best[1], best[2]

def egcd(a,b):
    # returns (g,s,t) with s*a+t*b=g
    oa,ob=a,b
    s0,t0=ONE,ZERO; s1,t1=ZERO,ONE
    while not eeq(b,ZERO):
        q,r=e_round_div(a,b)
        a,b=b,r
        s0,s1=s1,esub(s0,emul(q,s1))
        t0,t1=t1,esub(t0,emul(q,t1))
        if enorm(b)>enorm(a)*2+100:
            raise AssertionError("euclid not decreasing")
    return a,s0,t0

def einv(a,pi):
    # solve a*s + pi*t = unit; return s/unit
    g,s,t=egcd(a,pi)
    if enorm(g)!=1:
        raise AssertionError(f"not invertible: {a} mod {pi}, gcd={g}")
    # s*a = g mod pi => a*(s*g^-1)=1; g unit: g^-1=conj(g)/1? unit inverse: find u with u*g=1
    for u in UNITS:
        if eeq(emul(u,g),ONE):
            return emul(s,u)
    raise AssertionError("unit inv fail")

def epowmod2(base,e,pi):
    r=ONE
    b=emod2(base,pi)
    while e>0:
        if e&1: r=emulmod2(r,b,pi)
        b=emulmod2(b,b,pi); e>>=1
    return r

def emod2(a,pi):
    _,r=e_round_div(a,pi)
    return r

def emulmod2(a,b,pi): return emod2(emul(a,b),pi)

def econg2(a,b,pi): return eeq(emod2(esub(a,b),pi),ZERO)

def cubic_symbol2(alpha,pi):
    if econg2(alpha,ZERO,pi): return None
    N=enorm(pi)
    v=epowmod2(alpha,(N-1)//3,pi)
    if econg2(v,ONE,pi): return 0
    if econg2(v,OMEGA,pi): return 1
    w2=emul(OMEGA,OMEGA)
    if econg2(v,w2,pi): return 2
    raise AssertionError(f"bad symbol val {v} for {alpha} mod {pi} N={N}")

# enumerate
primes=enum_primary_primes(5000)
print("count eligible (primary, N<5000, excluding above 3):", len(primes))
for pi,N,k,rp in primes[:12]:
    print(estr(pi), N, k, rp, "primary?", is_primary(pi))

# check primariness + mod3 condition
bad=[(pi,N) for pi,N,k,rp in primes if not is_primary(pi)]
print("nonprimary count:", len(bad))

# pairwise symbols among first few (smallest norms)
small=[p for p in primes if p[1]<200]
print("small count:", len(small))
for pi,N,k,rp in small[:20]:
    print(estr(pi),N)
