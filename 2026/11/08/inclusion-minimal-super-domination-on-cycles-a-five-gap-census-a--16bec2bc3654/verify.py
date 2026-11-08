"""Reproducibility checks for minimal super domination in cycles; stdlib only.
Run: python3 verify.py
This is finite corroboration; the general argument is mathematical.
"""
from collections import Counter
from math import floor

# Independent graph-definition test, not the gap criterion.
def super_dom(n, selected):
    allv = (1 << n) - 1
    outside = allv ^ selected
    nbr = [(1 << ((i - 1) % n)) | (1 << ((i + 1) % n)) for i in range(n)]
    for u in range(n):
        if not ((outside >> u) & 1):
            continue
        if not any(((selected >> v) & 1) and (nbr[v] & outside) == (1 << u)
                   for v in range(n) if (nbr[u] >> v) & 1):
            return False
    return True


def direct_minimal_polynomial(n):
    count = Counter()
    tested = 0
    allv = (1 << n) - 1
    for chosen in range(1 << n):
        tested += 1
        if not super_dom(n, chosen):
            continue
        if all(not super_dom(n, chosen & ~(1 << v)) for v in range(n) if (chosen >> v) & 1):
            count[chosen.bit_count()] += 1
    return dict(count), tested

# The determinant polynomial D(x,z). Key (length,selected-vertices), coefficient.
D = {(0,0):1, (3,2):-1, (4,2):-1, (5,3):-2,
     (6,4):-2, (7,5):-1, (8,5):1, (9,6):2, (10,7):1}

def rational_coefficients(max_n):
    # M(x,z)=(-x dD/dx)/D; recurrence coefficient-by-coefficient.
    m = [Counter() for _ in range(max_n+1)]
    for n in range(1, max_n+1):
        curr = Counter()
        for (length,size),coef in D.items():
            if length == n:
                curr[size] -= length*coef
            if 1 <= length <= n:
                for oldsize,num in m[n-length].items():
                    curr[size+oldsize] -= coef*num
        m[n]=Counter({k:v for k,v in curr.items() if v})
    return [dict(x) for x in m]


def independent_gap_transfer(max_n):
    """Directly enumerate rooted cyclic gap words in the three-state automaton."""
    from fractions import Fraction
    transitions = {
        0: [(1,1,0), (2,1,0), (1,2,1), (2,2,1)],
        1: [(0,3,2), (1,3,2)],
        2: [(0,4,3), (0,5,4)],
    }  # (next_class, vertices_consumed, selected_vertices)
    answers=[Counter() for _ in range(max_n+1)]
    for first in range(3):
        dp={(0,0,first):1}
        for k in range(1,max_n+1):
            next_dp={}
            for (length,size,last),ways in dp.items():
                for nxt,block_len,block_size in transitions[last]:
                    ln=length+block_len
                    if ln>max_n:continue
                    key=(ln,size+block_size,nxt)
                    next_dp[key]=next_dp.get(key,0)+ways
            dp=next_dp
            for (length,size,last),ways in dp.items():
                if last==first:
                    answers[length][size]+=Fraction(length*ways,k)
            if not dp:break
    assert all(v.denominator==1 for c in answers for v in c.values())
    return [{size:int(value) for size,value in c.items()} for c in answers]

def formula_upper(n):
    base=5*n//7
    return base-(n>=16 and n%7==2)-(n>=10 and n%7==3)

def main():
    max_n=154
    coeff=rational_coefficients(max_n)
    total=0; minsets=0
    for n in range(3,20):
        brute,seen=direct_minimal_polynomial(n)
        total+=seen
        minsets+=sum(brute.values())
        assert brute==coeff[n],(n,brute,coeff[n])
    # Independent rooted-gap transfer counts check the determinant series.
    gap_counts=independent_gap_transfer(45)
    for n in range(3,46):
        assert gap_counts[n]==coeff[n],(n,gap_counts[n],coeff[n])
    for n in range(3,max_n+1):
        counts=coeff[n]
        assert counts
        assert min(counts)==(n+1)//2 if n%4 in (0,3) else min(counts)>=(n+1)//2
        assert max(counts)==formula_upper(n),(n,max(counts),formula_upper(n))
        if n%7==0:
            assert counts[5*n//7]==7,(n,counts[5*n//7])
    # Verify graph-level minimum cardinalities against known formula for cycles.
    for n in range(3,20):
        minimum=(n+1)//2 if n%4 in (0,1,3) else (n+2)//2
        # General known exact minimum is ceil(n/2), except n congruent 2 mod 4 +1.
        minimum=(n+1)//2 + (n%4==2)
        assert min(coeff[n])==minimum,(n,min(coeff[n]),minimum)
    print('VERIFY_OK direct_graph_n=3..19 subsets=%d minimal_sets=%d rational_coefficients_n=3..%d upper_quasiperiodic=PASS extremal_seven=PASS' % (total,minsets,max_n))

if __name__=='__main__':main()
