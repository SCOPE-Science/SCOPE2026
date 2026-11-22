"""Standalone standard-library checks for a cyclic proper-3-color frozen-state theorem.
No finite test is used as a substitute for the theorem's transfer-matrix proof.
"""
from itertools import product, permutations


def frozen_formula(n):
    L0,L1=2,1
    if n==0: lucas=2
    elif n==1:lucas=1
    else:
        for _ in range(2,n+1):L0,L1=L1,L0+L1
        lucas=L1
    r=[3,-1,1]
    for k in range(3,n+1):r.append(-r[-1]-r[-3])
    epsilon=(2 if n%3==0 else -1)
    return lucas+2+epsilon+2*r[n]


def proper(x):
    n=len(x)
    return all(x[i]!=x[(i+1)%n] for i in range(n))


def legal_swap_degree(x):
    n=len(x)
    count=0
    for i in range(n):
        j=(i+1)%n
        y=list(x)
        y[i],y[j]=y[j],y[i]
        if y!=list(x) and proper(y):count+=1
    return count


def signword(x):
    return tuple(1 if (x[(i+1)%len(x)]-x[i])%3==1 else 0 for i in range(len(x)))


def sign_degree(s):
    n=len(s)
    return sum(s[(i-1)%n]==s[i]==s[(i+1)%n] for i in range(n))


def is_sign_frozen(s):
    return not any(s[i]==s[(i+1)%len(s)]==s[(i+2)%len(s)] for i in range(len(s)))


def construction(n):
    if n%2==0:return (0,1)*(n//2)
    if n>=9 and n%2==1:return (0,0,1)*3+(0,1)*((n-9)//2)
    raise ValueError('No general construction for odd n < 9')


def symbolic_determinant_check():
    # Expand det(I-z M) in Z[z,w] using permutation signs. Each
    # nonzero M[i,j] is w^k, k=1 or 2, where M=w*T(w).
    m={(0,1):2, (1,2):1, (1,3):2, (2,0):1,
       (2,1):2, (3,2):1}
    coeff={}
    for perm in permutations(range(4)):
        inversions=sum(perm[i]>perm[j] for i in range(4)
                       for j in range(i+1,4))
        terms={(0,0):(-1 if inversions%2 else 1)}
        for i,j in enumerate(perm):
            factor={}
            if i==j: factor[(0,0)]=1
            if (i,j) in m: factor[(1,m[(i,j)])]=-1
            nxt={}
            for (a,b),v in terms.items():
                for (c,d),w in factor.items():
                    nxt[a+c,b+d]=nxt.get((a+c,b+d),0)+v*w
            terms=nxt
        for key,val in terms.items():coeff[key]=coeff.get(key,0)+val
    d0={}
    d1={},{}
    c0,c1=d1
    for (k,p),v in coeff.items():
        d0[k]=d0.get(k,0)+v
        residue=p%3
        A,B= ((1,0) if residue==0 else (0,1) if residue==1 else (-1,-1))
        c0[k]=c0.get(k,0)+A*v
        c1[k]=c1.get(k,0)+B*v
    assert [d0.get(k,0) for k in range(5)]==[1,0,-1,-2,-1]
    assert [c0.get(k,0) for k in range(5)]==[1,0,-1,1,-1]
    assert all(not v for v in c1.values())
    print('Two twisted degree-four characteristic determinants: PASS')


def determinant_check():
    # characteristic polynomial \\det(I-zM) asserted in proof;
    # verify traces and recurrences from integer matrix powers for t=1.
    T=((0,1,0,0), (0,0,1,1), (1,1,0,0), (0,0,1,0))
    P=[[int(i==j) for j in range(4)] for i in range(4)]
    trace=[]
    for k in range(1,26):
        P=[[sum(P[i][h]*T[h][j] for h in range(4)) for j in range(4)] for i in range(4)]
        trace.append(sum(P[i][i] for i in range(4)))
        if k>=5:
            # D0=1-z^2-2z^3-z^4
            assert trace[k-1]==trace[k-3]+2*trace[k-4]+trace[k-5]
    return trace[:12]


def main():
    symbolic_determinant_check()
    print('T(1) trace powers:',determinant_check())
    total=0
    for n in range(3,14):
        frozen=0;proper_count=0
        for x in product(range(3),repeat=n):
            if not proper(x):continue
            proper_count+=1
            s=signword(x)
            observed=legal_swap_degree(x)
            predicted=sign_degree(s)
            assert observed==predicted,(n,x,s,observed,predicted)
            frozen+=(observed==0)
        assert proper_count==2**n+2*(-1)**n,(n,proper_count)
        assert frozen==frozen_formula(n),(n,frozen,frozen_formula(n))
        print('n=%2d: proper=%6d frozen=%5d formula=%5d' % (n,proper_count,frozen,frozen_formula(n)))
        total+=proper_count
    print('Directly checked proper colorings:',total)
    for n in range(3,21):
        count=0
        for mask in range(1<<n):
            p=mask.bit_count()
            if (2*p-n)%3:continue
            s=tuple((mask>>i)&1 for i in range(n))
            if is_sign_frozen(s):count+=3
        assert count==frozen_formula(n),(n,count,frozen_formula(n))
    print('All eligible sign words exhaustively checked n=3..20')
    assert [n for n in range(3,21) if frozen_formula(n)==0]==[3,5,7]
    for n in range(4,302):
        if (n%2==0) or (n>=9 and n%2):
            s=construction(n)
            assert len(s)==n and (2*sum(s)-n)%3==0 and is_sign_frozen(s)
    print('Frozen existence constructions passed n=4..301')
    print('PASS')


if __name__=='__main__':main()
