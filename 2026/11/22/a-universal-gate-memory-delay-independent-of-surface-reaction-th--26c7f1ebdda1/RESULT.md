# A universal gate-memory delay independent of surface-reaction thresholds

## Finding

A Brownian searcher on a half-line encounters a target that switches between reflecting and reactive states. After every Poisson positional reset, the accumulated reactive-state boundary local time and its independently sampled reaction threshold are replaced by fresh values. Compare (K) retaining the target's two-state conformation at the reset and (F) independently redrawing that conformation from its stationary law. **For every almost surely finite, nonnegative distribution of reaction thresholds, the difference in their unconditional mean reaction times is independent of the threshold distribution**, and is strictly positive:

\[
\boxed{\mathbb E T_{\mathrm K}-\mathbb E T_{\mathrm F}=
\frac{\beta}{\alpha(\alpha+\beta)}
\sqrt{\frac{r}{r+\alpha+\beta}}
\exp\!\left[-L\left(\sqrt{\frac{r+\alpha+\beta}{D}}-\sqrt{\frac rD}\right)\right]>0.}
\]

The numerical expression is known for a **perfectly absorbing open gate** [2, Eq. (49)]. The finding is its **distribution-universal extension** to arbitrary (including deterministic, gamma, or heavy-tailed) boundary-contact reaction thresholds that are redrawn at resets. It is not a new claim about the perfectly absorbing special case.

## Assumptions and scope

Fix \(D,L,r,\alpha,\beta>0\). Between resets a particle follows reflected Brownian motion \(X\) on \([0,\infty)\) with interior generator \(D\partial_{xx}\). An independent target gate \(G_t\in\{0,1\}\) has generator

\[
Q=\begin{pmatrix}-\alpha&\alpha\\\beta&-\beta\end{pmatrix},
\qquad \pi=\left(\frac{\beta}{\alpha+\beta},\frac{\alpha}{\alpha+\beta}\right).
\]

The target is fully reflecting when \(G_t=0\). When \(G_t=1\), it accumulates open-state boundary local time \(\ell_t^{(1)}=\int_0^t\mathbf 1_{\{G_u=1\}}\,d\ell_u\), with ordinary boundary local time normalized by

\[
\ell_t=\lim_{\varepsilon\downarrow0}\frac D\varepsilon\int_0^t\mathbf1_{\{0\le X_u<\varepsilon\}}\,du.
\]

A fresh random threshold \(\Lambda\ge0\), finite almost surely and independent of the trajectory and gate, is sampled at the beginning of each excursion; reaction occurs as soon as \(\ell_t^{(1)}\ge\Lambda\). If \(\Lambda=0\), reaction means the first encounter at the boundary *while the gate is open*, rather than immediate killing at the initial position. Poisson resets of rate \(r\) replace \(X\) by \(L\), \(\ell^{(1)}\) by zero, and \(\Lambda\) by an independent sample from its original distribution. Protocol K leaves \(G\) unchanged; protocol F independently redraws \(G\sim\pi\). Both start from \(X_0=L\) and independent \(G_0\sim\pi\). All waiting and reaction times are measured from this start.

These assumptions are essential: *retaining the accumulated contact threshold at resets* defines a different, generally nonrenewal problem and is not covered.

## Proof

**1. The no-reset transforms share a single reaction-law factor.** Let \(\tau\) be the first reaction time in one reset-free excursion, and write \(h_j(s)=\mathbb E_{L,j}[e^{-s\tau}]\). Set \(\sigma=\inf\{t\ge0:X_t=0,G_t=1\}\), the first boundary contact while the gate is open, with \(c_j(s)=\mathbb E_{L,j}[e^{-s\sigma}]\). Since no open-state local time has accumulated before \(\sigma\), strong Markov restarting at \((0,1)\) proves

\[
h_j(s)=c_j(s)\,\varphi(s),\qquad
\varphi(s)=\mathbb E_{0,1}[e^{-s\tau_{\Lambda}}]\in(0,1],
\]

where \(\tau_\Lambda\) is the time to accumulate the independently drawn open-state local-time threshold from \((0,1)\). Crucially \(\varphi\) is **independent of the initial gate state** \(j\). This factorization remains true for nonexponential threshold distributions; it uses Markovity of the reflected Brownian/gate pair at the first open contact, not memorylessness of \(\Lambda\).

**2. Exact open-contact transforms.** Define \(\Gamma=\alpha+\beta\), \(\mu=\sqrt{s/D}\), \(\nu=\sqrt{(s+\Gamma)/D}\). The backward ODEs \(D c''+Qc=sc\), with decay at infinity, reflecting boundary condition \(c_0'(0)=0\), and open-contact boundary condition \(c_1(0)=1\), yield

\[
\begin{aligned}
c_0(s)&=\frac{\alpha[\nu e^{-\mu L}-\mu e^{-\nu L}]}{\alpha\nu+\beta\mu},\\
c_1(s)&=\frac{\alpha\nu e^{-\mu L}+\beta\mu e^{-\nu L}}{\alpha\nu+\beta\mu}.
\end{aligned}
\]

Indeed the general decaying solution is \(c_0(x)=A e^{-\mu x}+\alpha B e^{-\nu x}\) and \(c_1(x)=A e^{-\mu x}-\beta B e^{-\nu x}\); the two boundary conditions give \(A=\alpha\nu/(\alpha\nu+\beta\mu)\) and \(B=-\mu/(\alpha\nu+\beta\mu)\). Consequently

\[
\beta c_0+\alpha c_1=\Gamma\frac{\alpha\nu e^{-\mu L}}{\alpha\nu+\beta\mu},\qquad
c_1-c_0=\frac{\Gamma\mu e^{-\nu L}}{\alpha\nu+\beta\mu}.
\]

**3. Exact gate-state kernel across one reset.** Fix \(s=r\) and write \(h=(h_0(r),h_1(r))^{\mathsf T}\), \(e_1=(0,1)^{\mathsf T}\). The expected duration until either absorption or the next reset, conditional on initial gate state, is the vector \(u=(\mathbf1-h)/r\). The discounted, surviving gate-state kernel is

\[
R_{ji}=\int_0^\infty e^{-rt}\mathbb P_{L,j}(\tau>t,G_t=i)\,dt.
\]

Because absorption always occurs in gate state \(1\), a decomposition at absorption with the continued free gate chain gives

\[
R=(I-he_1^{\mathsf T})(rI-Q)^{-1}.
\]

This is a conditional-probability identity: with no killing, the gate occupancy Laplace transform is \((rI-Q)^{-1}\); after first absorption, its contribution is \(h e_1^{\mathsf T}(rI-Q)^{-1}\). All entries of \(h\) are positive, so \(I-rR\) is invertible. Renewal in F and gate-state Markov renewal in K give respectively

\[
\mathbb ET_{\mathrm F}=\frac{1-\pi h}{r\pi h},\qquad
\mathbb ET_{\mathrm K}=\pi(I-rR)^{-1}u.
\]

Direct inversion of the two-by-two matrices, valid for all positive parameters, yields the exact difference identity

\[
\mathbb E T_{\mathrm K}-\mathbb E T_{\mathrm F}
=\frac{\beta(h_1-h_0)}{\Gamma(\beta h_0+\alpha h_1)}.
\]

**4. Threshold-law cancellation and positivity.** By step 1, both entries of \(h\) contain the common factor \(\varphi(r)>0\); it cancels in the last ratio. Substitute the two identities from step 2 at \(s=r\). The result is the boxed formula, which is strictly positive for every allowed parameter. This proves the claimed invariance for the *entire law* of \(\Lambda\), not merely an asymptotic regime.

For clarity, the individual means do retain reaction-law dependence. Writing \(\Phi=\varphi(r)\),

\[
\mathbb ET_{\mathrm F}=
\frac{e^{\mu L}(\alpha\nu+\beta\mu)}{r\alpha\nu\Phi}-\frac1r,
\qquad \mathbb ET_{\mathrm K}=\mathbb ET_{\mathrm F}+\Delta,
\]

where \(\Delta\) denotes the boxed difference. The inverse open-state local-time process gives \(\Phi=\mathbb E[e^{-q(r)\Lambda}]\) with \(q(r)=\Gamma\mu\nu/(\alpha\nu+\beta\mu)\), using the normalization specified above. This follows by the strong Markov property at successive open-state boundary-local-time levels, or by identifying the Laplace transform from exponential (Robin) thresholds.

**5. Finite Robin reaction.** If \(\Lambda\) is exponential with rate \(\kappa/D\), \(\kappa>0\), the open-state boundary is Robin reactive, and

\[
\Phi=\frac{\kappa}{\kappa+Dq(r)}.
\]

The mean under each protocol exceeds its perfectly absorbing open-gate counterpart by the **same** positive amount:

\[
\boxed{
\mathbb ET_{\mathrm F}(\kappa)-\mathbb ET_{\mathrm F}(\infty)
=\mathbb ET_{\mathrm K}(\kappa)-\mathbb ET_{\mathrm K}(\infty)
=\frac{\Gamma\sqrt{D/r}}{\alpha\kappa}\,e^{L\sqrt{r/D}}.
}
\]

Thus the memory delay cannot be changed by tuning the finite Robin surface reactivity while keeping the other parameters fixed.

## Verification

`CHECK.py` is a standalone computational cross-check requiring `numpy`, `scipy`, and `sympy`; run `python CHECK.py`. It verifies the two-by-two Markov-renewal cancellation symbolically for general conditional absorption transforms, the cancellation for an arbitrary shared threshold-transform scalar, and five independent pairs of finite-difference mean-first-passage boundary-value problems for different finite Robin reactivities. Ten direct matrix-renewal tests additionally use exponential, deterministic, gamma, and two-point threshold laws. The independent PDE approximations agree with the exact formulas to the stated discretization tolerance; they do **not** substitute for the analytic proof of the infinite-dimensional continuum and arbitrary-law statements.

## Relationship to prior work

Mercado-Vásquez and Boyer [2], Appendix B, Eq. (49), *already derived the same numerical delay* when the open target absorbs instantly. Bressloff [1] developed the gate-refreshing renewal protocol, and Bressloff [3] derived partially reactive resetting statistics for a gate-refreshing protocol with a general boundary-local-time reaction distribution. The separate study [4] analyzes the distinctions between position-only and local-time resetting in models without the present two-state gating. The **additional statement here** is that the *exact protocol difference remains unchanged for arbitrary fresh local-time reaction-threshold distributions*, including nonexponential laws, with both protocols refreshing their reaction progress. Neither the published perfect-absorber difference alone nor the refreshed-gate generalized-reaction formula alone asserts that invariance. General Markov-renewal and inverse-local-time methods are antecedents, not claimed as inventions.

## Limitations

The result is exact for the specified half-line, two-state gate, stationary gate preparation, Poisson position resets, and complete refreshing of threshold/contact progress. It does not apply automatically when contact progress is retained, gate switching depends on the particle, the reset clock is non-Poissonian, or the geometry differs. It establishes a difference of **means**, not an ordering of the complete reaction-time distributions. It does not assert that optimal reset rates are independent of reaction chemistry. Independent publication-priority review and independent mathematical audit have not been performed.

## References

1. P. C. Bressloff, *Diffusive search for a stochastically-gated target with resetting*, arXiv:2009.02739, first posted 2020-09-06. https://arxiv.org/abs/2009.02739
2. G. Mercado-Vásquez and D. Boyer, *Search of stochastically gated targets with diffusive particles under resetting*, arXiv:2107.02148, first posted 2021-07-05; see Appendix B, Eq. (49). https://arxiv.org/abs/2107.02148
3. P. C. Bressloff, *Stochastically switching diffusion with partially reactive surfaces*, arXiv:2205.13985, first posted 2022-05-27; see Sections 4–5. https://arxiv.org/abs/2205.13985
4. P. C. Bressloff, *Threshold surface reactions and local time resetting*, arXiv:2203.04868, first posted 2022-03-09. https://arxiv.org/abs/2203.04868
5. Y. Scher and S. Reuveni, *A Unified Approach to Gated Reactions on Networks*, arXiv:2101.05124, first posted 2021-01-13. https://arxiv.org/abs/2101.05124
