import numpy as np, math

P = 3**10
def cantor_int(n):
    ivs = [(0, P)]
    for _ in range(n):
        n0 = []
        for (A, B) in ivs:
            L = (B-A)//3
            n0.append((A, A+L)); n0.append((B-L, B))
        ivs = n0
    return ivs

def Qpair(A1, B1, A2, B2, h):
    F2 = lambda w: 0.0 if w == 0 else (w*w/2)*(math.log(abs(w))-1.5)
    a, b, c, d = A1/P, B1/P, A2/P, B2/P
    return -(F2(b-c)-F2(b-d)-F2(a-c)+F2(a-d))/(h*h)

n = 8
cells = cantor_int(n); N = len(cells); h = (cells[0][1]-cells[0][0])/P
Qm = np.array([[Qpair(A1, B1, A2, B2, h) for (A2, B2) in cells] for (A1, B1) in cells])
ones = np.ones(N)
o = np.array([1.0 if ((A+B)/2 < P/9 or (A+B)/2 > 8*P/9) else 0.0 for (A, B) in cells])
Qinv1 = np.linalg.solve(Qm, ones)
Qinvo = np.linalg.solve(Qm, o)
S11 = ones@Qinv1; S12 = ones@Qinvo; S22 = o@Qinvo
S = np.array([[S11, S12], [S12, S22]])
# constraint o'w >= t (outer mass at least t): dual gam <= 0, stationarity S[lam,gam]=[1,t] gives gam<0. Consistent.
# dual value = 2lam+2 gam t - [lam,gam]S[lam,gam] = lam*1+gam*t (at stationarity) = lam + gam t.
for a0 in [0.25, 0.255]:
    t = 2*a0
    sol = np.linalg.solve(S, np.array([1.0, t]))
    lam, gam = sol
    print(f"a0={a0}: lam+gam*t = {lam+gam*t:.8f} gam={gam:.6f}")
# Stability: d(val)/dS11 etc: val = c'S^{-1}c, c=(1,t). d val/dS = -zz', z=S^{-1}c=(lam,gam).
# |dval| <= lam^2 |dS11| + 2|lam gam| |dS12| + gam^2 |dS22|.
# If each S certified to abs err e, val err <= (lam^2+2|lam gam|+gam^2) e = (|lam|+|gam|)^2 e ~ (1.77)^2 e ~ 3.2e.
# So need e << 0.009/3.2 ~ 0.003. Interval S with 1e-6 accuracy is plenty IF Qinv solves certifiable.
# Certifying Q^{-1}-based S: S11 = 1'Q^{-1}1 etc. Rigorous route: compute FLOAT x1=Q^{-1}1, xo=Q^{-1}o,
# residuals r1=1-Q x1, ro=o-Q xo (interval, using Klo/Khi entrywise + summation margins),
# then S11 in [x1'1 - ||Q^{-1}||...]. Needs operator-norm bound on Q^{-1}: cond ~ ? eig min?
ev = np.linalg.eigvalsh(Qm)
print("Qm eig: min=", ev.min(), "max=", ev.max(), "cond=", ev.max()/ev.min())
print("S eig:", np.linalg.eigvalsh(S))
# residual sizes in float (non-rigorous preview)
x1 = Qinv1; xo = Qinvo
r1 = ones-Qm@x1; ro = o-Qm@xo
print("||r1||inf=", np.abs(r1).max(), "||ro||inf=", np.abs(ro).max())
