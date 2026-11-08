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

# Verification of the time-conscious hierarchy theorem

Run `python3 verify.py` after extracting this record. The supplied checker constructs weighted-interval max-heaps and difference-array messages, compares the exact optimum with independent exhaustive enumeration on 5,750 reproducible finite randomly generated trees (two to six voters, up to four time instants), checks every returned schedule, and tests a four-voter instance with individual paths but no confluent solution.

All inputs in those experiments have integer scores and valid trust horizons satisfying the stated bounds. The proof in RESULT.md covers every finite tree with explicitly listed consecutive availability times; no finite battery alone certifies the universal quantifiers.
