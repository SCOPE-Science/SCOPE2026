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

# Reproduction

Run `python3 checker.py` with standard Python 3 (no external library). The code enumerates all relations on the rooted star with up to three leaves, checks the two confluence quantifiers directly, compares both possibility and both necessity operators on every persistent proposition, computes canonical isomorphism orbit representatives, and checks each permutation's fixed count against the cycle-index formula. It also computes the partition sum in exact rational arithmetic for the first eight leaf sizes.

Expected final output is `ROOTED_STAR_CONFLUENCE_ORBIT_OK`. For one, two and three leaves the checked pairs (labelled relations, isomorphism classes) are \((7,7)\), \((89,50)\) and \((5119,940)\). Tests on one leaf are a boundary check; the theorem is stated for \(m\ge2\). The arbitrary-size result is proved mathematically using confluence case analysis and Burnside's lemma; finite exhaustion is not a substitute for this proof. No independent audit has been conducted.
