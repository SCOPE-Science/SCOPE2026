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

# Reproducible verification and limitations

Run `python CHECK.py` with Python 3, requiring only the standard library. The script enumerates the entire set of admissible maps for each \(1\le k\le m\le n\le6\) (56 parameter triples), using canonical nested labeled sets, and derives cycles directly from the maps. It compares every pair of complete directed-cycle partitions, the two-region stable-rank counts, exact totals, both probability identities, and the \((n,m,k)=(5,3,2)\) example to the mathematical formulas.

Successful execution prints `RESTRICTED_RANGE_CYCLE_CENSUS_VERIFIED 56`.

The infinite theorem relies on the explicit directed-forest proof in `RESULT.md`. Finite exhaustive enumeration does not establish any bound outside the tested sizes. The proof does not classify transient tail lengths, complete functional-graph isomorphism types, or abstract semigroup isomorphism by dynamic signatures. A literature novelty check is not an independent publication-priority certification.
