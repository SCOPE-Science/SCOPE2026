"""Independent finite transfer enumerator for fixed binary-majority gears."""
from itertools import product
from math import comb

S = [(0,0),(0,1),(1,0),(1,1)]

def transpose_word_count(n):
    # A finite-state path count with a marked start/end state, and a weight for ones.
    ans = [0]*(n+1)
    for start in range(4):
        paths={(start,0):1}
        for _ in range(n):
            nxt={}
            for (v,k),count in paths.items():
                a,b=S[v]
                for c in (0,1):
                    if (a,b,c)==(1,0,1):
                        continue
                    dest=S.index((b,c)); key=(dest,k+c)
                    nxt[key]=nxt.get(key,0)+count
            paths=nxt
        for (v,k),count in paths.items():
            if v==start: ans[k]+=count
    return ans

def run_formula(n):
    ans=[0]*(n+1)
    ans[0]=ans[n]=1
    for j in range(1,n):
        for r in range(1,min(j,(n-j)//2)+1):
            ans[j]+=n*comb(j-1,r-1)*comb(n-j-r-1,r-1)//r
    return ans

def direct_words(n):
    ans=[0]*(n+1)
    for x in product((0,1),repeat=n):
        if any((x[(i-1)%n],x[i],x[(i+1)%n])==(1,0,1) for i in range(n)):
            continue
        ans[sum(x)]+=1
    return ans

if __name__=='__main__':
    for n in range(3,46):
        a=transpose_word_count(n)
        b=run_formula(n)
        assert a==b,(n,a,b)
        if n<=12: assert a==direct_words(n),(n,a,direct_words(n))
        print(f'n={n} admissible={sum(a)} fixed={2*sum(a[:n//2+1])}')
    print('PASS transfer and run formula for n=3..45; direct cyclic-word check for n=3..12')
