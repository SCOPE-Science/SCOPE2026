"""Step H: Lee E2 (Phi-induced) differential ranks on Kh homology for 10_124.
Method: for each (h,q): Kh(h,q) = ker(d_h)/im(d_{h-1}). Phi: C(h,q)->C(h+1,q+4).
Induced map: restrict Phi to ker(d_h), project to coker... compute rank of
  ker(d_h) --Phi--> C(h+1,q+4)/im(d_{h,q+4})  i.e. rank of [Phi; d] stacking.
Concretely: induced rank = rank(M) - rank(d_{h,q+4}) where M = stack(Phi_rows; d_{h,q+4}_rows) restricted to ker basis? Standard formula:
  rank(f) = dim(Phi(ker d_h)) mod im(d_{h,q+4}) = rank([Phi*K, D]) - rank(D)
where K = basis matrix of ker(d_h) (cols), D = matrix of d_{h,q+4} (as row space), Phi*K composed.
Implement with dense mod-p elimination (blocks are small: max block 297? homology dims are 0/1 so ranks are 0/1 decisions — cheap).
Also verify Lee homology dim = 2 (knot) as global check: rank of full d_Lee.
"""
import json, sys
sys.path.insert(0, 'output/artifacts')
from kh_stepD import parse_pd, smoothing_data
from kh_stepG import build_differentials, sparse_rank
from collections import defaultdict

P = 1000000007

def nullspace_basis(rows, cols, d, P):
    # d: col->[(row,val)]; return list of vectors (len cols) spanning ker
    R = defaultdict(dict)
    for col, lst in d.items():
        for (r, v) in lst:
            R[r][col] = (R[r].get(col, 0) + v) % P
    piv = {}
    prow = {}
    for r in sorted(R):
        row = dict(R[r])
        for pc in sorted(piv):
            if pc in row:
                f = row[pc] * pow(piv[pc][0], P - 2, P) % P
                if f:
                    for cc, vv in piv[pc][1].items():
                        row[cc] = (row.get(cc, 0) - f * vv) % P
                    row.pop(pc, None)
        nz = {c: v % P for c, v in row.items() if v % P != 0}
        if not nz:
            continue
        c0 = min(nz)
        inv = pow(nz[c0], P - 2, P)
        row = {c: v * inv % P for c, v in nz.items()}
        piv[c0] = (1, row)
        prow[r] = (c0, row)
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * cols
        v[f] = 1
        for c0 in sorted(piv, reverse=True):
            s = 0
            for cc, vv in piv[c0][1].items():
                if cc != c0:
                    s = (s + vv * v[cc]) % P
            v[c0] = (-s) % P
        basis.append(v)
    return basis
