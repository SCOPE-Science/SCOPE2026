# Exact transverse-log covariance spectrum on the chaotic axis of a coupled logistic population map

## Finding
Consider the Type-2 two-population polynomial map of Lee, Chan, Im, Chan and Cheang,
\[
F(x,y)=\bigl(4x(1-x)-\mu_1xy,\;-\nu_0y(1-y)+\nu_1xy\bigr),
\]
with \(\mu_1>0\), \(\nu_1>0\), and \(0<\nu_0<\nu_1\). The predator-free axis \(y=0\) carries the fully chaotic logistic map. For \(x_0=\sin^2(\pi\theta)\), with \(\theta\) uniform on \([0,1)\), the exact **normal variational multiplier** after \(n\ge1\) iterates is
\[
D_n(\theta)=\prod_{j=0}^{n-1}\bigl(-\nu_0+\nu_1\sin^2(2^j\pi\theta)\bigr).
\]
Put \(\eta=\nu_0/\nu_1\), \(\phi=\pi^{-1}\arcsin\sqrt\eta\in(0,1/2)\), and \(B_2(t)=t^2-t+1/6\) for \(0\le t<1\), extended periodically. For every \(m\ge0\), define
\[
\Gamma_m(\phi)=\frac{\pi^2}{2^m}\left[B_2\bigl(\{(2^m+1)\phi\}\bigr)+B_2\bigl(\{(2^m-1)\phi\}\bigr)\right].
\]
Then, without taking a long-time limit, the stationary covariance and finite-horizon variance obey
\[
\operatorname{Cov}\!\left(\log|\nu_1(x_0-\eta)|,\log|\nu_1(x_m-\eta)|\right)=\Gamma_m(\phi),
\]
\[
\boxed{\operatorname{Var}(\log|D_n|)=n\Gamma_0(\phi)+2\sum_{m=1}^{n-1}(n-m)\Gamma_m(\phi).}
\]
For almost every initial \(\theta\), the transverse Lyapunov exponent is \(\lim_{n\to\infty}n^{-1}\log|D_n|=\log(\nu_1/4)\), independent of \(\nu_0\) throughout the stated interval.

At the genuinely neutral choice \(\nu_1=4\), two intrinsic zeros of the transverse multiplier have contrasting finite-time statistics. When \(\nu_0=2\), the zero is the logistic turning point \(x=1/2\), and
\[
\operatorname{Var}(\log|D_n|)=\frac{\pi^2}{12}\left(2-2^{1-n}\right)\longrightarrow\frac{\pi^2}{6}.
\]
When \(\nu_0=3\), the zero is the repelling fixed point \(x=3/4\), and
\[
\boxed{\operatorname{Var}(\log|D_n|)=\frac{\pi^2}{9}\left(3n-4+2^{2-n}\right)\sim\frac{\pi^2}{3}n.}
\]
The critical-turning-point autocorrelation is known from Anteneodo's work on finite-time Lyapunov exponents; the contribution here is the **parameterized transverse-cocycle spectrum** and the explicit contrasting fixed-point-zero case in the population map.

## Assumptions and scope
The polynomial map is considered on real phase space. Only the invariant axis \(y=0\) and its **infinitesimal normal linearization** are analyzed, not the nonlinear response of strictly positive predator populations. Because \(-\nu_0+\nu_1x\) can change sign, the linearized normal perturbation can change sign; the theorem makes no positivity, persistence or physical invasion assertion. The stationary distribution on the axis is the logistic parameter-four invariant probability, with density \([\pi\sqrt{x(1-x)}]^{-1}\) for \(0<x<1\), equivalently \(\theta\) uniform. Singular initial angles at which a multiplier vanishes form a null set. Covariance and variance are integrals against this invariant distribution; the formulas hold for every stated integer horizon.

## Proof
**1. Exact normal cocycle.** On \(y=0\), \(x_{j+1}=4x_j(1-x_j)\) and \(x_j=\sin^2(2^j\pi\theta)\). The Jacobian on this axis is upper triangular:
\[
DF(x,0)=\begin{pmatrix}4-8x&-\mu_1x\\0&-\nu_0+\nu_1x\end{pmatrix}.
\]
The quotient derivative normal to the invariant axis is the scalar lower-right entry, so its \(n\)-step product is precisely \(D_n\), independent of \(\mu_1\). This does **not** identify the normal quotient with an invariant vertical subspace of the full Jacobian.

**2. Zero mean throughout the open band.** For \(\eta=\sin^2(\pi\phi)\), the sine-difference identity gives the centered observable
\[
H_\phi(\theta):=\log\left|4\bigl(\sin^2(\pi\theta)-\eta\bigr)\right|
=\log|2\sin\pi(\theta+\phi)|+\log|2\sin\pi(\theta-\phi)|.
\]
Both summands belong to \(L^2([0,1])\) and each integrates to zero. Thus \(\mathbb E\log|\nu_1(x_j-\eta)|=\log(\nu_1/4)\). Since doubling \(\theta\mapsto2\theta\pmod1\) is ergodic and the observable is integrable, Birkhoff's theorem yields the claimed almost-everywhere exponent. The statement makes no assertion of a common exponent for exceptional periodic or precritical seeds.

**3. Exact correlations.** The classical \(L^2\) Fourier expansion
\[
\log|2\sin(\pi t)|=-\sum_{k=1}^\infty\frac{\cos(2\pi kt)}{k}
\]
gives
\[
H_\phi(\theta)=-2\sum_{k=1}^\infty\frac{\cos(2\pi k\phi)}{k}\cos(2\pi k\theta).
\]
The two-time integral of the product of Fourier modes at lags zero and \(m\) vanishes unless the first frequency equals \(2^m\) times the second. Parseval/Cauchy–Schwarz justify passage from finite Fourier sums to the \(L^2\) correlation. Hence
\[
\operatorname{Cov}(H_\phi(\theta),H_\phi(2^m\theta))
=\frac2{2^m}\sum_{k=1}^\infty\frac{\cos(2\pi 2^mk\phi)\cos(2\pi k\phi)}{k^2}.
\]
Applying \(2\cos u\cos v=\cos(u+v)+\cos(u-v)\) and the absolutely convergent Fourier identity
\[
\sum_{k=1}^\infty\frac{\cos(2\pi kt)}{k^2}=\pi^2B_2(\{t\})
\]
proves the formula for \(\Gamma_m\). Because the process is stationary, expanding the variance of its sum yields the finite-horizon identity exactly.

**4. The two geometrically selected zeros.** At \(\eta=1/2\), \(\phi=1/4\) and the Bernoulli evaluations give \(\Gamma_0=\pi^2/12\) and \(\Gamma_m=-\pi^2/(24\,2^m)\) for all \(m\ge1\). At \(\eta=3/4\), \(\phi=1/3\) and \(\Gamma_m=\pi^2/(9\,2^m)\) for every \(m\ge0\). The exact geometric identity
\[
\sum_{m=1}^{n-1}\frac{n-m}{2^m}=n-2+2^{1-n}
\]
then gives the two displayed formulas. The turning-point case is additionally a multiplicative coboundary: at \((\nu_0,\nu_1)=(2,4)\), for angles avoiding zero denominators,
\[
D_n(\theta)=(-1)^n\frac{\sin(2^{n+1}\pi\theta)}{\sin(2\pi\theta)}.
\]
For \((\nu_0,\nu_1)=(3,4)\), the zero is instead the invariant repelling prey fixed point, and its strictly positive covariance sequence yields the linear variance.

## Verification
Execute \(\texttt{python3 verify.py}\) with the standard Python library. The included checker evaluates 38 exact-rational Bernoulli coefficient identities, 12 independent truncated-Fourier correlation approximations, 36 exact finite-horizon variance identities, and 24 finite-product telescoping diagnostics. All passed in the package preparation environment. The finite computations test formulas at the specified cases; the proof above establishes the identities for all horizons and all \(0<\eta<1\).

## Relationship to prior work
Lee et al., arXiv:2301.11669, introduced precisely this Type-2 coupled logistic map (their equation (20)) and gave equilibrium multipliers and numerical bifurcation/Lyapunov diagnostics. Their inspected Sections 2.1, 2.4, 2.6 and 3 do not evaluate the stationary normal log-cocycle covariance or its full parameter family. Anteneodo, arXiv:nlin/0309065, equations (11)–(14), proved a general Fourier autocorrelation method and exactly evaluated the **standard logistic derivative** case, which, after normalization, agrees with our \(\eta=1/2\) example. That example is a comparison, not claimed new. The present model-specific Bernoulli spectrum for arbitrary displaced multiplier zero, and especially the explicit positive covariance at the logistic fixed-point zero \(\eta=3/4\), are not statements of either inspected source. General Fourier correlation methods are a substantial antecedent, and an unlocated equivalent calculation remains possible.

## Limitations
This is a stationary infinitesimal-transverse result, not nonlinear predator extinction, uniform orbitwise stability, an invariant-positive-quadrant theorem, a central limit theorem, or a classification of all possible finite-time distributions. Almost-everywhere exponent statements exclude exceptional seeds. The base-two Lyapunov normalization used in the original paper differs from the natural-log normalization here by a factor \(\log2\). The turnover at the map's turning point is already known in derivative statistics; no originality is asserted for it separately.

## References
1. W. S. Lee, H. F. Chan, K. I. Im, K. I. Chan, U. H. Cheang, *Predator Extinction arose from Chaos of the Prey: the Chaotic Behavior of a Homomorphic Two-Dimensional Logistic Map in the Form of Lotka-Volterra Equations*, arXiv:2301.11669, first public version January 27, 2023, https://arxiv.org/abs/2301.11669.
2. C. Anteneodo, *Statistics of finite-time Lyapunov exponents in the Ulam map*, arXiv:nlin/0309065, September 24, 2003, especially equations (11)–(14), https://arxiv.org/abs/nlin/0309065.
