---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independently checked every 6- and 7-subset of the 27 words. Each descendant is represented by the three coordinate symbol sets; equality of these nonempty Cartesian products is exactly equality of the three projections. The check compares the signatures of all nonempty coalitions of size at most 3. There were 135 valid 6-subsets and no valid 7-subsets, which excludes all larger codes by heredity. Direct application of the 1296 distinct isometries to the stated representatives partitions the census into orbits of 27 and 108. Orbit–stabilizer gives 48 and 12, and direct coordinate and pair-projection counting gives exactly the stated profiles. The independently recovered census hash matches the frozen one.

## originality

FAIL

A distinct indexed Resultary result, catalogued October 4 UTC, already states the same maximum, count, two orbits under the identical action, stabilizers and representatives. The projection profiles are not stated there verbatim but are mechanically implied by these representatives and the complete orbit statement. This is demonstrable equivalent coverage, not a judgment about authorship or provenance based on dates alone.

## value

FAIL

The ternary boundary is well motivated and a first complete classification would be useful. Here the main invariant and full equality cases are already covered. The added projection counts are immediate from the two known representatives; the independent recheck of the known census does not supply a new structural result or exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
