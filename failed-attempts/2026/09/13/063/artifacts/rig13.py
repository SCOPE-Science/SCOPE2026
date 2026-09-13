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
v = np.linalg.solve(Qm, ones); m = v/v.sum(); m = (m+m[::-1])/2; m /= m.sum()
Vf = 1/v.sum()
# free row values r = Qm m = Vf (const). variability of KERNEL vs cell average:
# For x in cell k, U^m(x) - Vf = sum_j m_j (K(x,cell_j) - Qm[k,j]).
# Each term j!=k: monotone in x -> range = |T(A_k)-T(B_k)| (computed); j==k: self range.
# TOTAL width W_k = sum_j m_j range_{kj} (this is what we had: osc ~0.05).
# But for the ENERGY GAP we don't need widths: use DUAL feasible point!
# Dual of min{w'Qw: sum=1, o'w<=t}: max{lam*t... } — derive properly:
# L(w,lam,gam) = w'Qw - 2 lam (sum w -1) - 2 gam (o'w - t), gam>=0.
# min_w L = t... : w* = lam Q^{-1} 1 + gam Q^{-1} o; min value = 2 lam + 2 gam t - w*'Q w*.
# So lower bound = 2 lam + 2 gam t - [lam,gam]' S [lam,gam], S=[[1'Q^{-1}1, 1'Q^{-1}o],[o'Q^{-1}1, o'Q^{-1}o]].
# With EXACT S this is a rigorous 2x2 dual bound PROVIDED Qm is the true kernel matrix.
# Since Qm entries are elementary closed forms, S can be interval-certified with O(N^3) careful work,
# or bounded via rigorous linear solves. Pilot with floats:
Qinv1 = np.linalg.solve(Qm, ones)
Qinvo = np.linalg.solve(Qm, np.array([1.0 if ((A+B)/2 < P/9 or (A+B)/2 > 8*P/9) else 0.0 for (A, B) in cells]))
S11 = ones@Qinv1; S12 = ones@Qinvo; S22 = np.array([1.0 if ((A+B)/2 < P/9 or (A+B)/2 > 8*P/9) else 0.0 for (A, B) in cells])@Qinvo
print("S =", S11, S12, S22)
S = np.array([[S11, S12], [S12, S22]])
for a0 in [0.25, 0.255]:
    t = 2*a0
    # maximize 2 lam + 2 gam t - [lam,gam] S [lam,gam} over gam>=0
    # optimum: S [lam,gam] = [1, t]
    sol = np.linalg.solve(S, np.array([1.0, t]))
    lam, gam = sol
    val = 2*lam+2*gam*t - sol@S@sol
    print(f"a0={a0}: lam={lam:.6f} gam={gam:.6f} dualval={val:.8f} (primal f computed before)")
# Sensitivity: d(val)/dS entries; if S certified to +-1e-9 relative, dual value error?
print("cond(S)=", np.linalg.cond(S))
# Radius analysis: dualval - Vf vs V_up - Vf.
print("Vf=", Vf)
