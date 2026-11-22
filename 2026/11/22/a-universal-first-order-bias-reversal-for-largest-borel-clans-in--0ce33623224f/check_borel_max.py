"""Standalone numerical checks for the near-critical maximum-clan CDF.

Only the Python standard library is required.  Results are checks, not proofs.
"""
import math


def ibase(z):
    e = math.erfc(math.sqrt(z / 2.0))
    onehalf = math.sqrt(2.0 * math.pi) * e
    threehalf = 2.0 * math.exp(-z / 2.0) / math.sqrt(z) - onehalf
    return threehalf, threehalf - onehalf / 3.0


def predicted(mu, a, x):
    i, f = ibase(a*x)
    b = mu * a / math.sqrt(2*math.pi)
    p0 = math.exp(-b*i)
    correction = -p0*b*f
    return p0, correction


def exact(mu, a, x, n):
    delta=math.sqrt(a/n)
    theta=1-delta
    r=theta*math.exp(1-theta)
    log_r=math.log(r)
    kstart=int(n*x)+1
    # Summation beyond 100/delta^2 is negligible (<1e-20) for these checks.
    kmax=max(kstart+200, math.ceil(100/(delta*delta)))
    tail=0.0
    for k in range(kstart,kmax+1):
        logp=-math.log(theta)-1.5*math.log(k) - .5*math.log(2*math.pi)+k*log_r
        # exact factorial correction: k! / sqrt(2pi k) (k/e)^k
        stirling_err=math.lgamma(k+1)-((k+.5)*math.log(k)-k+.5*math.log(2*math.pi))
        tail += math.exp(logp-stirling_err)
    return math.exp(-mu*n*delta*tail)


def run():
    mu=1.4
    a=1.0
    import statistics
    for x in (0.5, 1.0, 2.5, 4.0):
        p0,coef=predicted(mu,a,x)
        print(f'x={x} limit={p0:.10f} coefficient={coef:.10f}')
        scaled_errors=[]
        for n in (400,1600,6400):
            p=exact(mu,a,x,n)
            scaled=(p-p0)/math.sqrt(a/n)
            scaled_errors.append(abs(scaled-coef))
            print(f' n={n}: exact={p:.10f} first_order_scaled={scaled:.9f} error={scaled_errors[-1]:.9f}')
            assert (p-p0)*coef>0
        assert scaled_errors[-1] < scaled_errors[0]
    z=1.8889859435151004
    assert abs(ibase(z)[1])<1e-12
    assert ibase(1.0)[1] > 0 and ibase(2.5)[1]<0
    print('ALL CHECKS PASSED')

if __name__=='__main__': run()
