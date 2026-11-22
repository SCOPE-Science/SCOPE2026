"""Independent numerical spot checks for the Rayleigh--Lindley crossing theorem.
Python 3 standard library only; the analytic proof is in RESULT.md.
"""
import math

W1 = 0.5671432904097838729999686622
LAM = -math.log1p(-W1)
PINF = math.exp(-1)
QINF = 1-PINF


def R(theta, x):
    return (1+theta)*math.exp(theta*x)/(1+theta+theta*x) - 1


def omega(theta, alpha, x):
    return R(theta, x)**2/(2*alpha**2)


def a(theta, alpha, x):
    return -math.expm1(-(omega(theta, alpha, x)-omega(theta, alpha, x-1)))


def b(theta, alpha, x):
    return math.exp(math.exp(-omega(theta, alpha, x))-1)


def alpha_star(theta):
    return R(theta, 1)/math.sqrt(2*LAM)


def bisect(f, lo, hi, steps=100):
    vlo, vhi = f(lo), f(hi)
    assert vlo < 0 < vhi, (lo, hi, vlo, vhi)
    for _ in range(steps):
        mid=(lo+hi)/2
        if f(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def root_x(theta, alpha):
    f=lambda x: a(theta,alpha,x)-b(theta,alpha,x)
    hi=2.
    while f(hi)<0:
        hi *= 1.4
        assert hi<100.
    return bisect(f,1.,hi)


def root_w(theta):
    c=1-math.exp(-2*theta)
    f=lambda w: 1-math.exp(-c*w)-math.exp(math.exp(-w)-1)
    return bisect(f,0.,16.)


def check():
    assert abs(W1-math.exp(-W1))<1e-15
    for theta in (.25,.8,1.4):
        astar=alpha_star(theta)
        assert abs(a(theta,astar,1)-b(theta,astar,1))<5e-15
        for alpha in (.3*astar,astar,2*astar,20*astar):
            aa=[a(theta,alpha,k) for k in range(1,16)]
            bb=[b(theta,alpha,k) for k in range(1,16)]
            assert all(aa[i]<=aa[i+1]+1e-15 for i in range(14))
            assert any(aa[i]<aa[i+1]-1e-10 for i in range(14))
            assert all(bb[i]>=bb[i+1]-1e-15 for i in range(14))
            assert any(bb[i]>bb[i+1]+1e-10 for i in range(14))
            assert all(0<x<=1 for x in aa+bb)
            signs=[x-y for x,y in zip(aa,bb)]
            assert all(signs[i]<0 or signs[i+1]>0 for i in range(14))
            if alpha<astar:
                assert all(z>0 for z in signs)
            elif alpha>astar:
                assert signs[0]<0
                root=root_x(theta,alpha)
                assert root>1
                assert abs(a(theta,alpha,root)-b(theta,alpha,root))<2e-12
                log_surv_v=0.
                ratios=[]
                for k in range(1,50):
                    log_surv_v += math.log1p(-b(theta,alpha,k))
                    ratios.append(-omega(theta,alpha,k)-log_surv_v)
                assert ratios[0]>0
                assert any(z<0 for z in ratios)
                assert not any(ratios[i]<-1e-12 and ratios[i+1]>1e-12 for i in range(len(ratios)-1))
        w=root_w(theta)
        errors=[]
        for factor in (1e3,1e5,1e7):
            alpha=factor*astar
            xx=root_x(theta,alpha)
            predicted=(math.log(alpha)+math.log(math.log(alpha))+math.log(math.sqrt(2*w)/(1+theta)))/theta
            errors.append(abs(xx-predicted))
        assert errors[2]<errors[0]
        # Product correction: increasing partial products are actually decreasing;
        # they approach a positive limit after summable excess hazards.
        alpha=2*astar
        product=1.
        for k in range(1,50):
            hk=b(theta,alpha,k)
            assert PINF-1e-15<=hk<1
            product *= (1-hk)/QINF
        assert 0<product<1
        print(f"theta={theta:.2f}, alpha*={astar:.12g}, w={w:.12g}, root-errors={errors}, geometric-C≈{product:.12g}")
    print("PASS: numerical spot checks (not a substitute for the all-index proof).")

if __name__ == '__main__':
    check()
