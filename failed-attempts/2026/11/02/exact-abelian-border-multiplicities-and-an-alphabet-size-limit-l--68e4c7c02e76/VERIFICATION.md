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

Complementing overlapping prefix/suffix Parikh sums pairs each border j with n−j. Pairing the two outer halves yields an independent walk with q labeled holding increments, not just one. The multinomial-square return count, first-return factor U=1+FU and return-free tail T then give the stated two series: an odd word has q free middle letters; an even final return contributes one border instead of two; the empty word gives 1. Ordered sets of marked positive return times give factorial moments by multiplying the return probabilities at their successive gaps. In q−1 coordinates the increments span the integer lattice and include a hold; the Fourier integral has a unique modulus-one point on the torus, with covariance 2(q⁻¹I−q⁻²11ᵀ) and determinant 2^(q−1)q^(−q). Gaussian scaling gives the asserted local-return constant. In the ternary moment sum, the cubes of side ⌊m/k⌋ and m bracket the simplex, giving exponential moments after log scaling. In the binary simplex integral the discarded small coordinates cost O(√δ) after scaling, so the integrable singularities cause no extra constant. In the transient regime the renewal mass gives escape parameter 1/U_q(q^−2), and the even central correction vanishes in probability by the local-return estimate (a mere bounded difference would not suffice there).

## originality

FAIL

A distinct indexed result gives the exact same full distribution after the deterministic shift D_n=K(w)+1, for all q and all nonempty lengths, with the same limiting regimes and constants. The zero-length convention supplies no additional result. This establishes present claim-level coverage, not historical precedence: the matching entry is dated later and no inference is made from dates about who proved the result first. The published binary predecessor, general alphabet walk reduction and classical fixed-walk return tools separately limit the novelty of the method.

## value

FAIL

The full proper-border count is a natural statistic and the change of regimes is useful. The frozen theorem contributes no uncovered precise invariant beyond an exact all-parameter coinciding law and a routine renewal/local-limit derivation from the established walk reduction. The change of terminology from composition deficit to proper borders and a compulsory shift does not yield a further theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
