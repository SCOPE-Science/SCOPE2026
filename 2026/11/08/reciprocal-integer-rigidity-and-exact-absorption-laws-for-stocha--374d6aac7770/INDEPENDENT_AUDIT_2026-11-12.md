# Independent mathematical audit

## correctness

PASS

For unbiased nearest-integer stochastic rounding on Z and q∈(0,1), if q=1/b with integer b≥2 the two possible adjacent states after any step map into the same new adjacent pair; conditional unbiasedness fixes probabilities uniquely, proving X_t in law R(n/b^t) for all n,t and varying reciprocal integer steps. Conversely, for nonreciprocal q choose m=floor(1/q), n=floor(m/q)+1; the first support is {m,m+1}, then strictly positive support {0,1,2}, unlike direct R(q²n), so t=2 necessity is universal. Nonnegative chain has absorbing zero and P(τ>t)=min(1,n/b^t); tail summation yields Eτ=floor(log_b n)+1+[n/b^floor(log_b n)]/(b−1) and a nonconstant 1-periodic phase. Independently checked rational transitions q=1/2,1/5 and counterexample q=2/3 and exact algebraic boundary; finite cases corroborate proof.

## originality

PASS

Stochastic-rounding surveys and El Arar et al. supply unbiasedness, moment error analysis and probabilistic variance bounds, not an exact all-starting-value distributional semigroup criterion or log-periodic absorption law. Resultary comparisons with finite-bit rounding and negative-slope affine contractions have different kernels. Accept best-of-knowledge, noting possible equivalent two-point linear-interpolation-kernel composition theorem outside numerical analysis.

## value

PASS

It identifies exactly when independent per-step random lattice rounding loses no distributional information relative to one rounding, which is a natural rigidity property of a Markov kernel rather than generic mean conservation. The exact absorption law and logarithmic lattice phase provide precise stopping-time information for discrete scalar decay and suggest which rounding schedules exhibit noise accumulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
