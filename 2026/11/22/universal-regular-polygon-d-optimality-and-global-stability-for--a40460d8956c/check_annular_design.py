"""Numerical sanity checks for the stated annular sampling identities.

Run: python check_annular_design.py
Dependency: mpmath (arbitrary precision). Finite tests, not an infinite proof.
"""
import mpmath as mp
mp.mp.dps = 50

def theta(z, p):
    return mp.qp(z, p) * mp.qp(p / z, p)

def verify(qtext, rtext, rhotext, N):
    q, r, rho = map(mp.mpf, (qtext, rtext, rhotext))
    assert 0 < q < rho < 1 and r > 0
    p, R = q*q, rho*rho
    L, a = -mp.log(p), -mp.log(R)
    def v(t):
        return mp.log(abs(theta(mp.exp(1j*t),p)/theta(R*mp.exp(1j*t),p))**2)
    for t in [mp.mpf('.71'), mp.mpf('1.5'), mp.mpf('2.3'), mp.pi]:
        right_d = 4*mp.pi/L * mp.fsum(
            (1-mp.cos(2*mp.pi*h*a/L))*mp.sinh(2*mp.pi*h*(mp.pi-t)/L)/mp.sinh(2*mp.pi**2*h/L)
            for h in range(1, 301))
        right_dd = -8*mp.pi**2/L**2 * mp.fsum(
            h*(1-mp.cos(2*mp.pi*h*a/L))*mp.cosh(2*mp.pi*h*(mp.pi-t)/L)/mp.sinh(2*mp.pi**2*h/L)
            for h in range(1,301))
        assert abs(mp.diff(v,t)-right_d) < mp.mpf('1e-28')
        assert abs(mp.diff(v,t,2)-right_dd) < mp.mpf('1e-28')
        assert right_dd<0
    # Laurent truncation and theta-product determinant ratio are independent.
    mm = list(range(-180,181))
    coeff = [rho**(2*m)/(1+r*q**(2*m)) for m in mm]
    def gram(tt):
        return mp.matrix([[mp.fsum(c*mp.exp(1j*m*(tt[i]-tt[j])) for m,c in zip(mm,coeff)) for j in range(N)] for i in range(N)])
    regular = [2*mp.pi*j/N for j in range(N)]
    other = regular[:]
    other[1] += mp.mpf('.07')
    def potential(tt):
        return mp.fsum(v(tt[j]-tt[i]) for i in range(N) for j in range(i+1,N))
    D_reg, D_oth = mp.re(mp.det(gram(regular))),mp.re(mp.det(gram(other)))
    assert D_reg>D_oth>0
    assert abs(mp.log(D_reg/D_oth)-(potential(regular)-potential(other)))<mp.mpf('1e-28')
    residues = [mp.fsum(c for m,c in zip(mm,coeff) if m%N==j) for j in range(N)]
    assert abs(D_reg-N**N*mp.fprod(residues))/D_reg<mp.mpf('1e-28')
    gaps = [other[(i+1)%N]-other[i] if i<N-1 else other[0]+2*mp.pi-other[-1] for i in range(N)]
    curvature = (8*mp.pi**2/L**2)*(1-mp.cos(2*mp.pi*a/L))/mp.sinh(2*mp.pi**2/L)
    assert mp.log(D_reg/D_oth) >= curvature/4*mp.fsum((x-2*mp.pi/N)**2 for x in gaps)
    return True

if __name__=='__main__':
    cases=[('.25','.2','.55',3),('.4','1','.7',4),('.6','3','.81',3)]
    for case in cases:
        assert verify(*case)
        print('PASSED',case)
    print('PASS: 3 parameter sets, Fourier/theta/determinant/stability comparisons')
