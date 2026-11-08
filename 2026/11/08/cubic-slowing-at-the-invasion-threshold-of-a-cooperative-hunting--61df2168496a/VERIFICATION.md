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

# Verification information

Run `python3 verify.py` from this directory. The script needs only Python's standard library. It performs 60 exact-rational series-coefficient/invariant-graph assertions across 20 admissible parameter pairs, followed by three original-map numerical orbit checks for one rational parameter pair. The observed result of the bundled script is `VERIFY_OK 63 exact coefficient identities and orbit checks`.

The exact symbolic assumptions and proof of the infinite-time results are given in `RESULT.md`, including the negative cubic coefficient and one-dimensional reciprocal-power summations. The numerical tests are finite approximations, not global stability evidence or proof of the limits. Claims concern a local neighborhood of the predator-free state and do not include any independently validated audit.
