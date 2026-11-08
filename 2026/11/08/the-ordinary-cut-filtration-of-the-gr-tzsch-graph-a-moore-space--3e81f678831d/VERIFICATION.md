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

# Reproducibility
Run `python3 verify_grotzsch_cuts.py` in an environment with Python 3 and its standard library. The program neither downloads papers nor uses precomputed homology tables. Compare all printed checks with `verification_output.txt`.

It rebuilds the Grötzsch graph from the five-cycle Mycielskian construction, independently tests each face by two complementary enumerations, verifies the full reversed Hasse digraph is acyclic, and calculates all integral Morse differentials by signed gradient-path recursion. At the three-cut level the exact matrix has absolute determinant two and a unit two-by-two minor; at the four-, five- and six-cut levels rank-sized unit minors certify all nonzero Smith factors are units. Direct mod-two simplicial boundary ranks provide a separate chain-level check. The finite checks cover all vertex subsets and all face incidences for the named graph; they do not assert an infinite graph-family theorem.

The homotopy conclusions additionally use the standard discrete-Morse CW equivalence and the classification of attaching maps from a sphere to a wedge of equal-dimensional spheres in dimension at least three. No independent external audit has been performed.
