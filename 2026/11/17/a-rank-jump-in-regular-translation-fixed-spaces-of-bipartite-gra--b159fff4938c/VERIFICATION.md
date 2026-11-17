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

# Reproducible checks
The standard-library Python script `verify.py` enumerates undirected translation edge orbits as inverse-pairs of nonzero group elements and explicitly builds the corresponding Cayley graph for each selection. It tests bipartiteness by breadth-first two-coloring, without appealing to the claimed character criterion. It compares the result against the proposed \(2a+1\)-facet model for \(C_{2^a}\times C_2\) at \(a=1,2,3,4\), exhausting respectively 8, 32, 512 and 131072 selections.

A separate reduction of the facet nerve to binary matrices gives reduced mod-two Betti numbers \(\widetilde\beta_1=1,2,3,4\) and no others in these finite cases. For odd direct factors, two group examples are checked exhaustively and one is checked over all singletons/pairs plus 12000 deterministic pseudorandom masks; the code's seed and algorithm are fixed. The saved `verification_output.txt` contains the result of executing the exact included verifier. These checks corroborate the general proof and do not assert that finite enumeration proves an infinite theorem.

Run locally using `python verify.py`; no input data, remote service, or additional package is required. The `RESULT.md` proof establishes the unbounded claim by an explicit nerve argument, not by extrapolation. Independent mathematical audit has not occurred.
