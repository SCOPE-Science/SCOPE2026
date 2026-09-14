"""Knapp-scaling margin check for the BR sparse vertex P2 (d=2).

Tests whether elementary Knapp-box scaling can separate the vertex
q_opt = 4/(1+6λ) from the interior q > q_opt for p_λ = 4/(3+2λ).

The Knapp necessary condition for (p,q)-sparse domination in d=2 is
    1 - 1/q <= 3*(1 - 1/p)   [(d+1)/(d-1) = 3],
with margin M(p,q) = 3*(1-1/p) - (1-1/q).  M > 0 means the Knapp ratio
grows like a positive power of 2^j (rules out larger q region boundary);
M = 0 means borderline: Knapp scaling is O(1) and inconclusive, so any
vertex disproof needs log-scale/multi-scale analysis beyond Knapp.
Also verifies q_opt = 2  <=>  λ = 1/6 (the solved Stein-Tomas case).
"""
import json

def margin(p, q):
    return 3.0 * (1.0 - 1.0 / p) - (1.0 - 1.0 / q)

lambdas = [0.02, 0.05, 0.10, 1.0 / 6.0, 0.25, 0.40, 0.49]
rows = []
for lam in lambdas:
    p = 4.0 / (3.0 + 2.0 * lam)
    qopt = 4.0 / (1.0 + 6.0 * lam)
    m_vertex = margin(p, qopt)
    m_above = margin(p, 1.5 * qopt)   # interior point q > q_opt
    m_below = margin(p, 0.9 * qopt)   # outside region (should be < 0)
    homog = 1.0 / p + 1.0 / qopt      # == 1 + 2λ at vertex
    rows.append({
        "lambda": lam, "p": p, "q_opt": qopt,
        "M_vertex": m_vertex, "M_above": m_above, "M_below": m_below,
        "homog_1/p+1/q": homog, "1+2λ": 1.0 + 2.0 * lam,
    })
    print(f"λ={lam:.4f} p={p:.4f} q_opt={qopt:.4f} "
          f"M(vertex)={m_vertex:+.2e} M(1.5q)={m_above:+.4f} "
          f"M(0.9q)={m_below:+.4f} 1/p+1/q={homog:.4f} vs 1+2λ={1+2*lam:.4f}")

gap = abs((4.0 / (1.0 + 6.0 * (1.0 / 6.0))) - 2.0)
print(f"\nq_opt(λ=1/6) - 2 = {gap:.2e}  (L^2/Stein-Tomas case)")

ok_vertex = all(abs(r["M_vertex"]) < 1e-12 for r in rows)
ok_above = all(r["M_above"] > 0 for r in rows)
ok_homog = all(abs(r["homog_1/p+1/q"] - r["1+2λ"]) < 1e-12 for r in rows)
print(f"\nvertex margin == 0 (borderline, Knapp inconclusive): {ok_vertex}")
print(f"interior margin > 0: {ok_above}")
print(f"vertex homogeneity 1/p+1/q = 1+2λ: {ok_homog}")

with open("knapp_scaling.json", "w") as f:
    json.dump(rows, f, indent=2)
print("\nRESULT:", "BORDERLINE-CONFIRMED" if (ok_vertex and ok_above and ok_homog) else "UNEXPECTED")
