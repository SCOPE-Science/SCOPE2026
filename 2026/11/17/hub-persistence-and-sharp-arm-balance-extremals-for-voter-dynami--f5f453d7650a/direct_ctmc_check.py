"""Independent labelled-state CTMC check for root persistence on spider trees."""
from fractions import Fraction
from itertools import product
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

def probability(arms):
    k=len(arms)
    N=sum(arms)
    if N>12: raise ValueError('Keep independent state space moderate')
    adj=[]
    gateways=[]
    ix=0
    for r in arms:
        gateways.append(ix)
        for j in range(r):
            nei = [-1] if j==0 else [ix+j-1]
            if j+1<r: nei.append(ix+j+1)
            adj.append(tuple(nei))
        ix+=r
    terminal=(1<<N)-1
    mat=lil_matrix((terminal,terminal),dtype=float)
    rhs=[0.0]*terminal
    for s in range(terminal):
        total=0.0
        for g in gateways:
            if (s>>g)&1 == 0: total+=1/k # hub copies an opposing gateway
        for u,neighbors in enumerate(adj):
            bit=(s>>u)&1
            for v in neighbors:
                nbit=1 if v==-1 else (s>>v)&1
                if nbit!=bit:
                    rate=1/len(neighbors)
                    total+=rate
                    target=s^(1<<u)
                    if target==terminal: rhs[s]+=rate
                    else: mat[s,target]-=rate
        mat[s,s]+=total
    vec=spsolve(mat.tocsr(),rhs)
    return float(vec[0])

def main():
    cases=[(1,),(2,),(3,),(4,),(5,), (1,1),(1,2),(2,2),(1,3),(2,3),(3,3),(1,1,2),(1,2,3),(2,2,2),(1,1,1,3),(1,2,2,2)]
    for arms in cases:
        k=len(arms)
        expected=Fraction(1)
        for r in arms:expected*=Fraction(k,k+2*r-1)
        observed=probability(arms)
        assert abs(observed-float(expected)) < 1e-10, (arms,observed,expected)
        print(f'arms={arms}: CTMC={observed:.12f}; exact={expected}')
    print('PASS: independent labelled-state CTMC on',len(cases),'spiders.')
if __name__=='__main__': main()
