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

## Reproduction

Run `python3 verify_kneser.py` (Python 3 standard library) and `python3 verify_petersen.py` (requires `networkx`). Both programs were run from the actual embedded source contents and returned PASS. Neither uses or imports a log, prior package, or another verifier's output.

The first constructs the Petersen graph directly as the disjointness graph on all ten pairs of five labels, and tests every deletion subset of size up to five by union-find. The second builds the wheel-and-spokes graph `networkx.petersen_graph()` and tests forest status using an independent graph routine. Both form the entire vertex set and edges of the budget-four and budget-five addition/removal networks; both search shortest paths completely from every one of the 400 budget-five states.

Verified quantities: minimum deletion sets 20; feasible four-sets 140; feasible five-sets 240; budget-four graph 160 vertices and 140 edges, with five 29-state components and fifteen singleton components; budget-five graph 400 vertices and 980 edges, connected; minimum-pair distance distribution 30 at 2, 90 at 4, 70 at 6; size-conditioned state eccentricities (3,8):20, (4,9):140, (5,10):240; 120 unordered pairs at diameter ten. The 400-state all-pairs test includes 79,800 unordered distances.

## Scope and limits

The all-order reasoning in the result is for this exact finite labelled graph, not a statistical sample. The constructive optimum-pair routes and the budget threshold have direct proofs. The two complete finite enumerations certify the finer radius/diameter/eccentricity numbers; failed execution or a non-exhaustive modified loop would not certify them. The independent audit remains unperformed.
