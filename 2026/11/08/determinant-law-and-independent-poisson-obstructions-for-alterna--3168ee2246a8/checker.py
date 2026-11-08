"""Exact checks for two independent matching-equivalence modal frames.

Usage: python checker.py. Uses only the Python standard library.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def perfect_matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        yield {}
        return
    x = vertices[0]
    for j in range(1, len(vertices)):
        y = vertices[j]
        rest = vertices[1:j] + vertices[j+1:]
        for tail in perfect_matchings(rest):
            out = dict(tail)
            out[x] = y
            out[y] = x
            yield out


def reach(start, partners, depth):
    s = {start}
    for i in range(depth):
        r = partners[i % 2]
        s |= {r[x] for x in tuple(s)}
    return s


def direct_probability(n, p, depth):
    e = {i: i ^ 1 for i in range(2*n)}
    total = Fraction()
    matching_count = 0
    for f in perfect_matchings(range(2*n)):
        matching_count += 1
        reach_sets = [reach(v, (e,f), depth) for v in range(2*n)] + [reach(v, (f,e), depth) for v in range(2*n)]
        for mask in range(1 << (2*n)):
            marked = {i for i in range(2*n) if (mask >> i) & 1}
            if all(s & marked for s in reach_sets):
                k = len(marked)
                total += p**k * (1-p)**(2*n-k)
    return total / matching_count, matching_count


def multiply(A, B):
    k = len(A)
    return [[sum((A[i][a]*B[a][j] for a in range(k)), Fraction()) for j in range(k)] for i in range(k)]


def transfer_traces(p, depth, max_l):
    k = 2*depth
    T = [[Fraction() for j in range(k)] for i in range(k)]
    for i in range(k):
        T[i][0] += p
        if i+1 < k:
            T[i][i+1] += 1-p
    Q = multiply(T, T)
    R = [[Fraction(int(i==j)) for j in range(k)] for i in range(k)]
    ans = []
    for l in range(1, max_l+1):
        R = multiply(R, Q)
        ans.append(sum((R[i][i] for i in range(k)), Fraction()))
    return ans


def coefficient_probability(n, p, depth):
    tr = transfer_traces(p, depth, n)
    b = [Fraction(1)]
    for m in range(1, n+1):
        b.append(sum((tr[l-1]*b[m-l] for l in range(1,m+1)), Fraction()) / (2*m))
    return b[n] / Fraction(comb(2*n,n),4**n)


def independent_cyclic_probability(n, p, depth):
    # Another exact check: average the forbidden-run probability over all F matchings.
    E = {i:i^1 for i in range(2*n)}
    total = Fraction()
    count=0
    for F in perfect_matchings(range(2*n)):
        count+=1
        seen=set()
        factor=Fraction(1)
        for v in range(2*n):
            if v in seen:continue
            comp=set([v])
            todo=[v]
            while todo:
                w=todo.pop()
                for t in (E[w],F[w]):
                    if t not in comp:
                        comp.add(t);todo.append(t)
            seen.update(comp)
            # Exact probability of all marked/nonmarked assignments on the component.
            nodes=sorted(comp)
            all_reaches = [reach(x,(E,F),depth) for x in nodes]+[reach(x,(F,E),depth) for x in nodes]
            a=Fraction()
            for mask in range(1<<len(nodes)):
                marks={x for i,x in enumerate(nodes) if (mask>>i)&1}
                if all(s&marks for s in all_reaches):
                    k=len(marks);a+=p**k*(1-p)**(len(nodes)-k)
            factor*=a
        total+=factor
    return total/count


def double_factorial_odd(m):
    z=1
    for j in range(1,m+1,2):z*=j
    return z


def component_sizes(n,F):
    E={i:i^1 for i in range(2*n)}
    unseen=set(range(2*n))
    out=[]
    while unseen:
        x=next(iter(unseen)); comp={x};todo=[x]
        while todo:
            v=todo.pop()
            for y in (E[v],F[v]):
                if y not in comp:comp.add(y);todo.append(y)
        unseen.difference_update(comp)
        out.append(len(comp)//2)
    return out


def check_component_expectations():
    checks=0
    for n in range(1,6):
        totals=[0]*(n+1);count=0
        for F in perfect_matchings(range(2*n)):
            count+=1
            for l in component_sizes(n,F):totals[l]+=1
        assert count==double_factorial_odd(2*n-1)
        for l in range(1,n+1):
            expected=Fraction(totals[l],count)
            pred=Fraction(comb(n,l)*2**(l-1)*factorial(l-1)*double_factorial_odd(2*(n-l)-1),double_factorial_odd(2*n-1))
            assert expected==pred,(n,l,expected,pred)
            checks+=1
    return checks


def main():
    checks=0
    for n in range(1,5):
        for depth in (1,2,3):
            p=Fraction(2,5)
            a,count=direct_probability(n,p,depth)
            b=coefficient_probability(n,p,depth)
            c=independent_cyclic_probability(n,p,depth)
            assert a==b==c,(n,depth,a,b,c)
            checks+=1
            print('n',n,'depth',depth,'matchings',count,'prob',a)
    print('MATCHING_MODAL_DETERMINANT_EXACT_OK',checks, 'CYCLE_EXPECTATION_CHECKS',check_component_expectations())


if __name__ == '__main__':
    main()
