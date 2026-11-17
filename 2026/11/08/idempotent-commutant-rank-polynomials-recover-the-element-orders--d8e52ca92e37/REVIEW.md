# Independent mathematical audit

## correctness

PASS

The final all-finite-group result is correctly normalized: idempotents of restriction monoid are the 2^n partial identities; each nonempty restricted translation has unique g; e_A commutes with s_{g,B} exactly when membership of A is constant along edges x->gx selected by B. A proper selection of j edges of an l-cycle is a forest with l-j components and 2^(l-j) A-choices; a full cycle adds the extra y^l, giving ((2+y)^l+y^l)^(n/l). The g=1 contribution is 2^n(1+y)^n and the duplicated empty restriction requires subtraction of 2^n for each g!=1. Expansion after subtracting baseline shows H_{n,l} first nonzero term (n/l)2^(n-l)y^l and gives triangular recovery of every element-order multiplicity. The even-order asymptotic follows by monotonic decrease of (3^l+1)^(1/l), with all l>=3 bounded by 28^(n/3). Independently enumerated explicit commuting pairs for C4 and V4, obtaining [16,160,176,96,24] and [16,160,192,112,28]. No inference about group isomorphism from equal histograms is made.

## originality

PASS

No inspected earlier complete theorem supplies both the all-regular-action idempotent/partial-translation commuting-pair polynomial and the converse triangular recovery of element orders. Fernandes provides the underlying cyclic inverse monoid; Konieczny treats permutation centralizers and regularity, not this ordered pair invariant; other Resultary permutation-centralizer rank results count idempotents of a different monoid. The proof itself uses standard cycle-forest combinatorics. Best-of-knowledge originality is limited by possible general semigroup cycle-index centralizer formulas.

## value

PASS

This is a natural intrinsic rank-graded invariant of inverse monoids recovering the full element-order profile of any finite group, distinguishing same-size groups including C4 and V4. The reconstruction theorem goes beyond a routine total count and is potentially useful in finite inverse-semigroup and group invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
