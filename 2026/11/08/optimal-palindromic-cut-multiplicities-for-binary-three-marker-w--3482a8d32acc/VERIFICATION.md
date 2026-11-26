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

At most four pieces always suffice by splitting off the leading zeros, a two-one palindrome, and a word with one one. If b=c one three-one middle palindrome suffices with the outer zero pieces; if an outer gap is at most max(b,c), take a corresponding one- or two-one palindromic prefix (or suffix) and factor the remainder into at most two pieces. In the claimed four-piece region both extreme palindrome pieces must consist only of zeros, and a three-one palindrome is impossible. For an optimal four-piece cut, leave p and q zeros adjacent to the first and last ones after cutting the outer pieces. The middle one counts must be (1,2) or (2,1), giving p+q=b or c respectively. Each nonnegative solution gives exactly one cut list with both extreme pieces nonempty, including a possible zero inner gap. Thus M=b+c+2. For h=max(b,c), ℓ=min(b,c), write h=ℓ+1+s and a,d=h+1 plus independent slacks. Then n=8+3s+4ℓ+slacks and k=3+s+2ℓ, with two orientations. This gives the series; at fixed k, choosing the smallest h>ℓ gives τ(k), and slack realizes every larger length. For the limit, scaled lattice points converge by Riemann sums in a bounded Jordan-measurable simplex slice; the available outer-gap length is 1−3h−ℓ. In t=h+ℓ coordinates the h integration runs from t/2 to min(t,(1−t)/2), with weight 2(1−t−2h). The two pieces, normalizing volume 1/36, and moments were checked by exact integration. The conditioning and indexed (not reversal-quotiented) convention are necessary.

## originality

PASS

The four-factor regime and length-only series are covered. The earlier positive-five-run multiplicity theorem also covers the zero-inner-gap slice. What is distinct is completing the fixed-three-one multiplicity formula for two positive unequal internal gaps and deriving the full bivariate distribution, attainable spectrum and conditional law. This comparison does not establish absolute priority.

## value

PASS

The count measures ambiguity of optimal palindrome segmentation, which minimal length alone does not capture. Fixed weight three is a natural first class with PL=4. The result resolves every optimal cut in this class, precisely classifies attainable multiplicities, and gives a nondegenerate conditional law. The contribution is beyond the known eligibility and five-run subcase, not a numerical census or a claim about larger weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
