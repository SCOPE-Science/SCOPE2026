"""Standalone exact-integer checks for quartic-graph progression counts and extension classification.
Requires only Python 3 standard library. No external data or downloads.
"""
from math import gcd
from random import Random


def prime_powers(n):
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            k=0
            while n%p==0:n//=p;k+=1
            out.append((p,k))
        p+=1 if p==2 else 2
    if n>1:out.append((n,1))
    return out


def valuation(a,p,k):
    if a%p**k==0:return k
    s=0
    while a%p==0:
        a//=p;s+=1
    return s


def local_class(p,k,y,h):
    """Return (is_4AP, extends_to_5) from the claimed valuation classification."""
    s=valuation(h,p,k)
    t=valuation(y,p,k)
    a=(k+3)//4
    b=(k+1)//2
    full=(s>=a and t>=max(0,b-s))
    exceptional=(p==5 and k%4==1 and s==(k-1)//4 and t>=s+1)
    assert not(full and exceptional)
    return (full or exceptional),full


def local_counts(p,k):
    a=(k+3)//4
    b=(k+1)//2
    full=p**(k+k//2)+(b-a)*(p-1)*p**(k+k//2-1)
    exception=4*5**(3*(k-1)//2) if p==5 and k%4==1 else 0
    return full,exception


def crt_counts(n):
    full=total=1
    for p,k in prime_powers(n):
        f,e=local_counts(p,k)
        full*=f;total*=f+e
    return full,total


def brute_4ap(n):
    inv2=pow(2,-1,n)
    got=0;full=0
    for h in range(n):
        hs=[(j*h)%n for j in range(5)]
        for x in range(n):
            vals=[pow((x+hh)%n,4,n) for hh in hs]
            is4=(vals[2]-2*vals[1]+vals[0])%n==0 and (vals[3]-2*vals[2]+vals[1])%n==0
            is5=is4 and (vals[4]-2*vals[3]+vals[2])%n==0
            y=(x+3*h*inv2)%n
            local=[local_class(p,k,y%(p**k),h%(p**k)) for p,k in prime_powers(n)]
            predicted4=all(a for a,b in local)
            predicted5=all(b for a,b in local)
            assert is4==predicted4,(n,x,h,is4,predicted4)
            assert is5==(is4 and predicted5),(n,x,h,is5,predicted5)
            got+=is4;full+=is5
    return full,got


def verify():
    tested=0; ns=[]
    for n in range(5,151):
        if gcd(n,6)!=1:continue
        actual=brute_4ap(n)
        predicted=crt_counts(n)
        assert actual==predicted,(n,actual,predicted)
        ns.append(n);tested+=n*n
    for p,k in [(5,3),(5,4),(7,3),(11,2),(13,2),(17,2),(5,5)]:
        n=p**k
        full,ex=local_counts(p,k)
        if n<=625:
            assert brute_4ap(n)==(full,full+ex)
        else:
            rng=Random(20261106)
            for _ in range(10000):
                y=rng.randrange(n);h=rng.randrange(n)
                x=(y-3*h*pow(2,-1,n))%n
                vals=[pow((x+j*h)%n,4,n) for j in range(5)]
                is4=(vals[2]-2*vals[1]+vals[0])%n==0 and (vals[3]-2*vals[2]+vals[1])%n==0
                is5=is4 and (vals[4]-2*vals[3]+vals[2])%n==0
                prediction=local_class(p,k,y,h)
                assert (is4,is5)==prediction,(p,k,y,h,prediction,is4,is5)
            # Construct explicitly all three types of special components.
            for h in range(5,n,25):
                for y in range(0,n,25):
                    x=(y-3*h*pow(2,-1,n))%n
                    vals=[pow((x+j*h)%n,4,n) for j in range(5)]
                    assert (vals[2]-2*vals[1]+vals[0])%n==0
                    assert (vals[3]-2*vals[2]+vals[1])%n==0
                    assert (vals[4]-2*vals[3]+vals[2])%n!=0
    print('VERIFY_OK composite_moduli=',len(ns),'exhaustive_start_step_pairs=',tested)
    print('prime_power_tests=5^3,5^4,7^3,11^2,13^2,17^2; random/exceptions at 5^5')
    print('sample_local_counts_5=',[(k,local_counts(5,k)) for k in range(1,10)])

if __name__=='__main__':verify()
