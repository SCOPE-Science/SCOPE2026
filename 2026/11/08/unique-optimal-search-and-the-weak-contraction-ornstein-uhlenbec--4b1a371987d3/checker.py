"""Numerical diagnostics for partial-rescaling first-passage optimization.

Requires mpmath. Analytic uniqueness and limit arguments are in RESULT.md;
finite evaluations here do not replace their proofs.
"""
import mpmath as mp
mp.mp.dps = 55


def R(a):
    a = mp.mpf(a)
    if a == 0:
        return mp.mpf(1)
    return mp.qgamma(mp.mpf('0.5'), a*a)/mp.sqrt(1-a*a)


def terms(a, beta, limit=False, N=90):
    """Return F, beta F', beta^2 F'' for nonnegative series."""
    a = mp.mpf(a)
    beta = mp.mpf(beta)
    if limit:
        oddmult = mp.sqrt(mp.pi/2)
        ce, co = mp.mpf(1), mp.mpf(1)
    else:
        oddmult = R(a)
        ce, co = mp.mpf(1), mp.mpf(1)
    s0=s1=s2=mp.mpf(0)
    for n in range(N):
        if n:  # ce corresponds C_2(n+1), co C_(2n+1)
            if limit:
                co *= 2*n-1
                ce *= 2*n
            else:
                co *= 1-a**(2*n-1)
                ce *= 1-a**(2*n)
        # limit scaled F*(b) coefficients use ce=2^n n! and co=(2n-1)!!
        # even C_2(n+1)/eps^n, odd C_(2n+1)/eps^n
        e = ce*beta**(2*n+2)/mp.factorial(2*n+2)
        o = co*oddmult*beta**(2*n+1)/mp.factorial(2*n+1)
        for k,v in ((2*n+2,e),(2*n+1,o)):
            s0+=v; s1+=k*v; s2+=k*(k-1)*v
    return s0,s1,s2


def optimum(a, limit=False):
    def residual(b):
        f,bdf,_=terms(a,b,limit)
        return bdf-2*f
    lo=mp.mpf('0.01'); hi=mp.mpf('30')
    assert residual(lo)<0 and residual(hi)>0
    for i in range(180):
        mid=(lo+hi)/2
        if residual(mid)>0: hi=mid
        else: lo=mid
    root=(lo+hi)/2
    return root,terms(a,root,limit)[0]/root**2


def phi_ou(b):
    return mp.quad(lambda y: mp.exp(b*b*y*y/2)*mp.sqrt(mp.pi/2)/b *
                   (1+mp.erf(b*y/mp.sqrt(2))), [0,1])


def run():
    tests=0
    # Exact coefficients in the published formula at a=0 are e^beta-1.
    for beta in (mp.mpf('.1'),mp.mpf('1'),mp.mpf('2'),mp.mpf('3')):
        f,_,_=terms(0,beta)
        assert abs(f-mp.expm1(beta)) < mp.mpf('1e-45')
        tests+=1
    for a in ('0','0.25','0.5','0.8','0.9','0.99'):
        root, val=optimum(a)
        f,dff,ddff=terms(a,root)
        assert abs(dff-2*f) < mp.mpf('1e-42')
        assert ddff-2*f>0
        assert terms(a,root*mp.mpf('.88'))[0]/(root*mp.mpf('.88'))**2>val
        assert terms(a,root*mp.mpf('1.12'))[0]/(root*mp.mpf('1.12'))**2>val
        tests+=4
        if mp.mpf(a) != 0:
            b=root*mp.sqrt(1-mp.mpf(a))
            print('a=',a, 'b*= ',mp.nstr(b,16), 'min(DT/L^2)=',mp.nstr(val,16))
    b0, t0=optimum(0,True)
    assert abs(phi_ou(b0)-t0)<mp.mpf('1e-42')
    tests+=1
    for b in (mp.mpf('.3'),mp.mpf('.8'),mp.mpf('1.3'),mp.mpf('2.5')):
        f=terms(0,b,True)[0]/b**2
        assert abs(f-phi_ou(b))<mp.mpf('1e-42')
        tests+=1
    print('limit b*=',mp.nstr(b0,30))
    print('limit b*^2=',mp.nstr(b0**2,30))
    print('limit min DT/L^2=',mp.nstr(t0,30))
    print('passed diagnostics=',tests)

if __name__=='__main__':
    run()
