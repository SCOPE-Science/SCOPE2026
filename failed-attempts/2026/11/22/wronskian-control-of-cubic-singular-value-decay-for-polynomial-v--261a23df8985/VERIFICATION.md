---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

In the Hardy monomial basis a symbol monomial a_m z^m contributes m a_m/(k+m) on shift m. Subtracting the two composition denominators gives the factor m n (m−n)/[(k+m)(k+n)(k+m+n)] and hence the exact leading polynomial W=z³(g''h'−g'h''). The finite-band remainder after replacing each diagonal by w_L(k+1)^−3 has tail norm O(M^−4) after the first M columns, hence s_j(E)=O(j^−4). The leading operator is multiplication by W times the positive-frequency multiplier (k+1)^−3; its extension by zero to the negative Fourier modes of the circle is a classical order −3 pseudodifferential operator with principal symbol W on the positive unit covector and zero on the negative one. The published singular-value Weyl law thus gives precisely the normalized angular mean of |W|^(1/3), cubed. Taking perturbing indices of order j^β for 3/4<β<1 in the forward and reverse singular-value inequalities leaves the limit unchanged. If W=0 the rational ratio of the derivatives, whenever the denominator is nonzero as a polynomial, is constant (and a zero derivative separately gives the zero commutator); otherwise the limit is positive and gives infinite rank, the claimed Schatten threshold and the harmonic logarithmic mean. Compactness and strict triangularity rule out every nonzero eigenvalue. The frozen block proof gives the same coefficient: in passing from weak Toeplitz distributions to hard counts one takes continuity thresholds (for constant |W|, the one exceptional radial level is negligible, or use the exact monomial shift case).

## originality

FAIL

The main singular-value limit and its nonzero coefficient are already covered by a stronger published Weyl theorem once the order and principal symbol are computed. This is demonstrable coverage, not a failure to establish a date or to retrieve the Toeplitz chapter. The exact Volterra phrasing need not have appeared verbatim.

## value

FAIL

The Wronskian formula is a useful illustrative specialization, but as a narrow exact-invariant finding it is mechanically supplied by the published singular-value Weyl law plus the routine leading-symbol calculation, and the frozen elementary proof does not extend the law to a new operator regime. The Schatten and logarithmic assertions are immediate consequences, not a surviving independent contribution. This verdict does not dispute correctness or pedagogical utility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
