# Critical-window survival law for a randomly attacked cycle

## Finding

Let \(C_n\) be the simple cycle on \(n\) vertices. Each edge independently transmits an attack with probability \(p_n=1-\lambda/n\), where \(\lambda>0\) is fixed and \(n>\lambda\). A uniformly chosen seed is attacked, and the attack propagates along every retained edge; equivalently, the infected set is the connected component of the seed in bond percolation with retention probability \(p_n\). Write \(K_n\) for the number of infected vertices and \(Y_n=1-K_n/n\) for the surviving fraction.

Then \(Y_n\) converges in distribution to a random variable \(Y_\lambda\) with an atom at zero and a continuous density on \((0,1)\):

\[
\Pr(Y_\lambda=0)=(1+\lambda)e^{-\lambda},\qquad
f_\lambda(y)=\lambda^2(1-y)e^{-\lambda(1-y)}\quad(0<y<1).
\]

Its cumulative distribution function on \([0,1]\) is

\[
F_\lambda(y)=(1+\lambda(1-y))e^{-\lambda(1-y)}.
\]

For each fixed \(y<1\), \(F_\lambda(y)\) is strictly decreasing in \(\lambda\); hence the surviving fraction is stochastically increasing as \(\lambda\) grows (equivalently, as the per-edge transmission probability decreases within this scaling window).

In the network-formation interpretation where every cycle edge is purchased exactly once at a fixed cost \(c_e\), the total connectivity benefit after the attack is \((n-K_n)^2\): when the infected component is proper, the remaining vertices form one path of size \(n-K_n\), and if the attack reaches the entire cycle the benefit is zero. Therefore

\[
\lim_{n\to\infty}\frac{\mathbb E[\text{total connectivity benefit}]-nc_e}{n^2}
=\mathbb E[Y_\lambda^2]
=1-\frac{4(1-e^{-\lambda})}{\lambda}
+\frac{6(1-(\lambda+1)e^{-\lambda})}{\lambda^2}.
\]

The expression tends to \(0\) as \(\lambda\downarrow0\), with leading term \(\lambda^2/12\), and to \(1\) as \(\lambda\to\infty\). The law gives the full survival-risk profile, not only the first two moments of the percolation cluster.

## Assumptions and scope

The graph is exactly \(C_n\); edge transmissions are independent; the seed is uniform over vertices; and \(p_n=1-\lambda/n\) with fixed \(\lambda>0\). The scaling is a near-certain-transmission window, distinct from the fixed-transmission-probability regime. The welfare statement assumes each of the \(n\) cycle edges is purchased once and costs \(c_e=O(1)\). No equilibrium claim is made for this regime. The result concerns the fraction of vertices that survive the single seeded cascade and the corresponding connectivity-benefit functional.

## Proof

Let \(M_n\) be the number of edges that fail to transmit. Then \(M_n\sim\operatorname{Bin}(n,\lambda/n)\), so \(M_n\Rightarrow M\), where \(M\sim\operatorname{Poisson}(\lambda)\).

If \(M_n=0\), every edge transmits and the attack reaches the whole cycle. If \(M_n=1\), deleting the single failed edge turns the percolation subgraph into a path on all \(n\) vertices, so it is still connected and the attack again reaches all vertices. Thus \(Y_n=0\) on these two events. Their limiting combined probability is \(\Pr(M\le1)=e^{-\lambda}(1+\lambda)\).

Condition on \(M_n=m\ge2\), with \(m\) fixed as \(n\to\infty\). The failed edges split the cycle into \(m\) consecutive components. Their normalized lengths converge to a \(\operatorname{Dirichlet}(1,\ldots,1)\) vector: choosing the failed-edge set uniformly gives uniform positive compositions of \(n\), whose normalized composition converges to uniform simplex measure. Because the seed is uniform among vertices, it selects a component with probability proportional to that component's length. If \((S_1,\ldots,S_m)\sim\operatorname{Dirichlet}(1,\ldots,1)\), a size-biased coordinate has density \(m(m-1)x(1-x)^{m-2}\) on \((0,1)\), namely the \(\operatorname{Beta}(2,m-1)\) law. Therefore the surviving fraction \(1-x\), conditional on \(M=m\), has density

\[
 f_{Y\mid M=m}(y)=m(m-1)y^{m-2}(1-y),\quad 0<y<1.
\]

The mixture over the Poisson limit is justified by first truncating \(M_n\) at a fixed integer and then using tightness of \(M_n\); the variables \(Y_n\) are bounded by one. For \(0<y<1\), the limiting density is

\[
\begin{aligned}
f_\lambda(y)
&=e^{-\lambda}(1-y)\sum_{m=2}^{\infty}\frac{\lambda^m}{m!}m(m-1)y^{m-2}\\
&=\lambda^2(1-y)e^{-\lambda(1-y)},
\end{aligned}
\]
using \(m(m-1)/m!=1/(m-2)!\). Integrating this density and adding the atom at zero gives \(F_\lambda(y)=(1+\lambda(1-y))e^{-\lambda(1-y)}\). Its derivative with respect to \(\lambda\), for fixed \(y<1\), is \(-\lambda(1-y)^2e^{-\lambda(1-y)}<0\), proving stochastic monotonicity.

For the welfare formula, the surviving vertices form a single path whenever \(Y_n>0\), so the sum of their component sizes is \((n-K_n)^2=n^2Y_n^2\); it is also zero when \(Y_n=0\). Since \(0\le Y_n^2\le1\), convergence in distribution gives convergence of second moments. The limiting second moment is

\[
\int_0^1 y^2\lambda^2(1-y)e^{-\lambda(1-y)}\,dy
=1-\frac{4(1-e^{-\lambda})}{\lambda}
+\frac{6(1-(\lambda+1)e^{-\lambda})}{\lambda^2}.
\]
The purchase cost contributes \(nc_e/n^2=c_e/n\to0\). Taylor expansion at zero gives \(\mathbb E[Y_\lambda^2]=\lambda^2/12+O(\lambda^3)\); the formula also gives the limit one as \(\lambda\to\infty\).

## Verification

The derivation is analytic; finite simulations or finite enumerations are not used as proof. The mass check is exact: the atom \((1+\lambda)e^{-\lambda}\) plus the integral of the density equals one. The density differentiates the stated CDF, and the CDF has the correct endpoints \(F_\lambda(0)=(1+\lambda)e^{-\lambda}\) and \(F_\lambda(1)=1\). Direct integration gives the displayed second moment. The cost term vanishes after division by \(n^2\) for any bounded fixed edge cost.

## Relationship to prior work

Chen, Jabbari, Kearns, Khanna, and Morgenstern study network formation under random seeded attacks and independent-cascade propagation, deriving equilibrium edge-density and welfare bounds. Their paper does not state the near-one scaling law \(p_n=1-\lambda/n\) or the limiting survival-fraction distribution proved here. Jevtić, Lanchier, and La Salle give exact first and second moments of typical bond-percolation cluster sizes on rings, paths, and stars; their moment results are directly relevant to the welfare functional, so the second-moment corollary alone is not claimed as the main novelty. Allard and coauthors give a general finite-graph method for exact bond-percolation component distributions. The present claim is the explicit Poisson-mixture limit law for the surviving fraction in the critical window, including its atom, density, and stochastic ordering; no inspected source states that limit in this network-attack formulation.

## Limitations

The result is for a single seeded cascade on a cycle and the scaling \(p_n=1-\lambda/n\). It does not classify equilibria, establish an equilibrium in this regime, or extend automatically to other graph families or multiple seeds. The full text of the 2020 ring-moment paper was not available through the accessible open sources during this review; its abstract confirms exact first and second moments, and that remains a residual comparison risk for moment-only corollaries. A generic finite-graph percolation algorithm can in principle compute finite-size distributions, but no explicit critical-window limit was found in the inspected sources.

## References

1. “Network Formation under Random Attack and Probabilistic Spread,” IJCAI 2019, pp. 180–186; arXiv:1906.00241 (first public version dated 2019-06-01).
2. P. Jevtić, N. Lanchier, and A. La Salle, “First and second moments of the size distribution of bond percolation clusters on rings, paths and stars,” *Statistics & Probability Letters* 161 (2020), 108714, DOI: 10.1016/j.spl.2020.108714.
3. A. Allard, L. Hébert-Dufresne, P.-A. Noël, V. Marceau, and L. J. Dubé, “Exact solution of bond percolation on small arbitrary graphs,” arXiv:1201.4369 (first public version dated 2012-01-20).
