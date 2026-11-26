# Independent mathematical audit

## correctness

FAIL

The stability interval, variance, unique median rule and factor-two limit are correct. The frozen Finding also states an incorrect boundary claim: its exterior regimes include q_c=q_a or q_c=q_b, but at either equality both distinct endpoints attain the same worst variance. For example a=1/4 and b=3/4 give q_a=q_c=−1/2, which is stable; h[2(1+β)−h]=3/16 at both endpoints. Single-endpoint control holds for strict exterior inequalities when a<b. To reconstruct the rest, Jury's test is |β|<1, h>0 and h<2(1+β), and the stable causal covariance solves the two scalar Yule–Walker identities, giving the displayed V. Time-independent covariance does not require a stationary innovation law; arbitrary finite-variance initial transients and their cross terms decay. The positive variance denominator is concave in h after factors independent of h are removed. With x=1+β the derivative in x has sign x²−h, and V(b)≥V(a) holds for β≤q_c if a<b. Thus the decreasing/increasing pieces select the median uniquely. q_c is above the common lower stability bound by a/2; q_b is strictly between that bound and 1, and q_a is chosen only when it is stable. If a=b, use the single-mode minimizer. For b=ca and a sufficiently small, both optima use the a-mode, signed at √a−1 and nonnegative at zero, yielding the stated ratio. Inspected RESULT.md, VERIFICATION.md and verify.py. The script compares a bounded scalar optimizer, covariance solves and finite samples but does not separately check uniqueness away from the optimizer as claimed in RESULT.md line 48. No frozen code was executed.

## originality

FAIL

The modal formula and the exact worst-endpoint objective are already published for constant stabilizing parameters (including signed momentum). The particular closed minimizer and small-curvature ratio were not located verbatim, but both follow mechanically by differentiating the two known rational branches and comparing their single crossing; in the small-curvature regime the second comparison is just the unconstrained and clipped optima of the same known single-mode formula. The precedents that trade off rate and noise with a varying step are not themselves the fixed-step optimum.

## value

FAIL

Fixed stepsize and worst-mode noise are motivated engineering settings, and the sign effect can be useful to note. But once the published exact endpoint formula is used, the entire claim is two one-variable stationary points, one linear tie and a substitution for the cost. The boundary correction would not leave a distinct nonmechanical finding to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
