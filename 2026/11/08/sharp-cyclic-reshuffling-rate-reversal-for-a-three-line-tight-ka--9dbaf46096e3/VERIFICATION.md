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

# Reproducible checks

Run `python verify.py` with Python 3 and SymPy (see `requirements.txt`). The stored stdout is in `verification_output.txt`.

The script rebuilds the normal vectors, row updates, six permutation sweeps, the uniform reshuffling second-moment matrix and the with-replacement factor. It checks exact factorization and the cyclic discriminant; exact rational isolation of the reshuffle optimum and inequalities supporting the all-horizon proof; and the defective cyclic Jordan identity. As additional finite checks, it averages first- and second-epoch matrices at four fixed rational parameters. The complete theorem for all relaxations and infinitely many epochs follows from the analytic proof in `RESULT.md`, not from finite sampling or test enumeration. No external audit or certification has been performed.
