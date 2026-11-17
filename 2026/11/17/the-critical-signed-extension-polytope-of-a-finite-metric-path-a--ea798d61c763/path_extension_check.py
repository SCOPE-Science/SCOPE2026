"""Exact small-case checks for signed one-point extensions from finite paths."""
from fractions import Fraction as Q
from itertools import product, permutations
from math import factorial


def coefficients(F):
    return [F[0]] + [F[i] - F[i-1] for i in range(1, len(F))] + [1-F[-1]]


def radii(F, lengths):
    m=len(lengths)
    return [sum(lengths[i]*abs(F[i]-(1 if j <= i else 0))
                for i in range(m)) for j in range(m+1)]


def critical_inequalities(F, lengths):
    D=sum(lengths)
    if not all(0<=x<=1 for x in F): return False
    if sum(l*f for l,f in zip(lengths,F)) != D/2: return False
    return all(2*sum(lengths[i]*F[i] for i in range(j))
               <=sum(lengths[:j]) for j in range(1,len(lengths)))


def dual_norm_by_edge_signs(w, lengths, at):
    m=len(lengths)
    M=Q(0)
    for sig in product((-1,1),repeat=m):
        f=[Q(0)]
        for si,l in zip(sig,lengths): f.append(f[-1]+si*l)
        M=max(M,abs(sum(wi*fi for wi,fi in zip(w,f))-f[at]))
    return M

profiles=0
sampled=0
for m in range(1,6):
    weight_sets=[tuple([Q(1)]*m),
                 tuple(Q(i+1) for i in range(m)),
                 tuple(Q(i+1,i+2) for i in range(m))]
    for lengths in weight_sets:
        D=sum(lengths)
        for cells in product(range(5), repeat=m):
            F=tuple(Q(v,4) for v in cells)
            expected=critical_inequalities(F,lengths)
            observed=max(radii(F,lengths))<=D/2
            assert expected==observed, (m,lengths,F,expected,observed)
            sampled+=1
        for cells in list(product((0,1,2),repeat=m))[:32]:
            F=[Q(3*v-1,4) for v in cells]  # Signed coefficients are permitted.
            w=coefficients(F)
            for j,v in enumerate(radii(F,lengths)):
                assert v==dual_norm_by_edge_signs(w,lengths,j)
            profiles+=1
print('EXACT_TREE_TRANSPORT_DUAL_AND_CRITICAL_FACE_PASS',
      'tested_cumulative_vectors=',sampled,'dual_profiles=',profiles)

for m in range(3,8):
    raw=[3**i for i in range(m)]
    avg=Q(sum(raw),m)
    F=tuple(Q(1,2)+Q(v-avg,3**m) for v in raw)
    assert all(0<f<1 for f in F)
    admissible=nonnegative=0
    for p in permutations(F):
        if critical_inequalities(p,tuple([Q(1)]*m)):
            admissible+=1
            if all(p[i]<=p[i+1] for i in range(m-1)):
                nonnegative+=1
    assert admissible==factorial(m-1),(m,admissible)
    assert nonnegative==1,(m,nonnegative)
    print('CYCLIC_BALLOT_PERMUTATIONS_PASS', 'edges=',m,
          'admissible=',admissible,'positive=',nonnegative,
          'fraction_positive=1/'+str(factorial(m-1)))

# A negative interior weight is feasible at the critical radius for every positive
# weighted path with at least three edges.
for lengths in ([Q(1)]*3,[Q(1,3),Q(9,2),Q(1,5)],
                [Q(3),Q(2),Q(5),Q(1),Q(4)]):
    m=len(lengths)
    eps=min(Q(1,20), lengths[0]/(20*lengths[1]))
    F=[Q(1,2)]*m
    F[0]-=eps*lengths[1]/lengths[0]
    F[1]+=eps
    w=coefficients(F)
    assert w[2]<0 and critical_inequalities(F,lengths)
print('CRITICAL_FOUR_VERTEX_SIGNED_THRESHOLD_PASS')
print('WEIGHTED_PATH_SIGNED_OPTIMAL_EXTENSION_ALL_CHECKS_PASS')
