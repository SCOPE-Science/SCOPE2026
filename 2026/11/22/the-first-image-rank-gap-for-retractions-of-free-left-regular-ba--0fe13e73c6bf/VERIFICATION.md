---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For the unital free left-regular band the injective words, including the empty word, are the normal forms. Substitution of arbitrary generator images respects first-occurrence reduction: a repeat of a generator cannot introduce any letter not already introduced by its first image. Thus the generator-image tuples parametrize all and only the unital endomorphisms. Independent bounded Python enumeration evaluated the entire map for each of the 2, 25, and 4096 tuples, tested its composition square on every word, and counted distinct outputs including the unit. The full three histograms match the frozen polynomials. The totals are 2, 17, and 535; the first two supports are intervals, and the third omits 11, 13, 14, and 15, with six maps of image size 12. Replay: python3 /workspace/branches/1e44eec6-9e30-47c8-8300-25f862a6659d/reproduce_census.py; captured output in the same directory, replay.txt. This verifies only the stated finite unital census.

## originality

PASS

Best-of-knowledge pass for the exact census and resulting first gap, not for the injective-word model, substitution, or the enumeration method. The exact local index hit points back to the frozen result itself. No distinct matching census or dominating rank classification was established by the bounded comparisons.

## value

PASS

Whether image sizes interpolate between the trivial and full retract is a natural structural question, and the census goes beyond exhibiting isolated examples. The first gap rules out interpolation at the smallest failing number of generators; it identifies both an interior forbidden size and a sharp proper-image maximum of 12 versus the full size 16. These exact obstructions and counts are useful small-rank constraints on proposed structural descriptions. No general-rank claim is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
