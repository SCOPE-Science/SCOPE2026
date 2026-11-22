"""Independent numerical and local-series checks for ellipse inner erosion geometry.
Requires mpmath, numpy. Run: python checker.py.
"""
import math
import mpmath as mp
import numpy as np
mp.mp.dps=65

def exact(a,b,t):
    a,b,t=map(mp.mpf,(a,b,t))
    if not (a>b>0 and 0<=t<=b): raise ValueError('a>b>0, 0<=t<=b')
    t0=b*b/a
    if t==b:return mp.mpf('0'),mp.mpf('0'),mp.pi/2
    theta=mp.mpf('0') if t<=t0 else mp.acos(b*mp.sqrt(b*b-t*t)/(t*mp.sqrt(a*a-b*b)))
    h=lambda u:mp.sqrt(a*a*mp.cos(u)**2+b*b*mp.sin(u)**2)
    rho=lambda u:a*a*b*b/h(u)**3
    area=2*mp.quad(lambda u:(h(u)-t)*(rho(u)-t),[theta,mp.pi/2])
    peri=4*mp.quad(lambda u:(rho(u)-t),[theta,mp.pi/2])
    return area,peri,theta

def steiner(a,b,t):
    P=4*mp.quad(lambda u:mp.sqrt(a*a*mp.sin(u)**2+b*b*mp.cos(u)**2),[0,mp.pi/2])
    return mp.pi*a*b-P*t+mp.pi*t*t,P

def area_numerical_halfplanes(a,b,t,n=2048):
    # Independent half-space intersection via Qhull, which correctly prunes
    # redundant ellipse tangent lines after the focal phase transition.
    from scipy.spatial import HalfspaceIntersection, ConvexHull
    ang=np.linspace(0,2*math.pi,n,endpoint=False)
    support=np.hypot(a*np.cos(ang),b*np.sin(ang))-t
    planes=np.column_stack([np.cos(ang),np.sin(ang),-support])
    vertices=HalfspaceIntersection(planes,np.array([0.,0.])).intersections
    return ConvexHull(vertices).volume

def main():
    a,b=mp.mpf('2'),mp.mpf('1')
    t0=b*b/a
    alpha=b*b*(a*a-b*b)/(2*a**3)
    predicted=mp.mpf(16)/105*alpha**(-mp.mpf(3)/2)
    predicted_p=mp.mpf(-8)/15*alpha**(-mp.mpf(3)/2)
    print('alpha',mp.nstr(alpha,20),'coeff_A',mp.nstr(predicted,20),'coeff_P',mp.nstr(predicted_p,20))
    for t in [mp.mpf('0.2'),mp.mpf('0.5'),mp.mpf('0.55'),mp.mpf('0.7'),mp.mpf('0.92')]:
        A,P,theta=exact(a,b,t)
        As,P0=steiner(a,b,t)
        if t<=t0: assert mp.almosteq(A,As,rel_eps=mp.mpf('1e-50'))
        else: assert A>As and P<P0-2*mp.pi*t
        A2=area_numerical_halfplanes(float(a),float(b),float(t),4096)
        err=abs(float(A)-A2)
        print('area check',float(t),float(A),A2,err)
        assert err<2e-4
    for delta in [mp.mpf('0.01'),mp.mpf('0.002'),mp.mpf('0.0004'),mp.mpf('0.00008')]:
        A,P,_=exact(a,b,t0+delta)
        As,P0=steiner(a,b,t0+delta)
        ca=(A-As)/delta**(mp.mpf(7)/2)
        cp=(P-(P0-2*mp.pi*(t0+delta)))/delta**(mp.mpf(5)/2)
        print('cusp',mp.nstr(delta,9),mp.nstr(ca,20),mp.nstr(cp,20))
    delta=mp.mpf('0.00008')
    A,P,_=exact(a,b,t0+delta)
    As,P0=steiner(a,b,t0+delta)
    assert abs((A-As)/delta**(mp.mpf(7)/2)/predicted-1)<mp.mpf('0.003')
    assert abs((P-P0+2*mp.pi*(t0+delta))/delta**(mp.mpf(5)/2)/predicted_p-1)<mp.mpf('0.003')
    # Exact endpoint check and geometrical nonnegative active curvature.
    for a0,b0 in [(3,1),(1.4,1),(2,0.3)]:
        t0=mp.mpf(b0)**2/a0
        for m in range(1,13):
            t=t0+(mp.mpf(b0)-t0)*m/13
            A,P,theta=exact(a0,b0,t)
            assert A>0 and P>0 and theta>0
            h=lambda u:mp.sqrt(a0*a0*mp.cos(u)**2+b0*b0*mp.sin(u)**2)
            assert a0*a0*b0*b0/h(theta)**3>=t
            assert A<mp.pi*a0*b0
    print('All deterministic erosion, area, curvature and cusp checks PASS.')

if __name__=='__main__':main()
