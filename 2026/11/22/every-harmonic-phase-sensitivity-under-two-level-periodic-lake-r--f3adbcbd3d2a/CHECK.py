"""Independent numerical checks of an exact two-regime oxygen-response theorem.

Run: python3 CHECK.py (standard library only). These finite diagnostics
support, but do not replace, the analytical nonvanishing proof.
"""
import cmath
import math
import random


def kernel(T, h, high, low, n):
    assert 0 < h < T and 0 < low < high and n >= 1
    eh = math.exp(-high * h)
    el = math.exp(-low * (T-h))
    delta = (1/low - 1/high)/(1-eh*el)
    w0 = 1/high + eh*delta*(1-el)
    wh = 1/high + delta*(1-el)
    frequency = 2*math.pi*n/T
    R = high*low*(1-eh*el)
    u = high*(1-el)+low*el*(1-eh)
    v = high*eh*(1-el)+low*(1-eh)
    z = cmath.exp(1j*frequency*h)
    W = -delta*(z*(R+1j*frequency*u)-(R+1j*frequency*v)) / (
        1j*frequency*T*(high+1j*frequency)*(low+1j*frequency))
    def w(t):
        if t <= h:
            return 1/high + (wh-1/high)*math.exp(-high*(h-t))
        return 1/low + (w0-1/low)*math.exp(-low*(T-t))
    return W, w, u, v, w0, wh


def simpson(fn, a, b, steps=800):
    assert steps % 2 == 0
    dt = (b-a)/steps
    return dt/3*(fn(a)+fn(b)+4*sum(fn(a+i*dt) for i in range(1,steps,2))
               +2*sum(fn(a+i*dt) for i in range(2,steps,2)))


def exact_periodic_solution(T,h,high,low,n,r0,r1,phase):
    omega=2*math.pi*n/T
    def flow(t0,t1,m,x0):
        dt=t1-t0
        e=math.exp(-m*dt)
        inc=r0*(1-e)/m + r1*(cmath.exp(1j*phase)*(
            cmath.exp(1j*omega*t1)-e*cmath.exp(1j*omega*t0))/(m+1j*omega)).real
        return e*x0+inc
    b=flow(h,T,low,flow(0,h,high,0.0))
    x0=b/(1-math.exp(-high*h-low*(T-h)))
    xh=flow(0,h,high,x0)
    def x(t):
        return flow(0,t,high,x0) if t<=h else flow(h,t,low,xh)
    return x


def main():
    rng=random.Random(472901)
    tested=0
    for j in range(220):
        T=rng.uniform(0.6,5)
        h=T*rng.uniform(.15,.85)
        low=rng.uniform(.3,2)
        high=low+rng.uniform(.2,3)
        n=rng.randint(1,7)
        r0=rng.uniform(.8,2)
        r1=r0*rng.uniform(.1,.8)
        phase=rng.uniform(-4,4)
        W,w,u,v,w0,wh=kernel(T,h,high,low,n)
        assert u>v>0 and w0<wh
        freq=2*math.pi*n/T
        Wquad=(simpson(lambda t:w(t)*math.cos(freq*t),0,h)
              +simpson(lambda t:w(t)*math.cos(freq*t),h,T)
              +1j*(simpson(lambda t:w(t)*math.sin(freq*t),0,h)
              +simpson(lambda t:w(t)*math.sin(freq*t),h,T)))/T
        assert abs(W-Wquad)<1e-9,(j,'Fourier',W,Wquad)
        x=exact_periodic_solution(T,h,high,low,n,r0,r1,phase)
        xbar=(simpson(x,0,h)+simpson(x,h,T))/T
        predicted=r0*(simpson(w,0,h)+simpson(w,h,T))/T + r1*(cmath.exp(1j*phase)*W).real
        assert abs(xbar-predicted)<2e-8,(j,'mean',xbar,predicted)
        assert abs(x(0)-x(T))<5e-13
        tested+=5
    # Equal duty: the raw switching rate has no nonzero even Fourier mode,
    # but every even harmonic of the oxygen-residence kernel persists.
    for n in (2,4,6,8,10):
        W,w,u,v,*_=kernel(2,1,2,1,n)
        assert abs(W)>1e-5/n**3
        assert abs((2-1)*(cmath.exp(1j*math.pi*n)-1)/(1j*math.pi*n*2))<1e-12
        tested+=2
    print('PASS',tested,'independent diagnostic assertions')
    print('Example half-duty second-harmonic response:',kernel(2,1,2,1,2)[0])

if __name__=='__main__':
    main()
