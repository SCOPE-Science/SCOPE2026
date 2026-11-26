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

Reassessed the corrected result. The main-text circuit uses U_F=U_odd U_even with even bonds (2j,2j+1) and odd bonds (2j−1,2j), the Heisenberg matrix unit at site 1, and cut 0|1; these conventions are now explicit. (S22),(S37),(S38) give the flat branch spectra and product-binomial squared masses for the normalized matrix. Supplement II C proves the Hermitian equality: M_H=(M+VM)/√2 with V†V=I and M†VM=0. Hilbert–Schmidt orthogonality of the row/column count blocks makes the low-difference mass exactly q_t(b); rank subadditivity bounds the rank of their sum by t(t+1)2^(b√t). Eckart–Young makes this a lower bound on the optimal retained mass at that budget. The complementary operator norm bound follows by summing block norms, and trace/nuclear norm duality gives the stated upper estimate. No joint Schmidt orthogonality is needed. The additionally credited (S55) gives F_t(r)≤q_t(b)+r2^(−b√t) and also implies the limiting upper profile. L−K has the law Bin(2t−1,1/2)−(t−1), so g(L−K)/√t converges to |N(0,1/2)|. Taking b above and below a/log 2 yields erf(a/log 2), with a=0 by letting the upper cutoff decrease to zero. The fixed squared-error quantile then follows from strict continuous monotonicity, for every fixed ε in (0,1). An independent exact staggered-packet check at t=1–4 verified all 40 count blocks by uniform disjoint rectangular components and checked that right indices remain ket/bra diagonal (`python3 /workspace/review_checks.py 1`); all-time flatness is sourced from the supplementary derivation, not these finite checks.

## originality

PASS

The frozen discussion materially understated the prior bound: direct inspection of (S55) and its use in (S57) confirms a linear factor r, not r². This gives the sharp upper retained-weight limit already. Corrected RESULT.md, REVIEW.md, AUDIT.json and SLOGAN.txt credit that implication and claim novelty only for matching sufficient rank and the resulting equality. The additional construction is a low-difference count-block approximation, not a substitution into (S55); it retains the requisite mass at matching scale despite the absence of a joint count-block Schmidt basis. No compared source supplies the matching profile. The original evidence is unchanged.

## value

PASS

After crediting the known sharp necessary scale, attainability is the substantive issue: a lower rank bound alone cannot tell how much accuracy a given resource budget achieves. The low-difference construction proves the matching achievable exponent for every fixed squared error and the whole optimal mass curve in a concrete integrable model. This is a quantitative single-cut benchmark, not an improvement of the prior converse or a rephrasing of the entropy growth law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
