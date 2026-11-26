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

In b^d at most one radical factor survives. On arrow a:i→j this yields y_a times the geometric sum in its two endpoint values, which evaluates the divided difference for the source polynomial, including f_i' when the endpoint values coincide. An arrow coefficient on the left is multiplied only by the target diagonal. Thus zero-arrow inputs force all vertex and arrow value functions to vanish; varying a single arrow with equal endpoint values forces the source derivative to vanish at every field element. Unequal-value differences already vanish. Since H=X^q−X is split with simple roots (H'=−1), the stated H or H² divisibilities are necessary and sufficient. Peirce multiplication preserves the resulting two-sided ideal. Hermite interpolation at all field elements gives independent value and emitting-vertex derivative functions and independent target offsets, proving the function count over every prime power. A bijection induces a bijection on the equal-size diagonal fibers, and on each fiber it is diagonal affine on the arrows. Once every vertex value function is a permutation, unequal endpoint differences are nonzero automatically; the remaining requirement is precisely nonzero emitting-vertex derivatives. This gives the permutation formula. For a nonloop, (e_i b)^2 has source value s² and arrow multiplier s at b=se_i+te_j+ya, inconsistent with the required multiplier s+t at (s,t)=(0,1) as y varies. Hence it is not any right-polynomial function. All-loop algebras are commutative and ordinary substitution proves closure. This concerns the full function set, not a universal closure statement for the bijections. The supplied checker was inspected, not run; its prime-field examples do not replace the argument.

## originality

PASS

The two-sidedness theorem and componentwise dual-number classification already cover substantial parts. The triangular null criteria also recover the global kernel by intersecting inverse images under elementary arrow quotients, and the total map count then follows, so these are not independent novelty claims. The distinct whole-quiver contribution is the simultaneous bijection criterion and census with shared vertex data, and the sharp nonrepresentability boundary for compositions of actual functions. The strongest checked composition predecessor uses the same ansatz for a different and weaker conclusion, not nonrepresentability by every polynomial. No checked statement or mechanical specialization supplies the complete classification with these conclusions.

## value

PASS

The classifier makes the effect of arrow orientation and shared sources on otherwise noncommutative polynomial functions explicit. In particular, the exact permutation criterion handles parallel arrows, loops and cycles simultaneously, and the function-level nonclosure test is strictly stronger than failure of the naive law for composing formal polynomials. Both are useful across a natural class; they are not obtained by just multiplying independent per-arrow counts. The known two-sidedness and the kernel-derived total count alone would not establish this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
