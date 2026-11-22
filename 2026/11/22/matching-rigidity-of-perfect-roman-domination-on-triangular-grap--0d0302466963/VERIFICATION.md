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

The displayed theorem is proved algebraically for all integers \(n\ge3\). The following bounded, independent computational checks were actually performed with the scripts included here:

1. `g++ -std=c++17 -O3 support_enum.cpp -o support_enum && ./support_enum` exhausts all label-two supports for \(3\le n\le7\). It reproduces the six fields of `support_enum_output.txt` for each row and shows that all optimal supports have root degree at most one.
2. `g++ -std=c++17 -O3 ternary_enum.cpp -o ternary_enum && ./ternary_enum` enumerates all \(3^{\binom n2}\) labelings for \(3\le n\le6\). It verifies the original neighbor-of-label-two condition without using the root-degree formula. It produces `ternary_enum_output.txt`.
3. `python3 formula_check.py` checks every matching-defined optimizer and its actual label condition, weight, and labelled matching count for \(3\le n\le10\), reproducing `formula_check_output.txt`.

The software's finite ranges do not establish the infinite claim; that claim follows from the degree inequality and strict quadratic minimization in `RESULT.md`. The published edge variant requiring the entire zero-neighborhood label sum to equal two is a different model. No external independent audit has been carried out.
