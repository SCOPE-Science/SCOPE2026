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

The interpolation is uniformly convergent since the j-th term has pointwise valuation at least j. For x=4u+b the numerator factors with h congruent to b modulo 2 or 4 give the claimed Gauss coefficient bounds after using v_2(j!)=j-s_2(j); in the zero branch factor out 4u first and apply the counts to h=1,...,j-1. The bounds tend to infinity (for the zero branch the expression is 3+2 floor((j-1)/4)-((j-1) mod 2)+2s_2(j)); the three exact finite certificates were checked independently. The linear term vanishes because every nonconstant summand is divisible by u^2. Its quadratic coefficient is 16 Li_2(2). The asserted identity for Li_2 follows formally by differentiation and the zero constant term, converges at 2 and its transform 2/(2-1), and gives cancellation because log(-1)=0 by log((-1)^2)=2log(-1). Thus the cubic factor is exact, not just a truncated congruence. In both the linear branches and the normalized odd-unit cubic branches the difference quotient is odd; the latter uses w^2+wz+z^2 odd for odd w,z. Reduction gives bijections at every compatible precision, hence surjectivity by compactness. The negative-index binomial identity gives the reflection; its rational generating function can also be obtained by differentiating z^n/(1-z)^(n+1) n times and dividing by n!. The four output sectors are distinct modulo 16, two complete balls have total measure 1/8, and the two shells at depth 3a have total measure 2^(-3a), summing to 1/7. At finite precision unresolved shells contribute just their center residues, yielding the stated counts including 1,2,4 initially. Preimages of any attained cylinder are open and nonempty, hence contain infinitely many nonnegative indices. Replay: python3 /workspace/branches/check_delannoy.py independently recomputes the Gauss congruences and checks image sets through 2^11 using the original binomial sum with terms discarded only when 2^j is zero modulo the modulus. These finite checks are not the infinite argument.

## originality

FAIL

A distinct matching public catalogue statement (70933221cf22, Finding) explicitly covers the same full binary image, counting formula and Haar measure and additionally gives fiber multiplicities. This is demonstrable mathematical coverage, not a resolution of which same-day version was first. The earlier shift theorem also independently covers the two unrestricted balls. No distinct surviving theorem is claimed beyond the covered image/counts and recurrence of represented classes (the latter follows even from continuity and density).

## value

FAIL

The full dyadic range is a well-motivated exact invariant, and distinguishing valuation containment from unit surjectivity is mathematically useful. But the proposed contribution is the very image, measure and counts already provided by a distinct stronger fiber record, plus an immediate repetition consequence. No separate useful new invariant or claimed proof improvement survives that coverage. The rejection concerns incremental value of this frozen claim, not the intrinsic interest of the Delannoy range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
