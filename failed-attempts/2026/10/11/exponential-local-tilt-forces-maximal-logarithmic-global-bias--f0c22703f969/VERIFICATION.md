---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

As a formal deduction from the explicitly cited 2026 paper statements, the mathematics is sound. From e^{t(xi1-xi2)} with xi=k/2 one gets staircase pressure eta=t/2 (no missing factor). For eta_n->eta !=0, z_n=P_n'(eta_n), P_n'(0)=O(1), and c n <= P_n''(u) <= C n uniformly on the bounded segment, the mean value theorem gives sgn(t) z_n between positive linear multiples of n. With the source-attributed exact twist S_{nN0}=2z_n and |S_{k+1}-S_k|<=2, this extends to all k. The source-attributed A_N=S_(nu_N)/4, nu_N~log N, and B_N~sqrt(log N) establish the sign, order, and divergence. The bounds require t finite nonzero and bounded-type alpha; no statement is made for t=0. The named nonstandard source theorems themselves were not independently re-read because the full primary preprint was inaccessible; confidence is conditional on the stated attributions, and this is a recorded verification risk, not a fabricated proof of those lemmas.

## originality

FAIL

The new statement is an immediate quantitative corollary of the very published results the package cites. In the package’s own proof, Theorem 1.25 and Proposition 11.7 yield eta_n -> eta=t/2 != 0 and z_n=P_n'(eta_n). The cited Proposition 8.9 and curvature inputs yield P_n'(0)=O(1) and c n <= P_n''(u) <= C n on the fixed parameter segment. The mean value theorem therefore gives sgn(t) z_n = Theta(n), and published Theorem 4.5 converts that directly into S_{nN0}=2z_n. Bounded increments and published Theorems 1.9-1.10 immediately give the entire advertised statement. This is implication coverage by the combined published theorems, whether or not their authors printed the corollary verbatim. Source full-text access was blocked, so individual theorem hypotheses remain a recorded verification risk, not an invented independent full-text reading.

## value

FAIL

The local-to-global quantitative hierarchy is a natural question, but the package contributes no independent structural lemma, method, new invariant, classification, or limiting computation. Once the published genericity, pressure-curvature, height, and centering statements are assembled, the whole result is one routine mean value theorem and O(1)-block interpolation. It is suitable as a clearly attributed illustrative corollary, but does not meet the bar for a separate research finding: it changes neither the applicable class nor the underlying analytical conclusion beyond what the cited general estimates already entail. Failure is substantive and not based on small numerical scope, inaccessible sources, or absence of a downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
