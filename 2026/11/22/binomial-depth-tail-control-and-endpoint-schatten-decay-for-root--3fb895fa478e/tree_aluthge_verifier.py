"""Finite-tree diagnostics for the rooted-tree Aluthge Schatten bound.

Run: python3 tree_aluthge_verifier.py
All tests are finite diagnostics, not a substitute for the infinite proof.
Uses only Python's standard library.
"""
import math
import random

RNG = random.Random(20261105)
CHECKS = 0


def verify(condition, message):
    global CHECKS
    if not condition:
        raise AssertionError(message)
    CHECKS += 1


def parent_norms(children, edge):
    return [math.sqrt(sum(abs(edge[u]) ** 2 for u in branch)) for branch in children]


def aluthge_step(parent, rho, edge, t):
    out = [0j]
    for u in range(1, len(parent)):
        v = parent[u]
        out.append(edge[u] * (rho[u] / rho[v]) ** t if rho[v] else 0j)
    return out


def binomial_cdf_leq_depth(n, t, d):
    if d >= n:
        return 1.0
    return sum(math.comb(n, k) * t ** k * (1 - t) ** (n-k)
               for k in range(d+1))


def test_tree(parent, edge):
    count = len(parent)
    children = [[] for _ in range(count)]
    depth = [0] * count
    for u in range(1, count):
        children[parent[u]].append(u)
        depth[u] = depth[parent[u]] + 1

    for t in (0.17, 0.5, 0.83):
        for p in (0.5, 1.0, 2.0, 4.0):
            cur = edge[:]
            rho_initial = parent_norms(children, cur)
            a_initial = [x**p for x in rho_initial]
            for n in range(14):
                rho = parent_norms(children, cur)
                energy = sum(x**p for x in rho)
                rhs = sum(a_initial[u] * binomial_cdf_leq_depth(n,t,depth[u])
                          for u in range(count))
                verify(energy <= rhs + 1e-9*(1+rhs),
                       ('depth bound', n,t,p,energy,rhs))
                if n:
                    verify(energy <= previous + 1e-9*(1+previous),
                           ('monotonicity',n,t,p))
                if n==0:
                    verify(abs(energy-rhs)<1e-9*(1+rhs),'initial equality')
                if n==1:
                    # Direct matrix formula: |W| has diagonal rho, while
                    # U maps parent v to its normalized vector of children.
                    for u in range(1,count):
                        v=parent[u]
                        polar=(edge[u]/rho_initial[v] if rho_initial[v] else 0j)
                        direct=(rho_initial[u]**t)*polar*(rho_initial[v]**(1-t))
                        expected=edge[u]*(rho_initial[u]/rho_initial[v])**t if rho_initial[v] else 0j
                        verify(abs(direct-expected)<1e-10,('polar',u,direct,expected))
                previous = energy
                cur = aluthge_step(parent,rho,cur,t)
    

def nonuniform_path(L,n,p,t):
    c=L**(-1.0/p)
    parent=[-1]+[k-1 for k in range(1,L+1)]
    children=[[] for _ in range(L+1)]
    for u in range(1,L+1): children[u-1].append(u)
    edge=[0j]+[complex(c)]*L
    for _ in range(n):
        rho=parent_norms(children,edge)
        edge=aluthge_step(parent,rho,edge,t)
    energy=sum(x**p for x in parent_norms(children,edge))
    verify(abs(energy-(L-n)/L)<1e-10,('path',L,n,p,t,energy))


def main():
    for _ in range(65):
        count=RNG.randrange(4,22)
        parent=[-1]+[RNG.randrange(u) for u in range(1,count)]
        edge=[0j]+[complex(RNG.uniform(-1,1),RNG.uniform(-1,1))
                    if RNG.randrange(7) else 0j for _ in range(1,count)]
        test_tree(parent,edge)
    for n in (1,3,10):
        for p in (0.5,1,2,4):
            for t in (0.17,0.5,0.83):
                nonuniform_path(300,n,p,t)
    print('ROOTED_ALUTHGE_DEPTH_DIAGNOSTICS_OK', CHECKS)


if __name__=='__main__':
    main()
