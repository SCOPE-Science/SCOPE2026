"""Optional numerical reproduction of the local resetting-onset constants.
Requires mpmath; unlike certificate.py this is NOT a rigorous interval proof.
"""
import mpmath as mp
mp.mp.dps = 50

def first_moment(x):
    return -x*mp.log(x)-(1-x)*mp.log(1-x)

def second_moment(x):
    h = first_moment(x)
    return mp.pi**2/3 - 2*((1-x)*mp.polylog(2,1-x)+x*mp.polylog(2,x)+h)

def third_moment(x):
    # First Green inversion in normalized time.
    a = mp.quad(lambda y: second_moment(y)/(1-y), [0,x])
    b = mp.quad(lambda y: second_moment(y)/y, [x,1])
    return 3*((1-x)*a+x*b)

def laplace(x, rate):
    a=(1+mp.sqrt(1-4*rate))/2
    b=1-a
    c=mp.gamma(2-a)*mp.gamma(2-b)
    return mp.re(c*(x*mp.hyp2f1(a,b,2,x)+(1-x)*mp.hyp2f1(a,b,2,1-x)))

def main():
    c1=lambda x: first_moment(x)**2-second_moment(x)/2
    x=mp.findroot(c1,(mp.mpf('.8152'),mp.mpf('.8154')))
    u1=first_moment(x);u2=second_moment(x);u3=third_moment(x)
    c2=u1**3-u1*u2+u3/6
    cp=2*u1*mp.log((1-x)/x)+mp.polylog(2,x)-mp.polylog(2,1-x)
    k=-cp/(4*c2)
    print('xcrit =',mp.nstr(x,24))
    print('mcrit =',mp.nstr(2*x-1,24))
    print('c1prime =',mp.nstr(cp,22))
    print('c2crit =',mp.nstr(c2,22))
    print('slope rate/magnetization =',mp.nstr(k,22))
    for mstr in ['.6307','.631','.632']:
        m=mp.mpf(mstr); y=(1+m)/2
        guess=k*(m-(2*x-1))
        def mean_restart(rate):
            F=laplace(y,rate)
            return (1-F)/(rate*F)
        opt=mp.findroot(lambda rate: mp.diff(mean_restart,rate),
                        (guess*mp.mpf('.8'),guess*mp.mpf('1.2')))
        print('m=',mstr,'opt_rate=',mp.nstr(opt,14),
              'local_slope_ratio=',mp.nstr(opt/(m-(2*x-1)),14))
    a=(1+mp.sqrt(1-4*mp.mpf('.2')))/2;b=1-a
    def testfunc(t):
        return mp.re(mp.gamma(2-a)*mp.gamma(2-b)*(t*mp.hyp2f1(a,b,2,t)+(1-t)*mp.hyp2f1(a,b,2,1-t)))
    residual=x*(1-x)*mp.diff(testfunc,x,2)-mp.mpf('.2')*testfunc(x)
    assert abs(residual)<mp.mpf('1e-35')
    print('hypergeometric ODE residual:',mp.nstr(residual,7))
if __name__=='__main__':main()
