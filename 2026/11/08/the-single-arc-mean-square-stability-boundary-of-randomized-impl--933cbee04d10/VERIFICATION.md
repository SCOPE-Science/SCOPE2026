---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For the stated multiplier and fresh independent stages, the second moment multiplies by E|R|² each step. With q=y² and D=(1+xt)²+qt², subtracting one from the integrand gives −D'/D+(x²+q)/D (prime in t); substitution t/(1+xt) integrates the latter and yields Φ. The q derivative has numerator 1−2t+2xt(1−t), over D². Pairing t with 1−t gives a nonnegative integral from the first term since D⁻² decreases; the second term is strictly positive for x>0, and at x=0, q>0 the first term is strict. The real-axis derivative (x²−2)/(1+x)² gives the unique positive cutoff X. Growth in y is uniform over x∈[0,X]: for y≥1+X the arctangent term is at least πy/4, dominating the logarithm. Pairing the squared multipliers at t and 1−t by AM–GM excludes Re z≥0; poles on the positive real axis have infinite second moment. Strict signs at every fixed y>0 over x=0 and x=X force B to tend to zero at each endpoint. Smoothness in the interior and the two disjoint upper/lower arcs joined at just the endpoints give the asserted bounded Jordan domain. At the origin Φ=−2x+q²/6+O(x²+xq+q³), giving B⁴∼12x. At X the ratio g'(X)/Φ_q(X,0)=3(X²−2)(1+X)/(X(3+2X)) gives C². The explicit defect is a quadratic in q with leading coefficient 1/3 and, for small x>0, negative constant term −2x+O(x²). Its unique positive root gives y⁴∼6x and the exact ratio 2^(1/4). The precise theorem in lines 23–27 is the one assessed: the interval is nonempty only for 0<x<X, not at every negative real part literally; line 82's two arcs are the upper and lower ones. The shipped numerical run is ancillary and was not rerun.

## originality

PASS

The supported distinct contribution is the global strict frequency monotonicity and the resulting single Jordan boundary, including the negative-endpoint square-root law and the quantitative comparison derived from the two boundary widths. The multiplier, moment test, left-half-plane containment, boundedness and real-axis cutoff are prior. The explicit coefficient follows immediately from its published moment polynomial. The implicit quartic contact is also covered by a broader same-day result; no priority between same-day records is inferred and that local law is not credited as distinct.

## value

PASS

The global one-interval result converts a pointwise test or plot into a certified frequency limit at every damping value in the stable range, with no disconnected bands or additional components. The endpoint laws describe how that allowable band closes at both extremes, and the near-axis ratio quantifies exactly how much width is gained over the explicit method in a regime where both bands collapse. These are concrete stability questions for the original methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
