---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Conjugating the metric equation by V gives [Λ,V†ηV]=0; the simple real spectrum forces a positive diagonal D and every such D works. For B=VD⁻¹ᐟ², η⁻¹=BB† has the same eigenvalues as B†B, and inversion does not change the condition number. An optimum exists in all dimensions: rescale S=D⁻¹ᐟ² so min s_i=1; because G has unit diagonal, κ₂(SGS)≥(max s_i)², making any nonempty bounded sublevel set compact. For a pair, its η-cross term vanishes. After rephasing, the equal squared η-norms of the sum and difference bound 2λ_min(η)(1+c) from above and 2λ_max(η)(1−c) from below, giving the claimed obstruction. At fixed determinant in 2D the scaled Gram trace is minimized uniquely by equal diagonal entries, so D is scalar up to common scale, also when c=0. Its condition number is (1+c)/(1−c), giving the half-angle formula and asymptotic. Sharpness does not assert attainment for an arbitrary higher-dimensional basis; the two-dimensional extremizer can be embedded in an orthogonal direct sum. For n=1 there is no pair bound to apply. The inspected artifacts/verify.py is a bounded real-matrix sanity check and was not executed; the complex and all-dimension claims follow analytically.

## originality

FAIL

The two-level theorem, including optimum value and uniqueness of the ray, follows from the already indexed Schatten-infinity minimization after minimizing over metric scale. The pairwise obstruction is exactly the classical Wielandt inequality for the inverse square root of the metric acting on orthogonal lines. The diagonal-Gram step expresses the standard metric family in the standard one-sided column-scaling objective; it introduces no additional optimizer or estimate.

## value

FAIL

Optimizing metric conditioning is a meaningful problem, but this record stops at transferring an existing angle inequality and an equivalent known two-level optimization, plus a direct Gram reformulation in higher dimension. As a distinct mathematical finding it supplies neither a new mechanism controlling conditioning nor a new higher-dimensional solution or estimate. It is useful exposition, not a new conditioning theorem under the stated value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
