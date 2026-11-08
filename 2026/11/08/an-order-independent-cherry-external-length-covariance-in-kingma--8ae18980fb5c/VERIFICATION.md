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

# Reproducible mathematical checks

Run `python3 verify_kingman.py` using Python 3 standard-library modules `fractions`, `itertools`, and `math`.

The script implements two structurally different computations: (1) exact forward dynamic programming for the probability and accumulated expected external length of states indexed by singleton-lineage and accumulated-cherry counts, for every sample size from 2 through 30; (2) literal enumeration of all ordered merger histories for sample sizes 4 through 8, independently evaluating the cherry count and external-length reward. It verifies the \(-2/9\) covariance for every tested sample size at least four and the entire stagewise singleton covariance profile in exhaustive cases. The eight-leaf enumeration consists of 1,587,600 histories; every transition probability is exactly \(1/\binom{k}{2}\), so equal weighting of complete histories is exact. It also checks \(\mathbb E C_n=n/3\) for \(n\ge3\) and \(\mathbb E E_n=2\).

These finite computations test normalization, exceptional orders, index ranges, and the algebra. They do not prove the statements for all sample sizes. The proof in RESULT.md supplies that step through exact factorial moments, past/future cherry recurrences, and an exact finite sum. The historical novelty assessment is literature-based and remains subject to independent review.
