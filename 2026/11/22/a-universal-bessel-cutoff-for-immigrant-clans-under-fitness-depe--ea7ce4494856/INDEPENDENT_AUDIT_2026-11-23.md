# Independent mathematical audit

## correctness

PASS

For fixed interior fitness and positive R, conditioning on the last clearing age gives the stationary Poisson-family PGF. Its first immigration derivative is controlled by the integrable clearing age; taking the v-fold product yields the compound-Poisson exponent with finite total intensity ≤a/R. The one-founder mass has geometric ratio x=λ(1−e^(−gt))/(μ−λe^(−gt)), and dx/dt is λ times its positive-state prefactor. An independent limit replay therefore gives Λ_n=(a/λ)∫_0^(λ/μ) x^(n−1)[(λ−μx)/(λ(1−x))]^(R/g) dx. Set μ=1, w=g, u=n(1−x). The support becomes nw≤u≤n; the bracket before exponentiation is (1−nw/u)/(1−w) in [0,1]. Since nR→s and nw→0, its power tends to exp(−s/u) at each u>0; (1−u/n)^(n−1) is bounded by exp(−u/2) for n≥2. The upper-edge density is finite by ν<1 and the β condition, and q tends to zero there, so a/λ→1. Dominated convergence gives nΛ_n→∫_0^∞exp(−u−s/u)du=2√s K_1(2√s), with the stated two endpoint asymptotics of the profile. This proves the ordered limits under the frozen site model, not simultaneous network convergence. CHECK.py was inspected, not executed; its finite experiments are supplementary.

## originality

PASS

The distinct result is the exact joint moving-size cutoff, including its normalized kernel. The same-model Grange Eq. (32) already contains the site PGF that yields the dilute compound-Poisson representation by first-order expansion and independence; no separate priority is assigned to that mechanism or to log-series or factorial-moment formulas. The checked same-model moment and mixed-occupation results give different observables, and the catastrophe-family paper's analyzed power-law approximation does not provide the stated exact rescaled cutoff. Priority remains best of current knowledge.

## value

PASS

The crossover function determines individual large-clan intensities on the clearing scale, distinguishes the near-log-series and stretched-exponential regimes, and explains which parameters disappear under rescaling. Neither a fixed-fitness tail nor finitely many integrated moment thresholds describes this crossover. The model's independently factorized scope and the ordered limits are essential to this interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
