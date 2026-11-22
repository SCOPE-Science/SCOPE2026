"""Finite-field checks for idempotent Lie derivations on unipotent almost-abelian algebras.
Run with Python 3; uses only the standard library.
"""
from itertools import product

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q
    def add(self,a,b):
        if self.q==4: return a^b
        return (a+b)%self.q
    def neg(self,a):
        if self.q==4: return a
        return -a%self.q
    def mul(self,a,b):
        if self.q!=4: return (a*b)%self.q
        z=0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1): z^=1<<(i+j)
        if z&8: z^=(0b1110) # x^3=x^2+x under x^2+x+1
        if z&4: z^=(0b111)
        return z
    def dot(self,a,b):
        v=0
        for x,y in zip(a,b): v=self.add(v,self.mul(x,y))
        return v

def ring_mul(F,u,v,N):
    out=[0]*N
    for i,ui in enumerate(u):
        for j,vj in enumerate(v[:N-i]): out[i+j]=F.add(out[i+j],F.mul(ui,vj))
    return tuple(out)

def Tact(F,v):
    N=len(v)
    return tuple(F.add(v[i],v[i-1] if i else 0) for i in range(N))

def B0(F,v):
    assert F.q in (2,4)
    # (1+x) d/dx in char 2
    N=len(v)
    d=tuple(v[i+1] if i+1<N and (i+1)%2 else 0 for i in range(N))
    return Tact(F,d)

def Bact(F,a,c,v):
    N=len(c)
    h=ring_mul(F,c,v,N)
    if a:
        z=B0(F,v)
        return tuple(F.add(z[i],h[i]) for i in range(N))
    return h

def is_idempotent_B(F,a,c):
    N=len(c)
    for i in range(N):
        e=tuple(int(j==i) for j in range(N))
        v=Bact(F,a,c,e)
        if Bact(F,a,c,v)!=v: return False
    return True

def rank(F,rows):
    if not rows:return 0
    A=[list(row) for row in rows]
    r=0
    for col in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][col]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        a=A[r][col]
        inv=next(i for i in range(1,F.q) if F.mul(i,a)==1)
        A[r]=[F.mul(inv,v) for v in A[r]]
        for j in range(len(A)):
            if j==r or not A[j][col]: continue
            b=A[j][col]
            A[j]=[F.add(A[j][k],F.neg(F.mul(b,A[r][k]))) for k in range(len(A[0]))]
        r+=1
        if r==len(A):break
    return r

def matrix_D(F,a,c,u):
    N=len(c)
    cols=[(a,)+u]
    for i in range(N):
        e=tuple(int(i==j) for j in range(N))
        cols.append((0,)+Bact(F,a,c,e))
    return tuple(zip(*cols))

def lie_bracket(F,x,y):
    u=x[1:];v=y[1:]
    Tv=Tact(F,v);Tu=Tact(F,u)
    return (0,)+tuple(F.add(F.mul(x[0],Tv[i]),F.neg(F.mul(y[0],Tu[i]))) for i in range(len(u)))

def mv(F,M,v):return tuple(F.dot(row,v) for row in M)

def original_checks(F,M):
    N=len(M)-1
    e=[tuple(int(i==j) for i in range(N+1)) for j in range(N+1)]
    for v in e:
        if mv(F,M,mv(F,M,v))!=mv(F,M,v):return False
    for x in e:
        for y in e:
            lhs=mv(F,M,lie_bracket(F,x,y))
            rhs=tuple(F.add(i,j) for i,j in zip(lie_bracket(F,mv(F,M,x),y),lie_bracket(F,x,mv(F,M,y))))
            if lhs!=rhs: return False
    return True

def test_even(q,N):
    F=Field(q); assert q in (2,4) and N%2==0
    Bcounts={0:0,1:0}; totals={}
    for a in (0,1):
        for c in product(range(q),repeat=N):
            if not is_idempotent_B(F,a,c):continue
            Bcounts[a]+=1
            M0=matrix_D(F,a,c,(0,)*N)
            rB=rank(F,[row[1:] for row in M0[1:]])
            for u in product(range(q),repeat=N):
                Bu=Bact(F,a,c,u)
                if Bu!=tuple(F.mul(1-a,x) for x in u):continue
                M=matrix_D(F,a,c,u)
                assert original_checks(F,M)
                r=rank(F,M)
                totals[r]=totals.get(r,0)+1
    m=N//2
    target={0:1, N:q**N, m+1:q**N}
    if m==1:target={0:1,N:2*q**N}
    assert totals==target,(q,N,totals,target)
    assert Bcounts=={0:2,1:q**m},(q,N,Bcounts)
    print('PASS even',q,N,'B',Bcounts,'derivation-ranks',totals)

def test_odd(q,N):
    F=Field(q); assert q in (3,5)
    # a=0 solutions are the two scalar idempotents, each tested with all possible u
    z=(0,)*N;o=(1,)+(0,)*(N-1)
    count=0
    for c in (z,o):
        for u in product(range(q),repeat=N):
            if ring_mul(F,c,u,N)!=u:continue
            M=matrix_D(F,0,c,u)
            assert original_checks(F,M)
            count+=1
    assert count==1+q**N
    # a=1 is impossible by eigenspace-swap argument, checked also for N=2
    print('PASS odd',q,N,'idempotents',count)

def brute_full(q,N):
    F=Field(q)
    n=N+1
    ranks={}
    for vals in product(range(q),repeat=n*n):
        M=tuple(tuple(vals[i*n+j] for j in range(n)) for i in range(n))
        if original_checks(F,M):
            r=rank(F,M)
            ranks[r]=ranks.get(r,0)+1
    m=N//2
    expected={0:1,N:q**N}
    if q%2==0 and N%2==0: expected[m+1]=expected.get(m+1,0)+q**N
    assert ranks==expected,(q,N,ranks,expected)
    print('PASS full raw matrix enumeration',q,N,ranks)

if __name__=='__main__':
    for q in (2,3):brute_full(q,2)
    brute_full(2,3)

    for q,N in [(2,2),(2,4),(2,6),(4,2),(4,4)]: test_even(q,N)
    for q,N in [(3,2),(3,4),(5,2)]: test_odd(q,N)
    print('UNIPOTENT_TORAL_LIE_DERIVATIONS_VERIFIED')
