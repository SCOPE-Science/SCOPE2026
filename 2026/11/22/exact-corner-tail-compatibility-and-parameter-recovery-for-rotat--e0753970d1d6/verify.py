"""Standalone exact-arithmetic tests for corner-tail recovery in rotated Clayton mixtures.

Python 3.9+ standard library only. Tests finite small thresholds; the proof of
limits and the all-dimensional statements is given separately.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import deque


def vertices(m):
    return list(product((0, 1), repeat=m))


def flip(v, i):
    r = list(v)
    r[i] = 1 - r[i]
    return tuple(r)


def edge_array(weights, m):
    """Common Clayton parameter theta=1, so h=(m-1)/m."""
    h = F(m-1, m)
    return {(v, i): h*weights[v]/(weights[v] + weights[flip(v,i)])
            for v in vertices(m) for i in range(m)}


def check_array(lam, m):
    edge_sums = {lam[v,i] + lam[flip(v,i),i]
                  for v in vertices(m) for i in range(m)}
    assert len(edge_sums) == 1
    h = next(iter(edge_sums))
    assert 0 < h < 1
    assert all(0 < x < h for x in lam.values())
    faces = 0
    for v in vertices(m):
        for i in range(m):
            for j in range(i+1,m):
                left = (lam[flip(v,i),i]/lam[v,i] *
                        lam[flip(flip(v,i),j),j]/lam[flip(v,i),j])
                right = (lam[flip(v,j),j]/lam[v,j] *
                         lam[flip(flip(v,j),i),i]/lam[flip(v,j),i])
                assert left == right
                faces += 1
    recovered = {tuple([0]*m): F(1)}
    queue = deque(recovered)
    while queue:
        v = queue.popleft()
        for i in range(m):
            w = flip(v,i)
            ratio = lam[w,i]/lam[v,i]
            candidate = recovered[v]*ratio
            if w not in recovered:
                recovered[w] = candidate
                queue.append(w)
            else:
                assert recovered[w] == candidate
    s = sum(recovered.values(), F(0))
    recovered = {v: val/s for v,val in recovered.items()}
    assert edge_array(recovered, m) == lam
    return h, recovered, faces


def clayton_cdf(vals):
    """Clayton with theta=1 on a subset; rational argument, exact."""
    if not vals:
        return F(1)
    return 1 / (sum((1/x for x in vals), F(0))-len(vals)+1)


def rotated_event(k, target, indices, t):
    """Exact P(U_i in the requested t-corner for all indices) under rotation k."""
    lower = [i for i in indices if target[i] == k[i]]
    upper = [i for i in indices if target[i] != k[i]]
    out = F(0)
    for sz in range(len(upper)+1):
        for subset in combinations(upper, sz):
            out += (-1)**sz * clayton_cdf([t]*len(lower)+[1-t]*len(subset))
    assert out >= 0
    return out


def mix_event(weights, target, indices, t):
    return sum((weights[k]*rotated_event(k,target,indices,t)
                for k in weights), F(0))


def main():
    num_cases = 0
    num_faces = 0
    for m in (3,4):
        vs = vertices(m)
        for shift in (0,3,11):
            raw = {v: F((7*i+shift)%23+1) for i,v in enumerate(vs)}
            mass = sum(raw.values(),F(0))
            weights = {v:w/mass for v,w in raw.items()}
            lam = edge_array(weights,m)
            h,rec,faces = check_array(lam,m)
            assert h == F(m-1,m)
            assert rec == weights
            num_faces += faces
            num_cases += 1

    m = 3
    vs = vertices(m)
    weights = {v:F(i+1,36) for i,v in enumerate(vs)}
    lam = edge_array(weights,m)
    discrepancies=[]
    for t in (F(1,1000),F(1,10000),F(1,100000)):
        maxerr=F(0)
        for j in vs:
            full = mix_event(weights,j,range(m),t)
            for i in range(m):
                denom=mix_event(weights,j,[k for k in range(m) if k != i],t)
                ratio=full/denom
                maxerr=max(maxerr,abs(ratio-lam[j,i]))
        discrepancies.append(maxerr)
    assert discrepancies[2] < discrepancies[1] < discrepancies[0]
    assert discrepancies[2] < F(1,1000)

    # A locally admissible but globally incompatible table: all edge sums fixed.
    bad = dict(edge_array({v:F(1,8) for v in vs},3))
    zero=(0,0,0)
    other=flip(zero,0)
    bad[zero,0]=F(1,4)
    bad[other,0]=F(5,12)
    try:
        check_array(bad,3)
    except AssertionError:
        pass
    else:
        raise AssertionError('Incompatible four-cycle table incorrectly accepted')

    print('PASS: %d positive rational parameter families; %d exact square-face checks.' %
          (num_cases,num_faces))
    print('PASS: three exact finite-threshold convergences, max errors:',
          ', '.join('%.9g'%float(x) for x in discrepancies))
    print('PASS: constant-edge-sum table with a violated face is rejected.')
    print('Scope: numerical and finite rational diagnostics; not an infinite proof.')


if __name__ == '__main__':
    main()
