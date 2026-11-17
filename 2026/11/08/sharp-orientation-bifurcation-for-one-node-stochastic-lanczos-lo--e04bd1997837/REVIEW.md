# Independent mathematical audit

## correctness

PASS

Exact first-node 3x3 rank-one spiked estimator is 3 log(1+α(ε·u)^2), with α=θ/3. Sign-pair product P=((1+α)^2−4α²q)^2+64α³r, q=sum xixj, r=prod xi, xi=ui². At fixed q>1/4 minimizing r gives two equal larger coordinates; P(z) derivative 4α²(3z−1)(1+αz)(3αz−2α+1) has no interior minimum. Endpoints P2=(1+2α)^2 and P3=(1+α/3)^3(1+3α) cross only at θ*=5√10−14; q<=1/4 already bounded by P2. Jensen gives axis-only maximum 3log(1+α) and strictly positive expected logdet bias. Independently checked symbolic four-sign identity and derivative/endpoints plus 1200 rational/real orientation checks; analytic proof handles continuum.

## originality

PASS

Best-of-knowledge original exact 3D one-node SLQ orientation bifurcation: a natural fixed-spectrum expectation problem has competing support-two and support-three minimizers crossing once at θ*=5√10−14 and coordinate-vector maximizers. The original method and the separate 2D mean-squared benchmark do not imply that sharp three-coordinate transition.

## value

PASS

Fixed spectrum and rank-one spike are natural tests for orientation sensitivity of one-node stochastic Lanczos estimates. The exact support-pattern bifurcation and equality cases identify a mathematically nontrivial orientation effect that method definitions and Jensen bounds alone cannot give; narrow dimensions do not invalidate its standalone interest.

The dated certificate retains the supplied scientific assessment, sources and limitations.
