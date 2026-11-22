# Four alternating signs of temporal magnetization covariance under Pareto global resetting

## Finding
For the thermodynamic conditional magnetization of a globally reset, one-dimensional finite-temperature Glauber–Ising chain, an exactly Pareto-square inter-reset clock can induce **at least four distinct temporal covariance zero crossings** before two and a half minimum waiting intervals. In dimensionless units the consecutive signs at lags \(0,\tfrac12,\tfrac65,\tfrac95,\tfrac52\) are \(+,-,+,-,+\), for every sufficiently large positive relaxation-to-clock ratio \(k\). This is an existence theorem for four reversals, not a count of all zeros.

## Assumptions and scope
Let \(W_i\) be independent waits with probability density \(f(w)=2w^{-3}\mathbf 1_{\{w\ge1\}}\). Thus \(\mathbb E W_i=2\). Use the two-sided stationary renewal process and let \(A_s\) be time since its last event. Fix \(m_0\ne0\), \(k>0\), and define \(M_s=m_0e^{-kA_s}\), with \(C_k(t)=\operatorname{Cov}(M_0,M_t)/m_0^2\) for \(t\ge0\). A physical clock with minimum interval \(\tau_0\) is converted to these units by \(s=t/\tau_0\) and \(k=\tau_0[1-\tanh(2\beta J)]\); the relaxation rate is positive at finite temperature. The claim refers to the macroscopic, age-conditioned magnetization, after the thermodynamic limit, rather than the fluctuating spin of a single site at finite system size.

Write \(\nu(t)=\sum_{n\ge1}f^{*n}(t)\) for the density of later renewal epochs following an event at zero. Only finitely many terms occur for fixed \(t\), since each wait is at least one.

## Proof
**Stationary age and two-time small-age density.** The stationary age density is \(p_A(a)=S(a)/2\), where \(S(a)=1\) for \(0\le a<1\) and \(S(a)=a^{-2}\) for \(a\ge1\). Consequently \(k\mathbb E e^{-k A_0}\to\tfrac12\). Fix \(t>0\) away from integer renewal thresholds and choose \(\delta>0\) so small that \(\delta<\min(1,t)\), and \(t+a-b\) stays away from those thresholds for \(a,b\in[0,\delta]\). Both ages small requires at least one event between observations. As an event just before zero has no possible successor during the remaining part of the initial minimum waiting interval, the joint age density in this square is exactly
\[
q_t(a,b)=\tfrac12 S(b)\nu(t+a-b)=\tfrac12\nu(t+a-b),\qquad 0<a,b<\delta.
\]
The contribution to \(\mathbb E[e^{-k(A_0+A_t)}]\) from outside that square is at most \(e^{-k\delta}\). The contribution with no renewal is also exponentially small in \(k\), since then \(A_t=A_0+t\). Continuity of the finite convolution sum at \(t\) and the two-dimensional Laplace approximate identity therefore give
\[
\lim_{k\to\infty}k^2C_k(t)=\frac{\nu(t)}2-\frac14.\tag{1}
\]
At zero lag \(C_k(0)=\operatorname{Var}(e^{-kA_0})>0\) for every \(k>0\).

**Five strict sign witnesses.** For \(0<t<1\) there can be no later renewal event, so \(\nu(\tfrac12)=0\) and the right-hand side of (1) is \(-\tfrac14\). For \(1<t<2\), only one interval can fit and \(\nu(t)=2t^{-3}\); hence
\[
\lim_{k\to\infty}k^2C_k(\tfrac65)=\frac{71}{216}>0,
\qquad
\lim_{k\to\infty}k^2C_k(\tfrac95)=-\frac{229}{2916}<0.
\]
At \(t=\tfrac52\), only one or two full intervals fit, giving
\[
\nu(\tfrac52)=\frac{16}{125}+\int_1^{3/2}\frac{4\,ds}{s^3(\tfrac52-s)^3}.
\]
On the integration interval, \(s(\tfrac52-s)\le25/16\), so
\[
\nu(\tfrac52)\ge \frac{16}{125}+\frac12\frac4{(25/16)^3}=\frac{10192}{15625}>\frac12,
\quad
\lim_{k\to\infty}k^2C_k(\tfrac52)\ge\frac{4759}{62500}>0.
\]
Each nonzero limiting sign remains strict for all \(k\) beyond a common finite threshold. Finally, boundedness, right-continuity of the renewal-age process and the absence of fixed-time renewal atoms imply continuous \(C_k(t)\). Intermediate-value arguments across each of the four successive lag intervals prove four distinct zero crossings.

## Verification
Run \(\texttt{python3 checks.py}\) in the same folder. The standalone standard-library checker verifies the precise rational witnesses, strict two-renewal convolution bound, and an independent Simpson quadrature for the nontrivial convolution. It is a finite consistency check, not a replacement for the stationary-density and approximate-identity proof.

## Relationship to prior work
Anagha V K and Apoorva Nagar (2026) introduce Pareto resetting of Glauber–Ising magnetization and derive its single-time distributions, including the one-dimensional exponential relaxation. The new assertion concerns **joint stationary observations at different times** and a fourfold sign-alternation mechanism controlled by renewal-event spacing. Classical renewal theory supplies the stationary-age and renewal-density framework; the mechanism is an application of those tools, not a claim to have discovered the general renewal identity. General shot-noise first-passage results and age/residual-life dependence studies do not state these four precise covariance sign witnesses in the Ising setting.

## Limitations
The result proves a sufficiently-large-\(k\) regime but does not give a numerical or sharp minimum \(k\), uniqueness of any zero, or the total number of zero crossings. It does not assert four reversals of single-spin fluctuations or finite-volume stochastic magnetization, nor does it cover clocks lacking a strict waiting-time cutoff. The statement is for a specific, physically natural marginal Pareto exponent \(2\), the boundary of finite interarrival variance. General renewal-density literature could contain an implicit version of this special-case consequence; publication priority requires external verification.

## References
- Anagha V K and Apoorva Nagar, *Ising Model with Power Law Resetting*, arXiv:2602.15495 (first public February 17, 2026); Phys. Rev. Research 8, 023197 (2026), doi:10.1103/d3hg-bgmh. https://arxiv.org/abs/2602.15495
- R. J. Glauber, *Time-dependent statistics of the Ising model*, Journal of Mathematical Physics 4, 294 (1963). https://doi.org/10.1063/1.1703954
- J. Brémont, *Beyond Poisson: First-Passage Asymptotics of Renewal Shot Noise*, Phys. Rev. Lett. 136, 107101 (2026), doi:10.1103/bbh8-n8dt. https://arxiv.org/abs/2510.21670
