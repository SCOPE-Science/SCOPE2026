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

## Reproduction

Run `python3 verify.py` in the directory containing this file, `RESULT.md`, and `verify.py`. Python 3 standard library only. The script performs rational matrix/eigenvector identities, independent heat-trace derivative comparisons, boundary-root and conductance-support checks, and finite-size consistency trials. The expected final output begins `PASS: 10812 finite checks`.

## What is and is not checked

The algebraic proof in `RESULT.md` is the primary evidence for universal correctness. The checker samples sizes and parameters and tests exact spectral identities at those sampled parameters; it does not enumerate an infinite family, exhaust all asymmetric conductance assignments, or establish publication priority. Strict convexity and symmetry in the proof are needed for the unrestricted minimizer statement. The independent audit status remains not performed.
