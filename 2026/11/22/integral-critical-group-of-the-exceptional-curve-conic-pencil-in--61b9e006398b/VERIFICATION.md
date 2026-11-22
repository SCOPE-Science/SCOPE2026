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

# Verification record

Reproduce with `python3 verify.py`. All matrix entries and transformations are exact integers. The script builds the 16 exceptional divisor classes, 10 conic divisor classes, 40 reducible fibers and the 26-vertex Laplacian, and checks row degrees and column degrees. It verifies a separate five-bit parity presentation, all entries of the Gram matrix, three Smith forms (including integral left and right transformation matrices), and three Bareiss determinants. Expected output: `DEL_PEZZO_CONIC_INCIDENCE_CRITICAL_GROUP_VERIFIED_OK`. Independently, a SymPy integer Smith calculation and determinant computation agreed for the last-vertex sink. These finite computations certify the supplied finite matrix claims; the geometric identification is justified separately in the proof using the complete classical blow-up class lists. No independent audit or machine formalization was carried out.
