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

# Verification instructions

The package contains two Python 3 standard-library programs. Run `python3 verify_exhaustive.py` and `python3 verify_independent.py` from the directory containing them. Both must terminate successfully with their `VERIFIED` summaries; a false claim triggers an assertion rather than a partial success message.

`verify_exhaustive.py` builds the Fano plane from the nonzero binary triples and enumerates all 16,384 vertex-deletion masks. A union-find forest test checks all remaining edges. It constructs every TAR state and transition for budgets five and six; checks exactly fourteen 51-state components and 168 isolated states at five; checks connectedness on 3,136 states at six; runs shortest-path searches from all 3,136 sources; checks all 2,415 distinct pairs of four-vertex minima, every state eccentricity, the diameter, and all pair-distance excesses. Its output includes an all-pair distance histogram.

`verify_independent.py` instead constructs Fano lines as translates of \(\{0,1,3\}\) modulo seven and uses a recursive undirected DFS for cycle testing. It independently verifies all fourteen geometric five-vertex kernels and all seventy minimum sets, the two TAR component/connectedness assertions, then searches each optimum pair for an *explicit monotone route*: additions are restricted to the target difference and deletions to the source difference, with capacity at most six and all intermediate configurations tested for feasibility. Every pair succeeds. The path proof is thus exact for every pair, not a random sampling experiment.

Important boundaries: the theorem concerns only the labelled Fano incidence graph and the specified minimum/maximum deletion-set cardinalities. Complete enumeration of this fixed graph is exhaustive proof for this finite claim; the code does not provide a proof for all cubic or finite-projective-plane incidence graphs. No external independent validation or proof-assistant certificate is asserted.
