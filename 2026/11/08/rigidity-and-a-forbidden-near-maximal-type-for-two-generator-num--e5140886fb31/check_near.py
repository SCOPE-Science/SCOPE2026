#!/usr/bin/env python3
"""Exact finite checks for near-maximal types in two-generator quotients."""
import math
import heapq


def quotient_generators(a, b, modulus):
    result = {a, b}
    for i in range(modulus):
        for j in range(modulus):
            if i + j and (i*a + j*b) % modulus == 0:
                result.add((i*a+j*b)//modulus)
    return sorted(result)


def independent_pf(a, b, modulus):
    generators = quotient_generators(a, b, modulus)
    multiplicity = generators[0]
    dist = [10**30]*multiplicity
    dist[0] = 0
    heap = [(0, 0)]
    while heap:
        value, residue = heapq.heappop(heap)
        if value != dist[residue]:
            continue
        for g in generators:
            nr = (residue+g) % multiplicity
            nv = value+g
            if nv < dist[nr]:
                dist[nr] = nv
                heapq.heappush(heap,(nv,nr))
    assert max(dist) < 10**30
    return sorted(w-multiplicity for w in dist if all(
        dist[(w+g)%multiplicity] <= w+g-multiplicity for g in generators))


def near_type(a_residue, b_residue, modulus):
    step = a_residue * pow(b_residue, -1, modulus) % modulus
    minimum = modulus+1
    count = 0
    for i in range(1,modulus+1):
        j = (a_residue-step*i-1) % modulus + 1
        if j < minimum:
            minimum = j
            count += 1
    return count


def pareto_pf(a,b,p):
    pts=[(i,j,(a*b-i*a-j*b)//p)
         for i in range(1,p+1) for j in range(1,p+1)
         if a*b>i*a+j*b and (a*b-i*a-j*b)%p==0]
    return sorted(z for i,j,z in pts if not any(
        (u<=i and v<=j and (u<i or v<j)) for u,v,_ in pts))


def run():
    exact = 0
    pairs_near = 0
    boundary_observed = 0
    for p in range(2,14):
        for a in range(p+1,66):
            for b in range(a+1,67):
                if math.gcd(a,b) != 1 or (a*b)//p > 2500:
                    continue
                actual = independent_pf(a,b,p)
                predicted = pareto_pf(a,b,p)
                assert actual == predicted, ('pareto error',a,b,p,actual,predicted)
                exact += 1
                if min(a,b)>=2*p+1 and math.gcd(a*b,p)==1:
                    t = near_type(a%p,b%p,p)
                    assert len(actual) == t,(a,b,p,actual,t)
                    pairs_near += 1
    for p in range(5,101):
        units = [r for r in range(1,p) if math.gcd(r,p)==1]
        for r in units:
            for s in units:
                t = near_type(r,s,p)
                for n in range((p-2)//3+1):
                    # Here 3*n+2 <= p, including p=5 and n=1.
                    if 3*n+2>p:
                        continue
                    predicted = (r == s == (1-n)%p)
                    assert (t==p-n)==predicted,(p,r,s,n,t,predicted)
                    boundary_observed += 1
    for p in range(5,301):
        # Check one explicit infinite-family witness in every allowed class.
        for n in range((p-2)//3+1):
            r=(1-n)%p
            if math.gcd(r,p)!=1:
                continue
            assert near_type(r,r,p)==p-n,(p,n,r)
    print('EXACT_FINITE_CHECKS_PASS')
    print('independent_Dijkstra_vs_Pareto_cases=',exact)
    print('Dijkstra_vs_affine_record_cases=',pairs_near)
    print('near_maximal_residue_comparisons=',boundary_observed)
    print('moduli_near_comparison=5..100_all_units')
    print('witness_moduli=5..300')
    print('all_checks=PASS')

if __name__=='__main__':
    run()
