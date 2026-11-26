---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Stable convolution over the deterministic intervals gives the geometric weights and an independent uniform phase. At fixed phase, distinct coordinates have zero covariance. In the mixed fourth moment, products of squared components from different draws give d⁻², and terms in a single draw give 1/[d(d+2)]; terms with off-diagonal cross contractions vanish. The resulting phase mixture has covariance (v/a)^4 d⁻² times Var(S)−2 E(P)/(d+2). Direct integration of the squared- and fourth-weight sums confirms the closed formulas. For uniform k=u/θ, S=θ/2+θ²(k²−k)+O(θ³) uniformly, giving Var(S)=θ⁴/180+O(θ⁵); P=θ³/4+O(θ⁴), which dominates the fast-period sign for fixed d. At the slow end the bracket tends to −2/(d+2). Independent rational enclosure of the d=41 bracket at θ=3 gives the exact claimed positive bounds and the rational signs at θ=1 and 10. Since E(P)>0, the bracket is increasing in d at each fixed θ. The bracket is real analytic on θ>0 and not identically zero, so the opposite signs bracketing θ=3 guarantee distinct sign-changing zeros. The sufficient dimension is not a minimal-dimension theorem, and no uniqueness of either crossing is proved.

## originality

PASS

The conditional sphere moment identity and stable harmonic weight representation are general tools. The distinct claim supported here is the explicit stationary deterministic-clock phase mixture and its two opposite sign reversals with a certified sufficient dimension. The strongest located mixed-coordinate result assumes a Poisson clock and gives one transition. The inspected nonexponential and finite-tumble papers do not supply the periodic-clock cross-energy result. The bounded comparison leaves identifiable access and unindexed-theory risks.

## value

PASS

The result isolates a competition between the positive variance of the shared phase-dependent scale and the negative spherical angular constraint, invisible in ordinary coordinate covariance. It gives a rigorous reentrant benchmark rather than extending a Poisson sign diagram by matching mean waiting times. The exact witness and contrasting end regimes are useful without a claim to the smallest possible dimension or a full arbitrary-renewal phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
