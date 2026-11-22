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

# Verification
Run `python3 transvection_braid_check.py` in the directory containing this file and inspect `transvection_braid_check_output.txt`. No packages beyond the Python standard library are needed. The checker explicitly enumerates primitive outer-product transvections, multiplies matrices in each of ten actual finite commutative rings, and checks all ordered pairs for the braid identity. It confirms the exact predicted orbit-type counts for each instance. The three distinct order-eight local rings with residue field size two all produce the same predicted total of 432 pairs in dimension two. The dual-number computation in dimension three confirms the nonprincipal-independent formula at a larger matrix size.

The abstract proof in `RESULT.md` separately establishes the exhaustive local dichotomy, simultaneous normal forms, stabilizer counts, and residue-map fibers for all finite commutative local rings and all dimensions at least two. Exhaustive finite verification is not presented as a proof of that infinite statement. Historical originality is subject to the explicit priority risks in `REVIEW.md`; no independent external audit was performed.
