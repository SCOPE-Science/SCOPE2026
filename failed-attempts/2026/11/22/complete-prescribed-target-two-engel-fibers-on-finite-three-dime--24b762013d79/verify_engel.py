"""Independent exhaustive check of finite-field second Engel fibers.

Uses direct 2x2 matrix products, not the adjoint-square identity.
Run: python3 verify_engel.py
"""
from collections import Counter
from itertools import product


def field(p, m=1):
    """Arithmetic for F_p, F_4=F_2[t]/(t^2+t+1), F_9=F_3[t]/(t^2+1)."""
    if m == 1:
        return p, lambda a,b:(a+b)%p, lambda a,b:(a*b)%p
    assert (p,m) in [(2,2),(3,2)]
    q=p*p
    def add(a,b):
        return ((a%p+b%p)%p)+p*((a//p+b//p)%p)
    def mul(a,b):
        x,y=a%p,a//p
        z,w=b%p,b//p
        if p==2: # t^2 = t+1
            return ((x*z+y*w)%p)+p*((x*w+y*z+y*w)%p)
        # t^2 = -1
        return ((x*z-y*w)%p)+p*((x*w+y*z)%p)
    return q,add,mul


def test_case(p,m=1):
    q,add,mul=field(p,m)
    zero=0
    def neg(a):
        return next(t for t in range(q) if add(a,t)==zero)
    def sub(a,b):return add(a,neg(b))
    elements=list(product(range(q),repeat=3))
    def prod(U,V):
        a,b,c=U;d,e,f=V
        return (add(mul(a,d),mul(b,f)),
                sub(mul(a,e),mul(b,d)),
                sub(mul(c,d),mul(a,f)),
                add(mul(c,e),mul(a,d)))
    def bracket(U,V):
        uv=prod(U,V);vu=prod(V,U)
        return tuple(sub(uv[i],vu[i]) for i in range(3))
    counter=Counter()
    for X in elements:
        for Y in elements:
            counter[bracket(X,bracket(X,Y))]+=1
    if p==2:
        assert counter==Counter({(0,0,0):q**6}), (p,m,counter)
        return (q,len(counter),q**6)
    squares={mul(t,t) for t in range(1,q)}
    strata=Counter()
    for Z in elements:
        a,b,c=Z; Q=add(mul(a,a),mul(b,c))
        if Z==(0,0,0): expected=2*q**4-q**2; name='zero'
        elif Q==0: expected=2*q**2*(q-1);name='isotropic'
        elif Q in squares: expected=q*(q-1)**2;name='square'
        else: expected=q*(q*q-1);name='nonsquare'
        assert counter[Z]==expected,(q,Z,Q,name,counter[Z],expected)
        strata[name]+=1
    assert strata==Counter({'zero':1,'isotropic':q*q-1,
                            'square':q*(q*q-1)//2,
                            'nonsquare':q*(q-1)**2//2}),strata
    assert sum(counter.values())==q**6
    return (q,len(counter),dict(strata))


if __name__=='__main__':
    for p,m in [(2,1),(2,2),(3,1),(3,2),(5,1),(7,1)]:
        print('verified',test_case(p,m))
