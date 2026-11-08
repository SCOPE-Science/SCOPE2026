#!/usr/bin/env python3
"""Exact rational independent tests of sharp finite-tree Haar endpoint envelopes.

Run with Python 3; no third-party packages.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def leaves(weights):
    # weights maps each internal node tuple to the probability of left child
    d=max(map(len,weights))+1 if weights else 0
    return [tuple(x) for x in product((0,1),repeat=d)]


def mass(path, weights):
    v=F(1)
    for j,b in enumerate(path):
        p=weights[path[:j]]
        v*=p if b==0 else 1-p
    return v


def haar(node, x, weights):
    if x[:len(node)]!=node: return F(0)
    p=weights[node]
    m=mass(node,weights)
    # basis vector normalized in L2:  on left sqrt((1-p)/(p*m)),
    # on right -sqrt(p/((1-p)*m)); products avoid square roots
    return (1-p)/(p*m) if x[len(node)]==0 else p/((1-p)*m)


def kernel_entry(x,y,weights, signs):
    # direct orthogonal projections using normalized Haar products
    k=F(signs["__constant__"])
    for node in weights:
        if x[:len(node)]!=node or y[:len(node)]!=node:continue
        p=weights[node];m=mass(node,weights)
        bx=x[len(node)];by=y[len(node)]
        if bx==by==0: z=(1-p)/(p*m)
        elif bx==by==1:z=p/((1-p)*m)
        else:z=-1/m
        k+=signs[node]*z
    return k


def exact_matrix_norm(weights):
    X=leaves(weights);nodes=["__constant__"]+list(weights)
    masses={x:mass(x,weights) for x in X}
    best=F(0)
    for es in product((-1,1),repeat=len(nodes)):
        signs=dict(zip(nodes,es))
        val=max(sum(masses[y]*abs(kernel_entry(x,y,weights,signs)) for y in X) for x in X)
        best=max(best,val)
    return best


def row_path_value(path,weights):
    best=F(0)
    for signs in product((-1,1),repeat=len(path)):
        t=F(1);score=F(0)
        for j,(b,e) in enumerate(zip(path,signs)):
            prob=weights[path[:j]]
            p=prob if b==0 else 1-prob
            score+=(1-p)*(1-e*t)
            t=p*t+(1-p)*e
        best=max(best,score+abs(t))
    return best


def envelope(rs):
    a=F(0);b=F(1)
    for r in reversed(rs):
        a+=(1-r)*(1+b)
        b=(1-r)-r*b
    return a+b


def check():
    rng=Random(10619)
    cnt=0
    for d in range(1,4):
        for k in range(13):
            weights={node:F(rng.randint(1,9),10) for level in range(d) for node in product((0,1),repeat=level)}
            x=leaves(weights)
            direct=exact_matrix_norm(weights)
            via=max(row_path_value(path,weights) for path in x)
            assert direct==via,(d,weights,direct,via)
            rs=[]
            for level in range(d):
                rs.append(min(min(weights[node],1-weights[node]) for node in weights if len(node)==level))
            assert via<=envelope(rs),(d,weights,via,rs,envelope(rs))
            cnt+=1
    print('EXACT_FULL_HAAR_MATRIX_ROW_COMPARISONS_PASSED',cnt)

    cnt=0
    for d in range(1,9):
        for k in range(30):
            rs=[F(rng.randint(1,5),10) for _ in range(d)]
            best=F(0)
            for es in product((-1,1),repeat=d):
                t=F(1);v=F(0)
                for p,e in zip(rs,es):
                    v+=(1-p)*(1-e*t)
                    t=p*t+(1-p)*e
                best=max(best,v+abs(t))
            assert best==envelope(rs),(rs,best,envelope(rs))
            cnt+=1
    print('EXACT_PRODUCT_ENVELOPE_EQUALITY_CHECKS_PASSED',cnt)

    cnt=0
    for d in range(1,10):
        fair=envelope([F(1,2)]*d)
        for j in range(1,d+1):
            c=F(4,9)*(2+F(-1,2)**(j-1))*(2+F(-1,2)**(d-j))
            for r in (F(1,10),F(1,4),F(2,5)):
                rs=[F(1,2)]*d;rs[j-1]=r
                expected=fair+c*(F(1,2)-r)
                assert envelope(rs)==expected,(d,j,r,envelope(rs),expected)
                cnt+=1
    print('EXACT_SINGLE_NODE_BIAS_STABILITY_COEFFICIENTS_PASSED',cnt)

    cnt=0
    for d in range(1,4):
        for j in range(1,d+1):
            for v in product((0,1), repeat=j-1):
                weights={node:F(1,2) for level in range(d) for node in product((0,1),repeat=level)}
                weights[v]=F(1,4)
                c=F(4,9)*(2+F(-1,2)**(j-1))*(2+F(-1,2)**(d-j))
                assert exact_matrix_norm(weights)==envelope([F(1,2)]*d)+c*F(1,4)
                cnt+=1
    print('EXACT_FULL_MATRIX_SINGLE_BIAS_CASES_PASSED',cnt)

    w={():F(1,4),(0,):F(1,2),(1,):F(1,10)}
    scores={x:row_path_value(x,w) for x in leaves(w)}
    assert scores == {(0,0):F(5,2),(0,1):F(5,2),(1,0):F(27,10),(1,1):F(11,10)}
    assert exact_matrix_norm(w)==F(27,10)
    print('MAJORITY_FIRST_BRANCH_COUNTEREXAMPLE_PASSED',scores)
    print('ALL_NONHOMOGENEOUS_TREE_HAAR_CHECKS_PASSED')

if __name__=='__main__':check()
