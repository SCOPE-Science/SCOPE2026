#!/usr/bin/env python3
"""Standalone finite-precision diagnostics for a steep sigmoid rotation map."""
import mpmath as mp
mp.mp.dps = 105
tested=0
worst_u=mp.mpf('0')
worst_multiplier=mp.mpf('0')
worst_response=mp.mpf('0')
worst_arithmetic=mp.mpf('0')
for n,k,a in [(4,1,400),(4,3,400),(5,1,550),(5,2,550),(5,3,550),(5,4,550),(7,2,700),(7,3,700)]:
    a=mp.mpf(a)
    q=mp.exp(-a/(2*n))
    h=1/(2*mp.mpf(n))
    for sigma in [-3,-1,0,1,3]:
        sig=mp.mpf(sigma)
        b=mp.mpf(k)/n + sig*q/n
        def F(x):
            g=1/(1+mp.exp(-a*x))
            return x+b-g
        def H(u):
            x=h+u/a
            y=x
            for _ in range(n):
                y=F(y)
            return (y-x)/q
        pred=mp.asinh(sig/2)
        u=mp.findroot(H,(pred-mp.mpf('0.1'),pred+mp.mpf('0.1')))
        x=h+u/a
        C=mp.cosh(pred)
        tstar=next(t for t in range(1,n) if (t*k)%n==n-1)
        c0=-(1+(tstar*sig/n)*mp.exp(pred))/(2*C)
        y=x
        mu=mp.mpf(1)
        Db=mp.mpf(0)
        seen=set()
        m=0
        for j in range(n):
            assert m not in seen
            seen.add(m)
            ref=(mp.mpf(m)+mp.mpf('0.5'))/n
            assert abs(y-ref-u/a) < 30*q
            coeff=c0+j*sig/n
            if j>0: coeff+=mp.exp(-pred)
            if j>tstar: coeff-=mp.exp(pred)
            discrepancy=abs((y-ref-pred/a)/q-coeff)
            assert discrepancy < 60/a+100*a*q
            worst_arithmetic=max(worst_arithmetic,discrepancy)
            g=1/(1+mp.exp(-a*y))
            fprime=1-a*g*(1-g)
            assert 0 < fprime <= 1
            Db=fprime*Db+1
            mu*=fprime
            y=F(y)
            m=m+k if m<0 else m+k-n
        assert m==0
        assert abs((y-x)/q) < mp.mpf('1e-70')
        erru=abs(u-pred)
        errm=abs((1-mu)/(2*a*q)-mp.cosh(pred))
        errDb=abs(Db-n)
        assert erru < 50*a*q
        assert errm < 50*a*q
        assert errDb < 50*a*q
        worst_u=max(worst_u,erru)
        worst_multiplier=max(worst_multiplier,errm)
        worst_response=max(worst_response,errDb)
        tested+=1
print("EOS_ALL_DENOMINATOR_DETUNING_OK", "cases="+str(tested),
      "max_u_error="+mp.nstr(worst_u,8),
      "max_mult_error="+mp.nstr(worst_multiplier,8),
      "max_db_error="+mp.nstr(worst_response,8),
      "max_arith_coeff_error="+mp.nstr(worst_arithmetic,8))
