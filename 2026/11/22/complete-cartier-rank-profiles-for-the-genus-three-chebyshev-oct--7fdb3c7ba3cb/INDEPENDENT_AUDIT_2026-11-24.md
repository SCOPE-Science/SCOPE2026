# Independent mathematical audit

## correctness

PASS

For odd p the roots come from z^16=−1 under x=z+z^{-1}; none has z=±1 and reciprocal pairing gives eight distinct images. This verifies separability and genus three. The invariants x=z+z^{-1}, y=w/z^4 of the genus-seven cover generate a degree-two fixed field, and the tame involution sends ω_i to −ω_{8−i}; its invariant differential space is exactly the three antisymmetric pairs (1,7),(2,6),(3,5). The binomial coefficient rule on the cover is nonzero exactly at pi≡j mod 16 for 1≤i,j≤7: pi−j is in [0,8(p−1)], including the edge case p=5,i=7,j=3, and h=(p−1)/2<p. Complementary pairs give exponents k and h−k and equal nonzero coefficients; multiplication by p is a permutation mod 16, so there is no cancellation or merging of distinct surviving paths under restriction. Duality may reverse arrows without changing power ranks. In residue order 1,3,5,7,9,11,13,15 the powers give (3,3,3),(2,1,1),(1,0,0),(2,2,2),(1,1,1),(2,1,1),(1,0,0),(0,0,0); thereafter each surviving path is on a cycle. The stable ranks and the first-rank defect give p-rank and a-number respectively, so ordinary iff the rank is 3 and superspecial iff a=3. Separately /workspace/reproduction/check_2.py (check_2.out) uses powers of the quartic in x², extracts coefficients directly on the genus-three curve, and tests minors of the matrix powers. All 44 primes 5≤p<200 agree, with every residue represented. The general theorem follows from the quotient calculation, not the finite check.

## originality

PASS

The supported distinct contribution is the complete eight-class table of Cartier-power ranks for this exact degree-eight Chebyshev curve. Prior maximality over F_{p²} covers the all-zero row p≡15 mod 16, which the finding explicitly does not claim as an independent novelty. Exact automorphism, maximality or Newton information and the known monomial Hasse–Witt method are not this full table. Remaining access and historical-priority qualifications are material but bounded.

## value

PASS

This is an exact classification of good reductions of a natural genus-three member of a studied Chebyshev family by their Cartier ranks. The nonmaximal rows distinguish non-superspecial p-rank-zero reductions and separate equal-stable-rank cases by the nilpotent Cartier part and a-number. Those distinctions are useful for testing descriptions of positive-characteristic strata and are not in a maximality criterion, while the proof identifies why the residue table appears. The result does not claim a full EO type or Newton polygon classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
