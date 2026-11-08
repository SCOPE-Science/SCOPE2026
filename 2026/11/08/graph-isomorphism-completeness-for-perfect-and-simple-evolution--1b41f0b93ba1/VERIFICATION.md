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

# Reproducibility and limits

Run `python3 checker.py` with Python 3.8 or later in the same directory as `RESULT.md`. It uses only the standard library. The exact output is in `verification_output.txt`.

The checker separately computes (i) linear algebra isomorphisms via the monomial scalar equations and (ii) two-color directed graph isomorphisms through canonical forms obtained by enumerating every vertex permutation, for all invertible two-dimensional matrices over \(\mathbb F_2\) and \(\mathbb F_3\). It also checks \(15^2=225\) pairs drawn at a fixed stride from the \(180\) invertible two-dimensional matrices over the non-prime field \(\mathbb F_4\), using the irreducible polynomial \(X^2+X+1\). Both methods agree.

For each of the \(75\) labeled undirected simple graphs on one through four vertices, the checker constructs the connected universal-hub graph, constructs the corresponding simple evolution algebra, independently verifies invertibility in characteristics two and three, tests strong connectivity of its multiplication graph, and confirms recovery of the original graph's isomorphism class (including isolated vertices). The observed graph-isomorphism class counts for graph orders one through four are \(1,2,4,11\).

The checker directly inspects its constructed structures; it does not rely on an external certificate. Finite tests are not the proof of polynomial-time reduction for arbitrary dimension or of completeness for every finite field: the universal mathematical argument is in `RESULT.md`. No implementation of a general graph-isomorphism decision algorithm is claimed. Independent mathematical validation has not been performed.
