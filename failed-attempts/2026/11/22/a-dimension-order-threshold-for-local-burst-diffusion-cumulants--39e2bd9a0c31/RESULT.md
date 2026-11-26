# A dimension–order threshold for local burst-diffusion cumulants

## Finding
A stationary point source of independently diffusing, exponentially mortal particles launched in Poisson bursts has a sharp **dimension-times-cumulant-order threshold** for shrinking-detector factorial cumulants. This statement concerns microscopic detector counts, rather than pointwise probability densities or distant-point correlations.

Fix an integer spatial dimension \(d\ge1\) and an integer factorial-cumulant order \(k\ge1\). Let \(F_k(\varepsilon)\) be the order-\(k\) factorial cumulant of the stationary number of living particles in the ball \(B(0,\varepsilon)\). Write \(b>0\) for burst rate, \(D>0\) for diffusion coefficient, \(\mu>0\) for death rate and \(m_k=\mathbb E[(J)_k]\in(0,\infty)\) for the positive finite \(k\)-th falling-factorial moment of burst size \(J\). Put
\[
 v_d=\frac{\pi^{d/2}}{\Gamma(1+d/2)},\qquad
 c_{d,k}=\left(\frac{v_d}{(4\pi)^{d/2}}\right)^k,
 \qquad Q_d(u)=\Pr\{|Z_u|\le 1\},
\]
where \(Z_u\sim N(0,2uI_d)\). Then, as \(\varepsilon\downarrow0\),
\[
F_k(\varepsilon)\sim b m_k\begin{cases}
 c_{d,k}D^{-dk/2}\Gamma(1-dk/2)(k\mu)^{dk/2-1}\varepsilon^{dk},&dk<2,\\[3pt]
 \dfrac{c_{d,k}\varepsilon^2}{D}\log\!\dfrac{D}{\mu\varepsilon^2},&dk=2,\\[6pt]
 \dfrac{C_{d,k}\varepsilon^2}{D},&dk>2,
\end{cases}
\qquad C_{d,k}=\int_0^\infty Q_d(u)^k\,du\in(0,\infty).
\]
The \(dk>2\) leading coefficient is independent of mortality. Two explicit natural constants are \(C_{2,2}=\tfrac12\log2\) and \(C_{3,1}=\tfrac12\).

There is a sharp spatial contrast. For a ball \(B(x,\varepsilon)\) centred at any fixed \(x\ne0\), the same factorial cumulant is asymptotic to
\[
 b m_k v_d^k\varepsilon^{dk}
 \int_0^\infty e^{-k\mu t}(4\pi Dt)^{-dk/2}
 \exp\!\left(-\frac{k|x|^2}{4Dt}\right)\,dt,
\]
whose coefficient is finite and strictly positive. Thus the source-centred logarithm or saturated \(\varepsilon^2\) law is a genuine local singularity, not an ordinary detector-volume effect.

## Assumptions and scope
Bursts occur according to a homogeneous rate-\(b\) Poisson process on the entire time line. Each event at the origin introduces an independent copy of a nonnegative integer burst size \(J\), with \(m_k=\mathbb E[J(J-1)\cdots(J-k+1)]\in(0,\infty)\). Every child starts at the origin; conditional on birth, all particles have independent Brownian motions with generator \(D\Delta\) in \(\mathbb R^d\) and independent exponential lifetimes with rate \(\mu\). Bursts, paths and deaths are independent of one another. There are no targets, interactions, reflecting boundaries or bulk birth events. Stationarity is constructed from the infinite past. In particular, \(\mathbb E J<\infty\), so the stationary number of living particles is almost surely finite.

For a count \(N_\varepsilon\), define its factorial cumulant by
\[
 F_k(\varepsilon)=\left.\frac{d^k}{dz^k}\log\mathbb E[(1+z)^{N_\varepsilon}]\right|_{z=0};
\]
under the assumed finite \(k\)-th burst moment this means the derivative from the generating-function domain, or the equivalent algebraic factorial-moment cumulant. These are not ordinary cumulants of the count: Poisson shot noise contributes only to the first factorial cumulant. For \(\mathbb E[(J)_k]=0\), the exact \(F_k\) is zero and a positive leading asymptotic is not claimed.

## Proof
**1. Exact Poisson-cluster representation.** A burst of age \(t>0\) contributes a binomially thinned count with per-child probability \(a_\varepsilon(t)=e^{-\mu t}q_{d,\varepsilon}(t)\), where
\[
q_{d,\varepsilon}(t)=\Pr\bigl\{|\sqrt{2D}W_t|\le\varepsilon\bigr\}
=Q_d(Dt/\varepsilon^2).
\]
The marked-Poisson exponential formula gives
\[
\log\mathbb E[(1+z)^{N_\varepsilon}]
=b\int_0^\infty\left(\mathbb E[(1+za_\varepsilon(t))^J]-1\right)dt.
\]
Taking its \(k\)-th derivative at zero yields the exact identity
\[
 F_k(\varepsilon)=bm_k\int_0^\infty e^{-k\mu t}q_{d,\varepsilon}(t)^k\,dt
=\frac{bm_k\varepsilon^2}{D}\int_0^\infty
 e^{-k\mu\varepsilon^2u/D}Q_d(u)^k\,du.\tag{1}
\]
This formula is valid for each \(d,k\) and every \(\varepsilon>0\). Finite \(m_k\) permits termwise derivative by dominated convergence, since \(0\le a_\varepsilon(t)\le e^{-\mu t}\).

**2. Exact Gaussian asymptotic and threshold.** With \(v_d\) the unit-ball volume, integrating the Gaussian heat kernel over the unit ball shows
\[
Q_d(u)=\int_{|y|\le1}\frac{e^{-|y|^2/(4u)}}{(4\pi u)^{d/2}}\,dy
=\frac{v_d}{(4\pi u)^{d/2}}\bigl(1+O(u^{-1})\bigr)
\quad (u\to\infty).
\]
Moreover \(0<Q_d(u)\le\min\{1,v_d(4\pi u)^{-d/2}\}\). If \(dk>2\), the integral \(C_{d,k}\) is finite by this bound. Dominated convergence applied to (1) gives the saturated \(\varepsilon^2\) formula, including its mortality independence.

If \(dk=2\), write \(Q_d(u)^k=c_{d,k}/u+O(u^{-2})\) for \(u\ge1\). Put \(\delta=\mu\varepsilon^2/D\). Splitting the integral into \((0,1)\) and \((1,\infty)\) and subtracting \(c_{d,k}/u\) on the latter gives
\[
\int_0^\infty e^{-k\delta u}Q_d(u)^k\,du
=c_{d,k}\log(1/\delta)+O(1),\quad\delta\downarrow0,
\]
by the standard exponential-integral logarithm; the bounded-error estimate follows from integrability of the \(O(u^{-2})\) remainder. This is the stated critical logarithm.

If \(dk<2\), use instead the original time integral. For each fixed \(t>0\), \(\varepsilon^{-d}q_{d,\varepsilon}(t)\to v_d(4\pi Dt)^{-d/2}\), bounded above by that same expression. The function \(t^{-dk/2}e^{-k\mu t}\) is integrable at both ends precisely for \(dk<2\). Dominated convergence and the Gamma integral produce its claimed constant. Among integer \(d,k\), this regime consists solely of \(d=k=1\).

**3. Exact special constants.** In the planar case \(Q_2(u)=1-e^{-1/(4u)}\). After substitution \(z=1/(4u)\) and integration by parts,
\[
 C_{2,2}=\frac14\int_0^\infty\frac{(1-e^{-z})^2}{z^2}\,dz
=\frac12\int_0^\infty\frac{e^{-z}-e^{-2z}}z\,dz
=\frac{\log2}{2},
\]
using Frullani's integral. In three dimensions the potential kernel for generator \(\Delta\) is \(G(y)=(4\pi|y|)^{-1}\), so
\[
C_{3,1}=\int_{|y|\le1}\!G(y)dy
=\int_0^1r\,dr=\frac12.
\]
For \(d=1,k=1\), an exact additional test is \(F_1(\varepsilon)=\frac{bm_1}{\mu}(1-e^{-\varepsilon\sqrt{\mu/D}})\).

**4. Detector away from the source.** For fixed \(x\ne0\), the probability of being in \(B(x,\varepsilon)\) is \(v_d\varepsilon^d(4\pi Dt)^{-d/2}e^{-|x|^2/(4Dt)}(1+o(1))\) for each fixed \(t>0\). For sufficiently small \(\varepsilon<|x|/2\), its volume-normalized value is bounded by a constant times \(t^{-d/2}e^{-|x|^2/(16Dt)}\). Raising to order \(k\) and multiplying by \(e^{-k\mu t}\) gives an integrable majorant at both \(t=0\) and \(t=\infty\). Dominated convergence proves the off-source formula.

## Verification
The attached standalone `checker.py` uses SciPy numerical quadrature for the exact scaled integral (1), its asymptotic constants and the two closed forms. It passes 21 asymptotic convergence comparisons spanning all three regimes, three exact one-dimensional mean-resolvent checks, and two special-constant checks. These are numerical consistency tests; the stated arbitrary-dimension/order theorem follows from the analytic proof above, not numerical extrapolation. Running `python checker.py` from the extracted files reproduces these tests, given Python, NumPy and SciPy.

## Relationship to prior work
Mercado-Vásquez and Boyer (2026), arXiv:2611.04843v1, derive general stationary **mean** density and bursty synthesis target-search results, including Brownian examples. Equation (20) there is the order-one spatial Green representation; it does not state the microscopic all-order factorial-cumulant threshold or the on-source/off-source contrast. Cottrell, Swain and Tupper (2012) develop spatial branching generating functions and mean/variance spatial covariances for gene expression; this is an important broader conceptual method, but their displayed concentration-correlation results do not give the \(dk=2\) cutoff for instantaneous burst-cluster detector counts. Miles (2025) studies point-source expression with telegraph-modulated source intensity and derives mean/variance statistics, rather than this independent-parent burst model and its all-order small-ball law. General Poisson-cluster generating-function theory and Brownian Green kernels are established tools; neither is claimed as a new discovery.

## Limitations
The results are for a fixed point source and source-centred or fixed-offset Euclidean ball detectors shrinking to zero. They require independent post-birth paths, exponential mortality, homogeneous diffusion, Poisson burst times, a finite positive \(k\)-th burst factorial moment, and no interactions. The exponent threshold is not asserted for anomalous diffusion, correlated descendants, finite-sized sources or bounded domains. The absolute amplitude still depends on the burst factorial moment, and in the \(dk<2\) regime on mortality. The results do not imply priority over every possible older equivalent: unrestricted generating-function identities in the literature may permit unreported specializations, and independent historical assessment remains appropriate.

## References
1. G. Mercado-Vásquez and D. Boyer, *Stochastic synthesis and degradation of arbitrary diffusive processes*, arXiv:2611.04843v1 (first public 2026-11-03), https://arxiv.org/abs/2611.04843 .
2. D. Cottrell, P. S. Swain and P. F. Tupper, *Stochastic branching-diffusion models for gene expression*, PNAS 109 (2012), 9699–9704, https://pmc.ncbi.nlm.nih.gov/articles/PMC3382520/ .
3. C. E. Miles, *Incorporating spatial diffusion into models of bursty stochastic transcription*, J. R. Soc. Interface 22 (2025), 20240739, https://pmc.ncbi.nlm.nih.gov/articles/PMC11978452/ .
