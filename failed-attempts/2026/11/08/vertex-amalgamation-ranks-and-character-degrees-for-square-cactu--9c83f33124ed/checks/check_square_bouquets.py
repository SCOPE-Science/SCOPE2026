"""Direct finite-field rank census for one-vertex bouquets of four-cycles.
Uses matrix elimination and an independently enumerated graph class formula.
"""
from itertools import product
from collections import Counter
from math import comb


def gauss_rank(a,p):
    a=[row[:] for row in a]; m=len(a); r=0
    for j in range(m):
        pivot=next((i for i in range(r,m) if a[i][j]%p),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j]%p,-1,p)
        for k in range(j,m): a[r][k]=(a[r][k]*inv)%p
        for i in range(r+1,m):
            if a[i][j]:
                fac=a[i][j]
                for k in range(j,m): a[i][k]=(a[i][k]-fac*a[r][k])%p
        r+=1
    return r


def edges_of_square_bouquet(t):
    e=[]
    for i in range(t):
        a,b,d=3*i+1,3*i+2,3*i+3
        e.extend([(0,a),(a,b),(b,d),(d,0)])
    return e


def direct_rank_hist(p,t):
    n=3*t+1; edges=edges_of_square_bouquet(t); hist=Counter()
    for values in product(range(p), repeat=len(edges)):
        M=[[0]*n for _ in range(n)]
        for (i,j),v in zip(edges,values):
            M[i][j]=v; M[j][i]=-v%p
        r=gauss_rank(M,p)
        assert r%2==0
        hist[r//2]+=1
    return dict(sorted(hist.items()))


def expected_rank_hist(q,t):
    A=q*(q*q-1);B=q*q*(q*q-1)
    # (1-z)(1+A*z)^t + z*(q^2+B*z)^t
    d=Counter()
    for s in range(t+1):
        c=comb(t,s)
        d[s]+=c*A**s
        d[s+1]-=c*A**s
        d[s+1]+=c*q**(2*(t-s))*B**s
    return dict(sorted((k,v) for k,v in d.items() if v))


def class_number_from_vertex_support(q,t):
    e=edges_of_square_bouquet(t);n=3*t+1;m=4*t;total=0
    for mask in range(1<<n):
        U={i for i in range(n) if mask>>i&1}; neigh=set(U)
        for i,j in e:
            if i in U or j in U:neigh.update((i,j))
        rem=set(U); c=0
        while rem:
            c+=1;v=rem.pop();stack=[v]
            while stack:
                k=stack.pop()
                for i,j in e:
                    nbr=j if i==k else i if j==k else -1
                    if nbr in rem: rem.remove(nbr);stack.append(nbr)
        exp=m+c-len(neigh)
        assert exp>=0
        total+=(q-1)**len(U)*q**exp
    return total


def main():
    for q,t in ((2,1),(3,1),(5,1),(7,1),(2,2),(3,2),(2,3)):
        actual=direct_rank_hist(q,t)
        expected=expected_rank_hist(q,t)
        assert actual==expected,(q,t,actual,expected)
        assert sum(actual.values())==q**(4*t)
        if q%2:
            chars={r:q**(3*t+1-2*r)*N for r,N in actual.items()}
            assert all(v==int(v) for v in chars.values())
            assert sum(chars[r]*q**(2*r) for r in chars)==q**(7*t+1)
            closed=(q*q-1)*q**(2*t-1)*(q*q+q-1)**t+q**(3*t-1)*(2*q*q-1)**t
            assert sum(chars.values())==closed
            assert class_number_from_vertex_support(q,t)==closed
            print('q=%d t=%d rank_hist=%s chars=%s class_count=%d PASS'%(q,t,actual,chars,closed))
        else:
            print('q=%d t=%d rank_hist=%s PASS'%(q,t,actual))
    print('SQUARE_BOUQUET_SKEW_RANK_AND_CHARACTER_DEGREE_PASS')
if __name__=='__main__':main()
