"""Independent alternating-interval certificate of coloring and sharp cliques.
Requires only Python 3 standard library. Run: python check_intervals.py
"""
from itertools import combinations


def toggle_neighbors(word):
    n=len(word)
    out=set()
    for a in range(n):
        for b in range(a+1,n,2):   # even lengths only: b-a is odd
            factor=word[a:b+1]
            if all(factor[i]!=factor[i+1] for i in range(len(factor)-1)):
                other=word[:a]+''.join(str(1-int(c)) for c in factor)+word[b+1:]
                out.add(other)
    return out


def family(n,k):
    r=min(k,n-k)
    for j in range(r+1):
        core='10'*j+'01'*(r-j)
        if k <= n-k:
            yield core+'0'*(n-2*r)
        else:
            yield ''.join(str(1-int(c)) for c in core)+'1'*(n-2*r)


def prove_examples():
    edges=0
    for n in range(2,15):
        for k in range(n+1):
            r=min(k,n-k)
            words=[''.join('1' if i in indices else '0' for i in range(n))
                   for indices in combinations(range(n),k)]
            S=set(words)
            for w in words:
                class_no=sum(i for i,c in enumerate(w,1) if c=='1')%(r+1)
                near=toggle_neighbors(w)
                assert near <= S, (n,k,w,near-S)
                for v in near:
                    assert sum(i for i,c in enumerate(v,1) if c=='1')%(r+1) != class_no
                    edges+=1
            F=list(family(n,k))
            assert len(set(F))==r+1
            for a,b in combinations(F,2):
                assert b in toggle_neighbors(a), (n,k,a,b)
    # Nonperfectness persists for every n >= 8 and 4 <= k <= n-4:
    base=['01011001','10011001','10010101','10101010','01011010']
    for n in range(8,17):
        for k in range(4,n-3):
            ext=['0'*(n-k-4)+s+'1'*(k-4) for s in base]
            for i,j in combinations(range(5),2):
                assert (ext[j] in toggle_neighbors(ext[i])) == (j-i in (1,4)), (n,k,i,j)
    print('PASS: direct interval generation n <= 14, %d directed edges; padded C5 for all 8 <= n <= 16.' % edges)

if __name__=='__main__':
    prove_examples()
