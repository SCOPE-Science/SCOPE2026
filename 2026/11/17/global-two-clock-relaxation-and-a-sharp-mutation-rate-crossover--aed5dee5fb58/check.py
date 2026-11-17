"""Independent algebraic identities and finite numerical diagnostics for the stated flow.
Run: python check.py. Finite tests supplement, not replace, the proof.
"""
from fractions import Fraction as Q
from math import exp, log, sqrt, cos, sin


def cyc(i):
    return (i + 1) % 3, (i + 2) % 3


def field(x, alpha, beta, mu):
    S = sum(x)
    return [x[i] * (1 - x[i] - alpha*x[(i+1)%3] - beta*x[(i+2)%3]) + mu*(S-3*x[i]) for i in range(3)]


def B(u):
    return [-(u[(i+1)%3]-u[(i+2)%3])/3 for i in range(3)]


def N(u):
    return [-u[i]*(u[(i+1)%3]-u[(i+2)%3]) for i in range(3)]


def exact():
    count=0
    for k in [1,2,3,5]:
      for alpha in [Q(1,4),Q(2,3),Q(1),Q(3,2),Q(7,4)]:
        beta=2-alpha
        mu=Q(k,17)
        for x in [(Q(1,3),Q(2,5),Q(5,4)),(Q(4,3),Q(1,3),Q(2,7)),(Q(1,9),Q(1,9),Q(1,9))]:
            S=sum(x)
            dx=field(x,alpha,beta,mu)
            assert sum(dx)==S*(1-S), 'mass logistic'
            p=[xx/S for xx in x]
            dp=[(dx[i]-p[i]*sum(dx))/S for i in range(3)]
            a=alpha-1
            RHS=[-a*S*p[i]*(p[(i+1)%3]-p[(i+2)%3])+mu*(1-3*p[i]) for i in range(3)]
            assert dp==RHS, 'frequency reduction'
            Hdot=-sum(dp[i]/p[i] for i in range(3))
            assert Hdot==-mu*(sum(1/z for z in p)-9), 'exact entropy dissipation'
            u=[z-Q(1,3) for z in p]
            BU=B(u); BBU=B(BU)
            assert all(BBU[i]==-u[i]/3 for i in range(3)), 'rotation square on E'
            assert sum(BU)==0 and sum(N(u))==0
            assert all(dp[i]==-3*mu*u[i]+a*S*(BU[i]+N(u)[i]) for i in range(3)), 'linear-nonlinear separation'
            count+=1
    print('PASS: exact rational tests:',count,'states, five identities each')


def integrate():
    # Fast RK4 integration; analytic rotation removal is checked for two asymmetric cases.
    for alpha, mu, x0 in [(Q(1,2),0.09,(0.48,0.27,0.63)),(Q(3,2),0.11,(0.31,0.91,0.15))]:
      alpha=float(alpha); beta=2-alpha; a=alpha-1
      x=list(x0)
      S0=sum(x)
      h=0.01; nmax=5500
      outputs=[]
      def f(v):return field(v,alpha,beta,mu)
      for k in range(nmax+1):
        if k in (3500,4500,5500):
          t=k*h; S=sum(x)
          p=[xi/S for xi in x]; u=[pi-1/3 for pi in p]
          C=1/S0-1
          tau=log((exp(t)+C)/(1+C))
          omega=a*tau/sqrt(3)
          # exp(-a B tau)u = cos(omega)u - sqrt(3)sin(omega) B u
          Bu=B(u)
          w=[exp(3*mu*t)*(cos(omega)*u[i]-sqrt(3)*sin(omega)*Bu[i]) for i in range(3)]
          outputs.append((t,w))
          assert abs(S-1/(1+C*exp(-t)))<1e-9, 'mass logistic numerical check'
        if k==nmax:break
        k1=f(x)
        k2=f([x[i]+h*k1[i]/2 for i in range(3)])
        k3=f([x[i]+h*k2[i]/2 for i in range(3)])
        k4=f([x[i]+h*k3[i] for i in range(3)])
        x=[x[i]+h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in range(3)]
      t1,w1=outputs[0];t3,w3=outputs[-1]
      err=sqrt(sum((u-v)**2 for u,v in zip(w1,w3)))
      mag=sqrt(sum(u*u for u in w3))
      assert mag>0.0001
      assert err/mag<0.1,(err,mag,outputs)
      print('PASS: numerical normalized rotating asymptote alpha=',alpha,'mu=',mu,'last norm=',mag,'relative drift=',err/mag)

if __name__=='__main__':
 exact()
 integrate()
