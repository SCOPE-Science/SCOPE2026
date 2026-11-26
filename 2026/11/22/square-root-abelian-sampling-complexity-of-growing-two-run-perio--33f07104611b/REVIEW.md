# Independent mathematical audit

## correctness

PASS

Reconstructed the cyclic-multiplicity reduction in RESULT.md lines 21–34. Each vector c of nonnegative integers summing to k is realized by distinct nonnegative indices j+ℓq, 0≤ℓ<c_j, in residue j. For shift n the starting residue of its h-window is −n mod q, so all cyclic starts occur. The q window sums v_i are between 0 and k and sum to hk; p distinct integer values use at least p(p−1)/2 of this sum, proving the three upper bounds. Under k≥h, t=floor(sqrt(2hk)) is at least h, and q≥t+1 provides an actual coordinate t outside the starts and ends of the t−h+1 selected windows. The prefix c_j=floor(j/h) consumes at most t(t−1)/(2h)≤k, so c_t is a nonnegative remainder. The first window of this prefix is zero and sliding it increases its sum by c_{i+h}−c_i=1 until the last selected start, proving the full consecutive interval 0,…,t−h independently of the remainder or wrap-around windows. This includes k=h and h=1. The error from the square-root law is uniformly O(h+1) in the displayed regime, and the stated limit holds with fixed h along any allowed periods. Inspected verify.py and the stored 4,995 constructive / 168 exhaustive finite checks; these are corroborative only, not used in the universal proof.

## originality

PASS

Best-of-knowledge pass for the explicit realization of the sharp leading coefficient in the growing-period regime, not for the elementary triangular-sum bound or the general definition of complexity. Both Abelian-complexity and cyclic integer sum formulations were checked; the best available related statements do not establish this quantitative extremum.

## value

PASS

This resolves the leading-order sampling diversity of a canonical periodic binary family in an explicit regime where the period grows at least on the stated square-root scale. The lower construction shows how overlapping h-windows can attain an essentially triangular budget rather than merely invoking fixed-period boundedness or disjoint sampling, and exposes the sharp dependence on the length of the one-run.

The dated certificate retains the supplied scientific assessment, sources and limitations.
