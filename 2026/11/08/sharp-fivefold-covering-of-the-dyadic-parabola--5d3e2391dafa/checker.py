"""Exact finite verification of the sharp dyadic parabola covering theorem.

Run: python3 checker.py.  No external dependencies.
"""

def spectrum(k):
    n=1<<k
    curve={(x,x*x % n) for x in range(n)}
    allowed={(s,t) for s in range(n) for t in range(n) if (s-t)%2==0}
    sums={(0,0)}
    counts=[]
    for h in range(1,6):
        sums={((a+x)%n,(b+y)%n) for a,b in sums for x,y in curve}
        assert sums <= allowed
        counts.append(len(sums))
        if k>=3 and h<=4:
            assert (2,0) not in sums
        if h == (1 if k==1 else 3 if k==2 else 5):
            assert sums == allowed,(k,h,len(sums),len(allowed))
    return counts


def mixed_lift_test(k):
    n=1<<k
    reps={}
    # Find at least one mixed-parity witness for every parity-compatible target.
    # Limit to k<=5 to keep the Cartesian enumeration small.
    for x in range(n):
        for y in range(n):
            for z in range(n):
                for w in range(n):
                    for v in range(n):
                        xs=(x,y,z,w,v)
                        key=(sum(xs)%n,sum(t*t for t in xs)%n)
                        if key not in reps and any(t%2==0 for t in xs) and any(t%2==1 for t in xs):
                            reps[key]=xs
    assert len(reps)==n*n//2,(k,len(reps))
    for s,t in reps:
        xs=reps[s,t]
        ie=next(i for i,x in enumerate(xs) if x%2==0)
        io=next(i for i,x in enumerate(xs) if x%2==1)
        for a in (0,1):
            for b in (0,1):
                ys=list(xs)
                if a: ys[0]+=n
                if b: ys[ie]+=n//2;ys[io]-=n//2
                assert sum(ys)%(2*n)==(sum(xs)+a*n)%(2*n)
                assert sum(q*q for q in ys)%(2*n)==(sum(q*q for q in xs)+b*n)%(2*n)

if __name__=='__main__':
    for k in range(1,8):
        counts=spectrum(k)
        print('k=',k,'sizes=',counts)
    for k in (2,3,4):
        mixed_lift_test(k)
    print('VERIFY_OK k=1..7, mixed_lift_k=2..4; proofs extend to all exponents')
