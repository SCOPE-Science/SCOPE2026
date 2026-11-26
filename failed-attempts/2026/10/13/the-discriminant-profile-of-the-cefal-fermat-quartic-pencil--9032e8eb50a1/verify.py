#!/usr/bin/env python3
from itertools import combinations, product
from math import comb

def grad(z, t):
    S=sum(a*a for a in z)
    return [4*a*(S+t*a*a) for a in z]

def affine_hessian(rep3, k):
    # For f=(1+x^2+y^2+z^2)^2-k(1+x^4+y^4+z^4),
    # H_ii=4S+(8-12k)x_i^2 and H_ij=8x_ix_j.
    S=1+sum(a*a for a in rep3)
    H=[]
    for i,a in enumerate(rep3):
        row=[]
        for j,b in enumerate(rep3):
            if i==j:
                row.append(4*S+(8-12*k)*a*a)
            else:
                row.append(8*a*b)
        H.append(row)
    return H

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

expected_counts={1:4,2:12,3:16,4:8}
expected_dets={1:64,2:-512,3:2304,4:-8192}
for k in range(1,5):
    pts=[]
    for supp in combinations(range(4),k):
        first=supp[0]
        rest=supp[1:]
        for signs in product((1,-1), repeat=k-1):
            z=[0,0,0,0]
            z[first]=1
            for idx,sgn in zip(rest,signs): z[idx]=sgn
            pts.append(tuple(z))
    assert len(pts)==comb(4,k)*2**(k-1)==expected_counts[k]
    for z in pts:
        assert grad(z,-k)==[0,0,0,0]
        S=sum(a*a for a in z); Q=sum(a**4 for a in z)
        assert S==k and Q==k
        assert S*S-k*Q==0
        assert Q!=0  # parameter direction smooths this node to first order
    # Representative with fourth homogeneous coordinate 1.
    rep3=tuple([1]*(k-1)+[0]*(4-k))
    d=det3(affine_hessian(rep3,k))
    assert d==expected_dets[k] and d!=0
assert sum(expected_counts.values())==40
assert 4*3**3==108
assert 108-sum(expected_counts.values())==68
assert 68+4+12+16+8==108
print('VERIFY_OK')
