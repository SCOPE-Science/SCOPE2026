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

The number of ones in uu is even, so a factor here has zero or two ones. Zero-one-count factors contribute exactly floor(max(a,b,c,d)/2). Each two-one square has a unique pair x,y of exterior zero counts, with internal gap x+y. Its ones must be adjacent among the three ones of the word. For the first pair the admissible integer x runs from max(0,b−c) to min(a,b), and the second uses the corresponding b,d;c interval. Two pairwise strings coincide only at b=c; then x,y must satisfy x≤a and y≤d in addition to x+y=b, giving precisely the stated overlap. This also checks all zero-gap cases (111 has one square string). In the aggregate, a shape for one pair contributes z^{2(x+y)+r+s+t} over five free nonnegative parameters; a common shape contributes z^{3(x+y)+r+s} over four. For zero-only shapes of length 2k, inclusion-exclusion over the gaps ≥2k gives the binomial sum in (2). The dominant pole at 1 has order five and coefficient H_4/2+1/2=37/24; the overlap pole has order four there and all nontrivial-root poles are at most double. Coefficient extraction and division by binom(m+3,3) yield the claimed 37/96 slope with O(1) remainder. Uniform scaled weak compositions converge by Riemann sums to the uniform simplex. Off b=c the difference between S/n and F(a/n,b/n,c/n,d/n) is O(1/n); only O(m²) of the Θ(m³) compositions are on that diagonal. This proves the weak limit. S/n is uniformly bounded by the counting formula, so its limiting mean is the same 37/96. F at the two displayed interior examples is 0.60 and 0.44; open neighborhoods have positive probability, proving positive variance.

## originality

PASS

The supported claim is the exact ordinary distinct-square count for every linear indexed weight-three word, including the duplicate-string diagonal, and its aggregate and distributional consequences. Published sparse-word bounds do address the same population but do not give the count. The closest catalogue statements change the weight, equality of halves, or linear boundary. No inspected stronger statement already determines this count and its conditional limit.

## value

PASS

Weight three is the first weight with competing adjacent marked pairs whose repeated strings can coincide. Resolving that overlap gives an exact per-word answer where sparse-word maxima or upper bounds do not suffice, and the OGF and nondegenerate conditional law quantify typical growth. This is a motivated finite-weight classification, not an arbitrary fixed length or a numerical census alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
