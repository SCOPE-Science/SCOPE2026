"""Exact standard-library checks of Johnson-graph clique-homology characters.

Usage: python3 verify_johnson_equivariant.py
No external packages, network access, or auxiliary files are needed.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb, factorial


def parts(n, hi=None):
    if hi is None:
        hi = n
    if n == 0:
        yield ()
    else:
        for a in range(min(n, hi), 0, -1):
            for b in parts(n-a, a):
                yield (a,) + b


def strip_data(outer, inner):
    cells = {(r, c) for r, width in enumerate(outer) for c in range(width)}
    cells -= {(r, c) for r, width in enumerate(inner) for c in range(width)}
    if not cells:
        return None
    if any((r+1,c) in cells and (r,c+1) in cells and (r+1,c+1) in cells
           for (r,c) in cells):
        return None
    seen = set()
    frontier = [next(iter(cells))]
    while frontier:
        r, c = frontier.pop()
        if (r,c) in seen:
            continue
        seen.add((r,c))
        for point in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
            if point in cells and point not in seen:
                frontier.append(point)
    if seen != cells:
        return None
    return len({r for r,c in cells})-1


@lru_cache(None)
def specht_character(shape, cycle_type):
    """Murnaghan--Nakayama recursion, with exact integer arithmetic."""
    if not cycle_type:
        return int(not shape)
    length = cycle_type[0]
    target = sum(shape)-length
    if target < 0:
        return 0
    total = 0
    for mu in parts(target):
        if len(mu) > len(shape) or any(a > b for a,b in zip(mu,shape)):
            continue
        height = strip_data(shape,mu)
        if height is not None:
            total += (-1)**height * specht_character(mu,cycle_type[1:])
    return total


def fixed_poly(cycles):
    n = sum(cycles)
    result = [1] + [0]*n
    for length in cycles:
        for j in range(n-length,-1,-1):
            result[j+length] += result[j]
    return result


def coeff_without(cycles, delete, degree):
    if degree < 0:
        return 0
    reduced = list(cycles)
    for length in delete:
        reduced.remove(length)
    p = fixed_poly(reduced)
    return p[degree] if degree < len(p) else 0


def predicted_trace(n,k,cycles):
    """Lefschetz formula from vertex, incidence and signed-edge modules."""
    fixed = fixed_poly(cycles)
    a = cycles.count(1)
    b = cycles.count(2)
    value = fixed[k-1] + fixed[k] + fixed[k+1] - 1
    if a:
        value -= a*(coeff_without(cycles,(1,),k-1)
                    +coeff_without(cycles,(1,),k))
    if a >= 2:
        value += comb(a,2)*coeff_without(cycles,(1,1),k-1)
    if b:
        value -= b*coeff_without(cycles,(2,),k-1)
    return value


def facets(n,k):
    ground = set(range(n))
    star = [tuple(sorted(tuple(sorted(a+(x,))) for x in sorted(ground-set(a))))
            for a in combinations(range(n),k-1)]
    top = [tuple(sorted(tuple(x for x in b if x != z) for z in b))
           for b in combinations(range(n),k+1)]
    return star+top


def faces_by_size(n,k):
    ans = {}
    for facet in facets(n,k):
        for r in range(1,len(facet)+1):
            ans.setdefault(r,set()).update(combinations(facet,r))
    return {r: sorted(faces) for r,faces in ans.items()}


def class_permutation(cycles):
    a = 0
    sigma = list(range(sum(cycles)))
    for length in cycles:
        for i in range(length):
            sigma[a+i] = a+(i+1)%length
        a += length
    return sigma


def inversion_sign(original, sigma):
    imaged = [tuple(sorted(sigma[x] for x in v)) for v in original]
    inv = sum(imaged[i] > imaged[j]
              for i in range(len(imaged)) for j in range(i+1,len(imaged)))
    return -1 if inv%2 else 1


def direct_trace(faces,sigma):
    result = -1 # reduced versus unreduced Lefschetz number
    for size, allfaces in faces.items():
        fset = set(allfaces)
        for face in allfaces:
            image = tuple(sorted(tuple(sorted(sigma[x] for x in v)) for v in face))
            if image != face:
                continue
            result += (-1)**(size-1)*inversion_sign(face,sigma)
    return result


def binary_rank(columns):
    pivots = {}
    for x in columns:
        while x:
            i = x.bit_length()-1
            if i in pivots:
                x ^= pivots[i]
            else:
                pivots[i] = x
                break
    return len(pivots)


def mod2_betti(faces):
    dimensions = sorted(faces)
    ranks = {}
    for degree in dimensions[1:]:
        index = {v:i for i,v in enumerate(faces[degree-1])}
        cols=[]
        for simplex in faces[degree]:
            x=0
            for sub in combinations(simplex,degree-1):
                x ^= 1 << index[sub]
            cols.append(x)
        ranks[degree]=binary_rank(cols)
    return {degree-1:len(faces[degree])-ranks.get(degree,0)-ranks.get(degree+1,0)
            for degree in dimensions}


def verify():
    cases = 0
    conjugacy_classes = 0
    named_checks = 0
    for n in range(6,10):
        for k in range(3,n//2+1):
            if n-k<3: continue
            faces=faces_by_size(n,k)
            for cyc in parts(n):
                sigma=class_permutation(cyc)
                direct=direct_trace(faces,sigma)
                formal=predicted_trace(n,k,cyc)
                irreducible=sum(specht_character((n-j-2,j,1,1),cyc)
                                for j in range(1,min(k,n-k)))
                assert direct == formal == irreducible, (n,k,cyc,direct,formal,irreducible)
                conjugacy_classes += 1
            assert predicted_trace(n,k,(1,)*n) > 0
            if n<=8:
                bets=mod2_betti(faces)
                assert bets[0]==1 and bets[1]==0
                assert bets.get(2)==predicted_trace(n,k,(1,)*n)
                assert all(not value for degree,value in bets.items() if degree>=3), (n,k,bets)
                named_checks += 1
            cases += 1
            print('case',n,k,'betti2',predicted_trace(n,k,(1,)*n),
                  'specht_summands',min(k,n-k)-1,'faces',sum(map(len,faces.values())))
    print('VERIFY_OK cases=%d class_trace_checks=%d mod2_full_chain_checks=%d'
          %(cases,conjugacy_classes,named_checks))


if __name__ == '__main__':
    verify()
