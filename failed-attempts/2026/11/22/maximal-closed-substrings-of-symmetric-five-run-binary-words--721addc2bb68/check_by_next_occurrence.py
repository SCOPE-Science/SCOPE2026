"""Independent longest-common-extension and nearest-next-occurrence MCS checker."""
from itertools import product

def next_oracle(word):
    n=len(word)
    lcp=[[0]*(n+1) for _ in range(n+1)]
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if word[i]==word[j]:lcp[i][j]=1+lcp[i+1][j+1]
    out={(i+1,i+1) for i in range(n)
         if (i==0 or word[i]!=word[i-1]) and (i==n-1 or word[i]!=word[i+1])}
    for i in range(n):
        earlier_max=0
        for j in range(i+1,n):
            h=lcp[i][j]
            if h>earlier_max and h>0 and (i==0 or word[i-1]!=word[j-1]):
                out.add((i+1,j+h))
            earlier_max=max(earlier_max,h)
    return out

def expected(a,b,c):
    n=2*a+2*b+c
    out={(1,a),(a+1,a+b),(a+b+1,a+b+c),
         (a+b+c+1,a+2*b+c),(a+2*b+c+1,n)}
    for t in range(1,min(a,c-1)+1):
        out.add((a-t+1,a+b+t))
        out.add((a+b+c-t+1,a+2*b+c+t))
    for t in range(1,b):out.add((a+b-t+1,a+b+c+t))
    for t in range(min(a,c),a+1):out.add((a-t+1,a+2*b+c+t))
    return out

def gf_coefficient(n,k):
    return sum((2*a+2*b+c ==n) and (a+b+4+min(a-1,c-1)+2*(c>a)==k)
      for a in range(1,n) for b in range(1,n) for c in [n-2*(a+b)] if c>=1)

if __name__=='__main__':
    cases=0; total=0
    for a,b,c in product(range(1,19),repeat=3):
        w='0'*a+'1'*b+'0'*c+'1'*b+'0'*a
        got=next_oracle(w); want=expected(a,b,c)
        assert got==want,(a,b,c,sorted(got-want),sorted(want-got))
        cases+=1;total+=len(got)
    for n in range(5,81):
        values=[(a,b,c,a+b+4+min(a-1,c-1)+2*(c>a))
            for a in range(1,n) for b in range(1,n)
            for c in [n-2*(a+b)] if c>=1]
        if not values:continue
        expectedmax=6 if n==5 else (2*n)//3+4
        assert max(v[-1] for v in values)==expectedmax,(n,expectedmax,max(v[-1] for v in values))
        assert sum(gf_coefficient(n,k) for k in {v[-1] for v in values})==len(values)
    print('NEAREST_LCE_ORACLE PASS cases',cases,'MCS_occurrences',total,'max_length',90,'extrema_lengths_through',80)
