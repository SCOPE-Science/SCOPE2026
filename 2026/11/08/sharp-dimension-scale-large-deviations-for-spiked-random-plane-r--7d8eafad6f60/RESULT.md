# Sharp dimension-scale large deviations for spiked random-plane Rayleigh–Ritz ascent

## Finding

For rank-one-spiked positive-semidefinite eigenproblems, exactly optimized independent random-plane Rayleigh–Ritz steps have a sharp **dimension-proportional iteration reliability law**. Fix any real \(c>0\), put \(k_d=\lfloor cd\rfloor\), and write \(\varepsilon_k\) for the largest-eigenvalue Rayleigh gap. Then

\[
Y_d=-\log\left(\frac{\varepsilon_{k_d}}{\varepsilon_0}\right)
\]

satisfies a full large-deviation principle with speed \(d\) and good rate function

\[
I_c(s)=
\begin{cases}
\frac12\left(s-c-c\log\frac{s}{c}\right),&s>0,\\
+\infty,&s\le0.
\end{cases}
\]

In particular, for every \(s>c\), respectively \(0<s<c\), the exact exponential success and failure probabilities obey

\[
\lim_{d\to\infty}\frac1d\log\Pr\{\varepsilon_{k_d}\le e^{-s}\varepsilon_0\}=-I_c(s),\qquad s>c,
\]

\[
\lim_{d\to\infty}\frac1d\log\Pr\{\varepsilon_{k_d}\ge e^{-s}\varepsilon_0\}=-I_c(s),\qquad 0<s<c.
\]

The rate is strictly positive except at the typical improvement \(s=c\). This identifies the exact high-dimensional rare-event cost of outperforming or missing a prescribed multiplicative error reduction at linearly many iterations.

## Assumptions and scope

For every integer \(d\ge3\), let \(u\in\mathbb R^d\) be a unit vector, \(\lambda_\perp\ge0\), \(\Delta>0\), and let the symmetric positive-semidefinite Gram matrix be

\[
H_d=\lambda_\perp I_d+\Delta uu^\mathsf T.
\]

It is the Gram matrix of some real forward operator, and has top eigenvalue \(\lambda_\perp+\Delta\) with a simple leading eigenspace. Begin at any deterministic unit vector \(v_0\) with

\[
0<\varepsilon_0=(\lambda_\perp+\Delta)-v_0^\mathsf TH_dv_0\le\Delta.
\]

At each iteration independently sample \(x_k\) uniformly on the unit sphere of the Euclidean tangent space \(v_k^\perp\), then choose an exact maximizer

\[
v_{k+1}\in\operatorname*{argmax}_{\substack{z\in\operatorname{span}\{v_k,x_k\}\\\|z\|_2=1}}z^\mathsf TH_dz.
\]

Set \(\varepsilon_k=\lambda_\perp+\Delta-v_k^\mathsf TH_dv_k\). Sampling is fresh at every step. The assertion holds for arbitrary deterministic starts of positive gap and is independent of \(\lambda_\perp\), \(\Delta\), and the spike orientation. In the limit \(d\to\infty\), these parameters and the initial vector may vary with dimension as long as the same assumptions hold.

## Proof

**Step 1: The one-step law.** Set \(\alpha_k=u^\mathsf Tv_k\), \(p_k=(u-\alpha_kv_k)/(1-\alpha_k^2)^{1/2}\) whenever the gap is positive. The projection of \(u\) on the random plane has squared norm

\[
\alpha_k^2+(1-\alpha_k^2)(p_k^\mathsf Tx_k)^2.
\]

Since maximizing the Rayleigh quotient of \(H_d\) is equivalent to maximizing squared overlap with \(u\), the exact Ritz update therefore satisfies

\[
\frac{\varepsilon_{k+1}}{\varepsilon_k}=1-(p_k^\mathsf Tx_k)^2.
\]

Conditional on the entire past, \(p_k\) is a fixed unit tangent vector and \(x_k\) is uniform on a sphere in a space of dimension \(d-1\). The usual Gaussian normalization of a Haar-spherical vector yields

\[
(p_k^\mathsf Tx_k)^2\sim\mathrm{Beta}\left(\frac12,\frac{d-2}{2}\right),\quad
W_k=\frac{\varepsilon_{k+1}}{\varepsilon_k}\sim\mathrm{Beta}\left(a_d,\frac12\right),\quad a_d=\frac{d-2}{2}.
\]

This conditional distribution is independent of the past and does not depend on the position or earlier random choices. Consequently the factors \((W_k)\) are independent and identically distributed. In dimension at least three, all are strictly between zero and one almost surely; hence every finite-step gap remains positive. The independent-factor identity is the distributional input, not the new large-deviation conclusion.

**Step 2: Finite-dimensional moment control.** For every \(q>-a_d\) and integer \(k\ge0\), the Beta integral gives

\[
\mathbb E\left[\left(\frac{\varepsilon_k}{\varepsilon_0}\right)^q\right]
=\left[\frac{\Gamma(a_d+q)\Gamma(a_d+\frac12)}{\Gamma(a_d)\Gamma(a_d+\frac12+q)}\right]^k.
\]

In particular \(\mathbb E[\varepsilon_k/\varepsilon_0]=((d-2)/(d-1))^k\), in agreement with the sharp expected contraction already computed in the motivating paper. At each fixed dimension the strong law for \(\log W_k\) also gives

\[
\lim_{k\to\infty}\frac1k\log\left(\frac{\varepsilon_k}{\varepsilon_0}\right)
=\psi(a_d)-\psi\left(a_d+\frac12\right)\quad\text{almost surely},
\]

where \(\psi\) is the logarithmic derivative of the gamma function. At \(d=3\), this is \(-2\log2\), whereas \(\log\mathbb E[\varepsilon_k/\varepsilon_0]/k=-\log2\). The different exponents distinguish typical from expected decay.

**Step 3: Dimension-scale cumulants.** For fixed \(c>0\), write \(k_d=\lfloor cd\rfloor\), \(Y_d=-\sum_{j=0}^{k_d-1}\log W_j\), and for a fixed \(\theta<1/2\) consider

\[
\Lambda_d(\theta)=\frac1d\log\mathbb E[e^{\theta dY_d}]
=\frac{k_d}{d}\log\left[
\frac{\Gamma(a_d-\theta d)\Gamma(a_d+\frac12)}
{\Gamma(a_d)\Gamma(a_d+\frac12-\theta d)}\right].
\]

The gamma-ratio asymptotic \(\Gamma(t+\frac12)/\Gamma(t)\sim\sqrt t\) as \(t\to\infty\), applied to \(t=a_d\) and \(t=a_d-\theta d\), yields

\[
\Lambda_d(\theta)\longrightarrow
\Lambda_c(\theta)=-\frac c2\log(1-2\theta),\qquad\theta<\frac12.
\]

For every fixed \(\theta\ge1/2\), the corresponding negative Beta moment is infinite for all sufficiently large dimensions. The limiting cumulant is differentiable for every \(\theta<1/2\), satisfies \(\Lambda_c'(\theta)=c/(1-2\theta)\), and its slope ranges from zero to infinity over that interval. These properties give a full large-deviation principle through exponential tilting and exponential tightness, as detailed next.

**Step 4: Matched upper and lower estimates.** For any \(s>0\), select the unique tilt

\[
\theta_s=\frac12\left(1-\frac cs\right)<\frac12,
\qquad\Lambda_c'(\theta_s)=s.
\]

The Chernoff inequality provides the upper exponential estimate on the side of \(c\) containing \(s\). For the matching local lower estimate, tilt the law of \(Y_d\) by the density \(e^{d\theta_sY_d-d\Lambda_d(\theta_s)}\). Differentiating the displayed gamma-ratio expression, using the asymptotic expansions of the digamma and trigamma functions, shows that under this tilted law

\[
\mathbb E_{\theta_s}Y_d\to s,\qquad
\operatorname{Var}_{\theta_s}(Y_d)=\frac{2c}{d(1-2\theta_s)^2}+o(d^{-1}).
\]

Thus any fixed neighborhood of \(s\) has tilted probability tending to one. Undoing the tilt establishes its original probability's lower logarithmic exponent \(-\theta_ss+\Lambda_c(\theta_s)\), after shrinking the neighborhood. Chernoff estimates at positive and negative tilts provide exponential tightness and upper bounds for arbitrary closed sets; finite covers provide the compact-set upper bound. The matching local lower bounds give the open-set lower bound. Hence the full large-deviation principle holds with rate

\[
I_c(s)=\sup_{\theta<1/2}\{\theta s-\Lambda_c(\theta)\}
=\frac{s-c-c\log(s/c)}2\quad(s>0).
\]

It is infinite at \(s\le0\): all realizations have \(Y_d>0\), and \(I_c(s)\to+\infty\) as \(s\downarrow0\). The rate tends to infinity also as \(s\to\infty\), so its level sets are compact. Since it decreases strictly on \((0,c)\) and increases strictly on \((c,\infty)\), the stated two one-sided tail exponents follow with no loss from taking half-lines.

## Verification

The accompanying standalone \(\texttt{verify.py}\) uses independently solved exact two-dimensional Ritz eigenproblems to check 320 sampled one-step identities across dimensions \(3,4,7,20\); compares twelve Beta moments with their gamma-function values; and checks twelve scaled-cumulant and Legendre-transform identities. Running it with Python, NumPy and SciPy prints \(\texttt{VERIFY\_OK}\). These finite checks test implementations and normalization, while the distributional and large-deviation assertions are proved above.

## Relationship to prior work

Bresch and Melnyk (2026), Example 2.4, derive the rank-one-spike Ritz ascent identity and the exact **expected** contraction factor. Their Proposition 2.5 separately bounds a first-entry-time tail using spherical-cap probabilities and an incomplete Beta function. The geometric one-step Beta calculation here is implicit in those ingredients and is not claimed as an independently new method. The additional claim is the exact joint dimension-and-iteration large-deviation rate and the resulting sharp probabilities on both sides of the typical reduction, not implied by an expectation bound or by the paper's general geometric first-entry upper bounds.

The earlier operator-norm algorithm of Bresch, Lorenz, Schneppe and Winkler (2024) gives almost-sure convergence, and the generalized-Rayleigh study of Bresch, Melnyk, Schoen and Steidl (2025) analyzes a broader algorithm with sublinear guarantees, not the displayed spiked high-dimensional probability rate. Standard Cramér and spherical-coordinate results underpin the argument; their generic statements alone do not identify the exact algorithm-specific probability without the specialized Ritz factor law.

## Limitations

The exact result requires a single rank-one spectral spike, isotropic independent tangent directions, exact plane maximization, real Euclidean geometry, and exact arithmetic. It is not an exact rare-event law for arbitrary nondegenerate spectra, other random search distributions, finite precision, or noisy objective evaluations. The large-deviation assertion is for \(k_d/d\to c\) with fixed positive \(c\), not for every joint dimension-iteration scaling. The source's distributional ingredients mean the mathematical advance is specifically the sharp large-deviation reliability classification. A complete historical-priority survey remains open.

## References

- J. Bresch and O. Melnyk, *Stochastic Rayleigh–Ritz Ascent: Global Linear Convergence under a Spectral Gap*, arXiv:2610.42071v1 (first public 2026-10-30). In particular Algorithm (2), Example 2.4 and Proposition 2.5. https://arxiv.org/abs/2610.42071
- J. Bresch, D. A. Lorenz, F. Schneppe and M. Winkler, *Matrix-free stochastic calculation of operator norms without using adjoints*, arXiv:2410.08297v1 (2024). https://arxiv.org/abs/2410.08297
- J. Bresch, O. Melnyk, M. Schoen and G. Steidl, *Stochastic Zeroth-Order Method for Computing Generalized Rayleigh Quotients*, arXiv:2512.05520v1 (2025). https://arxiv.org/abs/2512.05520
- P. Frankl and H. Maehara, *Some geometric applications of the beta distribution*, Ann. Inst. Statist. Math. **42** (1990), 463–474; standard spherical-coordinate Beta law.
