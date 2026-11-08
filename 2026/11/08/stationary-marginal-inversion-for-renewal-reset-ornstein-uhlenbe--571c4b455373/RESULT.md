# Stationary-marginal inversion for renewal-reset Ornstein–Uhlenbeck motion: exact identifiability and smooth instability

## Finding

**Theorem (one-time inverse law, realizability, and its limitations).** Fix \(\kappa,D>0\). Between complete resets to zero, let \(X\) solve \(dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dB_t\), using fresh independent Brownian increments after each reset. The reset intervals \(T\) are independent, identically distributed, strictly positive and independent of Brownian motion, with finite mean \(\mu=\mathbb ET\). Observe the process in its equilibrium-renewal regime, with stationary position law \(P_T\). Put \(s^2=D/\kappa\).

1. **Exact inversion and image.** The *entire one-time* law \(P_T\), with known \(\kappa,D\), uniquely determines the law of \(T\), including its mean. Specifically, write \(U=e^{-2\kappa A}\), where \(A\) is the equilibrium age since the most recent reset. Its density is
   \[
   g(u)=\frac{\mathbb P(T>-\log(u)/(2\kappa))}{2\kappa\mu\,u},\qquad 0<u<1.
   \]
   The position characteristic function and even moments are
   \[
   \phi_{P_T}(t)=\int_0^1\exp[-s^2(1-u)t^2/2]\,g(u)\,du,\qquad
   \frac{\mathbb E_{P_T}X^{2j}}{(2j-1)!!\,s^{2j}}=\int_0^1(1-u)^j g(u)\,du.
   \]
   Conversely, a probability law \(P\) is of the form \(P_T\) for a strictly positive, finite-mean renewal law precisely if its characteristic function has the displayed Gaussian-mixture representation for a probability density \(g\) on \((0,1)\) such that \(q(u)=u g(u)\) admits a nondecreasing left-continuous version on \((0,1)\) with \(0<c:=\lim_{u\uparrow1}q(u)<\infty\). Such \(g\) is unique up to null sets, and the exact inverse is
   \[
   \mu=\frac1{2\kappa c},\qquad
   \mathbb P(T>a)=\frac{q(e^{-2\kappa a})}{c},\quad a\ge0,
   \]
   with the convention \(q(1)=c\) and the indicated left-continuous choice at discontinuities of \(q\).

2. **Finite-moment aliases at any prescribed mean.** For each \(K\ge1\), each target mean \(\mu>0\), and the same fixed \(\kappa,D\), there exist two distinct reset-time laws having strictly positive smooth densities and mean \(\mu\) whose first \(K\) stationary even moments agree exactly. Thus any finite initial block of moments, including odd moments, cannot uniquely identify the reset law.

3. **Ill-conditioning even for smooth laws at fixed mean.** For every fixed \(\kappa,D\), there exist a smooth positive waiting-time law \(T_0\) of mean \(1/(2\kappa)\) and smooth positive laws \(T_n\) of that same mean such that
   \[
   \|P_{T_n}-P_{T_0}\|_{\mathrm{TV}}\longrightarrow0,
   \qquad\liminf_{n\to\infty}\|\mathcal L(T_n)-\mathcal L(T_0)\|_{\mathrm{TV}}>0.
   \]
   More explicitly, for any nonzero nonnegative \(\eta\in C_c^\infty((1/3,2/3))\) and sufficiently small fixed \(\varepsilon>0\), the construction in the proof has limiting reset-law total-variation distance \(\frac{\varepsilon}{\pi}\int_0^1u\eta(u)\,du\) while its position-law distance is \(O(n^{-1})\).

Here total variation is \(\|P-Q\|_{\mathrm{TV}}=\sup_B|P(B)-Q(B)|\). Parts 1–3 jointly describe exact theoretical identifiability, finite-moment nonidentifiability, and severe inverse instability.

## Assumptions and scope

The environment is one-dimensional, overdamped and has **known** positive relaxation \(\kappa\) and diffusion coefficient \(D\). At a reset, the position is exactly zero; independent Brownian forcing begins afresh. Resets are exogenous renewal events with strictly positive interarrival times and finite mean, and are independent of the Brownian path. The equilibrium-renewal observation is the long-time invariant-time sampling convention; for arithmetic interarrival laws it includes randomized equilibrium phase, rather than asserting an unphased pointwise temporal limit. No assumption of a waiting-time density is needed in Part 1; deterministic and discrete reset intervals are included. Parts 2–3 additionally use smooth, strictly positive waiting-time densities. All recovery statements concern an ideal complete probability law with known dynamical parameters, not finite-sample statistical estimation.

## Proof

**1. Last-reset mixture.** In an equilibrium renewal process, the age \(A\) has density \(f_A(a)=\mathbb P(T>a)/\mu\) on \([0,\infty)\). Conditional on age \(a\), a fresh Ornstein–Uhlenbeck trajectory from zero is centered Gaussian with variance \(s^2(1-e^{-2\kappa a})\). Therefore \(P_T\) is the corresponding mixture. The monotone transformation \(u=e^{-2\kappa a}\), with \(|da/du|=(2\kappa u)^{-1}\), gives the stated density \(g\), characteristic function and Gaussian even-moment formula. All moments exist because the conditional variance never exceeds \(s^2\).

**2. Uniqueness of mixing and inverse image.** Define \(V=1-U\in(0,1)\). The normalized even moment of order \(2j\) is \(\mathbb EV^j\). These moments, for all integers \(j\ge0\), uniquely determine a probability measure on \([0,1]\) by the Hausdorff moment theorem (equivalently, density of polynomials in continuous functions). Thus \(P_T\) uniquely determines the law of \(U\), and therefore the a.e. density \(g\). The positive finite-mean reset law entails \(q(u)=u g(u)=\mathbb P(T> -\log u/(2\kappa))/(2\kappa\mu)\). Its canonical representative is nondecreasing and left-continuous since \(a\mapsto\mathbb P(T>a)\) is nonincreasing and right-continuous. As \(u\uparrow1\), strict positivity of \(T\) implies \(q(u)\to1/(2\kappa\mu)=c\). The claimed inversion follows.

Conversely, take any density \(g\) satisfying the monotonicity, continuity and endpoint conditions. Extend \(q\) to \(u=1\) by \(q(1)=c\), and normalize \(S(a)=q(e^{-2\kappa a})/c\), using the canonical left-continuous version of \(q\). It is right-continuous, nonincreasing and satisfies \(S(0)=1\). Also \(\lim_{u\downarrow0}q(u)=0\), because a positive limit would contradict \(\int_0^1q(u)\,du/u=1\). Hence \(S(a)\to0\) at infinity and defines a strictly positive finite random variable \(T\) through \(S(a)=\mathbb P(T>a)\). Its mean is exactly
\[
\mathbb ET=\int_0^\infty S(a)\,da
=\frac1{2\kappa c}\int_0^1\frac{q(u)}{u}\,du
=\frac1{2\kappa c}.
\]
The forward change-of-variable formula returns \(g\) and therefore \(P\), completing the exact range statement.

**3. Infinitely many finite-moment aliases.** Given \(K\ge1\) and target \(\mu>0\), set \(\alpha=(2\kappa\mu)^{-1}\), and begin with the exponential-reset mixing density \(g_0(u)=\alpha u^{\alpha-1}\) and \(q_0(u)=\alpha u^\alpha\). Choose nonzero \(\psi\in C_c^\infty((1/3,2/3))\) with \(\psi^{(K+1)}\not\equiv0\). Set
\[
g_\pm(u)=\alpha u^{\alpha-1}\pm\delta\psi^{(K+1)}(u),\quad
q_\pm(u)=u g_\pm(u).
\]
Repeated integration by parts gives \(\int_0^1 u^j\psi^{(K+1)}(u)\,du=0\) for every integer \(0\le j\le K\). Thus \(g_\pm\) are normalized and have the same first \(K\) polynomial moments, and hence the same moments of \(1-U\) through degree \(K\). On the compact support of the perturbation, both \(g_0\) and \(q_0'\) have strictly positive minima. Taking \(\delta>0\) sufficiently small makes \(g_\pm>0\) and \(q_\pm'>0\) everywhere. Off that support, the unperturbed functions are unchanged. Their endpoint values satisfy \(q_\pm(1-)=\alpha\), so the inverse in Step 2 yields two distinct strictly positive smooth reset-time densities of the same prescribed mean \(\mu\). They produce exactly equal stationary moments up to \(2K\), whereas their full stationary laws differ by Step 2.

**4. Smooth fixed-mean total-variation instability.** Choose nonzero \(\eta\ge0\) in \(C_c^\infty((1/3,2/3))\), and let the baseline be \(g_0(u)=1\), \(q_0(u)=u\), corresponding to \(T_0\sim\mathrm{Exp}(2\kappa)\). For positive integers \(n\) define
\[
g_n(u)=1+\frac{\varepsilon}{n^2}\frac{d}{du}[\eta(u)\cos(nu)],\qquad q_n(u)=u g_n(u).
\]
The perturbation integrates to zero and is supported away from both endpoints, so \(\int_0^1g_n=1\) and \(q_n(1-)=1\). Uniformly in \(u\),
\[
q_n'(u)=1-\varepsilon u\eta(u)\cos(nu)+O(\varepsilon/n).
\]
Fix \(\varepsilon>0\) small enough that \(\varepsilon\sup_u u\eta(u)<1/4\). For all sufficiently large \(n\), the densities \(g_n\) are positive and \(q_n'\) is bounded below by \(1/2\). The inverse construction therefore gives smooth positive interarrival densities \(f_{T_n}(a)=2\kappa e^{-2\kappa a}q_n'(e^{-2\kappa a})\), all with mean \(1/(2\kappa)\). Mixing with a probability kernel cannot increase total variation, whence
\[
\|P_{T_n}-P_{T_0}\|_{\mathrm{TV}}
\le\frac12\int_0^1|g_n(u)-1|\,du=O(\varepsilon/n).
\]
On the other hand, the change of variable \(u=e^{-2\kappa a}\) and the common endpoint constant give exactly
\[
\|\mathcal L(T_n)-\mathcal L(T_0)\|_{\mathrm{TV}}
=\frac12\int_0^1|q_n'(u)-1|\,du.
\]
The uniform derivative approximation and the elementary averaging limit \(\int_0^1w(u)|\cos(nu)|\,du\to(2/\pi)\int_0^1w(u)\,du\) for continuous compactly supported \(w\) now yield
\[
\lim_{n\to\infty}\|\mathcal L(T_n)-\mathcal L(T_0)\|_{\mathrm{TV}}
=\frac{\varepsilon}{\pi}\int_0^1u\eta(u)\,du>0.
\]
This proves all three parts.

## Verification

Run the dependency-free Python 3 script `python3 verify.py`. It checks rational Hausdorff/Gaussian moments for an exponential reference law, verifies exact polynomial-perturbation cancellations through a nontrivial finite-moment example, exercises the mean-normalization identity for deterministic intervals, and checks the analytically derived total-variation age formula for a discrete contrast. These are finite arithmetic diagnostics; they do not replace the proof of uniqueness, monotonicity, the existence of smooth aliases, or the infinite-frequency averaging limit. In particular, the smooth-instability limit is proved analytically in Step 4.

## Relationship to prior work

Masoliver and Montero, *Anomalous diffusion under stochastic resettings: A general approach* (Phys. Rev. E 100, 042103, 2019), provide an arbitrary-renewal forward stationary-density integral, likewise not an inverse classification. Eule and Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting* (arXiv:1510.07876), establish the arbitrary-renewal resetting framework and general forward stationary mixtures. Lapeyre and Dentz, *Unified approach to reset processes and application to coupling between process and reset* (arXiv:1903.08055), likewise provide general reset-age functional formulas. Olsen, *Steady-state moments under resetting to a distribution* (arXiv:2310.04840; first publicly posted 7 October 2023), explicitly computes Ornstein–Uhlenbeck moments for **Poisson** reset intervals and variable spatial reset positions, and discusses non-Poisson intervals as a further direction. The result here fixes the spatial reset point and instead reconstructs a **general renewal interarrival law from one complete stationary position marginal**. Jolakoski, *Ridge Regression from Poisson Resetting: A Renewal Perspective on Spectral Regularization* (arXiv:2605.30059), studies equilibrium-age Laplace transforms as deterministic gradient-flow spectral filters across curvatures and an additive-noise extension; that broader renewal-age machinery is relevant, but the single-OU-marginal image criterion and fixed-mean smooth inverse discontinuity are different claims. Standard Gaussian-scale-mixture identifiability and the Hausdorff moment theorem are used rather than claimed as new.

## Limitations

No finite set of stationary moments, and no finitely sampled empirical position histogram, supplies the exact inverse without additional model constraints; the smooth-law instability makes inversion ill-conditioned under total variation. The theorem assumes known \(\kappa,D\), complete zero resets, exogenous finite-mean renewal intervals and equilibrium-time observation. It does not address joint identification of dynamical and reset parameters, dependent resets, imperfect or spatially distributed resets, infinite-mean stationary regimes, rates of statistical estimation, or finite observation windows. The general renewal mixture, Gaussian-mixture uniqueness and age-transform properties are prior mathematical ingredients; publication priority of the assembled inverse classification and smooth instability has not been independently established against all unindexed literature.

## References

1. K. S. Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840, first posted 2023-10-07. https://arxiv.org/abs/2310.04840
2. S. Eule and J. J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, arXiv:1510.07876, first posted 2015-10-27. https://arxiv.org/abs/1510.07876
3. G. J. Lapeyre Jr. and M. Dentz, *Unified approach to reset processes and application to coupling between process and reset*, arXiv:1903.08055, first posted 2019-03-19. https://arxiv.org/abs/1903.08055
4. P. Jolakoski, *Ridge Regression from Poisson Resetting: A Renewal Perspective on Spectral Regularization*, arXiv:2605.30059, first posted 2026-05-28. https://arxiv.org/abs/2605.30059
5. J. Masoliver and M. Montero, *Anomalous diffusion under stochastic resettings: A general approach*, Physical Review E 100, 042103 (2019). https://doi.org/10.1103/PhysRevE.100.042103
6. Classical Hausdorff moment-determinacy theorem on the compact interval \([0,1]\); used as standard prior mathematics.
