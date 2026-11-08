"""Reproduce rank-refined counts of square-zero matrices over finite local rings.

Run with Python 3: python verify_squarezero.py
"""
from itertools import product
from math import prod


def gaussian(n, k, q):
    if not 0 <= k <= n:
        return 0
    num = prod(q ** (n - i) - 1 for i in range(k))
    den = prod(q ** (k - i) - 1 for i in range(k))
    assert num % den == 0
    return num // den


def gl(k, q):
    return prod(q ** k - q ** i for i in range(k))


def count_formula(n, q, d):
    return [gaussian(n, t, q) * gaussian(n - t, t, q) * gl(t, q)
            * q ** (d * ((n-t)**2 + t*t))
            for t in range(n//2+1)]


def modring(k, q=None):
    q = q or k
    return (k, lambda a, b:(a+b)%k, lambda a, b:(a*b)%k, lambda x:x%q, q)


def dual(q):
    return (q*q,lambda a,b:(a%q+b%q)%q + q*((a//q+b//q)%q),
           lambda a,b:(a%q*b%q)%q + q*(((a%q)*(b//q)+(a//q)*(b%q))%q),
           lambda a:a%q,q)


def square2():
    return (8,lambda a,b:a^b,
            lambda a,b:((a&1)*(b&1)) ^ ((((a&1)*((b>>1)&1)+((a>>1)&1)*(b&1))&1)<<1) ^ ((((a&1)*((b>>2)&1)+((a>>2)&1)*(b&1))&1)<<2),
            lambda a:a&1,2)



def squarezero_local(q, d):
    # F_q[u_1,...,u_d]/(u_i*u_j for all i,j); q prime in these checks.
    order=q**(d+1)
    def digits(x):
        out=[]
        for _ in range(d+1):
            out.append(x%q); x//=q
        return out
    digits_table=[digits(x) for x in range(order)]
    def encode(ds):
        return sum(a*(q**i) for i,a in enumerate(ds))
    def add(a,b):
        x=digits_table[a]; y=digits_table[b]
        return encode([(x[i]+y[i])%q for i in range(d+1)])
    def mul(a,b):
        x=digits_table[a]; y=digits_table[b]
        return encode([(x[0]*y[0])%q]+[(x[0]*y[i]+y[0]*x[i])%q for i in range(1,d+1)])
    return (order,add,mul,lambda a:a%q,q)

def rank_mod(mat, n, q):
    a=[list(mat[i*n:(i+1)*n]) for i in range(n)]
    rank=0
    for col in range(n):
        pivot=next((j for j in range(rank,n) if a[j][col]%q),None)
        if pivot is None:
            continue
        a[pivot],a[rank]=a[rank],a[pivot]
        fac=pow(a[rank][col],-1,q)
        a[rank]=[(v*fac)%q for v in a[rank]]
        for r in range(n):
            if r!=rank and a[r][col]:
                k=a[r][col]
                a[r]=[(a[r][i]-k*a[rank][i])%q for i in range(n)]
        rank+=1
    return rank


def census(n, ring, label):
    order,add,mul,residue,q=ring
    M=[[mul(a,b) for b in range(order)] for a in range(order)]
    observed=[0]*(n//2+1)
    for x in product(range(order),repeat=n*n):
        valid=True
        for i in range(n):
            for j in range(n):
                z=0
                for k in range(n):
                    z=add(z,M[x[i*n+k]][x[k*n+j]])
                if z:
                    valid=False
                    break
            if not valid:break
        if valid:
            t=rank_mod(tuple(residue(v) for v in x),n,q)
            assert t <= n//2
            observed[t]+=1
    d=0 if order==q else round(__import__('math').log(order/q,q))
    expected=count_formula(n,q,d)
    assert observed==expected,(label,n,observed,expected)
    print(f'{label} n={n}: reduction-rank counts {observed} OK')


def anti_dim(n,t,q):
    # A has t nontrivial length-two Jordan blocks; coefficient-matrix rank.
    a=[[0]*n for _ in range(n)]
    for k in range(t):a[2*k][2*k+1]=1
    eq=[]
    for i in range(n):
        for j in range(n):
            row=[0]*(n*n)
            for k in range(n):
                row[k*n+j]=(row[k*n+j]+a[i][k])%q
                row[i*n+k]=(row[i*n+k]+a[k][j])%q
            eq.append(row)
    rank=0
    for j in range(n*n):
        piv=next((i for i in range(rank,len(eq)) if eq[i][j]),None)
        if piv is None:continue
        eq[piv],eq[rank]=eq[rank],eq[piv]
        inv=pow(eq[rank][j],-1,q)
        eq[rank]=[(v*inv)%q for v in eq[rank]]
        for i in range(len(eq)):
            if i!=rank and eq[i][j]:
                c=eq[i][j]
                eq[i]=[(eq[i][k]-c*eq[rank][k])%q for k in range(n*n)]
        rank+=1
    dim=n*n-rank
    assert dim==(n-t)**2+t*t,(q,n,t,dim)


def run():
    for q in (2,3,5):
        for n in range(1,8):
            for t in range(n//2+1):
                f=count_formula(n,q,1)[t]
                assert f>=0
            if n<=4:
                for t in range(n//2+1):anti_dim(n,t,q)
    census(2,modring(2),'F2')
    census(3,modring(2),'F2')
    census(2,modring(3),'F3')
    census(2,modring(4,2),'Z4')
    census(3,modring(4,2),'Z4')
    census(2,dual(2),'F2[eps]/eps2')
    census(3,dual(2),'F2[eps]/eps2')
    census(2,modring(9,3),'Z9')
    census(2,dual(3),'F3[eps]/eps2')
    census(2,square2(),'F2[u,v]/(u,v)^2')
    census(2,squarezero_local(3,2),'F3[u,v]/(u,v)^2')
    census(2,squarezero_local(2,3),'F2[u,v,w]/(u,v,w)^2')
    print('VERIFY_OK')

if __name__=='__main__':run()
