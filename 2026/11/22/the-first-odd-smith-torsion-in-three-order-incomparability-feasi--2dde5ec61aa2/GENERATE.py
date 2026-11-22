#!/usr/bin/env python3
"""Construct exact elementary-unimodular certificates for fixed small grids."""
import json
from VERIFY import kernel, apply

def reduce(n):
    A=kernel(n); m=len(A); p=0; ops=[]
    def move(op):
        apply(A,op);ops.append(op)
    while p < m:
        nz=[(abs(A[i][j]),i,j) for i in range(p,m) for j in range(p,m) if A[i][j]]
        if not nz:break
        value,i,j=min(nz)
        assert all(A[a][b]%value==0 for a in range(p,m) for b in range(p,m))
        if i!=p:move(['S',p,i,0])
        if j!=p:move(['T',p,j,0])
        if A[p][p]<0:move(['N',p,0,-1])
        assert A[p][p]==value
        for i in range(p+1,m):
            if A[i][p]:
                assert A[i][p]%value==0
                move(['R',i,p,-A[i][p]//value])
        for j in range(p+1,m):
            if A[p][j]:
                assert A[p][j]%value==0
                move(['C',j,p,-A[p][j]//value])
        p+=1
    diag=[A[i][i] for i in range(m)]
    assert all(A[i][j]==0 for i in range(m) for j in range(m) if i!=j)
    assert diag[:p]==sorted(diag[:p])
    return {'n':n,'target_diagonal':diag,'operations':ops}

if __name__=='__main__':
    data={'schema':'elementary-unimodular-operations-v1','cases':[reduce(n) for n in (1,2,3)]}
    with open('CERTIFICATE.json','w',encoding='utf-8') as f:json.dump(data,f,separators=(',',':'),ensure_ascii=False)
    print([ (a['n'], len(a['operations']),a['target_diagonal'].count(1)) for a in data['cases']])
