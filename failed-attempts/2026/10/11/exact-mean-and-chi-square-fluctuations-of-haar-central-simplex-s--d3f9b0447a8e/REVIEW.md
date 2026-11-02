# Independent mathematical audit

## correctness

PASS

For every integer m>=3, a generic centroidal hyperplane intersects exactly the simplex edges joining normal coordinates with opposite signs. If K is the number of positive coordinates, N_m=K(m-K)=m²/4-(K-m/2)². A Haar normal on the zero-sum space is the direction of Y_i=Z_i-mean(Z), iid Z_i~N(0,1). Its off-diagonal correlation is -1/(m-1), so the bivariate Gaussian opposite-sign probability is arccos[-1/(m-1)]/pi and summing over C(m,2) edges yields the stated mean exactly. Expanding arcsin at 1/(m-1) yields m²/4-sigma² m+O(1/m), sigma²=1/4-1/(2pi). The source grid/Chebyshev argument correctly establishes empirical-CDF stochastic equicontinuity at the random sample mean; the independent influence representation is m^-1/2 sum [1{Z_i>0}-1/2-phi(0)Z_i]+o_p(1), with variance sigma². The iid CLT, continuous mapping and Slutsky give the two asserted chi-square limits. m=3 gives N_3=2 deterministically and the exact formula agrees. Independent Gaussian simulation m=3,4,8,32,256,1000 agreed with expectation within sample fluctuation and normalized K variance approached sigma²; finite data are corroboration only, not proof of limit. All normalization, quantifiers, genericity and boundary cases checked.

## originality

FAIL

A distinct already published result, Joint chi-square face-vector fluctuations of random central regular-simplex sections (Resultary published 2026-10-11), provides exactly the full face-vector law, exact focal vertex mean (its Eq.(4)), and joint chi-square deficits for all fixed ranks (its Eq.(2)). Setting j=0 gives the assigned vertex deficit limit and applying its exact mean gives the centered limit. The assigned m=3 boundary is elementary, while the stronger result covers m>=4. Thus every nontrivial assertion of the focused claim is explicitly stated or immediately implied; neither different title nor naming changes the mathematical coverage. Exact chronological priority within 2026-10-11 is not asserted; the documented separate full-source mathematical overlap is decisive.

## value

FAIL

A Haar-random central simplex section vertex count is intrinsically natural, and its exact expectation and chi-square scaling are meaningful invariants. However, the separately published stronger joint face-vector theorem already computes this exact mean and j=0 fluctuation law, including an explicit full proof. The present statement adds no new exact invariant, generalization, distinguished case, counterexample, or necessary structural lemma beyond that known mathematical coverage. It is an instructive specialization but not an independent valuable research contribution under the shared C/O/V standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
