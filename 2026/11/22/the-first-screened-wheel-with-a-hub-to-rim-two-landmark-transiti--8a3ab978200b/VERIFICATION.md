---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The residual covariance vanishes on observed rows and columns and equals the inverse unobserved principal precision block on the rest. Its trace is p'(mu)/p(mu), with strictly positive grounded determinants even at zero because the connected Laplacian's quadratic form is strictly positive on nonzero vectors vanishing on the landmarks. An independent incidence-matrix/characteristic-polynomial calculation (python3 /workspace/branches/independent_exact.py wheels, SymPy) matches every supplied finite determinant and comparison coefficient and verifies the exact zero-screening rows for m=7 and 8. For 4≤m≤6 every comparison with the maximally separated rim pair has strictly positive numerator, and m=3 is K4. At m=7 the two nearer rim types have positive differences from the farthest rim type; the hub-minus-farthest numerator is 2P, with negative constant and all positive higher coefficients. It has just one positive crossing, independently isolated between 0.175354708826 and 0.175354708827 by rational evaluation. Counting orbit types gives 2,5,3 optimal pairs for m=4,5,6 and 7,14,7 in the three m=7 regimes. For all m≥9 the tridiagonal inverse formulas follow from the root r+r^{-1}=3 and zero endpoint conditions. Geometric sums bound the path inverse traces and row sums as stated. The rim-pair Schur correction has denominator at most 2sqrt(5) and numerator at least 1+(m−2sqrt(5))²/(m−2) by Cauchy–Schwarz; the lower bound after subtracting the hub trace increases for m≥9 and is strictly positive at 9. Continuity extends the zero-screening preference to positive screening. The large-mu inverse expansion at fixed m has hub-minus-rim leading term (m−3)/mu² from the difference of unobserved degree sums, so the hub loses for sufficiently large mu. Uniqueness of the crossover is proved only at m=7.

## originality

PASS

The positive-screening classification of two landmark sets is distinct in the inspected evidence. An earlier wheel result establishes the exact zero-screening classification. The strongest same-day positive-screening comparison treats one landmark on cones, including wheels, rather than the two-landmark decision; another treats budgets on stars, not wheels. Their date does not establish priority or equivalent coverage.

## value

PASS

The smallest positive-screening switch on a simple family is a motivated boundary, distinguished from the known unscreened transition by competing pair geometries at fixed m. The exact crossover and tie structure quantify when a high-degree hub loses against separated rim measurements. The result across all larger wheels shows the reversal is not an isolated small calculation, while leaving intermediate regimes open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
