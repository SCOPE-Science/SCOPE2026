# A sharp sign phase diagram for stationary position kurtosis of a trapped inertial run-and-tumble particle

## Finding

The stationary position of a one-dimensional inertial run-and-tumble particle in a harmonic trap can have **positive** fourth cumulant although its propulsion force is bounded and takes only two values. There is an exact, global sign classification in the two dimensionless mechanical/activity parameters. In particular, positive excess kurtosis is impossible unless the propulsion-direction decorrelation rate exceeds **eight-thirds of the mechanical amplitude damping rate**; above this threshold, it occurs exactly beyond one explicit trap-stiffness boundary. The curve of zero fourth cumulant still consists of compactly supported, non-Gaussian stationary distributions.

Let
\[
\beta=\frac{\gamma}{2m},\quad q=\frac{\mu/m}{\beta^2},\quad z=\frac{2/\tau_a}{\beta},\quad
\mathcal K=\frac{\mathbb E[X^4]}{(\mathbb E[X^2])^2}-3.
\]
All mechanical parameters, propulsion magnitude and switching time are strictly positive. Define positive-coefficient polynomials
\[
B(z)=26z^3+224z^2+476z+264,\qquad
H(z)=3z^5+48z^4+288z^3+816z^2+1104z+576
\]
and
\[
P(q,z)=(9z-24)q^2-B(z)q-H(z).
\]
Then the exact stationary excess kurtosis is
\[
\boxed{\mathcal K=\frac{3qP(q,z)}{(z+2)^2(q+3)(z^2+6z+9q)(z^2+6z+q+8)}.}
\]
All denominator factors are strictly positive. Thus \(\mathcal K<0\) for every \(q>0\) if \(0<z\le 8/3\). For each \(z>8/3\), define
\[
q_*(z)=\frac{B(z)+\sqrt{B(z)^2+4(9z-24)H(z)}}{2(9z-24)}.
\]
This is the unique positive boundary and
\[
\boxed{\mathcal K<0\ \text{for }q<q_*(z),\qquad
\mathcal K=0\ \text{for }q=q_*(z),\qquad
\mathcal K>0\ \text{for }q>q_*(z).}
\]
Both strict signs occur for the same oscillator when the switching rate changes: with \(q=1000\), the values \(z=1,4,100\) give negative, positive and negative fourth cumulants respectively. At \(q=1000,z=4\), the exact excess kurtosis is \(590125/14847409>0\). This is a sharp, non-Gaussian *position* kurtosis classification, not a kinetic-energy or velocity classification.

## Assumptions and scope

For \(m,\gamma,\mu,a_0,\tau_a>0\), let \(\sigma_t\in\{-1,1\}\) flip symmetrically at rate \(1/\tau_a\). Consider the unique stationary solution of
\[
\dot X=V,\qquad m\dot V=-\gamma V-\mu X+a_0\sigma_t.
\]
There is no additive Gaussian thermal noise. The mechanical drift is exponentially stable. The stationary position is centered, non-degenerate, and bounded because it is a stable linear convolution of bounded forcing. In particular, it cannot be Gaussian, even when its fourth cumulant vanishes. The statement concerns exactly the stationary one-time fourth cumulant, not the sign of a time correlation, the appearance of specific density peaks, or a thermodynamic phase transition.

Put \(\beta=\gamma/(2m)\), \(f=a_0/m\), and use scaled time \(s=\beta t\), position \(Y=\beta^2X/f\), velocity \(W=\beta V/f\), and telegraph sign \(S=\sigma\). In these variables,
\[
\frac{dY}{ds}=W,\qquad \frac{dW}{ds}=-2W-qY+S,
\]
where \(q=(\mu/m)/\beta^2>0\) and the sign has decay \(\mathbb E[S(0)S(s)]=e^{-z|s|}\) with \(z=(2/\tau_a)/\beta>0\). The sign of the fourth cumulant and the normalized excess kurtosis are unchanged by this rescaling.

## Proof

**1. Existence and moment hierarchy.** Since the roots of \(u^2+2u+q\) have negative real parts for every \(q>0\), the driven oscillator has a unique stationary causal solution. Its position and velocity are bounded linear filters of \(S\), hence all polynomial moments exist and generator identities are legitimate. Symmetry \((Y,W,S)\mapsto(-Y,-W,-S)\) makes all odd-total-degree moments vanish. Write
\[
M_{ijh}=\mathbb E[Y^iW^jS^h],\qquad i,j\in\mathbb Z_{\ge0},\quad h\in\{0,1\}.
\]
The generator, including sign flips at rate \(z/2\), applied to a monomial yields the exact stationary recurrence
\[
\boxed{0=iM_{i-1,j+1,h}-2jM_{ijh}-qjM_{i+1,j-1,h}+jM_{i,j-1,1-h}-hzM_{ijh}.}\tag{1}
\]
Terms with zero coefficient are omitted; the base is \(M_{000}=1\). The finite linear systems formed by (1) in even total degrees two and four determine all moments needed here uniquely: they are restrictions of the stationary polynomial generator and all its nonconstant eigenvalues have strictly negative real parts, since its diagonal-degree action consists of sums of stable oscillator eigenvalues, shifted by \(-z\) on odd sign sectors.

**2. Exact second and fourth moments.** Solving the degree-two system, followed by the degree-four system, gives
\[
\mathbb E[Y^2]=\frac{z+2}{2q(z^2+2z+q)}
\]
and
\[
\mathbb E[Y^4]=
\frac{3N(q,z)}{4q^2(q+3)(z^2+2z+q)(z^2+6z+9q)(z^2+6z+q+8)},
\]
where the polynomial numerator is
\[
\begin{aligned}
N(q,z)={}&qz^4+3z^4+11qz^3+42z^3+9q^2z^2+53qz^2+204z^2\\
&+45q^2z+136qz+408z+12q^2+132q+288.
\end{aligned}
\]
The accompanying standalone checker constructs the entire degree-four polynomial generator from (1) over exact rationals, solves its fifteen-moment even-parity system symbolically, and verifies both identities by exact polynomial simplification. A direct subtraction of \(3(\mathbb E[Y^2])^2\) produces
\[
\kappa_4(Y)=\frac{3P(q,z)}{4q(q+3)(z^2+2z+q)^2(z^2+6z+9q)(z^2+6z+q+8)},
\]
with the stated \(P\). Dividing by \((\mathbb E[Y^2])^2\) proves the exact formula for \(\mathcal K\). This is an identity for **every** \(q,z>0\), rather than an asymptotic expansion or numerical extrapolation.

**3. Global phase diagram.** Since all coefficients of \(B,H\) are positive, \(P(q,z)<0\) for all \(q>0\) whenever \(0<z\le8/3\). If \(z>8/3\), the quadratic \(P(q,z)\) has positive leading coefficient, strictly negative constant term, and exactly one positive and one negative real root. Its unique positive root is \(q_*(z)\) by the quadratic formula. The sign of this upward-opening quadratic is negative before that root and positive after it, proving all three cases and sharpness. For the rational witness \((q,z)=(1000,4)\), exact substitution gives \(P=4532160>0\) and \(\mathcal K=590125/14847409\). At \(z=1\) and \(100\), the same \(q=1000\) gives negative values of \(P\). Finally, the bounded, nonconstant stationary position variable cannot have a Gaussian distribution: a non-degenerate Gaussian has unbounded support. Thus the zero-kurtosis boundary is *not* a Gaussianity boundary. \(\square\)

## Verification

The self-contained Python 3 checker at `checks/verify.py` uses exact SymPy arithmetic for the full finite stationary polynomial generator and its symbolic solution; it also verifies the two rationally separated signs and tests the closed formulas against a numerically solved stationary generator at a grid of positive parameters. Run `python checks/verify.py` after extracting the files to a common folder. The proof, not finite diagnostics, establishes the global sign classification. The environment must have `sympy` and `numpy`; neither a proprietary solver nor a remote certificate is used.

## Relationship to prior work

Dutta, Kundu, Sabhapandit and Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension* (2024), establish this stochastic model and its exact stationary second moments, finite-support boundaries, and selected approximate marginal distributions. Their full text, including Sections III–V and Appendix B, does **not** present an exact stationary position fourth-moment expression or a fourth-cumulant sign classification. Those established second moments are not claimed as new. Caprini and Marini Bettolo Marconi, *Inertial self-propelled particles* (2020), give exact two-time **second-order** correlations for a linearly confined, Gaussian active Ornstein–Uhlenbeck drive; Gaussianity forces its stationary position fourth cumulant to vanish and so does not cover the dichotomous-force result. Patel and Chaudhuri, *Exact moments for trapped active particles* (2024), study rotational-diffusion active Brownian particles in dimensions two and three, not a one-dimensional telegraph sign; their Section 5 classifies a different position kurtosis and reports nonpositive displacement kurtosis in that model. Their general moment-generator technique is credited, rather than treated as new. Pawula, *Dichotomous-noise-driven oscillators* (1987), states a general expression for output moments of higher-order dichotomous-noise filters, so it supplies potentially relevant general machinery, but the accessible abstract gives no sharp stationary position-kurtosis sign diagram for the inertial harmonic trap. Its complete paper was not accessible for full-text comparison; this is a substantive residual novelty risk. Searches for equivalent stochastic-switching oscillator fourth moments and exact kurtosis sign conditions did not locate a covering primary theorem; this does not prove publication priority.

## Limitations

Only the no-thermal-noise, one-dimensional stationary harmonic model with symmetric binary switching and strictly positive rates is classified. At a fixed amplitude of independent thermal Gaussian noise, fourth cumulants are unchanged but **normalized** excess kurtosis and the second moment change; that extension is not asserted here. A vanishing fourth cumulant does not imply a Gaussian position law, and positive kurtosis does not by itself prove any specific modality of the density. Statistical precision from finite samples, physical phase transitions, and arbitrary switching protocols are outside scope. Independent mathematical review and a comprehensive publication-priority search have not been performed. Related unindexed fourth-moment results remain a residual novelty risk.

## References

1. D. Dutta, A. Kundu, S. Sabhapandit, U. Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension*, arXiv:2406.06120 (first public 2024-06-10), https://arxiv.org/html/2406.06120v2 and https://arxiv.org/abs/2406.06120.
2. L. Caprini, U. Marini Bettolo Marconi, *Inertial self-propelled particles*, arXiv:2009.14032 (2020), https://arxiv.org/abs/2009.14032, especially Section IV.2 and Appendix C.
3. R. F. Pawula, *Dichotomous-noise-driven oscillators*, Physical Review A 35, 3102–3106 (1987), https://doi.org/10.1103/PhysRevA.35.3102; abstract inspected, full text not accessible.
4. M. Patel, D. Chaudhuri, *Exact moments for trapped active particles: inertial impact on steady-state properties and re-entrance*, arXiv:2404.01107 (2024), https://arxiv.org/html/2404.01107v1, especially Sections 2 and 5.
