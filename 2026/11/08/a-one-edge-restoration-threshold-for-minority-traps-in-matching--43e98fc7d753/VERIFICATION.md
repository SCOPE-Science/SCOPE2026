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

The assertion is proved for all \(n\ge3\) and all integer \(0\le t\le n\) by conjugating the update to majority-with-tie-flip on a bipartite graph, constructing finite paths to polar absorbing states, and classifying all local equilibria at the complete-deletion endpoint.

Two standalone, standard-library Python 3 programs check the derivation in complementary ways. `verify_transitions.py` exhaustively constructs the asynchronous update graph and computes terminal strongly connected components for 22 graph instances with \(3\le n\le6\), testing 36,352 labelled configurations. `verify_equilibria.py` independently evaluates the original rule's local inequalities for 39 graph instances with \(3\le n\le8\), testing 757,248 labelled configurations, and checks nonoptimal cut sizes. Recorded outputs in `transition_output.txt` and `equilibria_output.txt` were reproduced by executing the included scripts.

Finite enumeration does not prove the all-size classification or historical priority; the algebraic proof handles the former. No absorption-time bounds, noisy-chain analysis, or independent scientific audit has been performed.
