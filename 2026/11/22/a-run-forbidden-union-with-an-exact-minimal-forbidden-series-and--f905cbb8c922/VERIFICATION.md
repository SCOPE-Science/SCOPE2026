---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

A finite word avoiding 0^m extends bilaterally by padding with ones, and conversely; the complementary argument applies to 1^m. The forbidden words of the union therefore contain both runs. Minimality says each length-(n-1) deletion must erase one type; the same type cannot be erased by both deletions, since every such occurrence would have to span the word, which also contains the other type. Consequently each endpoint holds one exact run of the appropriate type, neither type occurs again, and in either orientation the intervening word is empty or is a unique sequence of pairs of alternating runs of length 1 through m-1. Conversely those pairs give minimal forbidden words. Thus the series is 2z^(2m)/(1-R_m(z)^2), R_m=z+...+z^(m-1), with infinitely many nonzero coefficients. For |z| below the positive solution R_m=1 the denominator cannot vanish, and that positive singularity is not canceled. The overlap allows all alternating run compositions with lengths ≤m-1, including arbitrary boundary runs: every finite word with this constraint extends by alternating letters at both ends. Its nonempty word series is 2R_m/(1-R_m), with the same radius. The m=2 overlap is the period-two orbit, and the minimal forbidden counts 2 at the even lengths from four onward give limsup entropy zero despite empty odd levels. A component has primitive run-state transition matrix and words growing at the root lambda_m of the defining sum; the union has the maximum of the two component entropies. An ergodic measure lives on one component, where only its Parry measure can maximize entropy; the overlap has strictly less entropy, so these two component maximizers are distinct. The Parry process of each primitive SFT is Bernoulli, and affinity of entropy under ergodic decomposition gives exactly their convex combinations. Finally lambda_r tends to 2 and r(2-lambda_r)≤r lambda_2^(-r) for r≥2, so 2-lambda_r=lambda_r^(-r)=2^(-r)(1+o(1)); subtraction of the two adjacent deficits gives the coefficient 2^(-m-1) in the log gap. As independent finite corroboration, enumerate binary words for m=2 through 5 and n=1 through 14, test both endpoint deletions, and compare the actual sets with the alternating-run constructions and their cardinalities with the formal series. All 56 cases agreed. The frozen CHECKER.py was inspected, not executed; its larger finite range is not the proof of the all-length or limiting claims.

## originality

PASS

Prior entropy-gap results already give finiteness and Bernoulli up to period, and standard component theory gives the two measures once the equal competing entropies and lower overlap are known. Prior regular-language methods are also credited for minimal-forbidden computation and rationality. The independently significant residue is the closed complementary-run formula and its overlap-entropy identity, which quantify the positive gap and its decay in an exact two-phase family. No inspected theorem states or directly implies these family-specific formulas without computing the mixed obstructions. This is best-of-knowledge only; the closest automata article's full text was not accessible in this comparison.

## value

PASS

This family provides an exact test case for the relation between minimal obstructions and phase overlap in symbolic dynamics. The computation produces all obstruction counts, identifies the exponent with that of the overlap, and supplies an explicit rate at which a strictly positive entropy gap can shrink while two distinct Bernoulli maximizing phases persist. These quantitative features are more informative than merely exhibiting multiple maximizing measures or asserting rationality of an antidictionary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
