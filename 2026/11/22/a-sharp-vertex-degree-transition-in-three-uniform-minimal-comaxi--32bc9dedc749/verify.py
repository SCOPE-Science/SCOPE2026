"""Exact incidence census for minimal comaximal hypergraphs.

Uses integer arithmetic and direct enumeration of finite rings; no dependencies.
"""
from itertools import combinations, product
from math import comb, factorial


def prod(xs):
    result = 1
    for x in xs:
        result *= x
    return result


def predicted_edges(q, k, j=1):
    total = sum(
        (-1)**a * comb(k, a) * prod(t**k - 1 - a*(t-1) for t in q)
        for a in range(k+1)
    ) * j**k
    assert total % factorial(k) == 0
    return total // factorial(k)


def predicted_degree(q, k, cosupport, j=1):
    C = set(cosupport)
    prefactor = prod(q[i]**(k-1) for i in C) - prod(q[i]**(k-1)-1 for i in C)
    other = sum(
        (-1)**a * comb(k-1, a) * prod(
            q[i]**(k-1)-1-a*(q[i]-1)
            for i in range(len(q)) if i not in C
        ) for a in range(k)
    )
    total = prefactor * other * j**(k-1)
    assert total % factorial(k-1) == 0
    return total // factorial(k-1)


def check_ring(residue_sizes, coordinates, is_unit, k, radical_size):
    # This enumerates actual elements, not abstract weighted supports.
    vertices = [x for x in product(*[range(s) for s in coordinates])
                if any(is_unit(i, a) for i,a in enumerate(x))
                and not all(is_unit(i, a) for i,a in enumerate(x))]
    d = {x:0 for x in vertices}
    edges = 0
    for T in combinations(vertices, k):
        if not all(any(is_unit(i, x[i]) for x in T)
                   for i in range(len(coordinates))):
            continue
        if not all(any(is_unit(i,x[i]) and all(not is_unit(i,y[i]) for y in T if y!=x)
                       for i in range(len(coordinates))) for x in T):
            continue
        edges += 1
        for x in T:
            d[x]+=1
    assert edges == predicted_edges(residue_sizes,k,radical_size), (coordinates,k,edges)
    for x,value in d.items():
        C = [i for i,a in enumerate(x) if is_unit(i,a)]
        expect = predicted_degree(residue_sizes,k,C,radical_size)
        assert value==expect,(coordinates,k,x,value,expect)
    print('PASS_RING', coordinates, 'residues',residue_sizes,'radical',radical_size,'k',k,
          'vertices',len(vertices),'edges',edges,'max_degree',max(d.values()))


def max_support(n):
    degrees={s:predicted_degree([2]*n,3,range(s)) for s in range(1,n)}
    maxdegree=max(degrees.values())
    maxima=[s for s,v in degrees.items() if v==maxdegree]
    expected=(n-2 if n<=4 else n-3 if n<=10 else n-4)
    assert maxima==[expected],(n,maxima,expected)
    return expected,maxdegree


def main():
    for n in range(3,9):
        check_ring([2]*n,[2]*n,lambda i,a:a!=0,3,1)
    for q in [[2,3,4],[2,2,3,2],[2,3,2,4]]:
        for k in range(2,min(len(q),3)+1):
            check_ring(q,q,lambda i,a:a!=0,k,1)
    # A nonreduced product R=(Z/4Z) x F_3 x F_2, radical size 2.
    for k in (2,3):
        check_ring([2,3,2],[4,3,2],
                   lambda i,a:(a%2==1) if i==0 else (a!=0), k, 2)
    for n in range(3,31):
        s,deg=max_support(n)
        print('PASS_MODE','n',n,'support',s,'codim',n-s,'maximum_degree',deg)
    print('VERIFY_OK')


if __name__=='__main__':
    main()
