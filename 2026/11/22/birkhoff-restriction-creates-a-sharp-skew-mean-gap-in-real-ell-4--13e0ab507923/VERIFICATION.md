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

For t≠1 the generalized quadratic form for the scalar norm of M_t has a simple top eigenline with RQ≠0. Every nonzero real (R,Q) is attained by (a²−b²,2ab) by complex squaring; over the maximizing eigenline its preimages are two perpendicular input lines. Thus every nonzero coordinate row of an unrestricted maximizing pair is proportional to (a,b) or (b,−a), with ab(a²−b²)≠0. One line, including the case of only one nonzero row, is incompatible with both columns having norm one. Distinct lines and the two norm conditions give equal absolute scales, so the Birkhoff functional is a nonzero scalar multiple of ab(a²−b²). Compactness now gives strictness. The explicit balanced pair at t=1 attains 2^(3/4). For the local law, quartic expansion of the two norm arguments under x⊥_B y gives the displayed J and B. The uniform small-t expansion over both orientations confines all maximizing ratios to a neighborhood of u0 and the positive-linear orientation. At u0, q=3u0 and (1−u0)²=2u0, giving J=c and B=1/√3; differentiation gives f1″=−c(7+4√3)/4 and f2′=1+√3/2. The analytic implicit equation is ∂_u((F−1)/t)=0, which extends to t=0 and is nondegenerate there; concavity near u0 and exclusion outside the neighborhood yield one ratio and one ordered-pair orbit. The drift is −f2′/f1″ and substituting it changes the cubic coefficient by −(f2′)²/(2 f1″), giving (7√3−9)c/18. The unrestricted linear coefficient is √2/4 and c²=2/(3√3)<1/2. Neither uniqueness nor the cubic series is claimed at large t. The supplied checker was inspected and not executed; several coefficient checks use numerical tolerances, so the analytic calculation is decisive.

## originality

PASS

The two-weight unrestricted expression and its operator-norm derivation, and the leading reverse Birkhoff residual, are prior. The supported contribution is ruling out unrestricted equality under the Birkhoff constraint away from equal weights and establishing the optimized mean's local coefficients and moving orbit. The strongest matching Resultary proofs give either the unrestricted objective or the restricted difference quotient; neither gives the restricted sum maximum. The equality exclusion uses known generalized-eigenvalue data but additionally analyzes all norming rows under both unit constraints. The perturbation proof additionally optimizes a different Taylor series and is not a normalization of the earlier difference law.

## value

PASS

The real quartic plane is a natural smooth non-Hilbert test case for directional orthogonality constants. The theorem resolves exactly when the restriction changes the sharp arithmetic mean and quantifies both the optimized loss and how a maximizing pair moves. The leading common residual alone cannot reveal the linear versus quadratic optimizer motion of the sum and difference problems. This is a substantive comparison beyond evaluating a known formula at one weight, with no claimed closed form for the restricted mean at arbitrary weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
