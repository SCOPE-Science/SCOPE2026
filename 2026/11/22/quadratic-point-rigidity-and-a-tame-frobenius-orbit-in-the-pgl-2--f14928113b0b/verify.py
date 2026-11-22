"""Independent finite-field census for the smooth Borges--Korchmaros--Speziali pencil.
No third-party packages are needed.
"""
from itertools import product


def census(p):
    assert p >= 5 and all(p % a for a in range(2, int(p ** .5) + 1))
    D = next(d for d in range(2, p) if pow(d, (p-1)//2, p)==p-1)
    K = [(a,b) for a in range(p) for b in range(p)]
    def mul(u,v):
        a,b=u; c,d=v
        return ((a*c+D*b*d)%p, (a*d+b*c)%p)
    def power(u,n):
        out=(1,0)
        while n:
            if n&1: out=mul(out,u)
            u=mul(u,u); n//=2
        return out
    zero=(0,0)
    def sub(u,v):return ((u[0]-v[0])%p,(u[1]-v[1])%p)
    def scale(u,a):return ((u[0]*a)%p,(u[1]*a)%p)
    expected=(p**3+p+2)//2
    for lam in range(p):
        if lam in (1,p-1):continue
        count2=1
        for x,y in product(K,repeat=2):
            N=power(y,p+1)
            Trx=sub(power(x,p),scale(x,-1))
            w=sub(mul(y,y),scale(x,2))
            v=sub(sub(N,Trx),scale(power(w,(p+1)//2),lam))
            if v==zero: count2+=1
        target=p**3+1 if lam==0 else expected
        assert count2 == target,(p,lam,count2,target)
    print(f'p={p} extension-F_(p^2) counts: lambda=0 -> {p**3+1}, all lambda nonzero except +-1 -> {expected}')
    return expected

if __name__=='__main__':
    for p in (5,7,11):
        census(p)
    print('INDEPENDENT_BRUTE_FORCE_POINT_COUNT_CHECKS_PASSED')
