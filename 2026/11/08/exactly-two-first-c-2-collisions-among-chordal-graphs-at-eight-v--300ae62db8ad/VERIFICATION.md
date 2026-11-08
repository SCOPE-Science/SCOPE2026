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
Execute `python3 verify.py` with Python 3 and no third-party dependencies. The deterministic output is archived in `verification_output.txt` and ends `VERIFY_OK`. The checker implements two essential exact procedures: clique-extension generation plus graph-isomorphism backtracking, and globally matched color refinement. At order eight it verifies 1614 connected and 2119 total chordal graph types, partitioned into 2117 color-refinement classes, precisely two of size two. Both exceptional pairs are nonisomorphic and connected and match the four stated graph6 representations. The two equitable degree-quotients independently witness color-refinement equivalence of the explicit pairs.

The connected counts through eight match McKay's catalogue, and the total counts through eight match OEIS A048193. As a supplementary independent finite check, NetworkX's standard graph atlas filtered by `networkx.is_chordal` gives `1,2,4,10,27,94,393` for orders one through seven. The published counts and external atlas are scope checks; they do not establish the two exceptional-class counts, which are proved by the exhaustive verifier. The 18 rounds used for all graphs of order at most eight exceed the standard pairwise stabilization limit of at most 16 rounds. The theorem is a finite classification and does not extrapolate beyond eight vertices.
