#!/usr/bin/env python3
"""Reproduce exact flat-spectrum leave-one-out trace identities.

Uses standard-library rational arithmetic for the algebraic identities and
projector checks; seeded Gaussian experiments are supplementary diagnostics.
"""
from fractions import Fraction as F
import random
import math

checks = 0

def test(statement, description):
    global checks
    if not statement:
        raise AssertionError(description)
    checks += 1

def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))

def residual(x, vectors):
    basis = []
    for v in vectors:
        w = list(v)
        for b in basis:
            t = dot(w, b) / dot(b, b)
            w = [z - t * y for z, y in zip(w, b)]
        if any(w):
            basis.append(w)
    w = list(x)
    for b in basis:
        t = dot(w, b) / dot(b, b)
        w = [z - t * y for z, y in zip(w, b)]
    return w, len(basis)

# Exact moments: a and b are independent Gaussian vectors in dimension q.
# Their independent radii have chi-square(q) squared lengths; squared
# directional inner product has first two moments 1/q and 3/[q(q+2)].
for rank in range(1, 81):
    for k in range(1, rank + 1):
        d = rank - k + 1
        q = d + 1
        u1 = F(1, q)
        u2 = F(3, q * (q + 2))
        cross = q * q * (1 - 2 * u1 + u2)
        cov = cross - d * d
        test(cov == F(2*d, d+3), 'Gaussian angular covariance')
        marginal_var = 2*d
        combined = F(marginal_var, k) + F(k-1, k) * cov
        expected = F(2*d*(rank+3), k*(d+3))
        test(combined == expected, 'exact trace variance')
        if k >= 2:
            posterior = F(marginal_var-cov, k)
            wanted = F(2*d*(d+2), k*(d+3))
            test(posterior == wanted, 'posterior variance expectation')
            test(posterior / combined == F(rank-k+3, rank+3),
                 'posterior calibration ratio')
    d = 1
    test(F(2*d*(rank+3),rank*(d+3)) == F(rank+3,2*rank),
         'rank-saturation variance')

# Exact arithmetic tests of the one-pass Nyström identity, in the effective
# nonzero-eigenvalue subspace. This is also sufficient for any ambient N>=rank.
rng = random.Random(6206305)
for rank in range(1, 9):
    for k in range(1,rank+2):
        for rep in range(15):
            probes = [[F(rng.randint(-8,8)) for _ in range(rank)]
                      for __ in range(k)]
            _, rk_full = residual([F(0)]*rank,probes)
            if rk_full != min(k, rank):
                continue
            bases = []
            valid = True
            for i in range(k):
                others = probes[:i]+probes[i+1:]
                xi_vec, rank_leave = residual(probes[i],others)
                if rank_leave != min(k-1, rank):
                    valid = False
                    break
                bases.append((xi_vec,rank_leave))
            if not valid:
                continue
            c = F(5,3)  # any prescribed value f(lambda)
            terms = [c*rank_leave + c*dot(xi,xi)
                     for xi,rank_leave in bases]
            est = sum(terms,F(0))/k
            if k <= rank:
                target = c*(k-1)+c*sum((dot(xi,xi) for xi,_ in bases),F(0))/k
                test(est==target,'projector exact formula')
            else:
                test(est==c*rank, 'one extra sample exactly resolves flat spectrum')

# Independent direct Monte Carlo: recompute Gram-Schmidt residuals for each
# leave-one-out set, rather than sampling moments from the analytical formula.
def leave_norm_float(a, vectors):
    basis=[]
    for v in vectors:
        w=v.copy()
        for b in basis:
            t=sum(x*y for x,y in zip(w,b))
            w=[x-t*y for x,y in zip(w,b)]
        norm=math.sqrt(sum(x*x for x in w))
        if norm>1.e-10:
            basis.append([x/norm for x in w])
    w=a.copy()
    for b in basis:
        t=sum(x*y for x,y in zip(w,b))
        w=[x-t*y for x,y in zip(w,b)]
    return sum(x*x for x in w), len(basis)

numrng=random.Random(16172026)
for rank,k,reps in [(2,2,8000),(5,2,8000),(6,5,8000),(8,8,8000),(5,6,2000)]:
    actual=[];posterior=[]
    for _ in range(reps):
        vs=[[numrng.gauss(0,1) for _ in range(rank)] for j in range(k)]
        bases=[leave_norm_float(vs[j],vs[:j]+vs[j+1:])
               for j in range(k)]
        vals=[dim+nrm for nrm,dim in bases]
        est=sum(vals)/k
        actual.append(est)
        if k>1:
            posterior.append(sum((v-est)**2 for v in vals)/(k*(k-1)))
    var=sum((v-rank)**2 for v in actual)/reps
    if k<=rank:
        d=rank-k+1
        theory=2*d*(rank+3)/(k*(d+3))
        test(abs(var-theory)<0.13*theory,'Gaussian risk simulation')
        if k>1:
            pmean=sum(posterior)/reps
            pred=2*d*(d+2)/(k*(d+3))
            test(abs(pmean-pred)<0.13*pred,'Gaussian posterior simulation')
    else:
        test(var<1.e-19,'rank saturation simulation')

print('PASS:',checks,'algebraic, exact-projector and seeded numerical checks')
