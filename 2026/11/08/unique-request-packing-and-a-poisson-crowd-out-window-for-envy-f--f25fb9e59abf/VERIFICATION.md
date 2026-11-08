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

# Reproduction of finite checks

Run `python3 verification/checker.py` in the extracted package directory. The checker uses Python 3's standard library only. It computes the welfare optimum in two independent ways: exhaustive assignment of every good to an agent followed by literal pairwise envy-freeness tests, and exact set packing of uniquely occurring demand sets. It exhausts every profile for the parameter triples \((m,r,n)=(2,2,2),(2,2,3),(3,2,3),(3,2,4),(4,2,4),(4,2,5),(4,3,4),(4,3,5)\), and samples additional specified profiles using a fixed pseudorandom seed. The total is 10,862 profiles.

For six small pairs of values of \((M,n)\), it independently enumerates every sequence of demand-type draws and checks the inclusion-exclusion formula for zero singleton types and the first two factorial-moment identities against exact rational arithmetic. Expected final output: `PASS 10862 finite demand profiles and six exact occupancy cases`.

The deterministic packing proof, complexity reduction, Poisson method-of-moments argument, and intersecting-pair bound are contained in `RESULT.md` and do not rely on the finite checker. The finite tests do not establish any infinite limit or stand in for a proof of NP-completeness. No independent external scientific assessment has been performed.
