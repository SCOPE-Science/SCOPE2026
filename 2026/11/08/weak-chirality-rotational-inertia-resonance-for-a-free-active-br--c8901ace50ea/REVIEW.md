# Independent mathematical audit

## correctness

PASS

Stationary OU covariance Dr exp(−|t|/τ)/τ integrates exactly to Var(θ_t−θ_0−Ωt)=2Dr[t−τ(1−e^(−t/τ))]; Green–Kubo gives K(τ,Ω)=∫ Cτ(t) cos Ωt dt. At τ↓0 the first derivative is positive Dr²/(Dr²+Ω²). For fixed Ω≠0, Cτ′ has a single negative extremum and two integrations by parts give |K|≤2 max|Cτ′|/Ω²→0 as τ→∞; continuity ensures a finite interior global maximum. At Ω=0, Cτ increases strictly and its Gaussian-scale integral ~√(πτ/(2Dr)). Under τ=Dr x/Ω², dominated Gaussian rescaling gives |Ω|K→F(x)=√(πx/2)e^(−x/2); small-x integral and large-x integration-by-parts bounds exclude escaping maximizers, so x→1 and F(1)=√(π/(2e)). Independently checked F′ and the OU variance identity algebraically; limited numerical tests do not certify universal limit.

## originality

PASS

Best of knowledge, the entire exact chiral OU diffusivity kernel and qualitative inertial peak are ALREADY known from Scholz et al. (2018) and explicitly not claimed original. The surviving new assertion is sharp GLOBAL weak-chirality optimizer localization and universal singular coefficient, not found in the accessible material. Interacting 2024 chiral particle models and overdamped-chirality studies are different observables. Closely relevant full text could not be retrieved by arXiv/OA and authorized Oxford access was blocked; residual risk recorded, not an originality failure automatically.

## value

PASS

A singular optimization phase boundary distinguishes the zero-chirality and every finite-chirality transport regimes, including a universal exact optimum scale and divergent amplitude. This quantifies a physically motivated and mathematically nontrivial global crossover beyond a known integrable correlation kernel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
