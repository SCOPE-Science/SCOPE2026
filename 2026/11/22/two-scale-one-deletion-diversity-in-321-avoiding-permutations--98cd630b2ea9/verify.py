"""Independent finite checks for the one-deletion spectrum on 321-avoiding permutations.
Run: python3 verify.py
Uses only Python's standard library. Exhaustive tests are finite evidence, not a proof.
"""
from collections import Counter
from itertools import permutations
from math import comb


def avoid321(p):
    # The smallest element to the right of a descent witnesses a 321 triple.
    smallest = len(p) + 1
    for j in range(len(p) - 1, -1, -1):
        for i in range(j):
            if p[i] > p[j] > smallest:
                return False
        smallest = min(smallest, p[j])
    return True


def reduced(p):
    order = {v: i for i, v in enumerate(sorted(p))}
    return tuple(order[x] for x in p)


def predicted(n):
    # Sum over arbitrary marked ascending and descending bonds.
    # Coefficient of z^n in C(z/(1-(u-1)z)) / (1-(v-1)z^2 C(...)).
    # Work first with factorial-moment variables X=u-1, Y=v-1.
    C = [comb(2*m, m)//(m+1) for m in range(n+1)]
    T = [Counter() for _ in range(n+1)]
    T[0][0] = 1
    for m in range(1,n+1):
        for a in range(n-m+1):
            T[m+a][a] += C[m] * comb(m+a-1,a)
    # Multiply polynomials in z and X, using a sparse dictionary.
    def multiply(p,q):
        out=[Counter() for _ in range(n+1)]
        for i,pd in enumerate(p):
            for j,qd in enumerate(q[:n+1-i]):
                for a,va in pd.items():
                    for b,vb in qd.items():
                        out[i+j][a+b] += va*vb
        return out
    product=[[Counter({0:1})]+[Counter() for _ in range(n)]]
    for k in range(1,n//2+2):
        product.append(multiply(product[-1],T))
    factorial_marked=Counter()
    for d in range(n//2+1):
        for a,val in product[d+1][n-2*d].items():
            factorial_marked[a,d]+=val
    actual=Counter()
    for (a,d),v in factorial_marked.items():
        for j in range(a+1):
            for k in range(d+1):
                actual[j,k] += v*comb(a,j)*comb(d,k)*(-1)**(a-j+d-k)
    return +actual


def test():
    for n in range(1,10):
        observed=Counter()
        for p in permutations(range(n)):
            if not avoid321(p):
                continue
            a=sum(p[i+1] == p[i]+1 for i in range(n-1))
            d=sum(p[i+1] == p[i]-1 for i in range(n-1))
            outputs={reduced(p[:i]+p[i+1:]) for i in range(n)}
            assert len(outputs)==n-a-d,(n,p,a,d,len(outputs))
            observed[a,d]+=1
        expected=predicted(n)
        assert observed==expected,(n,observed,expected)
        print('n=%d Catalan=%d joint_cells=%d OK'%(n,sum(observed.values()),len(observed)))
    print('VERIFY_OK')
if __name__=='__main__':
    test()
