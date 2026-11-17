"""Exact independent checks for Euclidean vertex radii of K_{2,q} graphical zonotopes."""
from collections import Counter
from itertools import product
from math import factorial, comb
from fractions import Fraction


def formula(q):
    out = Counter()
    for a in range(q+1):
        for b in range(q-a+1):
            c = q-a-b
            d = a-b
            two_radius_sq = d*d+c*c+2*(a+b)
            ways = factorial(q)//(factorial(a)*factorial(b)*factorial(c))
            out[two_radius_sq] += ways*(2 if c>0 else 1)
    return out


def independent_orientation_enumeration(q):
    out = Counter()
    # Independent directed-graph Kahn test, without assuming the three-state classification.
    for edgesigns in product([-1, 1], repeat=2*q):
        n=q+2
        successors=[[] for _ in range(n)]
        indegree=[0]*n
        outdegree=[0]*n
        for leaf in range(q):
            for hub in range(2):
                sign=edgesigns[2*leaf+hub]
                u,v=(hub,leaf+2) if sign==1 else (leaf+2,hub)
                successors[u].append(v)
                outdegree[u]+=1
                indegree[v]+=1
        pending=indegree.copy()
        queue=[v for v in range(n) if pending[v]==0]
        head=0
        while head<len(queue):
            u=queue[head]
            head+=1
            for v in successors[u]:
                pending[v]-=1
                if pending[v]==0:
                    queue.append(v)
        if head!=n:
            continue
        twice_coordinates=[outdegree[v]-indegree[v] for v in range(n)]
        squared_radius_twice=sum(t*t for t in twice_coordinates)//2
        assert sum(t*t for t in twice_coordinates)%2 == 0
        out[squared_radius_twice]+=1
    return out


def min_count(q):
    if q%2:
        m=(q-1)//2
        return q-Fraction(1,2), 2*factorial(q)//(factorial(m)**2)
    m=q//2
    count=comb(q,m) + 4*factorial(q)//(factorial(m)*factorial(m-1)) + factorial(q)//(factorial(m-1)**2)
    return q,count


def expected_exact(q):
    three_to_q=3**q; two_to_q=2**q
    expectation_ternary=Fraction(q*q,18)+Fraction(10*q,9)
    expectation_binary=Fraction(3*q,2)
    return (2*three_to_q*expectation_ternary - two_to_q*expectation_binary)/(2*three_to_q-two_to_q)


def run():
    tot=0
    for q in range(2,9):
        calc=independent_orientation_enumeration(q)
        theory=formula(q)
        assert calc==theory,(q,calc,theory)
        assert sum(theory.values())==2*3**q-2**q
        low,lc=min_count(q)
        assert Fraction(min(calc),2)==low and calc[min(calc)]==lc,(q,calc,min_count(q))
        assert Fraction(max(calc),2)==Fraction(q*(q+2),2)
        assert calc[max(calc)]==2
        actual_mean=Fraction(sum(Fraction(k,2)*count for k,count in calc.items()),sum(calc.values()))
        assert actual_mean==expected_exact(q),(q,actual_mean,expected_exact(q))
        tot+=sum(calc.values())
    for q in range(2,151):
        theory=formula(q)
        low,lc=min_count(q)
        assert Fraction(min(theory),2)==low and theory[min(theory)]==lc
        assert max(theory)==q*(q+2) and theory[max(theory)]==2
        assert sum(theory.values())==2*3**q-2**q
        assert Fraction(sum(k*count for k,count in theory.items()),2*sum(theory.values()))==expected_exact(q)
    print(f'K2Q_RADIAL_PASS independently_enumerated_dimensions=2..8 independently_enumerated_vertices={tot} symbolic_dimensions=2..150')

if __name__=='__main__': run()
