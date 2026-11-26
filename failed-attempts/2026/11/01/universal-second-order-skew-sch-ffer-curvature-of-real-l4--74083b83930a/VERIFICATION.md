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

Reconstructed RESULT.md lines 21–83. Expanding (x²+√2xy−y²)² cancels the mixed quadratic term and gives 2+2√2(P−Q) on integration. If δ is the L2 norm of this defect and e1,e2,e3 are its pairings with x²,y²,xy, then e1−e2−√2e3=2−4E and e1+e2=√2(P+Q); Hölder gives |ei|≤δ. The displayed P,Q,E estimates give |3E−P²−Q²−5/4|≤7δ≤12√d using |P²−P0²|≤(1+1/(2√2))|P−P0| and similarly for Q. Differentiating the square root of the norm fourth power gives the third-derivative bound 72/||z||4 for unit directions; along either segment ||z||4≥7/8, so the Taylor remainder bound 24h³ is conservative. The corresponding norm second derivative is nonnegative and ≤3/||z||4, validating the ≤8 bound used for the difference of the two norms. The arithmetic mean squared subtracts (u−v)²/4 from the quadratic-mean square, costing at most 2√2h²d+32h⁴. The remaining coefficient of hd is ≥1/2; completing the square costs 72h³, and 32h⁴≤4h³, giving 100. Two disjoint supported unit functions exist in any real L4 of dimension at least two: the finite measure weighted by |x|⁴+|y|⁴ for independent x,y must admit a positive split, or their normalized coordinate functions are constant on its only atom. The given a,b pair has E=1/2 and P=−Q=−1/(2√2); its two outputs are coordinate permutations with signs and thus have equal norm. This gives the common upper bound, including the maximum endpoint, and the square root has coefficient 9/16. The frozen finite verifier was inspected, not executed; the analytic proof, not the finite checks, establishes the bound.

## originality

FAIL

Indexed record 2846c5f281be already proves the uniform second-order law for precisely the same space, infimum, and all outer means including infinity. It uses the same quartic square, stability of the arithmetic mean coefficient, and equal-output upper pair. The new numerical remainder constant is a routine explicit bound obtainable from that proof on the same interval; it does not supply a distinct mathematical result.

## value

FAIL

A sharp curvature coefficient uniform through the maximum-mean endpoint is a worthwhile result, but is established in the matching indexed theorem, which also gives near-minimizer rigidity. The only nominal increment, the deliberately conservative constant 100 at the same local cutoff, is neither mathematically motivated nor stronger than an explicit reckoning of the existing estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
