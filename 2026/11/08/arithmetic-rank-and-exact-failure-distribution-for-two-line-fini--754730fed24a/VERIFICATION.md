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

The accompanying `check_two_lines.py` directly constructs finite-field dot products, traces and self-restricted Fourier matrices for all unordered pairs of projective lines. It computes complex singular values independently of the cross-ratio formula and compares their numerical nullity with the predicted multiplicative-order nullity; separately it checks the closed count of full-rank pairs. The test fields are \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11},\mathbb F_{13},\mathbb F_{17},\mathbb F_4,\mathbb F_8,\mathbb F_{16},\mathbb F_9,\mathbb F_{25}\). All checks passed with a numerical small-singular-value threshold of \(10^{-7}\). The exact all-fields proof is supplied separately; finite computations are only corroboration. Reproduction uses Python 3 with NumPy; execute `python check_two_lines.py` in the extracted package directory. No independent audit has been performed.
