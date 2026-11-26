# Independent mathematical audit

## correctness

PASS

The Li–Tang all-index bound and recurrence use the same vectors, weights, signs and nonnegative m as the frozen theorem. In the coefficient identity theta(0)=1 and xi=q+O(q²), so at q and q² the coordinates are a=y_{m,1} and b=12y_{m,1}+y_{m,2}. The h=12 term cancels, giving D_m=−Lambda^m_{2,1}. I recomputed both relevant columns via coefficients of theta xi^i at q³ and q⁶, and the fifteen exterior-square weights: the leading pair (2,1) has value 3 with Delta=395433=9·43937 and unit −1; every other pair has weight at least 4, with three zero minors. The next exterior-square iteration therefore has its unique least valuation 2m+9, while other terms have valuation at least 2m+10 by the all-index bound. The positive base minor 698368·3⁷ has unit 1; this gives the claimed alternating negative-sign determinant law and exact valuations. Li–Tang Theorem 1.2(ii) supplies existence at m+5 for all n, with n=0 trivial. Eliminating any integer multiplier from n=1 and n=2 at modulus 3^(m+6), and using Theorem 1.1 on the lower-level coefficients, would force D_m divisible by 3^(2m+8), a contradiction. In my own bounded reproduction (`/tmp/opencode/frozen-review-repro.py partition`), counting directly by odd part multiplicities and k choices of tag for multiplicity k replicated determinant valuations 7,9,11,13 and units 2,1,2,1 at depths 0–3, as well as both claimed congruence instances at each depth. I inspected but did not run the frozen checker. RESULT.md line 51 has a harmless u_3(0) typo for nu_3(0), already defined on line 21. Infinite-depth validation relies on the cited all-index bound and the exact induction, not on these examples.

## originality

PASS

The first two matrix columns, exact base minor, minor inequalities and achievable modulus are prior. The result that persists at every positive depth is exact sharpness and its leading unit, obtained by separating the leading exterior-square term from all other contributions and transferring this to arbitrary integer multipliers. The strongest closely related results inspected do not give that equality or its equivalent.

## value

PASS

This resolves the sharp modulus of a named infinite-family congruence, not an arbitrary slice or numerical base check. A precise determinant obstruction handles every possible multiplier and explains the signed noncancellation throughout the progression. The separate 8 progression and other extracted families are not covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
