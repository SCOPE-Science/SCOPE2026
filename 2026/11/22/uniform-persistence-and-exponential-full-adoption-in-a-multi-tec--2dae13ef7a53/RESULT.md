# Uniform persistence and exponential full adoption in a multi-technology opinion network

## Finding

In the finite-community Multi-technology AdopTion-opinion co-Evolution (MATE) model, every physically admissible trajectory with any initially non-susceptible mass eventually has a uniformly positive adopter fraction for every technology at every community. The fraction never adopting any technology decreases geometrically to zero at every community. These conclusions hold at every admissible opinion–adoption feedback strength, with no equilibrium uniqueness, convergence, weak-coupling, or physical-network aperiodicity assumption. Full adoption here means depletion of the never-adopted class, not disappearance of dissatisfaction.

Let there be \(n\ge1\) communities and \(m\ge2\) technologies. Define
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
The constants \(q,\eta,c,B,\rho\) belong to \((0,1]\). For every \(i,k\) and integer \(t\ge T\),
\[
 \boxed{\quad a_i^{[k]}(t)\ge\eta B,\qquad
 s_i(t)\le s_i(T)(1-\rho)^{t-T}.\quad}
\]
Also \(d_i^{[k]}(t)\ge\delta_*\eta B\) for \(t\ge T+1\). The initial seed may consist exclusively of dissatisfied people and may be confined to one community.

## Assumptions and scope

The fractions in community \(i\) are nonnegative, with \(s_i+\sum_k(a_i^{[k]}+d_i^{[k]})=1\). The opinions \(x_i^{[k]}\) are in \([0,1]\), and each innate opinion satisfies **\(0<p_i^{[k]}\le1\)**. Both \(W\) and \(\widetilde W\) are nonnegative row-stochastic matrices, and \(W\) is irreducible. All \(\beta_i^{[k]},\gamma_i^{[k]},\delta_i^{[k]}\) are positive, with \(\delta_i^{[k]}\le1\), \(\sum_k\beta_i^{[k]}\le1\), and \(\sum_k\gamma_i^{[k]}\le1\). Opinion weights \(\lambda_i^{[k]},\xi_i^{[k]}\ge0\) satisfy \(\lambda_i^{[k]}+\xi_i^{[k]}<1\). Coefficients are time-independent, and initial opinions may vanish.

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

**1. Admissibility, opinion floor and monotone seed mass.** The opinion update is a convex combination of inputs in \([0,1]\). All fraction updates are nonnegative by the rate bounds, and the total fraction is conserved by cancellation of the inflows and outflows. Thus every admissible initial state remains admissible. Nonnegativity in the opinion update gives \(x_i^{[k]}(t)\ge x_*>0\) for all \(t\ge1\). The susceptible equation gives \(b_i(t+1)\ge b_i(t)\).

**2. Four-step local mixing, for every technology.** Discard nonnegative susceptible inflow and consider only transitions among \(A_1,\ldots,A_m,D_1,\ldots,D_m\) at a fixed community. The resulting time-dependent matrix is column-stochastic. For \(t\ge1\) the edges \(A_k\to D_k\) and \(D_k\to A_r\) for \(r\ne k\) have probabilities at least \(\delta_*\) and \(\gamma_*x_*\), respectively. Also \(D_k\to D_k\) has probability \(1-\sum_{r\ne k}\gamma_i^{[r]}x_i^{[r]}(t)\ge\gamma_i^{[k]}\ge\gamma_*\). All these edges have probability at least \(q\). Fix a target \(A_r\) and any \(\ell\ne r\). The following are four-step paths to \(A_r\):

- \(A_r\to D_r\to A_\ell\to D_\ell\to A_r\);
- \(D_r\to D_r\to A_\ell\to D_\ell\to A_r\);
- \(A_k\to D_k\to D_k\to D_k\to A_r\) for \(k\ne r\);
- \(D_k\to D_k\to D_k\to D_k\to A_r\) for \(k\ne r\).

Thus the \(A_r\) row of each four-consecutive-step product, beginning at time \(t\ge1\), is entrywise at least \(\eta=q^4\). Adding back the nonnegative inflows gives
\[
 a_i^{[r]}(t+4)\ge\eta b_i(t),\qquad t\ge1.
\]

**3. Seed propagation over the physical network.** Pick \(j\) with \(b_j(0)=b_*\). Use the orientation \(u\to v\) when \(W_{vu}>0\). Strong connectivity makes every vertex reachable from \(j\) within \(n-1\) edges. Suppose the previous vertex \(u\) on a path has \(b_u(t)\ge b_*c^{\ell-1}\) for \(t\ge6(\ell-1)\). At \(t_0=6(\ell-1)+5\), Part 2 gives \(a_u^{[r]}(t_0)\ge\eta b_*c^{\ell-1}\) for any fixed \(r\). Write \(L=\beta_*x_*W_{vu}\eta b_*c^{\ell-1}\in[0,1]\). The susceptible hazard at the next vertex \(v\) is at least \(L\). Hence
\[
 b_v(t_0+1)\ge b_v(t_0)+(1-b_v(t_0))L\ge L\ge b_*c^\ell.
\]
The bound persists by monotonicity. Starting with \(j\) and using \(c\le1\), induction gives \(b_i(t)\ge B\) for every \(i\) when \(t\ge6(n-1)\), including \(n=1\).

**4. Uniform coexistence and geometric susceptible depletion.** For \(t\ge T\), Part 2 applied at \(t-4\) gives \(a_i^{[k]}(t)\ge\eta B\) and row-stochasticity gives \((Wa^{[k]}(t))_i\ge\eta B\). One technology alone supplies a hazard at least \(\beta_*x_*\eta B=\rho\). Therefore \(s_i(t+1)\le(1-\rho)s_i(t)\), and iteration proves the claimed bound. The dissatisfaction update gives \(d_i^{[k]}(t+1)\ge\delta_i^{[k]}a_i^{[k]}(t)\ge\delta_*\eta B\).

## Verification

The accompanying `verify_mate_persistence.py` specifies 6,300 rational four-step matrix comparisons for two through six technologies and 738 numerical comparisons for a two-community, three-technology coupled example. These are checks of orientation, indexing and finite examples, not an all-size or all-time certificate. The analytic four-step bound and graph induction establish the theorem.

## Relationship to prior work

Alutto, Dabbene, Fontan, Johansson and Ravazzi (arXiv:2611.04407v1) introduce the multitechnology MATE model and analyze its equilibrium structure. Their Theorem 3 gives convergence to a unique adoption-diffused equilibrium under condition (11), which also implies eventual persistence and depletion in that regime. Appendix B.6 uses three-step local minorization toward a dissatisfied state; appending a switch yields a local adopter minorization as well. The claim here is the quantitative network consequence for every admissible feedback strength and any nonzero seed. It establishes neither convergence of all compartments nor a new local mixing technique. The earlier two-technology model (arXiv:2601.16719v1) studies coexistence equilibria. The network consequence here uses the susceptible hazard and monotone non-susceptible mass to turn local mixing into a trajectory-wide bound.

## Limitations

The constants can be very conservative and deteriorate with the number of communities and the initial seed. No optimal mixing length or decay exponent is claimed. The result does not imply convergence of the opinion or adoption shares, and does not address stochastic finite populations or the removal of the positivity and graph assumptions.

## References

1. M. Alutto, F. Dabbene, A. Fontan, K. H. Johansson and C. Ravazzi, *Competition, Switching, and Control in Coupled Adoption-Opinion Dynamics*, arXiv:2611.04407v1, https://arxiv.org/abs/2611.04407, §§2–3 and Appendix B.6.
2. M. Alutto, F. Dabbene, A. Fontan, K. H. Johansson and C. Ravazzi, *On a Coupled Adoption-Opinion Framework for Competing Innovations*, arXiv:2601.16719v1, https://arxiv.org/abs/2601.16719.
3. I. C. F. Ipsen and T. M. Selee, *Ergodicity Coefficients Defined by Vector Norms*, SIAM Journal on Matrix Analysis and Applications 32 (2011), 153–200, https://doi.org/10.1137/090752948.
