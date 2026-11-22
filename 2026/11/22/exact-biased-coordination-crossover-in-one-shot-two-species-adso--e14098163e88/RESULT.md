# Exact biased coordination crossover in one-shot two-species adsorption on regular trees

## Finding

Consider independent one-shot deposition attempts of two incompatible particle species on the infinite regular tree of degree \(z\). The complete root one-point law is determined by a two-dimensional cavity system at any color bias. Its conserved quantity gives the exact signed-density identity
\[
\rho_A(t)-\rho_B(t)=(2p-1)t.
\]
At equal species probabilities the total terminal coverage is
\[
\rho_z(1)=
\begin{cases}
1-e^{-1},&z=2,\\
1-(z/2)^{-2/(z-2)},&z>2.
\end{cases}
\]
For large degree, \(\rho_z(1)\sim 2\log(z/2)/z\). By contrast, for each fixed \(p>1/2\), the minority species B has the sharp asymptotic
\[
\rho_B(1)=\frac1z\log\frac{p}{2p-1}+o(z^{-1}),\qquad
\rho_A(1)=2p-1+\rho_B(1).
\]
Interchange species for \(p<1/2\). These are statements about one-shot adsorption, not the repeated-proposal model, for which an initially rejected site may be attempted again.

## Assumptions and scope

The substrate is the infinite, undirected \(z\)-regular tree, where the integer \(z\ge2\) is fixed before the infinite-graph process is constructed. Every vertex independently receives one attempted deposition time uniformly distributed on \([0,1]\), and independently a proposed type A with probability \(p\in(0,1)\) or B with probability \(q=1-p\). At that time the vertex becomes permanently occupied by its proposed type if and only if no adjacent vertex has already accepted the *opposite* type. Failed proposals are never retried. Let \(\rho_A(t)\) and \(\rho_B(t)\) denote the probabilities that a distinguished vertex has accepted A or B by time \(t\in[0,1]\). They are deterministic occupation probabilities, not asserted almost-sure coverage limits on finite graphs.

The boundary biases \(p=0,1\) have trivial full coverage by the sole allowed species at final time. The integer \(z=2\) is the infinite line, serving as an exact reference case.

## Proof

**1. Well-defined construction.** To determine a vertex's occupancy, inspect only neighbors with strictly earlier proposed times, then earlier neighbors of those vertices, and so on. For a fixed path of \(n\) edges all its \(n+1\) independent continuous clocks must occur in strictly decreasing order, an event of probability \(1/(n+1)!\). The number of such paths from a fixed root is at most \(z(z-1)^{n-1}\), so the probability of any unresolved dependency reaching depth \(n\) is at most \(z(z-1)^{n-1}/(n+1)!\to0\). Every fixed vertex therefore has an almost surely finite causal past, defining the infinite process without boundary assumptions.

**2. Exact two-type cavity equations.** Delete the edge from a vertex to its parent and hold the parent absent. Let \(a(t)\) and \(b(t)\) be the probabilities that the branch-root has accepted A and B by time \(t\). It has \(z-1\) independent descendant branches. Because the branch-root has not yet proposed at its own time, its descendants behave as though it were absent. Conditioning on a proposed A in \([t,t+dt]\), acceptance requires all descendants to have no B, each with probability \(1-b(t)\). Therefore
\[
 a'(t)=p(1-b(t))^{z-1},\qquad
 b'(t)=q(1-a(t))^{z-1},\qquad a(0)=b(0)=0.
\]
At the distinguished full root the corresponding derivatives use \(z\) independent branches rather than \(z-1\):
\[
 \rho_A'(t)=p(1-b(t))^z,\qquad
 \rho_B'(t)=q(1-a(t))^z,\qquad
 \rho_A(0)=\rho_B(0)=0.
\]
The right-hand sides are locally Lipschitz on the closed probability square; hence these equations uniquely determine the probabilities for every allowed parameter. This is an exact finite-dimensional characterization for arbitrary bias.

**3. Conserved density imbalance.** Set \(u=1-a\), \(v=1-b\), so \(u'=-pv^{z-1}\) and \(v'=-qu^{z-1}\). Differentiating \(q(1-u^z)\) and \(p(1-v^z)\) yields in both cases \(pqz u^{z-1}v^{z-1}\). Both vanish initially; thus
\[
 q(1-u(t)^z)=p(1-v(t)^z).
\]
Rearrangement gives \(pv(t)^z-qu(t)^z=p-q\). By the full-root equations this is \(\rho_A'(t)-\rho_B'(t)=p-q\), so integration gives the claimed exact all-time imbalance identity.

**4. Balanced adsorption.** For \(p=q=1/2\), uniqueness implies \(a=b\). Then \(u'=-(1/2)u^{z-1}\). For \(z>2\),
\[
 u(t)=\bigl[1+(z-2)t/2\bigr]^{-1/(z-2)};
\]
for \(z=2\), \(u(t)=e^{-t/2}\). Since the total occupation rate is \(u^z\), and \((u^2)'=-u^z\), the total probability is exactly \(1-u(t)^2\). The displayed formula follows. For fixed \(t>0\), the total occupancy strictly decreases with \(z\), because for \(x>0\) the function \(\log(1+xt/2)/x\) strictly decreases: its derivative has numerator \([xt/(2+xt)]-\log(1+xt/2)<0\). At \(t=1\), expanding the exponential gives \(1-\exp[-2\log(z/2)/(z-2)]\sim2\log(z/2)/z\).

**5. Unequal bias and the exact minority coefficient.** It suffices to take \(p>q>0\), and write \(\delta=p-q>0\). The invariant yields
\[
 v(t)^z=\frac{\delta+qu(t)^z}{p}\ge\frac{\delta}{p}.
\]
As \(0\le v\le1\), \(a'(t)=pv(t)^{z-1}\ge pv(t)^z\ge\delta\), hence \(u(t)\le1-\delta t\). In particular, \(u(1)^z\le(1-\delta)^z\to0\). Using \(\rho_B(1)=q\int_0^1 u(t)^z\,dt\), substituting \(u\) via its differential equation, then \(r=u^z\), gives the *exact* finite-degree representation
\[
 z\rho_B(1)=\frac qp\int_{u(1)^z}^1
 r^{1/z}\left(\frac{\delta+qr}{p}\right)^{-(z-1)/z}\,dr.
\]
On the integration interval, the integrand (including \(q/p\)) is bounded by \(q/\delta\). Pointwise for \(r>0\), it tends to \(q/(\delta+qr)\), while the lower limit tends to zero. Dominated convergence therefore yields
\[
 \lim_{z\to\infty}z\rho_B(1)=\int_0^1\frac{q\,dr}{\delta+qr}
 =\log\left(\frac{\delta+q}{\delta}\right)
 =\log\left(\frac p{p-q}\right).
\]
The exact imbalance identity gives \(\rho_A(1)=p-q+\rho_B(1)\), concluding the result. Exchange labels when \(p<q\). The limit is taken at *fixed* strictly nonzero bias; no uniform asymptotic through \(p=1/2\) is claimed.

## Verification

The accompanying standalone `check.py` runs an independently programmed numerical integration of the cavity equations across balanced and biased cases. It compares the complete equal-bias formula, the all-time density imbalance, the analytic one-dimensional hyperbolic formula in do Amaral--dos Santos, and causal finite-depth Monte Carlo estimates. It also checks finite-degree values against the limiting minority coefficient. Successful execution reports 296 deterministic assertions. These numerical tests are consistency checks, not a substitute for the infinite-tree and large-degree arguments above.

## Relationship to prior work

Do Amaral and dos Santos (2023) define the same one-attempt two-type rule on the infinite line and derive the all-bias one-dimensional density. Taking \(z=2\) in this theorem reproduces that benchmark exactly; this special case is not claimed new. Meyfroyt (2017 thesis, Chapter 5; 2018 journal paper) studies one-attempt random sequential activation on trees with blocking according to the *number* of previously active neighbors, but the binary active/inactive threshold mechanism does not encode the rule that equal-color occupied neighbors are allowed and opposite-color neighbors alone block. Martins, Dickman and Ziff (2022 preprint; 2023 journal) study two-type antagonistic adsorption on a two-dimensional lattice with **repeated proposals** and prove the leading rare-minority coefficient \(q/(z+1)\); that first-order law is likewise not claimed new and its agreement with the one-attempt process does not imply the all-bias tree formula or its high-degree asymptotics.

Related public indexed results include exact one-attempt finite-cycle coverage and one-dimensional same-type cluster laws, and repeated-proposal complete-multipartite saturation. These differ in graph, retry policy, or observable. The claimed addition is the exact tree cavity characterization, the balanced closed all-degree density, and the fixed-bias sharp high-degree minority coefficient, as one combined result.

## Limitations

The exact formulas require an infinite acyclic regular substrate, independent continuous attempt times and independently sampled fixed proposal types, and no retry after rejection. No extension to finite random regular graphs, cyclic lattices, repeated-proposal dynamics, other adsorption exclusion rules, or uniform limits in the joint regime \(p-1/2\to0\), \(z\to\infty\) is proved. The tree-degree limit concerns the one-point density, not percolation or almost-sure cluster structure. Bibliographic priority is assessed against inspected accessible sources and indexed abstracts, not certified against every possible unpublished or unindexed theorem.

## References

1. C. S. do Amaral and D. C. dos Santos, *One-dimensional AB random sequential adsorption with one deposition per site*, arXiv:2306.09786 (initial public version 16 June 2023), https://arxiv.org/abs/2306.09786 ; Journal of Physics A 56 (2023), 475204, doi:10.1088/1751-8121/ad02cd.
2. T. M. M. Meyfroyt, *Threshold-based communication algorithms for large-scale mesh networks*, PhD thesis, Eindhoven University of Technology (2017), Chapter 5, https://pure.tue.nl/ws/portalfiles/portal/85310076/20171122_Meyfroyt.pdf ; related journal article *Degree-dependent threshold-based random sequential adsorption on random trees*, Advances in Applied Probability 50 (2018), 302--326, doi:10.1017/apr.2018.14.
3. P. H. L. Martins, R. Dickman and R. M. Ziff, *Percolation in two-species antagonistic random sequential adsorption in two dimensions*, arXiv:2211.04622 (initial preprint 9 November 2022), https://arxiv.org/abs/2211.04622 ; Physical Review E 107 (2023), 024104.
