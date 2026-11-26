"""Independent numerical tests of the Gaussian-kernel three-node determinant and collision spectrum."""
import mpmath as mp
mp.mp.dps=65
count=0
for L in [mp.mpf('0.01'),mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2'),mp.mpf('4'),mp.mpf('8')]:
    q=mp.exp(-L**2/4)
    det_mid=(1-q)**3*(1+q)
    residual=det_mid/(1-mp.exp(-L**2))
    expected=(1-q)**2/(1+q**2)
    assert mp.almosteq(residual,expected,rel_eps=mp.mpf('1e-55'))
    for j in range(1,60):
        a=mp.mpf(j)/60
        z=[mp.mpf('0'),a*L,L]
        mat=mp.matrix([[mp.exp(-(z[i]-z[k])**2/2) for k in range(3)] for i in range(3)])
        det=mp.det(mat)
        assert det>=0
        assert (det<det_mid if j != 30 else mp.almosteq(det,det_mid,rel_eps=mp.mpf("1e-45")))
        expdet=1-mp.exp(-a*a*L*L)-mp.exp(-(1-a)**2*L*L)-mp.exp(-L*L)+2*mp.exp(-L*L*(1-a+a*a))
        assert mp.almosteq(det,expdet,abs_eps=mp.mpf('1e-52'))
        count+=1
for a in [mp.mpf('0.11'),mp.mpf('0.25'),mp.mpf('0.5'),mp.mpf('0.65'),mp.mpf('0.88')]:
    targetmid=mp.mpf(2)/3*(a*a-a+1)
    targetsmall=a*a*(1-a)**2/(4*(a*a-a+1))
    for L in [mp.mpf('0.15'),mp.mpf('0.075'),mp.mpf('0.0375')]:
        z=[mp.mpf('0'),a*L,L]
        mat=mp.matrix([[mp.exp(-(z[i]-z[k])**2/2) for k in range(3)] for i in range(3)])
        eig=sorted(mp.eigsy(mat,eigvals_only=True))
        assert abs(eig[1]/(L*L)-targetmid)<L*L*3
        assert abs(eig[0]/(L**4)-targetsmall)<L*L*3
        count+=1
for L in [mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('2.3')]:
    c=mp.exp(-L**2/2)
    r=mp.exp(-L**2/8)
    lam_minus=(2+c-mp.sqrt(c*c+8*r*r))/2
    lam_plus=(2+c+mp.sqrt(c*c+8*r*r))/2
    z=[mp.mpf('0'),L/2,L]
    mat=mp.matrix([[mp.exp(-(z[i]-z[k])**2/2) for k in range(3)] for i in range(3)])
    eig=sorted(mp.eigsy(mat,eigvals_only=True))
    assert mp.almosteq(eig[0],lam_minus,rel_eps=mp.mpf('1e-40'))
    assert mp.almosteq(eig[1],1-c,rel_eps=mp.mpf('1e-40'))
    assert mp.almosteq(eig[2],lam_plus,rel_eps=mp.mpf('1e-40'))
    count+=1
print('PASS',count,'independent high-precision geometry/spectrum checks')
