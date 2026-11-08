"""Exact finite certificate for squarefree four-prime 3-near-perfect classification.

Run: python3 check.py (standard library only).
The finite search is exhaustive because of the separate prime bounds in RESULT.md.
"""
from itertools import combinations
from math import isqrt

EXPECTED = (210,330,390,510,570,690,770,798,858,910,1190,1302,1430,1554,1610,
1806,1938,2002,2010,2090,2130,2210,2530,2590,2870,2990,3010,3230,
3290,3354,3738,3770,4026,4070,4510,4686,4690,4970,5110,5170,5538,
6474,6942,7490,8034,8890,9590,9906,10842,11622,12714)

def prime(t):
    if t < 2: return False
    for d in range(2, isqrt(t)+1):
        if t % d == 0: return False
    return True

def theorem_certificate():
    solutions = {}
    tested_pairs = 0
    candidate_templates = 0
    for p in (3,5,7):
        for q in range(p+1, 24):
            if not prime(q) or (p==5 and q>17) or (p==7 and q != 11):
                continue
            tested_pairs += 1
            A = -p*q + 3*p + 3*q + 3
            B = 3*(p+1)*(q+1)
            basic = (1,2,p,2*p,q,2*q,p*q,2*p*q)
            templates = tuple((0,d) for d in basic) + tuple((d,0) for d in basic if d!=2*p*q)
            assert len(templates)==len(set(templates))==15
            for combo in combinations(templates,3):
                candidate_templates += 1
                C = sum(t[0] for t in combo)
                E = sum(t[1] for t in combo)
                assert E < B  # rules out the exceptional denominator A-C=0
                if A == C: continue
                num, den = E-B, A-C
                if num % den: continue
                r = num // den
                if r <= q or not prime(r): continue
                n=2*p*q*r
                excluded = tuple(sorted(a*r+b for a,b in combo))
                assert excluded[0] >= 1 and len(set(excluded))==3
                assert all(d < n and n % d == 0 for d in excluded)
                assert sum(excluded) == 3*(p+1)*(q+1)*(r+1) - 2*n
                solutions.setdefault(n,set()).add(excluded)
    assert tuple(sorted(solutions))==EXPECTED
    assert len(solutions)==51
    assert sum(map(len,solutions.values()))==60
    assert tested_pairs == 12, tested_pairs
    assert candidate_templates == tested_pairs*455
    assert max(solutions)==12714
    return solutions, tested_pairs, candidate_templates

def independently_scan_n(bound):
    found = {}
    for n in range(2,bound+1):
        k=n
        factors=[]
        for p in range(2,isqrt(k)+1):
            if k % p==0:
                count=0
                while k % p==0:
                    k//=p
                    count+=1
                factors.append((p,count))
        if k>1: factors.append((k,1))
        if len(factors)!=4 or any(e!=1 for _,e in factors): continue
        sigma=1
        for p,e in factors: sigma*=p+1
        excess=sigma-2*n
        if excess<=0: continue
        divs=[d for d in range(1,n) if n%d==0]
        witnesses={t for t in combinations(divs,3) if sum(t)==excess}
        if witnesses: found[n]=witnesses
    return found

if __name__ == '__main__':
    answers,pairs,templates=theorem_certificate()
    brute=independently_scan_n(13000)
    assert brute==answers
    multiple={k:len(v) for k,v in answers.items() if len(v)>1}
    assert sum(v-1 for v in multiple.values()) == 9
    print('THEOREM_CERT_OK n_count=51 witness_count=60 max_n=12714 pairs=%d templates=%d' %(pairs,templates))
    print('INDEPENDENT_SCAN_OK bound=13000 same_solution_and_witness_sets=yes')
    print('MULTIPLE_WITNESS_CASES',sorted(multiple.items()))
