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

# Reproduction

Run `python3 verify_degree_induced.py` with Python 3 and no external packages. It emits the exact lines in `verification_output.txt`. The program builds the entire augmented simplicial chain complex for all parameters in the tested range; computes ranks over distinct prime fields; enumerates all facewise signed traces for the specified group actions; and reconstructs all displayed triangle-join fillers directly. The checks are exact integer/modular arithmetic, not heuristic floating-point approximations.

Independent of the all-parameter proof, the finite checks cover 240 field-rank comparisons at part sizes two through five and thresholds zero through four; 4,096 product-action signed reduced Lefschetz traces; 2,464 equal-part-exchange traces; and 100 explicit threshold-two cycle fillings. Expected comparisons are reconstructed from the claimed exterior-power characters and multiplicities. They cannot prove that the formula holds for arbitrarily large part sizes. The general claim is supported by the self-contained natural homology and homotopy arguments in `RESULT.md`.

Independent mathematical audit has not been performed.
