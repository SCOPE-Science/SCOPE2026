---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In the one-operation signature a binary term has coefficient A in R=F_p[T] and complement I-A. The achieved set, containing 0 and I, is closed under A,B -> TA+(I-T)B. Composition with the coefficient-zero projection gives the two maps multiplying by T and by I-T; invertibility and finiteness make them permutations of the achieved set. Taking preimages proves closure under addition, and hence it contains all polynomial coefficients. A many-variable equation is a homogeneous block linear map with block entries in R. Their generated ideal is principal in F_p[X]/(m_T); factoring the block entries through a generator g(T) gives one image inclusion and Bézout gives the other. Uniform sampling then gives p^(-rank g(T)), attained by the binary term for coefficient g(T) equated to y. If a display needs syntactically both variables even for probability one, a positive finite-order iterate of the left translation z -> x*z applied to y is an identity witness. On each f^lambda primary block an f-adic valuation a gives image dimension deg(f) max(lambda-a,0); choosing the product of primary factors realizes every truncated valuation tuple, including rank zero. For reducible m_T, a proper irreducible factor f has f(T) nonzero, with a nonzero operator (m_T/f)(T) annihilated by it, so its rank is intermediate; in the irreducible case every nonzero coefficient is a unit. The proposed p>=3 Jordan family has ranks n, k-1, ..., 0 and satisfies the two invertibility hypotheses. Read the supplied verify.py and VERIFICATION.md without executing them; their frozen replay path is verify.py relative to the source directory. Separate exact modular checks compared closure and kernels for 50 ring elements across five representative cases, including the rank-one Jordan example with 27 satisfying pairs out of 81 and a ternary associativity equation with 81 solutions out of 729. At p=3,n=4 the four level counts were independently corroborated. These finite calculations are not an all-dimensions or all-terms proof.

## originality

FAIL

A distinct indexed Resultary result states and proves the exact same spectrum in the same finite one-operation Latin Alexander signature, with binary witnesses, the same elementary-divisor formula and the same irreducible-minimal-polynomial criterion. Its primary-power level-count theorem also yields the frozen fixed-order assertion by taking one size-k Jordan block and n-k scalar blocks at any allowable scalar. This is theorem-level equivalent coverage, not a chronology or priority claim.

## value

FAIL

An exact term-equation probability invariant on a natural affine family is worthwhile in principle. In this record it duplicates the indexed exact formula, and the attainable fixed-order number of levels is an immediate specialization of the known primary-power formula. The alternative coefficient-closure proof does not establish an uncovered invariant or further mathematical application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
