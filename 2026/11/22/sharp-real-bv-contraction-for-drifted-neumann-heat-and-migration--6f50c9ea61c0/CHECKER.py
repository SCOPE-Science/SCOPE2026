"""Numerical consistency checks for sharp BV contraction of drifted Neumann heat.
Standard-library Python 3. No finite test replaces the analytic proof.
"""
import math

PI = math.pi

def spectral(t, y, b, derivative=False):
    """S_b(t,y) or its y-derivative via the uniformly convergent sine series."""
    h = 0.5 * b
    nmax = max(50, int(8 / math.sqrt(t)) + 2)
    total = 0.0
    for k in range(1, nmax + 1):
        z = k * PI
        a = 2 * z * (1 - (-1)**k * math.exp(-h)) / (z*z + h*h)
        w = math.exp(-z*z*t)
        if derivative:
            total += a*w*(h*math.sin(z*y) + z*math.cos(z*y))
        else:
            total += a*w*math.sin(z*y)
    return math.exp(h*y-h*h*t)*total

def maximizing_y(t,b):
    lo, hi = 1e-9, 1-1e-9
    assert spectral(t,lo,b,True)>0 and spectral(t,hi,b,True)<0
    for _ in range(65):
        mid=(lo+hi)/2
        if spectral(t,mid,b,True)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def dirichlet_column_integral(t,y,b,steps=1500):
    """Independent Simpson quadrature of positive Dirichlet kernel column."""
    assert steps % 2 == 0
    nmax = max(50, int(8/math.sqrt(t))+2)
    a=[2*math.exp(-(k*PI)**2*t)*math.sin(k*PI*y) for k in range(1,nmax+1)]
    def q(x):
        return math.exp(b*(y-x)/2-b*b*t/4)*sum(aa*math.sin((k+1)*PI*x) for k,aa in enumerate(a))
    h=1/steps
    return h/3*(q(0)+q(1)+4*sum(q(i*h) for i in range(1,steps,2))+2*sum(q(i*h) for i in range(2,steps,2)))

def asymptotic_position(b):
    return .5+math.atan(b/(2*PI))/PI

def correction(b):
    p=b/(2*PI)
    return -4*PI*math.tanh(b/4)/((4*PI*PI+b*b/4)*math.sqrt(1+p*p))

def test():
    for b in (-3.,-1.,0.,1.,2.,5.):
        for t in (.03,.08,.2,.4):
            y=maximizing_y(t,b)
            s=spectral(t,y,b)
            assert 0 < s < 1 and 0 < y < 1
            # The candidate maximizes a sampled grid; all spatial derivative
            # values to either side have the predicted sign.
            for i in range(1,101):
                z=i/101
                d=spectral(t,z,b,True)
                if z < y-1e-8: assert d > -2e-12
                if z > y+1e-8: assert d < 2e-12
            assert abs(spectral(t,y,b)-spectral(t,1-y,-b))<3e-13
            assert abs(spectral(t,y,b)-dirichlet_column_integral(t,y,b))<3e-9
    print('POSITIVE_KERNEL_COLUMN_AND_UNIQUE_PEAK_SAMPLING_PASS')
    print('DRIFT_REFLECTION_AND_INDEPENDENT_QUADRATURE_PASS')

    # At b=0, only odd eigenmodes survive and y=1/2 is exact.
    for t in (.03,.1,.25):
        direct=spectral(t,.5,0)
        odd=sum(4/PI*(-1)**j/(2*j+1)*math.exp(-((2*j+1)*PI)**2*t) for j in range(30))
        assert abs(direct-odd)<1e-14
        assert abs(maximizing_y(t,0)-.5)<1e-13
    print('DRIFTLESS_ODD_MODE_IDENTITY_PASS')

    b=2.
    small=[]
    for t in (.003,.005,.01):
        y=maximizing_y(t,b)
        s=spectral(t,y,b)
        ratio=(1-s)/(8*math.sqrt(t/PI)*math.exp(-1/(16*t)))
        small.append(((y-.5)/t,ratio))
    assert 1.94<small[0][0]<1.97
    assert .95<small[0][1]<1.01
    assert small[0][0]>small[1][0]>small[2][0]
    assert small[0][1]>small[1][1]>small[2][1]
    print('SMALL_TIME_DRIFT_COMPENSATION_AND_DEFICIT_PASS')

    yinf=asymptotic_position(b)
    c=correction(b)
    prev=None
    for t in (.15,.2,.25):
        dy=maximizing_y(t,b)-yinf
        ratio=dy/(c*math.exp(-3*PI*PI*t))
        assert abs(ratio-1)<.005
        if prev is not None: assert abs(ratio-1)<abs(prev-1)
        prev=ratio
    for b in (-2.,0.,2.):
        yi=asymptotic_position(b)
        z=maximizing_y(.4,b)
        assert abs(z-yi)<2e-6
    print('LONG_TIME_OPTIMIZER_FIRST_SPECTRAL_CORRECTION_PASS')
    print('ALL_DRIFTED_NEUMANN_BV_CHECKS_PASS')

if __name__ == '__main__': test()
