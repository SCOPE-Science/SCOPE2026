"""Independent numerical and exact-algebra checks for a six-direction linear mode.

Requires mpmath; no external data access.
"""
from mpmath import mp

mp.dps = 65


def matrix(r, p, k, theta):
    one = mp.mpf(1)
    J = mp.matrix([[one / 6] * 6 for _ in range(6)])
    I = mp.eye(6)
    L = mp.matrix(6)
    for i in range(6):
        L[i, i] = -2
        L[i, (i - 1) % 6] = one
        L[i, (i + 1) % 6] = one
    E = mp.matrix(6)
    for i in range(6):
        E[i, i] = mp.cos(theta - i * mp.pi / 3)
    return L - (1j * k * p) * E * ((1-r)*I-r*J) - k*k * ((1-r)*I+r*J)


def branch(r, p, k, theta):
    eig = mp.eig(matrix(r, p, k, theta), left=False, right=False)
    z = min(eig, key=lambda v: abs(v))
    assert abs(mp.im(z)) < mp.mpf('1e-45')
    return mp.re(z)


def angle_diff_coefficient(r, p):
    return p**6 * (1-r)**5 * (2*r - 1) / 576


def test():
    # Exact algebra of the two six-step angular winding contributions.
    # Mode gaps are Gamma_1=1, Gamma_2=3, Gamma_3=4, Gamma_4=3, Gamma_5=1.
    gaps = [mp.mpf(1),mp.mpf(3),mp.mpf(4),mp.mpf(3),mp.mpf(1)]
    assert mp.fprod(gaps)==36
    for rtxt, ptxt in [('0.2','2'),('0.35','4'),('0.65','3'),('0.8','6')]:
        r,p=mp.mpf(rtxt),mp.mpf(ptxt)
        winding_b = -(p**6)*(1-2*r)*(1-r)**5/(32*mp.fprod(gaps))
        assert mp.almosteq(winding_b,p**6*(1-r)**5*(2*r-1)/1152)
        target=angle_diff_coefficient(r,p)
        errors=[]
        for ktxt in ['0.03','0.015']:
            k=mp.mpf(ktxt)
            diff=branch(r,p,k,0)-branch(r,p,k,mp.pi/6)
            ratio=diff/(target*k**6)
            errors.append(abs(ratio-1))
            assert abs(ratio-1) < mp.mpf('0.3'), (r,p,k,ratio)
        assert errors[1] < errors[0], (r,p,errors)
        print('rho', rtxt,'Pe',ptxt,'relative errors', *[mp.nstr(x,7) for x in errors])

    # Exact invariant subspace at half filling, for arbitrary k and heading.
    r=mp.mpf('0.5')
    u=mp.matrix([mp.mpf(1)/6]*6)
    for ptxt,ktxt,atxt in [('2','0.08','0.17'),('8','0.6','0.71'),('1','1.4','0.0')]:
        p,k,th=mp.mpf(ptxt),mp.mpf(ktxt),mp.mpf(atxt)
        residual=matrix(r,p,k,th)*u+k*k*u
        assert max(abs(v) for v in residual)<mp.mpf('1e-58')
    print('half-filling exact eigenvector checks: passed')
    print('six-winding angular coefficient and high precision eigenvalue checks: passed')


if __name__=='__main__':
    test()
