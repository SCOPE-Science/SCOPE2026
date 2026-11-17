"""Independent computational spot-checks for short-area boundary chords.
Only uses analytic input geometry; not a substitute for the proof.
"""
import math
import mpmath as mp
mp.mp.dps = 38

def oval(m,eps,theta):
    m=int(m); e=mp.mpf(eps)
    x=mp.sin(theta)+e/2*(mp.sin((m+1)*theta)/(m+1)+mp.sin((m-1)*theta)/(m-1))
    y=-mp.cos(theta)+e/2*(-mp.cos((m+1)*theta)/(m+1)+mp.cos((m-1)*theta)/(m-1))
    return x,y

def cap(m,eps,theta0,h):
    m=int(m); e=mp.mpf(eps);h=mp.mpf(h);theta0=mp.mpf(theta0)
    s=lambda t:t+e*mp.sin(m*t)/m
    sm=s(theta0)
    minus=mp.findroot(lambda t:s(t)-sm+h/2,theta0-h/2)
    plus=mp.findroot(lambda t:s(t)-sm-h/2,theta0+h/2)
    f=lambda t:oval(m,e,t)
    def integrand(t):
       x,y=f(t);rho=1+e*mp.cos(m*t)
       return x*rho*mp.sin(t)-y*rho*mp.cos(t)
    x0,y0=f(minus);x1,y1=f(plus)
    return (mp.quad(integrand,[minus,plus])-(x0*y1-y0*x1))/2

def local(m,eps,theta0,h):
    e=mp.mpf(eps);t=mp.mpf(theta0);h=mp.mpf(h)
    rho=1+e*mp.cos(m*t);dr=-e*m*mp.sin(m*t);ddr=-e*m*m*mp.cos(m*t)
    # k=1/rho, dk/ds=-rho_theta/rho^3, d2k/ds2=-rho_tt/rho^4+3rho_t^2/rho^5
    k=1/rho;k2=-ddr/rho**4+3*dr**2/rho**5
    return k*h**3/12+(k2/480-k**3/240)*h**5

def check():
    for h in [mp.mpf('0.3'),mp.mpf('0.15'),mp.mpf('0.075')]:
        area=cap(2,0,0.37,h)
        exact=(h-mp.sin(h))/2
        assert mp.almosteq(area,exact,rel_eps=mp.mpf('1e-24'))
        print('circle',mp.nstr(h,8),'area',mp.nstr(area,12),'residual',mp.nstr(area-local(2,0,0.37,h),12))
    for m,e,th in [(2,'0.5','0.38'),(3,'0.4','0.75'),(4,'0.2','0.6')]:
        residual=[]
        for h in ['0.24','0.12','0.06']:
            h=mp.mpf(h)
            area=cap(m,e,th,h); appr=local(m,e,th,h)
            residual.append(abs(area-appr))
            print('oval',m,e,'h',mp.nstr(h,6),'area',mp.nstr(area,15),'error/h^7',mp.nstr((area-appr)/h**7,12))
        assert residual[0]>residual[1]>residual[2]
        assert residual[0]/residual[1]>40 and residual[1]/residual[2]>40
    for m,e in [(2,mp.mpf('0.5')),(2,mp.mpf('0.6')),(2,mp.mpf('0.7')),(3,mp.mpf('0.4')),(3,mp.mpf('0.5'))]:
        jf=lambda t:(e*m*mp.sin(m*t)/(1+e*mp.cos(m*t)))**2
        J=mp.quad(jf,[2*mp.pi*j/64 for j in range(65)])
        formula=2*mp.pi*m*m*(1/mp.sqrt(1-e*e)-1)
        assert mp.almosteq(J,formula,rel_eps=mp.mpf('1e-27'))
        sign='negative' if J>2*mp.pi else 'positive' if J<2*mp.pi else 'zero'
        print('gradient',m,str(e),'J',mp.nstr(J,15),'B_sign',sign)
    # Circle unit: exact probability of small area vs its first two terms.
    for t in [mp.mpf('1e-3'),mp.mpf('1e-4'),mp.mpf('1e-5')]:
        h=mp.findroot(lambda h:(h-mp.sin(h))/2-t,(12*t)**(mp.mpf(1)/3))
        true=h/mp.pi
        approx=(12*t)**(mp.mpf(1)/3)/mp.pi+t/(5*mp.pi)
        print('CDF_circle',mp.nstr(t,8),'true',mp.nstr(true,15),'approx',mp.nstr(approx,15),'error/t^(5/3)',mp.nstr((true-approx)/t**(mp.mpf(5)/3),12))
        assert abs(true-approx)<mp.mpf('5')*t**(mp.mpf(5)/3)
    print('SMOOTH_CAP_AREA_CHECKS_OK')
if __name__=='__main__':check()
