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

# Reproducible finite computations

Run `python3 VERIFY.py` in the same directory as the file. It uses only the Python standard library. The procedure builds \(K_{m,n}\) by its adjacency list; finds shortest paths by a breadth-first-search distance function; explicitly packs sets of clear paths with disjoint interiors; exhaustively enumerates all nonempty subsets; compares their face numbers with the stated closed polynomial; and separately calculates the augmented simplicial boundary ranks over \(\mathbb F_2\) by bitset elimination.

The computations cover exactly \((m,n,q)=(4,4,1),(4,4,2),(5,5,2),(5,5,3),(5,6,3),(6,5,2),(6,6,3)\), totaling 6149 nonempty faces. All seven cases passed, and the exact output is in `VERIFY_OUTPUT.txt`. The \(q=1\) case only tests the known ordinary-visibility boundary; it is not a novel claim.

For \(q=2\) on \(K_{4,4}\), the resulting reduced mod-two third Betti number is 27. For \(q=2\) on \(K_{6,5}\), the reduced mod-two Betti numbers in degrees four, five and six are each 20. These match the integral wedge theorem, but the finite computations alone neither establish higher-dimensional integral torsion-freeness nor prove the formula for arbitrarily large shores or redundancy. Those claims follow from the explicit all-parameter simplicial pushout and nullhomotopy proof in RESULT.md. No external proof assistant or independent auditor is represented.
