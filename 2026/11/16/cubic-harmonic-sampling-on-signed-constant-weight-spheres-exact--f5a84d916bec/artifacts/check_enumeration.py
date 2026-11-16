#!/usr/bin/env python3
"""Independent direct sign-support enumeration; uses NumPy only for matrix products."""
from itertools import combinations, product
from math import comb
import numpy as np

def cubic_rows(d):
    out=[]
    for i in range(d): out.append(('Z',i))
    for i in range(d):
        others=[j for j in range(d) if j!=i]
        for j in others[:-1]:out.append(('T',i,j,others[-1]))
    for a,b,c in combinations(range(d),3):out.append(('S',a,b,c))
    return out

def evaluate(desc,v):
    if desc[0]=='Z':
        _,i=desc
        return (len(v)+2)*v[i]**3-3*v[i]*sum(x*x for x in v)
    if desc[0]=='T':
        _,i,j,r=desc
        return v[i]*(v[j]*v[j]-v[r]*v[r])
    _,a,b,c=desc
    return v[a]*v[b]*v[c]

def moment_norm(desc,d):
    # Unit sphere exact L2 norms of integral-coefficient cubics.
    den=d*(d+2)*(d+4)
    if desc[0]=='Z':return 6*(d-1)/(d*(d+4))
    if desc[0]=='T':return 4/den
    return 1/den

def formula(d,k):
    z=(d+4)*(d+2-3*k)**2/(6*k*k*(d-1))
    t=(k-1)*(d-k)*(d+2)*(d+4)/(2*k*k*(d-1)*(d-2))
    s=(k-1)*(k-2)*(d+2)*(d+4)/(k*k*(d-1)*(d-2))
    return z,t,s

def main():
    for d,k in [(3,1),(3,2),(4,3),(5,3),(5,4),(6,3),(7,3),(7,4)]:
        B=cubic_rows(d)
        rows=[]
        for support in combinations(range(d),k):
            for signs in product([-1,1],repeat=k):
                v=np.zeros(d,dtype=np.int64)
                v[list(support)]=signs
                rows.append([evaluate(desc,v) for desc in B])
        M=np.asarray(rows,dtype=np.float64)
        G=M.T@M/(len(rows)*k**3)
        vals=[]
        for kind in ('Z','T','S'):
            inds=[j for j,q in enumerate(B) if q[0]==kind]
            samples=[G[j,j]/moment_norm(B[j],d) for j in inds]
            vals.append(samples)
        expected=formula(d,k)
        for seq,pred in zip(vals,expected):
            assert max(abs(x-pred) for x in seq)<1e-10, (d,k,seq,pred)
        if (d,k)==(7,3):
            assert all(abs(G[i,j])<1e-12 for i in range(d) for j in range(len(B)))
        print(d,k,'direct orbit points',len(rows),'multiplicities',tuple(len(seq) for seq in vals),'eigenvalues',tuple(round(x,10) for x in expected))
    print('ALL_DIRECT_ENUMERATION_CHECKS_PASS')
if __name__=='__main__':main()
