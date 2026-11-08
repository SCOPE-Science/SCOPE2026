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

# Reproducibility and boundaries

The executable `verify.py` enumerates \((\alpha,B)\) directly from the defining star brackets. It computes ranks by finite-field Gaussian elimination, including a genuine four-element field implementation; compares exact rank multiplicities against the Gaussian-binomial expression; and separately forms the full alternating Kirillov matrix on the whole Lie algebra for all small cases. The independently evaluated calculations pass in six configurations. `verification_output.txt` records exact results. To reproduce, run `python3 verify.py` in the directory containing this verification document and compare the printed output with `verification_output.txt`.

The software does not establish the formula for infinitely many ranks or fields. The symbolic proof in `RESULT.md` supplies the general derivation. The full-matrix check for larger dimensions is sampled, whereas the closed rank-spectrum check exhausts all functional parameters that influence the bracket in each listed configuration. No independent scientific audit has yet been performed.
