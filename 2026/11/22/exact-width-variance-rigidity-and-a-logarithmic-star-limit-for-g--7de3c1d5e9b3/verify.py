#!/usr/bin/env python3
"""Finite diagnostic checks for Euclidean spherical widths of graph-indexed disk sums.
Run: python3 verify.py. Standard-library only. Analytic theorems are in RESULT.md.
"""
import itertools
import math
import random
from collections import Counter

MU = math.sqrt(math.pi / 2.0)

def simpson(f, a, b, N=600):
    assert N > 0 and N % 2 == 0
    h = (b-a)/N
    v = f(a)+f(b)
    for j in range(1,N):
        v += (4 if j % 2 else 2)*f(a+j*h)
    return v*h/3

def f_abs(x):
    return math.sqrt(2/math.pi)*simpson(lambda z: math.hypot(x,z)*math.exp(-z*z/2),0,11,600)

def shared_covariance():
    second = math.sqrt(2/math.pi)*simpson(lambda x:f_abs(x)**2*math.exp(-x*x/2),0,11,600)
    return second - MU**2

C = shared_covariance()
assert 0.2087 < C < 0.2090, C

def radial_mean(n):
    return math.sqrt(2)*math.exp(math.lgamma((n+1)/2)-math.lgamma(n/2))

def moments(n, edges):
    m=len(edges)
    degree=Counter(v for e in edges for v in e)
    q=sum(v*(v-1)//2 for v in degree.values())
    mean=2*m*MU/radial_mean(n)
    second=4/n*(2*m+MU**2*m*(m-1)+2*C*q)
    return mean,second,second-mean**2,q

def check_tree_extremizers():
    count=0
    for n in range(3,8):
        best=(n-2)
        worst=(n-1)*(n-2)//2
        for prufer in itertools.product(range(n),repeat=n-2):
            counts=[1]*n
            for v in prufer: counts[v]+=1
            q=sum(d*(d-1)//2 for d in counts)
            assert best <= q <= worst, (n,prufer)
            assert (q==best)==(max(counts)<=2)
            assert (q==worst)==(max(counts)==n-1)
            count+=1
    return count

def monte_carlo(n,edges,samples=45000,seed=20261116):
    rng=random.Random(seed+1000*n+len(edges))
    total=0.0
    total_sq=0.0
    for _ in range(samples):
        g=[rng.gauss(0,1) for _ in range(n)]
        norm=math.sqrt(sum(z*z for z in g))
        w=2*sum(math.hypot(g[i],g[j]) for i,j in edges)/norm
        total+=w
        total_sq+=w*w
    return total/samples,total_sq/samples

def main():
    tested=0
    for n in range(4,9):
        examples={
            'path':[(i,i+1) for i in range(n-1)],
            'star':[(0,i) for i in range(1,n)],
            'cycle':[(i,(i+1)%n) for i in range(n)],
            'complete':[(i,j) for i in range(n) for j in range(i+1,n)]
        }
        for label,edges in examples.items():
            true_mean,true_second,_,_=moments(n,edges)
            mc_mean,mc_second=monte_carlo(n,edges)
            assert abs(mc_mean-true_mean) < 0.085,(n,label,'mean',true_mean,mc_mean)
            assert abs(mc_second-true_second) < 0.85,(n,label,'second',true_second,mc_second)
            tested+=1
    for n in range(4,30):
        p=[(i,i+1) for i in range(n-1)]
        s=[(0,i) for i in range(1,n)]
        gap=moments(n,s)[2]-moments(n,p)[2]
        assert abs(gap-(4*C*(n-2)*(n-3)/n))<1e-10
    total_trees=check_tree_extremizers()
    asymptotic_path=8-3*math.pi+8*C
    assert asymptotic_path>0
    print(f'DISCOTOPE_WIDTH_CHECK_PASS samples_per_graph=45000 graphs={tested} trees={total_trees} c={C:.10f} path_variance={asymptotic_path:.10f}')
if __name__=='__main__':main()
