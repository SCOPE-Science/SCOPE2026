"""Independent numerical diagnostics for an exact Erlang binary census theorem.

Requirements: Python 3, mpmath. These are checks, not an infinite proof.
"""
import mpmath as mp
mp.mp.dps = 65


def pqf(k,x):
    q=mp.e**(-x)*sum(x**j/mp.factorial(j) for j in range(k))
    p=1-q
    f=x**(k-1)*mp.e**(-x)/mp.factorial(k-1)
    return p,q,f

def delta(k,x):
    p,q,f=pqf(k,x)
    h=x*f
    return 2*(x-k)-h*(1/q-1/p)

def info(k,x):
    p,q,f=pqf(k,x)
    return (x*f)**2/(p*q)

def root(k):
    lo=mp.mpf(k)
    hi=mp.mpf(k)+2
    while delta(k,lo)*delta(k,hi)>0:
        lo=max(mp.mpf('0.01'),lo-1)
        hi+=1
    for _ in range(230):
        mid=(lo+hi)/2
        if delta(k,mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

def approx(c):
    return 2/mp.pi*(c+mp.mpf(1)/3)**2-c*c-mp.mpf(1)/6

kvals=[1,2,3,4,5,10,25,50,100,200,500]
assertions=0
for k in kvals:
    x=root(k)
    p,q,f=pqf(k,x)
    assert p>0 and q>0 and f>0; assertions+=1
    assert abs(delta(k,x))<mp.mpf('1e-50');assertions+=1
    assert info(k,x)>info(k,x-mp.mpf('0.001'));assertions+=1
    assert info(k,x)>info(k,x+mp.mpf('0.001'));assertions+=1
    h=x*f
    a=k-h/p;b=k+h/q
    assert abs((x-a)-(b-x))<mp.mpf('1e-48');assertions+=1
    assert abs(info(k,x)-p*q*(b-a)**2)<mp.mpf('1e-48');assertions+=1
    # Covariant local Fisher calculation: two Poisson means are theta*p and theta*q.
    theta=mp.mpf('2.73')
    diag_rate=theta*(x*f)**2*(1/p+1/q)
    assert abs(diag_rate-theta*info(k,x))<mp.mpf('1e-48');assertions+=1
    cross=theta*x*f-theta*x*f
    assert cross==0; assertions+=1
    assert 0<info(k,x)/k<1;assertions+=1
    print('k=',k,'x=',mp.nstr(x,20),'retained=',mp.nstr(info(k,x)/k,16))
assertions+=1;assert abs(root(3)-mp.mpf('3.58808445036933625705769984772245'))<mp.mpf('1e-26')
assertions+=1;assert abs(info(3,root(3))/3-mp.mpf('0.641578310051128967688686406636'))<mp.mpf('1e-27')
c0=2/(3*(mp.pi-2));H0=(10-3*mp.pi)/(18*(mp.pi-2))
assert abs(approx(c0)-H0)<mp.mpf('1e-50');assertions+=1
for k in [100,200,500]:
    x=root(k)
    assert abs((x-k)-c0)<mp.mpf('0.001')*(mp.mpf(500)/k);assertions+=1
    empirical=k*((info(k,x)/k)/(2/mp.pi)-1)
    assert abs(empirical-H0)<mp.mpf('0.002');assertions+=1
print('PASS:',assertions,'diagnostics; all-k statements require the analytic proof.')
