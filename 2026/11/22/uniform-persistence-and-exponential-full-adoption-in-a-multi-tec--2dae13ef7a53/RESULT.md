# Uniform persistence and exponential full adoption in a multi-technology opinion network

## Finding

In the finite-community Multi-technology AdopTion-opinion co-Evolution (MATE) model, **every physically admissible trajectory with any initially non-susceptible mass** eventually has a uniformly positive adopter fraction for *every* technology at *every* community. Simultaneously, the fraction never adopting any technology decreases geometrically to zero at every community. These conclusions hold with **arbitrarily strong admissible opinion–adoption feedback**, with no equilibrium uniqueness, convergence, weak-coupling, or aperiodicity assumption on the physical network.

Here is an explicit universal, though deliberately conservative, bound. Let the model have \(n\ge1\) communities and \(m\ge2\) technologies, and put
\[
\begin{aligned}
 b_i(t)&=1-s_i(t)=\sum_{k=1}^m(a_i^{[k]}(t)+d_i^{[k]}(t)),\\
 x_*&=\min_{i,k}\bigl(1-\lambda_i^{[k]}-\xi_i^{[k]}\bigr)p_i^{[k]},\\
 \gamma_*&=\min_{i,k}\gamma_i^{[k]},\qquad
 \delta_* =\min_{i,k}\delta_i^{[k]},\qquad
 \beta_* =\min_{i,k}\beta_i^{[k]},\\
 w_*&=\min\{W_{ij}:W_{ij}>0\},\qquad
 b_* =\max_i b_i(0)>0,\\
 q&=\min\{\delta_*,\gamma_*x_*\},\qquad \eta=q^4,\\
 c&=\beta_*x_*w_*\eta,\qquad B=b_*c^{n-1},\\
 \rho&=\beta_*x_*\eta B,\qquad T=6(n-1)+5.
\end{aligned}
\]
All constants \(q,\eta,c,B,\rho\) are strictly positive and at most one. For every community \(i\), technology \(k\), and integer \(t\ge T\),
\[
 \boxed{\quad a_i^{[k]}(t)\ge\eta B,\qquad
 s_i(t)\le s_i(T)(1-\rho)^{t-T}.\quad}
\]
Also \(d_i^{[k]}(t)\ge\delta_*\eta B\) for every integer \(t\ge T+1\). The initial seed may consist exclusively of dissatisfied people and may be confined to one community.

## Assumptions and scope

The state in community \(i\) consists of \(s_i,a_i^{[k]},d_i^{[k]}\in[0,1]\), normalized by \(s_i+\sum_k(a_i^{[k]}+d_i^{[k]})=1\), and opinion coordinates \(x_i^{[k]}\in[0,1]\). Here \(W\) and \(\widetilde W\) are row-stochastic; the nonnegative physical-contact matrix \(W\) is irreducible. Each \(p_i^{[k]}>0\), each \(\beta_i^{[k]},\gamma_i^{[k]},\delta_i^{[k]}>0\), with \(\delta_i^{[k]}\le1\), \(\sum_k\beta_i^{[k]}\le1\), and \(\sum_k\gamma_i^{[k]}\le1\). Opinion weights \(\lambda_i^{[k]},\xi_i^{[k]}\ge0\) satisfy \(\lambda_i^{[k]}+\xi_i^{[k]}<1\). All coefficients are time-independent; initial data may have arbitrary admissible opinions, including zeros. These are the corresponding positive-rate conditions of the cited MATE equations. There is no assumption about the numerical strength of \(\xi\) beyond admissibility.

The update equations for each \(i,k\) are
\[
\begin{aligned}
 s_i(t+1)&=s_i(t)\left[1-\sum_k\beta_i^{[k]}x_i^{[k]}(t)(Wa^{[k]}(t))_i\right],\\
 a_i^{[k]}(t+1)&=(1-\delta_i^{[k]})a_i^{[k]}(t)+s_i(t)\beta_i^{[k]}x_i^{[k]}(t)(Wa^{[k]}(t))_i
 +\gamma_i^{[k]}x_i^{[k]}(t)\sum_{\ell\ne k}d_i^{[\ell]}(t),\\
 d_i^{[k]}(t+1)&=\delta_i^{[k]}a_i^{[k]}(t)
 +d_i^{[k]}(t)\left[1-\sum_{\ell\ne k}\gamma_i^{[\ell]}x_i^{[\ell]}(t)\right],\\
 x_i^{[k]}(t+1)&=(1-\lambda_i^{[k]}-\xi_i^{[k]})p_i^{[k]}
 +\lambda_i^{[k]}(\widetilde W x^{[k]}(t))_i+\xi_i^{[k]}(Wa^{[k]}(t))_i.
\end{aligned}
\]
The result concerns the deterministic discrete-time community mean-field model, not random finite-person adoption realizations.

## Proof

**1. Uniform opinion floor and monotone seed mass.** Nonnegativity and the last update show \(x_i^{[k]}(t)\ge x_*>0\) for all \(t\ge1\). Conservation and the susceptible equation give \(b_i(t+1)\ge b_i(t)\), with initial mass \(b_*>0\) at some community \(j\).

**2. Four-step local mixing, for every technology.** At each community, discard the nonnegative inflow from susceptible adoption and consider only transitions among \(A_1,\ldots,A_m,D_1,\ldots,D_m\). The resulting time-dependent \(2m\)-state transition matrix is column-stochastic. Available transitions are \(A_k\to D_k\) with probability \(\delta_i^{[k]}\), \(D_k\to A_r\) for \(r\ne k\) with probability \(\gamma_i^{[r]}x_i^{[r]}\), and \(D_k\to D_k\) with probability \(1-\sum_{r\ne k}\gamma_i^{[r]}x_i^{[r]}\). Their respective probabilities are at least \(\delta_*\), \(\gamma_*x_*\), and \(\gamma_*\), so each is at least \(q\). Fix a target \(A_r\) and choose any \(\ell\ne r\) (possible because \(m\ge2\)). From each initial state there is a four-step path to \(A_r\):

- \(A_r\to D_r\to A_\ell\to D_\ell\to A_r\);
- \(D_r\to D_r\to A_\ell\to D_\ell\to A_r\);
- \(A_k\to D_k\to D_k\to D_k\to A_r\) when \(k\ne r\);
- \(D_k\to D_k\to D_k\to D_k\to A_r\) when \(k\ne r\).

All four transitions in each path have probability at least \(q\). Thus the \(A_r\)-row of every four-consecutive-step transition product is entrywise at least \(\eta=q^4\). Because new susceptible inflow is nonnegative, for each \(i,r\) and integer \(t\ge1\),
\[
 \boxed{\ a_i^{[r]}(t+4)\ge\eta b_i(t).\ }
\]
This step does not require slowly changing opinions or convergence of the local transition products.

**3. Seed propagation over the physical network.** Let \(j\) attain \(b_j(0)=b_*\). By monotonicity, \(a_j^{[r]}(t)\ge\eta b_*\) for every \(t\ge5\). Define a directed edge \(u\to v\) exactly when \(W_{vu}>0\). Strong connectivity makes every vertex reachable from \(j\) by a path of length at most \(n-1\). Suppose along such a path a vertex \(u\) at depth \(\ell-1\) has \(b_u(t)\ge b_*c^{\ell-1}\) whenever \(t\ge6(\ell-1)\). At time \(t_0=6(\ell-1)+5\), step 2 gives \(a_u^{[r]}(t_0)\ge\eta b_*c^{\ell-1}\), where \(r\) is any fixed technology. The susceptible update at its neighbor \(v\), using \(s_v=1-b_v\), therefore yields
\[
\begin{aligned}
 b_v(t_0+1)&\ge b_v(t_0)+(1-b_v(t_0))\beta_*x_*W_{vu}\eta b_*c^{\ell-1}\\
 &\ge c b_*c^{\ell-1}=b_*c^\ell.
\end{aligned}
\]
The last inequality uses \(0\le b_v\le1\) and \(\beta_*x_*W_{vu}\eta b_*c^{\ell-1}\le1\). Monotonicity propagates this bound to all later times. Induction gives \(b_i(t)\ge B=b_*c^{n-1}\) for every \(i\) and all \(t\ge6(n-1)\); this also covers the trivial one-community case.

**4. Uniform coexistence and geometric susceptible depletion.** Applying step 2 after the graph-propagation time yields \(a_i^{[k]}(t)\ge\eta B\) whenever \(t\ge T=6(n-1)+5\), for every technology and node. Row-stochasticity then implies \((Wa^{[k]}(t))_i\ge\eta B\). Taking just one technology in the nonnegative susceptible hazard,
\[
 s_i(t+1)\le(1-\beta_*x_*\eta B)s_i(t)=(1-\rho)s_i(t),\qquad t\ge T.
\]
Iteration proves the stated geometric bound. Finally \(d_i^{[k]}(t+1)\ge\delta_i^{[k]}a_i^{[k]}(t)\ge\delta_*\eta B\), proving uniform persistence of the dissatisfied compartments as well.

## Verification

The accompanying `verify_mate_persistence.py` uses exact rational arithmetic to form four successive, independently varying local switching matrices and verifies their relevant adopter-row lower bound in 6,300 component comparisons, for two through six technologies. It also runs the full coupled model on a two-community, three-technology directed-contact example with nonzero opinion feedback, checking state conservation and 738 specified four-step, propagation and geometric comparisons. The exact four-step path proof, rather than finite simulation, establishes the all-size, all-time theorem. Execute with `python verify_mate_persistence.py` using Python's standard library.

## Relationship to prior work

Alutto, Dabbene, Fontan, Johansson and Ravazzi (arXiv:2611.04407v1) introduce the multitechnology MATE model, derive its equilibrium structure (Theorems 3.1–3.4) and prove convergence to a unique adoption-diffused equilibrium under a stringent **weak opinion-feedback condition** (Theorem 3.5). Their Appendix B.6 derives three-step mixing toward a dissatisfied state for a *different purpose*. The theorem above instead proves uniform all-technology persistence and a quantified rate of full susceptible depletion for **every** admissible feedback strength, including regimes where multiple adoption-diffused equilibria can occur and full-state convergence has not been established. It neither asserts global convergence of all compartments nor reclaims the local mixing technique as new.

Their earlier two-technology model (arXiv:2601.16719v1) proves existence and uniqueness of a coexistence equilibrium, not the graph-wide all-initial-condition quantitative persistence and depletion bound. The general stochastic-matrix theory surveyed by Ipsen and Selee (2011) supplies established mixing machinery but does not independently identify the adoption-model transmission mechanism or the explicit network saturation theorem. Thus the scientific contribution is the **unconditional global network implication**, not irreducibility, geometric iteration or a standard Doeblin argument in isolation.

## Limitations

The constants are sufficient and can be numerically very conservative; no optimal mixing length or sharp decay exponent is claimed. The theorem requires strictly positive baseline predispositions, switching probabilities and dissatisfaction, a finite irreducible physical network, and nonzero initial non-susceptible mass. Removing any of these assumptions can permit a technology or a community to remain unadopted. It does not ensure convergence of adoption shares or opinions to a single equilibrium, excludes stochastic finite-population fluctuations, and does not predict practical adoption times from uncertain fitted parameters. Historical priority remains subject to independent literature review.

## References

1. M. Alutto, F. Dabbene, A. Fontan, K. H. Johansson and C. Ravazzi, *Competition, Switching, and Control in Coupled Adoption-Opinion Dynamics*, arXiv:2611.04407v1, 3 November 2026, https://arxiv.org/abs/2611.04407 . Specifically §2, §3 and Appendix B.6.
2. M. Alutto, F. Dabbene, A. Fontan, K. H. Johansson and C. Ravazzi, *On a Coupled Adoption-Opinion Framework for Competing Innovations*, arXiv:2601.16719v1, 23 January 2026, https://arxiv.org/abs/2601.16719 . Specifically §§2–3.
3. I. C. F. Ipsen and T. M. Selee, *Ergodicity Coefficients Defined by Vector Norms*, SIAM Journal on Matrix Analysis and Applications 32 (2011), 153–200, https://doi.org/10.1137/090752948 .
