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

Run `python3 CHECK.py` using Python 3 and the standard library. The script enumerates \(\binom{11}{7}=330\) subsets and reduces them to 20 dihedral classes, proves each seven-node real moment matrix and its seven Cramer sign determinants are decisively separated from zero by a rational approximation margin, and verifies 33 admissible subsets in three 11-member classes. The terminal line is `CERTIFIED_11TH_ROOT_SEVEN_NODE_CLASSIFICATION_PASSED`.

The certificate uses Machin's exact arctangent identity, rational alternating-series truncations for \(\pi\), rational Taylor approximants for trigonometric entries, scaled integer matrices, and exact Bareiss elimination. Every normalized determinant differs from its certified approximation by less than \(10^{-7}\), while the exact computed approximation is separated from zero by more than \(10^{-3}\). Hence every determinant sign is rigorous.

The six-node impossibility follows from a mathematical argument independent of the checker. The complete classification does not extend by assertion to any other modulus, and the certificate is not an independent audit.
