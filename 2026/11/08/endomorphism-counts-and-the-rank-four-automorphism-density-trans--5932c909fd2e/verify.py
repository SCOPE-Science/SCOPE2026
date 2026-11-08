"""Standalone finite-field checks for square-zero endomorphism counts.
No external packages are required.
"""
from itertools import product
from collections import Counter


def mul(a,b,n,p):
    out=[0]*(1<<n)
    for i,ai in enumerate(a):
        if not ai: continue
        for j,bj in enumerate(b):
            if bj and not(i&j):
                out[i|j]=(out[i|j]+ai*bj)%p
    return out


def matrix_rank_mod(M,p):
    A=[row[:] for row in M]
    height=len(A); width=len(A[0]) if A else 0
    row=0
    for col in range(width):
        pivot=next((i for i in range(row,height) if A[i][col]%p),None)
        if pivot is None: continue
        A[row],A[pivot]=A[pivot],A[row]
        inv=pow(A[row][col],-1,p)
        for j in range(col,width): A[row][j]=(A[row][j]*inv)%p
        for i in range(row+1,height):
            c=A[i][col]
            if c:
                for j in range(col,width): A[i][j]=(A[i][j]-c*A[row][j])%p
        row+=1
        if row==height: break
    return row


def squarezero_distribution(n,p):
    counts=Counter()
    num_squares=0
    for coeff in product(range(p),repeat=(1<<n)-1):
        u=(0,)+coeff
        if any(mul(u,u,n,p)): continue
        num_squares+=1
        cols=[mul(u,[int(j==k) for j in range(1<<n)],n,p) for k in range(1<<n)]
        rank=matrix_rank_mod([list(t) for t in zip(*cols)],p)
        counts[rank]+=1
    return num_squares,counts


def theoretical_odd_n4(p):
    return p**7*(p**3+5*p-5)


def run():
    for p in (3,5):
        N,rank_counts=squarezero_distribution(3,p)
        assert N==p**3*(4*p-3)
        expected={0:1,1:p-1,2:p*(p**3-1),4:3*(p-1)*p**3}
        assert dict(rank_counts)==expected, (p,rank_counts,expected)
        independently_weighted=sum(count*p**(8-rank) for rank,count in rank_counts.items())
        assert independently_weighted==theoretical_odd_n4(p)
        print(f"ODD_{p}: squarezeros_B3={N}, annihilator_ranks={dict(sorted(rank_counts.items()))}, squarezeros_B4={independently_weighted}")
    for p in (2,3,5):
        for n in (1,2):
            N,_=squarezero_distribution(n,p)
            predicted=p**((1<<n)-1) if p==2 else (p if n==1 else p*(2*p-1))
            assert N==predicted,(n,p,N,predicted)
        print(f"SMALL_{p}: OK")
    # Direct exhaustive binary four-variable square-zero test: 2^15 elements.
    N4_binary,_=squarezero_distribution(4,2)
    assert N4_binary==32768
    print(f'BINARY_4: squarezeros={N4_binary}')
    # Independently count invertible substitution pairs for n=2, q=3.
    nilpotents=[]
    for coeff in product(range(3),repeat=3):
        y=(0,)+coeff
        if not any(mul(y,y,2,3)): nilpotents.append(y)
    automorphisms=0
    for y,z in product(nilpotents,repeat=2):
        if (y[1]*z[2]-y[2]*z[1])%3: automorphisms+=1
    assert automorphisms==2*(3-1)**2*3**2==72
    print(f'AUT_2_ODD_3: {automorphisms}')
    print('VERIFY_OK')
if __name__=='__main__': run()
