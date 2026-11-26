# Independent mathematical audit

## correctness

PASS

Independently derive the identity with the uniform cut encoding, K_N=1+sum of N−1 fair independent cut bits. An occurrence beginning at unit offset a=0,...,t fixes w−1 internal bits (r−1 ones) and h additional boundary bits to one, where h=1_{a>0}+1_{a<t}. Its probability is 2^(−w+1−h), and on the event the mean of K_N increases by (2r−w−1+h)/2. Thus it contributes 2^(−w−h)(2r−w−1+h) to covariance. Summing these indicators counts overlapping occurrences without assuming independence among their events. At t=0 there is just h=0; at t≥1 there are two h=1 offsets and t−1 h=2 offsets, yielding the asserted numerator (2r−w+1)t+6r−3w−1. The frozen marked-occurrence series u^r z^w C(z,u)^2 and coefficient extraction give the same moments; at t=1 both rational coefficient formulas continue to hold. With d=2r−w the signs of d−1 and (d+1)t+3d−1 give the complete integer classification; d=−1 yields the stated nonzero constant for t≥1. In the two zero cases a positive-probability occurrence forces K_N=r or r+1 respectively, but the binomial cut count is nondegenerate. The limiting slope follows. Ran python /workspace/reproductions/check.py 5: 130918 exact word/N comparisons through N=16 by the cut-mask calculation. The frozen checker was read, not run; neither finite comparison establishes the all-N theorem.

## originality

PASS

Best-of-knowledge pass for the explicit arbitrary-exact-word, finite-N mixed covariance law and the sharp dependent-zero sign classification in unrestricted uniform compositions. The checked exact indexed covariances change both observables and conditioning, the fixed-word indexed and paper overlaps use avoidance or other statistics, and the general local-event result is asymptotic. No novelty credit is assigned to the marked-occurrence method. Coverage by a weighted full occurrence enumerator is a specific unresolved implication risk, not a conclusion from the inability to retrieve it.

## value

PASS

This is a natural finite dependence statistic for local patterns of an unrestricted composition. The full weight/length collapse despite self-overlap, exhaustive sign switch (including two dependent zero cases), and sample-size-invariant negative covariance family are independently useful exact features that an asymptotic normality or avoidance formula does not explain. Credit is for the full classification, not for introducing a new enumeration method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
