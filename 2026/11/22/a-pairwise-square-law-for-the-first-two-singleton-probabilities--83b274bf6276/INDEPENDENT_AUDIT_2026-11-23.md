# Independent mathematical audit

## correctness

PASS

Independent Poisson clocks with rates p_i preserve the iid discrete label sequence. The last first-arrival clock is unique almost surely; its density p_j exp(-p_j t) multiplies independent factors F_i(t) for at least two arrivals, or p_i t exp(-p_i t) for the other singleton. For U=1 integrate against d(-exp(-p_j t)); the lower boundary vanishes since N>=2 and F_i(0)=0, and the upper vanishes by boundedness and p_j>0. Differentiation replaces a factor by p_i² t exp(-p_i t). Each ordered U=1 product-rule term is p_i/p_j times the corresponding ordered U=2 contribution. Subtracting the U=2 contributions and summing both orientations of an unordered pair yields (p_i-p_j)² times the common kernel. The kernel is strictly positive at all t>0 and bounded above by t exp(-(p_i+p_j)t). Therefore equality holds exactly for uniform weights. At N=2 the empty-product kernel is (p_1+p_2)^(-2)=1. A separate exact rational occupancy-state and kernel comparison tested 125 weight vectors and 634 assertions; for (1,2,3), the masses are 287/600 and 71/200 and their difference is 37/300; for (1,1,1), both equal 7/18. Replay: python3 /workspace/reviews/evidence/1-coupon-check.py. This is finite corroboration, not the all-size proof. Frozen verifier inspected, not executed.

## originality

PASS

The full distribution and Poisson coefficient formulas are not new. The checked sources furnish the two atoms, but no checked result furnishes their nonuniform difference as a positive pairwise-square sum or asserts the resulting strict all-size comparison. Long's related pairwise-square dissipation applies to a different functional. This is a bounded statement about checked sources, not a priority certification.

## value

PASS

At the natural stopping time, the smallest two possible deficit masses provide a direct local test distinguishing identical coupon weights from every heterogeneous vector, in every finite dimension. The nonnegative pair decomposition identifies the cause of strictness, rather than supplying a table of coefficient evaluations. It does not assert a global mode or stochastic-order theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
