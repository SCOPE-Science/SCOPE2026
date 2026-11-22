"""Standalone executable algebra and finite-time checks for the two-type matching predator--prey damping law.
No numerical experiment in this file is offered as proof of a long-time theorem.
Python >=3.9, sympy, numpy and scipy required.
"""
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp


def exact_algebra():
    n0,n1,h0,h1,u,v,c,g,p,r=sp.symbols('n0 n1 h0 h1 u v c g p r',positive=True)
    N=n0+n1;H=h0+h1;a=2*c*u+p*v;b=2*g*v-r*u
    nf=[n0*(a-c*N-p*h0),n1*(a-c*N-p*h1)]
    hf=[h0*(b-g*H+r*n0),h1*(b-g*H+r*n1)]
    Vdot=sum((1-u/z)*f for z,f in zip((n0,n1),nf))+(p/r)*sum((1-v/z)*f for z,f in zip((h0,h1),hf))
    assert sp.simplify(Vdot+c*(N-2*u)**2+(p*g/r)*(H-2*v)**2)==0
    I=sp.I;J=sp.Matrix([[-2,-1],[1,-2]])
    F=sp.Matrix([-sp.Rational(1,4),sp.Rational(1,4)])
    W=(2*I*sp.eye(2)-J).inv()*F
    assert sp.simplify(W[0]-(-sp.Rational(19,260)+sp.Rational(11,130)*I))==0
    assert sp.simplify(W[1]-(sp.Rational(17,260)-sp.Rational(3,130)*I))==0
    D=sp.simplify(sum(sp.expand_complex(z*sp.conjugate(z)) for z in W))
    assert D==sp.Rational(9,520)
    assert sp.simplify(1/(2*D)-sp.Rational(260,9))==0
    th,R=sp.symbols('th R',real=True)
    A=R**2*(sp.re(W[0])*sp.sin(2*th)+sp.im(W[0])*sp.cos(2*th))
    B=R**2*(sp.re(W[1])*sp.sin(2*th)+sp.im(W[1])*sp.cos(2*th))
    x=R*sp.cos(th);y=R*sp.sin(th)
    dx=-A*x-sp.Rational(1,2)*(A*y+B*x)
    dy=-B*y+sp.Rational(1,2)*(A*y+B*x)
    cubic_average=sp.simplify(sp.integrate(2*(x*dx+y*dy),(th,0,2*sp.pi))/(2*sp.pi)/R**4)
    assert cubic_average==-sp.Rational(9,260)
    print('PASS entropy identity; exact transfer coefficients; cubic radial average -9/260; tR^2 -> 260/9')


def numerical_checks():
    tests=[(1.,1.,1.,1.,1.,1.,[1.08,.92,1.06,.94]),
           (2.,1.,.5,1.2,1.4,.9,[2.16,1.84,1.06,.94]),
           (.6,1.5,1.7,.7,.8,1.3,[.648,.552,1.59,1.41])]
    for u,v,c,g,p,r,initial in tests:
        a=2*c*u+p*v;b=2*g*v-r*u
        omega=(p*r*u*v)**.5
        J=np.array([[-2*c*u,-p*u],[r*v,-2*g*v]],dtype=float)
        F=np.array([-omega/(4*u),r*omega/(4*p*u)])
        W=np.linalg.solve(2j*omega*np.eye(2)-J,F)
        D=c*abs(W[0])**2+p*g/r*abs(W[1])**2
        target=1/(2*u*D)
        def ode(t,z):
            n0,n1,h0,h1=z;N=n0+n1;H=h0+h1
            return [n0*(a-c*N-p*h0),n1*(a-c*N-p*h1),h0*(b-g*H+r*n0),h1*(b-g*H+r*n1)]
        sol=solve_ivp(ode,(0,12000),initial,rtol=2e-8,atol=1e-10,max_step=0.7)
        assert sol.success and min(sol.y[:,-1])>0
        X=sol.y[0,-1]-sol.y[1,-1]
        Y=sol.y[2,-1]-sol.y[3,-1]
        actual=12000*(X*X+(p*u/(r*v))*Y*Y)
        assert abs(actual/target-1)<0.12,(actual,target)
        print('PASS finite-time approach, 12,000 time units: observed tR^2=',round(actual,6),'theorem limit=',round(target,6))

if __name__=='__main__':
    exact_algebra()
    numerical_checks()
