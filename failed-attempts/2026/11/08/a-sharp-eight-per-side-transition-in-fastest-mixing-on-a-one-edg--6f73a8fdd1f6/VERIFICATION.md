---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Reconstructed all 2n eigenvalues from the ordinary within-class, exchange-even and odd quotient blocks, and the convex objective max{|1-nx|,|T|,F(x,t)}. At n<=7, the odd block lower bound 1/sqrt(n) is attained at x=1/n,t=0 and other modes lie below it. At n>=8, explicit candidate x=2/[2(n-1)+sqrt(n²-8n+8)] has t=0, T=(n-2)/Z and odd eigenvalues ±T; the displayed convex subgradient cancellation gives a global lower bound for all invariant kernels, and symmetrization applies globally. Independent full-matrix eigenvalue comparisons at n=3,4,7,8,9,20,60 confirmed formulas; they are corroboration, not an infinite proof.

## originality

FAIL

The exact full mathematical theorem was publicly established on October 25, 2026. Its domain G_n=K_{n,n} with one missing edge, symmetric nonnegative row-stochastic matrices with holding, n>=3, SLEM objective, both phase branches, analytic radical, globally optimal two-orbit weights and n=8 transition are identical. Source text was read in full rather than inferred from a title.

## value

FAIL

Although the graph and exact optimization problem are naturally motivated, the submitted piecewise SLEM threshold and optimal chain weights are already explicitly published in an exact theorem. Repeating its proof or computations has no distinct new scientific invariant, structural boundary, or result to evaluate; novelty and independent value therefore fail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
