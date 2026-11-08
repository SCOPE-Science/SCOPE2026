# Exact mean-square energy growth from independent random steps in symplectic Euler

## Finding

For the unit-frequency harmonic oscillator, every fixed symplectic-Euler stepsize strictly between zero and two has a bounded numerical trajectory. In contrast, independently sampling the stepsizes from **any non-point-mass probability distribution supported in \((0,2)\)** makes the expected physical energy grow exponentially from every nonzero deterministic initial condition. The exact exponential factor is the Perron spectral radius of an explicitly defined three-dimensional second-moment operator and is strictly greater than one.

For equally likely stepsizes \(h-\varepsilon\) and \(h+\varepsilon\), where \(0<\varepsilon<\min\{h,2-h\}\), the factor satisfies the sharp weak-jitter expansion

\[
\rho(h,\varepsilon)=1+\frac{2h^2}{4-h^2}\,\varepsilon^2+O_h(\varepsilon^4),\qquad \varepsilon\longrightarrow0.
\]

For instance, the individually stable stepsizes \(3/4\) and \(5/4\) have a common mean-square energy growth factor \(1.0414937063628626\ldots\) per update.

## Assumptions and scope

Let \(q'=p\), \(p'=-q\), with physical energy \(E(q,p)=(q^2+p^2)/2\). Kick-then-drift symplectic Euler is defined by

\[
 p_{j+1}=p_j-H_jq_j,\qquad q_{j+1}=q_j+H_jp_{j+1},
 \qquad x_{j+1}=M(H_j)x_j,
\]

\[
 x_j=(q_j,p_j)^\top,\qquad M(z)=\begin{pmatrix}1-z^2&z\\-z&1\end{pmatrix}.
\]

Assume the steps \((H_j)_{j\ge0}\) are independent and identically distributed, independent of a fixed nonzero \(x_0\), and obey \(\mathbb P(0<H_j<2)=1\). No smoothness or finite-support assumption is imposed. The law is *nondegenerate* if \(H_j\) is not almost surely constant. Since \(H_j\in(0,2)\), all moments needed below exist.

Define the positive-map action on symmetric \(2\times2\) matrices

\[
 \mathcal T(X)=\mathbb E[M(H_0)XM(H_0)^\top],\quad
 \rho=\operatorname{spr}(\mathcal T),
\]

where \(\operatorname{spr}\) denotes spectral radius. The conclusion is that \(\rho>1\) for a nondegenerate law and that for each \(x_0\ne0\) there exist \(0<c(x_0)\le C(x_0)<\infty\), independent of \(j\), with

\[
 c(x_0)\rho^j\le\mathbb E[E(x_j)]\le C(x_0)\rho^j
 \quad\text{for all integers }j\ge0.
\]

For a point-mass law \(H_j=h\in(0,2)\), the spectral radius is exactly one and trajectories remain bounded. The theorem describes **mean-square / expected-energy growth**, not an almost-sure Lyapunov exponent.

## Proof

**1. Fixed-step ellipticity and invariant metrics.** For every \(z\in(0,2)\), \(\det M(z)=1\), \(\operatorname{tr}M(z)=2-z^2\in(-2,2)\). Thus \(M(z)\) has distinct unit-modulus nonreal eigenvalues; in particular it has no real invariant line. Direct multiplication yields

\[
 G_z=\begin{pmatrix}1&-z/2\\-z/2&1\end{pmatrix}\succ0,
 \qquad M(z)^\top G_zM(z)=G_z.
\]

In this elliptic regime, all positive-definite invariant quadratic forms are positive scalar multiples of \(G_z\): conjugate \(M(z)\) using \(G_z^{1/2}\) to a nontrivial planar rotation, whose invariant symmetric forms are scalar. Distinct values of \(z\) give nonproportional normalized matrices \(G_z\).

**2. Positive Perron eigenmatrices.** The map \(\mathcal T\) preserves the closed, pointed, generating cone of positive-semidefinite symmetric matrices. Finite-dimensional cone Perron–Frobenius theory supplies a nonzero \(S\succeq0\) such that \(\mathcal T(S)=\rho S\), \(\rho>0\). This \(S\) is positive definite: if it had rank one, every positive summand \(M(H)SM(H)^\top\) would need to have the same one-dimensional range as \(S\), almost surely. That would give a real invariant line for almost every elliptic \(M(H)\), which is impossible. The analogous argument applied to \(\mathcal T^*(W)=\mathbb E[M(H)^\top W M(H)]\) produces a positive-definite \(W\) satisfying \(\mathcal T^*(W)=\rho W\).

**3. Strict growth for any nontrivial law.** Since every \(M(H)\) has determinant one, strict concavity of \(\log\det\) on positive-definite matrices gives

\[
 \log\det(\rho S)
 =\log\det\mathbb E[M(H)SM(H)^\top]
 \ge\mathbb E\log\det[M(H)SM(H)^\top]
 =\log\det S.
\]

It follows that \(\rho\ge1\). If equality held, strict equality in Jensen's inequality would force \(M(H)SM(H)^\top=S\) almost surely. Consequently the inverse quadratic form \(S^{-1}\) would be invariant under every stepsize in the essential support; step 1 shows this can occur only if the stepsize is almost surely constant. For a nondegenerate distribution, therefore, \(\rho>1\).

**4. Exact exponential rate for every initial vector.** Independence yields the covariance recursion \(\mathbb E[x_{j+1}x_{j+1}^\top]=\mathcal T(\mathbb E[x_jx_j^\top])\). By duality,

\[
 \mathbb E[x_j^\top W x_j]
 =\rho^j x_0^\top W x_0.
\]

Since \(W\succ0\), its smallest and largest eigenvalues compare \(x^\top Wx\) with \(\|x\|_2^2\) uniformly. This proves the two-sided expected-energy inequalities. For deterministic \(H=h\), the invariant form \(G_h\) bounds every iterate and \(\rho=1\).

**5. Exact binary-jitter transfer and sharp coefficient.** Let \(H=h\pm\varepsilon\) with equal probabilities, and write a symmetric covariance matrix in coordinates \((X_{11},X_{12},X_{22})\). Setting \(u=h^2+\varepsilon^2\) and \(v=h^4+6h^2\varepsilon^2+\varepsilon^4\), direct expansion gives

\[
 \mathsf T_{h,\varepsilon}=\begin{pmatrix}
 1-2u+v&2h(1-h^2-3\varepsilon^2)&u\\
 h(h^2+3\varepsilon^2-1)&1-2u&h\\
 u&-2h&1
 \end{pmatrix}.
\]

As an independent exact positivity certificate,

\[
 \det(I-\mathsf T_{h,\varepsilon})
 =-2\varepsilon^2(h-\varepsilon)^2(h+\varepsilon)^2<0.
\]

At \(\varepsilon=0\), the eigenvalue one of \(\mathsf T_{h,0}\) is simple: the remaining eigenvalues are \(e^{\pm2i\theta}\), where \(\cos\theta=1-h^2/2\) and \(\theta\in(0,\pi)\). Choose \(S=G_h^{-1}\) as its right eigenmatrix and \(G_h\) as the left eigenmatrix. An exact calculation gives

\[
 \operatorname{tr}\left(G_h[\mathcal T_{h,\varepsilon}(S)-S]\right)
 =\frac{4\varepsilon^2(h^2+\varepsilon^2)}{4-h^2},\qquad
 \operatorname{tr}(G_hS)=2.
\]

Analytic perturbation of the simple eigenvalue, noting that the transfer matrix is an even polynomial in \(\varepsilon\), yields

\[
 \rho(h,\varepsilon)=1+\frac{2h^2}{4-h^2}\varepsilon^2+O_h(\varepsilon^4).
\]

The eigenvalue is the Perron eigenvalue for sufficiently small jitter by continuity. In the example \(h=1\), \(\varepsilon=1/4\), the exact characteristic polynomial is

\[
 \lambda^3-\frac{33}{256}\lambda^2-\frac{441}{2048}\lambda-\frac{49}{64},
\]

or, equivalently, \(2048\lambda^3-264\lambda^2-441\lambda-1568\), whose spectral-radius root is \(1.0414937063628626\ldots\).

## Verification

The standalone script `verify_symplectic_jitter.py` uses exact symbolic algebra and independent finite-horizon enumeration to check the invariant quadratic form, the matrix transfer, the determinant identity, perturbation numerator, the example cubic, and sampled spectral radii. It also independently enumerates all binary step sequences for selected initial states and horizons. Run with Python, SymPy 1.14.0 and NumPy 2.3.5:

```bash
python verify_symplectic_jitter.py
```

The delivered `verification_output.txt` records **75 passed checks**. These finite tests and symbolic identities support the analytical argument; they do not replace the Perron, strict-concavity and perturbation proofs for infinitely many time steps and arbitrary nondegenerate distributions.

## Relationship to prior work

Abdulle and Garegnani [1] develop randomized time-step integrators, show the geometric properties of each map, and establish energy accuracy on step-dependent long but finite time scales under a variance-scaling hypothesis (Theorem 6 and Remarks 12–13). The present result concerns a fixed, nonzero stepsize distribution and the exact **infinite-horizon** second-moment exponent; it is compatible with that finite-time theorem and does not claim the random-step construction itself.

Richardson and Finn [2] explain how deterministic, periodically varying steps cause parametric instabilities in symplectic schemes, including oscillator examples. Their resonance mechanism does not state iid-jitter instability for every nonconstant law or an exact iid covariance rate. Melbø and Higham [3] investigate long-time second moments of **additive-noise stochastic oscillators**, rather than randomizing the deterministic integrator's timestep. Moshchuk and Khasminskii [4] analyze moment Lyapunov exponents of continuous-time randomly perturbed conservative systems. These works motivate comparisons but do not, on the inspected evidence, supply the exact discrete transfer and weak-jitter coefficient proved here.

The underlying Perron theory, strict log-determinant concavity, and harmonic-oscillator symplectic Euler invariant are standard tools. The contribution is their exact integration into the global iid-random-step instability law and the sharp discrete leading coefficient. No universal originality guarantee is claimed.

## Limitations

The theorem concerns a single linear oscillator, the kick-then-drift symplectic Euler scheme, independent identically distributed steps strictly inside its deterministic stability interval, and **annealed** (expected-energy) growth. It does not imply that every sample path diverges exponentially, nor does it directly cover stochastic differential equations, higher-order symplectic methods, state-dependent or correlated step choices, or noise with support beyond \((0,2)\). The small-jitter asymptotics hold for each fixed \(h\in(0,2)\); the remainder is not uniform as \(h\to2\). A potentially relevant specialist paper on continuous-time moment exponents [4] could not be read in full, leaving residual bibliographic uncertainty.

## References

[1] A. Abdulle and G. Garegnani, *Random time step probabilistic methods for uncertainty quantification in chaotic and geometric numerical integration*, first publicly posted 2018-01-04, arXiv:1801.01340, https://arxiv.org/abs/1801.01340 (particularly Sections 2 and 7).

[2] A. S. Richardson and J. M. Finn, *Symplectic integrators with adaptive time steps*, first publicly posted 2011-08-01, arXiv:1108.0322, https://arxiv.org/abs/1108.0322 (particularly Section 2).

[3] A. H. Strømmen Melbø and D. J. Higham, *Numerical simulation of a linear stochastic oscillator with additive noise*, Applied Numerical Mathematics 51 (2004), 89–99, https://doi.org/10.1016/j.apnum.2004.02.003; https://strathprints.strath.ac.uk/164/ (abstract available).

[4] N. Moshchuk and R. Khasminskii, *Moment Lyapunov exponent and stability index for linear conservative system with small random perturbation*, SIAM Journal on Applied Mathematics 58 (1998), 245–256, https://doi.org/10.1137/S003613999529589X (abstract available).
