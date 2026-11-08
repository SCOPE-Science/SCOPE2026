# Poisson plateau of fixed-size components in high-retention finite-range cycle percolation

## Finding

Fix an integer \(m\ge2\), a constant \(\lambda\in(0,\infty)\), and an integer \(K\ge m\). In independent bond percolation on the \(m\)-th power of an \(n\)-cycle, suppose the edge deletion probability \(q_n\in(0,1)\) satisfies

\[
q_n\longrightarrow0,\qquad n q_n^{m(m+1)}\longrightarrow\lambda.
\]

Write \(N_{n,k}\) for the number of connected components of the retained graph having exactly \(k\) vertices. Then

\[
(N_{n,m},\ldots,N_{n,K})\ \Longrightarrow\ (P_m,\ldots,P_K),
\]

where the limit coordinates are independent and

\[
P_m\sim\operatorname{Poisson}(m\lambda),\qquad
P_k\sim\operatorname{Poisson}(\lambda)\quad(m+1\le k\le K).
\]

The exceptional factor \(m\) at size \(m\), followed by a size-independent Poisson intensity for every other fixed size, is the finite-component *Poisson plateau*. The statement is finite-dimensional for each fixed \(K\); it is not a connectivity theorem.

## Assumptions and scope

For each \(n>2m\), let \(H_n=C_n^m\) have vertex set \(\mathbb Z/n\mathbb Z\), with distinct vertices adjacent if their cyclic distance is at most \(m\). Retain each of its \(nm\) edges independently with probability \(1-q_n\). Components refer to maximal connected components of the retained graph, not connected induced vertex sets of the host. The constants \(m,K,\lambda\) remain fixed as \(n\to\infty\), with \(K\ge m\ge2\). No uniformity in growing \(K\), no claim about isolated vertices or components of size below \(m\), and no claim about the largest component are asserted.

## Proof

**1. Boundary minimizers for bounded connected sets.** Let \(S\) be a host-connected set with \(|S|=k\ge m\), with \(k\) fixed. For sufficiently large \(n>mk\), at least one of its cyclic successive gaps exceeds \(m\). Cut the circle at such a gap and write its vertices as increasing integers \(x_1<\cdots<x_k\). No host edge of \(S\) crosses the cut. Its induced edge count \(e_H(S)\) is therefore bounded by

\[
e_H(S)\le\sum_{j=1}^k\min\{m,j-1\}
=mk-\frac{m(m+1)}2.
\]

Every vertex of \(H_n\) has degree \(2m\); consequently its edge boundary \(\partial_H S\) obeys

\[
|\partial_H S|=2mk-2e_H(S)\ge B:=m(m+1).
\]

For \(k=m\), equality means that \(S\) is a clique of size \(m\): after the unique macroscopic gap, its other \(m-1\) vertices may be any \(m-1\) of the next \(m\) sites. For \(k\ge m+1\), equality forces each \(x_j\), \(j\ge m+1\), to be adjacent to all \(m\) preceding vertices and the first \(m\) vertices to be a clique. In particular \(x_{m+1}-x_1\le m\); hence these first \(m+1\) distinct integers are consecutive. Inductively \(x_j-x_{j-m}\le m\) forces every next gap to equal one. So \(S\) is a cyclic interval of \(k\) consecutive sites. Conversely all those sets attain the boundary \(B\).

For large \(n\), there are exactly \(mn\) distinct \(m\)-cliques (the unique large cyclic gap gives one starting location and \(\binom m{m-1}=m\) choices), and exactly \(n\) cyclic intervals of every fixed size \(k\ge m+1\). Since boundary sizes are even, every other host-connected \(k\)-set has boundary at least \(B+2\).

**2. Exclude all nonminimal small components.** For fixed \(k\), the number of \(k\)-vertex connected subsets of a graph with maximum degree \(2m\) is \(O_{m,k}(n)\), by rooting at a vertex and enumerating bounded-size spanning trees. A retained connected component \(S\) must be host-connected and have all host boundary edges deleted. Therefore

\[
\Pr\{\exists\text{ a size-}k\text{ component with }|\partial_H S|>B\}
\le O_{m,k}(nq_n^{B+2})=o(1).
\]

Summing over the finite range \(m\le k\le K\) preserves this bound.

**3. Replace true components by boundary events.** Let \(\mathcal F_{n,m}\) contain all \(m\)-cliques, and \(\mathcal F_{n,k}\) for \(k>m\) all length-\(k\) cyclic intervals. For each \(S\) in their union define \(I_S=\mathbf1\{\text{all }B\text{ edges in }\partial_H S\text{ are absent}\}\). All these indicators have probability \(q_n^B\). If \(I_S=1\) but \(S\) is not a retained connected component, its induced retained graph is disconnected; as the host induced graph is connected and has a fixed number of edges, this requires at least one absent internal edge. By independence,

\[
\Pr\{I_S=1,\ G_n[S]\text{ disconnected}\}\le |E_H(S)|q_n^{B+1}.
\]

There are \(O_{m,K}(n)\) such sets, so the expected number of disagreements is \(O(nq_n^{B+1})=o(1)\). Along with step 2 this implies

\[
\Pr\left\{(N_{n,k})_{k=m}^K\ne\left(\sum_{S\in\mathcal F_{n,k}}I_S\right)_{k=m}^K\right\}\to0.
\]

**4. Joint Poisson limit.** Associate to \(I_S\) the fixed-size edge set \(D_S=\partial_H S\). Two such indicators are independent whenever their edge sets are disjoint. Every candidate is contained in a cyclic window of bounded length depending on \(m,K\); thus each \(D_S\) shares edges with at most \(O_{m,K}(1)\) other candidate cutsets.

Distinct candidates cannot have identical cutsets for sufficiently large \(n>2K\). Indeed \(D_S=D_T\) would imply that the symmetric-difference membership \(\mathbf1_S\oplus\mathbf1_T\) is constant along every host edge. Since \(H_n\) is connected this makes \(S=T\) or \(S=T^c\), the latter impossible when both sizes are at most \(K<n/2\). Consequently, whenever two different candidate cutsets overlap, their union has at least \(B+1\) edges.

Fix nonnegative integers \(r_m,\ldots,r_K\) and expand the mixed factorial moment of the sums in step 3 as a sum over \(r=\sum r_k\) distinct labeled candidates of the prescribed sizes. Partition candidates into connected clusters according to intersections among their cutsets. If there are \(c\) clusters, the number of such configurations is \(O_{m,K,r}(n^c)\), because each cluster can be placed after choosing one of \(O(n)\) translations and its remaining vertices have bounded relative displacement. Cutsets from different clusters are disjoint. If at least one cluster contains two candidates, their union has at least \(B+1\) edges and every other cluster has at least \(B\) edges. Hence the total contribution of all tuples with any nontrivial cluster is

\[
O_{m,K,r}\left(\sum_{c=1}^{r-1}n^c q_n^{cB+1}\right)=o(1),
\]

using \(nq_n^B\to\lambda\). Tuples consisting solely of singleton clusters have mutually disjoint cutsets and therefore probability exactly \(q_n^{rB}\). Their count equals

\[
\bigl(mn\bigr)^{r_m}\prod_{k=m+1}^K n^{r_k}+O_{m,K,r}(n^{r-1}).
\]

The mixed factorial moments therefore converge to

\[
(m\lambda)^{r_m}\prod_{k=m+1}^K\lambda^{r_k},
\]

which are precisely those of independent Poisson variables of the stated means. Multivariate factorial-moment determinacy and the approximation in step 3 prove the theorem. \(\square\)

## Verification

The standalone script `verify_band.py` uses integer arithmetic to check the host cut-size minimizers for \(m=2,3,4\), component sizes \(m\le k\le m+3\), and each enumerated configuration in a finite local window, as well as the \(mn\) count of host \(m\)-cliques on a finite cycle. The script reported `LOCAL_CHECKS_PASS 95879`. Those checks are finite diagnostics; the preceding analytic arguments establish the all-\(n\), all-fixed-\(m\) limit. Run with `python3 verify_band.py`.

## Relationship to prior work

Chakraborty, Luh, and Singh (2026, arXiv:2610.42107v1) formulate the same band-percolation model and prove an isolated-vertex Poisson law in the substantially different growing-bandwidth regime \(m/\log n\to\infty\). Their Section 7 explicitly asks about nontrivial finite interval components at small bandwidth; their results do not imply the fixed-\(m\), high-retention vector limit here. Chang and Shrock (2021, arXiv:2105.13415) compute *mean* percolation cluster counts in certain infinite lattice strips, but their reported theorems neither specify the finite-cycle-power geometry nor furnish the joint critical-window Poisson law or the exceptional \(m\)-clique intensity. Standard local-dependence Poisson arguments inform step 4, but the geometric boundary minimizer classification and resulting flat intensity profile are additional model-specific inputs.

## Limitations

The theorem does not resolve the connectivity critical window of fixed-bandwidth cycle powers, the number of components of unbounded size, nor any growing-\(K\) joint limit. In fact, components smaller than \(m\) can have diverging counts at the stated scale. Historical priority remains subject to comparison with broader lattice-transfer and rare-cut limit results; no independent mathematical audit has been performed. Computations are checks of finite instances only.

## References

1. Shantanav Chakraborty, Kyle Luh, and Rudransh Pratap Singh, *Band Random Graphs: Connectivity, Geometry, and Transport* (2026), arXiv:2610.42107v1, https://arxiv.org/abs/2610.42107 (first publicly posted 2026-10-30); especially Sections 1, 4, and 7.
2. Shu-Chiuan Chang and Robert Shrock, *Exact Results for Average Cluster Numbers in Bond Percolation on Infinite-Length Lattice Strips* (2021), arXiv:2105.13415, https://arxiv.org/abs/2105.13415, published as *Physical Review E* **104**, 044107.
