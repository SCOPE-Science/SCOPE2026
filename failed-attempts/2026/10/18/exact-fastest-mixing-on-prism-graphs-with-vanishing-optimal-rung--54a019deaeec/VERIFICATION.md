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

Averaging over cycle rotations/reflections and layer interchange preserves admissibility and cannot increase the norm off constants. For the invariant weights, the weighted Laplacian is a Kronecker sum, with eigenvalues a d_j and a d_j+2b where d_j=2−2cos(2πj/n). The least nonstationary Laplacian eigenvalue is min(aδ,2b), with zeros counted, and the largest is aΔ+2b. If t bounds the modulus and g=1−t, then a≥g/δ, b≥g/2, and aΔ+2b≤2−g. Consequently g≤2δ/(Δ+2δ). At equality both weight constraints are tight, which proves uniqueness in the invariant class. The proposed weights realize the bounds and are feasible: Δ+δ−4=δ>0 for even n, and equals 2(1−cos(π/n))(1+2cos(π/n))>0 for odd n, including n=3. Thus the attained norm is Δ/(Δ+2δ) for all n≥3. The stated asymptotic weights and modulus follow from δ=4π²/n²+O(n⁻⁴), Δ=4+O(n⁻²); the equal-edge benchmark has gap δ/4 for large n. No uniqueness outside the natural invariant class is needed for the proof.

## originality

FAIL

The exact prism claim is demonstrably covered by a distinct indexed product theorem. In Resultary 78a82f1ea5ed both factors qualify, and no extra hypothesis is required for the value, weights or invariant uniqueness. Its optimization domain matches exactly, and the specialization gives all three probabilities and the same SLEM for every n≥3. The indexed general record has a later path date than the frozen prism, so this is an equivalent-coverage finding, not a claim that the general result predates the prism mathematically or that its authorship or provenance is established. Older primary treatments inspected here do not themselves give the entire result.

## value

FAIL

A prism is a natural benchmark and the allocation is mathematically correct. As a separate research finding, however, the exact weights and value require only substituting two factors into the verified indexed coverage, and the vanishing-rung coefficient follows by a routine expansion. This provides a useful example, not an independent exact invariant or other substantive surviving contribution under the stated scientific-value criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
