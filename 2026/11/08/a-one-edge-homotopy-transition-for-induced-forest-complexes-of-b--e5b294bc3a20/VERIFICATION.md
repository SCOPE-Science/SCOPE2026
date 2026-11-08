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

# Verification of the induced-forest homotopy transition

Run `python3 verify.py` with Python 3. The verifier constructs edges and induced forests independently by union–find cycle detection. It calculates simplicial boundary ranks over \(\mathbb F_2\) by binary Gaussian elimination, without assuming the asserted Betti-number formulas when constructing the complexes.

All bipartite graphs on bipartitions \((2,2)\), \((2,3)\), \((2,4)\), and \((3,3)\) are checked exhaustively across every edge subset. Further larger bipartitions are checked with fixed-seed samples. All single-cross-edge deletions are checked in the specified larger bipartitions; the sharp two-deletion case is checked by direct face enumeration, chain-rank calculation and unique top boundary faces.

The integral proof uses the explicit fundamental-cycle basis of \(H_1(K_{a,b};\mathbb Z)\) and the corresponding connecting homomorphism in the Mayer–Vietoris sequence; finite calculations over \(\mathbb F_2\) cannot establish this integer result, so they are reported only as corroboration.

The theorem does not classify higher homotopy for arbitrary proper bipartite graphs. No independent mathematical audit has been performed.
