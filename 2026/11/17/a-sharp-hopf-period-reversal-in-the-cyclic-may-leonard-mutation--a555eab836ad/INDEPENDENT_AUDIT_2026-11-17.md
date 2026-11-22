# Independent mathematical audit

## correctness

PASS

The frozen RESULT.md specifies the original three-species quadratic ODE with α,β>0, α+β>2, α≠β and mutation μ_H=λ/(3σ), λ=(α+β−2)/2, σ=2λ+3, w=√3(β−α)/2. Verified the invertible original-time complex/stable-mode transform U=x+iy, z, with exact equations U′=(3δ+iw/σ)U+(λ−iw)conj(U)^2+[−(σ+3)/2+iw]Uz, z′=−z−σz²+2λ|U|², δ=μ_H−μ. The nonzero Hopf frequency, stable eigenvalue −1, second-harmonic coefficient i(λ−iw)/(3w/σ) and slaved mean 2λr² yield the fundamental cubic with real part −λ(σ+3)<0: supercritical attracting small cycle for δ>0. The imaginary cubic determines T/T_H=1+[2σ/(λ(σ+3))][3−λ+σλ²/w²]δ+o(δ), T_H=2πσ/|w|; sign of signed frequency was treated consistently for both signs of w. Positivity of α,β is |w|<√3(λ+1), so negative slope is possible exactly when λ³−6λ²−15λ−9>0. Derivative factor 3(λ−5)(λ+1) proves a unique positive root λ*=8.0123119705... . Independent exact rational spot checks at λ=10,w=16 and 37/2 yield 2921/8320>0 and −8809/177970<0, and original CHECK.py has directly checked transformed population equations and harmonic coefficient formulas. The analytic Hopf theorem, not finite integrations, establishes the branch. The zero-slope locus is only first-order neutral.

## originality

PASS

The directly relevant 2022/2023 Jaramillo–Mrad–Stepien primary text presents the identical linearly mutated May–Leonard model, its coexistence Hopf threshold and cycle stability, but its inspected Hopf/cylindrical analysis does not supply the signed original-physical-time derivative, its feasibility cubic, or two feasible opposite-slope branches. The classical unmutated May–Leonard system and the balanced or spatial variants have different assumptions. Standard Hopf normal-form theory supplies a calculation method, not this explicit model-specific sign phase diagram. Resultary semantic query recovered this assigned record itself plus distinct models, no stronger same-model formula. Best-of-knowledge originality survives with unindexed-coefficient risks.

## value

PASS

The physical period is a natural experimentally observable invariant independent of cycle existence and orbital stability. The sharp positive-competition threshold separates a regime where mutation reduction must lengthen all locally born oscillations from one admitting both signs at the same competition sum and Hopf point. The model-specific frequency drift and positivity boundary resolve a meaningful parameter-response question, not merely restate the known Hopf surface.

The dated certificate retains the supplied scientific assessment, sources and limitations.
