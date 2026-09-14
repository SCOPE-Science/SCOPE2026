"""Recovery test: permutation-symmetric coupled exponential family in 2D.

f_eps(x1,x2) ~ exp(-(x1+1)-(x2+1)-eps*(x1+x2)^2) on [-1,inf)^2 (log-concave
for eps>=0). Whiten to isotropic Y and report Var(|Y|^2)/n vs 8.
"""
import math

def moments(eps, L=14.0, N=721):
    # grid on [-1, L]^2, midpoint-ish uniform; tail beyond L neglected
    a = -1.0
    h = (L - a) / (N - 1)
    # 1D arrays
    xs = [a + h * i for i in range(N)]
    # weights * exp argument: ex[i] = -(x+1)
    ex = [-(x + 1.0) for x in xs]
    # s = x1+x2; quad term couples -> full 2D loop in blocks with Kahan-ish sum
    Z = 0.0
    # accumulate needed raw moments (use symmetry: only store canonical)
    s00 = 0.0; s10 = 0.0; s11 = 0.0; s20 = 0.0
    s30 = 0.0; s21 = 0.0
    s40 = 0.0; s31 = 0.0; s22 = 0.0
    for i, x1 in enumerate(xs):
        e1 = ex[i]
        for j, x2 in enumerate(xs):
            ssum = x1 + x2
            w = math.exp(e1 + ex[j] - eps * ssum * ssum)
            Z += w
            s10 += w * x1
            s11 += w * x1 * x2
            s20 += w * x1 * x1
            s30 += w * x1 ** 3
            s21 += w * x1 * x1 * x2
            s40 += w * x1 ** 4
            s31 += w * x1 ** 3 * x2
            s22 += w * (x1 * x1) * (x2 * x2)
    Z *= h * h
    nrm = 1.0 / (Z / (h * h))  # normalize sums (h^2 cancels)
    E1 = s10 * nrm / 1.0
    # raw moments (divide by count Z/h^2)
    def av(s):
        return s * nrm
    # E[X1]=E[X2]=m
    m = av(s10)
    r11 = av(s20)      # E X1^2
    r12 = av(s11)      # E X1 X2
    r111 = av(s30)
    r112 = av(s21)     # E X1^2 X2 (= E X1 X2^2)
    r1111 = av(s40)
    r1112 = av(s31)
    r1122 = av(s22)
    # central moments (symmetric)
    # cov: v = Var(X1), c = Cov
    v = r11 - m * m
    c = r12 - m * m
    # third central: t111 = E[(X1-m)^3], t112 = E[(X1-m)^2 (X2-m)]
    t111 = r111 - 3 * m * r11 + 2 * m ** 3
    t112 = r112 - 2 * m * r11 - m * r12 + 2 * m ** 3
    # fourth central
    u1111 = r1111 - 4 * m * r111 + 6 * m * m * r11 - 3 * m ** 4
    u1112 = r1112 - 3 * m * r112 - m * r111 + 3 * m * m * r11 + 3 * m * m * r12 - 3 * m ** 4
    # check: E[(X1-m)^3(X2-m)] = E[X1^3 X2] -3m E[X1^2 X2] - m E[X1^3] +3m^2 E[X1^2]+3m^2 E[X1X2] -3m^4
    u1122 = (r1122 - 2 * m * r112 - 2 * m * r112 + m * m * r11
             + m * m * r11 + 4 * m * m * r12 - 3 * m ** 4)
    # whiten: Sigma = [[v,c],[c,v]]; eig: lam+ = v+c (dir e+), lam- = v-c (dir e-)
    lp = v + c
    lm = v - c
    # Y1 = (D1+D2)/sqrt(2 lp)? define D=X-m; S=D1+D2, F=D1-D2; Y1=S/sqrt(2lp), Y2=F/sqrt(2lm)
    # E|Y|^4 = E[(S^2/(2lp) + F^2/(2lm))^2]
    # need E[S^4], E[F^4], E[S^2 F^2]
    # S^4 = D1^4+D2^4+4(D1^3D2+D1D2^3)+6 D1^2D2^2
    ES4 = 2 * u1111 + 8 * u1112 + 6 * u1122
    EF4 = 2 * u1111 - 8 * u1112 + 6 * u1122
    # S^2 F^2 = (D1^2+D2^2+2D1D2)(D1^2+D2^2-2D1D2) = (D1^2+D2^2)^2 -4 D1^2 D2^2
    # = D1^4+D2^4+2D1^2D2^2-4D1^2D2^2 = D1^4+D2^4-2D1^2D2^2
    ES2F2 = 2 * u1111 - 2 * u1122
    A = 1.0 / (2 * lp)
    B = 1.0 / (2 * lm)
    EY4 = A * A * ES4 + 2 * A * B * ES2F2 + B * B * EF4
    var = EY4 - 4.0
    return {"m": m, "v": v, "c": c, "lp": lp, "lm": lm,
            "EY4": EY4, "Var": var, "Var/n": var / 2.0,
            "u1111": u1111, "u1112": u1112, "u1122": u1122}

if __name__ == "__main__":
    for eps in [0.0, 0.05, 0.2, 0.5, 1.0, 2.0]:
        r = moments(eps)
        print(f"eps={eps:5.2f} Var/n={r['Var/n']:.6f} EY4={r['EY4']:.6f} "
              f"v={r['v']:.4f} c={r['c']:.4f} u1111={r['u1111']:.4f} "
              f"u1112={r['u1112']:.4f} u1122={r['u1122']:.4f}")
