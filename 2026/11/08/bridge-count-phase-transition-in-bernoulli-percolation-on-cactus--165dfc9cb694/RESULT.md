# Bridge-count phase transition in Bernoulli percolation on cactus graphs

## Finding

Let \(G\) be a finite connected simple cactus graph with \(m\ge1\) edges. Write \(c_1,\ldots,c_r\ge3\) for the lengths of its (edge-disjoint) simple cycles and \(b=m-\sum_{j=1}^r c_j\) for the number of edges outside those cycles. Independently retain each edge with probability \(p\in(0,1)\), and let \(X\) count all retained edges and \(B\) count retained edges that are bridges in the retained spanning subgraph. Then the *entire joint probability-generating function* is

\[
\mathbb E[s^X t^B]=(1-p+pst)^b\prod_{j=1}^r\left[(1-p+pst)^{c_j}+(ps)^{c_j}(1-t^{c_j})\right].
\]

In particular,

\[
\operatorname{Cov}(X,B)=p(1-p)\left[m-\sum_{j=1}^r c_j^2p^{c_j-1}\right].
\]

This covariance changes sign exactly once, from positive to negative, at a unique \(p_*\in(0,1)\), **if and only if** \(\sum_j c_j^2>m\), equivalently \(b<\sum_j c_j(c_j-1)\). The threshold solves \(\sum_j c_j^2 p_*^{c_j-1}=m\). If \(\sum_j c_j^2\le m\), the covariance is strictly positive for every \(0<p<1\). Both endpoints \(p=0,1\) have zero covariance and are not counted as interior crossings.

There is also a fixed-edge-budget conclusion. Under the uniform distribution on all retained \(e\)-edge subsets, \(0\le e\le m\), the conditional mean of bridges is

\[
 f(e):=\mathbb E[B\mid X=e]=e-\sum_{j=1}^r c_j\frac{(e)_{\underline{c_j}}}{(m)_{\underline{c_j}}}.
\]

This sequence is discretely concave for every cactus. If \(\sum_j c_j^2>m\), it rises initially and has a unique maximizing position or two adjacent maximizing positions (a one-step plateau); otherwise it is nondecreasing. Here \((a)_{\underline k}=a(a-1)\cdots(a-k+1)\) for nonnegative integers \(a,k\), with the product zero when \(k>a\).

## Assumptions and scope

The base graph is a finite connected simple graph in which each edge lies in at most one simple cycle, so its noncyclic edges are bridges. Its cycles may share vertices but never edges. The retained graph uses all original vertices and an independent Bernoulli retention indicator for every original edge; its bridge count includes bridges in any connected component. There is no restriction on the number, location, or lengths of the edge-disjoint cycles, beyond \(c_j\ge3\). The case \(r=0\) is a tree and is included. The case \(m=0\) is excluded. The same identity is valid for a disconnected cactus forest with \(m\ge1\), but this extension is not needed for the statement.

## Proof

Every simple cycle of the retained subgraph must have been a simple cycle of the base cactus. For a base cycle \(C_j\), if all its \(c_j\) edges survive, they all lie on a retained cycle and therefore none is a bridge. If even one is absent, no retained edge of that base cycle lies on *any* retained cycle; hence every retained edge of that cycle is a bridge. Noncyclic original edges are always bridges when retained. Thus, writing \(K_j\) for the number of retained edges on base cycle \(C_j\) and \(I_j\) for its all-retained indicator,

\[
 X=Y+\sum_{j=1}^rK_j,\qquad B=Y+\sum_{j=1}^r(K_j-c_jI_j),
\]

where \(Y\sim\mathrm{Bin}(b,p)\). The edge blocks in this decomposition are mutually independent. Within a cycle block, the ordinary binomial generating function is \((1-p+pst)^{c_j}\). Its all-retained term \((pst)^{c_j}\) must be replaced by \((ps)^{c_j}\) because the \(c_j\) edges then contribute zero to \(B\). Multiplying independent block contributions proves the displayed bivariate generating function.

For each \(j\), \(\mathbb E I_j=p^{c_j}\) and \(\operatorname{Cov}(K_j,I_j)=c_j p^{c_j}(1-p)\). Since \(\operatorname{Var}(X)=mp(1-p)\), subtracting \(\sum_j c_jI_j\) gives precisely the claimed covariance. The function \(q(p)=\sum_j c_j^2p^{c_j-1}\) is continuous, satisfies \(q(0)=0\), and is strictly increasing on \((0,1)\) if any cycle exists. As \(q(1)=\sum_j c_j^2\), this proves the if-and-only-if threshold and its uniqueness; if there are no cycles, the positive covariance is \(mp(1-p)\). Since \(m=b+\sum_j c_j\), the equivalent inequality follows.

Conditional on \(X=e\), the selected \(e\)-edge subset is uniform. The probability that all \(c_j\) edges of cycle \(j\) were selected is \((e)_{\underline{c_j}}/(m)_{\underline{c_j}}\), proving the conditional mean formula. The forward differences are

\[
 f(e+1)-f(e)=1-\sum_{j=1}^r\frac{c_j^2(e)_{\underline{c_j-1}}}{(m)_{\underline{c_j}}},\quad 0\le e<m,
\]

and the second differences are

\[
 f(e+2)-2f(e+1)+f(e)=-\sum_{j=1}^r\frac{c_j^2(c_j-1)(e)_{\underline{c_j-2}}}{(m)_{\underline{c_j}}}\le0,
\]

for \(0\le e\le m-2\). The first difference equals \(1\) at \(e=0\); the final one equals \(1-\sum_j c_j^2/m\) at \(e=m-1\). Concavity gives the claimed conditional monotonicity/unimodality, allowing an equality plateau between two adjacent budgets.

## Verification

The accompanying `verify_cactus.py` independently enumerates all edge subsets of eight explicitly specified cacti, determines bridge counts by graph traversal with each retained edge removed in turn, and checks the exact joint distribution, covariance, and conditional means for three nontrivial rational retention probabilities per graph. It also checks discrete concavity and the threshold criterion. The resulting 24 exhaustive Bernoulli-model comparisons and eight conditional concavity checks pass. Finite enumeration is a cross-check; the proof for arbitrary cactus size is the algebraic cycle-block argument above.

For one triangle with no noncyclic edges, \(m=3,c_1=3\), the unique crossing is \(p_*=1/\sqrt3\). Attaching six noncyclic bridges gives \(m=9\), so the covariance is positive at every interior \(p\) and reaches zero only at \(p=1\); these examples demonstrate both sides of the sharp criterion.

## Relationship to prior work

Allard, Hébert-Dufresne, Noël, Marceau and Dubé (arXiv:1201.4369, original posting 2012-01-20) provide a general exact computational framework for component-size distributions under independent bond percolation on finite graphs, with a computational burden that grows exponentially for arbitrary graphs. This does not explicitly give the bridge/edge joint probability-generating function or its all-size cactus threshold. Bonneau, Tishby, Biham, Katzav and Kühn (arXiv:2101.09977, 2021) examine single-edge bridge probabilities in percolation on networks and develop cavity methods; their inspected bridge section does not provide a joint count distribution or this finite-cactus phase criterion. Chae, Yook and Kim (arXiv:1209.1937, 2012) study *agglomerative* percolation on the triangular cactus, a different stochastic process. Known cycle decomposition of a cactus is the structural starting point, not claimed as new.

## Limitations

This statement does not apply directly to general graphs with overlapping cycles, for which an edge may belong to several alternative cycles. It assumes one common independent retention probability; heterogeneous probabilities would require a different threshold analysis. The result is an elementary, exact finite-graph theorem and does not establish a universal critical phenomenon for arbitrary networks. Historical completeness is not guaranteed: a broader reliability-polynomial or bridge-distribution identity might imply parts of the formula. The verification does not substitute for independent mathematical auditing.

## References

- A. Allard, L. Hébert-Dufresne, P.-A. Noël, V. Marceau, and L. J. Dubé, *Exact solution of bond percolation on small arbitrary graphs*, arXiv:1201.4369 (first posted 2012-01-20), https://arxiv.org/abs/1201.4369 .
- H. Bonneau, I. Tishby, O. Biham, E. Katzav, and R. Kühn, *The Fate of Articulation Points and Bredges in Percolation*, arXiv:2101.09977 (first posted 2021-01-25), https://arxiv.org/abs/2101.09977 .
- H. Chae, S.-H. Yook, and Y. Kim, *Agglomerative percolation on the Bethe lattice and the triangular cactus*, arXiv:1209.1937 (first posted 2012-09-10), https://arxiv.org/abs/1209.1937 .
