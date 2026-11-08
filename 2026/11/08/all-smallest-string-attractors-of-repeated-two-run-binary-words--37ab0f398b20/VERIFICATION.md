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

Direct check: `python verify.py` was run against the bundled script without dependencies. Parameter cases 360; distinct factor-pattern instances 188975; matching optimal position pairs 18192. Exhaustive \(1\le a,b\le6\), \(2\le k\le6\) plus 180 seeded larger cases all passed. These checks do not constitute a proof for all parameters; the proof in RESULT.md does. Independent audit has not been performed.
