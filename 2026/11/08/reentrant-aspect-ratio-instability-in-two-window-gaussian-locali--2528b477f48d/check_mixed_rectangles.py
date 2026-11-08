"""Independent numerical checks for reciprocal-squeeze Gaussian localization formulas.

Only mathematics and reproducibility; no external dependencies.
"""
import cmath
import math

PI = math.pi

def J(c, t):
    return t*math.erf(math.sqrt(PI*c)*t)/math.sqrt(c) + math.expm1(-PI*c*t*t)/(PI*c)

def D(c, t):
    return t*math.erf(math.sqrt(PI*c)*t)/math.sqrt(c)

def D2(c, t):
    return D(c,t)+2*t*t*math.exp(-PI*c*t*t)

def energy(s, area, log_aspect):
    a=math.sqrt(area)*math.exp(log_aspect)
    b=math.sqrt(area)*math.exp(-log_aspect)
    k=2/(s+1/s)
    return (J(s,a)*J(1/s,b)+J(1/s,a)*J(s,b)+2*k*J(k,a)*J(k,b))/4

def curvature(s,area):
    t=math.sqrt(area); k=2/(s+1/s)
    return ((D2(s,t)*J(1/s,t)+J(s,t)*D2(1/s,t)-2*D(s,t)*D(1/s,t))/2
            + k*(J(k,t)*D2(k,t)-D(k,t)**2))

def midpoint_conv(c,t,n=300):
    # Independently double-integrate the original difference kernel on [0,t]^2.
    h=t/n; return h*h*sum(math.exp(-PI*c*(i-j)**2*h*h) for i in range(n) for j in range(n))

def overlap_numeric(s, t, x, xi, n=16000):
    # Direct complex quadrature of <g_s, M_xi T_x g_t>.
    lo=min(0,x)-9;hi=max(0,x)+9;h=(hi-lo)/n
    norm=(4*s*t)**.25
    accum=0j
    for j in range(n):
        v=lo+(j+.5)*h
        accum+=norm*math.exp(-PI*(s*v*v+t*(v-x)**2))*cmath.exp(2j*PI*xi*v)
    return abs(accum*h)**2

def overlap_closed(s,t,x,xi):
    return 2*math.sqrt(s*t)/(s+t)*math.exp(-2*PI*(s*t*x*x+xi*xi)/(s+t))

def main():
    for c,t in [(1,1),(5,.6),(.025,3)]:
        assert abs(J(c,t)-midpoint_conv(c,t))/J(c,t)<3e-5
    for s,t,x,xi in [(1,1,.5,.25),(20,.05,.7,.4),(3,2,-.2,.8)]:
        got=overlap_numeric(s,t,x,xi)
        expected=overlap_closed(s,t,x,xi)
        assert abs(got-expected)<2e-7, (got,expected)
    for s,area in [(20,1),(100,1),(100,.001),(100,10000),(500,1)]:
        cur=curvature(s,area)
        h=.0003
        fd=(energy(s,area,h)+energy(s,area,-h)-2*energy(s,area,0))/h**2
        assert abs(fd-cur)<2e-5*max(1,abs(cur)),(cur,fd)
    assert curvature(100,1)>0.04
    assert curvature(100,.001)<0
    assert curvature(100,10000)<0
    assert energy(100,1,2)>energy(100,1,0)+0.06
    for s in [100,400,1600,6400]:
        ratio=curvature(s,1)*2*math.sqrt(s)
        assert .5<ratio<1.05,(s,ratio)
    print('MIXED_SQUEEZE_RECTANGLE_PASS overlap_cases=3 convolution_cases=3 curvature_cases=5 reentrance_s=100')
    print('s=100 A=1 H0=%.12f H2=%.12f curvature=%.12f'%(energy(100,1,0),energy(100,1,2),curvature(100,1)))
if __name__=='__main__':main()
