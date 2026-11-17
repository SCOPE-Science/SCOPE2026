# Independent mathematical audit

## correctness

PASS

For every kappa>1, L>0 and independent centered additive noise with variance sigma², the supplied cubic AR(3) follows from delayed extrapolation y_{k-1}; matching coefficients with DREAM equation (81) supplies Schur stability, not assumed stochastic stationarity. Independently eliminated the four Yule–Walker equations and checked R=(1-b-c²-ac)/[(1+a-b+c)(1-a-b-c)(1+b-c²+ac)] by symbolic algebra and eight separate discrete Lyapunov solutions. The q→0 slow/fast expansions yield Rslow~2/q³ and Rfast~16/(7q), hence sigma² kappa^(3/2)/(8L²) and sigma²sqrt(kappa)/(7L²). The delayed-GD characteristic quadratic minimizes worst-case radius at h*=kappa²/[L(kappa+1)²]; its separate AR(2) variance tends to 5sigma²kappa/(6L²), so (3/20)sqrt(kappa) is the ratio. The unbounded assertion is analytic; eight finite Lyapunov cases are corroborative only.

## originality

PASS

The generic acceleration/noise tradeoff is prior art, but the particular exact three-state one-delay DREAM stationary variance, both endpoint constants, and comparison to its independently rate-optimal one-delay GD are not implied by the inspected older statements.

## value

PASS

An exact noise floor for a current delay-resistant accelerator is a motivated quantitative gap: deterministic sqrtκ acceleration incurs a divergent (3/20)sqrtκ stationary mean-square penalty relative to separately deterministic-rate-optimal delayed GD. The explicit slow/fast modal constants are useful for model/tuning choices; the modest two-mode, one-delay scope is stated, not disguised as a universal lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
