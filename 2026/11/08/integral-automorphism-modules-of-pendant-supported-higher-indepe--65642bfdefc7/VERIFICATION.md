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

# Computational corroboration and limits

`verify.py` uses only Python 3 standard-library functions. It reconstructs faces by directly enumerating vertex subsets and induced-graph connected components. It separately constructs mod-two simplicial boundaries, calculates reduced ranks by independent bitset Gaussian elimination, and computes signed fixed-face Lefschetz numbers for generated graph automorphisms. A character function derives the predicted trace from the cycle polynomial of leaf permutations and the core orientation sign. Every nonempty subset of core vertices is also tested to have a deletion-complex cone apex among its former pendant leaves.

The finite test set comprises 11 core graph/leaf profiles: a star; two asymmetric/symmetric double-stars; two three-core paths; two triangles; a four-core path, cycle, complete graph, and branched core. Each r from 1 through vertex-count plus one is tested. The executed output reports **712 homology/character checks** and **819 cone checks**, all passing. Independently replay with `python3 verify.py` and compare to `verify_output.txt`.

These calculations do not certify any infinite statement and do not check integral torsion. The unrestricted, integral result follows from the explicit natural relative-chain isomorphism and exactness of the augmented simplex chain complex in `RESULT.md`. No independent audit has been performed.
