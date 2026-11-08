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

Run the included dependency-free `dp4_verify.py` using Python 3. It enumerates all 1920 signed permutations with even sign product; computes every action on the 16 even sign vectors, 40 unordered Hamming-distance-four pairs and 80 directed flags; confirms the classical blow-up incidence rules; checks the 18 type frequencies, all first-extension polynomials, all symbolic extension-count profiles through degree twelve, and the F9 general-position example, with a monotonicity certificate that all eighteen first-extension polynomials stay positive for q at least six. The saved output includes the complete 18-entry table of curve/node/branch cycle lengths and ends in `ALL_CHECKS_PASSED`.

The exact group enumeration verifies a finite universal Weyl-group classification. The validity for all finite fields and all extension degrees is proved by the geometric normalization and Picard-trace identities in the result; a finite sample of field sizes would not suffice. Some formal Frobenius types need not occur over the smallest fields. Historical priority cannot be proved by searching, and independent external mathematical validation has not been performed.
