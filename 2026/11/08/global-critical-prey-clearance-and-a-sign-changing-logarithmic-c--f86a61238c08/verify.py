"""Exact coefficient checks and finite-horizon diagnostics for a discrete ecological map."""
import sympy as s
import mpmath as mp

def symbolic():
    x=s.symbols('x')
    for a in [s.Rational(3,100),s.Rational(1,10)]:
        h=m=s.Rational(1,2); k=s.Integer(1); b=d=s.Rational(1,100)
        Y=h*m; D=1+k*Y; R=(d+b*Y)*D
        L=b+R*k/D**2; C=a+h*L; S=R*k**2*h**2/D**3
        B=C**2/s.Integer(2)-L*C+S
        A=C/s.Integer(2)+L-S/C
        H=Y+h*x+C*x*x
        F=x*s.exp(R/(1+k*H)-d-a*x-b*H)
        G=H*s.exp(h-H/(m+x))
        fx=s.series(F,x,0,4).removeO()
        gy=s.series(G,x,0,3).removeO()
        center=s.series(Y+h*F+C*F**2,x,0,3).removeO()
        assert s.simplify(fx-(x-C*x*x+B*x**3))==0
        assert s.simplify(gy-center)==0
        assert s.simplify((C*C-B)/C-A)==0
        assert s.simplify(R-s.Rational(1,64))==0
        assert s.simplify(L-s.Rational(1,50))==0
        assert s.simplify(S-s.Rational(1,500))==0
        assert s.simplify(A-({s.Rational(3,100):-s.Rational(1,100),s.Rational(1,10):s.Rational(5,88)}[a]))==0
        assert a > s.Rational(9,800)/(s.exp(s.Rational(1,2))-1)
        print('EXACT',a,'C',C,'A',A)
    astar=(2*s.sqrt(11)-3)/100
    cstar=astar+s.Rational(1,100)
    assert s.simplify(cstar/s.Integer(2)+s.Rational(1,50)-s.Rational(1,500)/cstar)==0
    assert astar>s.Rational(3,100) and astar<s.Rational(1,10)
    print('SIGN_THRESHOLD',astar)

def numerical():
    mp.mp.dps=35
    for astr in ('0.03','0.1'):
        a=mp.mpf(astr); b=d=mp.mpf('0.01'); h=m=mp.mpf('.5'); k=mp.mpf(1)
        Y=h*m; R=(d+b*Y)*(1+k*Y); L=b+R*k/(1+k*Y)**2
        C=a+h*L; S=R*k*k*h*h/(1+k*Y)**3; A=C/2+L-S/C
        x=mp.mpf('.04'); y=mp.mpf('.27')
        vals={}
        for n in range(1,25001):
            x,y=x*mp.exp(R/(1+k*y)-d-a*x-b*y),y*mp.exp(h-y/(m+x))
            if n in (10000,25000): vals[n]=(x,y,1/x-C*n-A*mp.log(n))
        print('NUM',astr,'n*x',mp.nstr(25000*vals[25000][0],13),'theory',mp.nstr(1/C,13),
              'n*(y-Y)',mp.nstr(25000*(vals[25000][1]-Y),13),'theory',mp.nstr(h/C,13),
              'log-adjusted',mp.nstr(vals[25000][2],13))
        assert abs(25000*vals[25000][0]-1/C)<mp.mpf('.7')
        assert abs(25000*(vals[25000][1]-Y)-h/C)<mp.mpf('.36')
    print('VERIFY_OK')

if __name__=='__main__':
    symbolic(); numerical()
