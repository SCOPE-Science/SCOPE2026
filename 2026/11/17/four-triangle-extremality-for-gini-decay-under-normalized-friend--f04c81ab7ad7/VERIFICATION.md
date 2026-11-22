---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The exact generator decomposes into complementary C (constants), P (peripheral pair means centered across pairs), and R, with Q eigenvalues 0,-1/2,-3/2. Thus modulo constants H=bI+(a-b)P with a=e^{-t/2}, b=e^{-3t/2}. Layer-cake decomposition of any signal into nested indicator cuts reduces the projection norm to cuts. Randomly replacing split pairs by full/empty pairs preserves expected cross-pair and hub variation and deletes within-pair variation, so only whole-pair indicators need testing. For r whole pairs their Gini ratio is 2h(m+1)/(m(2h+1)), h=m-r, maximized by r=1, giving c_m=2(m²-1)/(m(2m-1)). The one-full-pair witness aligns signs in the triangle inequality, giving equality for all t. d_m=c_m-1=(m-2)/(m(2m-1)) has its unique maximum 1/14 at m=4; its bound proves strict contraction. Independently enumerated ALL binary cuts for m=1..6 at t=.7: norms match formula to <4e-16. Inspected source verify.py rational spectral and orbit checker. The symbolic cut reduction proves all m and real t.

## originality

PASS

A closely related published RESULT.md computes the same normalized semigroup on the same family but in EDGE-SUM variation J and finds amplification for m≥5, rather than Gini. This is real partial overlap in dynamics and witness; not covering because variation functionals differ and the Gini sharp constant/always-contracting conclusion cannot follow directly from an edge-sum bound. Estrada studies graph spectra and clustering, and Sandryhaila–Moura adjacency-shift graph variation.

## value

PASS

Gini all-pairs variation is a natural global dispersion statistic distinct from graph-edge total variation. Exact contraction for every friendship-graph size despite slow spectral decay, with the nonmonotone sharp four-triangle extremal size, is a motivated exact operator-norm fact useful for comparing dissipation geometries on hub graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
