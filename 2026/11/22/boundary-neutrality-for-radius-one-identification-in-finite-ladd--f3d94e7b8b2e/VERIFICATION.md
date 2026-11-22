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

## Exact computational checks

- `python3 verify_transfer.py` generates 256 four-column states, evaluates 737 allowed interior transitions, and recomputes the exact integer cost vectors from length four through length twenty. The complete componentwise identity is checked directly, including the explicit base-vector formula. This check establishes periodicity for all lengths only when combined with the min-plus recurrence proof in `RESULT.md`.
- `certificate.json` contains the 256-entry vectors at lengths six and thirteen, the fixed terminal mask and tested optimum lengths. The verifier recomputes all arrays from first principles rather than trusting stored data.
- `python3 verify_direct.py` enumerates every possible selected sensor set for widths two through nine and independently checks every closed-neighborhood signature. It verifies claimed minimum sizes and counts of minimum codebooks at those widths. This is a finite cross-check, not the all-length argument.
- `python3 construct_witnesses.py` creates and validates an optimum sensor pattern for every width two through thirteen. The construction is separate from the finite certificate and supplies explicit upper-bound witnesses at the base lengths.

## Unverified limits

No independent mathematical audit has been performed. The all-length conclusion rests on the exact local equivalence, the 256-component min-plus identity, and the translation-invariant recurrence proof; enumeration at a finite set of lengths alone would not establish the theorem. Priority versus unindexed historical computations is not independently certified.
