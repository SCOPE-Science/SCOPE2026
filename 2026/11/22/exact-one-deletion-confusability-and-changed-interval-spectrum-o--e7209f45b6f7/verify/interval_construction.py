"""Second check: construct confusable pairs via minimal unequal intervals.

Does not calculate any deletion shadows, and compares the resulting edge sets
with the elementary closed-form polynomial in the alphabet size.
Requires only Python 3 standard library.
"""
from itertools import product
from collections import Counter


def valid(x):
    return all(a != b for a,b in zip(x,x[1:]))


def edges_by_span(q,n):
    alphabet=range(q)
    found=set()
    mode_count=Counter()
    for x in product(alphabet,repeat=n):
        if not valid(x):continue
        # Single-position replacements.
        for i in range(n):
            for z in alphabet:
                if z == x[i]:continue
                y=x[:i]+(z,)+x[i+1:]
                if valid(y):
                    found.add(tuple(sorted((x,y))))
        # Canonical left-deletion/right-deletion intervals.
        for i in range(n-1):
            for j in range(i+1,n):
                for z in alphabet:
                    if z==x[j]:continue
                    y=x[:i]+x[i+1:j+1]+(z,)+x[j+1:]
                    if valid(y) and x[i]!=y[i]:
                        e=tuple(sorted((x,y)))
                        found.add(e)
                        mode_count[e]+=1
    return found,mode_count

def formula(q,n):
    # Integer form avoids negative exponents in arithmetic for n=1.
    B=n*n*(q-2)**2+3*n*(q-2)-(q-3)
    return q*(q-1)**max(n-2,0)*B//(2*((q-1) if n==1 else 1))


def run():
    for q,nmax in ((2,8),(3,6),(4,5),(5,4)):
        for n in range(1,nmax+1):
            pairs,modes=edges_by_span(q,n)
            assert len(pairs)==formula(q,n),(q,n,len(pairs),formula(q,n))
            # Each difference interval has at most two orientations; both
            # precisely for alternating complementary-phase pairs.
            for (x,y),m in modes.items():
                assert 1 <= m <=2,(q,n,x,y,m)
                d=[i for i in range(n) if x[i]!=y[i]]
                if len(d)>1 and m==2:
                    i,j=d[0],d[-1]
                    assert j-i+1==len(d)
                    assert all(x[k]==x[k+2] for k in range(i,j-1))
            print('q=%d n=%d interval-generated=%d PASS'%(q,n,len(pairs)))
    print('PASS: interval construction, multiplicities, and total law')

if __name__=='__main__':run()
