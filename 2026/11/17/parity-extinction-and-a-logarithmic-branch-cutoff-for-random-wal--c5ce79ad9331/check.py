"""Exact rational diagnostics for edge variation of Markov powers on a balanced double star.

Run: python check.py. Requires only Python's standard library.
"""
from fractions import Fraction as F
from itertools import product


def graph(k):
    # Left hub 0, right hub 1, left leaves 2..k+1, right leaves k+2..2k+1.
    n = 2*k+2
    neighbors = [[] for _ in range(n)]
    edges = [(0, 1)] + [(0, j) for j in range(2, k+2)] + [(1, j) for j in range(k+2, n)]
    for a,b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)
    return neighbors,edges


def step(f, neighbors):
    return [sum((f[j] for j in nb), F(0)) / len(nb) for nb in neighbors]


def variation(f, edges):
    return sum((abs(f[a]-f[b]) for a,b in edges), F(0))


def cut(neighbors, edges, edge):
    # Piecewise constant 0/1 profile separated by one tree edge.
    a,b=edge
    comp={a};front=[a]
    while front:
        u=front.pop()
        for v in neighbors[u]:
            if {u,v}=={a,b} or v in comp:
                continue
            comp.add(v);front.append(v)
    return [F(int(i in comp)) for i in range(len(neighbors))]


def predicted(k,m):
    if m%2==0:
        return F(1)
    q=F(k,k+1)
    return 1+F(2,2*k+1)*max(F(0),2*k*q**m-1)


def bridge_column(k,m):
    q=F(k,k+1)
    d=2*k+1
    x=(q**m-(-1)**m)/d
    y=(2*k*q**m+(-1)**m)/d
    return 2*k*abs(x)+abs(y)


def leaf_column(k,m):
    if m==0:
        return F(1)
    q=F(k,k+1);d=2*k+1
    if m%2:
        x=-(1+q**m)/d
        z=-(1-q**(m-1))/d
        y=(1+q**m)/d
    else:
        x=(1+q**(m-1))/d
        z=(1-q**m)/d
        y=-(1-q**m)/d
    return k*(abs(x)+abs(z))+abs(y)


def main():
    cases=0
    for k in range(1,15):
        neighbors,edges=graph(k)
        signals=[cut(neighbors,edges,e) for e in edges]
        for m in range(0,65):
            vals=[variation(f,edges) for f in signals]
            assert all(v == 1 for v in vals[1:])
            expected=predicted(k,m)
            assert bridge_column(k,m)==(expected if m%2 else 1)
            assert leaf_column(k,m)==1
            assert max(vals)==expected,(k,m,max(vals),expected)
            signals=[step(f,neighbors) for f in signals]
            cases+=1
    print('EXACT_ALL_CUT_NORMS_AND_CLOSED_FORM_PASSED', cases)

    # Check full inequalities for signed input pairs, not just extremal cuts.
    tested=0
    for k in range(1,9):
        neighbors,edges=graph(k)
        n=len(neighbors)
        for seed in range(110):
            x=[F(((i*17+seed*29+11)%23)-11, 1+((3*i+seed)%4)) for i in range(n)]
            y=[F(((i*31+seed*7+19)%29)-14, 2+((i+seed)%5)) for i in range(n)]
            d=[a-b for a,b in zip(x,y)]
            denom=variation(d,edges)
            if denom==0:continue
            for m in range(0,14):
                assert variation(d,edges)<=predicted(k,m)*denom,(k,m,seed)
                d=step(d,neighbors)
                tested+=1
    print('EXACT_SIGNED_INPUT_STABILITY_PASSED',tested)

    # Direct verification of support and strictness of the finite odd-power window.
    thresholds=0
    for k in range(1,55):
        q=F(k,k+1)
        prev=F(2*k)
        for m in range(1,1500,2):
            amplification=predicted(k,m)
            assert (amplification>1)==(F(2*k)*q**m>1)
            if amplification>1:
                thresholds+=1
            else:
                break
    print('EXACT_ODD_POWER_THRESHOLD_TESTS_PASSED',thresholds)
    print('ALL_BALANCED_DOUBLE_STAR_VARIATION_TESTS_PASSED')

if __name__=='__main__':
    main()
