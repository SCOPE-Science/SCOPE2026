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

# Verification procedures and limits

The analytic proof in RESULT.md gives exact moment identities and complete reconstruction. To replay the computational checks, place `verify.py` beside this file and run `python3 verify.py`; no third-party Python dependencies are required. The code performs 1,200 exact rational inverse checks, independently integrates nonzero-cross-term polynomial moments in four parameter cases, checks the explicit two-moment collision, simulates 600,000 random point-pair differences, and checks a separate convex-order consequence at 35,000 absolute difference pairs. A successful execution prints a `VERIFY_OK` marker. Its random seed is fixed for reproducibility.

The sample comparisons are **not** proofs for arbitrary real side lengths and angles. The universal conclusions rely on direct finite polynomial algebra and root inversion in RESULT.md. Numerical instability of estimated moments, statistical identifiability at finite sample size, and priority of earlier literature are not certified by these calculations.
