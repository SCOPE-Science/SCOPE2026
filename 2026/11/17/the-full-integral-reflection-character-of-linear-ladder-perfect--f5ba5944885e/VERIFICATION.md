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

# Reproducibility
Run `python3 verify_ladder.py` with a standard Python 3 interpreter. The program needs no third-party modules. Compare its output with `verify_output.txt`.

The actual execution checked the complete perfect-matching face sets for \(2\le n\le12\), totaling 597,868 faces, and the signed reduced simplicial Lefschetz traces of four graph symmetries at each parameter (44 traces). It independently computed mod-two reduced homology using boundary-matrix ranks through \(n=8\). Output ends with `VERIFY_OK`. The code uses explicitly constructed faces and signed permutation traces rather than substituting the claimed character into its calculation.

The finite checks cannot certify statements for unbounded \(n\) or establish integral torsion-freeness by themselves. The proof uses an exact fold recurrence giving the integral homotopy type and a uniform signed-trace recurrence giving the reversal orientation. Neither an independent external audit nor a formal proof assistant check has been performed.
