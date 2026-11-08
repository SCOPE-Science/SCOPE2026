# Arithmetic resonance permits stable exact anticipation with two positive delays

## Finding
For two independent undamped oscillatory modes, exact anticipation by a positive **distributed** delay is possible precisely when every delay differs from the target anticipation time by a common period of both modes. Two incommensurate frequencies force the delay distribution to be a single point mass. Commensurate frequencies admit arbitrary probability mixtures supported on their common-period lattice. A non-singleton mixture can even produce exponentially stable exact anticipation, with an explicit positive coupling window.

More precisely, let \(\omega_1,\omega_2>0\), \(r_1,r_2>0\), and set
\[
J=\operatorname{diag}(\omega_1 R,\omega_2 R),\qquad R=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad x(t)=e^{Jt}x_0,
\]
where both two-dimensional components of \(x_0\) have nonzero norm. For a Borel probability measure \(\mu\) on \([0,\infty)\), consider the driver–response equation
\[
\dot y(t)=Jy(t)+\kappa\left[x(t)-\int_{[0,\infty)}y(t-s)\,d\mu(s)\right],\qquad\kappa>0.
\]
Fix \(T>0\). Define
\[
\mathcal L=\{\ell\in\mathbb R:\omega_1\ell\in2\pi\mathbb Z\ \text{and}\ \omega_2\ell\in2\pi\mathbb Z\}.
\]
Then \(y(t)=x(t+T)\) for all real \(t\) is an exact response solution **if and only if**
\[
\operatorname{supp}\mu\subseteq(T+\mathcal L)\cap[0,\infty).
\]
For irrational \(\omega_1/\omega_2\), one has \(\mathcal L=\{0\}\), so exact anticipation requires \(\mu=\delta_T\). For rational \(\omega_1/\omega_2=p/q\) in lowest terms, write \(\omega_1=p\Omega\), \(\omega_2=q\Omega\). Then \(\mathcal L=(2\pi/\Omega)\mathbb Z\), and every probability mixture on the corresponding admissible delay lattice is exact.

If furthermore \(\mu\) is supported in \([0,S]\), with \(S>0\), and
\[
c=\min\{\cos(\omega_1T),\cos(\omega_2T)\}>0,
\]
then \(y(t)=x(t+T)\) attracts every response history exponentially in the linear delay equation whenever \(0<\kappa<c/(4S)\). The specific choice
\[
\omega_1=1,\quad\omega_2=2,\quad T=\pi/6,\quad
\mu=\tfrac12\delta_{\pi/6}+\tfrac12\delta_{13\pi/6},\quad \kappa=\tfrac1{100}
\]
is an explicit stable example with two distinct positive delays. The anticipated signal is genuinely shifted: \(T=\pi/6\) is less than the common period \(2\pi\).

## Assumptions and scope
The delay law is a nonnegative normalized Borel measure; atomic distributions are allowed. The driver consists of two nonzero harmonic components, the feedback operator is a scalar positive gain times the identity, and the same delay law acts on all coordinates. Existence of exact anticipation allows arbitrary delay support; the exponential-attraction assertion assumes **bounded** delay support. Every trajectory statement refers to response histories with a prescribed ongoing driver \(x\). No claim is made for arbitrary nonlinear drivers or noisy measurements.

## Proof
First substitute \(y(t)=x(t+T)\). Since \(x\) solves \(\dot x=Jx\), the differential equation is satisfied exactly if and only if
\[
 x(t)=\int x(t+T-s)\,d\mu(s)\quad\text{for every }t.
\]
In the complex coordinate of the \(j\)-th rotating mode, nonzero amplitude makes this equivalent to
\[
 \int e^{i\omega_j(T-s)}\,d\mu(s)=1,\qquad j=1,2.
\]
Each integrand has modulus one. Its expectation equals one precisely when the integrand equals one \(\mu\)-almost surely: indeed the nonnegative function \(1-\operatorname{Re} e^{i\omega_j(T-s)}\) has zero integral. Intersecting the two full-measure conditions gives \(s-T\in\mathcal L\) almost surely. As the lattice intersection is closed, this is equivalent to the stated support inclusion. The converse is immediate. Elementary arithmetic yields \(\mathcal L=\{0\}\) when the frequency ratio is irrational and \(\mathcal L=(2\pi/\Omega)\mathbb Z\) when it is rational in lowest terms.

For attraction, set \(e(t)=y(t)-x(t+T)\). Every two-dimensional complex mode of the error satisfies
\[
 \dot z(t)=i\omega_jz(t)-\kappa\int z(t-s)\,d\mu(s).
\]
Its characteristic roots satisfy \(\lambda=i\omega_j-\kappa\widehat\mu(\lambda)\), with \(\widehat\mu(\lambda)=\int e^{-\lambda s}\,d\mu(s)\). If \(\operatorname{Re}\lambda\ge0\), positivity of \(\mu\) gives \(|\widehat\mu(\lambda)|\le1\), so \(|\lambda-i\omega_j|\le\kappa\). For bounded support \([0,S]\), the identity
\[
 |e^{-\lambda s}-e^{-i\omega_js}|\le s|\lambda-i\omega_j|e^{s|\lambda-i\omega_j|}
\]
yields
\[
 |\widehat\mu(\lambda)-\widehat\mu(i\omega_j)|\le S\kappa e^{S\kappa}.
\]
The arithmetic support condition gives \(\widehat\mu(i\omega_j)=e^{-i\omega_jT}\), whose real part is at least \(c\). Under \(\kappa<c/(4S)\), since \(0<c\le1\), we have \(S\kappa e^{S\kappa}<(c/4)e^{1/4}<c\). Consequently \(\operatorname{Re}\widehat\mu(\lambda)>0\), contradicting \(\operatorname{Re}\lambda=-\kappa\operatorname{Re}\widehat\mu(\lambda)\ge0\). Conjugation handles the opposite rotational eigenvalue.

The finite-delay characteristic equations have only finitely many roots in each half-plane \(\operatorname{Re}\lambda\ge-\eta\), because there \(|\lambda-i\omega_j|\le\kappa e^{\eta S}\). Thus absence of roots in the closed right half-plane gives a strictly negative spectral bound. Standard linear retarded-equation theory then gives exponential decay of every error history. In the concrete example, \(S=13\pi/6\), \(c=1/2\), and \(1/100<c/(4S)\), establishing the asserted stability.

## Verification
Execute `python verify.py` with Python 3. The checker compares the exact two-frequency feedback cancellation at multiple times, confirms the two phase aliases, and checks the explicit root-exclusion inequality. Numerical checks illustrate exact identities and are not substituted for the proof. The analytic characteristic-root exclusion provides the infinite-dimensional stability argument.

## Relationship to prior work
Ortiz del Campo, Galla, and Toral introduced the normalized distributed-delay driver–response framework and analyzed mode-dependent anticipation, reporting generic failure of a common shift in two-mode examples. Their equations permit exceptional resonant delay distributions, but their results do not classify their support or exhibit the stable two-delay example above. The general single-delay anticipation construction is classical (Voss), and the unit-modulus expectation criterion is a standard elementary Fourier/probability observation; neither is claimed novel in isolation. The contribution is the sharp arithmetic *if-and-only-if* boundary with an explicit exponentially attracting nondegenerate two-frequency counterexample to generic loss of exact anticipation. Earlier distributed-delay synchronization literature studies other synchronization arrangements and does not establish this claimed boundary in the inspected material.

## Limitations
The theorem concerns harmonic, finite-dimensional drivers under scalar linear distributed self-feedback, not general chaotic synchronization. It proves existence of the exact shifted trajectory for any admissible Borel measure but establishes exponential attraction only with bounded delay support and the given sufficient coupling bound, which is not claimed optimal. The lattice-supported examples are discrete delay laws rather than absolutely continuous broad kernels: incommensurate two-frequency drivers forbid every nonsingleton positive delay law. Historical priority outside inspected primary and retrieved published records remains provisional; independent validation has not been performed.

## References
Ortiz del Campo, D., Galla, T., and Toral, R. (2026). *Anticipated synchronization in systems with distributed delay*, arXiv:2603.02918v1, first posted March 3, 2026. https://arxiv.org/abs/2603.02918

Voss, H. U. (2000). *Anticipating chaotic synchronization*. Physical Review E 61, 5115–5119 (fixed-delay construction; identified through the cited primary work).

Wetzel, L., Morelli, L. G., Oates, A. C., Jülicher, F., and Ares, S. (2016). *Synchronization in the presence of distributed delays* (distinct network-synchronization setting; abstract examined).
