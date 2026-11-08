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

# Verification

Run `python verify.py` using Python 3 and its standard library. The checker separately constructs original partial maps, checks the full simplex-preimage definition of strict continuity, tests composition idempotence, enumerates oriented matchings, constructs the oriented-edge conflict graph and verifies its independent-set polynomial and absence of induced claws in representative finite cases. The recorded output is in `verification_output.txt`.

The tests comprise eight exhaustive partial-map configurations, 22 oriented-matching configurations, 14 complete conflict-graph polynomial configurations, and 44 claw-free tests. The maximum path/cycle length for matching enumeration is 12; the claw checks extend through 23 vertices. These are finite checks only. The universal formulas are proved in `RESULT.md` by symbolic counting and an established real-rootedness theorem. No external independent audit was performed.
