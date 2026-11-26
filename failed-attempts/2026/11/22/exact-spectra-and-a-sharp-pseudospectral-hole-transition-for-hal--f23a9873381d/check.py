"""Independent finite diagnostic for the half-flux three-frequency spectral formula.

Uses only Python's standard library; analytical all-parameter proof is in RESULT.md.
"""
import cmath
import math
import itertools


def predicted_min(a,b,c):
    r = sorted((abs(a),abs(b),abs(c)))
    return max(0.,r[2]-math.hypot(r[1],r[0]))


def predicted_max(a,b,c):
    lens = sorted((abs(a),abs(b),abs(c)))
    s = sum(x*x for x in lens)
    return math.sqrt(2*s) if lens[2]*lens[2] <= s/2 else lens[2]+math.hypot(lens[0],lens[1])


def exact_fiber_quantities(a,b,c,u,v):
    # Matrix [[a+bu,cv],[cv,a-bu]] for unit complex u and v.
    m00,m01,m11 = a+b*u,c*v,a-b*u
    det = m00*m11-m01*m01
    tr = abs(m00)**2+abs(m11)**2+2*abs(m01)**2
    discriminant = max(0.,tr*tr-4*abs(det)**2)
    return math.sqrt(max(0.,(tr-math.sqrt(discriminant))/2)), math.sqrt((tr+math.sqrt(discriminant))/2), det,tr


def pseudospectrum_test(t,B,C,eps):
    M,m = max(B,C),min(B,C)
    mu=max(0.,t-math.hypot(B,C),M-math.hypot(t,m))
    if eps < M-m:
        inner=math.sqrt((M-eps)**2-m*m)
        prescribed=inner<t<math.hypot(B,C)+eps
    elif eps == M-m and M>m:
        prescribed=0<t<math.hypot(B,C)+eps
    else:
        prescribed=0<=t<math.hypot(B,C)+eps
    return (mu<eps)==prescribed


def run():
    n=0
    phases=(1, -1, 1j, -1j)
    for a,b,c in itertools.product(range(5), repeat=3):
        S=a*a+b*b+c*c
        for u,v in itertools.product(phases,repeat=2):
            lo,hi,det,tr=exact_fiber_quantities(a,b,c,u,v)
            assert abs(tr-2*S)<1e-9
            assert abs(det-(a*a-b*b*u*u-c*c*v*v))<1e-9
            assert lo>=-1e-10 and hi<=predicted_max(a,b,c)+1e-9
            assert lo+1e-9>=predicted_min(a,b,c)
            n+=4
    for B,C in itertools.product((0,0.5,1.,2.,3.),repeat=2):
        for eps in (0.1,0.5,1.,2.,3.,5.):
            for i in range(101):
                t=(i+.125)/16.
                assert pseudospectrum_test(t,B,C,eps)
                n+=1
    # Complex-coefficient and non-root phases; trace and determinant are phase-covariant.
    for a,b,c in ((2+1j,1-2j,3+2j),(.3j,1+1j,-2j),(-1,2j,1j)):
        for i in range(80):
            u=cmath.exp(1j*i*.138)
            v=cmath.exp(1j*i*.173)
            lo,hi,det,tr=exact_fiber_quantities(a,b,c,u,v)
            assert abs(tr-2*(abs(a)**2+abs(b)**2+abs(c)**2))<1e-8
            assert abs(det-(a*a-b*b*u*u-c*c*v*v))<1e-8
            assert lo+1e-8>=predicted_min(a,b,c)
            assert hi<=predicted_max(a,b,c)+1e-8
            n+=4
    print('HALF_FLUX_THREE_TERM_CHECK_OK',n)

if __name__=='__main__':run()
