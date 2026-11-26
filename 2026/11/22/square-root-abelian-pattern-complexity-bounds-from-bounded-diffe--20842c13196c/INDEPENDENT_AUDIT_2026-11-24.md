# Independent mathematical audit

## correctness

PASS

Independently reconstructed the incidence argument in RESULT.md lines 21–42. For distinct shifts t<u each common pattern site s gives a different ordered increasing pair (s+t,s+u) of difference u−t. Of r+2 different counts at least r are at least two. The r selected blocks therefore have total size L≥r(r+3)/2. If d_s counts blocks through s, summing d_s(d_s−1) counts ordered intersecting block pairs with weight at most g per ordered pair, so Cauchy–Schwarz gives L²≤k(L+gr(r−1)). The function L²/(L+c) increases for L>0 and c≥0, including r=1, and substitution gives exactly the displayed rational bound. Its denominator is positive and expansion followed by inversion gives the stated O_g(1) remainder. A dyadic difference determines the smaller exponent by its 2-adic valuation, then determines the larger exponent. Substituting g=1,r=4 gives k≥98/13, ruling out six counts for k=6. Direct sampling gives 4,1,3,0,2 at the five listed shifts. The inspected verify.py and verification_output.txt are finite consistency checks, not the basis of the infinite proof.

## originality

PASS

Best-of-knowledge pass for the uniform finite inequality and its all-size square-root consequence under bounded positive-difference multiplicity. The dyadic lower witness is not credited as new; closing the upper side is elementary and is not the principal originality claim. The strongest plausibly covering cited text was not retrievable, and the limitations of the comparison are recorded below.

## value

PASS

A uniform quantitative bound from the natural additive restriction controls sampling at all arities without recurrence or acyclicity. It gives a concrete square-root constraint and a finite formula usable at small k; the elementary dyadic endpoint is an illustration rather than the only contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
