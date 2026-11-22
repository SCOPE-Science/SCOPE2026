# A sharp eight-sample mean-square barrier for Richardson stochastic dynamic mode decomposition

## Finding

**Theorem (exact moment and rare-event phases).** Let \(m\ge1\) be an integer, let \(h>0\), and let the \(m\) training sites be independent \(N(0,1)\) variables. Apply the empirical-generator, one-observable implementations of first-order stochastic dynamic mode decomposition (SDMD-1), Richardson-extrapolated SDMD (SDMD-R), and generator-Taylor SDMD-2 specified below to the Ornstein–Uhlenbeck process and observable \(\psi(x)=x^2\). Let \(Q_1,Q_R,Q_2\) denote their random one-step scalar multipliers and let \(\mathcal E_j=\|Q_j\psi-P_h\psi\|_{L^2(\rho)}^2\) be squared Koopman prediction errors. Then:

1. The empirical Gram matrix is positive almost surely, all three methods are well-defined almost surely, and the empirical Galerkin generator converges almost surely to the strictly negative population value \(-4/3\).
2. For every \(q>0\), \(\mathbb E|Q_1|^q<\infty\) exactly when \(m>2q\); \(\mathbb E|Q_R|^q<\infty\) exactly when \(m>4q\); and for \(h\ne1\), \(\mathbb E|Q_2|^q<\infty\) exactly when \(m>2q\). At \(h=1\), \(Q_2=1\) identically.
3. In particular, \(\mathbb E\mathcal E_1<\infty\) if and only if \(m\ge5\), while \(\mathbb E\mathcal E_R<\infty\) if and only if \(m\ge9\). For \(h\ne1\), \(\mathbb E\mathcal E_2<\infty\) exactly when \(m\ge5\); at \(h=1\) it is finite for every \(m\ge1\). Thus for every fixed \(h>0\), all sample counts \(5\le m\le8\) yield finite mean-squared error for SDMD-1 but infinite mean-squared error for SDMD-R, even though both use the same almost-surely invertible Gram matrix.
4. Put \(\Theta\sim\mathrm{Unif}(S^{m-1})\) and \(C_m=\mathbb E[(\sum_i\Theta_i^4)^{-m/2}]/\Gamma(m/2+1)\), a finite positive constant. The sharp large-error tails are
\[
\mathbb P(\mathcal E_R>z)\sim C_m(3h^4/4)^{m/8}z^{-m/8},\qquad
\mathbb P(\mathcal E_1>z)\sim C_m(3h^2)^{m/4}z^{-m/4}.
\]
If \(h\ne1\), the corresponding SDMD-2 tail is \(\mathbb P(\mathcal E_2>z)\sim C_m[3(h-h^2)^2]^{m/4}z^{-m/4}\). In particular, at the integer boundary sample counts \(m=8\) and \(m=4\), the respective mean-squared-error divergences are logarithmic.

## Assumptions and scope

Take the stationary scalar diffusion \(dX_t=-X_t\,dt+\sqrt2\,dW_t\), whose invariant probability law is \(\rho=N(0,1)\). Its generator is \(\mathcal A f=-xf'+f''\), and its Koopman semigroup is \(P_h f(x)=\mathbb E[f(X_h)\mid X_0=x]\). Use the one-function dictionary \(\mathcal V=\operatorname{span}\{\psi\}\) with \(\psi(x)=x^2\); the constant observable is intentionally *not* included. Draw independent training sites \(X_1,\ldots,X_m\sim\rho\), and reuse these sites for all empirical generator actions and extrapolation substeps.

Define the sample Gram and action scalars
\[
\widehat G=m^{-1}\sum_i\psi(X_i)^2,\quad
\widehat H=m^{-1}\sum_i\psi(X_i)(\mathcal A\psi)(X_i),\quad
\widehat J=m^{-1}\sum_i\psi(X_i)(\mathcal A^2\psi)(X_i).
\]
Let \(a_m=\widehat G^{-1}\widehat H\), \(b_m=\widehat G^{-1}\widehat J\), and set
\[
Q_1=1+h a_m,\quad Q_R=2(1+(h/2)a_m)^2-(1+h a_m),\quad
Q_2=1+h a_m+(h^2/2)b_m.
\]
These are the direct one-dimensional versions of SDMD-1, SDMD-R and SDMD-2 for one time step. Squared errors measure the random approximate function against the *true*, unprojected one-step Koopman image in \(L^2(\rho)\), with training randomness averaged only after taking that norm. No claim is made for generator-invariant dictionaries, regularized Gram inverses, dependent training data, or repeated-time propagation.

## Proof

First, \(\mathcal A\psi=2-2x^2\) and \(\mathcal A^2\psi=4x^2-4=-2\mathcal A\psi\). Write \(S_2=\sum_iX_i^2\) and \(S_4=\sum_iX_i^4\). Direct substitution gives
\[
\widehat G=S_4/m,\qquad a_m=-2+2S_2/S_4,\qquad b_m=-2a_m.
\]
Since independent Gaussian sites do not all vanish, \(S_4>0\) almost surely. The strong law gives \(S_2/m\to1\) and \(S_4/m\to3\), proving \(a_m\to-4/3\). Substituting \(b_m\) in the three update rules yields
\[
Q_1=1+ha_m,\qquad Q_R=1+ha_m+(h^2/2)a_m^2,\qquad Q_2=1+(h-h^2)a_m.
\]

Next use the exact polar decomposition of a standard Gaussian vector \(X=(X_i)_{i=1}^m\): \(X=R\Theta\), with \(R^2\sim\chi_m^2\), \(\Theta\) uniform on \(S^{m-1}\), and \(R\) independent of \(\Theta\). For \(m=1\) the sphere comprises two points and the same decomposition holds. The angular factor \(U=\sum_i\Theta_i^4\) obeys \(1/m\le U\le1\). Therefore
\[
a_m+2=\frac{2}{R^2U},\qquad
\mathbb E[(a_m+2)^q]
=2^q\mathbb E[U^{-q}]\,\mathbb E[(R^2)^{-q}],
\]
for all \(q>0\), with infinite values allowed. The chi-square density is proportional to \(r^{m/2-1}e^{-r/2}\) at radius-square \(r>0\); integrating near zero shows
\[
\mathbb E[(R^2)^{-q}]=2^{-q}\frac{\Gamma(m/2-q)}{\Gamma(m/2)}\quad(m>2q),
\]
and this expectation is infinite when \(m\le2q\). Since the angular factor is bounded above and below by positive constants, \(\mathbb E|a_m|^q<\infty\) exactly when \(m>2q\). A nonconstant degree-\(d\) real polynomial in \(a_m\) has finite \(q\)-th absolute moment precisely when \(m>2dq\), because its leading term dominates as \(a_m\to+\infty\). Applying this to the displayed multipliers gives the entire moment classification; the exceptional zero coefficient at \(h=1\) gives \(Q_2\equiv1\).

The exact OU transition law gives \(P_h\psi(x)=e^{-2h}x^2+1-e^{-2h}\). Using the Gaussian moments \(\int x^2\,d\rho=1\) and \(\int x^4\,d\rho=3\), any real scalar \(Q\) satisfies
\[
\|Q\psi-P_h\psi\|_{L^2(\rho)}^2
=3Q^2-2(1+2e^{-2h})Q+1+2e^{-4h}.
\]
The right side grows as \(3Q^2\) when \(|Q|\to\infty\), so its expectation is finite exactly when \(\mathbb E Q^2<\infty\). Applying \(q=2\) proves the three sharp square-risk thresholds, including equality cases.

Finally, the chi-square cumulative distribution at zero obeys \(\mathbb P(R^2\le r)\sim r^{m/2}/[2^{m/2}\Gamma(m/2+1)]\). Conditioning on \(U\), using \(a_m+2=2/(R^2U)\), and applying dominated convergence (the angular factor is bounded), gives
\[
\mathbb P(a_m>z)\sim\frac{\mathbb E[U^{-m/2}]}{\Gamma(m/2+1)}z^{-m/2}=C_m z^{-m/2}.
\]
Because the squared errors are polynomial functions of \(a_m\) with respective leading terms \((3h^4/4)a_m^4\), \(3h^2a_m^2\), and \(3(h-h^2)^2a_m^2\), elementary monotone-tail substitution yields the stated sharp constants and powers. At exponent one, integrating \(z^{-1}\) shows logarithmic divergence of the first moment. This completes the proof.

## Verification

The companion standard-library Python program `verify.py` checks the exact empirical Gram/action formulas, the identity \(b_m=-2a_m\), all three update-polynomial identities, the special \(h=1\) cancellation, the radial scaling identity, the chi-square integrability inequalities, and the exact quadratic Koopman-risk formula with rational arithmetic. Command: `python verify.py`. On the supplied test domain it prints `VERIFY_OK 78095 exact checks on 3900 finite vectors`. These finite checks test algebra and do not establish the all-sample-size moment or tail assertions, which are proved above analytically.

## Relationship to prior work

Xu's *A Second-Order Stochastic Dynamic Mode Decomposition by Richardson Extrapolation* (arXiv:2611.00793, first submitted 2026-10-31) introduces Richardson extrapolation of two empirical SDMD half steps using the same empirical generator. Its Theorem 3.3 bounds error for a prescribed matrix perturbation, Proposition 3.6 controls that perturbation on a high-probability Gram-smallness event, and Remark 3.7 extends the sampling estimate to unbounded-moment dictionaries. Its own OU example in Section 5.2 uses the five-function trigonometric dictionary \(\{1,\sin x,\cos x,\sin 2x,\cos 2x\}\), not the present one-function polynomial dictionary. The present claim isolates a **finite-data unconditional-integrability question**, rather than reproducing a convergence-rate estimate: it contrasts quadratic and linear polynomial dependence on the random inverse empirical Gram and determines exact sample thresholds and Pareto constants on a specific Ornstein–Uhlenbeck dictionary. Llamazares-Elias and collaborators (arXiv:2405.00539) study convergence and error bounds for sampled Koopman/generator approximations; their broad finite-data convergence framework is distinct from this exact one-observable tail classification. The classical Gaussian inverse-chi-square moment calculation is an ingredient, not asserted to be novel.

## Limitations

The dictionary omits constants and is not invariant under the generator; this is essential to the observed empirical random inverse effect. Gaussian iid training sites, exact generator evaluation, reuse of the *same* sample for Richardson half steps, and no Gram regularization are required. Positive or negative results cannot be transferred without further proof to bounded dictionaries, all higher-dimensional dictionaries, shared trajectories, or nonlinear multi-step stability. An almost-sure inverse exists even where the squared risk is nonintegrable; an error bound in probability or for bounded data need not contradict that fact. The findings have not received an independent mathematical audit, and exhaustive historical priority is not claimed.

## References

1. Y. Xu, *A Second-Order Stochastic Dynamic Mode Decomposition by Richardson Extrapolation*, arXiv:2611.00793 (first submitted 2026-10-31), https://arxiv.org/abs/2611.00793.
2. L. Llamazares-Elias, S. Llamazares-Elias, J. Latz, S. Klus, *Data-driven approximation of Koopman operators and generators: Convergence rates and error bounds*, arXiv:2405.00539 (first submitted 2024-05-01), https://arxiv.org/abs/2405.00539.
3. S. Klus et al., *Data-driven approximation of the Koopman generator: Model reduction, system identification, and control*, arXiv:1909.10638, https://arxiv.org/abs/1909.10638.
