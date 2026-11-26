"""Exact replay of commuting nilpotent partial-bijection rank/index spectra.

Requires Python 3 standard library; run: python3 checker.py
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb, factorial


def cycle_type_representative(parts):
    n = sum(parts)
    sigma = list(range(n))
    k = 0
    for ell in parts:
        for t in range(ell):
            sigma[k+t] = k+(t+1)%ell
        k += ell
    return tuple(sigma)


def partitions(n, maxpart=None):
    if n == 0:
        yield ()
        return
    if maxpart is None:
        maxpart = n
    for a in range(min(n,maxpart),0,-1):
        for rest in partitions(n-a,a):
            yield (a,) + rest


def all_partial_injections(n):
    values = range(n)
    for r in range(n+1):
        for domain in combinations(values,r):
            for image in combinations(values,r):
                for mapped in permutations(image):
                    b = [-1]*n
                    for i,j in zip(domain,mapped):
                        b[i]=j
                    yield tuple(b)


def commutes(sigma,b):
    for x in range(len(b)):
        a = b[sigma[x]]
        c = sigma[b[x]] if b[x] >= 0 else -1
        if a != c:
            return False
    return True


def nilpotency_index(b):
    n = len(b)
    worst = 1
    for x in range(n):
        y = x
        seen = set()
        visited = 0
        while y >= 0:
            if y in seen:
                return None
            seen.add(y)
            visited += 1
            y = b[y]
        worst = max(worst, visited)
    return worst


def polyconvolve(a,b):
    out=Counter()
    for i,c in a.items():
        for j,d in b.items():
            out[i+j]+=c*d
    return dict(out)


def one_length_formula(m,ell,h):
    ps = [{0:1}]
    for s in range(1,m+1):
        ans=Counter()
        for j in range(1,min(s,h)+1):
            multiplier = comb(s-1,j-1)*factorial(j)*ell**(j-1)
            power=ell*(j-1)
            for t,c in ps[s-j].items():
                ans[t+power]+=multiplier*c
        ps.append(dict(ans))
    return ps[m]


def formula_cycle_type(parts,h):
    out={0:1}
    for ell in sorted(set(parts)):
        out=polyconvolve(out,one_length_formula(parts.count(ell),ell,h))
    return out


def all_formula(parts):
    n=sum(parts)
    bound=max(parts.count(ell) for ell in set(parts))
    return {h:formula_cycle_type(parts,h) for h in range(1,bound+1)}


def check_all_small():
    for n in range(1,7):
        all_b=list(all_partial_injections(n))
        for parts in partitions(n):
            sigma=cycle_type_representative(parts)
            measured = Counter()
            for b in all_b:
                if commutes(sigma,b):
                    index = nilpotency_index(b)
                    if index is not None:
                        measured[index,sum(x>=0 for x in b)] += 1
            max_h=max(parts.count(ell) for ell in set(parts))
            for h in range(1,max_h+1):
                predicted = formula_cycle_type(parts,h)
                actual=Counter()
                for (index,rank),count in measured.items():
                    if index<=h:
                        actual[rank]+=count
                assert dict(actual)==predicted, (n,parts,h,dict(actual),predicted)
            assert sum(measured.values())==sum(formula_cycle_type(parts,max_h).values())
        print('n',n,'all cycle types match')


def check_example():
    p = (2,2,2,2)
    hs=all_formula(p)
    assert hs[1]=={0:1}
    assert hs[2]=={0:1,2:24,4:48}, hs[2]
    assert hs[3]=={0:1,2:24,4:144},hs[3]
    assert hs[4]=={0:1,2:24,4:144,6:192},hs[4]
    assert sum(hs[4].values())==361
    for ell in range(1,5):
        for m in range(1,8):
            for h in range(1,m+1):
                max_rank=ell*(m-(m+h-1)//h)
                p=one_length_formula(m,ell,h)
                assert max(p)==max_rank
                assert set(p)==set(ell*i for i in range(max_rank//ell+1))
    # Independently realize every equivariant partial injection on four 2-cycles
    # as an 8-point map; compare the actual composition power, not path lengths.
    sigma=cycle_type_representative((2,2,2,2))
    measured=Counter()
    for index_map in all_partial_injections(4):
        positions=[u for u,v in enumerate(index_map) if v>=0]
        for shifts in product(range(2),repeat=len(positions)):
            b=[-1]*8
            for u,shift in zip(positions,shifts):
                v=index_map[u]
                for p0 in range(2):
                    b[2*u+p0] = 2*v+(p0+shift)%2
            b=tuple(b)
            assert commutes(sigma,b)
            index=nilpotency_index(b)
            if index is not None:
                measured[index,sum(x>=0 for x in b)]+=1
    for h in range(1,5):
        actual=Counter()
        for (index,rank),count in measured.items():
            if index<=h:actual[rank]+=count
        assert dict(actual)==hs[h],(h,dict(actual),hs[h])
    assert sum(measured.values())==361
    print('example, sharp rank support, and direct 8-point centralizer match')

if __name__=='__main__':
    check_all_small()
    check_example()
    print('VERIFY_OK')
