"""Finite diagnostics for first-alias sampled-resolvent asymptotics.

These checks support numerical reproducibility; they do not certify the infinite theorem.
Requires Python 3.9+ standard library only.
"""
import cmath
import math


def damping(y, alpha, c_plus, c_minus, beta, lower_order):
    c = c_plus if y >= 0 else c_minus
    return c * abs(y)**alpha + lower_order * ((1 + abs(y))**beta - 1)


def scaled_error(T, xi, alpha, c_plus, c_minus, lam, beta, lower_order):
    eps = T**(1-alpha)
    y = xi/T
    u = T*(lam+damping(y, alpha, c_plus, c_minus, beta, lower_order))
    z = complex(u, -xi)
    if abs(z)<1e-3:
        h = z/12-z**3/720+z**5/30240-z**7/1209600
    else:
        h = 1/(1-cmath.exp(-z))-0.5-1/z
    return eps*h


def check():
    count = 0
    cases = [
        (0.45, 0.6, 1.1, 1e-9, 0.13, 0.3),
        (0.55, 1.2, 0.7, 1e-9, 0.20, 0.3),
        (0.30, 0.8, 0.8, 1e-11, 0.05, 0.2),
    ]
    for alpha, cp, cm, T, beta, lower_order in cases:
        eps = T**(1-alpha)
        limit = 1/(min(cp, cm)*(2*math.pi)**alpha)
        by_index = {}
        for n in (-3,-2,-1,1,2,3):
            c = cp if n>0 else cm
            center = 2*math.pi*n
            central = scaled_error(T, center, alpha,cp,cm,1.4,beta,lower_order)
            pred = 1/(c*(2*math.pi*abs(n))**alpha)
            assert abs(abs(central)/pred-1)<0.012, (n,central,pred)
            count+=1
            scores=[]
            for v in (-2.,-1.,-0.3,0.,0.3,1.,2.):
                actual=scaled_error(T,center+eps*v,alpha,cp,cm,1.4,beta,lower_order)
                model=1/complex(c*(2*math.pi*abs(n))**alpha,-v)
                assert abs(actual-model)/abs(model)<0.025, (alpha,n,v,actual,model)
                count+=1
                scores.append(abs(actual))
            by_index[n]=max(scores)
            assert abs(by_index[n]-pred)/pred<0.012
            count+=1
        best=max(by_index, key=by_index.get)
        assert abs(by_index[best]/limit-1)<0.012
        assert best in ((1,) if cp<cm else ((-1,) if cm<cp else (-1,1)))
        count+=2
        print('alpha',alpha,'c_plus',cp,'c_minus',cm,'scaled peak',round(by_index[best],8),'limiting constant',round(limit,8),'index',best)
    print('PASS',count,'finite scalar checks')

if __name__=='__main__':
    check()
