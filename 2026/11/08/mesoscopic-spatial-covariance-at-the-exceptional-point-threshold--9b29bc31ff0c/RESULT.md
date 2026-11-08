# Mesoscopic spatial covariance at the exceptional-point threshold of a noisy directed chain

## Finding
Consider an open one-way Ornstein–Uhlenbeck chain with fixed independent noise strength. Its finite-dimensional relaxation eigenvalues are all strictly negative, but its stationary covariance exhibits a dimension-dependent transition. The result here is the **complete critical finite-size covariance kernel**, including its detuning and spatial dependence.

Fix \(D>0\). For each \(N\ge1\), take independent standard Brownian motions \(W_1,\ldots,W_N\) and the unique stationary centered solution of
\[
 dX_i(t)=\bigl(-\kappa_N X_i(t)+\mathbf 1_{\{i<N\}}X_{i+1}(t)\bigr)\,dt+\sqrt{2D}\,dW_i(t),\qquad 1\le i\le N.
\]
For a fixed real detuning \(\zeta\), take \(\kappa_N=1+\zeta/N\), for all sufficiently large \(N\) so that \(\kappa_N>0\). For arbitrary fixed \(p\ge1\) and \(y_1,\ldots,y_p\in[0,\infty)\), define the observation sites \(i_a(N)=1+\lfloor y_a\sqrt N\rfloor\). Then the *stationary* Gaussian vector satisfies
\[
 \bigl(N^{-1/4}X_{i_a(N)}\bigr)_{a=1}^{p}\ \Longrightarrow\ \mathcal N_p(0,\mathcal K_\zeta),
 \quad (\mathcal K_\zeta)_{ab}=K_\zeta(y_a,y_b),
\]
where
\[
 \boxed{K_\zeta(y,z)=\frac D{\sqrt\pi}\int_0^1u^{-1/2}
 \exp\!\left(-2\zeta u-\frac{(y-z)^2}{4u}\right)\,du.}
\]
The integrand is assigned its limiting value at \(u=0\), where the integral is understood as an improper integral. This gives a nontrivial spatial coherence length of order \(\sqrt N\) and a stationary standard-deviation scale of order \(N^{1/4}\), even though the finite drift matrix has the constant eigenvalue \(-\kappa_N\) with multiplicity \(N\).

At exact criticality \(\zeta=0\), the normalized limiting correlation at mesoscopic separation \(s=|y-z|\) is the explicit positive function
\[
 \boxed{\rho(s)=\exp(-s^2/4)-\frac{\sqrt\pi\,s}{2}\operatorname{erfc}(s/2).}
\]
In particular, \(\rho(0)=1\), \(0<\rho(s)<1\) for \(s>0\), and \(\rho(s)\to0\) as \(s\to\infty\). For fixed microscopic separation the limiting correlation is instead one, hence the \(\sqrt N\) spatial scale is necessary to see nontrivial decorrelation within this critical window.

## Assumptions and scope
The sites form an open feedforward chain, not a periodic ring. Coupling from \(i+1\) to \(i\) has coefficient one and there is no reverse coupling. White noises are independent with common variance intensity \(2D\). The process is first placed in its unique finite-\(N\) stationary law; \(N\to\infty\) is then taken. The spatial coordinates \(y_a\), detuning \(\zeta\), dimension \(p\), and noise strength \(D\) are fixed as \(N\to\infty\). The formula does not claim uniformity in growing \(y_a\), nor interchange of limits for a genuinely infinite chain.

For arbitrary fixed \(N\), \(\kappa>0\), and \(1\le i\le j\le N\), the exact covariance is
\[
 \boxed{C_{ij}^{(N)}(\kappa)=\frac D\kappa\sum_{q=0}^{N-j}
 \frac{\binom{2q+j-i}{q}}{(2\kappa)^{2q+j-i}},\qquad C_{ji}^{(N)}=C_{ij}^{(N)}.}
\]
This exact identity also supplies an independently checkable finite-size definition of every quantity in the limit.

## Proof
**Stationarity and the finite formula.** Let \(J\) be the \(N\)-by-\(N\) shift with entries \(J_{i,i+1}=1\) and all others zero. The drift matrix is \(A=-\kappa I+J\). Since \(J^N=0\), the spectrum of \(A\) consists only of \(-\kappa\), so it is Hurwitz for every \(\kappa>0\) even though it is nonnormal and non-diagonalizable when \(N>1\). Its unique stationary Gaussian covariance is
\[
 C^{(N)}=2D\int_0^\infty e^{At}e^{A^{\mathsf T}t}\,dt.
\]
For \(i\le j\), the entries of the first exponential are \((e^{At})_{ik}=e^{-\kappa t}t^{k-i}/(k-i)!\) when \(k\ge i\), and zero otherwise. Therefore
\[
 C_{ij}^{(N)}=2D\sum_{k=j}^N\frac1{(k-i)!(k-j)!}
 \int_0^\infty e^{-2\kappa t}t^{2k-i-j}\,dt.
\]
Evaluating the gamma integral and substituting \(q=k-j\), \(d=j-i\), yields the displayed exact binomial sum. No asymptotic assertion is needed for this identity. Equivalently, its entries obey the stationary Lyapunov recursion
\[
 2\kappa C_{ij}^{(N)}=C_{i+1,j}^{(N)}+C_{i,j+1}^{(N)}+2D\mathbf 1_{\{i=j\}},
\]
with zero values beyond the right boundary \(N\).

**Uniform interior local limit.** Put \(d_N=|i_a(N)-i_b(N)|\) and \(m_N=N-\max(i_a(N),i_b(N))\). Then \(d_N/\sqrt N\to s=|y_a-y_b|\) and \(m_N/N\to1\). Define
\[
 p(q,d)=2^{-(2q+d)}\binom{2q+d}{q}.
\]
Stirling's formula applied uniformly for \(q/N\in[\varepsilon,1]\), with any fixed \(\varepsilon>0\) and \(d=O(\sqrt N)\), gives
\[
 \sqrt N\,p(q,d_N) = \frac{1}{\sqrt{\pi(q/N)}}
 \exp\!\left(-\frac{s^2}{4(q/N)}\right)+o(1),
\]
where the error is uniform over that interval. Indeed, \(p(q,d)\) is the mass at an offset \(d/2\) from the center of a binomial variable with \(2q+d\) trials; the binomial local central limit calculation has variance asymptotic to \(q/2\), giving exactly \(\exp(-d^2/(4q))\) and prefactor \((\pi q)^{-1/2}\).

**Control of the singular endpoint and detuning.** Uniformly in integers \(q,d\ge0\), the binomial mass satisfies \(p(q,d)\le C(q+1)^{-1/2}\) for an absolute constant \(C\), by the universal maximal-binomial-mass bound. Since \(\kappa_N=1+\zeta/N\), for all sufficiently large \(N\),
\[
 \sup_{0\le q\le N}\kappa_N^{-(2q+d_N+1)}\le e^{2|\zeta|+o(1)}.
\]
Thus the contribution of \(0\le q<\varepsilon N\) to \(N^{-1/2}C_{i_a i_b}^{(N)}\) is bounded by a constant times \(\sqrt\varepsilon+N^{-1/2}\), including the case \(d_N=0\). On the remaining interval, \(\kappa_N^{-(2q+d_N+1)}\to e^{-2\zeta(q/N)}\) uniformly and the preceding local limit converts the normalized sum into a Riemann integral. Letting \(\varepsilon\downarrow0\) proves the covariance-kernel limit.

Every finite vector is exactly Gaussian, so convergence of all entries of its covariance matrix proves the stated finite-dimensional weak convergence. Positive semidefiniteness of \(K_\zeta\) follows automatically as a limit of covariance matrices; alternatively, its integral representation is a positive combination of Gaussian spatial kernels.

**Closed critical profile.** At \(\zeta=0\), \(K_0(y,y)=2D/\sqrt\pi\). The substitution \(u=v^{-2}\) or integration by parts gives, for \(s\ge0\),
\[
 \int_0^1u^{-1/2}e^{-s^2/(4u)}\,du
 =2e^{-s^2/4}-s\sqrt\pi\operatorname{erfc}(s/2).
\]
Division by the diagonal variance yields \(\rho(s)\). Strict decrease from one and positivity are immediate from the integral before integration by parts, and convergence to zero follows by dominated convergence. This completes the proof.

## Verification
The accompanying standalone file `VERIFY.py` uses only the Python standard library. It independently solves the exact stationary Lyapunov recursion in rational arithmetic and compares every covariance entry against the finite binomial formula for multiple chain lengths, damping constants, and diffusion strengths. It then checks the predicted covariance crossover against large finite chains at several detunings and spatial separations, the complementary-error-function identity by quadrature, and the familiar subcritical infinite-chain variance. It reports 15,215 successful exact-rational and bounded numerical checks. Numerical tests do **not** replace the uniform local-limit and Gaussian-convergence proof above. Run it with `python VERIFY.py`.

## Relationship to prior work
Pal and Gupta (arXiv:2609.05391, first public September 4, 2026) analyze nonreciprocal Ornstein–Uhlenbeck chains and exceptional points, including polynomial-in-time relaxation and covariance formulas. Their general Gaussian covariance integral and nonnormal mechanism are established prior work. The present result is limited to the explicitly defined one-way open chain and derives a joint *stationary, large-size, spatially resolved* critical kernel at damping detuning of order \(N^{-1}\); it does not claim the stationary Lyapunov integral itself is new.

Detering, Fouque and Ichiba (arXiv:1805.01962, first public May 4, 2018), Section 4.2 and Remark 4.3, analyze infinite directed-chain Ornstein–Uhlenbeck fluctuations. They already give the stationary-variance formula for subcritical directed coupling and the growing-variance boundary at critical coupling. Those phenomena are known and not accepted here as novel. Their result takes an infinite chain followed by a temporal limit, whereas this theorem takes *finite-chain stationary laws* followed by a coupled spatial and detuning limit, retaining nontrivial correlations between sites separated by order \(\sqrt N\). The older variance dichotomy by itself does not imply the explicit kernel for arbitrary finite collections of mesoscopic sites.

Feng, Fouque and Ichiba (arXiv:2003.08840, first public March 19, 2020) study related directed-chain stochastic differential games and Catalan-process limits, but not this finite stationary Jordan-chain crossover. Hennequin, Vogels and Gerstner (2012) analyze general nonnormal amplification of neural fluctuations, but do not provide this open-chain spatial detuning kernel. These comparisons do not establish global publication priority; in particular, an unlocated general nonnormal covariance scaling theorem might subsume the limit.

## Limitations
The theorem concerns a solvable Gaussian feedforward model with uniform independent forcing and fixed open boundary; nonlinear drift, feedback, spatially correlated forcing, and periodic chains are outside the claim. Its novelty assessment is conditional on the inspected literature and database coverage and has not undergone independent priority verification. Convergence is finite-dimensional, not asserted in a function-space topology. The physical realization of the exactly one-way model may differ from broader chains treated by the motivating source. The usual subcritical infinite-chain variance is previously known. Independent scientific validation has not been performed.

## References
1. S. K. Pal and S. Gupta, *Non-reciprocally interacting Ornstein-Uhlenbeck processes: Exceptional points, Anomalous relaxation, Pseudo-equilibrium and Boundary refrigeration*, arXiv:2609.05391 (first public 2026-09-04), https://arxiv.org/abs/2609.05391.
2. N. Detering, J.-P. Fouque and T. Ichiba, *Directed Chain Stochastic Differential Equations*, arXiv:1805.01962 (first public 2018-05-04), https://arxiv.org/abs/1805.01962, Section 4.2.
3. Y. Feng, J.-P. Fouque and T. Ichiba, *Linear-Quadratic Stochastic Differential Games on Directed Chain Networks*, arXiv:2003.08840 (first public 2020-03-19), https://arxiv.org/abs/2003.08840.
4. G. Hennequin, T. P. Vogels and W. Gerstner, *Non-normal amplification in random balanced neuronal networks*, Physical Review E 86 (2012), https://cbl.eng.cam.ac.uk/publications/hennequin-pre-2012.pdf.
