"""Independent finite tests for two-spike nonlinear-complexity classification."""
from collections import Counter
from itertools import combinations,product

def predicted(n,i,j,a,b):
    d=min((j-i)%n,(i-j)%n)
    L=n-d
    if a != b:
        return d if d==L else L-1
    return d-1 if d==L else max(L-1,2*d)

def exact_nlc(seq):
    n=len(seq)
    for k in range(1,n+1):
        mapping={}
        for i in range(n):
            block=tuple(seq[(i+j)%n] for j in range(k))
            succ=seq[(i+k)%n]
            if block in mapping and mapping[block]!=succ:break
            mapping[block]=succ
        else:return k
    raise AssertionError('missing register')

def poly_counts(n,q):
    result=Counter()
    for d in range(1,(n-1)//2+1):
        result[max(n-d-1,2*d)]+=n*(q-1)
        result[n-d-1]+=n*(q-1)*(q-2)
    if n%2==0:
        result[n//2-1]+=(n//2)*(q-1)
        result[n//2]+=(n//2)*(q-1)*(q-2)
    return result

def run():
    nseq=0; pchecks=0; pairst=0
    for q in range(2,5):
        for n in range(4,24):
            counts=Counter()
            for i,j in combinations(range(n),2):
                for a,b in product(range(1,q),repeat=2):
                    w=[0]*n; w[i]=a;w[j]=b
                    got=exact_nlc(w)
                    expected=predicted(n,i,j,a,b)
                    assert got==expected,(n,q,i,j,a,b,got,expected)
                    counts[got]+=1;nseq+=1
            expected=poly_counts(n,q)
            assert counts==expected,(n,q,counts,expected)
            assert sum(counts.values())==(n*(n-1)//2)*(q-1)**2
            pchecks+=1
    # Independent maximal common-prefix test, 2nd definition
    for n in range(4,18):
        for d in range(1,n//2+1):
            for a,b in [(1,1),(1,2),(2,1)]:
                w=[0]*n;w[0]=a;w[d]=b
                for k in range(1,n+1):
                    ok=True
                    for i,j in combinations(range(n),2):
                        if all(w[(i+h)%n]==w[(j+h)%n] for h in range(k)) and w[(i+k)%n]!=w[(j+k)%n]:
                            ok=False;break
                    if ok:
                        assert k==predicted(n,0,d,a,b),(n,d,a,b,k)
                        break
                pairst+=1
    print('CHECK_OK', 'complete-word tests', nseq,'histograms',pchecks, 'pairwise-rotation cases',pairst)
if __name__=='__main__':run()
