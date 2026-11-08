# Sparse intraspecific completion with a uniform global coexistence basin

## Finding
For any number of interacting populations and any fixed intrinsic growth rates and pairwise interaction coefficients, two self-only higher-order per-capita monomials per population suffice to create positive coexistence with an explicit, dimension-independent attraction cube and an explicit exponential logarithmic convergence rate. No cross-species higher-order interactions are introduced. The same construction works even for pairwise interaction networks known to forbid stable coexistence in the purely pairwise model.

**Theorem.** Let \(n\ge1\), \(r_i\in\mathbb R\), and \(b_{ij}\in\mathbb R\) be arbitrary and fixed. Define
\[
 h_i=r_i+\sum_{j=1}^{n}b_{ij},\qquad
 \rho_i=\sum_{j=1}^{n}|b_{ij}|,\qquad
 H=\max_{1\le i\le n}(|h_i|+\rho_i),\qquad L=32(1+H).
\]
For the polynomial system
\[
 \dot x_i=x_i\bigg[r_i+\sum_{j=1}^{n}b_{ij}x_j+(L-h_i)x_i^2-Lx_i^3\bigg],\quad i=1,\ldots,n,
\]
let \(Q=[3/4,5/4]^n\). The set \(Q\) is forward invariant, the all-ones state is the only equilibrium in \(Q\), and for all \(x(0)\in Q\) and \(t\ge0\),
\[
 \|\log x(t)\|_\infty\le e^{-9t/2}\|\log x(0)\|_\infty.
\]
The rate and the size of \(Q\) do not deteriorate with \(n\) or the magnitude of the prescribed interactions; the chosen gain \(L\) scales with them. Only \(2n\) higher-order coefficients are nonzero, with \(L-h_i>0\) and \(-L<0\). The statement is about every initial condition in \(Q\), not every positive initial condition.

**Minimal maximum interaction order in this universal setting.** If one restricts additions to self-only quadratic per-capita terms, such a guarantee is false even for one species with \(r=b_{11}=-1\). Thus an order-four interaction is necessary for a construction claimed to handle *all* prescribed \((r,B)\), even though a particular ecology might require less.

## Assumptions and scope
This is a deterministic finite-dimensional autonomous ODE, in the positive population orthant, with entirely arbitrary real prescribed coefficients \(r_i\) and \(b_{ij}\). Signs and magnitudes of all original coefficients stay fixed. An interaction of order four means a cubic monomial in the per-capita growth (multiplied by \(x_i\) in the ODE). Repeated species indices are permitted in higher-order tensors. The monomials added to species \(i\) involve only its own density \(x_i\). No persistence or boundedness statement outside \(Q\) is claimed.

## Proof
**1. Exact equilibrium and algebra.** Write the per-capita right-hand side as \(G_i(x)\). The choice \(h_i=r_i+\sum_jb_{ij}\) yields the identity
\[
 G_i(x)=\sum_{j=1}^n b_{ij}(x_j-1)-h_i(x_i^2-1)-Lx_i^2(x_i-1).
\]
At \(x=\mathbf1\), the right-hand side vanishes, proving coexistence. Since \(L> |h_i|\), the higher-order self coefficients are strictly of opposite signs. The original constant and linear per-capita terms are unchanged.

**2. Positive invariance with explicit inward margins.** Put \(\delta=1/4\), \(\ell=3/4\), \(u=5/4\). If \(x\in Q\) and \(x_i=\ell\), the preceding identity implies
\[
 G_i(x)\ge \delta\left[\frac9{16}L-\rho_i-\frac74|h_i|\right]>0.
\]
If \(x\in Q\) and \(x_i=u\), the same identity gives
\[
 G_i(x)\le\delta\left[-\frac{25}{16}L+\rho_i+\frac94|h_i|\right]<0.
\]
Both strict inequalities follow from \(L=32(1+H)\) and \(H\ge|h_i|+\rho_i\). Since \(x_i>0\) on every face, the vector field points inward on each lower face and each upper face. The standard first-exit argument proves that \(Q\) is positively invariant, including corners. Smoothness and compactness give forward existence for every initial condition in \(Q\).

**3. Uniform contraction in logarithmic coordinates.** Set \(z_i=\log x_i\). On the convex box \(\log Q=[\log(3/4),\log(5/4)]^n\), the transformed vector field is \(\dot z=F(z)=G(e^z)\). Its Jacobian has the exact entries
\[
 \partial_{z_i}F_i=b_{ii}x_i-2h_ix_i^2+Lx_i^2(2-3x_i),
 \qquad \partial_{z_j}F_i=b_{ij}x_j\quad(j\ne i).
\]
For all \(x\in Q\), the cubic damping satisfies
\[
 x_i^2(2-3x_i)\le -\frac9{64}.
\]
Consequently each absolute row logarithmic-norm expression obeys
\[
 \begin{aligned}
 \partial_{z_i}F_i+\sum_{j\ne i}|\partial_{z_j}F_i|
 &\le -\frac9{64}L+\frac{25}{8}|h_i|+\frac54\rho_i\\
 &\le-\frac92(1+H)+\frac{35}{8}H\\
 &=-\frac92-\frac18H\le-\frac92.
 \end{aligned}
\]
Here the diagonal pairwise coefficient is bounded by \(5|b_{ii}|/4\) and is included in \(5\rho_i/4\). The logarithmic matrix norm for the sup norm therefore satisfies \(\mu_\infty(DF(z))\le-9/2\) everywhere on the convex logarithmic cube. The mean-value formula and the upper right Dini derivative of the sup norm give, for any two solutions staying in this cube, \(D^+\|z-\widetilde z\|_\infty\le-(9/2)\|z-\widetilde z\|_\infty\). Taking the second solution to be the equilibrium \(\widetilde z=0\) and integrating proves the stated exponential bound. If two distinct equilibria existed in \(Q\), this strict bound applied to them would be impossible. Hence the equilibrium is unique in \(Q\).

**4. Universal order-four obstruction at order three.** To see that additions of at most quadratic per-capita order do not suffice for *every* prescribed ecology, take the single-species fixed coefficients \(r=-1\) and \(b_{11}=-1\). The most general permitted quadratic-per-capita self augmentation has growth \(g(x)=-1-x+cx^2\). If \(c\le0\), no positive equilibrium exists. If \(c>0\), its sole positive root is
\[
 x_* =\frac{1+\sqrt{1+4c}}{2c},\qquad g'(x_*)=\sqrt{1+4c}>0.
\]
The scalar vector field is \(\dot x=xg(x)\); its derivative at this positive equilibrium equals \(x_*g'(x_*)>0\). Thus the equilibrium is repelling. This proves that cubic self terms in the per-capita growth (four-body order) cannot be dropped from a universal claim covering every prescribed one-species ecology. It is not a statement that every particular ecology needs fourth-order terms.

## Verification
The companion standalone code `verification/check.py` evaluates the exact completion identities and the rational inequalities in the contraction and inward-pointing estimates. It also checks an illustrative symmetric obligate-mutualism network, its Jacobian, five representative trajectories in the invariant square, and the one-species quadratic-order obstruction. Running the recorded code produced:

`VERIFY_OK exact_completion=1 exact_uniform_constants=4 example_positive_cube=5 quadratic_order_obstruction=1`

These computations support but do not replace the analytic uniform argument. The full theorem follows from the inequalities above, not from finite sampling. Dependencies: Python 3, SymPy, NumPy, SciPy.

## Relationship to prior work
Çelik, Isoldi, Portakal and Zucal, *Stable Coexistence in Ecologies and Games*, arXiv:2609.09286v1 (first public September 8, 2026), Theorem 4.2, prove that for arbitrary growth and pairwise coefficients, higher-order interactions can be added to obtain a locally asymptotically stable feasible equilibrium. Their construction uses total-population polynomials and supports general mixed-index higher-order tensor entries. The existence of fourth-order augmentation **is prior work**. The present theorem imposes a stricter support constraint (only two self-only coefficients for each species) and establishes a common, positive-invariant attraction cube with an explicit uniform logarithmic contraction rate, which that theorem does not assert.

Singh and Baruah, *Higher order interactions and species coexistence*, Theoretical Ecology 14 (2021), 71–83 (online 2020), study higher-order competitive effects and show that stronger intraspecific limitation can promote coexistence, in restricted ecological models. Duran-Sala, Meloni and Calleja-Solanas, arXiv:2501.09172 (initial 2025), study the stabilizing limits of mixed higher-order competition in heterogeneous communities. Hou and Baigent, *Global stability and repulsion in autonomous Kolmogorov systems*, Comm. Pure Appl. Anal. 14 (2015), develop global stability criteria on compact invariant sets. These results supply related biological mechanisms and established dynamical techniques, but the inspected statements do not claim the precise all-coefficient sparse completion and fixed-cube exponential estimate above.

## Limitations
The lower bound for maximum interaction order is universal over all prescribed coefficients, not a minimality theorem for the exact number of nonzero tensor entries. The gain \(L\) can be biologically very large and this is a mathematical existence construction, not an inferred mechanistic model or experimentally viable parameter choice. The proof does not give global attraction from the whole positive orthant, does not permit arbitrary fixed nonzero higher-order cross terms, and does not establish resilience to arbitrary perturbations of the added coefficients. The independent scientific assessment and definitive historical-priority analysis have not been performed; related diagonal-feedback and contraction results remain a historical-priority risk.

## References
1. T. Ö. Çelik, V. A. Isoldi, I. Portakal, G. Zucal, *Stable Coexistence in Ecologies and Games*, arXiv:2609.09286v1, 2026, https://arxiv.org/abs/2609.09286 .
2. P. Singh, G. Baruah, *Higher order interactions and species coexistence*, Theoretical Ecology 14, 71–83 (2021), first online 2020, https://doi.org/10.1007/s12080-020-00481-8 .
3. M. Duran-Sala, S. Meloni, V. Calleja-Solanas, *On the stability of competitive ecological communities with pairwise and higher-order interactions*, arXiv:2501.09172, 2025, https://arxiv.org/abs/2501.09172 .
4. Z. Hou, S. Baigent, *Global stability and repulsion in autonomous Kolmogorov systems*, Commun. Pure Appl. Anal. 14 (2015), 1205–1238, https://doi.org/10.3934/cpaa.2015.14.1205 .
