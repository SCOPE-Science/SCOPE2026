"""Reproduce the local second-variation identities for planar quadrilateral widths.

Requires Python 3 and SymPy. All displayed identities use exact SymPy
arithmetic; the angular calculations independently exercise sample polygons.
"""
import math
import random
import sympy as S


def exact_derivatives():
    sh, t, h, k = S.symbols('sh t h k', real=True)
    vertices = [S.Matrix([1+h,k]), S.Matrix([sh-h,t-k]),
                S.Matrix([-1+h,k]), S.Matrix([-sh-h,-t-k])]
    edges = [vertices[(i+1)%4]-vertices[i] for i in range(4)]
    def det(a,b): return a[0]*b[1]-a[1]*b[0]
    def dot(a,b): return a.dot(b)
    E2 = (S.pi*sum(dot(a,a) for a in edges)
          +2*sum(det(edges[i],edges[(i+1)%4])
                   +S.pi*dot(edges[i],edges[(i+1)%4])/2
                   +dot(edges[i],edges[(i+1)%4])**2/
                    det(edges[i],edges[(i+1)%4]) for i in range(4)))/(4*S.pi)
    P = sum(S.sqrt(dot(a,a)) for a in edges)
    F = S.pi**2*E2/P**2-1
    q=(sh,t,h,k)
    p={sh:0,t:1,h:0,k:0}
    assert S.simplify(P.subs(p)-4*S.sqrt(2))==0
    assert S.simplify(E2.subs(p)-(2+4/S.pi))==0
    assert all(S.simplify(S.diff(F,x).subs(p))==0 for x in q)
    H=S.Matrix([[S.simplify(S.diff(F,x,y).subs(p)) for y in q] for x in q])
    goal=S.diag(S.pi*(S.pi-2)/32,S.pi/8,S.pi*(2-S.pi)/8,S.pi*(2-S.pi)/8)
    assert H==goal, (H,goal)
    assert S.simplify(F.subs(p) - (S.pi**2/16+S.pi/8-1))==0
    return H


def sample_width_moments(q, steps=16384):
    sh,t,h,k=q
    vertices=((1+h,k),(sh-h,t-k),(-1+h,k),(-sh-h,-t-k))
    e=[(vertices[(j+1)%4][0]-vertices[j][0],
        vertices[(j+1)%4][1]-vertices[j][1]) for j in range(4)]
    # Direct maximum-minus-minimum projection integral, distinct from edge kernel.
    tot1=tot2=0.0
    for j in range(steps):
        angle=2*math.pi*(j+0.5)/steps
        c,s=math.cos(angle),math.sin(angle)
        proj=[x*c+y*s for x,y in vertices]
        w=max(proj)-min(proj)
        tot1+=w
        tot2+=w*w
    mu=tot1/steps; Ew2=tot2/steps
    P=sum(math.hypot(*edge) for edge in e)
    assert abs(mu-P/math.pi)<1e-6, (mu,P)
    # Independent exact all-pairs angular edge-kernel, no Taylor truncation.
    def V(theta):
        th=abs(theta)
        if th>math.pi: th=2*math.pi-th
        return (math.pi-th)*math.cos(th)+math.sin(th)
    angle=[math.atan2(y,x) for x,y in e]
    lens=[math.hypot(x,y) for x,y in e]
    Ew2kern=sum(lens[i]*lens[j]*V(angle[i]-angle[j])
                for i in range(4) for j in range(4))/(4*math.pi)
    assert abs(Ew2-Ew2kern)<3e-6, (Ew2,Ew2kern)
    return Ew2kern/(P/math.pi)**2-1


def numeric_checks(H):
    rng=random.Random(2307)
    checks=0
    base=(-1+math.pi**2/16+math.pi/8)
    for _ in range(28):
        sh=rng.uniform(-0.5,0.5)
        tau=rng.uniform(-0.5,0.5)
        h=rng.uniform(-0.5,0.5)
        k=rng.uniform(-0.5,0.5)
        for eps in (0.02,0.01):
            q=(eps*sh,1+eps*tau,eps*h,eps*k)
            exact=sample_width_moments(q,steps=8192)
            coeff=math.pi*(math.pi-2)/64*sh**2+math.pi/16*tau**2-math.pi*(math.pi-2)/16*(h*h+k*k)
            assert abs(exact-base-eps**2*coeff)<0.5*eps**3, (q,exact,coeff)
            checks+=1
    # Independent test of global parallelogram inequality, rather than proof.
    for j in range(250):
        a=math.exp(rng.uniform(-3,3)); b=math.exp(rng.uniform(-3,3))
        theta=rng.uniform(0.003,math.pi/2)
        gf=math.sin(theta)+(math.pi/2-theta)*math.cos(theta)
        Ew2=(a*a+b*b)/2+(2*a*b/math.pi)*gf
        mu=2*(a+b)/math.pi
        square_min=math.pi**2/16+math.pi/8-1
        assert Ew2/mu**2-1>=square_min-1e-12
        checks+=1
    return checks


if __name__=='__main__':
    H=exact_derivatives()
    n=numeric_checks(H)
    print('VERIFY_OK', n, 'second-order Hessian and independent width quadratures')
