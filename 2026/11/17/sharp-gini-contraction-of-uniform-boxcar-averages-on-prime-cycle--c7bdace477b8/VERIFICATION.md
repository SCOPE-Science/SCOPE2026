---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Positive linear boxcar averaging gives the exact all-real norm as a maximum over binary indicators by coarea. The substantive external input is Lev prime cyclic majorization as restated with parity conventions in Madiman–Wang–Woo Lemma 6.3; it implies convolution of a k-set and m-arc is majorized by interval-convolution. Gini is symmetric convex, so intervals suffice. With k<=floor(p/2), m<=floor(p/2), window overlaps form level lengths c_t=m+k-2t+1 for 1<=t<=min(k,m), and the layer-cake identity gives p m k-ab²-a(a²-1)/3. The resulting two piecewise rational Gini ratios strictly increase with k to the balanced cut, giving 1-(m²-1)/(3Q). For m>p/2, complementary windows give the exact factor d/m and same balanced witnesses. This proves all odd primes>=5 and all widths 1<=m<p; nonprime cases are not claimed.

## originality

PASS

Lev majorization is explicitly credited and provides shape, not the full two-parameter Gini norm or maximizing cut cardinality. Earlier exact 2-/3-tap results are special-width consequences but do not establish all widths. This work supplies the all-width optimization and width-complement duality.

## value

PASS

Sharp dispersion stability of a canonical finite moving average across every window width and odd-prime cycle, including the exact quadratic deficit and balanced-arc witnesses. The complete natural parameter family is mathematically useful independently of a downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
