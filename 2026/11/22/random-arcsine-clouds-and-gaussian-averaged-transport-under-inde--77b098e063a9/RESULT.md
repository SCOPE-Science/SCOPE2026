# Random arcsine clouds and Gaussian averaged transport under independent linear phase kicks

## Finding

Consider a nearest-neighbor quantum particle on the infinite lattice, launched at the origin, subjected once per period to a spatially linear phase kick with a freshly sampled Gaussian slope. Although the noise-averaged position converges after diffusive rescaling to a Gaussian, an individual kicked wavepacket does **not** approach a Gaussian cloud. Instead, its rescaled conditional position law converges **in distribution as a random probability measure** to an arcsine law with a Rayleigh-random radius. Its normalized conditional spatial variance converges to a unit-mean exponential law and therefore never self-averages.

Precisely, put \(h=gT>0\), \(r=\exp[-1/(2\xi^2)]\), and \(\alpha=(1+r)/(1-r)\), with \(0<\xi<\infty\). Let \(X_n\) denote a lattice-position measurement after \(n\) periods, with two levels of randomness: Gaussian kick history and the conditional Born distribution of position. Let \(V_n=\operatorname{Var}(X_n\mid q_1,\ldots,q_n)\). Then

\[
\frac{V_n}{2h^2\alpha n}\ \Longrightarrow\ \operatorname{Exp}(1),
\qquad
\frac{X_n}{\sqrt n}\ \Longrightarrow\ \mathcal N(0,2h^2\alpha)
\]

(the second convergence is after averaging over the kick histories). More strongly, the random conditional measures \(\mathcal L(X_n/\sqrt n\mid q_1,\dots,q_n)\) converge in distribution, under the weak topology on probability measures, to the arcsine measure of radius \(2hR\), where \(R\geq0\) has density \(2s\alpha^{-1}e^{-s^2/\alpha}\) for \(s>0\). In particular, \(\mathbb ER^2=\alpha\). The exact finite-step averaged variance is

\[
\mathbb E X_n^2=2h^2\left[\alpha n-\frac{2r(1-r^n)}{(1-r)^2}\right].
\]

The exponential variance law, random arcsine conditional profile, and exact Gaussian averaged-position limit form one joint quenched-versus-annealed transport theorem; the previously known growth rate of the averaged variance is not claimed as new.

## Assumptions and scope

The Hilbert space is \(\ell^2(\mathbb Z)\) with basis \(\{|m\rangle:m\in\mathbb Z\}\), and \(H=-g\sum_{m\in\mathbb Z}(|m+1\rangle\langle m|+|m\rangle\langle m+1|)\), where \(g>0\). Each complete period consists first of \(e^{-iTH}\), then of \(K_{q_j}|m\rangle=e^{-iq_j m}|m\rangle\); \(T>0\), and the real variables \(q_j\) are independent \(\mathcal N(0,\xi^{-2})\). The initial vector is \(|0\rangle\). No positional measurement occurs between periods; the final position follows Born's rule. Time is indexed by the integer number of periods. Infinite-lattice scope must not be confused with a fixed finite ring at arbitrarily large times.

For a random measure, convergence in distribution is with respect to noise realizations, not an almost-sure weak limit along one fixed noise trajectory. The parameter \(\xi\) is finite and fixed as \(n\to\infty\). The coherent limit \(\xi\to\infty\) is not interchangeable with that limit.

## Proof

**1. Exact conditional law.** Use the lattice Fourier convention \(\widehat\psi(k)=\sum_m\psi(m)e^{-ikm}\). A period acts as \(\widehat\psi_{j}(k)=e^{2ih\cos(k+q_j)}\widehat\psi_{j-1}(k+q_j)\). Since \(\widehat\psi_0=1\), induction gives

\[
\widehat\psi_n(k)=\exp\{2ih\operatorname{Re}(e^{ik}S_n)\},\qquad
S_n=\sum_{j=1}^n\exp\!\left(i\sum_{\ell=j}^nq_\ell\right).
\]

Writing \(S_n=|S_n|e^{i\phi_n}\), the Jacobi--Anger expansion yields for every integer \(m\), including negative indices,

\[
\mathbb P(X_n=m\mid q_1,\ldots,q_n)=J_m(2h|S_n|)^2.
\]

The classical Bessel identities \(\sum_{m\in\mathbb Z}J_m(a)^2=1\) and \(\sum_m m^2J_m(a)^2=a^2/2\) prove \(\mathbb E(X_n\mid q)=0\) and \(V_n=2h^2|S_n|^2\). A second Bessel identity gives the exact conditional characteristic function

\[
\mathbb E(e^{ikX_n}\mid q)=J_0\!\big(4h|S_n|\sin(k/2)\big).
\]

**2. Exact finite-step variance.** Reversing the iid kick sequence shows that \(S_n\) has the same distribution as \(\sum_{j=1}^n U_j\), where \(U_j=e^{i(q_1+\cdots+q_j)}\). Because \(\mathbb E(e^{iq_j})=r\), the cross expectation is \(\mathbb E(U_j\overline U_k)=r^{|j-k|}\). Consequently

\[
\mathbb E|S_n|^2=n+2\sum_{d=1}^{n-1}(n-d)r^d
=\alpha n-\frac{2r(1-r^n)}{(1-r)^2}.
\]

This proves the finite-step formula and calibrates \(\alpha\) without fitting a numerical prefactor.

**3. Two-dimensional phasor central limit theorem.** Let \(U_0=1\) and \(M_n=\sum_{j=1}^n(U_j-rU_{j-1})\). This is a complex martingale with bounded differences. Its increments satisfy

\[
\mathbb E(|\Delta M_j|^2\mid\mathcal F_{j-1})=1-r^2,\qquad
\mathbb E((\Delta M_j)^2\mid\mathcal F_{j-1})=(e^{-2/\xi^2}-r^2)U_{j-1}^2.
\]

The wrapped Gaussian random walk on the circle has a strictly positive transition density and unique uniform stationary distribution, hence is uniformly ergodic. Therefore \(n^{-1}\sum_{j=1}^nU_{j-1}^2\to0\) almost surely. The conditional real covariance matrices of \(M_n/\sqrt n\) converge to \((1-r^2)I_2/2\); bounded increments satisfy Lindeberg's condition. The vector martingale central limit theorem implies \(M_n/\sqrt n\Rightarrow\mathcal N_2(0,(1-r^2)I_2/2)\). The telescoping identity

\[
(1-r)\sum_{j=1}^nU_j=M_n-r(U_n-U_0)
\]

then proves \(S_n/\sqrt n\Rightarrow G\), where \(G\) is circular complex Gaussian with independent real and imaginary components of variance \(\alpha/2\). Thus \(|G|=R\) has the stated Rayleigh law and \(|G|^2/\alpha\sim\operatorname{Exp}(1)\). The conditional-variance limit follows. Bounded martingale differences also give uniform moment bounds of all fixed orders after \(\sqrt n\) scaling; in particular, the relative variance \(\operatorname{Var}(V_n)/(\mathbb EV_n)^2\to1\), so the non-self-averaging conclusion also holds at second-moment level.

**4. Random arcsine and averaged Gaussian limits.** For each fixed real \(k\), the conditional characteristic function of \(X_n/\sqrt n\) is

\[
J_0\!\left(4h|S_n|\sin\frac{k}{2\sqrt n}\right).
\]

As \(S_n/\sqrt n\Rightarrow G\), the continuous-mapping theorem and \(2\sqrt n\sin(k/(2\sqrt n))\to k\) identify the random weak limit as the unique probability measure with characteristic function \(J_0(2hRk)\). It is the arcsine law with density

\[
f_R(x)=\frac{\boldsymbol1_{\{|x|<2hR\}}}{\pi\sqrt{(2hR)^2-x^2}}.
\]

Tightness of the random measures follows from their conditional second moments \(V_n/n=2h^2|S_n|^2/n\), a tight family. Thus the convergence holds for random probability measures, not only for a single characteristic-function value. Finally, averaging \(J_0(2hRk)\) over the Rayleigh radius gives \(\mathbb E[J_0(2hRk)]=e^{-h^2\alpha k^2}\). By Levy's continuity theorem the noise-averaged position converges to \(\mathcal N(0,2h^2\alpha)\). All limits are proved at every fixed \(0<\xi<\infty\) and \(gT>0\).

## Verification

The standalone `verification.py` reproduces a four-kick full-lattice Fourier evolution and matches the exact Bessel-square site probabilities to maximum absolute error below \(3\times10^{-16}\); the computed sample spatial variance agrees with \(2h^2|S_n|^2\). It checks Bessel normalization, moments and characteristic-function identities at five amplitudes. A seeded \(22{,}000\)-history simulation of \(360\) kicks at \(\xi=0.94\) checks the closed finite-step mean, the exponential limiting CDF, component covariance, relative width fluctuations, and the averaged-position characteristic function. The strongest observed exponential-CDF discrepancy among six test thresholds was approximately \(0.00347\). These checks detect transcription and normalization errors but do not substitute for the analytic martingale proof.

Reproduce with `python verification.py` using Python 3, NumPy and SciPy. The code has no external inputs, network calls or separate data dependencies.

## Relationship to prior work

P. Wang (arXiv:2605.06701, first public version 2026-05-11) introduces precisely the Gaussian-slope linear-kick tight-binding model and represents the accumulated momentum phase by a phasor sum. Its Section V derives the noise-averaged second-moment growth rate, proportional to \((1+r)/(1-r)\); that structural observation and averaged diffusivity are treated as known. The present result instead resolves an individual history's **entire conditional position law**, obtains the nondegenerate exponential width distribution and random arcsine profile, and proves a full Gaussian ensemble central limit theorem with its prefactor for a delta-site launch.

G. Di Molfetta and F. Debbasch (arXiv:1409.2122) prove an averaged Gaussian limit for a **coined discrete-time** quantum walk subject to random gauge fields. That different step operator, coin structure and noise channel do not yield the conditional Bessel family or the exponential width law here. Standard coherent one-dimensional tight-binding quantum-walk Bessel formulas provide an algebraic ingredient but do not include the random phasor central limit theorem for this protocol. No theorem covering the combined statement was found in the inspected literature and indexed searches, but searches do not certify global novelty.

## Limitations

The theorem is for a delta-site launch, independent Gaussian slopes, constant positive hopping and period, and the infinite lattice. It does not establish that the same random arcsine conditional law holds for arbitrary initial coherent packets, spatially independent kicks, finite periodic rings at fixed size, temporally correlated kicks, or the singular zero-noise limit. The conditional wavefunction remains pure under each kick history; Gaussianity applies **only** after averaging position measurements over independent noise histories. The result has not undergone independent scientific review. Unindexed prior work and inaccessible source variants remain possible priority risks.

## References

1. P. Wang, *Diffusive transport from spatially correlated random phase kicks*, arXiv:2605.06701 (first posted 2026-05-11), https://arxiv.org/abs/2605.06701.
2. G. Di Molfetta and F. Debbasch, *Discrete-time quantum walks in random artificial gauge fields*, arXiv:1409.2122 (2014; revised version examined v3 2015-05-30), https://arxiv.org/abs/1409.2122.
3. A. M. Childs, *Random and quantum walks in one dimension*, lecture notes, https://www.cs.umd.edu/~amchilds/teaching/w11/l13.pdf (standard coherent tight-binding Bessel propagation).
