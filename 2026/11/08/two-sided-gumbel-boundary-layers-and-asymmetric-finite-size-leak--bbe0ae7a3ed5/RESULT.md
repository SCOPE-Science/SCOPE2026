# Two-sided Gumbel boundary layers and asymmetric finite-size leakage in a switching harmonic gas

## Finding

Consider a stationary population of \(N\) noninteracting one-dimensional Brownian particles in the same two-state, randomly switching harmonic trap. For the maximum position \(M_N=\max_{1\le j\le N}X_j\), the already-established leading large-\(N\) law of \(M_N/\sqrt{2\log N}\) has a compact interval of support. This result determines **both sharp finite-size edges** of that interval, the conditional localization of the hidden trap variance in edge events, and the unequal powers governing leakage at the two *unshifted* limiting endpoints.

Define \(L=\log N\),
\[
 a_N=\sqrt{2L}-\frac{\log L+\log(4\pi)}{2\sqrt{2L}},\qquad b_N=(2L)^{-1/2},
\]
and the standard Gumbel distribution function \(G(t)=\exp(-e^{-t})\). Define positive parameters \(v_-<v_+\), \(\Delta=v_+-v_-\), \(\alpha,\beta>0\), \(\overline v\), and the positive constants
\[
 A_- =\frac{v_-}{\overline v\,\mathrm B(\alpha,\beta)}\left(\frac{v_-}{\Delta}\right)^\alpha,
 \qquad
 A_+ =\frac{v_+}{\overline v\,\mathrm B(\alpha,\beta)}\left(\frac{v_+}{\Delta}\right)^\beta.
\]
Their physical definitions are in the next section. Then, for each fixed real \(t\), as integers \(N\to\infty\),
\[
 \boxed{L^\alpha\Pr\!\left(M_N\le\sqrt{v_-}(a_N+b_Nt)\right)
 \longrightarrow A_-\int_0^\infty s^{\alpha-1}G(t-s)\,ds,}
\]
\[
 \boxed{L^\beta\Pr\!\left(M_N>\sqrt{v_+}(a_N+b_Nt)\right)
 \longrightarrow A_+\int_0^\infty s^{\beta-1}[1-G(t+s)]\,ds.}
\]
Both limits are finite and strictly positive, with convergence locally uniform in \(t\). Consequently the lower and upper edges have different logarithmic powers, determined by the trap's two switching-rate-to-stiffness ratios.

For the leading-law endpoints **without Gaussian extreme-value recentering**, the corresponding rare-event probabilities exhibit a further asymmetry:
\[
 \boxed{\Pr\!\left(M_N\le\sqrt{2v_-\log N}\right)
 \sim\frac{A_-}{\alpha}\left(\frac{\log\log N}{2\log N}\right)^\alpha,}
\]
\[
 \boxed{\Pr\!\left(M_N>\sqrt{2v_+\log N}\right)
 \sim\frac{A_+\Gamma(\beta)}{\sqrt{4\pi}}(\log N)^{-\beta-1/2}.}
\]
Thus a single apparent hard support edge hides two qualitatively different types of finite-size leakage: a \(\log\log N\) enhancement below the lower edge, versus an extra Gaussian extreme-value factor \((\log N)^{-1/2}\) above the upper edge.

The profiles also identify the environmental state selected by a rare extreme event. Let \(U\) denote the common stationary variance-mixture coordinate defined below. Conditional on the lower-edge event in the first display, the random variable \(S_{-,N}=L\Delta U/v_-\) converges weakly to the density
\[
 \frac{s^{\alpha-1}G(t-s)}{\int_0^\infty z^{\alpha-1}G(t-z)\,dz},\qquad s>0.
\]
Conditional on the upper-edge exceedance in the second display, \(S_{+,N}=L\Delta(1-U)/v_+\) converges weakly to
\[
 \frac{s^{\beta-1}[1-G(t+s)]}{\int_0^\infty z^{\beta-1}[1-G(t+z)]\,dz},\qquad s>0.
\]
These are statements about the hidden variance conditional on an observed extreme event, not about independently observed trap-state trajectories.

## Assumptions and scope

Fix positive constants \(D,\mu_1,\mu_2,r_1,r_2\), with \(\mu_1>\mu_2>0\). For each \(N\ge1\), particles evolve in a shared stationary environment \(J_t\in\{1,2\}\) that jumps from state \(1\) to state \(2\) at rate \(r_1\), and conversely at rate \(r_2\). Given \(J\), the particle noises are independent and
\[
 dX_j(t)=-\mu_{J_t}X_j(t)\,dt+\sqrt{2D}\,dW_j(t),\quad 1\le j\le N.
\]
The probability laws asserted above refer to the joint stationary distribution and to a fixed physical parameter tuple as \(N\to\infty\). Set
\[
 v_- =D/\mu_1,\quad v_+=D/\mu_2,\quad \Delta=v_+-v_-,\quad
 \alpha=r_1/(2\mu_1),\quad\beta=r_2/(2\mu_2),\quad
 \overline v=v_-+\Delta\alpha/(\alpha+\beta).
\]
Here \(\mathrm B\) is the Euler beta function. The exact stationary conditional-Gaussian representation from Biroli, Kulkarni, Majumdar and Schehr is
\[
 U\in(0,1),\qquad
 h(u)=\frac{v_-+\Delta u}{\overline v\,\mathrm B(\alpha,\beta)}u^{\alpha-1}(1-u)^{\beta-1},\qquad
 (X_1,\ldots,X_N)\mid U=u\;\overset{d}=\;\big(\sqrt{v_-+\Delta u}\,Z_1,\ldots,\sqrt{v_-+\Delta u}\,Z_N\big),
\]
where \(Z_j\) are i.i.d. standard normal, independent of \(U\). This mixture is **prior work**, not a new assertion of this result. Its normalization follows from the ordinary beta integral and the expression for \(\overline v\). No direct particle interactions or state-dependent diffusion are included.

## Proof

**1. Exact finite-population starting point.** Write \(\Phi\) for the standard normal distribution function. Conditional independence gives for all real \(x\)
\[
 F_N(x):=\Pr(M_N\le x)=\int_0^1h(u)\Phi\!\left(\frac{x}{\sqrt{v_-+\Delta u}}\right)^Ndu.
 \tag{1}
\]
The exact equation is recorded to specify the normalization and to make both tail probabilities unambiguous. The new content is the nonuniform endpoint analysis of this integral.

**2. Gaussian-maximum scaling and compact-uniform estimates.** The elementary normal Mills bounds imply, for every fixed \(z\in\mathbb R\),
\[
 N\{1-\Phi(a_N+b_Nz)\}\longrightarrow e^{-z},\qquad
 \Phi(a_N+b_Nz)^N\longrightarrow G(z).
 \tag{2}
\]
The convergence is uniform for \(z\) in compact sets. The first conclusion follows by inserting the displayed expression for \(a_N\) into \(\overline\Phi(x)\sim e^{-x^2/2}/(x\sqrt{2\pi})\); the second follows from \((1-w_N)^N\to e^{-\lambda}\) if \(Nw_N\to\lambda\). Moreover the same two-sided Mills estimates imply the following integrable endpoint envelopes for each fixed bounded interval of \(t\): after substituting \(u=(v_-/\Delta)s/L\) in the lower integral, the rescaled integrands are bounded in the growing domain by \(C s^{\alpha-1}H_-(s)\), where \(H_-\) is bounded near zero and decays faster than \(e^{-cs}\) for large \(s\); after substituting \(1-u=(v_+/\Delta)s/L\) in the upper tail, they are bounded by \(C s^{\beta-1}e^{-cs}\) for large \(s\), with fixed positive \(C,c\). To see these bounds without a uniform Gumbel approximation at unbounded \(s\), apply \(\Phi(x)^N\le\exp[-N\overline\Phi(x)]\) in the lower case and \(1-\Phi(x)^N\le\min\{1,N\overline\Phi(x)\}\) in the upper case, then divide the \(s\)-domain into \(s\le\varepsilon L\) and \(s>\varepsilon L\), for a sufficiently small fixed \(\varepsilon\). The first range has an exponent respectively growing at least as \(e^{c s}\) or decaying at least as \(e^{-cs}\) by Mills' inequalities and \(v_-\le v(u)\le v_+\). The second contributes an exponentially (indeed, for the lower case, super-exponentially) small remainder in \(L\). This also supplies the domination required for the conditional measures in Step 4.

**3. Both centered edge limits.** At the lower edge put \(u=v_-s/(\Delta L)\), with fixed \(s\ge0\). Taylor expansion of the square-root ratio and \(a_N/b_N=2L+O(\log L)\) yields
\[
 \frac{\sqrt{v_-}(a_N+b_Nt)}{\sqrt{v_-+\Delta u}}
   =a_N+b_N(t-s+o(1)),
\]
while the transformed mixing measure satisfies
\[
 L^\alpha h(u)\,du\longrightarrow A_-s^{\alpha-1}ds.
\]
Equations (1)–(2), the integrable envelope from Step 2 and dominated convergence establish the first limit. At the upper edge put \(1-u=v_+s/(\Delta L)\). Then
\[
 \frac{\sqrt{v_+}(a_N+b_Nt)}{\sqrt{v_-+\Delta u}}
  =a_N+b_N(t+s+o(1)),\qquad
 L^\beta h(u)\,du\longrightarrow A_+s^{\beta-1}ds.
\]
Use \(1-F_N(x)\) in (1) and the same domination to obtain the second limit. The limiting integrals converge: \(G(t-s)\) decreases double-exponentially as \(s\to\infty\), while \(1-G(t+s)\sim e^{-t-s}\). Both integrands are positive. Compact uniformity in \(t\) follows from the same envelopes and continuity.

**4. Conditional environmental localization.** For every bounded continuous test function \(\varphi\), multiply the transformed integrands in Step 3 by \(\varphi(s)\) before taking the limit. Divide the resulting joint rare-event limits by the two strictly positive rare-event probabilities. This produces exactly the two probability densities displayed in the finding and proves weak convergence. The argument does not assume the environmental state itself is directly measured.

**5. Leakage at the unshifted lower endpoint.** Let \(x=\sqrt{2v_-L}\) and use \(s=L\Delta u/v_-\). For \(s=O(\log L)\), Mills' formula, uniformly in bounded multiples of \(\log L\), gives
\[
 N\overline\Phi\!\left(\frac{x}{\sqrt{v_-+\Delta u}}\right)
   =(4\pi L)^{-1/2}e^{s+o(1)}.
 \tag{3}
\]
Write \(c_L=\tfrac12\log(4\pi L)\). At \(s\le(1-\varepsilon)c_L\), the conditional probability that the maximum is below \(x\) tends uniformly to \(1\); at \(s\ge(1+\varepsilon)c_L\), it tends uniformly to \(0\), and the outer range contributes negligibly by the same Gaussian bounds as in Step 2. The small-\(u\) mixing mass obeys
\[
 \Pr\!\left(U\le\frac{v_-y}{\Delta L}\right)
 \sim \frac{A_-}{\alpha}(y/L)^\alpha
\]
for \(y\to\infty\) with \(y=o(L)\). Sandwiching the integral between the two cutoffs and then letting \(\varepsilon\downarrow0\) proves
\[
 F_N(\sqrt{2v_-L})\sim\frac{A_-}{\alpha}(c_L/L)^\alpha
 \sim\frac{A_-}{\alpha}(\log L/(2L))^\alpha.
\]

**6. Leakage at the unshifted upper endpoint.** At \(x=\sqrt{2v_+L}\), the normal-tail bound gives \(N\overline\Phi(x/\sqrt{v(u)})\le C L^{-1/2}\) for all \(u\). Hence \(1-\Phi(x/\sqrt{v(u)})^N=N\overline\Phi(x/\sqrt{v(u)})(1+o(1))\) uniformly. Setting \(1-u=v_+s/(\Delta L)\), Mills' formula gives
\[
 N\overline\Phi\!\left(\frac{x}{\sqrt{v_-+\Delta u}}\right)
 \sim (4\pi L)^{-1/2}e^{-s}
\]
for fixed \(s\), with an integrable exponential envelope. The mixing Jacobian is \(A_+L^{-\beta}s^{\beta-1}ds(1+o(1))\). Integration gives \(\Gamma(\beta)\) and the second unshifted-edge asymptotic. The factor \(L^{-1/2}\) is essential; it would be lost by treating the Gaussian maximum as a deterministic \(\sqrt{2L}\).

This completes the proof for every fixed positive physical parameter tuple and each fixed real profile argument \(t\).

## Verification

A reproducible independent quadrature script is included as `verify_edge.py`. It evaluates the finite-\(N\) conditional-normal integral in (1), separately evaluates the proposed Gumbel fractional integrals, checks mixing-law normalization, and compares centered and unshifted endpoint probabilities for two asymmetric physical parameter choices, three profile positions and sample sizes up to \(10^{24}\). It successfully completed **66 numerical and integral diagnostic assertions**. The convergence is logarithmically slow; conservative tolerances deliberately avoid representing finite tests as proof. The analytic proof above supplies the infinite-\(N\) statements.

## Relationship to prior work

Biroli, Kulkarni, Majumdar and Schehr [1] derived the exact stationary common-variance mixture and the compactly supported leading scale law for the largest particle. The mixture \(h\), the Gaussian conditional law and the leading support are all credited to [1]. Biroli, Larralde, Majumdar and Schehr [2], especially their Section III.2.1, give the general conditional-i.i.d. extreme-value framework and leading Gumbel-class concentration; they do not state the finite-population two-endpoint fractional-Gumbel profiles or unequal raw-edge leakage rates. A subsequent experimental study [3] uses exact finite-\(N\) order-statistic formulas in the same switching-trap model, but presents no two-sided logarithmic endpoint theorem. A related 2026 study [4] analyzes confinement with *instantaneous simultaneous resetting* rather than finite-rate two-stiffness switching and discusses slowly resolved harmonic extreme edges. This creates a real overlap risk concerning generic upper-edge mechanisms; its available summary does not establish that its statements imply the full two-sided theorem here. The formulas and their stated domain, not a claim of priority over all possible general mixture theorems, define the contribution.

## Limitations

The result is for the maximum of **signed positions** in one dimension, not the maximum of distances or all order statistics. All model parameters are fixed and strictly positive, with two distinct positive stiffnesses. It is not uniform in the degenerate limits \(\mu_1\to\mu_2\), \(r_i\to0\), or a stiffness approaching zero, and it does not account for direct/hydrodynamic particle interactions, measurement noise or finite-sample estimation uncertainty. The proof establishes asymptotics and conditional weak limits, not a finite-\(N\) exact closed form for the new profiles, a convergence-rate bound, or experimental validation. Independent scientific replication and publication-priority assessment remain open.

## References

[1] M. Biroli, M. Kulkarni, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570v1 (first posted 2023-12-05); Phys. Rev. E **109**, L032106 (2024). https://arxiv.org/abs/2312.02570

[2] M. Biroli, H. Larralde, S. N. Majumdar, G. Schehr, *Exact extreme, order and sum statistics in a class of strongly correlated system*, arXiv:2307.15351v1 (2023-07-28); Phys. Rev. E **109**, 014101 (2024). https://arxiv.org/abs/2307.15351

[3] M. Biroli, S. Ciliberto, M. Kulkarni, S. N. Majumdar, A. Petrosyan, G. Schehr, *Experimental evidence for strong emergent correlations between particles in a switching trap*, arXiv:2508.07199v1 (2025-08-10); Phys. Rev. Lett. **137**, 037102 (2026). https://arxiv.org/abs/2508.07199

[4] G. de Mauro, S. N. Majumdar, G. Schehr, *Effects of confinement in a Brownian gas with simultaneous stochastic resetting and dynamically emergent correlations*, arXiv:2606.31634v1 (2026-06-30), potentially relevant upper-edge mechanism; only a detailed accessible summary was examined. https://arxiv.org/abs/2606.31634
