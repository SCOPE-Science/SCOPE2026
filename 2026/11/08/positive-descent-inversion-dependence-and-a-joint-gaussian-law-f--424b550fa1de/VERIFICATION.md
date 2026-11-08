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

# Reproduction and boundaries

Execute the two standalone programs with Python 3:

```bash
python3 check.py
python3 sample_check.py
```

`check.py` requires only the Python standard library. It enumerates all permutations for deck sizes 2 through 7, checks conditional uniform-prefix formulas for every legal prefix length, and independently enumerates all card-choice histories for deck sizes 2 through 5 and shuffle counts 1 through 4. It checks the corresponding joint statistics through exact rational distributions and validates the finite covariance decomposition. It also checks the limiting projected variance identity at rational parameter values. The recorded result is `PASS: 75033 exact finite assertions`.

`sample_check.py` uses a fixed pseudorandom seed and compares three empirical normalized second moments against the theorem at deck size 500, with 4,000 replicates and fixed normalized time 1. The recorded empirical variance/variance/covariance values were approximately `0.07707362, 0.02847305, 0.00875357`, versus theoretical limits `0.07697893, 0.02968375, 0.00894029`; all diagnostics passed the script's stated tolerance. This experiment is not an infinite-sample proof.

The analytical proof is in `RESULT.md`. Its non-finite steps are a standard one-dependent triangular-array central limit theorem, Hoeffding's first-order pair projection with a degenerate remainder, and the uniform occupancy central limit theorem. These are not formally certified or independently audited here. This package does not assert any bound on finite-sample normal approximation error.
