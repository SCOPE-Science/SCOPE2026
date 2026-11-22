"""Finite numerical checks for the explicit invariant-volume winding law."""
import math

def period(h):
    root=math.sqrt(h)
    b=math.sqrt(.25+root)
    m=(.25-root)/(.25+root)
    x,y=1.,math.sqrt(1.-m)
    for _ in range(100):
        xn=(x+y)/2
        yn=math.sqrt(x*y)
        if abs(xn-yn)<1.e-15*xn:
            x,y=xn,yn
            break
        x,y=xn,yn
    return 4*math.pi/(b*(x+y))

def lost_volume(h,n=12000):
    # Substitute s=h*u*u to handle the logarithmic endpoint at s=0.
    total=0.
    for j in range(n):
        u=(j+.5)/n
        total+=math.pi*h*u*period(h*u*u)
    return total/n

assert abs(period(1/16-1e-10)-2*math.pi*math.sqrt(2))<1e-3
for h in [1e-5,1e-7,1e-9]:
    p=period(h)
    assert abs(p-2*math.log(4/h)) < .01
    r=p/(2*math.pi)
    volume_prob=lost_volume(h)/(math.pi/3)
    lead=12*math.pi*r*math.exp(-math.pi*r)
    assert .9 < volume_prob/lead < 1.12
for z,q in [(.3,.1),(.5,.2),(.7,.15)]:
    A=z*(1-z)
    zp=A-q
    qp=(2*z-1)*q
    dH=qp*(2*A-2*q)+2*q*(1-2*z)*zp
    assert abs(dH)<1e-13
assert abs((-.5+.31)*2+(1-2*.31))<1e-13
print('HOPF_VOLUME_TAIL_VERIFY_OK')
