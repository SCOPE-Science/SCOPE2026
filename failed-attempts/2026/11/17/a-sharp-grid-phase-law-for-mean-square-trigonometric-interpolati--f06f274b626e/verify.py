"""Supplementary independent checks of shifted-grid trigonometric interpolation.
Standard-library-only numerical diagnostics, not a proof of asymptotics.
"""
import cmath
import math

PI=math.pi

def square_integrand(t,shift):
    if t==0.0:
        return (2*PI*(shift-.5))**2
    a=PI/math.sin(PI*t)
    b=1/t
    # Stable expression at the removable singularity
    diff=PI*(1/math.sin(PI*t) - 1/(PI*t))
    return diff*diff + 2*a*b*(1-math.cos(2*PI*(shift-.5)*t))

def simpson(fun, a, b, steps=20000):
    if steps%2: raise ValueError('even subdivision count required')
    h=(b-a)/steps
    v=fun(a)+fun(b)
    for j in range(1,steps):
        v+=(4 if j%2 else 2)*fun(a+h*j)
    return v*h/3

def constant(shift):
    return 4+2*simpson(lambda t:square_integrand(t,shift),0,.5)

def exact_coeff(N,shift,k):
    return (1j*PI/N)*cmath.exp(-2j*PI*(shift-.5)*k/N)/math.sin(PI*k/N)

def sampled_coeff(N,shift,k):
    return sum((2*PI*(j+shift)/N)*cmath.exp(-2j*PI*k*(j+shift)/N)
               for j in range(N))/N

def scaled_error(N,shift):
    n=(N-1)//2
    dc=PI*(2*shift-1)/N
    low=2*sum(abs(exact_coeff(N,shift,k)-1j/k)**2 for k in range(1,n+1))
    # Total sum of reciprocal squares is pi^2/6.
    tail=2*(PI**2/6-sum(1/(k*k) for k in range(1,n+1)))
    return N*(dc**2+low+tail)

def main():
    for phase in (0.0,.1,.25,.5,.8):
        val=constant(phase)
        for N in (7,31,101):
            for k in (1,2,(N-1)//2):
                a=sampled_coeff(N,phase,k)
                b=exact_coeff(N,phase,k)
                assert abs(a-b)<1e-11,(N,phase,k,a,b)
        N=401
        got=scaled_error(N,phase)
        assert abs(got-val)<.02,(phase,got,val)
        print(f'phase={phase:.2f} F={val:.12f} N*L2error2={got:.12f}')
    assert constant(.5)<constant(.25)<constant(0.0)
    assert abs(constant(0.0)-constant(1.0))<1e-8
    def aligned_mid(t):
        if t==0.0:return 0.0
        diff=PI/math.tan(PI*t)-1/t
        return diff**2
    midpoint=4+2*simpson(aligned_mid,0,.5)
    assert midpoint>constant(.5)
    print(f'node midpoint F={midpoint:.12f}; all finite diagnostics passed')

if __name__=='__main__':main()
