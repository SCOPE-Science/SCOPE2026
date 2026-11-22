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

The theorem is proved constructively in `RESULT.md`. For the interval gap maps, the two-ended branch has derivative at least \(3/4\), the one-ended branches at least \(1/2\), and the coordinate displacement vanishes at gap endpoints. These facts yield a continuous invertible map on an arbitrary closed set's complementary gaps. The graph proof uses topological essential edges, not a chosen refinement, and verifies both measure-null and meagre exceptional sets and minimality at each target point.

Run `python3 verify.py` using the packaged standard-library source. The accompanying `verification_output.txt` records the observed output. The checker computes polynomial identities and finite examples using exact rational arithmetic. It is not an exhaustive certificate of an assertion over arbitrary closed sets, finite graphs of unbounded size, or the literature. There is no independent mathematical audit.
