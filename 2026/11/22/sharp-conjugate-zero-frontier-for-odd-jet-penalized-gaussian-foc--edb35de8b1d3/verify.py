import mpmath as mp
mp.mp.dps=40
checks=0
for m in (3,5,7,9):
    for tau in ('0.000001','0.03','1','200'):
        T=mp.mpf(tau)
        q=T/(1+T*mp.factorial(m))
        level=(m-1)*mp.pi
        def theta(s):
            return mp.findroot(lambda a:m*a-s*mp.sin(a)-level,(level/m,mp.pi-mp.mpf('0.0001')),solver='anderson')
        def g(s):return mp.log(q)+m*mp.log(s)-s*mp.cos(theta(s))
        lo=mp.mpf('1e-8');hi=mp.mpf('2')
        while g(hi)<0:hi*=2
        for _ in range(85):
            z=(lo+hi)/2
            if g(z)>0:hi=z
            else:lo=z
        r=(lo+hi)/2
        ang=theta(r)
        x=r*mp.exp(1j*ang)
        assert abs(mp.exp(x)-q*x**m)<mp.mpf('1e-18')
        checks+=1
        root_scale=q**(-mp.mpf(1)/m)/m
        roots=[-m*mp.lambertw(-root_scale*mp.exp(2*mp.pi*1j*j/m),k) for j in range(m) for k in range(-6,7)]
        nearest=min(abs(z) for z in roots)
        assert abs(nearest-r)<mp.mpf('1e-18')
        checks+=1
        rho=mp.findroot(lambda t:t+m*mp.log(t)+mp.log(q),(r/2,r))
        assert 0<rho<r
        checks+=1
print('PASS',checks,'diagnostics; finite checks supplement analytic proof')
