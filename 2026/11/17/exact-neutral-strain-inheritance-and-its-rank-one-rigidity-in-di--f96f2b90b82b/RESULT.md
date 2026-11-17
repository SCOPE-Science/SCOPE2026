# Exact neutral-strain inheritance and its rank-one rigidity in discrete network epidemics

## Finding

For the forward-Euler competitive SIS network map with a common, strictly positive, rank-one infection matrix and common node-independent recovery, **the initial contact-weighted fractions of every strain are exact first integrals**, and deviations from those fractions at every node decay by one exactly known multiplier. This identifies the particular limiting coexistence state, not just the existence of a continuum of coexistence equilibria. At the epidemic threshold, the same invariant identifies the exact universal inverse-generation extinction profile for *every* initially present strain. Conversely, existence of one positive fixed contact-weighted strain-share invariant for all initial states **characterizes rank-one infection matrices**.

Specifically, let \(N\ge2\) and \(m\ge2\) be finite integers, let \(u_i,w_i,d,h>0\), and assume
\[
 h\left(d+\max_{1\le i\le N}u_i\sum_{j=1}^Nw_j\right)\le1.
\]
For \(r=1,\dots,m\), the population fractions obey
\[
 x_i^{(r)}(k+1)=(1-hd)x_i^{(r)}(k)
 +h\bigl(1-z_i(k)\bigr)u_i\sum_{j=1}^Nw_jx_j^{(r)}(k),
 \qquad z_i(k)=\sum_{r=1}^m x_i^{(r)}(k).
\]
Suppose \(x_i^{(r)}(0)\ge0\), \(z_i(0)\le1\), and at least one strain is present. Define
\[
 S_r=\sum_iw_ix_i^{(r)}(0),\qquad S=\sum_r S_r>0,
 \qquad q_r=\frac{S_r}{S},\qquad a=1-hd\in(0,1).
\]
Then \(q_r\) remains the ratio of the weighted strain total to the weighted overall total at every generation, and **for every** \(i,r,k\ge0\),
\[
 \boxed{x_i^{(r)}(k)=q_rz_i(k)+a^k\bigl[x_i^{(r)}(0)-q_rz_i(0)\bigr].} \tag{1}
\]
Writing \(\rho=\sum_iw_iu_i\) and \(\mathcal K=\sum_iw_iu_i^2\), the complete trichotomy is:

- If \(\rho<d\), every strain goes extinct exponentially, with \(\sum_iw_iz_i(k)\le [1-h(d-\rho)]^k S\).
- If \(\rho=d\), all strains go extinct, but the exact critical law is
  \[
  \boxed{\lim_{k\to\infty}k x_i^{(r)}(k)=\frac{q_ru_i}{h\mathcal K}.}\tag{2}
  \]
  In particular, the network shape determines the universal spatial profile, whereas initial contact-weighted shares determine the lasting strain proportions.
- If \(\rho>d\), let \(s_*>0\) be the unique root of
  \[
  1=\sum_i\frac{w_iu_i}{d+u_is_*}.
  \]
  Every nonzero initial population converges to the **selected** equilibrium
  \[
  \boxed{\lim_{k\to\infty}x_i^{(r)}(k)=q_r\frac{u_is_*}{d+u_is_*}.}\tag{3}
  \]
  The entire nonzero equilibrium set is exactly the simplex of these states as \((q_1,\dots,q_m)\) ranges over the probability simplex.

There is also a converse. For *any* strictly positive \(N\)-by-\(N\) infection matrix \(B\), common recovery \(d\), and sufficiently small positive Euler step making the model physically admissible, some fixed strictly positive row vector \(w\) makes \((w^{\mathsf T}x^{(1)})/(w^{\mathsf T}(x^{(1)}+x^{(2)}))\) invariant after one update for **every** strictly interior two-strain initial condition if and only if \(B=uw^{\mathsf T}\) for a strictly positive column vector \(u\). The weights are unique up to common scaling.

## Assumptions and scope

This is the exact additive-incidence, synchronously updated Euler SIS model, not a finite-population stochastic epidemic, a product-of-independent-transmission model, or an implicitly updated map. A node may be susceptible or carry exactly one of \(m\) competing strains. Identical strains use the same matrix \(B=uw^{\mathsf T}\) and the same scalar healing parameter \(d\); the contact and susceptibility factors \(u_i,w_j\) may be heterogeneous and directed. The physical state space is \(x_i^{(r)}\ge0\) and \(\sum_r x_i^{(r)}\le1\). The displayed step restriction implies positive invariance; it is sufficient and not claimed necessary. Initial populations may lie on strain-free or node-free boundary faces, but the all-zero initial state is separately stationary and is excluded from the formulas defining \(q_r\).

For the converse, \(B\) need not initially have rank one. It is strictly positive and all two-strain interior states with \(0<x_i^{(1)},x_i^{(2)}\), \(x_i^{(1)}+x_i^{(2)}<1\) are used in the quantifier. Conservation for one particular trajectory would not imply rank one. No claim is made about unequal strain-specific contact matrices or recovery parameters.

## Proof

**1. Physical invariance and exact strain splitting.** Put \(z=\sum_rx^{(r)}\) and \(S_r(k)=w^{\mathsf T}x^{(r)}(k)\). The nonnegative update has strictly positive survivor multiplier \(a=1-hd\). Summing over strains gives
\[
 z_i^+=a z_i+h(1-z_i)u_iS(k),\quad S(k)=w^{\mathsf T}z(k).
\]
Because \(S(k)\le\sum_jw_j\),
\[
 0\le z_i^+\le a z_i+h u_i\Bigl(\sum_jw_j\Bigr)(1-z_i)\le1,
\]
using the step bound. Each strain stays nonnegative. Multiplying the strain equation by \(w_i\) and summing over nodes yields
\[
 S_r(k+1)=L(z(k))S_r(k),\quad
 L(z)=a+h\sum_iw_iu_i(1-z_i)>0.
\]
The **same** factor applies to every strain and to their total, hence each \(q_r=S_r(k)/S(k)\) is constant. Finally, subtract \(q_r\) times the total equation from the strain equation. The nonlinear infection term disappears exactly, leaving
\[
 x_i^{(r)}(k+1)-q_rz_i(k+1)
 =a\left[x_i^{(r)}(k)-q_rz_i(k)\right].
\]
Induction gives (1), including zero initial strain shares.

**2. Subcritical and critical extinction.** Write \(T(k)=\sum_iw_iu_i z_i(k)\), so the exact scalar identity is
\[
 S(k+1)=S(k)\,[1+h(\rho-d)-hT(k)].\tag{4}
\]
For \(\rho<d\), positivity and (4) give the displayed geometric bound. At \(\rho=d\), (4) reduces to \(S^+=S(1-hT)\). Since \(T\ge(\min_i u_i)S\), this positive sequence decreases to zero; a positive limit would contradict (4). To identify its profile, put \(e_i=z_i-(u_i/d)S\). Because \(\rho=d\), direct subtraction yields
\[
 e_i^+=a e_i-hS\left[u_i z_i-(u_i/d)T\right].\tag{5}
\]
The bounds \(0\le z_i\le S/w_i\) and \(T\le(\max_i u_i)S\) make the bracket in (5) uniformly \(O(S)\), so the forcing is \(O(S^2)\). Also \(S^+/S=1-hT\to1\). Dividing (5) by \(S^+\), for every sufficiently large \(k\), gives
\[
 \max_i\frac{|e_i(k+1)|}{S(k+1)}
 \le c\max_i\frac{|e_i(k)|}{S(k)}+C S(k),
 \qquad c<1.
\]
Iteration implies \(e_i(k)/S(k)\to0\), i.e. \(z_i/S\to u_i/d\). Therefore
\[
 \frac{T(k)}{S(k)}\longrightarrow\frac{\mathcal K}{d},
 \quad
 \frac1{S(k+1)}-\frac1{S(k)}
 =\frac{hT(k)}{S(k)[1-hT(k)]}\longrightarrow\frac{h\mathcal K}{d}.
\]
Cesàro averaging of these reciprocal increments proves
\(kS(k)\to d/(h\mathcal K)\), and thus \(kz_i(k)\to u_i/(h\mathcal K)\). In (1), \(k a^k\to0\), proving (2) for every strain.

**3. Supercritical global convergence.** For \(\rho>d\), a positive fixed point of the total-population map has \(z_i=u_is/(d+u_is)\), where \(s=w^{\mathsf T}z>0\). The scalar fixed-point equation is strictly decreasing from \(\rho/d>1\) at \(s=0\) to zero as \(s\to\infty\), hence has exactly one root \(s_*\). The zero state is the only other fixed point. Let \(H(z)_i=a z_i+h(1-z_i)u_iw^{\mathsf T}z\). On the physical cube,
\[
 \frac{\partial H_i}{\partial z_j}=hu_iw_j(1-z_i)\ge0\quad(j\ne i),
 \quad
 \frac{\partial H_i}{\partial z_i}
 =a-hu_iS+hu_iw_i(1-z_i)\ge0
\]
by the step bound. Thus \(H\) is order-preserving. The all-ones vector is a supersolution because \(H(\mathbf1)=a\mathbf1\le\mathbf1\). For any \(0<\varepsilon<1\), \(\varepsilon z_*\) is a strict subsolution: using \(H(z_*)=z_*\),
\[
 H_i(\varepsilon z_*)-\varepsilon z_{*,i}
 =h\varepsilon(1-\varepsilon)u_i z_{*,i}s_*>0.
\]
For any nonzero physical initial state, the total is strictly positive at every node after at most one update, because \(u,w,h,a>0\). It is therefore bracketed between \(\varepsilon z_*\) for some small \(\varepsilon>0\) and \(\mathbf1\). Their forward iterations respectively increase and decrease, remain bounded, and have nonzero fixed-point limits. Uniqueness forces both limits to equal \(z_*\). Order comparison now proves \(z(k)\to z_*\) globally. Formula (1) gives (3). Conversely all mixtures \(x^{(r)}=q_rz_*\) are stationary, and any other nonzero stationary state must have the same total \(z_*\), so (1) forces the stationary state to be one of these mixtures.

**4. Rigidity of the conserved positive weight.** For arbitrary strictly positive \(B\), put
\[
 M(z)=aI+h\operatorname{diag}(1-z)B.
\]
Fix any strictly interior total vector \(z\), and let \(x\) range over the open box \(0<x_i<z_i\), assigning \(x\) to strain one and \(z-x\) to strain two. If \(w^{\mathsf T}x/w^{\mathsf T}z\) is preserved after one step for every \(x\), then
\[
 (w^{\mathsf T}M(z))x
 =\frac{w^{\mathsf T}M(z)z}{w^{\mathsf T}z}\,w^{\mathsf T}x
\]
for all \(x\) in this open box. Equality of the coefficient rows implies \(w^{\mathsf T}M(z)=\lambda(z)w^{\mathsf T}\). Vary only coordinate \(z_i\) inside the open cube and subtract the two row identities. Because \(w_i>0\), the \(i\)th row of \(B\) must be proportional to \(w^{\mathsf T}\). This holds for every \(i\), so \(B=uw^{\mathsf T}\) with \(u_i>0\). The sufficiency follows from Step 1. Since a strictly positive rank-one matrix has a unique positive row factor up to scaling, so does the conserved-weight ray. This proves the converse without an asymptotic or linearized assumption.

## Verification

The standalone `CHECK.py` uses exact rational arithmetic to verify (1) on a two-node, three-strain example in subcritical, critical, and supercritical regimes for five iterations each. It separately simulates the critical limit for 100000 generations, the unique positive supercritical equilibrium for 1000 generations, and subcritical extinction for 400 generations. Execute with `python CHECK.py` using Python 3 without external dependencies; the final line must be `CHECK_OK`. Exact-rational finite checks and numerical limits are reproducibility diagnostics; the arbitrary-dimension and infinite-time claims are proved analytically above.

For a concrete directed, heterogeneous two-node contact example set \(u=(1,2)^{\mathsf T}\), \(w=(3,1)^{\mathsf T}\), \(h=1/20\), giving \(B=\begin{psmallmatrix}3&1\\6&2\end{psmallmatrix}\), \(\rho=5\), and \(\mathcal K=7\). For \(d=2\), the endemic force is \(s_*=(1+\sqrt{13})/2\); for \(d=5\), the critical profiles obey \(kz_1(k)\to20/7\) and \(kz_2(k)\to40/7\). With two-strain initial states \(x^{(1)}=(1/10,3/10)\) and \(x^{(2)}=(2/10,1/10)\), the limiting first-strain fraction is \(q_1=6/13\), in contrast with its unweighted initial fraction \(4/7\). This difference illustrates why the selected mixture is a network-dependent observable.

## Relationship to prior work

Gracy, Liu, Başar and Uribe [1] introduce the discrete competitive bivirus Euler SIS model, its monotonicity and threshold results, and sufficient conditions for coexistence. Their source specifies the update used here, but does not provide this contact-weighted strain invariant, the exact all-time coordinate decomposition, or the rank-one iff characterization. Ye, Anderson and Liu [2] and Gracy and collaborators [3] show that neutral continua of coexistence equilibria can occur in related continuous-time bi- and tri-virus network models; **the existence of neutral coexistence is therefore not claimed as new**. The recent aligned rank-one study [4] proves unique, locally stable coexistence under *linearly independent* recovery-adjusted strain profiles, explicitly excluding the proportional degenerate sector treated here. It does not imply global initial-share selection or the converse rigidity. General Perron-critical inverse-time epidemic laws are known for different SIS maps [5]; their leading-profile philosophy is background, while the exact conservation and full phase classification here concern the additive-incidence identical-strain Euler map. These comparisons are evidence for a narrower contribution, not a claim of absolute publication priority.

## Limitations

Equal strain dynamics, homogeneous node-independent recovery, strict positivity of contact factors, a fixed rank-one contact matrix and the physical Euler step restriction are essential hypotheses. The converse classifies invariance across **all** interior initial conditions, not sporadic conserved quantities or trajectory-specific identities. The subcritical statement gives a sufficient exponential bound, not the exact slowest decay rate for every initial state. The critical inverse-time law is deterministic and asymptotic, not an extinction-time distribution in a finite stochastic SIS epidemic. The theorem does not address nonidentical strains, stochastic contacts, or arbitrary contact rank. A related open-access tri-virus paper [3] was compared by its abstract only, so uninspected full-text overlap remains a publication-priority risk. Independent validation has not been performed.

## References

1. S. Gracy, J. Liu, T. Başar and C. A. Uribe, *A Discrete-time Networked Competitive Bivirus SIS Model*, arXiv:2310.13853v1, first public 2023-10-20. https://arxiv.org/abs/2310.13853
2. M. Ye, B. D. O. Anderson and J. Liu, *Convergence and Equilibria Analysis of a Networked Bivirus Epidemic Model*, arXiv:2111.07507, 2021. https://arxiv.org/abs/2111.07507
3. S. Gracy, M. Ye, B. D. O. Anderson and C. A. Uribe, *Towards Understanding the Endemic Behavior of a Competitive Tri-Virus SIS Networked Model*, arXiv:2303.16457, 2023. https://arxiv.org/abs/2303.16457
4. *Strictly concave coexistence potential for aligned rank-one competitive bivirus networks*, published research record, 2026-11-02, identifier `567a29ac68ce`. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-strictly-concave-coexistence-potential-for-aligned-rank-one-comp--567a29ac68ce
5. *Universal critical decay and a spectral collision coefficient for a product-hazard SIS network*, published research record, 2026-11-08, identifier `c0fb1830567e`. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-universal-critical-decay-and-a-spectral-collision-coefficient-fo--c0fb1830567e
