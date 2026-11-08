"""Independent direct multiplication checks for generalized dihedral group algebras."""
from collections import Counter
from itertools import product
from random import Random


def operations(q):
    if q==4:
        # F_4=F_2[u]/(u*u+u+1), field elements 0,1,u,u+1.
        plus=lambda a,b:a^b
        mul=lambda a,b: 0 if a*b==0 else (((a&1)*(b&1)) ^ ((((a&1)*((b>>1)&1)) ^ (((a>>1)&1)*(b&1)) ^ (((a>>1)&1)*((b>>1)&1)))<<1) ^ (((a>>1)&1)*((b>>1)&1)))
        # reduced u^2=u+1, thus constant ac+bd and u ad+bc+bd.
    else:
        plus=lambda a,b:(a+b)%q
        mul=lambda a,b:(a*b)%q
    neg=[next(j for j in range(q) if plus(i,j)==0) for i in range(q)]
    inv=[0]+[next(j for j in range(1,q) if mul(i,j)==1) for i in range(1,q)]
    return plus,mul,neg,inv


def dihedral_table(n):
    def mul(i,j):
        a,e=i%n,i//n
        b,f=j%n,j//n
        return (a+(b if not e else -b))%n+(e^f)*n
    N=2*n
    return [[mul(i,j) for j in range(N)] for i in range(N)]


def direct_rank(x,mult,field):
    q=len(field[2]);add,mul,neg,inv=field
    N=len(x)
    columns=[[0]*N for _ in range(N)]
    for i,coeff in enumerate(x):
        if not coeff:continue
        for j in range(N):
            a,b=mult[i][j],mult[j][i]
            columns[j][a]=add(columns[j][a],coeff)
            columns[j][b]=add(columns[j][b],neg[coeff])
    # Gaussian elimination on row matrix over F_q.
    mat=[[columns[j][i] for j in range(N)] for i in range(N)]
    r=0
    for j in range(N):
        pivot=next((i for i in range(r,N) if mat[i][j]),None)
        if pivot is None:continue
        mat[r],mat[pivot]=mat[pivot],mat[r]
        cinv=inv[mat[r][j]]
        for k in range(j,N):mat[r][k]=mul(cinv,mat[r][k])
        for i in range(r+1,N):
            a=mat[i][j]
            if a:
                for k in range(j,N):mat[i][k]=add(mat[i][k],neg[mul(a,mat[r][k])])
        r+=1
    return r


def expected_for_cyclic(n,q):
    from math import gcd
    d=1
    while pow(q,d,n) not in (1,n-1):d+=1
    assert (n-1)%(2*d)==0
    count=(n-1)//(2*d)
    distribution={0:1}
    for _ in range(count):
        updated=distribution.copy()
        for rank,v in distribution.items():
            updated[rank+2*d]=updated.get(rank+2*d,0)+v*(q**(3*d)-1)
        distribution=updated
    center_dim=2+count*d
    return {r:v*q**center_dim for r,v in distribution.items()}


def main():
    for q,n in ((4,3),(5,3)):
        F=operations(q);table=dihedral_table(n);cnt=Counter()
        for x in product(range(q),repeat=2*n):
            cnt[direct_rank(x,table,F)]+=1
        expectation=expected_for_cyclic(n,q)
        assert dict(cnt)==expectation,(q,n,cnt,expectation)
        print('exact direct census',q,n,dict(cnt))
    # Arithmetic splitting test: C5 changes from a single d=2 block over F2
    # to two d=1 blocks over F4. Both rank 2 and rank 4 must appear over F4.
    q,n=4,5;F=operations(q);table=dihedral_table(n)
    gen=Random(281828);sample=Counter()
    for _ in range(900):
        x=[gen.randrange(q) for _ in range(2*n)]
        sample[direct_rank(x,table,F)]+=1
    assert sample[2]>0 and sample[4]>0 and set(sample)<={0,2,4},sample
    print('F4 C5 sample rank support',dict(sample))
    print('VERIFY_FIELDS_OK')

if __name__=='__main__':main()
