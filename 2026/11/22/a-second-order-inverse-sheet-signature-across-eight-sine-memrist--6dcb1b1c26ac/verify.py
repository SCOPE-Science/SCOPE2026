"""Reproducible finite checks for inverse-sheet asymptotic formulas.

These diagnostics do not prove infinite asymptotic claims; see analytic proof.
"""
import math
from scipy.optimize import brentq
from scipy.integrate import quad

pi=math.pi

# Cases match the eight published formulas exactly, including the unscaled
# exponential term in the printed sixth model.
def phase(x, v, name, b=0.4, omega=pi, c=0.5):
    q=v-x
    e=math.exp(-math.cos(pi*q))-1
    Q=q*q-1
    A=abs(q)-1
    S=math.sin(pi*q)+c
    if name==1:m=Q; return omega*x*(1-b*m)
    if name==2:m=A; return omega*x*(1-b*m)
    if name==3:m=S; return omega*x*(1-b*m)
    if name==4:m=e; return omega*x*(1-b*m)
    if name==5:m=Q+A; return omega*x*(1-b*m)
    if name==6:return omega*(x*(1-b*A)-b*e)
    if name==7:m=Q+e; return omega*x*(1-b*m)
    if name==8:m=Q+e+A; return omega*x*(1-b*m)
    raise ValueError(name)

def deriv(x,v,name,b=0.4,omega=pi,c=0.5):
    q=v-x
    e=math.exp(-math.cos(pi*q))-1
    ep=pi*math.exp(-math.cos(pi*q))*math.sin(pi*q)
    Q=q*q-1; Qp=2*q
    A=abs(q)-1; Ap=(1 if q>0 else (-1 if q<0 else 0))
    S=math.sin(pi*q)+c; Sp=pi*math.cos(pi*q)
    if name==1: m,mp=Q,Qp
    elif name==2: m,mp=A,Ap
    elif name==3: m,mp=S,Sp
    elif name==4: m,mp=e,ep
    elif name==5: m,mp=Q+A,Qp+Ap
    elif name==6:return omega*(1-b*A + b*x*Ap + b*ep)
    elif name==7: m,mp=Q+e,Qp+ep
    elif name==8: m,mp=Q+e+A,Qp+ep+Ap
    return omega*(1-b*m+b*x*mp)

def count_phase_in_interval(lo, hi,level):
    # endpoint phases may duplicate across adjacent monotonic arcs; error O(K)
    if lo>hi:lo,hi=hi,lo
    if abs(level)==1:
        alpha=pi/2 if level==1 else -pi/2
        return max(0,math.floor((hi-alpha)/(2*pi))-math.ceil((lo-alpha)/(2*pi))+1)
    t=math.asin(level)
    def count(alpha):
        return max(0,math.floor((hi-alpha)/(2*pi))-math.ceil((lo-alpha)/(2*pi))+1)
    return count(t)+count(pi-t)

def inverse_count(R,v,model,level=0.26):
    # bracket stationary points using mesh 0.03; these particular finite inputs
    # have no unseen extremely narrow stationary intervals.
    n=int(math.ceil(2*R/0.03));xs=[-R+2*R*i/n for i in range(n+1)]
    h=lambda x:phase(x,v,model)
    d=lambda x:deriv(x,v,model)
    roots=[]
    for x,y in zip(xs,xs[1:]):
        dx=d(x);dy=d(y)
        if dx*dy<0:
            roots.append(brentq(d,x,y,xtol=1e-11))
    if -R<v<R:roots.append(v)
    boundaries=sorted([-R,R]+roots)
    nroots=sum(count_phase_in_interval(h(x),h(y),level) for x,y in zip(boundaries,boundaries[1:]))
    return nroots,len(boundaries)-1

def asy(R,model,b=0.4,omega=pi):
    base=2*omega*b/pi
    if model in (1,5,7,8):return base*R**3+(base*R**2 if model in (5,8) else 0)
    if model in (2,3,6):return base*R**2
    if model==4:return omega*b*(math.e-1/math.e)/pi*R**2
    raise ValueError

def run():
    # Derivative exactness via centered difference; include nonsmooth away from kink.
    for name in range(1,9):
        for x in [-5.17,-1.9,1.1,5.41]:
            h=1e-5; numerical=(phase(x+h,0.31,name)-phase(x-h,0.31,name))/(2*h)
            analytical=deriv(x,0.31,name)
            assert abs(numerical-analytical)<2e-6*(1+abs(analytical)),(name,x,numerical,analytical)
    # Exact total-variation mean identities; exponential integral is variation of e^-cos.
    ms=quad(lambda t: abs(pi*math.cos(pi*t)),0,2,epsabs=1e-12)[0]/2
    me=quad(lambda t: abs(pi*math.exp(-math.cos(pi*t))*math.sin(pi*t)),0,2,points=[0,1,2],epsabs=1e-12)[0]/2
    assert abs(ms-2)<1e-11
    assert abs(me-(math.e-1/math.e))<1e-11
    print('mean derivative magnitudes',round(ms,12),round(me,12))
    # Direct finite real preimage counts: periodic phases have O(R) remainder;
    # polynomial phases have at most O(1) turning points.
    for name in range(1,9):
        vals=[]
        for R in (18,38,75):
            count,segments=inverse_count(R,0.31,name,0.26)
            approximation=asy(R,name)
            assert count>0
            vals.append((R,count,round(approximation,2),round(count/approximation,5),segments))
        print('model',name,vals)
    # Quadratic term from adding |q| to Q: matching leading difference.
    for R in (20,40,80):
        n1,_=inverse_count(R,0.31,1,0.26)
        n5,_=inverse_count(R,0.31,5,0.26)
        n7,_=inverse_count(R,0.31,7,0.26)
        n8,_=inverse_count(R,0.31,8,0.26)
        expected=(2*pi*0.4/pi)*R*R
        assert abs((n5-n1)/expected-1)<0.4
        assert abs((n8-n7)/expected-1)<0.4
        print('absolute addition',R,n5-n1,n8-n7,round(expected,3))
    print('VERIFY_OK')
if __name__=='__main__':run()
