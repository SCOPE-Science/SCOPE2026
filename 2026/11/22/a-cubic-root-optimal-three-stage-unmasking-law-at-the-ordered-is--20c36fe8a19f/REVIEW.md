# Independent mathematical audit

## correctness

PASS

For the repaired direction, cancellation of mask weights and source-law averaging give Eq. (1); conditional entropy with two boundaries is a_k+a_l-a_(k+l), and the finite-end correction per site vanishes, including zero previous density. Geometric scaling, exponentially bounded rescaled tails and Gamma(1,1)/Gamma(2,1) log moments give F_r(u) ~ r/(2u) when r/u tends to zero and u tends to zero. Strict subadditivity gives a positive limit for nonzero bounded r/u, while r/u tending to infinity gives log 2. A cost O(r^(2/3)) forces p=O(r^(2/3)); it first forces q to zero, then q bounded below on the r^(1/3) scale by the final-round term, and then forces p and q into compact rescaled ranges by the second term. The three rescaled leading terms have constant product log(2)/4, and equalizing them gives exactly the stated constants for every global minimizer. Inspected the frozen checker’s finite likelihood direction and tests, without executing it; the limiting proof is analytic.

## originality

PASS

Known representations and optimization frameworks are credited. The closest exact all-fixed-round result does contain every constant and quantifier but explicitly cites this exact three-round record as its antecedent. It is evidence of subsequent coverage, not evidence of antecedent priority against this record. No earlier equivalent found in the examined material; not a global priority determination.

## value

PASS

Three rounds are a natural smallest budget with two optimizable intermediate densities. The theorem determines both seeding scales and sharp optimum for the actual fixed-round objective where a many-step geodesic is not valid, unlike a trial schedule that supplies only an upper bound. It makes no output-KL or practical training claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
