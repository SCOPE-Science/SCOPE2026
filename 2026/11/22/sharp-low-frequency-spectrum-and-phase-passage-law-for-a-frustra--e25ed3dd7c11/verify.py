"""Independent exact small-volume checks for a triangular three-part spin model.
Python 3 standard library only. Run: python verify.py
"""
from itertools import product
from fractions import Fraction
from math import comb


def exact_linear(A, b):
    n = len(A)
    a = [[Fraction(x) for x in row] + [Fraction(b[i])] for i,row in enumerate(A)]
    for c in range(n):
        pivot = next((r for r in range(c,n) if a[r][c]), None)
        if pivot is None: raise AssertionError('singular system')
        a[c],a[pivot] = a[pivot],a[c]
        p=a[c][c]
        for j in range(c,n+1): a[c][j]/=p
        for r in range(c+1,n):
            m=a[r][c]
            if m:
                for j in range(c,n+1): a[r][j]-=m*a[c][j]
    x=[Fraction(0)]*n
    for i in range(n-1,-1,-1):
        x[i]=a[i][n]-sum(a[i][j]*x[j] for j in range(i+1,n))
    return x


def check(n):
    all_states=list(product((-1,1),repeat=3*n))
    def energy(s):
        a,b,c=(sum(s[i*n:(i+1)*n]) for i in range(3))
        return a*b+b*c+c*a
    mine=min(map(energy,all_states))
    assert mine == -n*n
    states=[s for s in all_states if energy(s)==mine]
    assert len(states)==6*(2**n-1)
    idx={s:i for i,s in enumerate(states)}
    neighbors=[]
    for s in states:
        adj=[]
        for j in range(3*n):
            t=list(s);t[j]*=-1;t=tuple(t)
            if t in idx:
                adj.append(idx[t]);assert energy(t)==energy(s)
        neighbors.append(adj)
    # All allowed moves have zero energy and flip rate 1/2.
    corners=[s for s in states if all(abs(sum(s[k*n:(k+1)*n]))==n for k in range(3))]
    assert len(corners)==6
    # Every ground state is in a free-part hypercube; every endpoint belongs to two.
    for s in states:
        ms=[sum(s[k*n:(k+1)*n]) for k in range(3)]
        assert any(ms[a]==n and ms[b]==-n for a in range(3) for b in range(3) if a!=b)
    # Connect two fully polarized ground states if they differ on exactly one entire part.
    corner_adj={i:[j for j in range(6) if i!=j and sum(corners[i][k]!=corners[j][k] for k in range(3*n))==n] for i in range(6)}
    assert all(len(corner_adj[i])==2 for i in range(6))
    # Fix source corner, find d by traversing the six-corner cycle.
    source=0
    depths={source:0};queue=[source]
    for i in queue:
        for j in corner_adj[i]:
            if j not in depths:depths[j]=depths[i]+1;queue.append(j)
    assert sorted(depths.values())==[0,1,1,2,2,3]
    S=sum((Fraction(1,comb(n-1,k)) for k in range(n)),Fraction(0))
    hits=0
    for d in (1,2,3):
        target_j=next(j for j in range(6) if depths[j]==d)
        target=idx[corners[target_j]]
        remaining=[i for i in range(len(states)) if i!=target]
        pos={state:j for j,state in enumerate(remaining)}
        A=[]
        for i in remaining:
            row=[Fraction(0)]*len(remaining)
            row[pos[i]]=Fraction(len(neighbors[i]),2)
            for j in neighbors[i]:
                if j!=target:row[pos[j]]-=Fraction(1,2)
            A.append(row)
        times=exact_linear(A,[1]*len(remaining))
        observed=times[pos[idx[corners[source]]]]
        expected=Fraction((2**n-1)*d*(6-d),n)*S
        assert observed==expected,(n,d,observed,expected)
        hits+=1
    return len(states),hits

if __name__=='__main__':
    total=0
    for n in (1,2,3):
        states,hits=check(n);total+=hits
        print('n=',n,'states=',states,'corner-distances checked=',hits)
    print('EXACT_GROUND_WALK_CHECKS_PASSED',total)
