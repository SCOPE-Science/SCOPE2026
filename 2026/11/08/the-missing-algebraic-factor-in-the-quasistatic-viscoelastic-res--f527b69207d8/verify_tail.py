"""Numerical diagnostics for a specified strong-memory resetting density."""
import mpmath as mp
mp.mp.dps=40
count=0
for r in map(mp.mpf,['0.5','1','2']):
    S=(2*r+1)/r
    A=2*(r+1)/r
    B=1/r
    C=mp.gamma(r+1)/mp.sqrt(2*mp.pi*S)*(2*S*S/A)**r
    delta=-(2*r+1)**3/(2*(r+1))
    assert S>0 and A>2*B-1
    count+=1
    for x in [12,20,35]:
        f=lambda u: r*u**(r-1)/mp.sqrt(2*mp.pi*(S-A*u+B*u*u))*mp.exp(-x*x/2*(1/(S-A*u+B*u*u)-1/S))
        val=mp.quad(f,[0,mp.mpf('.00001'),mp.mpf('.001'),mp.mpf('.1'),1])
        ratio=val/(C*x**(-2*r))
        # Error follows an x^-2 law and is bounded by a conservative multiple.
        assert abs(ratio-1) < 2*abs(delta)/x**2
        count+=1
        if x>=20:
            # Expected relative x^-2 coefficient is numerically approached.
            assert abs((ratio-1)*x*x-delta) < .18*abs(delta)
            count+=1
print('PASS:',count,'deterministic asymptotic checks')
