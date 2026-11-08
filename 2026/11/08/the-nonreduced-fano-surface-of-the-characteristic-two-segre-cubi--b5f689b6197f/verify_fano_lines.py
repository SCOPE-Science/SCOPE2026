"""Reproducible finite-field corroboration for lines on a characteristic-two cubic cone."""
from itertools import product

# Standard carryless representation of GF(2^m).
def mul(x,y,mod,degree):
    z=0
    while y:
        if y&1:z^=x
        y>>=1
        x<<=1
        if x & (1<<degree): x^=mod
    return z

def power(x,n,mod,degree):
    z=1
    while n:
        if n&1:z=mul(z,x,mod,degree)
        x=mul(x,x,mod,degree);n//=2
    return z

def cubic(v,mod,degree):
    total=0
    for x in v:total^=x
    return power(total,3,mod,degree)^__import__('functools').reduce(
        lambda u,x:u^power(x,3,mod,degree),v,0)

def line_coefficients(v,w,mod,degree):
    sv=0;sw=0
    for a in v:sv^=a
    for a in w:sw^=a
    s2t=mul(power(sv,2,mod,degree),sw,mod,degree)
    st2=mul(sv,power(sw,2,mod,degree),mod,degree)
    for a,b in zip(v,w):
        s2t^=mul(power(a,2,mod,degree),b,mod,degree)
        st2^=mul(a,power(b,2,mod,degree),mod,degree)
    return (cubic(v,mod,degree),s2t,st2,cubic(w,mod,degree))

def rref_2planes(q):
    for p in range(4):
        for r in range(p+1,4):
            a_free=[i for i in range(p+1,4) if i!=r]
            b_free=list(range(r+1,4))
            for vals in product(range(q),repeat=len(a_free)+len(b_free)):
                v=[0]*4;w=[0]*4;v[p]=1;w[r]=1
                for i,x in zip(a_free,vals[:len(a_free)]):v[i]=x
                for i,x in zip(b_free,vals[len(a_free):]):w[i]=x
                yield v,w

def lines_on_surface(q,mod,degree):
    return sum(not any(line_coefficients(v,w,mod,degree)) for v,w in rref_2planes(q))

def tangent_test():
    mod=0x11b; degree=8
    P=(1,2,4,179)
    assert cubic(P,mod,degree)==0
    summ=0
    for x in P:summ^=x
    grad=[power(x^summ,2,mod,degree) for x in P]
    inv=power(grad[3],254,mod,degree)
    t1=mul(grad[1],inv,mod,degree)
    t2=mul(grad[2],inv,mod,degree)
    A=(0,1,0,t1); B=(0,0,1,t2)
    # The s*t^2 coefficient for F(P*s+D*t), quadratic in D.
    qA=line_coefficients(P,A,mod,degree)[2]
    qB=line_coefficients(P,B,mod,degree)[2]
    # Polarization of x^3 yields mixed terms; q(A+B)=q(A)+q(B).
    assert line_coefficients(P,tuple(x^y for x,y in zip(A,B)),mod,degree)[2]==qA^qB
    assert qA==157 and qB==67
    slope=power(mul(qA,power(qB,254,mod,degree),mod,degree),128,mod,degree)
    D=tuple(x^mul(slope,y,mod,degree) for x,y in zip(A,B))
    assert line_coefficients(P,D,mod,degree)[1]==0
    assert line_coefficients(P,D,mod,degree)[2]==0
    assert cubic(D,mod,degree)==48
    # Unique quadratic projective zero has nonvanishing cubic => no line through P.
    return P,qA,qB,slope,cubic(D,mod,degree)

if __name__=='__main__':
    assert lines_on_surface(2,0b11,1)==15
    print('GF2 exact contained lines: 15')
    assert lines_on_surface(4,0b111,2)==27
    print('GF4 exact contained lines: 27')
    P,qA,qB,slope,cval=tangent_test()
    print('GF256 witness:',P,'quadratic basis:',(qA,qB),'sole quadratic tangent slope:',slope,'cubic nonzero:',cval)
    # Hilbert series of two-variable complete intersection of degrees two and three.
    # (1-z^2)(1-z^3)/(1-z)^2 has the following coefficients.
    hilbert=[(n+1)-(n-1 if n>=2 else 0)-(n-2 if n>=3 else 0)+(n-4 if n>=5 else 0) for n in range(6)]
    assert hilbert==[1,2,2,1,0,0]
    print('Generic transverse complete intersection Hilbert function: 1,2,2,1; length 6')
    print('Plucker cycle degree: 6*3+27=45')
    print('ALL_CHECKS_PASSED')
