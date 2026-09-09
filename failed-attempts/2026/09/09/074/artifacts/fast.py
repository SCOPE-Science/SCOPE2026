"""Fast CRTBP/ERTBP propagation: vectorized RK45 with adaptive stepping in numpy.
Operates on batches of states (n,6) simultaneously. Pure numpy, no numba/scipy.
"""
import numpy as np

MU = 0.012150585609624

def crtbp_acc(s, mu=MU):
    x = s[..., 0]; y = s[..., 1]; z = s[..., 2]
    r1 = np.sqrt((x+mu)**2+y**2+z**2)
    r2 = np.sqrt((x-1+mu)**2+y**2+z**2)
    ax = x - (1-mu)*(x+mu)/r1**3 - mu*(x-1+mu)/r2**3
    ay = y - (1-mu)*y/r1**3 - mu*y/r2**3
    az = -(1-mu)*z/r1**3 - mu*z/r2**3
    return ax, ay, az

def crtbp_rhs_batch(t, s, mu=MU):
    s = np.asarray(s, float)
    ax, ay, az = crtbp_acc(s, mu)
    out = np.empty_like(s)
    out[..., 0] = s[..., 3]; out[..., 1] = s[..., 4]; out[..., 2] = s[..., 5]
    out[..., 3] = ax + 2*s[..., 4]; out[..., 4] = ay - 2*s[..., 3]; out[..., 5] = az
    return out

def ertbp_rhs_batch(f, s, mu=MU, e=0.0549):
    s = np.asarray(s, float)
    ax, ay, az = crtbp_acc(s, mu)
    den = 1.0 + e*np.cos(f)
    out = np.empty_like(s)
    out[..., 0] = s[..., 3]; out[..., 1] = s[..., 4]; out[..., 2] = s[..., 5]
    out[..., 3] = ax/den + 2*s[..., 4]; out[..., 4] = ay/den - 2*s[..., 3]; out[..., 5] = az/den
    return out

# Dormand-Prince coefficients
_C = np.array([0, 1/5, 3/10, 4/5, 8/9, 1.0, 1.0])
_A = [
    [],
    [1/5],
    [3/40, 9/40],
    [44/45, -56/15, 32/9],
    [19372/6561, -25360/2187, 64448/6561, -212/729],
    [9017/3168, -355/33, 46732/5247, 49/176, -5103/18656],
    [35/384, 0, 500/1113, 125/192, -2187/6784, 11/84],
]
_B5 = np.array([35/384, 0, 500/1113, 125/192, -2187/6784, 11/84, 0])
_B4 = np.array([5179/57600, 0, 7571/16695, 393/640, -92097/339200, 187/2100, 1/40])

def rk45_batch(fun, t, y, h, *a, **k):
    """One RK45 step on batch y (n,6). Returns (y5, err_vec(n,))."""
    k1 = fun(t, y, *a, **k)
    k2 = fun(t + _C[1]*h, y + h*(_A[1][0]*k1), *a, **k)
    k3 = fun(t + _C[2]*h, y + h*(_A[2][0]*k1 + _A[2][1]*k2), *a, **k)
    k4 = fun(t + _C[3]*h, y + h*(_A[3][0]*k1 + _A[3][1]*k2 + _A[3][2]*k3), *a, **k)
    k5 = fun(t + _C[4]*h, y + h*(_A[4][0]*k1 + _A[4][1]*k2 + _A[4][2]*k3 + _A[4][3]*k4), *a, **k)
    k6 = fun(t + _C[5]*h, y + h*(_A[5][0]*k1 + _A[5][1]*k2 + _A[5][2]*k3 + _A[5][3]*k4 + _A[5][4]*k5), *a, **k)
    y5 = y + h*(_A[6][0]*k1 + _A[6][1]*k2 + _A[6][2]*k3 + _A[6][3]*k4 + _A[6][4]*k5 + _A[6][5]*k6)
    k7 = fun(t + _C[6]*h, y5, *a, **k)
    y5 = y + h*(_B5[0]*k1 + _B5[1]*k2 + _B5[2]*k3 + _B5[3]*k4 + _B5[4]*k5 + _B5[5]*k6 + _B5[6]*k7)
    y4 = y + h*(_B4[0]*k1 + _B4[1]*k2 + _B4[2]*k3 + _B4[3]*k4 + _B4[4]*k5 + _B4[5]*k6 + _B4[6]*k7)
    sc = np.abs(y5) + 1.0
    err = np.max(np.abs(y5 - y4)/sc, axis=-1)
    return y5, err

def integrate_batch(fun, t0, Y0, t1, tol=1e-12, h0=0.02, hmin=1e-5, hmax=0.1, *a, **k):
    Y = np.array(Y0, float, copy=True)
    if Y.ndim == 1:
        Y = Y[None, :]
    t = t0
    h = h0 if t1 > t0 else -h0
    n = 0
    while (h > 0 and t < t1) or (h < 0 and t > t1):
        if (h > 0 and t + h > t1) or (h < 0 and t + h < t1):
            h = t1 - t
        Y5, err = rk45_batch(fun, t, Y, h, *a, **k)
        emax = np.max(err)
        if emax < tol or abs(h) < hmin*1.01:
            t = t + h; Y = Y5
        fac = 0.9*(tol/max(emax, 1e-20))**0.2 if emax > 0 else 2.0
        fac = min(3.0, max(0.3, fac))
        h = np.clip(h*fac, -hmax, hmax)
        if abs(h) < hmin:
            h = np.sign(h)*hmin
        n += 1
        if n > 60000:
            raise RuntimeError("too many steps")
    return Y

def prop_ert(s, f0, f1, e, tol=1e-12):
    Y = integrate_batch(ertbp_rhs_batch, f0, np.array(s, float), f1, tol=tol, e=e)
    return Y[0] if Y.shape[0] == 1 else Y
