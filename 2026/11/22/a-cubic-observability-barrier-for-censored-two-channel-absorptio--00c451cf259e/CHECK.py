"""Independent high-precision checks for censored outcome-dependent exponentials.

Run: python CHECK.py
Requires mpmath (pip install mpmath).
"""
import mpmath as m
m.mp.dps = 75

def fisher(B, p, l0, l1):
    a0, a1 = (1-p)*l0, p*l1
    v0, v1 = l0/(1-p), -l1/p
    mat = m.matrix(3)
    for ix, a, d, ell, v in ((0,a0,1-p,l0,v0), (1,a1,p,l1,v1)):
        for j in range(3):
            for k in range(3):
                def integrand(t):
                    z = [m.mpf('0')]*3
                    z[ix] = 1/a - t/d
                    z[2] = -v*t
                    return a*m.exp(-ell*t)*z[j]*z[k]
                mat[j,k] += m.quad(integrand, [0,B])
    surv = (1-p)*m.exp(-l0*B)+p*m.exp(-l1*B)
    d_surv = [-B*m.exp(-l0*B), -B*m.exp(-l1*B),
              m.exp(-l1*B)*(1+l1*B)-m.exp(-l0*B)*(1+l0*B)]
    for j in range(3):
        for k in range(3):
            mat[j,k] += d_surv[j]*d_surv[k]/surv
    aa = mat[0,0]*mat[1,1]-mat[0,1]*mat[1,0]
    subtract = (mat[2,0]*mat[0,2]*mat[1,1]
                -mat[2,0]*mat[1,2]*mat[0,1]
                -mat[2,1]*mat[0,2]*mat[1,0]
                +mat[2,1]*mat[1,2]*mat[0,0])/aa
    return mat[2,2]-subtract

def root_l2(B, a0,a1,p,p2):
    rates = [(a0/(1-p), a0/(1-p2),a0),
             (a1/p, a1/p2,a1)]
    integral = m.mpf('0')
    for ell, ell2, a in rates:
        integrand = lambda t: a*(m.exp(-ell*t/2)-m.exp(-ell2*t/2))**2
        integral += m.quad(integrand,[0,B])
    c = (1-p)*m.exp(-a0*B/(1-p))+p*m.exp(-a1*B/p)
    c2 = (1-p2)*m.exp(-a0*B/(1-p2))+p2*m.exp(-a1*B/p2)
    return integral+(m.sqrt(c)-m.sqrt(c2))**2

for p,l0,l1 in ((m.mpf('0.25'),m.mpf('1.2'),m.mpf('6')),
                (m.mpf('0.63'),m.mpf('0.8'),m.mpf('0.8')),
                (m.mpf('0.5'),m.mpf('7'),m.mpf('0.9'))):
    coeff = (l0**3/(1-p)+l1**3/p)/12
    ratios = [fisher(B,p,l0,l1)/(coeff*B**3)
              for B in map(m.mpf,('0.02','0.005','0.001'))]
    assert all(abs(float(t-1))<0.2 for t in ratios)
    assert abs(ratios[2]-1)<abs(ratios[1]-1)<abs(ratios[0]-1)
    print('Fisher coefficient check:', 'p=',p, 'rates=',l0,l1,
          'ratios=',*[m.nstr(t,11) for t in ratios])

for a0,a1,p,p2 in ((m.mpf('0.9'),m.mpf('1.5'),m.mpf('.25'),m.mpf('.55')),
                   (m.mpf('.4'),m.mpf('1.1'),m.mpf('.7'),m.mpf('.8'))):
    c = (a0*(a0/(1-p)-a0/(1-p2))**2
         +a1*(a1/p-a1/p2)**2)/12
    ratios=[root_l2(B,a0,a1,p,p2)/(c*B**3)
            for B in map(m.mpf,('0.02','0.005','0.001'))]
    assert abs(ratios[-1]-1)<m.mpf('.02')
    print('Hellinger coefficient check:', 'p=',p, 'p2=',p2,
          'ratios=',*[m.nstr(t,11) for t in ratios])

# Exact positive-definiteness and limiting leading coefficient are established
# in the accompanying proof, not inferred from these finite computations.
print('All high-precision tests passed.')
