"""Standard-library check of weighted transfer characteristic and first coefficients."""
from itertools import permutations
from math import comb
from collections import defaultdict

def padd(a,b):
    out=defaultdict(int,a)
    for k,v in b.items():out[k]+=v
    return {k:v for k,v in out.items() if v}
def pmul(a,b):
    out=defaultdict(int)
    for (i,j,k),v in a.items():
        for (ii,jj,kk),w in b.items():out[(i+ii,j+jj,k+kk)]+=v*w
    return {k:v for k,v in out.items() if v}
def det(A):
    out={}
    for perm in permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        term={(0,0,0):(-1)**inv}
        for i in range(4):term=pmul(term,A[i][perm[i]])
        out=padd(out,term)
    return out

def matrix():
    A=[[{} for _ in range(4)] for __ in range(4)]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                if (a,b,c)==(0,1,0):continue
                A[2*a+b][2*b+c]={(b,b*c,0):1}
    return A

if __name__=='__main__':
    A=matrix(); I=[[padd(({(0,0,1):1} if i==j else {}), {k:-v for k,v in A[i][j].items()}) for j in range(4)] for i in range(4)]
    expected={(0,0,4):1,(0,0,3):-1,(1,1,3):-1,(1,1,2):1,(2,1,1):-1}
    assert det(I)==expected,(det(I),expected)
    # Traces: each cyclic word no isolated 1, weighted by (number of 1s, number of adjacent 11 edges).
    def trace(n):
        cnt=defaultdict(int)
        for w in range(1<<n):
            bits=[(w>>i)&1 for i in range(n)]
            if any(bits[(i-1)%n]==0 and bits[i]==1 and bits[(i+1)%n]==0 for i in range(n)):continue
            k=sum(bits);e=sum(bits[i]&bits[(i+1)%n] for i in range(n))
            cnt[(k,e)]+=1
        return cnt
    for n in range(3,14):
        c=trace(n)
        selected=sum(v for (k,e),v in c.items() if 2*k>n and 2*e<n)
        formula=0
        for k in range(n//2+1,n):
            for r in range(1,min(k//2,n-k)+1):
                if 2*(k-r)<n:formula+=n*comb(k-r-1,r-1)*comb(n-k-1,r-1)//r
        assert selected==formula,(n,selected,formula)
        print(f'n={n} admissible_words={sum(c.values())} selected_words={selected}')
    print('TRANSFER_AND_WORD_COUNT_OK')
