# Independent mathematical audit

## correctness

PASS

For fixed labels a,b, the labels of the two products agree and the subset equations s_x t_(x+a)=t_x s_(x+b) factor across cosets of <a,b>. Both labels zero gives 4^n. On a two-point orbit with exactly one label nonzero there are eight solutions from a constant indicator and two from a nonconstant one; for equal nonzero labels there are 4+3*2 singular binary column pairs. For independent a,b put d=a+b. Up to translation the supports of S are empty, {0}, {0,a}, {0,b}, {0,d}, {0,a,b}, and full, with multiplicities 1,4,2,2,2,4,1. Substitution gives respectively 16,4,1,4,4,1,4 choices of T: the singleton sets t_a=t_b=0; the a-pair and the triple force all four t to zero; the b-pair and full set leave equality on a-pairs; the d-pair again forces t_a=t_b=0. Thus the four-point total is 58. Multiplying per orbit and summing over 1, 3(n-1), (n-1)(n-2) ordered labels proves the full count, with no independent-label case for n=2. The n empty elements commute with all of W_G. Replace their ordered-pair contribution 2n(n*2^n)-n^2 by 2|M_G|-1; no new commuting pair of nonempty elements is created since both products already have identical labels and differ, if at all, by subsets. The zero and nonempty partial identities give exactly 2^n idempotents in M_G, all mutually commuting. Since 58^(1/4)<sqrt(10) and 2<sqrt(10), the error term follows by division by |M_G|^2=n^2*4^n*(1+O(2^-n)), and the conditional idempotent probability is exactly 4^n/C(M_G). The independent python3 /workspace/independent_checks.py 5 composes explicit partial maps to obtain (46,31,7) and (1504,1129,61) at n=2,4, and independently counts the local 58. These are corroborative finite tests; the coset argument covers all k. The supplied checker was inspected, not run; its bit_count call requires Python 3.10+ despite the broader compatibility note in VERIFICATION.md. This does not affect the claim.

## originality

PASS

Existing work supplies the semidirect-product setting, the general commutation criterion, and closely analogous two-point and idempotent-dominance phenomena. The supported distinct result is the explicit all-pair orbit enumeration, including the independent-label factor 58 and the zero-collapse correction for the regular translation monoids. The applicable criterion does not supply those multiplicities without the extra local census and orbit argument. Historical priority remains provisional.

## value

PASS

Regular group translations give a natural inverse monoid of partial bijections, and the ordered commuting count measures its deviation from a commutative semilattice. The formula identifies the non-idempotent contributions by their orbit type, explains the effect of preserving or discarding empty labels, and yields an exponentially accurate comparison between the full commuting census and its idempotent pairs. The all-order family and quotient dependence offer more than a tiny instance or a single graph computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
