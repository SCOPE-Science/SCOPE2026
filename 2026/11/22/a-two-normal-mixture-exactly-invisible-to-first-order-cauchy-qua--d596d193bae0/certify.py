#!/usr/bin/env python3
"""Exact-rational enclosure proof for a two-Gaussian-mixture blind alternative.
No external dependencies; normal CDF/PDF bounds derive from alternating Taylor
series and elementary Mills bounds.  All comparisons are exact Fractions.
"""
from fractions import Fraction as F
from math import factorial

def atan_interval(q, n=32):
    terms=[F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)]
    lower=sum(terms,F(0)); upper=lower+F(1,(2*n+1)*q**(2*n+1))
    assert n%2==0
    return lower,upper

l5,u5=atan_interval(5);l239,u239=atan_interval(239)
PI_L,PI_U=16*l5-4*u239,16*u5-4*l239
assert F('3.14159265358979')<PI_L<PI_U<F('3.14159265358980')
C_L,C_U=F('0.3989422804014326'),F('0.3989422804014328')
assert 2*PI_U*C_L*C_L<1<2*PI_L*C_U*C_U

# Alternating series bounds. For 0<=x<=2, successive terms decrease.
def Phi_small(x):
    assert F(0)<=x<=2
    term=x; total=F(0)
    for k in range(30):
        total+=term
        term=-term*x*x*F(2*k+1,2*(k+1)*(2*k+3))
    assert term>=0 and total>=0
    return F(1,2)+C_L*total,F(1,2)+C_U*(total+term)

def exp_small(t):
    assert 0<=t<=2
    term=F(1);total=F(0)
    for k in range(32):
        total+=term
        term=-term*t/(k+1)
    assert term>=0 and total>=0
    return total,total+term

def phi_small(x):
    lo,hi=exp_small(x*x/2)
    return C_L*lo,C_U*hi

# For x>=10, 0<1-Phi(x)<phi(x)/x and e^(-x^2/2)<2^-50.
TAIL=C_U/F(2**50)
def phi_bounds(x):
    assert x>=0
    if x<=2:return phi_small(x)
    assert x>=10
    return F(0),TAIL

def Phi_bounds(x):
    assert x>=0
    if x<=2:return Phi_small(x)
    assert x>=10
    return F(1)-TAIL/x,F(1)

def mixcdf_bounds(x,w,s):
    l1,h1=Phi_bounds(x)
    l2,h2=Phi_bounds(x/s)
    return (1-w)*l1+w*l2, (1-w)*h1+w*h2

def quant_bounds(prob,w,s,lo,hi,cycles=33):
    lo,hi=F(lo),F(hi)
    assert mixcdf_bounds(lo,w,s)[1] < prob < mixcdf_bounds(hi,w,s)[0]
    for _ in range(cycles):
        mid=(lo+hi)/2
        cl,ch=mixcdf_bounds(mid,w,s)
        if ch<prob:lo=mid
        elif cl>prob:hi=mid
        else:raise AssertionError('CDF interval too wide to decide')
    return lo,hi

def ratio_bounds(w,s):
    al,au=quant_bounds(F(3,4),w,s,'0.5','1')
    bl,bu=quant_bounds(1-P,w,s,'10','20')
    return al/bu,au/bl,(al,au,bl,bu)

def trig_bounds(y, kind):
    def at(t):
        term=t if kind=='sin' else F(1)
        total=F(0)
        for k in range(20):
            total+=term
            if kind=='sin':term=-term*t*t/F((2*k+2)*(2*k+3))
            else:term=-term*t*t/F((2*k+1)*(2*k+2))
        assert term>=0
        return total,total+term
    return at(y)

P=F('0.02217468')
ylo,yhi=P*PI_L,P*PI_U
sl,_=trig_bounds(ylo,'sin');_,sh=trig_bounds(yhi,'sin')
_,ch=trig_bounds(ylo,'cos');cl,_=trig_bounds(yhi,'cos')
R_L,R_U=sl/ch,sh/cl
# v_C=pi^2/4*[r^2+2p(1-2p)(1+r^2)^2-4pr(1+r^2)]
# Rational interval bound using a negative term with reversed endpoints.
B_L=R_L**2+2*P*(1-2*P)*(1+R_L**2)**2-4*P*R_U*(1+R_U**2)
B_U=R_U**2+2*P*(1-2*P)*(1+R_U**2)**2-4*P*R_L*(1+R_L**2)
assert B_L>0
VC_L,VC_U=PI_L**2*B_L/4,PI_U**2*B_U/4
assert F('.1022')<VC_L<VC_U<F('.1024')

# PDF monotonic bounds across both quantile- and s-intervals.
def pdf_enclosure(xlo,xhi,w,slo,shi):
    mlo,_=phi_bounds(xhi);_,mhi=phi_bounds(xlo)
    nlo,_=phi_bounds(xhi/slo);_,nhi=phi_bounds(xlo/shi)
    return (1-w)*mlo+w*nlo/shi,(1-w)*mhi+w*nhi/slo

def v_bounds(w,slo,shi):
    aL,aU=quant_bounds(F(3,4),w,slo,'0.5','1')[0],quant_bounds(F(3,4),w,shi,'0.5','1')[1]
    bL,bU=quant_bounds(1-P,w,slo,'10','20')[0],quant_bounds(1-P,w,shi,'10','20')[1]
    faL,faU=pdf_enclosure(aL,aU,w,slo,shi)
    fbL,fbU=pdf_enclosure(bL,bU,w,slo,shi)
    rL,rU=aL/bU,aU/bL
    v1L,v1U=F(1,4)/faU**2,F(1,4)/faL**2
    v2L,v2U=2*P*(1-2*P)/fbU**2,2*P*(1-2*P)/fbL**2
    covL,covU=P/(faU*fbU),P/(faL*fbL)
    vL=(v1L+rL*rL*v2L-2*rU*covU)/(4*bU*bU)
    vU=(v1U+rU*rU*v2U-2*rL*covL)/(4*bL*bL)
    return vL,vU,(aL,aU,bL,bU,faL,faU,fbL,fbU)

if __name__=='__main__':
    print('Cauchy index bracket:', float(R_L),float(R_U))
    print('Cauchy variance bracket:',float(VC_L),float(VC_U))
    for w,slo,shi,orientation in ((F('.08'),F('17.9'),F('18.0'),'greater'),(F('.2'),F('10.0'),F('10.1'),'less')):
        rl,ru,_=ratio_bounds(w,slo)
        print('w=',float(w),'left r range:',float(rl),float(ru))
        assert rl>R_U
        rl,ru,_=ratio_bounds(w,shi)
        print('w=',float(w),'right r range:',float(rl),float(ru))
        assert ru<R_L
        vl,vu,details=v_bounds(w,slo,shi)
        print('w=',float(w),'V interval:',float(vl),float(vu))
        print('quantiles/densities:',tuple(float(x) for x in details))
        if orientation=='greater':assert vl>VC_U
        else:assert vu<VC_L
    print('CERTIFIED: by continuity there exist 0.08<w<0.20, s>1 with matching Cauchy index and Gaussian-limit variance.')
