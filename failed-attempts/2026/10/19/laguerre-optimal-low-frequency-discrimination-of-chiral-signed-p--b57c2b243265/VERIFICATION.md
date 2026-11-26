---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The contrast is 2/|W_n| times the determinant-weighted exponential sum. Summing the signs and expanding the resulting sine determinant, the first surviving choice of distinct odd powers is 1,3,...,2n-1; its two alternants give Δ_n(v)Δ_n(ω) and the Taylor factorials give the stated F_n. The next possible degree is n²+2, and a Taylor bound on the product of unit spheres is uniform. A reflecting wall in either variable annihilates the full contrast. In squared coordinates the log objective is strictly concave in the ordered simplex and tends to minus infinity at its boundary for n≥2. Euler's identity gives the multiplier n²/2; the critical equations yield the monic Laguerre ODE after z_i=n²a_i. The constant term of the monic Laguerre polynomial gives ∏z_i=n!, and evaluating zp_n'=np_n+n²p_(n−1) at its roots and iterating the three-term resultant gives discriminant ∏_{j=2}^n j^(2j−1). Uniformity permits taking the supremum before the limit. The n=1 formula is the ordinary two-point contrast. As an independent n=2 check, writing p=a_1a_2 gives Δ²=p(1−4p), maximal at p=1/8 with Δ²=1/16 and a_i=(2±√2)/4. The result is about the leading term, not finite-frequency maximizers.

## originality

FAIL

The exact assertion is covered by direct combination, not found here as a verbatim prior theorem. The two positive measures rewrite exactly as the published B_n sine determinant with a cardinality normalization. Its lowest Taylor alternant gives the coefficient by ordinary series multiplication. The remaining one-vector maximization is exactly the known Laguerre log-gas problem under x_i→x_i², and the two-vector problem is merely its product. The closed normalization follows by evaluating the standard Laguerre root product and discriminant. No separate extremal or Fourier theorem remains after these identifications.

## value

FAIL

Sensitivity of positive mirror-related orbit measures is a natural interpretation, and the exact normalization is correct. But this particular leading-order optimum adds no new extremal calculation beyond the published sine determinant, the published constrained Laguerre optimum and routine Laguerre identities. Taking two independent copies of the same optimizer and changing the measure normalization do not establish a distinct mathematical gap. No finite-frequency optimum or nontrivial restriction on the pair is proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
