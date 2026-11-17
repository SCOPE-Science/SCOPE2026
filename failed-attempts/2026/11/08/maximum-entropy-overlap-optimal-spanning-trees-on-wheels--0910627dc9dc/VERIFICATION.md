---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Deleting hub row of wheel Laplacian yields Z_m(w)=det(wI+L(C_m)), so spoke marginal s_m(w)=w/m d(log Z)/dw; every rim edge has marginal 1-s. The positive spectral formula makes s_m strictly increasing from 1/m to 1 and gives a unique s=1/2 conductance. Poisson-kernel averaging yields the displayed root equation. Cauchy–Schwarz forces minimum overlap m/2, KL divergence proves unique maximum entropy among equal-marginal laws, and expansion at x=1/3 gives 3^m(4/3-w_m)->64/9. The exact uniform-law excess follows from s_m(1). Independent numerical roots m=3..6 matched s=1/2 and the polynomial.

## originality

FAIL

The published October 25, 2026 weighted-wheel cut/cycle projection theorem already proves a unique moving conductance threshold tau_m solving tau_m*g0(tau_m)=1/2, where g0 is exactly the diagonal Green function of wI+L(C_m). By matrix-tree differentiation, w*g0(w) is precisely a spoke-inclusion probability of the weighted spanning-tree law. Hence the previous tau_m equals the submitted w_m, and its explicit Green kernel gives the very same root equation, monotonicity and 4/3 limit; a one-term expansion yields 64/9. General minimum-overlap spanning-tree theory and standard KL selection then imply the entropy statement. The uniform-vs-calibrated excess is a straightforward marginal-square substitution.

## value

FAIL

The problem of fair wheel tree sampling is natural, but the supposedly new tuning parameter and exact unique calibration were previously characterized exactly in another mathematical guise. The entropy and uniform-overlap formulas follow mechanically from published graph-general overlap principles plus known wheel Green functions; no nontrivial independent mathematical result remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
