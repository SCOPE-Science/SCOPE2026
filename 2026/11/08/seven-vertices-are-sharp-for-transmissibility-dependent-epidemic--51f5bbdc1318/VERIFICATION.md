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

# Computational verification

Run `python3 checker.py` using any standard Python 3 installation; no third-party dependencies are required. The checker was run directly on the supplied source and yielded `EXACT_CHECK_PASS`.

Expected tree counts for orders \(2,3,4,5,6,7\): \(1,1,2,3,6,11\) nonisomorphic classes from respectively \(1,3,16,125,1296,16807\) labelled Prüfer sequences. Exact Sturm counts show zero reversing seed pairs on any representative through six vertices and three unordered pairs across the eleven seven-vertex representatives, belonging to exactly two marked-tree classes. All are adjacent. For each witness, \(64\) distinct edge-retention patterns are independently enumerated at probabilities \(1/4\) and \(3/4\). The calculated exact mean differences agree with the distance-profile polynomial and have opposite signs.

Independent computational cross-check actually performed: NetworkX 3.6.1 generated nonisomorphic trees, SymPy 1.14.0 isolated polynomial roots exactly, yielding reversing pair counts \(0,0,0,0,0,3\) for trees of order \(2\) through \(7\).

The proof uses Prüfer's bijection, exact rooted-tree canonical strings and classical Sturm root counting. No stochastic simulation, approximate root estimate or extrapolation from seven vertices is used for the theorem. Independent external mathematical validation has not been performed. Bibliographic priority is not established by a search failure, and the 2002 specialized paper remains a stated access risk.
