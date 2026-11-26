---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The result uses unnormalized counting convolution on the full sixteen-bit group. A block is a two-flat incidence word, equivalently a weight-four word of RM(2,4); the span contains the quadratic monomials, linear terms (by adding two products sharing a factor), and the constant (a parallel class). Its annihilator is RM(1,4). In independent exact arithmetic, testing one character per affine coset via the degree-four Krawtchouk average and then summing signed reciprocal multipliers on each of the 2048 codewords reproduced the full frozen distribution and inverse table, including the zeros. Off the code the reciprocal character sum cancels by affine-frequency invariance. The corrected inverse statement is also verified without computing a spectrum: classification by alternating polar rank and the radical restriction of the linear part yields eight affine-coordinate orbits on the quadratic code. Counting h+P for all 140 distinct level-set products P and one representative h of each orbit gives the stated integer quotient matrix; independent replay verifies the matrix, its orbit-size balance and its convolution identity with the numerator column. Zero extension off the code preserves the identity Tk=δ0. A unit coordinate vector and the signs of one row attain respectively the column and row absolute-sum norms, both equal to 14468/3360=3617/840. The original numerical claims are true, but the repaired claim does not assert a new spectral classification. The supplied source script was inspected, not executed.

## originality

PASS

Pass for the repaired inverse-in-incidence-coordinates result and its sharp endpoint norm, not for the eight-level zero-free classification framed as new. The inspected four-variable Boolean orbit table gives the eight levels directly by fourth moments, and the full signed spectrum reduces to those levels weighted by the orbit sizes. No priority order is assumed for the public webpage. No inspected result supplies the spatial inverse or the endpoint norm. The repaired contribution exhibits the affine-orbit convolution equations which determine that concrete inverse directly.

## value

PASS

For this canonical sign-incidence recovery operator, the exact endpoint norm measures the strongest possible amplification of bounded error or ℓ¹ input error. It differs substantially from the ℓ² inverse norm and is not specified by just the unordered eight spectral levels. A small explicit affine-orbit convolution system supplies the spatial sign and size of every inverse coefficient and the sharp worst-case constant. This retains a meaningful exact invariant rather than rebranding the existing Boolean spectral table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
