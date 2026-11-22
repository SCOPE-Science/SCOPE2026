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

# Verification

Run `python checker.py` from a directory with Python 3 and SymPy. The program enumerates every injective word and computes every ordered semigroup product for the cases \(n=1,2,3,4\), verifying commutation is exactly prefix comparability. It constructs the full \(2\)-, \(5\)-, \(16\)-, and \(65\)-vertex adjacency matrices directly and checks exact symbolic characteristic polynomials against the formula from the theorem. It verifies the noncentral decomposition and all \(-1\) multiplicities in those cases.

The same checker independently calculates quotient determinants, exceptional-root derivatives, and the required principal minors through \(k=10\), and checks the claimed characteristic degrees and exponent sums through \(n=15\). It emits three markers: `DIRECT_ALL_PRODUCTS_AND_FULL_CHARPOLY_PASS`, `RADIAL_MINUS_ONE_SIMPLE_AND_MINOR_PASS`, and `DEGREE_AND_MULTIPLICITY_IDENTITIES_PASS`.

These finite checks do not establish the infinite theorem; the proof is the orthogonal invariant-space decomposition and determinant argument in `RESULT.md`. The counting-graph convention includes the empty word, with a separate noncentral corollary. The only assumed dependency is SymPy for symbolic matrices and polynomials. No external audit or formal proof certification has been performed.
