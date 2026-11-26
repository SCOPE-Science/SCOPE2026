# Independent mathematical audit

## correctness

PASS

At step t the conditional mean of the recruiter depth is the current mean depth A_(t−1); a_t=1/(t−1+1/m) is the fraction of vertices just born. Updating the depth mean and second raw moment gives expected drift a_t and a_t(1+2A_(t−1)), respectively. Thus centered average depth is a martingale; the expected within-tree variance q_t yields V_t−V_(t−1)=a_t²q_t and q_(t+1)=(1−a_t²)q_t+a_t(1−a_t). Conditioning D_j on the whole tree at time i gives 1+A_i plus a deterministic sum, so Cov(D_i,D_j)=V_(i−1)+a_iq_i for every j>i. Substituting the recursions and a_(i+1)=a_i/(1+a_i) cancels the q_i coefficient, leaving a_i a_(i+1)(1−a_i). D_2 is deterministic. Summation gives the nonnegative finite law and its strictly positive increments, and partial fractions and a 1/r²+O(r^−3) tail give L_m and the coefficient 1 of 1/i. For c≤1/4 the integral form of g shows strict decrease in its argument because x(1−e^(−u/x)) increases; the exact lower bound at 5/4 gives f′(c)>0. This leaves only m=1..4. I reproduced the exact rational K=30 interval separation and derivative inequality, the reported decimal values to their stated precision, and all 75 off-diagonal covariances for m=1..5 and steps 2..7 by enumerating finite recruiter-vertex choices; replay python3 /workspace/branches/independent_checks.py 4. The supplied CHECK.py was inspected, not run.

## originality

PASS

The distinct substantive result is the exact off-diagonal birth-index law, its independence of the later index, its 1/i correction and the globally proved integer optimum. The scalar function L_m is not new as an aggregate variance coefficient after normalization: the motivating paper effectively gives m²L_m. That prior result should be credited, not claimed as a newly computed total-path-length coefficient. The inspected prior results do not give the full indexed covariance or mechanically give the global optimum.

## value

PASS

The exact indexed covariance answers a natural dependence question not resolved by marginal depths or the total variance. Invariance under any increase of the later birth time and a persistent positive limit despite diverging single-batch depth variance describe the structure of shared history. Analytic optimization shows a genuine nonmonotonicity in the normalized two-point scale with a strict maximum at three, not just an observed best entry in a table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
