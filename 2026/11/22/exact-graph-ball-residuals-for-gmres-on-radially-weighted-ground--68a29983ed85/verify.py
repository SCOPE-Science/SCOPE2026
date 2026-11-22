#!/usr/bin/env python3
"""Exact rational GMRES checks for radially weighted grounded rooted trees.

No external packages. Run: python3 verify.py
"""
from fractions import Fraction
from itertools import product


def solve(M, y):
    n = len(y)
    T = [[Fraction(v) for v in row] + [Fraction(y[i])] for i, row in enumerate(M)]
    for j in range(n):
        p = next(i for i in range(j, n) if T[i][j] != 0)
        T[p], T[j] = T[j], T[p]
        v = T[j][j]
        for q in range(j, n+1): T[j][q] /= v
        for i in range(n):
            if i != j:
                v = T[i][j]
                if v:
                    for q in range(j, n+1): T[i][q] -= v*T[j][q]
    return [T[i][-1] for i in range(n)]


def run_case(branch, layer_weights, terminal_killing):
    H = len(branch)
    levels = [[0]]
    nbrs = [[]]
    for lev in range(H):
        nxt = []
        for parent in levels[-1]:
            for _ in range(branch[lev]):
                child = len(nbrs)
                nbrs.append([(parent, layer_weights[lev])])
                nbrs[parent].append((child, layer_weights[lev]))
                nxt.append(child)
        levels.append(nxt)
    n = len(nbrs)
    D = [sum(w for _, w in ns) + (terminal_killing if v in levels[-1] else 0) for v,ns in enumerate(nbrs)]
    def apply(x):
        return [D[v]*x[v]-sum(w*x[u] for u,w in nbrs[v]) for v in range(n)]
    b=[1]+[0]*(n-1)
    p=[b]
    for _ in range(H+1):p.append(apply(p[-1]))
    tests=0
    for k in range(H+1):
        ball=set().union(*[set(s) for s in levels[:k+1]])
        B=len(ball)
        target=[Fraction(1,B) if i in ball else Fraction(0) for i in range(n)]
        if k==0:
            residual=[Fraction(t) for t in b]
        else:
            cols=p[1:k+1]
            gram=[[sum(cols[i][v]*cols[j][v] for v in range(n)) for j in range(k)] for i in range(k)]
            rhs=[col[0] for col in cols]
            weights=solve(gram,rhs)
            residual=[Fraction(b[v])-sum(weights[j]*cols[j][v] for j in range(k)) for v in range(n)]
        assert residual==target,(branch,layer_weights,terminal_killing,k,residual,target)
        assert sum(a*a for a in residual)==Fraction(1,B)
        tests+=2
    cols=p[1:H+2]
    gram=[[sum(cols[i][v]*cols[j][v] for v in range(n)) for j in range(H+1)] for i in range(H+1)]
    y=solve(gram,[col[0] for col in cols])
    assert all(Fraction(b[v])==sum(y[j]*cols[j][v] for j in range(H+1)) for v in range(n))
    return tests+1


def main():
    tests=0;cases=0
    for H in range(1,6):
        for branch in product((1,2,3),repeat=H):
            count=1;shell=1
            for a in branch:
                shell*=a;count+=shell
            if count>80:continue
            for offset in range(3):
                weights=[1+((offset+2*j)%5) for j in range(H)]
                kill=1+offset*3
                tests+=run_case(branch,weights,kill)
                cases+=1
    for d in range(2,11):
        for k in range(21):
            B=1+d*sum((d-1)**j for j in range(k))
            if d==2:assert B==2*k+1
            else:assert B*(d-2)==(d-2)+d*((d-1)**k-1)
            tests+=1
    print(f"PASS: {tests} exact rational/integer assertions across {cases} weighted grounded trees")


if __name__=='__main__':main()
