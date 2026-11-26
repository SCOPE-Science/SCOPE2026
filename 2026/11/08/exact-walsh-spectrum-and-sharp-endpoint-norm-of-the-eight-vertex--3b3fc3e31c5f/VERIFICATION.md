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

Every matching uses each vertex once, so vertex switching multiplies all terms by the same sign. Fixing the seven incident signs at one vertex picks one point per orbit of size 128; with the switch fixed to zero at that vertex, even and odd switches pair the signs in each orbit. Fourier inversion gives kernel H/2^28. Its absolute sum is attained on a delta for the counting-measure ℓ¹ norm, and by the reflected kernel sign for ℓ∞. Independently, on every one of the 2^21 normalized assignments I evaluated the sum of the seven six-vertex principal hafnians (conditioning on the partner of the star vertex). Each six-vertex hafnian expands by a fixed vertex into five signed four-vertex hafnians, evaluated by their three products. Exact bounded integer arithmetic reproduces all 23 table entries and all absent levels, with first absolute sum 16854180, second sum 220200960, fourth sum 84777369600, and norm 4213545/524288. Oddness excludes zero. For magnitude 105, comparing the three ways of matching the star vertex and any triple while fixing a matching on the four other vertices forces the three signs on that triple equal; hence the two normalized matrices with all other signs constant are exactly the extremizers, giving 256 full points. The frozen Python and C certificates were inspected, not executed.

## originality

PASS

The evidence supports the distinct exact histogram and its absolute first moment for the K8 perfect-matching orbit. The matching identity, switching, and endpoint convolution reduction are background, not novelty. The nearest inspected results use Gaussian estimators or materially different matching supports. No global publication-priority claim is made.

## value

PASS

Perfect matchings form a canonical nonbipartite frequency orbit. Its projection's exact endpoint amplification is a meaningful invariant not recovered by cardinality, nonvanishing or Parseval. The entire order-eight law is reusable for exact comparison with other matching supports and for checking analytic bounds or higher-order censuses; the value does not depend on extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
