---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Reconstructed source Proposition 4.22 inverse return shells x_n=exp(1-(n+1)^delta). Because right first branch sends normalized uniform Y seeds to uniform [0,1], P(tau>n)=exp(1-(n+1)^delta), hence tau has exact floor((1+E)^(1/delta)) law with E~Exp(1). Integerization costs less than one per observation; true mean is asymptotically e Gamma(q+1) for q=1/delta. Tilted Z^q weights have a truncated Gamma(q+1,1) mass law, which concentrates at q with O(sqrt q) spread. For c<1 maxima lie below bq, c<b<1 while that truncated expectation mass→0; for c>1 truncate at bq with 1<b<c and variance ≤(bq)^q/(e^(cq)mu_q)→0, missing expectation→0. At c=1 cutoff q±q^(1/4) leaves half tilted mass below the cutoff, negligible middle mass, concentrated lower sum, and vanishing probability of any upper extreme. This proves deterministic critical 1/2 without assuming finite tests imply the triangular-array theorem. Independent Gamma CDF check at q=100,400,1600 gives at q .47344,.48671,.49335.

## originality

PASS

Bounded best-of-knowledge originality of the exact final claim, not of its credited general framework or existing endpoint computations. Full primary text was read where available; sources inaccessible in full are clearly identified and retained as priority risks.

## value

PASS

A precise, natural sample-complexity threshold for estimation of a finite but astronomically rare-event-dominated first-return mean. The one-half critical regime is a non-obvious quantitative obstruction to using independent orbit restarts, distinct from the cited orbitwise Hausdorff spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
