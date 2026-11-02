# Independent mathematical audit

## correctness

PASS

With positive weights (1,34,37,1,1), n=5, k=3, each ordered top-three word has probability product_{t=1}^3 w_{i_t}/(74-sum_{r<t}w_{i_r}). Independently enumerated all 60 words in exact fractions: total 1; P(I_2)=10761/10804; P(I_3)=113507/113880; P(I_2 I_3)=2091527/2106780; covariance =2941/1230359520>0. This is a fully correct finite counterexample to pairwise nonpositive covariance and thus to negative association, without any extrapolation to general weights.

## originality

FAIL

FAIL: Kenneth S. Alexander's March 1989 paper states for the EXACT same successive unequal-weight sample-without-replacement design that events of inclusion of two specified individuals CAN be positively correlated. The original's abstract describes precisely the n positive weights, k successive remaining-proportional selection, and positive pairwise covariance. That directly covers the purported discovery that this design violates negative association. The particular 5-vector and tiny rational value are not shown minimal, canonical, or to improve any known quantitative boundary; an arbitrary alternate numerical witness does not restore originality of the advertised phenomenon.

## value

FAIL

FAIL: The example's only stated motivation is to disprove negative association, which Alexander (1989) already did in the same probabilistic model. No minimization of the number of items, extremal covariance, robustness interval, new phase boundary, or other mathematical reason is established for precisely (1,34,37,1,1); its exact rational arithmetic is valid but not an independently valuable new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
