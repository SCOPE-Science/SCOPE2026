"""Independent finite checks of marked-tournament defect/orientation distributions.

Usage: python checker.py
Uses only Python standard library and exhaustive tournament enumeration.
"""
from collections import Counter
from fractions import Fraction
from math import comb, factorial


def comb3(n, a, b):
    return factorial(n) // (factorial(a)*factorial(b)*factorial(n-a-b))


def orientation_matrix(n, bits):
    e = [[False] * n for _ in range(n)]
    p = 0
    for x in range(n):
        for y in range(x+1, n):
            e[x][y] = bool((bits >> p) & 1)
            e[y][x] = not e[x][y]
            p += 1
    return e


def counts(e, k):
    n = len(e)
    out = [x for x in range(k,n) if all(e[x][z] for z in range(k))]
    inn = [y for y in range(k,n) if all(e[z][y] for z in range(k))]
    h = sum(e[x][y] for x in out for y in inn)
    # Direct semantics of exists x exists y forall z with x,y unmarked.
    phi = any(x != y and e[x][y] and all(e[x][z] and e[z][y] for z in range(k))
              for x in range(k,n) for y in range(k,n))
    assert phi == (h > 0)
    return (len(out), len(inn), h)


def theoretical(n,k,a,b,h):
    N=n-k
    if a+b>N or h>a*b:return Fraction(0)
    t=Fraction(1,2**k)
    u=1-2*t
    return comb3(N,a,b)*t**(a+b)*u**(N-a-b)*Fraction(comb(a*b,h),2**(a*b))


def main():
    trials=0
    formula_checks=0
    for n in range(2,7):
        total=2**(n*(n-1)//2)
        for k in range(1,n):
            observed=Counter()
            for bits in range(total):
                observed[counts(orientation_matrix(n,bits), k)]+=1
                trials+=1
                formula_checks+=1
            for a in range(n-k+1):
                for b in range(n-k-a+1):
                    for h in range(a*b+1):
                        expected=theoretical(n,k,a,b,h)
                        assert Fraction(observed.get((a,b,h),0),total)==expected, (n,k,a,b,h)
            assert sum(observed.values())==total
    print(f'MARKED_TOURNAMENT_EXACT_OK tournament_instances={trials} formula_checks={formula_checks}')

if __name__ == '__main__':main()

# Independent two-round EF-game check for the rank-two profile lemma.
def model(n, edge_bits, color_bits):
    return (orientation_matrix(n,edge_bits), tuple(bool((color_bits >> i) & 1) for i in range(n)))

def profile_fingerprint(m):
    e,c=m
    n=len(c)
    signatures=[]
    for x in range(n):
        neighbors=frozenset((c[y],e[x][y]) for y in range(n) if y != x)
        signatures.append((c[x],neighbors))
    return frozenset(signatures)

def pair_atomic_match(a,i,z,b,j,w):
    ea,ca=a; eb,cb=b
    return (ca[i]==cb[j] and ca[z]==cb[w]
            and (i==z)==(j==w) and ea[i][z]==eb[j][w]
            and ea[z][i]==eb[w][j])

def first_round_winning(a,i,b,j):
    ea,ca=a; eb,cb=b
    return (all(any(pair_atomic_match(a,i,z,b,j,w) for w in range(len(cb)))
                for z in range(len(ca)))
            and all(any(pair_atomic_match(a,i,z,b,j,w) for z in range(len(ca)))
                    for w in range(len(cb))))

def two_round_game_equiv(a,b):
    return (all(any(first_round_winning(a,i,b,j) for j in range(len(b[1])))
                for i in range(len(a[1])))
            and all(any(first_round_winning(a,i,b,j) for i in range(len(a[1])))
                    for j in range(len(b[1]))))

def check_ef_profiles():
    representatives={}
    num=0
    for n in range(1,5):
        for edges in range(1 << (n*(n-1)//2)):
            for colors in range(1 << n):
                m=model(n,edges,colors)
                s=profile_fingerprint(m)
                representatives.setdefault(s,[])
                if len(representatives[s])<2:
                    representatives[s].append(m)
                num+=1
    tests=0
    reps=[m for v in representatives.values() for m in v]
    for i,a in enumerate(reps):
        for b in reps[i:]:
            assert two_round_game_equiv(a,b)==(profile_fingerprint(a)==profile_fingerprint(b))
            tests+=1
    print(f'RANK_TWO_COLORED_TOURNAMENT_EF_OK models={num} signatures={len(representatives)} representative_pair_games={tests}')

if __name__ == '__main__':
    check_ef_profiles()
