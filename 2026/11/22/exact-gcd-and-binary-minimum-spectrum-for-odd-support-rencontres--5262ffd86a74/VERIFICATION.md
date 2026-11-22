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

The finite diagnostic program `check.py` calculates all odd moved-support rencontres entries and their actual row gcds for every \(4\le n\le240\). It also checks every exact binary-valuation and minimizing-column assertion on those rows, and an independent modular divisibility test for all odd primes at most 151 in rows up to 151.

Executed command: `python3 check.py`.

Observed output: `PASS: 17648 exact assertions; all rows n=4..240 and prime-support checks n<=151.`

Infinite correctness is justified by the algebraic and Lucas/Kummer proof in `RESULT.md`, not extrapolation from these calculations. Historical priority may be affected by an unlocated equivalent; no independent mathematical audit has been performed.
