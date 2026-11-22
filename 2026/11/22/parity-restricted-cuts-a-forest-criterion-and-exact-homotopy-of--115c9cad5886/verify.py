"""Independent exhaustive trace and graph-criterion check for parity-constrained cuts.
No external packages required. Run: python3 verify.py
"""
from itertools import combinations
from math import factorial

def edges(n): return [(i,j) for i in range(n) for j in range(i+1,n)]

def forest_odd_component(n, ed, mask):
    parent=list(range(n)); size=[1]*n
    def find(x):
        while parent[x]!=x: x=parent[x]
        return x
    for k,(u,v) in enumerate(ed):
        if not(mask>>k&1): continue
        ru,rv=find(u),find(v)
        if ru==rv: return False
        parent[rv]=ru; size[ru]+=size[rv]
    return n%2==1 or any(size[i]%2 for i in range(n) if parent[i]==i)

def test(n):
    ed=edges(n)
    # Coordinate incidence of all cuts with a shore of even cardinality.
    cuts=[]
    for S in range(1<<n):
        if S.bit_count()%2: continue
        bits=sum(((S>>u ^ S>>v)&1)<<k for k,(u,v) in enumerate(ed))
        cuts.append(bits)
    def shattered(F):
        outcomes={sum(((C>>k)&1)<<j for j,k in enumerate(F)) for C in cuts}
        return len(outcomes)==(1<<len(F))
    counts=[0]*(n+1)
    for mask in range(1<<len(ed)):
        F=[k for k in range(len(ed)) if mask>>k&1]
        criterion=forest_odd_component(n,ed,mask)
        truth=shattered(F)
        if criterion!=truth: raise AssertionError((n,F,criterion,truth))
        if truth: counts[len(F)]+=1
    return counts

def polynomial(n):
    # Labeled exponential formula for unrooted trees. Recurrence for exp(A).
    from fractions import Fraction
    N=n
    def eexp(even_only):
        a=[Fraction(0)]*(N+1)
        for j in range(1,N+1):
            if (not even_only) or j%2==0:
                a[j]=Fraction(1 if j==1 else j**(j-2),factorial(j))
        # b[t][k] counts coefficient [x^t z^k] exp(sum a_j x^j z^(j-1)).
        b=[[Fraction(0)]*(N+1) for _ in range(N+1)]
        b[0][0]=1
        for t in range(1,N+1):
            for j in range(1,t+1):
                if not a[j]: continue
                for k in range(j-1,N+1):
                    if b[t-j][k-(j-1)] if k>=j-1 else False:
                        b[t][k]+=Fraction(j,t)*a[j]*b[t-j][k-(j-1)]
        return [int(factorial(N)*b[N][k]) for k in range(N+1)]
    allf=eexp(False)
    excluded=eexp(True) if n%2==0 else [0]*(N+1)
    return [x-y for x,y in zip(allf,excluded)]

def beta_even(n):
    from fractions import Fraction
    def alt_sum(even_only):
        a=[Fraction(0)]*(n+1)
        for j in range(1,n+1):
            if not even_only or j%2==0:
                a[j]=Fraction((-1)**(j-1)*(1 if j==1 else j**(j-2)),factorial(j))
        e=[Fraction(0)]*(n+1);e[0]=1
        for t in range(1,n+1):
            e[t]=sum(j*a[j]*e[t-j] for j in range(1,t+1))/t
        return factorial(n)*e[n]
    return int(alt_sum(False)-alt_sum(True))

if __name__=='__main__':
    for n in (3,4,5,6):
        brute=test(n)
        formula=polynomial(n)
        assert brute==formula,(n,brute,formula)
        print('n=',n,'face_counts=',brute,'VC=',max(i for i,c in enumerate(brute) if c))
    for n in (4,6,8,10,12):
        print('n=',n,'homology_wedge_rank=',beta_even(n))
