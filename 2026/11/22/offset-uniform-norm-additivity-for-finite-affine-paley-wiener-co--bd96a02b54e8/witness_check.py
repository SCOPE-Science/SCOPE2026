"""Finite-window Mellin packet diagnostics for finite Paley-Wiener affine sums.
These calculations check finite test cases; the mathematical theorem is analytic.
"""
import math, cmath

def symbol(t, a, c):
    return sum(z/math.sqrt(s)*cmath.exp(-1j*t*math.log(s)) for s,z in zip(a,c))

def pure_packet_sq(t, a, c, R):
    ell=[math.log(s) for s in a]
    d=[z/math.sqrt(s) for s,z in zip(a,c)]
    return sum((d[j]*d[k].conjugate()*cmath.exp(-1j*t*(ell[j]-ell[k]))*
                max(0.,1.-abs(ell[j]-ell[k])/R))
               for j in range(len(a)) for k in range(len(a))).real

def offset_packet_sq(t, a, b, c, R, B, step=.01):
    ell=[math.log(s) for s in a]
    lower=B-R+min(ell)
    upper=B+max(ell)
    n=math.ceil((upper-lower)/step)
    dx=(upper-lower)/n
    total=0.
    for i in range(n):
        x=lower+(i+.5)*dx
        z=sum(c[j]/math.sqrt(a[j])*cmath.exp(-1j*t*ell[j])*cmath.exp(1j*b[j]*math.exp(x)/a[j])
              for j in range(len(a)) if B-R+ell[j] <= x <= B+ell[j])
        total+=abs(z)**2*dx/R
    return total

if __name__=='__main__':
    a=[1.,2.,4.]; c=[1.,1.,-1.]
    t=math.acos(1/(4*math.sqrt(2)))/math.log(2)
    exact=3*math.sqrt(5)/4
    assert abs(abs(symbol(t,a,c))-exact)<1e-12
    for R in (50.,200.,800.):
        measured=math.sqrt(pure_packet_sq(t,a,c,R))
        assert measured<exact and exact-measured < 2/R
    generic_a=[1.,2.,3.]; generic_c=[1.,1.,-1.]
    target=1+1/math.sqrt(2)+1/math.sqrt(3)
    best=min(range(1,2501), key=lambda k: abs(cmath.exp(-2j*math.pi*k*math.log(3)/math.log(2))+1))
    t=2*math.pi*best/math.log(2)
    assert target-abs(symbol(t,generic_a,generic_c))<.004
    estimate=math.sqrt(offset_packet_sq(t,generic_a,[1.3,-2.7,10.],generic_c,400.,-25.,.02))
    assert target-estimate<.02 and estimate<=target+1e-3
    print('PALEY_MELLIN_OFFSET_WITNESS_OK',best,'resonant=',round(exact,12),'generic=',round(target,12),'window=',round(estimate,12))
