# Independent mathematical audit

## correctness

PASS

The first component of T²(A,B)=(A,B) forces AB=−B, and the second becomes B−B², so the exact period-two pairs are precisely those with AB=−B, B²=0 and B≠0. The proof uses the stated multiplication order and also works in characteristic two: the first coordinate still changes when B≠0. The next matrix in the second coordinate is −B, so the rank count is a point count and division by two is correct. A rank-r square-zero map is equivalent to a flag im B=U⊆K=ker B together with an isomorphism V/K→U; choices of A extend −I on U and give q^{n(n−r)}. This also shows there is no such pair in dimension one. Expanding the product leaves exponent n²+nr−2r²=9n²/8−2(r−n/4)². For r=m+k and n=4m+s, the sums of the defects of the numerator factors are O_q(q^{r−n}+q^{2r−n})→0, which justifies product convergence despite the growing number of factors. The product multiplier is uniformly bounded by P_q⁻¹, so a summable discrete Gaussian dominates the zero-extended rank counts, proving both normalized limits and the orbit prefactor. The final sentence about a typical square-zero matrix is read in its stated conditional ensemble: B from a uniform two-cycle point. A uniformly sampled square-zero matrix by itself instead has leading rank exponent 2r(n−r), centered near n/2. The frozen script tests T² only after filtering B for square-zero and rank; it does not literally iterate all pairs as described in RESULT.md, and its limit check samples a central mass, not the entire law. As an independent unfiltered computation, /workspace/branches/replay_vieta_gf4.py checked all 65,536 ordered pairs in M₂(F₄) and found 240 exact period-two points, all rank one (120 orbits), in agreement with the formula. No packaged checker was executed.

## originality

PASS

Best-of-knowledge pass for the rank-refined dynamic census and fixed-field four-phase limit, with the orbit normalization. The same ring map, qualitative two-cycle existence criterion and exact square-zero rank stratum are prior content and are not credited as new. The distinction is the conditional orbit weight by rank and resulting quarter-centered limit, not the Gaussian-binomial ingredients in isolation.

## value

PASS

The theorem quantifies the period-two structure of a natural graph on full matrix algebras, where qualitative existence and the square-zero condition do not indicate the typical cycle rank. The extension multiplicity shifts the center from roughly n/2 to n/4, with order-one fluctuations and an explicit four-phase normalization for the orbit total. That weighting phenomenon and all-rank census provide useful information beyond rederiving the flag table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
