---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The killed generator is the irreducible labeled exclusion generator minus diag(κ), where each occupied pair contributes the sum of its two directed jump rates. Irreducibility follows by moving particles to vacancies and using a vacancy to swap two labels. Equality of the Doob rates forces its positive Perron eigenfunction to be constant along all allowed moves, hence κ constant; constant κ gives scalar killed-semigroup factorization and equality even for finite-horizon conditioning. Differentiation at time zero proves the converse from common survival. Comparing k-sets differing in one vertex gives zero sums of w_au−w_bu over all (k−1)-subsets of the remaining n−2 vertices. For k≤n−2, exchanges force the differences equal, hence zero; symmetry then forces uniform weights. At k=n−1 the hazard is W−d_v; 2W=nd gives (n−2)d/2. The degree-map rows are independent because a_i+a_j=0 for all i≠j implies all a_i=0 for n≥3, giving the stated dimension and explaining the uniform n=3 case. An independent clock with constant intensity and a pair choice proportional to pair intensity reproduces the pre-collision trajectory and unordered pair mark. If the terminal collided tuple is also wanted, split the pair mark into its two directed jumps in proportion to the two rates. The attached finite matrix checks were inspected, not rerun; they are illustrative only.

## originality

FAIL

An earlier, stronger Resultary theorem for connected supports already contains the main classification, both rates, and the independent exponential clock. The dimension and unordered pair kernel are not separately displayed there, but reduce respectively to the rank of the already identified degree constraints and normalization of the two directed jump intensities. The finite-to-infinite conditioning and labeled formulation do not give a materially distinct remainder in the complete case.

## value

FAIL

The packing-boundary exception is a useful question, but its exact classification and unmarked clock are already available on broader support. The remaining degree count and elementary marking rule do not supply another independently useful unknown boundary or invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
