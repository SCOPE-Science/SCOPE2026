# Strictly concave refresh-rate response of a two-state Pareto exponent

## Finding
Consider the stationary tail exponent \(\alpha(\mu)\) of the two-diffusivity, mean-field multiplicative-growth model described below. For every positive redistribution rate \(J\), distinct positive diffusivities \(0<d_\ell<d_h\), and low-diffusivity redraw probability \(0<\beta<1\), its dependence on Poisson redraw rate \(\mu>0\) is **strictly increasing and strictly concave**, and the exponent uniquely identifies the redraw rate if these other parameters are known.

Let \(\bar d=\beta d_\ell+(1-\beta)d_h\), and let \(q=\alpha-1\). On the exact domain
\[
\frac{J}{d_h}<q<\frac{J}{\bar d},
\]
the inverse function is
\[
\boxed{\mu=G(q):=\frac{(1+q)(J-d_\ell q)(d_h q-J)}{J-\bar d q}.}
\]
In particular \(G'(q)>0\), \(G''(q)>0\), and \(\alpha'(\mu)>0\), \(\alpha''(\mu)<0\) for every \(\mu>0\). The sharp endpoint laws are
\[
\alpha(\mu)=1+\frac{J}{d_h}+\frac{\beta}{J+d_h}\mu+O(\mu^2),\qquad \mu\downarrow0,
\]
\[
\alpha(\mu)=1+\frac{J}{\bar d}-\frac{K}{\mu}+O(\mu^{-2}),\qquad \mu\to\infty,
\]
where
\[
\boxed{K=\frac{(1+J/\bar d)J^2\beta(1-\beta)(d_h-d_\ell)^2}{\bar d^{3}}>0.}
\]
Thus the initial refresh sensitivity is independent of the low-diffusivity value, while the leading fast-refresh deficit is proportional to the diffusivity variance. Global concavity also yields the sharp tangent envelope
\[
0<\alpha(\mu)-\left(1+\frac{J}{d_h}\right)<\frac{\beta}{J+d_h}\mu \quad(\mu>0).
\]
The above statements concern the Pareto exponent selected by the source's stationary-tail determinant, not finite-population empirical estimators.

## Assumptions and scope
The relative-size process follows the Itô stochastic differential equation \(dX_t=J(1-X_t)dt+\sqrt{2D_t}\,X_t\,dB_t\), where the diffusivity \(D_t\) is independently redrawn at rate \(\mu\) from \(d_\ell\) with probability \(\beta\) and \(d_h\) otherwise. All five parameters satisfy \(J>0\), \(0<d_\ell<d_h\), \(0<\beta<1\), \(\mu>0\). The stochastic model and its stationary-tail selection via the smallest determinant root above one are established in the motivating preprint. The mathematical claim here is a global shape theorem for that explicitly specified root. It assumes the large-population mean-field regime, not finite interaction graphs or common-mode diffusivity.

## Proof
The known two-channel stationary-tail analysis yields \(F_i(\alpha)=\alpha[J-(\alpha-1)d_i]\) and the exact determinant equation
\[
F_\ell(\alpha)F_h(\alpha)+\mu\alpha[J-(\alpha-1)\bar d]=0.
\]
For \(q=\alpha-1\), divide by \(\alpha>0\) and isolate \(\mu\). This produces the stated \(G(q)\). Write \(a=J/d_h\), \(b=J/\bar d\). Because \(d_\ell<\bar d<d_h\), all factors of \(G(q)\) are positive for \(a<q<b\); moreover \(G(q)\to0\) at \(a\) and \(G(q)\to\infty\) at \(b\). In this interval,
\[
\frac{G'(q)}{G(q)}=\frac1{1+q}-\frac{d_\ell}{J-d_\ell q}+\frac{d_h}{d_hq-J}+\frac{\bar d}{J-\bar d q}>0.
\]
Indeed the first and third terms are positive and the final term strictly exceeds \(d_\ell/(J-d_\ell q)\), since \(d\mapsto d/(J-dq)\) increases strictly when its denominator is positive. Thus \(G\) is a bijection from \((a,b)\) to \((0,\infty)\), and its inverse defines the unique root on the physical interval. No further root below it can occur: for \(1<\alpha\le1+a\), every factor in the original determinant is nonnegative and the refresh contribution is positive. Thus this root is exactly the physical first root above unity.

For curvature, let \(P(q)=(1+q)(J-d_\ell q)(d_hq-J)\). Division of this cubic by \(J-\bar d q\) gives a quadratic polynomial of leading coefficient \(d_\ell d_h/\bar d\) and a simple-pole remainder
\[
\frac{R}{J-\bar d q},\qquad
R=P(J/\bar d)=\frac{(1+J/\bar d)J^2(\bar d-d_\ell)(d_h-\bar d)}{\bar d^2}>0.
\]
Consequently, throughout the entire physical interval,
\[
\boxed{G''(q)=\frac{2d_\ell d_h}{\bar d}+\frac{2\bar d^2 R}{(J-\bar d q)^3}>0.}
\]
Inverse differentiation gives \(\alpha'(\mu)=1/G'(q)>0\) and \(\alpha''(\mu)=-G''(q)/G'(q)^3<0\), where \(q=G^{-1}(\mu)\). This proves strict global concavity, rather than inferring it from plotted values or finite samples.

At \(q=a\), the derivative of the numerator is \((1+a)(J-d_\ell a)d_h\), and the denominator is \(J-\bar d a\). Their ratio is \(G'(a)=(J+d_h)/\beta\). The inverse-function expansion at this nonzero derivative proves the small-\(\mu\) law. At \(q=b\), \(G(q)\sim P(b)/[\bar d(b-q)]\); hence \(b-q\sim K/\mu\) with \(K=P(b)/\bar d\). Substituting \(\bar d-d_\ell=(1-\beta)(d_h-d_\ell)\) and \(d_h-\bar d=\beta(d_h-d_\ell)\) gives the displayed \(K\); the rational function yields the stronger \(O(\mu^{-2})\) remainder. Finally strict concavity and the tangent slope at zero imply the strict global tangent envelope. These steps hold for all stated real parameter values, not only the rational test samples.

## Verification
The accompanying standard-library Python program `verification/check_inverse.py` uses exact rational arithmetic. Run `python3 verification/check_inverse.py` from the extracted package root. It checks the determinant substitution, the independent quotient-rule and partial-fraction expressions for curvature, positivity, and both endpoint coefficients in 485 reproducible parameter cases, including near-endpoint points. These checks are computational cross-checks of identities; the proofs above establish the universal quantified assertions.

For example, \(J=1\), \(d_\ell=0.12\), \(d_h=1.10\), \(\beta=0.72\) gives \(\bar d=0.3944\), with the exponent ranging strictly from \(1+1/1.10\) toward \(1+1/0.3944\), but never reaching the latter for any finite refresh rate.

## Relationship to prior work
Arutkin and Vallée (2026, Section III.2, equations 27–39) derive the determinant equation, prove the bounds separating the slow- and fast-refresh values, and plot the exponent against refresh rate. Those ingredients and the stochastic derivation are not claimed here. Beare and Toda (2022, Proposition 5(iv) and Appendix B) give general first-order comparative statics showing that greater persistence can reduce Markov multiplicative-model Pareto exponents under a row/column condition. Therefore **monotonic response by itself is not claimed as an original general phenomenon**. The present added claim is the explicit model-specific inverse calibration, its strict global curvature with a positive pole decomposition, and the exact two endpoint sensitivity constants. The previous first-order results and the determinant alone do not state those strict curvature and coefficient laws; deriving them requires the present calculation.

## Limitations
This does not assert a universal concavity theorem for arbitrary Markov modulators, unbounded diffusivities, finite agent populations, heterogeneous exchange graphs, or common shocks. It does not infer microscopic transition rates from an observed exponent without independent knowledge of the other parameters and a valid stationary-tail model. The known determinant already makes numerical inversion possible; the contribution is its complete global calibration geometry. An earlier unindexed specialization of general spectral-perturbation theory could imply the curvature result; publication priority has not been independently audited. The model's stationary-tail existence/selection is inherited from its cited derivation, not newly proved from scratch here.

## References
1. M. Arutkin and A. Vallée, *Diffusing diffusivity selects Pareto tail exponent in random growth with redistribution* (2026), arXiv:2605.19464, first submitted 19 May 2026, https://arxiv.org/abs/2605.19464.
2. B. K. Beare and A. A. Toda, *Determination of Pareto Exponents in Economic Models Driven by Markov Multiplicative Processes*, Econometrica **90** (2022), 1811–1833, https://doi.org/10.3982/ECTA17984.
