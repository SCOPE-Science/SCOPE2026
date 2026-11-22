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

# Reproducibility of the fixed-composition law

Using Python 3 with no external packages, run `python verify/bruteforce.py` and `python verify/path_dp.py` after extracting this package. Both programs are self-contained, deterministic and terminate with a `PASS` message and exit code zero.

The direct enumeration examines every binary word of each length from one through eighteen (524,286 words total) and compares its Abelian-border property with the exact weight polynomial. The second program calculates the nonreturning paired walk through a separate state-space dynamic program for forty inward-pair lengths, and compares with the binomial formula, normalization, symmetry, variance and log-concavity predictions.

The verified computations do not establish the infinite result on their own. The actual all-length proof is the weight-preserving reflection and binomial-factor derivation in `RESULT.md`; its limit statement additionally uses Stirling's formula. No external audit has been performed.
