---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: Orthogonal energy decomposition f_i=m+d(s/L_i-1/2)+g_i with Dirichlet g_i shows the parallel-edge Green diagonal Q_B=C+(1/L_i-1/T)s(L_i-s)+(s/L_i-1/2)^2/c; pinching d to zero gives rose Q_R without final term. The coefficient of s(L_i-s) in Q_B is ((T-L_i)(c-1/L_i)-1)/(T(1+L_i(c-1/L_i))), strictly positive for r≥3 via Cauchy–Schwarz, while for r=2 it vanishes. Hence maxima for r≥3 are longest-edge midpoints on both graphs, K=C+M(T-M)/(4T), and r=2 banana is everywhere norming while rose only loop midpoints, both K=T/12. Midpoint Green representers coincide because the extra d-mode vanishes. Independent exact rational substitution L=(1,2,3) gives K=11/24; source independent nodal Poisson checker uses exact SymPy solves for seven families (finite corroboration).

## originality

FAIL

FAIL: Two earlier full published theorems already determine both sharp constants and all maximizers for these exact metric graphs. The November 8 longest-parallel-path theorem gives exactly K_B=C+M(T-M)/(4T) and midpoint localization; the November 8 flower/rose theorem provides Q_R=C+(1/L_i-1/T)s(L_i-s) on a single hub (its proof without pendants) and K_R with the same formula. The general cactus Green formula is an additional encompassing reference for bouquet loops. Equating the already explicit constants gives pinching invariance immediately; the Green representers at midpoints coincide by deleting the prior parallel-potential d term. These straightforward implications cover the new central assertion despite different wording.

## value

FAIL

FAIL: Topological pinching invariance is an attractive interpretation of two sharp inequalities, but with both sides and their equality sets previously known, the current comparison is immediate algebra and supplies no substantially new exact invariant, obstruction or mathematically independent classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
