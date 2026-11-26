#!/usr/bin/env python3
"""Reproduce analytical sharpness identities and independent Fourier tests.

Uses only the Python standard library. Numerical tests are supplementary to
continuous-measure proofs in RESULT.md.
"""
import cmath
import math
import random

PI = math.pi
TESTS = 0

def close(x, y, tol=2e-12):
    global TESTS
    TESTS += 1
    assert abs(x-y) <= tol * max(1.0, abs(x), abs(y)), (x,y)

def parabolic_data(a):
    s=math.sin(PI*a/2)
    c=math.cos(PI*a/2)
    M=2*s*c/PI
    gp=PI*s/(2*c)
    gm=PI*c/(2*s)
    return s,c,M,gp,gm

def exact_extremizer(a,m,upper):
    s,c,M,gp,gm=parabolic_data(a)
    assert -M-1e-14 <= m <= M+1e-14
    t=PI*a
    if upper:
        z=math.acos(max(-1,min(1,-PI*m/(2*c))))
        u=z-(PI-t)/2
        v=u+PI-t
        # Set |theta| in [0,u] union [v,pi].
        c1=(math.sin(u)-math.sin(v))/PI
        c2=(math.sin(2*u)-math.sin(2*v))/(2*PI)
        bound=M-2*gp*m*m
    else:
        y=math.acos(max(-1,min(1,PI*m/(2*s))))
        u=y-t/2
        v=u+t
        # Set |theta| in [u,v].
        c1=(math.sin(v)-math.sin(u))/PI
        c2=(math.sin(2*v)-math.sin(2*u))/(2*PI)
        bound=-M+2*gm*m*m
    return u,v,c1,c2,bound

def cell_coeffs(N):
    cells=[]
    h=2*PI/N
    for j in range(N):
        left=-PI+j*h
        right=left+h
        c1=(cmath.exp(-1j*left)-cmath.exp(-1j*right))/(2j*PI)
        c2=(cmath.exp(-2j*left)-cmath.exp(-2j*right))/(4j*PI)
        cells.append((c1,c2))
    return cells

def test():
    global TESTS
    rng=random.Random(0x42A70)
    for a in [0.04,0.11,0.25,0.39,0.5,0.62,0.82,0.97]:
        s,c,M,gp,gm=parabolic_data(a)
        close(M,math.sin(PI*a)/PI)
        close(2*gp*M,s*s*2)
        close(2*gm*M,c*c*2)
        for k in range(151):
            m=M*(2*k/150-1)
            for upper in (False,True):
                u,v,c1,c2,b=exact_extremizer(a,m,upper)
                close(c1,m,3e-12)
                close(c2,b,3e-12)
                assert -1e-10<=u<=PI+1e-10 and -1e-10<=v<=PI+1e-10
                TESTS+=1
                if upper:
                    close(abs(c2+gp*c1*c1),M-gp*abs(c1)**2)
                else:
                    close(abs(c2-gm*c1*c1),M-gm*abs(c1)**2)
                # Exact polynomial dual certificate, sampled at independent x.
                for theta in [0,0.121,0.7,1.4,2.1,2.96]:
                    x=math.cos(theta);x1=math.cos(u);x2=math.cos(v)
                    poly=2*(x-x1)*(x-x2)
                    trig=math.cos(2*theta)-2*(x1+x2)*x+1+2*x1*x2
                    close(poly,trig)
    for N in (40,80,128):
        cells=cell_coeffs(N)
        for K in [1,N//9,N//4,N//2,3*N//4,N-1]:
            if K<=0 or K>=N: continue
            a=K/N
            _,_,M,gp,gm=parabolic_data(a)
            for _ in range(240):
                ids=rng.sample(range(N),K)
                z1=sum(cells[j][0] for j in ids)
                z2=sum(cells[j][1] for j in ids)
                TESTS+=3
                assert abs(z1) <= M+3e-13
                assert abs(z2+gp*z1*z1)<=M-gp*abs(z1)**2+3e-13
                assert abs(z2-gm*z1*z1)<=M-gm*abs(z1)**2+3e-13
                m=z1.real; q=z2.real
                assert -M+2*gm*m*m-3e-13 <=q<=M-2*gp*m*m+3e-13
                TESTS+=1
    # Lens is exactly filled by the indicator purification lemma.
    # Its vertical width is 2M*(1 - (m/M)^2).
    for a in [0.11,0.28,0.5,0.77]:
        _,_,M,gp,gm=parabolic_data(a)
        for k in range(100):
            m=M*(2*k/99-1)
            width=2*M-2*(gp+gm)*m*m
            close(width,2*M*(1-(m/M)**2))
    print(f"PASS {TESTS} assertions; 8 aperture fractions, 151 mass/first-moment slices, ")
    print("two extremizer branches and 4,320 exact-integral randomized measurable masks")

if __name__=='__main__':test()
