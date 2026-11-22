"""Independent finite checks for a symmetry orbit formula on finite crown posets.
No external dependencies; execute with Python 3.9 or newer.
"""
from math import gcd


def fib(k):
    a,b=0,1
    for _ in range(k):a,b=b,a+b
    return a


def lucas(k):
    a,b=2,1
    for _ in range(k):a,b=b,a+b
    return a


def totient(k):
    return sum(gcd(i,k)==1 for i in range(1,k+1))


def predicted(n):
    rot=sum(totient(n//d)*lucas(2*d) for d in range(1,n+1) if n%d==0)
    return 2+fib(n+3)+rot//n,rot


def ideals(n):
    full=(1<<n)-1
    output=[]
    for a in range(1<<n):
        eligible=0
        for j in range(n):
            if a&(1<<j) and a&(1<<((j+1)%n)):
                eligible|=1<<j
        sub=eligible
        while True:
            output.append(a | (sub<<n))
            if sub==0:break
            sub=(sub-1)&eligible
    return output


def profiles(n):
    """All consistent one-point extensions, constructed directly from ideals/filters/bicliques."""
    base=set(ideals(n))
    assert len(base)==lucas(2*n),(n,len(base),lucas(2*n))
    full=(1<<(2*n))-1
    out={(L,0) for L in base} | {(0,full^I) for I in base}
    A=(1<<n)-1
    B=A<<n
    for subset in range(1,1<<n):
        possible=B
        for i in range(n):
            if (subset>>i)&1:
                possible &= ((1<<i)|(1<<((i-1)%n)))<<n
        choices=possible
        while choices:
            out.add((subset, choices))
            choices=(choices-1)&possible
    assert len(out)==2*lucas(2*n)-1+4*n,(n,len(out))
    return out


def map_mask(n,mask,k,sgn):
    ans=0
    for i in range(n):
        if mask>>i&1: ans |= 1<<((sgn*i+k)%n)
        if mask>>(n+i)&1:
            j=(i+k)%n if sgn==1 else (k-i-1)%n
            ans |= 1<<(n+j)
    return ans


def map_profile(n,p,k,sgn):
    return (map_mask(n,p[0],k,sgn),map_mask(n,p[1],k,sgn))


def run():
    for n in range(5,10):
        ps=profiles(n)
        unseen=set(ps)
        orbit_count=0
        while unseen:
            p=next(iter(unseen))
            orbit={map_profile(n,p,k,sgn) for k in range(n) for sgn in (-1,1)}
            assert orbit <= ps
            unseen.difference_update(orbit)
            orbit_count+=1
        expected,rotation_sum=predicted(n)
        assert orbit_count==expected,(n,orbit_count,expected)
        # Full fixed-point character, tested without Burnside.
        for k in range(n):
            fixed_rot=sum(map_profile(n,p,k,1)==p for p in ps)
            want_rot=(2*lucas(2*n)+4*n-1) if k==0 else (2*lucas(2*gcd(n,k))-1)
            assert fixed_rot==want_rot,(n,k,fixed_rot,want_rot)
            fixed_ref=sum(map_profile(n,p,k,-1)==p for p in ps)
            assert fixed_ref==2*fib(n+3)+1,(n,k,fixed_ref,2*fib(n+3)+1)
        fixref=[]
        for k in range(n):
            # Count fixed lower sets (rather than types) independently
            j=sum(map_mask(n,I,k,-1)==I for I in ideals(n))
            assert j==fib(n+3),(n,k,j,fib(n+3))
            fixref.append(j)
        print(f'n={n}: types={len(ps)}, symmetry_orbits={orbit_count}, fixed_ideal_reflections={set(fixref)}, PASS')
    # The all-index modular arithmetic formula is also exercised without enumeration.
    for n in range(5,51):
        pred,rot=predicted(n)
        assert rot%n==0,(n,rot)
        assert pred>0
    print('ALL_CHECKS_OK')


if __name__=='__main__':run()
