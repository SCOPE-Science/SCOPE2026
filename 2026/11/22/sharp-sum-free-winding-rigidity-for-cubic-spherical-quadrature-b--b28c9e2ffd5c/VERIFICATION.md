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
# Reproducibility and limits

The standalone `CHECK.py` script uses only the standard Python 3 library. Execute `python3 CHECK.py` next to this file. The checker symbolically enumerates all complex monomials of total degree at most three, tests exact Fourier frequency zeros against the sphere's target low-degree moments, and compares that condition against the pairwise-distinct, repeated-sum-free absolute-winding criterion. It also checks the reflection-derived lower bounds over finite sum-free subsets.

The reported run completed with: `PASS: 39304 signed primitive winding vectors in d=3,4; all sum-free sets of size 1..5 in [1,16] checked; odd-frequency equality examples.` Finite tests are *not* evidence of a proof over every dimension and winding magnitude. The all-dimensional argument is in `RESULT.md` and should be checked directly for Fourier normalization, integer reflection pairing, and the strict degree-four moment difference. Independent audit has not been performed.
