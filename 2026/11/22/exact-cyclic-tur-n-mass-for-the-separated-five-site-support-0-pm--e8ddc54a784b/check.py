#!/usr/bin/env python3
"""Independent numerical corroboration for a finite cyclic five-site Turán extremum.

All-dimensional assertions are proved in RESULT.md; finite tests only corroborate them.
Requires only the Python standard library.
"""
import math

COUNT = 0

def require(ok, message):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(message)

def formula(N):
    if N % 2 == 0:
        return (2.0, 0.5, 0.0, ())
    d = math.pi / N
    C = math.cos(d)
    r = (N + 1) // 6
    u = math.cos(2 * math.pi * r / N)
    w = C - u
    b = 1.0 / (8.0 * C * u * w)
    a = (3.0 - 4.0 * (C*C - C*u + u*u)) * b
    T = 1.0 + 2.0 * (a+b)
    return (T, a, b, (C, u, w, r))

def polynomial(N, a, b, j):
    t = 2.0 * math.pi * j / N
    return 1.0 + 2.0*a*math.cos(t) + 2.0*b*math.cos(3*t)

def exact_vertex_lp(N):
    # All vertices of the two-variable LP with x cos(theta), y cos(3theta).
    rows = [(math.cos(2*math.pi*j/N), math.cos(6*math.pi*j/N)) for j in range(N)]
    best = None
    for i in range(N):
        x1,y1 = rows[i]
        for j in range(i+1,N):
            x2,y2 = rows[j]
            det = x1*y2 - x2*y1
            if abs(det) < 1e-11:
                continue
            # 1+2*a*x1+2*b*y1=1+2*a*x2+2*b*y2=0.
            a = (y1-y2)/(2*det)
            b = (x2-x1)/(2*det)
            if min(1+2*a*x+2*b*y for x,y in rows) >= -1e-8:
                val = 1+2*(a+b)
                if best is None or val > best:
                    best = val
    if best is None:
        raise AssertionError('no LP vertex found')
    return best

def main():
    for N in range(7,2002):
        T,a,b,ext = formula(N)
        require(abs(T-(1+2*(a+b))) < 1e-10, ('objective',N))
        require(min(polynomial(N,a,b,j) for j in range(N)) >= -1e-9, ('positivity',N))
        if N%2 == 0:
            require(abs(T-2.0) < 1e-13, ('even',N))
            require(abs(polynomial(N,a,b,N//2)) < 1e-12, ('even-contact',N))
        else:
            C,u,w,r = ext
            require(C>0 and u>0 and w>0, ('roots',N))
            require(abs(u+w-C)<1e-12, ('root-sum',N))
            require(abs(polynomial(N,a,b,r)) < 1e-9, ('first-contact',N))
            require(abs(polynomial(N,a,b,(N-1)//2)) < 1e-9, ('second-contact',N))
            require(abs(T-((1+C)*(1-u)*(1-w))/(C*u*w)) < 1e-10, ('factorization',N))
            v = 4*u**3 - 3*u
            D = math.cos(3*math.pi/N)
            det = C*v-D*u
            lam = -(C-D)/det
            mu = -(u-v)/det
            require(lam>0 and mu>0 and det < 0, ('dual-positive',N))
            require(abs(lam*u-mu*C+1)<1e-9, ('dual-x',N))
            require(abs(lam*v-mu*D+1)<1e-9, ('dual-y',N))
            require(abs((lam+mu)-(2*a+2*b)) < 1e-8, ('duality',N))
            require(a>=-1e-10, ('positive-first-coeff',N))
            if N % 3 == 0:
                require(abs(a)<1e-9, ('triple-resonance',N))
                require(abs(T-(1+1/D))<1e-9, ('triple-formula',N))
            elif N % 6 == 1:
                nxt = math.cos(2*math.pi*(r+1)/N)
                require(nxt<w<u, ('bracket-one',N,nxt,w,u))
                require(a>0, ('first-positive',N))
            else:
                prv = math.cos(2*math.pi*(r-1)/N)
                require(u<w<prv, ('bracket-five',N,u,w,prv))
                require(a>0, ('first-positive',N))
        if N<=101:
            val=exact_vertex_lp(N)
            require(abs(val-T) < 1e-7, ('LP',N,val,T))
    print('PASS:',COUNT,'assertions for N=7..2001; independently enumerated LP vertices for N<=101.')

if __name__=='__main__':
    main()
