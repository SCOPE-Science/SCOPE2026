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

# Reproducibility and proof boundaries

Execute `python3 verify.py` with Python 3 and the standard library. The standalone program iterates all permutations of sizes one through nine, counts disjoint cycles directly, detects upper records directly, forms exact rational expectations, and compares each local covariance and the aggregate covariance to the formulas. Independently, for all prefix injections through size six, it checks the conditional expected completed cycle count against the number of already closed cycles plus a harmonic-number term. The executed program reported `PASS 2472 exact assertions`.

Those checks confirm finite instances and the central conditional-count identity on small domains only. Universal exactness is established by the exposed-arrow completion bijection and the explicit prescribed-cycle count in `RESULT.md`. The asymptotic bounds are proved by isolating the three extremal record positions and bounding the remaining binomial-denominator sum. Independent third-party audit has not been performed.
