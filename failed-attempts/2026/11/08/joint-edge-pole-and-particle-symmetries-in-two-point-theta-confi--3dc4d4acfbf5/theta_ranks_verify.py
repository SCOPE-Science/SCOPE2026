#!/usr/bin/env python3
"""Independent sparse exact finite-field rank checks for cellular boundary maps."""
from theta_character_verify import complex_data,boundary1,boundary2

def rank_sparse_mod(columns, row_map, p):
    pivots={}
    for c in columns:
        d={row_map[k]:v%p for k,v in c.items() if v%p}
        while d:
            r=max(d);a=d[r]
            if r not in pivots:
                inv=pow(a,-1,p)
                pivots[r]={k:v*inv%p for k,v in d.items() if v%p}
                break
            pc=pivots[r]
            for k,v in pc.items():
                w=(d.get(k,0)-a*v)%p
                if w:d[k]=w
                else:d.pop(k,None)
    return len(pivots)

for m in range(3,8):
    edges,C0,C1,C2=complex_data(m)
    r0={c:i for i,c in enumerate(C0)}
    r1={c:i for i,c in enumerate(C1)}
    for p in (2,3,5):
        a=rank_sparse_mod((boundary1(c,edges) for c in C1),r0,p)
        b=rank_sparse_mod((boundary2(c,edges) for c in C2),r1,p)
        assert a==len(C0)-1,(m,p,'rank_d1',a)
        assert b==len(C2),(m,p,'rank_d2',b)
        b1=len(C1)-a-b
        assert b1==m*m-m-1
        print('m',m,'prime',p,'rank_d1',a,'rank_d2',b,'b1',b1,'b2',len(C2)-b)
print('THETA_CELLULAR_BOUNDARY_RANK_CHECK_PASS')
