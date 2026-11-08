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

# Reproducibility and bounds of verification

The accompanying `CHECK.py`, with `requirements.txt`, runs on Python 3 with SymPy and mpmath. It performs exact-symbolic checks of the original six affine branches, all four core interval images, the gap constants and total gap length. It also verifies finite Fibonacci multiplicities and the rational generating function algebraically, and compares the exact truncated tube formula against the analytical log-periodic profile at three high-precision sample phases. Successful execution prints `EXACT_LORENZ_BRANCHES_OK`, `EXACT_FIBONACCI_GAPS_OK`, and `TUBE_ASYMPTOTIC_SPOTCHECK_OK`.

The proof in RESULT.md supplies the quantifiers, full generation recurrence, convergence and uniform tube asymptotic. Finite testing alone does not prove that every geometric gap is represented, that no other zeros or poles occur, or that the limiting tube profile holds for every small radius. Those conclusions follow from the stated analytic arguments. Full independent mathematical or publication-priority audit has not been performed.
