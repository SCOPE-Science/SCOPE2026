#!/usr/bin/env python3
"""Exact finite-state checks for an affine fixation criterion in a partisan voter model.
All computations use only Python standard-library fractions and integer arithmetic.
This checker supplements, but does not substitute for, the all-graph proof.
"""
from fractions import Fraction as F
from itertools import product


def connected(n, edges):
    reach = {0}
    while True:
        newer = reach | {v for i,j in edges for u,v in ((i,j),(j,i)) if u in reach}
        if len(newer) == len(reach):
            return len(reach) == n
        reach = newer


def all_graphs(n):
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    for mask in range(1,1 << len(pairs)):
        e = [pair for k,pair in enumerate(pairs) if mask >> k & 1]
        if connected(n,e):
            yield e


def rates(bits, edges, bias):
    n = len(bits)
    deg = [0]*n
    neighbors = [[] for _ in bits]
    for i,j in edges:
        deg[i] += 1; deg[j] += 1
        neighbors[i].append(j); neighbors[j].append(i)
    q = {}
    for i in range(n):
        r = sum((F(1) + bias[i]*(2*bits[j]-1))/(2*deg[i]) for j in neighbors[i] if bits[j] != bits[i])
        if r:
            nxt = tuple((1-b if k==i else b) for k,b in enumerate(bits))
            q[nxt] = r
    return q


def derivative(bits, edges, bias, coeff):
    return sum((r*(sum(coeff[i]*(nxt[i]-bits[i]) for i in range(len(bits)))))
               for nxt,r in rates(bits,edges,bias).items())


def solve(M, rhs):
    a = [[F(z) for z in row] + [F(rhs[i])] for i,row in enumerate(M)]
    n = len(a)
    for k in range(n):
        pos = next((i for i in range(k,n) if a[i][k]),None)
        assert pos is not None
        a[k],a[pos] = a[pos],a[k]
        c = a[k][k]
        a[k] = [v/c for v in a[k]]
        for i in range(n):
            if i!=k and a[i][k]:
                c=a[i][k]
                a[i]=[x-c*y for x,y in zip(a[i],a[k])]
    return [r[-1] for r in a]


def fixation(n, edges, bias):
    zero, one = (0,)*n,(1,)*n
    transient = [s for s in product((0,1),repeat=n) if s not in (zero,one)]
    m = len(transient)
    rows, rhs = [], []
    for s in transient:
        q = rates(s,edges,bias)
        total = sum(q.values(),F(0))
        rows.append([(total if s==t else F(0))-q.get(t,F(0)) for t in transient])
        rhs.append(q.get(one,F(0)))
    vals = solve(rows,rhs)
    return {zero:F(0),one:F(1),**dict(zip(transient,vals))}


def main():
    checks=0; graph_count=0
    for n in range(2,6):
        for e in all_graphs(n):
            graph_count += 1
            deg = [sum(i in edge for edge in e) for i in range(n)]
            weight = [F(d, sum(deg)) for d in deg]
            # Algebraic edge test: alternating bias (if possible), arbitrary bias,
            # and zero bias. Direct generator and edge-polynomial formula must match.
            assignment = [None]*n
            assignment[0]=1
            conflict=False
            while True:
                altered=False
                for i,j in e:
                    if assignment[i] is not None and assignment[j] is None:
                        assignment[j]=-assignment[i]; altered=True
                    elif assignment[j] is not None and assignment[i] is None:
                        assignment[i]=-assignment[j]; altered=True
                    elif assignment[i] is not None and assignment[j] is not None and assignment[i]==assignment[j]:
                        conflict=True
                if not altered: break
            assert all(v is not None for v in assignment)
            cases = [[F(0)]*n, [F((-1)**i,3) for i in range(n)]]
            if not conflict: cases.append([F(v,3) for v in assignment])
            for h in cases:
                should_be_harmonic=all(h[i]+h[j]==0 for i,j in e)
                observed=True
                for s in product((0,1),repeat=n):
                    lhs=derivative(s,e,h,weight)
                    observed &= (lhs==0)
                    # Independent edge expansion in spin variables.
                    spin=[2*b-1 for b in s]
                    d=[weight[i]/deg[i] for i in range(n)]
                    algebra= sum((d[i]-d[j])*(spin[j]-spin[i])/4 +
                                 (d[i]*h[i]+d[j]*h[j])*(1-spin[i]*spin[j])/4 for i,j in e)
                    assert lhs==algebra
                    checks += 1
                assert observed==should_be_harmonic,(n,e,h)
    # Independently solve entire absorbing Markov chain, not just the generator.
    examples = [
        (2,[(0,1)]),
        (3,[(0,1),(1,2)]),
        (3,[(0,1),(1,2),(0,2)]),
        (4,[(0,1),(1,2),(2,3),(3,0)]),
        (4,[(0,1),(0,2),(0,3)]),
        (4,[(0,1),(1,2),(2,0),(2,3)]),
        (4,[(i,j) for i in range(4) for j in range(i+1,4)])
    ]
    chain_count=0
    for n,e in examples:
        degree = [sum(i in edge for edge in e) for i in range(n)]
        assignment=[None]*n;assignment[0]=1; conflict=False
        while True:
            change=False
            for i,j in e:
                if assignment[i] is not None and assignment[j] is None:
                    assignment[j]=-assignment[i];change=True
                elif assignment[j] is not None and assignment[i] is None:
                    assignment[i]=-assignment[j];change=True
                elif assignment[i] is not None and assignment[j] is not None and assignment[i]==assignment[j]:
                    conflict=True
            if not change: break
        biases=[[F(0)]*n,[F((-1)**i,3) for i in range(n)]]
        if not conflict:biases.append([F(v,2) for v in assignment])
        for h in biases:
            u=fixation(n,e,h)
            is_affine=all(h[i]+h[j]==0 for i,j in e)
            eq=all(v==sum(F(degree[i],sum(degree))*s[i] for i in range(n)) for s,v in u.items())
            assert eq==is_affine, (e,h,u)
            assert all(F(0)<=v<=F(1) for v in u.values())
            chain_count += 1
    print('VERIFY_OK graphs=%d generator_assertions=%d exact_absorption_chains=%d' % (graph_count,checks,chain_count))

if __name__=='__main__':main()
