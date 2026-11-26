"""Exact-arithmetic finite checks for the all-budget star resolvent partition theorem.
Usage: python star_allbudget_verifier.py. Standard library only.
Finite checks supplement the algebraic proof; they do not establish the infinite claim.
"""
from fractions import Fraction as Q
from itertools import combinations

def inverse(M):
    n=len(M)
    A=[list(map(Q,row))+[Q(i==j) for j in range(n)] for i,row in enumerate(M)]
    for c in range(n):
        p=next(i for i in range(c,n) if A[i][c]);A[c],A[p]=A[p],A[c]
        a=A[c][c];A[c]=[v/a for v in A[c]]
        for i in range(n):
            if i!=c:
                q=A[i][c]
                A[i]=[a-q*b for a,b in zip(A[i],A[c])]
    return [row[n:] for row in A]

def partitions(n):
    a=[0]*n
    def rec(i,max_label):
        if i==n:
            yield tuple(a);return
        for j in range(max_label+2):
            a[i]=j
            yield from rec(i+1,max(max_label,j))
    yield from rec(1,0)

def g(N,r):
    q,t=divmod(N,r)
    return r*q*(q-1)//2+t*q

def F(m,k,alpha,h):
    return alpha*h+Q(h*(h-1),2)+g(m-h,k-1)

def star_inv(m,mu):
    L=[[Q(0) for _ in range(m+1)] for _ in range(m+1)]
    for j in range(1,m+1):
        L[0][0]+=1;L[j][j]+=1;L[0][j]-=1;L[j][0]-=1
    return inverse([[L[i][j]+(mu if i==j else 0) for j in range(m+1)] for i in range(m+1)])

def main():
    count=0
    for m in range(2,8):
        for mu in [Q(1,4),Q(1,2),Q(3,5),Q(1),Q(5,4),Q(2),Q(5)]:
            R=star_inv(m,mu)
            a=1/(mu*(mu+m+1));b=a/(mu+1)
            for j in range(1,m+1):
                assert R[0][j]==a
                for i in range(1,m+1):
                    if i!=j:assert R[i][j]==b
            alpha=(mu+1)**2
            for k in range(3,m+2):
                best=min(F(m,k,alpha,h) for h in range(m-k+2))
                winners={h for h in range(m-k+2) if F(m,k,alpha,h)==best}
                delta=[alpha+h-(m-h-1)//(k-1) for h in range(m-k+1)]
                assert all(delta[i+1]>delta[i] for i in range(len(delta)-1))
                for p in partitions(m+1):
                    if max(p)+1!=k:continue
                    groups=[[i for i,v in enumerate(p) if v==c] for c in range(k)]
                    h=len(groups[p[0]])-1
                    N=m-h
                    actual=sum(R[i][j]**2 for group in groups for i,j in combinations(group,2))
                    predicted=b*b*(alpha*h+Q(h*(h-1),2)+sum(Q((len(group))*(len(group)-1),2) for group in groups if 0 not in group))
                    assert actual==predicted
                    assert actual>=b*b*best
                    if actual==b*b*best:
                        assert h in winners
                        sizes=[len(group) for group in groups if 0 not in group]
                        assert max(sizes)-min(sizes)<=1
                    count+=1
    assert F(9,3,Q(4),0)==F(9,3,Q(4),1)<F(9,3,Q(4),2)
    assert F(9,3,Q(9,4),1)==Q(57,4)
    assert F(9,3,Q(9,4),0)==16
    print('PASS:',count,'exact partition tests; star inverse entries, all candidates, and boundary ties verified.')
if __name__=='__main__':main()
