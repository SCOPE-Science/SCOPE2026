# Parity-dependent Wigner-negativity threshold under Poisson Fock re-preparation and photon loss

## Finding
Let \(n\ge1\) be an integer, and let \(\alpha=r/\gamma>0\). In the loss-and-re-preparation model defined below, the unique stationary occupation probabilities are
\[
p_k(\alpha)=\frac{\alpha n!\,\Gamma(\alpha+k)}{k!\,\Gamma(\alpha+n+1)},\qquad k=0,\ldots,n.
\]
The stationary von Neumann entropy is strictly increasing for \(0<\alpha<1\), strictly decreasing for \(\alpha>1\), and has the unique maximum \(\log(n+1)\) at \(\alpha=1\). The stationary Wigner function is pointwise nonnegative for exactly one initial rate interval \(0<\alpha\le\alpha_n\), where \(\alpha_n=1\) for every odd \(n\), whereas \(1<\alpha_n<\infty\) for every even \(n\). In the two-photon case, \(\alpha_2\) is the unique positive zero of \(\alpha^3-\alpha-2\), approximately \(1.52137970680457\); beyond it the negative Wigner region is one annulus.

## Assumptions and scope
The system consists of one bosonic mode with annihilation operator \(b\), vacuum reservoir, one-photon Lindblad loss of rate \(\gamma>0\), and independent full-state Poisson re-preparation to the pure number state \(\rho_n=\lvert n\rangle\langle n\rvert\) at rate \(r>0\). Its trace-preserving master equation is
\[
\dot\rho=\gamma\left(b\rho b^\dagger-\tfrac12\{b^\dagger b,\rho\}\right)+r(\rho_n\operatorname{tr}\rho-\rho).
\]
A free harmonic phase rotation may be included: it does not affect number-diagonal stationary states. No thermal excitation, multi-photon loss, selective addition, or feedback control is assumed. A Wigner-positive state means its symmetrically ordered Wigner function is pointwise nonnegative; it need not have a positive Glauber--Sudarshan representation. Rates are scaled only by \(\alpha=r/\gamma\).

## Proof
**Stationary law and uniqueness.** Let \(T_t\) be the zero-temperature loss channel. Its action on a number state is the binomial thinning law
\[
T_t(\rho_n)=\sum_{k=0}^n\binom nk e^{-k\gamma t}(1-e^{-\gamma t})^{n-k}\lvert k\rangle\langle k\rvert.
\]
Condition on the age \(t\) since the last preparation. Its density is \(re^{-rt}\), so the stationary state is \(\rho_\alpha=\int_0^\infty re^{-rt}T_t(\rho_n)\,dt\). Under \(u=e^{-\gamma t}\), the measure becomes \(\alpha u^{\alpha-1}du\) on \((0,1)\), and beta integration gives the stated \(p_k\). The reset term contracts the trace distance of two evolving states by at least \(e^{-rt}\); hence the stationary state is globally unique. Its balance equations are \(\gamma[(k+1)p_{k+1}-kp_k]+r(\boldsymbol 1_{k=n}-p_k)=0\), with \(p_{n+1}=0\).

**Entropy and majorization.** The ratio \(p_{k+1}/p_k=(\alpha+k)/(k+1)\) is less than, equal to, or greater than unity uniformly in \(k<n\) according as \(\alpha<1\), \(\alpha=1\), or \(\alpha>1\). Thus \(p_k(1)=1/(n+1)\). For \(\alpha_2>\alpha_1\), the likelihood ratio \(p_k(\alpha_2)/p_k(\alpha_1)\) strictly increases with \(k\); therefore every proper low-index cumulative probability strictly decreases with \(\alpha\). For \(\alpha<1\), the descending occupation vector has the original index order; increasing \(\alpha\) strictly reduces each proper sum of the largest components. For \(\alpha>1\), the descending vector has reversed index order; increasing \(\alpha\) strictly increases each proper largest-component sum. Strict Schur concavity of Shannon entropy proves its stated strict monotonicity and unique maximum. For a diagonal density matrix this Shannon entropy is the von Neumann entropy.

**Wigner polynomial and rate order.** For phase-space amplitude \(w\in\mathbb C\), put \(z=4|w|^2\ge0\). The number-state Wigner formula gives
\[
W_{n,\alpha}(w)=\frac2\pi e^{-z/2}P_{n,\alpha}(z),\qquad P_{n,\alpha}(z)=\sum_{k=0}^n(-1)^kp_k(\alpha)L_k(z).
\]
Let \(R_a=\int_0^\infty ae^{-at}T_t\,dt\), now measuring time in units of \(1/\gamma\). For \(0<a<b\), the operator resolvent identity reads
\[
R_a=\frac ab R_b+\left(1-\frac ab\right)R_aR_b.
\]
The vacuum-loss channel \(T_t\) takes each pointwise nonnegative Wigner function to a nonnegative Wigner function, since its Wigner action is a rescaled positive Gaussian convolution. The same holds for its exponential mixture \(R_a\). Applying the identity to \(\rho_n\), if the state at a larger rate \(b\) is Wigner-positive, then the state at every smaller positive rate \(a\) is also Wigner-positive. Thus the Wigner-positive rates form an initial interval. Continuity of polynomial coefficients, together with a uniformly positive leading coefficient, proves closure at any finite positive endpoint.

**The uniform endpoint and parity.** The key existing balanced-beam-splitter identity is
\[
\frac1{n+1}\sum_{m=0}^{n}\sigma(m,n-m)=\frac1{n+1}\sum_{k=0}^n\lvert k\rangle\langle k\rvert,
\]
where \(\sigma(m,n-m)\) is the reduced output of a balanced beam splitter with Fock inputs \(\lvert m\rangle\), \(\lvert n-m\rangle\). Each \(\sigma\) has a nonnegative Wigner function (Vanbever, 2021, Lemma 2 and Eq. (30), building on the nonnegative convolution of two pure-state Wigner functions). Therefore the uniform state \(\rho_1\) is Wigner-positive. Moreover the summand \(\sigma(0,n)\) has polynomial \(\sum_{k=0}^n2^{-n}\binom nk(-1)^kL_k(z)=(z/2)^n/n!\), strictly positive for \(z>0\). Thus \(P_{n,1}(z)>0\) for every \(z>0\). At the origin it is \(P_{n,1}(0)=(1+(-1)^n)/(2(n+1))\).

If \(n\) is odd, the origin value is
\[
P_{n,\alpha}(0)=\alpha\int_0^1u^{\alpha-1}(1-2u)^n\,du.
\]
Pairing \(u\) with \(1-u\) on \((0,1/2)\) proves this integral strictly negative when \(\alpha>1\), strictly positive when \(0<\alpha<1\), and zero when \(\alpha=1\). The initial-interval property proves \(\alpha_n=1\) for odd \(n\).

If \(n\) is even, the origin value at \(\alpha=1\) is strictly positive as well, so \(P_{n,1}\) is strictly positive on \([0,\infty)\). Its leading coefficient is \(p_n(\alpha)/n!>0\), continuous and locally bounded away from zero at \(\alpha=1\). For \(\alpha\) in a sufficiently small compact neighborhood of unity, the leading term dominates the lower polynomial powers uniformly outside a large compact \(z\)-interval, while uniform continuity preserves positivity inside. Thus \(\alpha_n>1\). On the other hand \(\rho_\alpha\to\rho_n\) as \(\alpha\to\infty\); every nonvacuum pure Fock state has some negative Wigner value, so \(\alpha_n<\infty\). Initial-interval order and continuity supply the one sharp boundary.

**Exact two-photon boundary.** At \(n=2\), direct evaluation yields
\[
P_{2,\alpha}(z)=\frac{\alpha^2-\alpha+2-2\alpha^2z+\frac12\alpha(\alpha+1)z^2}{(\alpha+1)(\alpha+2)}.
\]
Its unique minimum on \(z\ge0\) is attained at \(z_*=2\alpha/(\alpha+1)\) with value \((-\alpha^3+\alpha+2)/((\alpha+1)^2(\alpha+2))\). Hence positivity holds precisely when \(\alpha^3-\alpha-2\le0\). The cubic has exactly one positive root, between 1 and 2. Above it the upward-opening quadratic is negative between two strictly positive roots; the phase-space negative set is an annulus.

## Verification
Run `python checker.py` with SymPy installed. The checker tests finite-family exact identities for occupation probabilities, Lindblad balance equations, uniform mixing, Laguerre polynomial normalization and leading coefficients, the balanced-loss identity, the complete \(n=2\) Wigner polynomial/minimum and rational test cases of strict occupation-vector majorization. It passes 642 exact symbolic identities and rational inequalities. The all-\(n\), all-rate claims follow from the analytic resolvent/majorization/beam-splitter proofs, not finite tests. The beam-splitter Wigner-positivity lemma is a cited prior published result; its concrete decomposition and strict positive component are explicitly identified above.

## Relationship to prior work
Vanbever (first public 2021-04-30) proves the Wigner positivity of equally weighted initial Fock mixtures, with balanced-beam-splitter decomposition, but does not consider the stationary law of Fock re-preparation competing with continuous photon loss, its rate ordering or odd/even cutoffs. Nugmanov, Zunikov and Khalili (first public 2022-01-10) prove the universal one-half transmissivity threshold for Wigner negativity under a *fixed-duration pure-loss channel acting on a pure non-Gaussian input*; that is not the mixed state obtained by a stochastic reset-age distribution, and their text explicitly distinguishes mixed inputs. Li and collaborators (first public 2023-08-16) implement cascaded selective photon addition rather than full-state Poisson re-preparation; their detailed process is non-equivalent. A broader dissipative quantum-control classification might implicitly contain some special cases; a global novelty theorem is not claimed.

## Limitations
The result concerns a zero-temperature one-photon loss semigroup, an ideal instantaneous state-preparation operation, and fixed finite photon index \(n\). The even-index threshold is known to exist uniquely, but no general closed form or asymptotic in \(n\) is proved; only the two-photon case is explicitly solved. Wigner positivity is not equivalent to positivity of the Glauber--Sudarshan representation. Physical implementation cost and noise in the preparation operation are outside the model. Independent expert review of publication priority has not occurred.

## References
1. L. Vanbever, *In Wigner phase space, convolution explains why the vacuum majorizes mixtures of Fock states*, arXiv:2104.14996, first public 2021-04-30, https://arxiv.org/abs/2104.14996 ; especially Lemma 2 and Eq. (30), full text https://arxiv.org/pdf/2104.14996 .
2. B. Nugmanov, N. Zunikov, F. Ya. Khalili, *Robustness of negativity of the Wigner function to dissipation*, arXiv:2201.03257, first public 2022-01-10, https://arxiv.org/abs/2201.03257 .
3. S. Li et al., *Autonomous Stabilization of Fock States in an Oscillator against Multiphoton Losses*, arXiv:2308.08296, first public 2023-08-16, https://arxiv.org/abs/2308.08296 .
