"""Independent finite checks of an analytical frontier--recovery identification theorem."""
import math

def simpson(f,a,b,n=24000):
    assert n % 2 == 0
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+j*h) for j in range(1,n,2))+2*sum(f(a+j*h) for j in range(2,n,2)))

def F(k,a,b):
    assert k>0 and a>b>0
    return simpson(lambda u:1/math.atan(k*u),b,a)

def ratio(k,a,b,c):
    return F(k,a,b)/F(k,b,c)

def eta(z):
    return z/((1+z*z)*math.atan(z))

def eta_prime(z):
    return ((1-z*z)*math.atan(z)-z)/((1+z*z)**2*math.atan(z)**2)

def invert_ratio(target,a,b,c):
    lo,hi=1e-6,1e6
    assert ratio(lo,a,b,c)<target<ratio(hi,a,b,c)
    for _ in range(70):
        mid=math.sqrt(lo*hi)
        if ratio(mid,a,b,c)<target:lo=mid
        else:hi=mid
    return math.sqrt(lo*hi)

def main():
    for z in [1e-3,.01,.1,.5,1,2,10,100]:
        assert eta_prime(z)<0
        d=(eta(z+1e-5)-eta(z-1e-5))/2e-5
        assert abs(d-eta_prime(z))<4e-6
    for a,b,c in [(0.8,0.78,0.76),(1,.5,.1),(.9,.3,.2),(.7,.69,.01)]:
        lower=math.log(a/b)/math.log(b/c); upper=(a-b)/(b-c)
        assert lower<upper
        vals=[ratio(k,a,b,c) for k in [1e-5,1e-3,.1,.3,1,3,10,100,1e5]]
        assert all(lower<v<upper for v in vals), (lower,vals,upper)
        assert all(vals[j]<vals[j+1] for j in range(len(vals)-1))
        k=.73
        recovered=invert_ratio(ratio(k,a,b,c),a,b,c)
        assert abs(recovered-k)<1e-8
    a,b,c=.8,.78,.76
    k=1
    d01=F(k,a,b);d12=F(k,b,c)
    assert abs(d01-0.029913936910669067)<4e-10
    assert abs(d12-(0.060394838057554606-0.029913936910669067))<4e-10
    # gamma=1, rho=pi/2 => gamma*pi/(2*rho)=1; N=1, alpha=2/pi => k=1.
    R=d01/d12
    kr=invert_ratio(R,a,b,c)
    alpha=2*kr/math.pi
    rho=math.pi*F(kr,a,b)/(2*d01)
    assert abs(alpha-2/math.pi)<1e-9
    assert abs(rho-math.pi/2)<1e-9
    print('PASS: derivative, strict ratio bounds, invertibility, recovery of both rates, ODE-trajectory quadratures')
    print('ratio=',format(R,'.12f'),'parameter-free bounds',format(math.log(a/b)/math.log(b/c),'.12f'),format((a-b)/(b-c),'.12f'))
    print('alpha=',alpha,'rho=',rho,'increments=',d01,d12)
if __name__=='__main__':main()

def ode_crossing_test():
    """Directly step the full five-compartment model with a fixed-step RK4 integrator."""
    pi=math.pi; gamma=1.; beta=3.; rho=pi/2; alpha=2/pi; beta_R=.05; N=1.
    def root(r):return r-1+math.exp(-3*r)
    lo,hi=.5,.999
    for i in range(70):
        m=(lo+hi)/2
        if root(m)>0: hi=m
        else:lo=m
    Rinf=(lo+hi)/2; Sinf=1-Rinf
    def rhs(y):
        P,S,I,R,Q=y
        X=S+I+R
        J=rho*I*(2/pi)*math.atan((pi/2)*alpha*P/N)
        G=beta_R*S*R/X
        return [-J,J-beta*S*I/X-G,beta*S*I/X-gamma*I,
                gamma*I-(Rinf/Sinf)*G,G/Sinf]
    def step(y,h):
        a=rhs(y)
        b=rhs([v+h*w/2 for v,w in zip(y,a)])
        c=rhs([v+h*w/2 for v,w in zip(y,b)])
        d=rhs([v+h*w for v,w in zip(y,c)])
        return [v+h*(a_i+2*b_i+2*c_i+d_i)/6 for v,a_i,b_i,c_i,d_i in zip(y,a,b,c,d)]
    y=[.8,.199,.001,0.,0.]
    levels=[.78,.76]
    found=[];h=.002
    for j in range(6000):
        nxt=step(y,h)
        if levels and y[0]>=levels[0]>nxt[0]:
            z=(y[0]-levels[0])/(y[0]-nxt[0]); yy=[u+z*(v-u) for u,v in zip(y,nxt)]
            C=yy[3]+Rinf*yy[4]; found.append(C);levels.pop(0)
        y=nxt
        if not levels: break
    assert len(found)==2
    expected=[F(1,.8,.78), F(1,.8,.76)]
    assert abs(found[0]-expected[0])<4e-7, (found,expected)
    assert abs(found[1]-expected[1])<4e-7, (found,expected)
    print('PASS: 5-compartment RK4, frontier crossings and cumulative-removal identity',found)

if __name__=='__main__':ode_crossing_test()
