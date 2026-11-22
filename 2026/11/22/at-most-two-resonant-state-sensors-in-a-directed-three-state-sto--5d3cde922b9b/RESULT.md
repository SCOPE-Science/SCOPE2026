# At most two resonant state sensors in a directed three-state stochastic cycle

## Finding

A three-stage unidirectional stochastic cycle can exhibit oscillatory relaxation while **every** single-state occupancy sensor has a strictly zero-frequency-maximized power spectrum. Among its three state-indicator sensors, at most **two** can exhibit a nonzero-frequency spectral maximum, and their oscillation efficiencies are ranked exactly by state exit rates: a faster-exiting, less frequently occupied state is never worse at detecting a spectral peak.

For a stationary three-state continuous-time Markov chain with positive clockwise exit rates \(a,b,c\), put
\[
P=ab+bc+ca,\qquad L=a^2+b^2+c^2,
\]
and
\[
H_1=b^2+bc+c^2,\quad H_2=a^2+ac+c^2,\quad H_3=a^2+ab+b^2.
\]
For the centered single-state occupancy observable \(f_i(t)=\mathbf1_{\{X_t=i\}}-\pi_i\), the **two-sided** stationary covariance power spectrum is exactly
\[
G_i(\omega)=\frac{2abc}{P}\frac{\omega^2+H_i}{\omega^4+L\omega^2+P^2},\qquad \omega\ge0.
\]
Define \(\Delta_i=P^2-LH_i\). Then sensor \(i\) has a **unique strict spectral maximum at positive frequency** if and only if \(\Delta_i>0\), where
\[
\omega_{i,*}^2=-H_i+\sqrt{H_i^2+\Delta_i}.
\]
If \(\Delta_i\le0\), its spectrum is strictly decreasing at every positive frequency, with maximum only at zero. At equality the spectrum is quartically flat at the origin. For any positive \(a,b,c\), at most two of the three values \(\Delta_i\) are positive. If \(a\le b\le c\), the set of resonant sensors is either empty, \(\{3\}\), or \(\{2,3\}\), including tie cases. The normalized peak heights and efficiencies have the same weak ordering from sensor 1 to sensor 3, and the ordering is strict whenever exit rates differ and at least the better sensor is resonant.

A particularly explicit complete one-parameter phase diagram arises for \((a,b,c)=(t,1,1)\). Let \(\theta=0.465571231876768\ldots\) be the **unique positive root** of \(\theta^3+2\theta^2+\theta-1=0\). The number of resonant individual-state sensors equals zero for \(0<t\le\theta\), two for \(\theta<t<1\), zero at \(t=1\), and one for \(t>1\). For \(0<t\le\theta\), the two nonstationary eigenvalues are nevertheless nonreal, so the complete lack of resonance in binary state readouts does **not** imply a real relaxation spectrum.

## Assumptions and scope

The state space is exactly \(\{1,2,3\}\), with only clockwise transitions \(1\to2\) at rate \(a>0\), \(2\to3\) at rate \(b>0\), and \(3\to1\) at rate \(c>0\). There are no reverse transitions or other channels. The continuous-time chain is initialized in its unique stationary law
\[
(\pi_1,\pi_2,\pi_3)=\frac{(bc,ca,ab)}P.
\]
For \(i=1,2,3\), the spectrum is the Fourier transform \(G_i(\omega)=\int_{-\infty}^{\infty}\operatorname{Cov}(f_i(0),f_i(s))e^{-\mathrm i\omega s}\,ds\). Oscillation efficiency is \(\eta_i=1-G_i(0)/\max_{\omega\ge0}G_i(\omega)\), with \(\eta_i=0\) when zero frequency is maximal. A sensor records whether the particle is in one individual state; arbitrary weighted real-valued observables are outside the simultaneous-sensor-count classification.

## Proof

**1. Stationary spectrum.** Let \(Q\) be the generator with rows \((-a,a,0),(0,-b,b),(c,0,-c)\), and \(T=a+b+c\). Direct determinant expansion gives
\[
\det(sI-Q)=s(s^2+Ts+P).
\]
For each state \(i\), with the other two exit rates \(r_j,r_k\), the diagonal resolvent is
\[
[(sI-Q)^{-1}]_{ii}=\frac{(s+r_j)(s+r_k)}{s(s^2+Ts+P)},\qquad \Re s>0.
\]
Stationarity and the semigroup give \(\int_0^\infty e^{-st}\operatorname{Cov}(f_i(0),f_i(t))\,dt=\pi_i\big([(sI-Q)^{-1}]_{ii}-\pi_i/s\big)\). The centered covariance decays exponentially, so taking twice the real part at \(s=\mathrm i\omega\) is legitimate for \(\omega>0\), with continuous extension to zero. Simplifying this rational expression proves the displayed spectrum for all \(i\) and all nonnegative frequencies.

**2. Individual modality.** Put \(z=\omega^2\ge0\), and remove the positive common prefactor from \(G_i\). The remaining function is \(h_i(z)=(z+H_i)/(z^2+Lz+P^2)\). Its derivative has the sign of
\[
\Delta_i-2H_i z-z^2.
\]
This expression decreases strictly on \([0,\infty)\). If \(\Delta_i\le0\), the power spectrum is strictly decreasing for all positive \(z\). If \(\Delta_i>0\), the derivative changes sign once, at \(z=-H_i+\sqrt{H_i^2+\Delta_i}>0\), proving the unique strict maximum. When \(\Delta_i=0\), \(h_i'(0)=0\) but \(h_i'(z)<0\) for all \(z>0\), so the first nonzero frequency correction is negative of order \(\omega^4\).

**3. Rigidity of simultaneous resonance and rate ordering.** The algebraic identities
\[
H_1+H_2+H_3=2L+P,\qquad P\le L
\]
(the latter is half the sum of three squared rate differences) imply
\[
\sum_i\Delta_i=3P^2-L(2L+P)=(P-L)(3P+2L)\le0.
\]
Hence all three \(\Delta_i\) cannot be positive. Moreover,
\[
H_1-H_2=(b-a)T,\qquad H_2-H_3=(c-b)T.
\]
For ordered exit rates \(a\le b\le c\), the \(H_i\) decrease and the \(\Delta_i\) increase; therefore resonant sensors form only a suffix of the ordered states, and its length cannot exceed two.

For \(z>0\), the normalized spectrum is
\[
\frac{G_i(\sqrt z)}{G_i(0)}=\frac{P^2(1+z/H_i)}{z^2+Lz+P^2}.
\]
The right-hand side strictly decreases in \(H_i\), so the state with larger exit rate and smaller stationary occupation is at least as efficient at every positive frequency; once one sensor resonates the respective maximal normalized gains are strictly ordered whenever the corresponding rates differ. The efficiency \(\eta_i\) is an increasing function of that maximal normalized gain.

**4. Complete reentrant phase for two equal rates.** Set \(a=t\), \(b=c=1\). Exact factorization gives
\[
\Delta_1=(t-1)(t+5),\qquad
\Delta_2=\Delta_3=-(t-1)(t^3+2t^2+t-1).
\]
The cubic is strictly increasing for positive \(t\), negative at zero and positive at one. It therefore has exactly one positive root \(\theta\in(0,1)\). The signs establish the claimed zero–two–zero–one sequence without reliance on numerical root finding. The nonzero eigenvalues of \(Q\) are the roots of \(\lambda^2+(t+2)\lambda+(2t+1)=0\); their discriminant is \(t(t-4)<0\) for \(0<t<4\), including the entire region \(0<t\le\theta\) with no individual-state resonance.

## Verification

The standalone `checker.py` reconstructs the exact diagonal generator resolvents using SymPy, verifies the polynomial identities and reentrant factors, and numerically compares the closed power spectra against matrix-resolvent evaluations for 300 randomly chosen positive rate triples and four positive frequencies per triple (3,600 scalar comparisons). It additionally checks peak locations and count for each sampled triple, special boundary cases, and the unique cubic threshold. Run with `python checker.py`; NumPy and SymPy are the only nonstandard Python dependencies. A successful run reports an `OK` line. The infinite-parametric conclusions follow from the analytic proof, not from this finite check.

## Relationship to prior work

Jia (2026) defined oscillation efficiency, proved a universal three-state ceiling, and solved a special one-way three-state model with two equal **slow** rates and one fast state, including an example with real relaxation eigenvalues but a positive-frequency peak. These are prior results. The new assertion here is a simultaneous, all-positive-rate **three-indicator** mode census with rate-order rigidity and an exact zero–two–zero–one visibility transition as one rate passes through the other two. Chen (2007) established general three-state fluctuation-spectrum formulas and an existence criterion for nonmonotone real-observable spectra; those broad analytic tools are also prior work. The distinction is the explicit **joint binary-sensor classification**, which cannot be inferred from a statement merely that some real observable is nonmonotonic. The priority status of the full general formula and any uninspected reductions remains subject to independent literature review.

## Limitations

The result concerns a stationary, exactly three-state, directed Markov cycle and spectra of single-state indicators. It is not a claim about all real-valued observables, more than three states, noisy or finite-duration frequency estimates, or finite-entropy-production chemical systems (strictly one-way transitions violate reverse-edge thermodynamic consistency). The older three-state full text could not be obtained for a conclusive statement-by-statement comparison, so a published equivalent of part or all of the sensor classification remains a material priority risk. No independently conducted mathematical audit has been performed.

## References

1. C. Jia, *Fundamental Bounds on the Oscillation Efficiency of Markov Networks*, arXiv:2610.23310 (first public version 2026-10-16). https://arxiv.org/abs/2610.23310
2. Y. Chen, *On the Monotonicity of Fluctuation Spectra for Three-State Markov Processes*, Fluctuation and Noise Letters 7 (2007), L181–L192, doi:10.1142/S0219477507003830. https://doi.org/10.1142/S0219477507003830
3. Y. Chen, M.-P. Qian and J.-S. Xie, *Irreversibility implies the occurrence of nonmonotonic power spectra*, Journal of Mathematical Physics 48 (2007), 073301, doi:10.1063/1.2747615. https://doi.org/10.1063/1.2747615
