"""Independent algebraic and high-precision checks for spherical rotation drift formulas."""
import sympy as S
import mpmath as m
h, s = S.symbols('h s', real=True, positive=True)

def series_drift(which):
    if which == 'stv2':
        a=s*h
    else:
        a=s*h/2
    u=S.sqrt(s*s+(1-s*s)*S.sin(a)**2)
    b=u*h if which == 'stv2' else u*h/2
    w=S.cos(a)*S.cos(b)
    if which=='stv2':
        d=w-s/u*S.sin(a)*S.sin(b)
        expr=(1+w)/S.sqrt(2*(1+d))
    else:
        d=w+s/u*S.sin(a)*S.sin(b)
        expr=2*d*w-S.cos(2*a)
    return S.series(expr,h,0,7).removeO().expand().collect(h)

v=series_drift('stv2')
r=series_drift('rich12')
assert S.simplify(v-1-h**4*s**2*(2*s**2-1)/8-h**6*s**4*(2-s**2)/24)==0
assert S.simplify(r-1+h**4*s**2*(1-s**2)/8-h**6*s**4*(1-s**2)/24)==0

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def norm(a):return m.sqrt(dot(a,a))
def sfe(p,hh,om=1):
    f=m.matrix([-om*p[1],om*p[0],0]); speed=norm(f)
    if speed==0:return p.copy()
    return m.cos(hh*speed)*p+m.sin(hh*speed)/speed*f

def stv2(p,hh,om=1):
    q=sfe(sfe(p,hh,om),hh,om)
    return (p+q)/norm(p+q)

def rich12(p,hh,om=1):
    coarse=sfe(p,hh,om)
    fine=sfe(sfe(p,hh/2,om),hh/2,om)
    return 2*dot(coarse,fine)*fine-coarse

def run(step,c,N,T=1,om=1):
    p=m.matrix([m.sqrt(1-c*c),0,c]); h=m.mpf(T)/N
    for _ in range(N):
        p=step(p,h,om)
        p=p/norm(p)
    return p[2]-c

m.mp.dps=65
for c in [m.mpf('0.3'),m.mpf('0.6'),m.sqrt(m.mpf('0.5')),m.mpf('-0.7')]:
    r2=1-c*c
    for step,coeff in [(stv2,c*r2*(2*r2-1)/8),(rich12,-c*r2*(1-r2)/8)]:
        e1=run(step,c,20);e2=run(step,c,40)
        if step==stv2 and abs(c*c-m.mpf('.5'))<m.mpf('1e-50'):
            coeff=c/64
            e1*=20**5;e2*=40**5
        else:
            e1*=20**3;e2*=40**3
        assert abs(e2-coeff)<abs(e1-coeff)+m.mpf('1e-25'),(c,step.__name__,e1,e2,coeff)
        assert abs(e2-coeff)<m.mpf('0.00025'),(c,step.__name__,e2,coeff)
print('PASS: two symbolic sixth-degree local expansions, eight convergent high-precision global checks')
