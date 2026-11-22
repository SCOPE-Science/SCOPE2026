#!/usr/bin/env python3
"""Check incidence identities and Jordan ranks without constructing the two-time-row wave."""
from check_matrix import incidence,rank_int_rows,matrix_product_rows

def run(s):
    b=incidence(s); p=s*s; l=s*s+s; n=p+l
    rows=[sum(b[i][j] <<(p+j) for j in range(l)) for i in range(p)]
    rows += [sum(b[i][j]<<i for i in range(p)) for j in range(l)]
    rho=rank_int_rows([sum(b[i][j]<<j for j in range(l)) for i in range(p)])
    mat=[1<<i for i in range(n)]
    ranks=[]
    for k in range(5):
       ranks.append(rank_int_rows(mat))
       mat=matrix_product_rows(mat,rows)
    if s%2:
        target=[n,2*p,2*p-1,2*p-2,2*p-2]
        assert rho==p
    else:
        target=[n,2*rho,s+1,0,0]
    assert ranks==target,(s,ranks,target)
    print('order',s,'incidence_rank',rho,'adjacency_power_ranks',ranks)
for s in (2,3,4,5):run(s)
print('PASS')
