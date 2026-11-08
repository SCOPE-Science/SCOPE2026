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

The claim uses deterministic threshold-two closure on finite connected simple graphs and exact uniformly selected seed sets. Run `python3 verify.py` with Python 3.10 or later; no third-party dependencies are used. The script enumerates all \(2^{\binom n2}\) labelled graph masks for every \(1\le n\le6\), checks connectedness, then enumerates every seed mask of each connected graph. It compares profiles only within identical sorted degree sequences and independently tests the two witness profiles using the static-fort criterion.

Verified results: connected labelled graph counts \((1,1,4,38,728,26704)\), zero profile-ranking reversals for orders at most five, exactly one reversing profile pair at order six, and witness vectors \((0,0,0,10,14,6,1)\) and \((0,0,0,12,13,6,1)\). The two profile classes have 180 and 90 labelled realizations; automorphism counts 4 and 8 prove these each consist of a single isomorphism orbit. The checker exits with `ALL_CHECKS_PASSED`.

The second method proves a seed set fails exactly when its complement contains a fort and computes the witness counts by this obstruction. The Bernoulli-seeding polynomial identity is proved by algebraic expansion in `RESULT.md`; sample exact-integer evaluations are additional checks, not an infinite proof. No empirical data, independent audit, or machine-formal proof is claimed. Historical priority remains subject to literature assessment.
