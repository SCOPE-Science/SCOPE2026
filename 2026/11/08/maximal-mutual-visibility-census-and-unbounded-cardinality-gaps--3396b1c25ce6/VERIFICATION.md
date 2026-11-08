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
# Reproducible finite and structural checks

Run `python3 verify.py` with Python 3 and no external libraries. The initial 2360-state check is exhaustive *as a theorem of the four-coordinate threshold-capping lemma given in RESULT.md*: counts greater than four can be capped at four with no change in any current or one-addition visibility predicate. Without this separate lemma, enumerating 2360 states would establish only a finite sample and not the stated infinite theorem.

A second, independent test constructs \(G_n\) from bipartite adjacency lists, calculates distances by breadth-first search, checks the geodesic definition for every subset, and tests inclusion-maximality by attempting every single addition. Graph orders \(n=4\) through \(9\) yield \(1,397,760\) checked subsets, \(1,351,121\) visible sets and \(3,456\) maximal sets. The program compares their complete cardinality polynomials against the theorem and asserts exact agreement.

Sample maximal-set polynomials: \(n=4\) yields \(8z^5+10z^6+32z^7+z^8\); \(n=5\) yields \(10z^6+2z^7+20z^8+50z^9+z^{10}\). These computations do not themselves prove any asymptotic or general statement. No independent mathematical audit has been performed.
