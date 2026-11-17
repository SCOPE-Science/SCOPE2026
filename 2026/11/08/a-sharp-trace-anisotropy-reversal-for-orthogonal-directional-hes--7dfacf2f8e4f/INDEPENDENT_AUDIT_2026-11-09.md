# Independent mathematical audit

## correctness

PASS

For exact quadratic oracle q(u)=uᵀHu, the calibrated M(u)=d q(u)((d+2)uuᵀ−I)/2 is unbiased by spherical fourth moments. Directly computing E[q(u)q(v)] over distinct Haar columns yields ((d+1)t²−2s)/(d(d−1)(d+2)). Hence the centered Frobenius cross-covariance is C=[(−d²+2d+4)/(2(d−1)(d+2))]s−[d(d+1)(d+4)/(4(d−1)(d+2))]t²; risk difference is (k−1)C/k. Sign: d=2 iff t²/s<2/9 and d=3 iff <1/42 for worse frame; d>=4 always improvement. PSD H has t²>=s and improves. Independent exact 2D integration of H=diag(1,−1) gives iid risk 3/2 versus orth risk 2. Equalities checked; no claim about nonquadratic/noisy oracle.

## originality

PASS

Existing incremental rank-one Hessian and two-frame mixed-direction estimators have different update rules. Their variance bounds do not subsume the exact finite-k calibrated one-step directional-curvature estimator and its saddle-dependent switch. Specialist inaccessible original remains residual originality risk.

## value

PASS

An exactly unbiased, evaluation-budget-matched zeroth-order Hessian estimator has a sharp dimension-two/three orthogonality failure and a dimension-four universal improvement cutoff, explaining when a widespread antithetic design helps/hurts curvature inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
