---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

The exact all-size proof is in `RESULT.md`. The standalone Python 3 script `check.py` uses only the standard library. Invoke `python3 check.py 80` from the package directory; it terminates by printing `VERIFY_OK` after the following checks.

1. It constructs every positive integer partition with two through five parts at each admissible fixed size through eighty. The resulting 364,194 profiles exhibit no same-size scalar collisions at two, three, or four parts and exactly the predicted 91 two-element collision fibers at five parts.
2. A separately coded combinations-with-replacement algorithm enumerates all five-part profiles through size sixteen, finding the unique pair \((1,3,4,4,4)\), \((2,2,2,5,5)\) at size sixteen and none earlier. There are 37 five-part profiles at that size.
3. The checker constructs all five-summand exponent multisets with exponent at most sixteen; among 20,349 multisets it finds 49 equal-exponent-sum and equal-power-sum pairs, all of which have precisely the classified three-bit resonance.
4. It directly generates one-point class assignments and adjacency-bit strings in small structures, checking both the scalar and adjacency-graded polynomial formulas and triangular inversion of the graded polynomial.

These are independent finite sanity checks, not a computer proof of all-size completeness. The combinatorial splitting proof covers arbitrary nonnegative exponents and is included in the main result. The statement is only about same-size scalar collisions and positive part sizes in a finite-class homogeneous structure. No independent external audit has been performed.
