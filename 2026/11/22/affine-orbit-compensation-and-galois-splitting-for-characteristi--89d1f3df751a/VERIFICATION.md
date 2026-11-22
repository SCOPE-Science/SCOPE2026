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

Run the embedded standalone checker with `python verify_anti_pre_lie.py` from the package directory. It requires only a standard Python interpreter and performs no downloads.

The original quadratic anti-pre-Lie identities are checked on all basis triples over \(\mathbb F_2\) and \(\mathbb F_3\). Every one of the \(512\) matrices over \(\mathbb F_2\) and the \(19683\) matrices over \(\mathbb F_3\) is tested directly against the *unreduced* Nijenhuis identity. In characteristic three, the verified rank counts are \(1,26,72,144\) and the complete automorphism-orbit rank counts are \(1,3,8,18\). The characteristic-three split-action derived-ideal-preserving stratum is enumerated independently and has \(21\) admissible centralizer-equation matrices and \(567\) corresponding operators. Six extension-degree arithmetic identities check the stated zeta logarithm.

The expected final success line is `ANTI_PRE_LIE_NIJENHUIS_VERIFIED`.

These are **finite** reproducibility checks, not a proof for every prime power or a certificate of the algebraic-geometric component classification. The general proof is given in `RESULT.md`. The full scalar-extension operator scheme may have non-ideal-preserving points; the zeta statement is confined to the derived-ideal-preserving subscheme. Independent audit has not been performed.
