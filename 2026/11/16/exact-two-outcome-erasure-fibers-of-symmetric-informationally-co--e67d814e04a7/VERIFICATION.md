---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

The general proof uses only Hermitian projector identities and real rank arguments, so no numerical computation is required for its validity. The pivotal steps are (i) \(\operatorname{tr}(D_jP_k)=\delta_{jk}\), (ii) traceless differences yielding multiples of \(P_r-P_s\), (iii) the exhaustive two-coordinate involution classification, (iv) the rank-two obstruction for unknown-norm signals in \(d\ge4\), and (v) the qutrit counterexample from the eigenvalues \(4/3,0,-2/3\).

After installing the Python dependencies from `requirements.txt`, run `python CHECK.py`. The checker constructs the Hesse SIC in dimension three, tests all nine pairwise projector overlaps, computes the two-erasure retained output for an explicit reflected pair, checks the lost-probability gap and chordal distance, and checks the qutrit exceptional eigenvalues. The observed output was:

`CHECK_OK dimension=3 sic_gram=exact_to_roundoff retained_outcomes=7 exact_gap=verified chordal_relation=verified unnormalized_exception=verified`

All floating-point comparisons use absolute tolerance \(10^{-12}\) and are evidence only for the specified finite test, not a proof of an arbitrary-dimensional statement. The full theorem is conditional on SIC existence and concerns the original unconditioned effects \(E_j=P_j/d\), not a postselected or normalized-after-erasure measurement.
