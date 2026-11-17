"""Independent finite checks for the weight-two shuffle-square root spectrum."""
from functools import lru_cache
from collections import Counter
from math import comb, ceil


def count_roots_by_shuffle(word):
    m = len(word)//2
    total = 0
    for k in range(m):
        root = '0'*k+'1'+'0'*(m-1-k)
        @lru_cache(None)
        def reachable(i,j):
            if i == m and j == m:
                return True
            h = i+j
            return ((i < m and word[h] == root[i] and reachable(i+1,j))
                    or (j < m and word[h] == root[j] and reachable(i,j+1)))
        total += reachable(0,0)
    return total


def count_roots_formula(a,b,c):
    m=(a+b+c+2)//2
    lo=max((a+1)//2,a+b-m+1)
    hi=min(a,(a+b)//2,m-1)
    return max(0,hi-lo+1)


def count_tail_formula(m,r):
    h=m-3*(r-1)
    return 1+3*comb(h,2) if h>=1 else 0


def verify():
    words=0
    direct_total=0
    max_roots=0
    for m in range(1,12):
        distribution=Counter()
        for a in range(2*m-1):
            for b in range(2*m-1-a):
                c=2*m-2-a-b
                word='0'*a+'1'+'0'*b+'1'+'0'*c
                brute=count_roots_by_shuffle(word)
                explicit=count_roots_formula(a,b,c)
                assert brute==explicit, (m,a,b,c,brute,explicit)
                words+=1
                direct_total+=brute
                max_roots=max(max_roots,brute)
                distribution[brute]+=1
                for r in range(1,1+(m+2)//3):
                    t=r-1
                    assert (brute>=r)==(a>=2*t and c>=2*t and b>=2*t+(a%2) and b<=m-r), (m,a,b,c,r)
        for r in range(1,(m+2)//3+2):
            assert sum(n for roots,n in distribution.items() if roots>=r)==count_tail_formula(m,r), (m,r,distribution)
        assert max(distribution)==(m+2)//3,(m,distribution)
        assert sum(distribution.values())==comb(2*m,2)
        assert sum(n for roots,n in distribution.items() if roots>0)==1+3*comb(m,2)
    # Arithmetic tail counts through larger lengths, independently counting all gap triples.
    for m in range(12,65):
        d=Counter()
        for a in range(2*m-1):
            for b in range(2*m-1-a):
                c=2*m-2-a-b
                d[count_roots_formula(a,b,c)]+=1
        for r in range(1,(m+2)//3+2):
            assert sum(v for k,v in d.items() if k>=r)==count_tail_formula(m,r),(m,r)
    print(f'VERIFY_OK direct_words={words} direct_root_memberships={direct_total} max_roots_tested={max_roots} lengths=1..64')

if __name__=='__main__':
    verify()
