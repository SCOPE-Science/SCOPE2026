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

# Reproducibility and scope

Run `python3 verify.py` with Python 3.9 or newer; no third-party packages or network calls are required. The program constructs all length-two insertion histories, forming an exact histogram by output word and positional embedding count. It also enumerates all hosts directly with an independent subsequence dynamic program in smaller parameter ranges. Each histogram is compared to the closed formulas for every locally distinct source word in the prescribed finite grid.

The same program checks the exact structural descriptions of all hosts of multiplicity three and four, and two outside-hypothesis boundary examples. Captured stdout is in `verify_output.txt`.

The finite checks cover \(1{,}226\) locally distinct words, \(513{,}126\) indexed insertion histories and \(484{,}024\) full-host dynamic-programming evaluations. The unrestricted integer parameters are justified by the disjoint candidate-position argument in `RESULT.md`, not by extrapolating these finite checks. Neither a proof of global entropy optimality nor independent validation is claimed.
