"""Direct exhaustive closed-neighborhood parity test for small rook graphs."""
from collections import Counter
from itertools import combinations
from math import comb

def predicted(m,n):
    terms=Counter()
    if m%2==0 and n%2==0:
        terms[m*n]=1
    elif m%2==0:
        for a in range(1,m+1,2):terms[n*a]+=comb(m,a)
    elif n%2==0:
        for b in range(1,n+1,2):terms[m*b]+=comb(n,b)
    else:
        for a in range(1,m+1,2):
            for b in range(1,n+1,2):
                terms[a*b+(m-a)*(n-b)]+=comb(m,a)*comb(n,b)
    return terms

def direct(m,n):
    nn=m*n
    closed=[]
    for i in range(m):
        for j in range(n):
            mask=sum(1<<(k*n+l) for k in range(m) for l in range(n)
                     if k==i or l==j)
            closed.append(mask)
    hist=Counter()
    for mask in range(1<<nn):
        if all((mask & v).bit_count()%2==1 for v in closed):
            hist[mask.bit_count()]+=1
    return hist

def main():
    for m in range(2,5):
        for n in range(2,5):
            expected=predicted(m,n)
            got=direct(m,n)
            assert got==expected,(m,n,got,expected)
            print(f'{m}x{n}: {sorted(got.items())}; total={sum(got.values())}')
    print('DIRECT_EXHAUSTIVE: PASS')
if __name__=='__main__':main()
