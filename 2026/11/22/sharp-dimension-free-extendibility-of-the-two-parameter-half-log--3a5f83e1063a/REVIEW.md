# Scientific review

## Correctness — PASS

The original normalized multiplicative generator has the exact inverse \(\Psi^{-1}(z)=\theta^{-1}\log[(1+\alpha qz)/(1-qz)]\) with \(q=(e^\theta-1)/(e^\theta+\alpha)\). For \(0<\alpha\le1\), the two convergent logarithmic series yield an explicit positive probability law on positive integers; direct mixture construction establishes every-dimensional copula validity. For \(\alpha>1\), the coefficient of \(e^{-2t}\) is negative. Shifting beyond the signed series' convergence threshold, uniqueness of finite signed Laplace transforms contradicts any positive Bernstein representation, so some finite dimension fails by the classical Archimedean criterion. Rational arithmetic additionally demonstrates an explicit trivariate failure. The supplied script was run and passed numerical identities and an exact rational obstruction. Analytical uniqueness and generator theorems, not the finite diagnostic tests, prove the infinite statement.

## Originality — PASS, with historical-priority qualification

The 2023 half-logistic paper, especially its Section 4, supplies the bivariate generator and a Frank limit but does not give the every-dimensional boundary, discrete frailty weights, parity support, or a trivariate obstruction. The 2009 McNeil--Nešlehová theorem supplies the *general* necessary-and-sufficient completely-monotone-generator criterion, so that part is prior theory, not a new claim. The 2020 generator paper gives bivariate construction methods without the present family-specific complete-monotonicity calculation. Searches for multivariate half-logistic copulas, frailty weights, and log-ratio generator aliases located no directly dominating result. An incomplete literature index cannot establish universal novelty; independent priority checking remains appropriate.

## Value — PASS

A bivariate Archimedean family does not automatically yield valid higher-dimensional copulas. The sharp parameter-independent boundary tells users exactly when the *same associative family* can model arbitrary numbers of variables. The positive discrete mixing weights give an explicit exchangeable stochastic construction and simulation algorithm, while the odd-only support at the half-logistic boundary and a concrete failure already in dimension three show structural behavior invisible from bivariate concordance and tail coefficients. The classification is a natural modeling feasibility question rather than a new name or routine moment computation.

## Closest sources and limitations

- Alzaid--Alhadlaq (2023 online), https://doi.org/10.3390/math12010101: source bivariate family, Section 4, and dependence calculations.
- McNeil--Nešlehová (2009), https://arxiv.org/abs/0908.3750: original general d-monotonicity and completely-monotone-generator theorems, used as prior theory.
- Alhadlaq--Alzaid (2020), https://doi.org/10.3390/sym12122108: predecessor generator methods.

This result does not characterize every finite dimension separately, nor does it exclude non-Archimedean extensions of the original bivariate margins. The Laplace-mixture proof applies to positive finite \(\alpha,\theta\); \(\theta=0\) is handled only as a limiting independence case. The initial literature and prior-record search cannot prove historical uniqueness.

Self-review: passed. Independent audit: not yet performed.
