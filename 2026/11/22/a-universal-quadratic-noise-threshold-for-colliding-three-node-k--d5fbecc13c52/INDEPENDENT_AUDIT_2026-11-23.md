# Independent mathematical audit

## correctness

PASS

The kernel mixture is strictly positive definite on distinct nodes because the component at every Q>0 is strictly positive definite. The even system gives the displayed exact threshold; the outer numerator at η=0 is a strictly positive cosh contribution plus Cov(e^(−Qd²),M_Q)≥0, since both functions decrease in Q, and η≥0 adds ηm(d). With M_Q=∫e^(−Qx²)μ(dx), directly m(0)A=−2Cov(Q,M_Q)+4E[Q²X²e^(−QX²)]>0, avoiding any need for a target moment. The second derivative of the integrand is uniformly bounded by a constant times Q, and the fourth-order expansion of k follows by dominated Taylor remainder using E[Q²]<∞. The determinant is 2Hd⁴+o(d⁴) at zero noise and 3cd²+o(d²) at η=cd²+o(d²) for c>0. The center and outer numerators respectively have leading coefficients m(0)(c−A) and m(0)(c+A/2) in d², including a zero limiting center at c=A without deciding its finite-d sign. These reproduce all stated limits and treat possibly negative thresholds. The Matérn-5/2 primitive differentiates to κ, with κ′(L)=−L(1+L)e^(−L)/3 and the inverse-gamma mixture has finite second moment. A fresh bounded numerical integration at λ=1,d=0.1 gave η_c≈0.000216563660 and noiseless w₀≈−5.528266003. The uploaded checker was read, not run; its reported groups are supplementary.

## originality

PASS

The supported distinction is the strict outer signs and sharp collision constants/regularized limits for Gaussian scale-mixture covariances and arbitrary symmetric non-point probabilities. Symmetry reduction and the corresponding pointwise formula on narrower families are not distinct novelty. The closest same-day target-mixture and rough Matérn results are credited below; date alone does not resolve priority.

## value

PASS

The theorem identifies the destabilized coordinate and sharp sign-restoration scale in a natural colliding design, with explicit coefficients for the divergent zero-noise regime and finite critical-regularization regime. The strict sign lemma is substantive for arbitrary symmetric targets without moments; it is not simply Gram-system inversion. The threshold classifies coefficients, not quadrature error or an optimal measurement-noise policy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
