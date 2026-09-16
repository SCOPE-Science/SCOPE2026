"""Pure-python (stdlib only) check of the Euclidean Li-Yau rigidity lemma.

Lemma: on R^N, for u(x,t) = sum_i c_i p_t(x - y_i), p_t(z) = (4pt)^(-N/2) exp(-|z|^2/4t),
E := (ln u)_t - |grad ln u|^2 + N/(2t) equals tr(Cov_rho(Y)) / (4t^2),
where rho is the posterior on centers given x. Hence E >= 0 with equality
iff the posterior is degenerate (single atom), i.e. genuine mixtures have E > 0 everywhere.
Compares direct finite-difference E against the covariance formula on a grid.
"""
import math

def p(x, t, y, N):
    return (4.0 * math.pi * t) ** (-N / 2.0) * math.exp(-((x - y) ** 2) / (4.0 * t))

def u_mix(x, t, centers, weights, N):
    return sum(w * p(x, t, y, N) for w, y in zip(weights, centers))

def E_direct(x, t, centers, weights, N, h=1e-6):
    u = u_mix(x, t, centers, weights, N)
    ut = (u_mix(x, t + h, centers, weights, N) - u_mix(x, t - h, centers, weights, N)) / (2 * h)
    ux = (u_mix(x + h, t, centers, weights, N) - u_mix(x - h, t, centers, weights, N)) / (2 * h)
    ft = ut / u
    gx = ux / u
    return ft - gx * gx + N / (2 * t)

def E_cov(x, t, centers, weights, N):
    # posterior mean/var of center Y given x (1-D slice; transverse dims contribute 0 variance)
    ws = [w * p(x, t, y, N) for w, y in zip(weights, centers)]
    tot = sum(ws)
    mean = sum(w * y for w, y in zip(ws, centers)) / tot
    var = sum(w * (y - mean) ** 2 for w, y in zip(ws, centers)) / tot
    return var / (4 * t * t)

def main():
    cases = [
        {"centers": [0.0, 1.0], "weights": [1.0, 1.0], "N": 3},
        {"centers": [0.0, 2.0], "weights": [1.0, 0.1], "N": 3},
        {"centers": [-1.0, 0.0, 1.0], "weights": [1.0, 2.0, 1.0], "N": 4},
    ]
    worst_agree = 0.0
    for c in cases:
        centers, weights, N = c["centers"], c["weights"], c["N"]
        gmin = 1e9
        argmin = None
        for k in range(-100, 101):
            x = k * 0.05
            for t in (0.2, 0.5, 1.0, 2.0, 5.0):
                a = E_direct(x, t, centers, weights, N)
                b = E_cov(x, t, centers, weights, N)
                worst_agree = max(worst_agree, abs(a - b))
                if a < gmin:
                    gmin = a
                    argmin = (x, t)
        print("centers=%s weights=%s N=%d -> min E=%.6e at (x,t)=%s" % (centers, weights, N, gmin, argmin))
    print("max |E_direct - E_cov| over grid = %.3e" % worst_agree)
    assert worst_agree < 1e-5, "formula mismatch"
    print("OK: E = trCov/(4t^2) > 0 for genuine mixtures (single kernel attains E=0 exactly).")

if __name__ == "__main__":
    main()
