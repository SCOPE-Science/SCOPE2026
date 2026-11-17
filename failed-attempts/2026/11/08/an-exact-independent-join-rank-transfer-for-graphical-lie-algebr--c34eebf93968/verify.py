"""Independent direct matrix-rank checks for independent-set graph joins.
Only finite-field arithmetic and a combinatorial prediction are used.
"""
from collections import Counter
from itertools import product
from math import prod


def mul(a,b,q):
    if q==4:
        z=0
        for i in range(2):
            if (b>>i)&1: z ^= a<<i
        if z&4: z ^= 0b111 # x^2=x+1
        return z
    return (a*b)%q

def add(a,b,q): return a^b if q==4 else (a+b)%q

def neg(a,q): return a if q==4 else (-a)%q

def inv(a,q):
    if a==0: raise ZeroDivisionError()
    if q==4:
        for b in range(1,4):
            if mul(a,b,4)==1:return b
        raise ValueError('inverse')
    return pow(a,-1,q)

def rank_mat(M,q):
    if not M: return 0
    A=[row[:] for row in M]
    n=len(A); p=len(A[0]); r=0
    for col in range(p):
        k=next((i for i in range(r,n) if A[i][col]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r]
        invp=inv(A[r][col],q)
        for j in range(col,p):A[r][j]=mul(A[r][j],invp,q)
        for i in range(r+1,n):
            if not A[i][col]:continue
            f=A[i][col]
            for j in range(col,p):A[i][j]=add(A[i][j],neg(mul(f,A[r][j],q),q),q)
        r+=1
        if r==n:break
    return r

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    assert num%den==0
    return num//den

def symp(r,q):return q**(r*r)*prod(q**(2*i)-1 for i in range(1,r+1))

def iso(r,t,q):
    if t<0 or t>r:return 0
    num=prod(q**(2*r-i)-q**i for i in range(t))
    den=prod(q**t-q**i for i in range(t))
    assert num%den==0
    return num//den

def nondeg(r,j,q):
    if j<0 or j>r:return 0
    return symp(r,q)//(symp(j,q)*symp(r-j,q))

def n_subspaces(m,r,d,j,q):
    h=m-2*r
    res=0
    for e in range(max(0,d-2*r),min(h,d)+1):
        a=d-e; u=a-2*j
        if 0<=u<=r and 0<=j<=r-u:
            res+=gaussian(h,e,q)*q**((h-e)*a)*iso(r,u,q)*nondeg(r-u,j,q)
    return res

def injections(n,t,q):return prod(q**n-q**i for i in range(t))

def transfer(base,m,n,q):
    out=Counter()
    for r,count in base.items():
        for t in range(min(m,n)+1):
            inj=injections(n,t,q)
            for j in range((m-t)//2+1):
                a=n_subspaces(m,r,m-t,j,q)
                if a:out[t+j]+=count*inj*a
    return dict(sorted(out.items()))

def brute_graph(m,edges,n,q):
    e=edges+[(i,m+j) for i in range(m) for j in range(n)]
    size=m+n
    ans=Counter()
    for weights in product(range(q),repeat=len(e)):
        A=[[0]*size for _ in range(size)]
        for (i,j),c in zip(e,weights):
            A[i][j]=c
            A[j][i]=neg(c,q)
        rk=rank_mat(A,q)
        assert rk%2==0
        ans[rk//2]+=1
    return dict(sorted(ans.items()))

def main():
    cases=[
      ('edgeless-2',2,[],2,2),
      ('edgeless-2',2,[],2,3),
      ('edgeless-2',2,[],2,4),
      ('edge-2',2,[(0,1)],2,2),
      ('edge-2',2,[(0,1)],2,3),
      ('edge-2',2,[(0,1)],2,4),
      ('path-3',3,[(0,1),(1,2)],2,2),
      ('cycle-4',4,[(0,1),(1,2),(2,3),(0,3)],1,3),
      ('cycle-4',4,[(0,1),(1,2),(2,3),(0,3)],2,2),
      ('cycle-4',4,[(0,1),(1,2),(2,3),(0,3)],2,3),
    ]
    for title,m,E,n,q in cases:
        base=brute_graph(m,E,0,q)
        theory=transfer(base,m,n,q)
        direct=brute_graph(m,E,n,q)
        assert theory==direct,(title,m,n,q,theory,direct)
        assert sum(theory.values())==q**(len(E)+m*n)
        print(title,'q='+str(q),'added='+str(n),'ranks='+str(direct),'PASS')
    # A separate structural check: the count of subspaces of each dimension.
    for q in (2,3,4):
        for m in range(1,7):
            for r in range(m//2+1):
                for d in range(m+1):
                    s=sum(n_subspaces(m,r,d,j,q) for j in range(d//2+1))
                    assert s==gaussian(m,d,q),(m,r,d,q,s)
    print('SYMPLECTIC_SUBSPACE_PARTITION_PASS')
    print('INDEPENDENT_JOIN_DIRECT_RANK_PASS')

if __name__=='__main__':main()
