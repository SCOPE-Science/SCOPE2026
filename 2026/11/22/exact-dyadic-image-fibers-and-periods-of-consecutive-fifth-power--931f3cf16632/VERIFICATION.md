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

# Verification record

The symbolic proof in `RESULT.md` establishes every infinite and exact claim. The factor \(4(t^2+ts+s^2)-(t+s)\) has two-adic valuation one when the two inputs are odd and congruent modulo four. The same holds for the normalized positive-valuation unit branches. These are the critical lifting steps; the surjectivity argument uses finite-ring bijections and two-adic compactness.

`check.py` uses exact Python integer arithmetic and no external packages. Run it with `python3 check.py`. A completed run reported **32,805 exact assertions passed** for every output residue at each level \(1\le k\le13\) and every full-period shift, with explicit exclusion of half-periods. The checker is a finite diagnostic, not an independent certification of the all-level argument.

No independent mathematical audit or external validation has been performed. The 2013 paper's full publisher text was not accessible in this literature comparison, so historical priority is qualified. No claim about odd primes or additional exponents is made.
