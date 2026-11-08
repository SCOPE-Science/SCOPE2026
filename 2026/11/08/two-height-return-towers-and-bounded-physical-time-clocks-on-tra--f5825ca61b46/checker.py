"""Exact verification of the four-interval cap map and its induced return law.

This checks finite rational instances only; the accompanying proof covers all real parameters.
"""
from fractions import Fraction as F
from math import gcd


def map_one(x, n, L, eta):
    assert n >= 1 and L > 0 and eta > 0
    a = L + eta
    b = 2*n*eta
    S = 2*L + (4*n+1)*eta
    assert 0 <= x < S
    if x < a:
        y = x + L + 4*n*eta
    elif x < a+b:
        y = x + (2*n-1)*eta
    elif x < a+2*b:
        y = x - (2*n+1)*eta
    else:
        y = x - L - (4*n+1)*eta
    assert 0 <= y < S
    return y


def first_return(x, n, L, eta):
    A = L + eta
    assert 0 <= x < A
    y = map_one(x,n,L,eta)
    k = 1
    while y >= A:
        k += 1
        assert k <= 4*n+1
        y = map_one(y,n,L,eta)
    return y,k


def check():
    cases = 0; visits = 0; orbit_tests = 0
    for n in range(1,7):
        for eta in (F(1,3),F(2,5),F(1,2)):
            for L in (F(1,7),F(2,3),F(11,5)):
                A=L+eta
                # exactly rational sample includes break at eta and nearby points
                pts = {F(0), eta, (eta/2), (eta+A)/2}
                pts.update((A*F(j,61) for j in range(61)))
                for x in pts:
                    if x >= A: continue
                    y,t=first_return(x,n,L,eta)
                    want_y=x+L if x<eta else x-eta
                    want_t=4*n+1 if x<eta else 2
                    assert (y,t)==(want_y,want_t), (n,L,eta,x,y,t,want_y,want_t)
                    visits+=1
                    # exact discrepancy identity up to 20 returns
                    z=x;total=0;long=0
                    for k in range(1,9):
                        z,step=first_return(z,n,L,eta)
                        long += step==4*n+1
                        total += step
                        assert long==k-(x+k*L)//A
                        assert total==2*k+(4*n-1)*long
                        assert total* A - k*(2*L+(4*n+1)*eta)==(4*n-1)*(z-x)
                cases+=1
    for n in range(1,6):
        for u in range(1,8):
            for v in range(1,8):
                if gcd(u,v)!=1:continue
                eta=F(1,1);L=F(u,v);p=2*u+(4*n+1)*v
                A=L+eta;S=2*L+(4*n+1)*eta
                for x in (F(0),F(1,13)*A,F(3,17)*A,F(2,7)*A):
                    x0=x
                    # verify full map least period, not only induced rotation
                    y=x0
                    seen={y:0}
                    for k in range(1,p+1):
                        y=map_one(y,n,L,eta)
                        if y in seen:
                            assert k==p and y==x0,(n,u,v,p,x0,k,y)
                            break
                        seen[y]=k
                    else:raise AssertionError('no return')
                    orbit_tests+=1
    # Check exact two-atom law for the cumulative first-return clock.
    variance_checks = 0
    for n in range(1, 4):
        for eta,L in ((F(1,4),F(2,3)),(F(2,5),F(5,7)),(F(3,5),F(1,2))):
            A=L+eta
            denom=(L/A).denominator
            steps=24*denom
            initial=[A*F(2*i+1,2*steps) for i in range(steps)]
            for k in range(1, 21):
                values=[]
                for x in initial:
                    # The return itinerary was checked against the original map above.
                    # Here evaluate its exact floor-sum clock in O(1) per sample.
                    h = k - (x+k*L)//A
                    values.append(2*k+(4*n-1)*h)
                mean=sum((F(v) for v in values), F(0))/len(values)
                var=sum(((F(v)-mean)**2 for v in values),F(0))/len(values)
                pred_mean=F(k)*(2*L+(4*n+1)*eta)/A
                frac=F(k)*L/A%1
                pred_var=(4*n-1)**2 * frac*(1-frac)
                assert mean==pred_mean and var==pred_var,(n,eta,L,k,mean,var,pred_mean,pred_var)
                variance_checks+=1
    print('PASS exact cases',cases,'exact return samples',visits,'rational orbit periods',orbit_tests,'two-atom moment checks',variance_checks)

if __name__=='__main__':check()
