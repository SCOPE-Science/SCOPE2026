#!/usr/bin/env python3
"""Independent numerical checks for a nonlinear graphon Ising fixed-point classification.
Standard-library only. All universal assertions rely on the accompanying proof, not sampling.
Run: python3 check.py
"""
import math

PI = math.pi

def logcosh(z):
    z = abs(z)
    return z + math.log1p(math.exp(-2*z)) - math.log(2)

def quarter(a, n=4096):
    assert a > 0 and n % 2 == 0
    # u = sin(theta) removes the endpoint square-root singularity.
    def f(theta):
        if theta >= PI/2:
            return math.sqrt(a / math.tanh(a))
        u = math.sin(theta)
        d = logcosh(a) - logcosh(a*u)
        return a*math.cos(theta)/math.sqrt(2*d)
    step = (PI/2)/n
    total = f(0)+f(PI/2)
    for k in range(1, n):
        total += (4 if k % 2 else 2)*f(k*step)
    return total*step/3

def trajectory(a,j,n=8192):
    q = quarter(a)
    beta = ((2*j+1)*q)**2
    v = math.sqrt(2*beta*logcosh(a))
    step = 1/n
    h = 0.0; d = v
    hs = [h]; ds=[d]
    def rhs(h,d):
        return d, -beta*math.tanh(h)
    for k in range(n):
        u1,v1 = rhs(h,d)
        u2,v2 = rhs(h+step*u1/2,d+step*v1/2)
        u3,v3 = rhs(h+step*u2/2,d+step*v2/2)
        u4,v4 = rhs(h+step*u3,d+step*v3)
        h+=step*(u1+2*u2+2*u3+u4)/6
        d+=step*(v1+2*v2+2*v3+v4)/6
        hs.append(h); ds.append(d)
    return beta,v,hs,ds

def integ(y):
    return (sum(y[1:-1])+(y[0]+y[-1])/2)/(len(y)-1)

def run():
    tests=0
    amps=[0.05,0.1,0.4,0.8,1.5,3,7,15]
    qs=[quarter(a) for a in amps]
    assert all(q>PI/2 for q in qs); tests+=len(qs)
    assert all(x<y for x,y in zip(qs,qs[1:])); tests+=len(qs)-1
    for a in [0.03,0.08,0.15]:
        q=quarter(a)
        assert abs((q/(PI/2)-1)/(a*a)-1/8) < 0.002;tests+=1
    for a in [30,100,300]:
        q=quarter(a)
        assert abs(q/math.sqrt(2*a)-1)<0.002;tests+=1
    for a in [0.4,1.1,3.2]:
        for j in range(4):
            beta,v,hs,ds=trajectory(a,j)
            assert beta > ((2*j+1)*PI/2)**2;tests+=1
            assert abs(ds[-1])<2e-5*(1+v);tests+=1
            assert abs(abs(hs[-1])-a)<2e-5*(1+a);tests+=1
            assert (-1)**j*hs[-1]>0;tests+=1
            mean=integ([math.tanh(h) for h in hs])
            assert abs(mean-v/beta)<3e-6;tests+=1
            for k in range(1,j+1):
                idx=round(len(hs[:-1])*2*k/(2*j+1))
                assert abs(hs[idx]) < 0.015;tests+=1
            # Return map: h(x)=beta * integral min(x,y)*tanh(h(y)) dy.
            ms=[math.tanh(h) for h in hs]
            N=len(hs)-1
            for index in [N//5,N//2,4*N//5,N]:
                x=index/N
                integ0=integ([min(x,t/N)*ms[t] for t in range(N+1)])
                assert abs(hs[index]-beta*integ0)<0.00012*(1+abs(hs[index]));tests+=1
    print('PASS',tests,'numerical consistency checks')
    print('Thresholds:',[round(((2*j+1)*PI/2)**2,12) for j in range(4)])
    print('Quarter periods:', [(a,round(q,9)) for a,q in zip(amps,qs)])
if __name__=='__main__':run()
