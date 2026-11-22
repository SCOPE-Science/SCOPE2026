"""Direct exhaustive check of the Kautz-word one-deletion graph.

Uses actual deletion-output sets and unordered pairs, with no interval formula.
Requires Python 3 standard library only.
"""
from collections import Counter
from itertools import combinations, product


def words(q, n):
    yield from (w for w in product(range(q), repeat=n)
                if all(w[k] != w[k+1] for k in range(n-1)))


def predicted(q, n):
    return q * (q-1)**(n-2) * (n*n*(q-2)**2 + 3*n*(q-2) - (q-3)) // 2


def run():
    cases = 0
    for q, max_n in ((2, 8), (3, 7), (4, 5), (5, 4)):
        for n in range(1, max_n+1):
            xx = list(words(q, n))
            shadows = [{x[:i]+x[i+1:] for i in range(n)} for x in xx]
            counts = Counter()
            for i,j in combinations(range(len(xx)),2):
                if not(shadows[i] & shadows[j]):
                    continue
                a,b = xx[i],xx[j]
                differences = [k for k in range(n) if a[k] != b[k]]
                first,last = differences[0],differences[-1]
                counts[(first,n-1-last,last-first+1)] += 1
            observed = sum(counts.values())
            assert observed == predicted(q,n),(q,n,observed,predicted(q,n))
            def boundary(t):
                return 1 if t==0 else (q-2)*(q-1)**(t-1)
            for L in range(1,n+1):
                for a in range(n-L+1):
                    b=n-L-a
                    observed_cell=counts[(a,b,L)]
                    factor=q*(q-1)//2 if L==1 else q*(q-1)**L-q*(q-1)//2
                    assert observed_cell==factor*boundary(a)*boundary(b), (
                        q,n,a,b,L,observed_cell,factor*boundary(a)*boundary(b))
            cases+=1
            print('q=%d n=%d vertices=%d edges=%d PASS' % (q,n,len(xx),observed))
    print('PASS: %d parameter cases; all span cells checked by deletion-output enumeration'%cases)
if __name__=='__main__':run()
