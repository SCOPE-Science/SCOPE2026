#!/usr/bin/env python3
"""Independent finite-field and matrix reproducibility checks for quartic-phase masks."""
from collections import Counter, defaultdict
import math
import numpy as np

CHECKS = 0

def check(flag, label):
    global CHECKS
    CHECKS += 1
    if not flag:
        raise AssertionError(label)

def primes(limit):
    for n in range(5, limit + 1):
        if all(n % d for d in range(2, math.isqrt(n) + 1)):
            yield n

def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def fibers(p):
    out = defaultdict(list)
    for x in range(p):
        out[(4 * x**3 + x) % p].append(x)
    return dict(out)

def m_expected(p):
    return (2 * p + chi(-3, p)) // 3

def basis_hermitian(p):
    out = []
    for j in range(p):
        a = np.zeros((p,p), complex)
        a[j,j] = 1
        out.append(a)
    for j in range(p):
        for k in range(j):
            a = np.zeros((p,p), complex)
            a[j,k] = a[k,j] = 1
            out.append(a)
            b = np.zeros((p,p), complex)
            b[j,k] = 1j
            b[k,j] = -1j
            out.append(b)
    return np.array(out)

def measurement_matrix(p, r):
    basis = basis_hermitian(p)
    js = np.arange(p)
    rows = []
    for s in range(r):
        for k in range(p):
            v = np.exp((2j*np.pi/p)*((s*js**4 + k*js) % p))/np.sqrt(p)
            rows.append(np.einsum('i,aij,j->a',v.conj(),basis,v).real)
    return np.asarray(rows)

def measure(H, p, r):
    js = np.arange(p)
    vals = []
    for s in range(r):
        for k in range(p):
            v = np.exp((2j*np.pi/p)*((s*js**4+k*js) % p))/np.sqrt(p)
            vals.append(v.conj()@H@v)
    return np.asarray(vals)

for p in primes(197):
    fs = fibers(p)
    e = chi(-3, p)
    c = Counter(map(len, fs.values()))
    check(len(fs)==m_expected(p), ('size',p))
    check(c[1]==(p-1)//2, ('one',p))
    check(c[2]==1+e, ('two',p))
    check(c[3]==(p-3-4*e)//6, ('three',p))
    check(set(c).issubset({1,2,3}), ('max multiplicity',p))
    for x in range(p):
        for y in range(p):
            if x!=y:
                L = ((4*x*x*x+x)-(4*y*y*y+y))%p
                R = (4*(x*x+x*y+y*y)+1)%p
                check((L==0)==(R==0), ('collision factor',p,x,y))
    # exact critical-value count, including separation
    cv = {(4*x**3+x)%p for x in range(p) if (12*x*x+1)%p==0}
    check(len(cv)==1+e, ('critical values',p))

for p in [5,7,11,13]:
    m = m_expected(p)
    for r in sorted({1,2,3,m-1,m,min(p,m+1),p}):
        if not 1<=r<=p: continue
        M = measurement_matrix(p,r)
        rank = np.linalg.matrix_rank(M,tol=1e-8)
        expect = 1+(p-1)*min(r,m)
        check(rank==expect, ('Hermitian rank',p,r,rank,expect))
        check(M.shape == (p*r,p*p), ('matrix dimensions',p,r))
    # In every case a traceless diagonal is invisible.
    D=np.diag([1,-1]+[0]*(p-2)).astype(complex)
    check(np.linalg.norm(measure(D,p,p))<1e-11, ('traceless diagonal',p))
    # Every non-singleton cubic fiber gives an invisible off-diagonal matrix.
    inv2=pow(2,-1,p)
    d=1
    lookup=defaultdict(list)
    for j in range(p):
        u=(j*pow(d,-1,p)-inv2)%p
        lookup[(4*u**3+u)%p].append(j)
    for pre in lookup.values():
        if len(pre)<2: continue
        a,b=pre[:2]
        H=np.zeros((p,p),complex)
        H[a,(a-d)%p]+=1
        H[(a-d)%p,a]+=1
        H[b,(b-d)%p]-=1
        H[(b-d)%p,b]-=1
        check(np.linalg.norm(measure(H,p,p))<1e-10,('fiber kernel',p,a,b))

# Independent full explicit Lagrange moment null relation for unsaturated masks.
for p,r in [(7,2),(11,3)]:
    d=1
    inv2=pow(2,-1,p)
    fs=defaultdict(list)
    for j in range(p):
        u=(j-inv2)%p
        fs[(4*u**3+u)%p].append(j)
    nodes={t:np.exp(-2j*np.pi*t/p) for t in fs}
    weights={t:1/np.prod([nodes[t]-nodes[u] for u in fs if u!=t]) for t in fs}
    check(len(fs)>r,('unsaturated',p))
    H=np.zeros((p,p),complex)
    for t,jlist in fs.items():
        j=jlist[0]
        H[j,(j-1)%p]+=weights[t]
        H[(j-1)%p,j]+=np.conj(weights[t])
    check(np.linalg.norm(measure(H,p,r))<1e-8, ('Lagrange kernel',p,r))

print('PASS:',CHECKS,'independent finite-field and Hermitian-matrix assertions')
