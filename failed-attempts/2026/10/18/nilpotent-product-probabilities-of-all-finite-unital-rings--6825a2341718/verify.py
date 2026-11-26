"""Independent exhaustive finite tests for nilpotent-product probabilities.
Run with: python verify.py
Only the stated finite instances are tested; a general proof is separate.
"""
from itertools import product
from collections import Counter
from fractions import Fraction


def mul(A, B, n, add, times, z=0):
    out=[]
    for i in range(n):
        for j in range(n):
            v=z
            for k in range(n):
                v=add(v, times(A[i*n+k], B[k*n+j]))
            out.append(v)
    return tuple(out)


def zero_power(A, n, add, times, bound):
    zero = (0,)*(n*n)
    P = A
    for _ in range(1, bound+1):
        if P == zero:
            return True
        P = mul(P, A, n, add, times)
    return False


def rank_mod_p(A, n, p):
    a=[list(A[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for c in range(n):
        k=next((k for k in range(r,n) if a[k][c] % p),None)
        if k is None:continue
        a[k],a[r]=a[r],a[k]
        inv=pow(a[r][c],-1,p)
        a[r]=[x*inv%p for x in a[r]]
        for k in range(n):
            if k!=r:
                f=a[k][c]
                a[k]=[(a[k][j]-f*a[r][j])%p for j in range(n)]
        r+=1
    return r


def check_field(p,n):
    mats=list(product(range(p),repeat=n*n))
    good=Counter(); rows=Counter()
    add=lambda a,b:(a+b)%p
    times=lambda a,b:(a*b)%p
    for A in mats:
        rank=rank_mod_p(A,n,p)
        rows[rank]+=1
        for B in mats:
            C=mul(A,B,n,add,times)
            if zero_power(C,n,add,times,n):good[rank]+=1
    expected=(2*p**n-1)*p**(2*n*n-2*n)
    assert sum(good.values())==expected,(p,n,sum(good.values()),expected)
    for r,number in rows.items():
        assert good[r]==number*p**(n*n-r),(p,n,r,good[r])
    print(f'M_{n}(F_{p}): {sum(good.values())}/{len(mats)**2}; ranks={dict(sorted(good.items()))}; PASS')


def mul_dual(a,b):
    return ((a&1)&(b&1)) | (((((a&1)*((b>>1)&1)) ^ (((a>>1)&1)*(b&1)))&1)<<1)


def check_dual_matrix():
    n=2
    mats=list(product(range(4),repeat=4))
    good=0
    for A in mats:
        for B in mats:
            C=mul(A,B,n,int.__xor__,mul_dual)
            if zero_power(C,n,int.__xor__,mul_dual,4): good+=1
    assert good==len(mats)**2*7//16
    print(f'M_2(F_2[eps]/eps^2): {good}/{len(mats)**2}; PASS')


def mul_local(a,b):
    # Basis 1,x,y,xy; relations x*x=y*y=y*x=0, x*y=xy, all products of length >= 3 zero.
    res=0
    for i in range(4):
        if (a>>i)&1:
            for j in range(4):
                if (b>>j)&1:
                    if i==0:res^=1<<j
                    elif j==0:res^=1<<i
                    elif (i,j)==(1,2):res^=1<<3
    return res


def check_local():
    a=list(range(16)); good=0
    for x in a:
        for y in a:
            z=mul_local(x,y)
            v=z
            for power in range(1,5):
                if v==0:
                    good+=1
                    break
                v=mul_local(v,z)
    assert mul_local(2,4)!=mul_local(4,2)
    assert good==192
    print(f'16-element noncommutative local ring: {good}/256; PASS')


def check_upper():
    # Encode [[a,b],[0,c]] with a,b,c in F_2.
    def mult(x,y):
        a,b,c=x&1,(x>>1)&1,(x>>2)&1
        d,e,f=y&1,(y>>1)&1,(y>>2)&1
        return (a*d)|((a*e^b*f)<<1)|((c*f)<<2)
    good=0
    for a in range(8):
        for b in range(8):
            x=mult(a,b)
            if mult(mult(x,x),x)==0:good+=1
    assert good==36
    print(f'Upper triangular M_2(F_2): {good}/64; PASS')


if __name__=='__main__':
    for p,n in [(2,1),(3,1),(2,2),(3,2),(2,3)]:
        check_field(p,n)
    check_dual_matrix()
    check_local()
    check_upper()
