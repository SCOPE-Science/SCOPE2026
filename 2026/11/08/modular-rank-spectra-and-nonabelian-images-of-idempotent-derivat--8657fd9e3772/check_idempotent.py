"""Direct arithmetic and original-identity checker for idempotent derivations of free class-two Lie algebras.
Uses independent basis multiplication and enumerates all possible central shifts for small q,d.
"""
from itertools import product, combinations
from collections import Counter
from math import comb

def add(a,b,q): return a^b if q==4 else (a+b)%q
def mul(a,b,q):
    if q!=4:return a*b%q
    out=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1: out^=1<<(i+j)
    if out&4:out^=7  # x^2=x+1
    return out

def gaussian(n,r,q):
    num=1;den=1
    for i in range(r):num*=q**(n-i)-1;den*=q**(r-i)-1
    return num//den

def projection_count(d,r,q): return gaussian(d,r,q)*q**(r*(d-r))
def rank_expected(d,r):return r*(d+1-r)
def exponent(d,r,q):
    s=d-r
    if q%2==0:return r*s*s+r*(comb(r,2)+comb(s,2))
    if r==0:return 0
    assert r==1
    return s*s+comb(s,2)

def matmul(A,B,q):
    n=len(A);p=len(B);m=len(B[0]); O=[[0]*m for _ in range(n)]
    for i in range(n):
        for k in range(p):
            if A[i][k]:
                for j in range(m):
                    O[i][j]=add(O[i][j],mul(A[i][k],B[k][j],q),q)
    return O

def matrix_rank(M,q):
    A=[row[:] for row in M];n=len(A);m=len(A[0]);r=0
    for j in range(m):
        k=next((i for i in range(r,n) if A[i][j]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r]
        # inverse in GF(q)
        inv=next(x for x in range(1,q) if mul(x,A[r][j],q)==1)
        A[r]=[mul(inv,x,q) for x in A[r]]
        for i in range(n):
            if i!=r and A[i][j]:
                b=A[i][j]
                A[i]=[add(A[i][v], -mul(b,A[r][v],q),q) if q!=4 else add(A[i][v],mul(b,A[r][v],q),q) for v in range(m)]
        r+=1
        if r==n:break
    return r

def neg(x,q):return x if q==4 else (-x)%q

def direct_check(d,q,full=True):
    pairs=list(combinations(range(d),2)); c=len(pairs);N=d+c
    pair_index={p:i for i,p in enumerate(pairs)}
    def bracket(x,y):
        if x==y or x>=d or y>=d:return [0]*N
        if x<y: s=1;p=(x,y)
        else:s=neg(1,q);p=(y,x)
        a=[0]*N;a[d+pair_index[p]]=s;return a
    def construct(A,phi):
        M=[[0]*N for _ in range(N)]
        for i in range(d):
            for j in range(d):M[j][i]=A[j][i]
            for z in range(c):M[d+z][i]=phi[z][i]
        for z,(i,j) in enumerate(pairs):
            for k in range(d):
                for h,v in enumerate(bracket(k,j)):
                    M[h][d+z]=add(M[h][d+z],mul(A[k][i],v,q),q)
                for h,v in enumerate(bracket(i,k)):
                    M[h][d+z]=add(M[h][d+z],mul(A[k][j],v,q),q)
        return M
    def is_idempotent(M):return matmul(M,M,q)==M
    def verify_derivation(M):
        for i in range(N):
            for j in range(N):
                # all nonzero commutators are one basis vector with sign; avoid extension sum
                if i<d and j<d and i!=j:
                    sign=1 if i<j else neg(1,q)
                    left=[mul(sign,M[h][d+pair_index[tuple(sorted((i,j)))]] ,q) for h in range(N)]
                else: left=[0]*N
                right=[0]*N
                for k in range(d):
                    for h,v in enumerate(bracket(k,j)):
                        right[h]=add(right[h],mul(M[k][i],v,q),q)
                    for h,v in enumerate(bracket(i,k)):
                        right[h]=add(right[h],mul(M[k][j],v,q),q)
                if left!=right:return False
        return True
    ids={}; hits=Counter();cases=0
    for flat in product(range(q),repeat=d*d):
        A=[list(flat[i*d:(i+1)*d]) for i in range(d)]
        if matmul(A,A,q)!=A:continue
        r=matrix_rank(A,q);ids[r]=ids.get(r,0)+1
        for z in product(range(q), repeat=c*d) if full else [tuple([0]*(c*d))]:
            phi=[list(z[i*d:(i+1)*d]) for i in range(c)]
            M=construct(A,phi)
            assert verify_derivation(M)
            cases+=1
            if is_idempotent(M):
                rr=matrix_rank(M,q)
                assert rr==rank_expected(d,r),(d,q,r,rr)
                hits[rr]+=1
    predicted=Counter()
    for r in range(d+1):
        if q%2 and r>1:continue
        predicted[rank_expected(d,r)]+=projection_count(d,r,q)*q**exponent(d,r,q)
    for k in list(predicted):
        if predicted[k]==0:del predicted[k]
    assert dict(hits)==dict(predicted),(d,q,hits,predicted)
    assert ids=={r:projection_count(d,r,q) for r in range(d+1)}
    if d==3 and q==2:
        A=[[1,0,0],[0,1,0],[0,0,0]]
        M=construct(A,[[0]*d for _ in range(c)])
        assert is_idempotent(M) and verify_derivation(M)
        wedge01=[0]*N; wedge01[d+pair_index[(0,1)]]=1
        augmented=[M[i]+[wedge01[i]] for i in range(N)]
        assert matrix_rank(augmented,q)==matrix_rank(M,q)+1
        # D(e0)=e0 and D(e1)=e1, but [e0,e1] is not in the image.
        print('NONABELIAN_IMAGE_AND_NONIDEAL_EXPLICIT_EXAMPLE_OK d=3 q=2 r=2')
    print(f'DIRECT_ORIGINAL_BRACKET_AND_IDEMPOTENCE_OK d={d} q={q} enumerated={cases} rank_counts={dict(sorted(hits.items()))}')

if __name__=='__main__':
    direct_check(2,2)
    direct_check(2,3)
    direct_check(2,4)
    direct_check(3,2)
    for d,q in [(3,3),(4,2),(5,2)]:
        data=[]
        for r in range(d+1):
            if q%2 and r>1:continue
            data.append((r,rank_expected(d,r),projection_count(d,r,q)*q**exponent(d,r,q)))
        print(f'FORMULA d={d} q={q}: {data}')
    print('FREE_TWO_STEP_IDEMPOTENT_DERIVATIONS_OK')
