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

# Verification evidence

The symbolic proof is in `RESULT.md`. The independent finite computation in `check_split.py` enumerates every set partition for the documented bounded population range, evaluates the literal symmetric valuations, and checks the predicted welfare-product maximum, positive-maximum multiplicity, exact stable-partition count, and expected stable-partition structure. It uses only the Python standard library.

Run `python3 check_split.py` alongside `RESULT.md`. Success prints `ALL ENUMERATED INSTANCES PASS`.

Enumeration is not an all-populations proof. The crucial arguments beyond finite checks are (i) every individually rational block is a friendship clique, (ii) merging core-only blocks increases every involved utility, (iii) strict convexity forces the welfare-maximizing core distribution, and (iv) a Nash-stable partition cannot place cores in two different coalitions. No statement about independently audited validity or historical priority is made.
