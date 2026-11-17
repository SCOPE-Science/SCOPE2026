---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For book graph K_{1,1,q}, polar dual lattice potentials modulo constants obey graph-edge |f(u)−f(v)|≤t. Fixing a hub at 0 and summing the other hub s∈[−t,t] gives exactly L_q(t)=(2t+1)^q+2∑_{s=1}^{t}(2t+1−s)^q; q independent leaves each have 2t+1−|s| choices. Bernoulli polynomial differentiation and triangular conversion to basis t^j(t+1)^(q+1−j) derive a1,a2,a3; exact rational interpolation checks full magic vectors q=1..6 and negative witnesses q=7..16. For q≥17, the four residue classes modulo 4 each have a negative a1, a2 or a3, propagated using Euler |B_{m+4}|/|B_m|>2 and explicit base Bernoulli values. The analytic argument covers the infinite tail; finite witnesses alone do not. Independent arithmetic reproduced q=6 positivity and q=7 a4=−5/4 and q=16 a8=−5493182/51.

## originality

PASS

Book graph K_{1,1,q}=K_2 join an independent q-set is one of the structurally distinguished Minkowski-decomposable graph families in Higashitani–Mori, but that structural theorem does not give its polar Ehrhart magic-coefficient signs. Konoike studies other classes and finite complete-bipartite tables, while Ohsugi–Tsuchiya positivity has restrictive simplicial/smooth hypotheses and cycle examples. Published sharp K_{2,q} and K_{3,q} polar thresholds are different graph families and different lattice-potential counts; the coincident K_{3,q} threshold 6 does not imply the book-graph cutoff. Searches found no covering book-graph classification, with residual historical-table risk.

## value

PASS

The book family is singled out by a structural graph-polytope classification; an exact natural dual Ehrhart invariant answers whether all magic coefficients stay positive as its leaf size grows. The sharp finite-to-infinite q=6/7 transition, with a rigorous four-residue Bernoulli no-return proof, supplies a reusable structural obstruction rather than an arbitrary isolated example or a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
