"""Independent kinematic-line verification of a closed fourth chord moment."""
from math import sqrt,log,pi,cos,sin
from scipy.integrate import quad

def closed(a,b,c):
    if min(a,b,c)<=0 or max(a,b,c)*2>=a+b+c:raise ValueError('nondegenerate sides required')
    area2=(a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c)/16
    z=0.0
    s=(a+b+c)/2
    for opposite,p,q in ((a,b,c),(b,a,c),(c,a,b)):
        ca=(p*p+q*q-opposite*opposite)/(2*p*q)
        si2=1-ca*ca
        def H(P,Q):
            h=P*ca
            return ((opposite**3-P**3)/3+h/2*((Q-h)*opposite+h*P+P*P*(1-ca*ca)*log(s/(s-Q))))
        z+=4*area2/(5*p*p*q*q)*(p*p*H(p,q)+q*q*H(q,p))
    return z

def line_quad(a,b,c):
    # vertices O=(0,0), B=(c,0), C=(x,y), with |OC|=b and |BC|=a.
    x=(b*b+c*c-a*a)/(2*c)
    y=sqrt(b*b-x*x)
    vs=((0.,0.),(c,0.),(x,y))
    def term(theta):
        nx,ny=cos(theta),sin(theta)
        ords=sorted(((nx*X+ny*Y,(X,Y)) for X,Y in vs),key=lambda t:t[0])
        (lo,A),(mid,B),(hi,C)=ords
        if hi-lo<1.e-14:return 0.0
        lam=(mid-lo)/(hi-lo)
        Q=(A[0]+lam*(C[0]-A[0]),A[1]+lam*(C[1]-A[1]))
        L2=(B[0]-Q[0])**2+(B[1]-Q[1])**2
        return (hi-lo)*L2*L2/5
    return quad(term,0,pi,epsabs=1e-10,epsrel=1e-10,limit=600,points=[k*pi/12 for k in range(1,12)])[0]

if __name__=='__main__':
    for abc in [(1,1,1),(2,3,4),(3,4,5),(2,2,3),(0.7,1.2,1.8),(10,10,0.5),(1,1.01,1.99),(2.3,3.1,4.4)]:
        x,y=closed(*abc),line_quad(*abc)
        print(abc,x,y,abs(x-y)/x)
        assert abs(x-y) <= 2.e-7*(1+x)
    from math import log
    assert abs(closed(1,1,1)-(9/40+27/160*log(3)))<1e-12
    for t in [0.1,0.3,2.7]:
        assert abs(closed(t,t,t)/(t**5)-(9/40+27/160*log(3)))<1e-10
    print('PASS 8 independent line-integral comparisons + 4 exact normalization tests')
