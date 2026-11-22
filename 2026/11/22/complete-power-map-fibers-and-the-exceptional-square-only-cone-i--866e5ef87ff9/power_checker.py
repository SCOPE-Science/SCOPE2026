"""Independent finite-field enumeration for power fibers in rectangular-band algebras."""
import itertools
from collections import Counter
from math import gcd


def operations(p, degree, modulus):
    q = p**degree
    def digits(t):
        out=[]
        for _ in range(degree):
            out.append(t % p);t //=p
        return out
    def pack(coefs):
        return sum((c%p)*p**i for i,c in enumerate(coefs))
    add=[[pack([a+b for a,b in zip(digits(x),digits(y))]) for y in range(q)] for x in range(q)]
    mul=[]
    for x in range(q):
        row=[]
        for y in range(q):
            f=[0]*(2*degree-1)
            for i,a in enumerate(digits(x)):
                for j,b in enumerate(digits(y)):
                    f[i+j]+=a*b
            for k in range(len(f)-1,degree-1,-1):
                for i,c in enumerate(modulus):
                    f[k-degree+i]-=f[k]*c
                f[k]=0
            row.append(pack(f[:degree]))
        mul.append(row)
    return q,add,mul


def expected_fiber(Z,m,n,k,q,add,mul):
    d=(m-1)*(n-1)
    if not any(Z):
        return (q**d*(q**(m-1)+q**(n-1)-1) if k==2 else q**(m*n-1))
    # rank at most one
    nz=next((i for i,x in enumerate(Z) if x),None)
    assert nz is not None
    i0,j0=divmod(nz,n)
    for i in range(m):
        for j in range(n):
            if mul[Z[i*n+j0]][Z[i0*n+j]]!=mul[Z[i*n+j]][Z[nz]]:
                return 0
    sr=[0]*m;sc=[0]*n
    for i in range(m):
        for j in range(n):
            z=Z[i*n+j]
            sr[i]=add[sr[i]][z];sc[j]=add[sc[j]][z]
    total=0
    for v in sr:total=add[total][v]
    if not total:
        return (q-1)*q**d if k==2 and not any(sr) and not any(sc) else 0
    roots=sum(1 for a in range(q) if _pow(a,k,mul)==total)
    return roots*q**d


def _pow(a,k,mul):
    ans=1
    for _ in range(k):ans=mul[ans][a]
    return ans


def direct_power(x,m,n,k,add,mul):
    # Directly multiply full coefficient matrices via the basis semigroup law.
    def product(a,b):
        out=[0]*(m*n)
        for i in range(m):
            for j in range(n):
                for h in range(m):
                    for l in range(n):
                        out[i*n+l]=add[out[i*n+l]][mul[a[i*n+j]][b[h*n+l]]]
        return tuple(out)
    ans=x
    for _ in range(k-1):ans=product(ans,x)
    return ans


def check(p, degree, modulus,m,n,ks):
    q,add,mul=operations(p,degree,modulus)
    elems=list(itertools.product(range(q),repeat=m*n))
    for k in ks:
        counts=Counter(direct_power(x,m,n,k,add,mul) for x in elems)
        for z in elems:
            want=expected_fiber(z,m,n,k,q,add,mul)
            got=counts[z]
            if got!=want:
                raise AssertionError((p,degree,m,n,k,z,got,want))
        print('PASS',f'q={q}',f'm={m}',f'n={n}',f'k={k}',f'targets={len(elems)}',f'image={len(counts)}')

if __name__=='__main__':
    for args in [
        (2,1,[0,1],1,2,[2,3,5]),
        (2,1,[0,1],2,2,[2,3,4,5]),
        (2,1,[0,1],2,3,[2,3,4]),
        (2,1,[0,1],3,3,[2,3]),
        (3,1,[0,1],2,2,[2,3,4,5]),
        (3,1,[0,1],2,3,[2,3,4]),
        (5,1,[0,1],2,2,[2,3,4]),
        (2,2,[1,1,1],2,2,[2,3,4,5]),
        (3,2,[1,0,1],2,2,[2,3,4]),
    ]:
        check(*args)
