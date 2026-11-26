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

For a nonzero integer combination of the first d shifted P-values, the first nonzero moment of the shift coefficients has order s<d by Vandermonde invertibility. Its contribution in degree d-s is irrational and the lower polynomial coefficients can only contribute at lower degree. Weyl's criterion therefore gives Haar distribution on the d-torus modulo m. Conditioning on a prefix of d specified residue letters amounts to restricting to one unit box; the fractional parts there are independent uniform coordinates in the limiting law. The d-th finite difference gives the last letter as sum_i w_i A_i plus the correction floor(theta+sum_i w_i x_i) mod m. The total magnitude of its negative weights is 2^(d-1)-1 (the endpoint coefficient +1 was removed from the d-th difference); the positive magnitude is 2^(d-1). Reflecting negative coordinates now gives the sum of independent uniforms of lengths v_i, shifted by -s. Inclusion-exclusion on the positive simplex intersected with their box gives H_d, with the divisor d! times the product of v_i. The sum has positive mass in every nonempty open subinterval of (0,2^d-1). Irrationality gives theta=q+t with 0<t<1, so the deterministic fractional coordinates cannot produce corrections outside q-s through q+2^(d-1), even at a unit-box boundary. Each listed integer is realized on a set of positive volume, and the floor discontinuities are contained in finitely many hyperplanes of measure zero. This justifies the frequency formula and distinguishes actual impossibility from merely frequency zero. Reduction of the consecutive correction interval modulo m gives exactly min(m,2^d) extensions per prefix. The argument handles negative leading coefficients and d=1 unchanged, and shifting theta by m leaves the formula invariant. The uploaded check.py and VERIFICATION.md were inspected, not executed. Samples use exact integer floors for the chosen polynomials but the convolution and empirical probability comparisons are finite decimal/numerical diagnostics, not an exact all-parameter enumeration.

## originality

PASS

Credit classical degree-one coding, prior one-point modular equidistribution, broader existence of block frequencies, the quadratic binary special case, and the shared rank/finite-difference obstruction for a related indexed gcd claim. The supported distinct result is the exact all-degree and all-modulus positive support threshold and weighted-box frequencies at length d+1. No inspected source yields this full quantitative classification; same-date entries were compared mathematically without assuming publication order.

## value

PASS

The first length beyond the rank-guaranteed equidistribution window is a natural place to ask which words can occur. The exact modulus threshold distinguishes full support from forbidden words and the volume formula distinguishes possible but very rare words from impossible ones. The finite-difference dependence is resolved quantitatively for every phase and all lower coefficients, rather than merely observing that independence of the continuous shifted coordinates fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
