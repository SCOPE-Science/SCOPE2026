"""Finite regression for the toroidal open odd-domination phase diagram.
Uses binary Gaussian elimination on the actual adjacency equations.
"""
from math import gcd

def affine_system(m, n):
    N=m*n
    pivots={}
    for i in range(m):
        for j in range(n):
            row=1<<N
            for a,b in (((i-1)%m,j),((i+1)%m,j),(i,(j-1)%n),(i,(j+1)%n)):
                row^=1<<(a*n+b)
            while True:
                col=(row & ((1<<N)-1)).bit_length()-1
                if col<0:
                    if row==(1<<N):return None
                    break
                if col in pivots:row^=pivots[col]
                else:
                    pivots[col]=row
                    break
    sol=0
    for col,row in sorted(pivots.items()):
        if ((row>>N)&1)^((row&sol).bit_count()&1):sol|=1<<col
    basis=[]
    for free in range(N):
        if free in pivots:continue
        v=1<<free
        for col,row in sorted(pivots.items()):
            if (row&v).bit_count()&1:v|=1<<col
        basis.append(v)
    return sol,basis

def translate(v,m,n,axis,step):
    r=0
    for i in range(m):
        for j in range(n):
            a,b=((i+step)%m,j) if axis==0 else (i,(j+step)%n)
            if (v>>(a*n+b))&1:r|=1<<(i*n+j)
    return r

def check():
    checked=0; mixed=0; fully=0; impossible=0
    for m in range(3,17):
        for n in range(3,17):
            x=affine_system(m,n)
            expected=(m%4==0 or n%4==0)
            assert (x is not None)==expected,(m,n,'existence')
            checked+=1
            if x is None:impossible+=1;continue
            sol,basis=x
            N=m*n
            def valid(z):
                for i in range(m):
                    for j in range(n):
                        nei=0
                        for a,b in (((i-1)%m,j),((i+1)%m,j),(i,(j-1)%n),(i,(j+1)%n)):
                            nei^=(z>>(a*n+b))&1
                        if nei!=1:return False
                return True
            assert valid(sol),(m,n,'particular')
            assert all(valid(sol^v) for v in basis),(m,n,'basis')
            if (m%4==0)^(n%4==0):
                mixed+=1
                if m%4: a=m//(m&-m);axis=1
                else:a=n//(n&-n);axis=0
                step=2*a
                assert translate(sol,m,n,axis,step)^sol==(1<<N)-1,(m,n,'anti',step)
                assert all(translate(v,m,n,axis,step)==v for v in basis),(m,n,'kernel anti',step)
                if len(basis)<=12:
                    for bits in range(1<<len(basis)):
                        z=sol
                        for k,v in enumerate(basis):
                            if (bits>>k)&1:z^=v
                        assert z.bit_count()==N//2,(m,n,'weight')
            if m%4==n%4==0:
                fully+=1
                perfect=0
                for i in range(m):
                    for j in range(n):
                        if (i%4,j%4) in ((0,0),(0,1),(2,2),(2,3)):perfect|=1<<(i*n+j)
                assert valid(perfect) and perfect.bit_count()==N//4,(m,n,'perfect')
    print('PASS: sizes 3..16 x 3..16:',checked,'solvable mixed:',mixed,'both fourfold:',fully,'none:',impossible)

if __name__=='__main__':check()
