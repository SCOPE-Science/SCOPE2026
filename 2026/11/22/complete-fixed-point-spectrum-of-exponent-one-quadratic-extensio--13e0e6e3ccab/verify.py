#!/usr/bin/env python3
"""Exact finite-field diagnostics for a fixed-point classification.
No finite test replaces the proof for arbitrary odd prime powers.
"""

def primes_upto(N):
    result = []
    for p in range(2,N+1):
        if all(p % k for k in range(2,int(p**0.5)+1)):
            result.append(p)
    return result

def make_field(p):
    D = next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
    def add(x,y): return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def neg(x): return ((-x[0])%p,(-x[1])%p)
    def mul(x,y): return ((x[0]*y[0]+D*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def power(x,n):
        z=(1,0)
        while n:
            if n & 1: z=mul(z,x)
            x=mul(x,x); n//=2
        return z
    return add,neg,mul,power

def full_test(p):
    add,neg,mul,power=make_field(p)
    v=[(a,b) for a in range(p) for b in range(p)]
    h=(p+1)//2
    hits=[]; total=0; high=[]
    X=[mul(x,power(x,2*(p-1))) for x in v]
    for a in v:
        s=power(neg(a),h)
        admissible = (a==(0,0) and (p+1)%3!=0) or (a!=(0,0) and (s==(p-1,0) or (p!=3 and s==(3%p,0))))
        if not admissible: continue
        total+=1
        values=[add(X[i],mul(a,x)) for i,x in enumerate(v)]
        assert len(set(values))==p*p, ('not permutation',p,a)
        fixed=sum(values[i]==x for i,x in enumerate(v))
        assert fixed in (1,2*p-1), ('bad fixed count',p,a,fixed)
        predicted= (a==(0,0)) or (a!=(0,0) and p%60 in (7,43) and (a[0]!=0 or a[1]!=0) and power(add((1,0),neg(a)),h)==(1,0))
        assert (fixed>1)==predicted,(p,a,fixed,predicted)
        if fixed>1: high.append(a)
    expected_total=(p+1)//2 if p==3 else p+1
    if (p+1)%3!=0: expected_total+=1
    expected_high=int((p+1)%3!=0)+2*int(p%60 in (7,43))
    assert total==expected_total,(p,total,expected_total)
    assert len(high)==expected_high,(p,high,expected_high)
    return total,high

if __name__=='__main__':
    done=0
    for p in [3,5,7,11,13,17,19]:
        n,high=full_test(p)
        print('FIELD_EXHAUSTIVE',p,n,len(high))
        done+=1
    torus=0
    for p in primes_upto(1999):
        if p<=5 or pow(5,(p-1)//2,p)!=p-1: continue
        add,neg,mul,power=make_field(p)
        # Obtain one t with t^2=5 using F_{p^2}; in the nonsquare case
        # use a normalized t in the existing quadratic basis.
        D = next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
        sqrt5 = next((0,b) for b in range(1,p) if (D*b*b-5)%p==0)
        phi=mul(add((1,0),sqrt5),((p+1)//2,0))
        w=power(phi,2)
        u=neg(power(w,2))
        assert add(add(power(u,2),mul((7%p,0),u)),(1,0))==(0,0)
        h=(p+1)//2
        a=add((1,0),neg(u))
        predicted=p%60 in (7,43)
        assert (power(u,h)==(1,0) and power(neg(a),h)==(3%p,0))==predicted,('torus',p)
        torus+=1
    print('FIELD_FIXED_POINT_DIAGNOSTICS_OK',done,'complete prime fields,',torus,'nonsplit torus fields through 1999')
