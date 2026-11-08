#!/usr/bin/env python3
"""Independent exhaustive rook-graph fort census versus a labeled-species coefficient calculation.
Standard-library only. Execute with: python3 verify.py
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from math import factorial


def product(p, q, m, n):
    out = defaultdict(Q)
    for (a,b,k), v in p.items():
        for (c,d,l), w in q.items():
            if a+c <= m and b+d <= n:
                out[a+c,b+d,k+l] += v*w
    return dict(out)


def exponential(terms, m, n):
    result = {(0,0,0):Q(1)}
    for (a,b,k), c in terms:
        factor = {(0,0,0):Q(1)}
        power = Q(1)
        limit = min(m//a if a else 10**9, n//b if b else 10**9)
        for j in range(1,limit+1):
            power *= c/j
            factor[a*j,b*j,k*j] = power
        result = product(result, factor, m, n)
    return result


def scalar_sum(*args):
    out = defaultdict(Q)
    for p, s in args:
        for key, val in p.items():
            out[key] += s*val
    return dict(out)


def isolates(axis, m, n):
    return ({(j,0,0):Q(1,factorial(j)) for j in range(1,m+1)} if axis=='x'
            else {(0,j,0):Q(1,factorial(j)) for j in range(1,n+1)})


def polynomial_via_components(m,n):
    # Every component of a minimal edge cover is a star. Size-one stars
    # are counted only in the xy term, not in either larger-star term.
    star_a = [((1,k,k),Q(1,factorial(k))) for k in range(2,n+1)]
    star_b = [((k,1,k),Q(1,factorial(k))) for k in range(2,m+1)]
    covered = exponential([((1,1,1),Q(1))]+star_a+star_b,m,n)
    # Remove precisely the all-center-degree>=2 oriented forests having
    # at least one center with degree >=3; all-degree-two cases survive.
    oriented_a = exponential(star_a,m,n)
    oriented_b = exponential(star_b,m,n)
    oriented_a2 = exponential([((1,2,2),Q(1,2))],m,n)
    oriented_b2 = exponential([((2,1,2),Q(1,2))],m,n)
    # Contract every degree-two B vertex into a labeled edge of a
    # multigraph on A.  If any A is unused, a minimal fort is a forest
    # or one pure cycle. The forest species uses Cayley's k^(k-2).
    def trees(a_max,b_max):
        return [((k,k-1,2*k-2),Q(k**(k-2),factorial(k)))
                for k in range(2,min(a_max,b_max+1)+1)]
    forest_a = product(isolates('x',m,n),exponential(trees(m,n),m,n),m,n)
    forest_b = product(isolates('y',m,n),
        exponential([((b,a,k),c) for (a,b,k),c in trees(n,m)],m,n),m,n)
    # A simple bipartite cycle (including a four-cycle) and at least
    # one unused vertex on either side; exactly one cycle is selected.
    cycle = {(k,k,2*k):Q(1,2*k) for k in range(2,min(m,n)+1)}
    exp_x = isolates('x',m,n)
    exp_y = isolates('y',m,n)
    cyc_x = product(exp_x,cycle,m,n)
    cyc_y = product(exp_y,cycle,m,n)
    cyc_xy = product(product(exp_x,exp_y,m,n),cycle,m,n)
    total = scalar_sum((covered,1),(oriented_a,-1),(oriented_a2,1),
        (oriented_b,-1),(oriented_b2,1),(forest_a,1),(forest_b,1),
        (cyc_x,1),(cyc_y,1),(cyc_xy,1))
    out={}
    for (a,b,k),v in total.items():
        if (a,b)==(m,n) and v:
            z=v*factorial(m)*factorial(n)
            assert z.denominator==1, (m,n,k,z)
            out[k]=int(z)
    return out


def brute_polynomial(m,n):
    size = m*n
    adj=[]
    for i in range(size):
        adj.append(sum(1<<j for j in range(size)
            if i!=j and (i//n==j//n or i%n==j%n)))
    has_fort = bytearray(1<<size)
    minimal = Counter()
    fort_count = 0
    for s in range(1,1<<size):
        # All immediate submasks were processed. If any proper subset
        # was a fort, at least one immediate submask contains a fort.
        proper_contains_fort = False
        v=s
        while v:
            bit=v&-v
            v-=bit
            if has_fort[s^bit]:
                proper_contains_fort=True
                break
        fort=all((adj[i]&s).bit_count()!=1
                 for i in range(size) if not ((s>>i)&1))
        if fort:
            fort_count += 1
            if not proper_contains_fort:
                minimal[s.bit_count()] += 1
        has_fort[s] = fort or proper_contains_fort
    return dict(minimal),fort_count,(1<<size)-1


def main():
    boards=[(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),
            (3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(4,4)]
    total_sets=total_forts=total_minimal=0
    for m,n in boards:
        predicted=polynomial_via_components(m,n)
        observed,fc,examined=brute_polynomial(m,n)
        assert predicted==observed,(m,n,predicted,observed)
        total_sets+=examined
        total_forts+=fc
        total_minimal+=sum(observed.values())
    for n in range(5,21):
        predicted=polynomial_via_components(2,n)
        from math import comb
        want={4:6*comb(n,4)+6*comb(n,3)+comb(n,2),n:2*n}
        assert predicted==want,(n,predicted,want)
    print(f'VERIFY_OK boards={len(boards)} examined_subsets={total_sets} '
          f'forts={total_forts} minimal_forts={total_minimal} '
          'coefficientwise=PASS thin_family_n5..20=PASS')

if __name__=='__main__':
    main()
