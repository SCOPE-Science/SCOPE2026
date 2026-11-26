#!/usr/bin/env python3
"""Standalone finite checks for zero forcing in cubed equal-arm spiders."""
from itertools import combinations
from math import cos, pi, sin

def graph(m, ell):
    n = 1 + m*ell
    edges = [set() for _ in range(n)]
    for arm in range(m):
        for depth in range(1, ell+1):
            v = 1 + arm*ell + depth - 1
            w = 0 if depth == 1 else v-1
            edges[v].add(w)
            edges[w].add(v)
    return edges

def distances(E):
    out = []
    for s in range(len(E)):
        d = [-1]*len(E)
        d[s] = 0
        q = [s]
        for v in q:
            for w in E[v]:
                if d[w] == -1:
                    d[w] = d[v]+1
                    q.append(w)
        out.append(d)
    return out

def force(E, selected):
    black = set(selected)
    while True:
        new = set()
        for v in black:
            W = E[v] - black
            if len(W) == 1:
                new.update(W)
        if not new: break
        black |= new
    return len(black)==len(E)

def cube(E):
    d = distances(E)
    return [{j for j in range(len(E)) if 0 < d[i][j] <= 3} for i in range(len(E))], d

def check_spectral(m, ell):
    E = graph(m, ell)
    n = len(E)
    d = distances(E)
    alpha = [2*cos(j*pi/(ell+1)) for j in range(1,4)]
    s1 = sum(alpha)
    s2 = alpha[0]*alpha[1]+alpha[0]*alpha[2]+alpha[1]*alpha[2]
    s3 = alpha[0]*alpha[1]*alpha[2]
    # A^3 entries count 3-walks; A^2 entries count 2-walks.
    A2 = [[len(E[u]&E[v]) for v in range(n)] for u in range(n)]
    A3 = [[sum(A2[u][w] for w in E[v]) for v in range(n)] for u in range(n)]
    for u in range(n):
        for v in range(n):
            val = (A3[u][v] -s1*A2[u][v] + s2*int(v in E[u]) -s3*int(u==v))
            if u != v:
                assert (abs(val)>1e-7)==(1<=d[u][v]<=3),(m,ell,u,v,d[u][v],val)
    for j in range(1,4):
        lam=alpha[j-1]
        for arm in range(m-1):
            v=[0.0]*n
            for dep in range(1,ell+1):
                x=sin(dep*j*pi/(ell+1))
                v[1+arm*ell+dep-1]=x
                v[1+(m-1)*ell+dep-1]=-x
            Av=[sum(v[w] for w in E[u]) for u in range(n)]
            assert max(abs(Av[u]-lam*v[u]) for u in range(n))<1e-8
    return s1,s2

def main():
    brute_cases=[]
    witness_cases=0
    spectral_cases=0
    for m in range(2,7):
        for ell in range(4,12):
            E=graph(m,ell)
            powE,_=cube(E)
            # Standard upper-bound seed: three outermost vertices on m-1 arms.
            B={1+arm*ell+dep-1 for arm in range(m-1) for dep in (ell-2,ell-1,ell)}
            assert len(B)==3*(m-1)
            assert force(powE,B),(m,ell,'seed')
            witness_cases+=1
            s1,s2=check_spectral(m,ell)
            assert s1>0 and s2>-2
            spectral_cases+=1
            if (m==2 and ell<=7) or (m==3 and ell<=6) or (m==4 and ell==4):
                goal=3*(m-1)
                n=len(E)
                for z in range(goal):
                    for S in combinations(range(n),z):
                        assert not force(powE,S),(m,ell,z,S)
                brute_cases.append((m,ell,n,goal))
    print('ZERO_FORCING_CUBE_SPIDER_VERIFY_OK')
    print('upper_seed_cases',witness_cases)
    print('spectral_support_and_eigenspace_cases',spectral_cases)
    print('brute_smaller_sets_cases',brute_cases)
    print('finite_checks_not_a_substitute_for_all_parameter_proof')

if __name__=='__main__': main()
