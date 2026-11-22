# A persistent component–edge covariance in random interval graphs

## Finding

For every integer \(n\ge2\), let \(G_n\) be the intersection graph of \(n\) intervals whose endpoints are \(2n\) independent draws from any **common atomless** probability law on the real line. Write \(C_n\) for the number of connected components and \(E_n\) for the number of graph edges. Define, for \(1\le k\le n-1\),
\[
p_{n,k}=\frac{\binom nk}{\binom{2n}{2k}}.
\]
Then the exact finite-sample mixed covariance is
\[
\boxed{\operatorname{Cov}(C_n,E_n)=-\frac23\sum_{k=1}^{n-1} k(n-k)p_{n,k}<0.}
\]
Furthermore,
\[
\operatorname{Var}(E_n)=\frac{n(n-1)(2n+1)}{45},
\quad
\operatorname{Cov}(C_n,E_n)\longrightarrow-\frac23,
\quad
\operatorname{Var}(C_n)\sim\frac1n,
\]
and the Pearson correlation obeys the sharp rate
\[
\boxed{n\operatorname{Corr}(C_n,E_n)\longrightarrow-\sqrt{10}.}
\]
Although \(\Pr(C_n>1)=n^{-1}+O(n^{-2})\), the unscaled covariance does not vanish: rare disconnections remove order-\(n\) expected intersection edges. The exact sign and asymptotic conclusions are independent of the common atomless endpoint distribution.

## Assumptions and scope

Intervals are formed by pairing \(U_{2i-1},U_{2i}\) into \([\min(U_{2i-1},U_{2i}),\max(U_{2i-1},U_{2i})]\), where all \(U_j\) are independent with the same atomless law. Intersections at shared endpoints occur with probability zero. The graph has vertex set \(\{1,\ldots,n\}\) and edges when the two closed intervals intersect. The formula applies to all integers \(n\ge2\); the sharp asymptotics take \(n\to\infty\). No continuity of a density or bounded support is required. Endpoint ties, dependent endpoints and heterogeneous endpoint laws are outside the theorem.

## Proof

**1. Matching and component cuts.** Every ordering of the \(2n\) labelled endpoints has equal probability. On deleting endpoint labels that identify intervals, their pairing is therefore a uniform perfect matching of the ordered positions \(1,\ldots,2n\). Let \(A_k\) be the event that the first \(2k\) positions are matched entirely within those positions. An interval crossing the cut after position \(2k\) exists exactly when \(A_k\) fails. A gap without any crossing interval separates two nonempty overlap components, and every separation between consecutive overlap components gives exactly such a gap. Hence
\[
C_n=1+\sum_{k=1}^{n-1}\mathbf1_{A_k}.
\]
The matching probability of a cut is
\[
\Pr(A_k)=\frac{(2k-1)!!(2n-2k-1)!!}{(2n-1)!!}
=\frac{\binom nk}{\binom{2n}{2k}}=p_{n,k}.
\]

**2. Conditional edge count.** Two independently generated intervals intersect in two of the three equally likely matchings of their four ordered endpoints, so \(\mathbb E E_m=2\binom m2/3=m(m-1)/3\). Given \(A_k\), the restrictions of the matching to the first \(2k\) and last \(2n-2k\) positions are independent uniform matchings, and no edge runs between the sides. Consequently
\[
\mathbb E(E_n\mid A_k)=\frac{k(k-1)+(n-k)(n-k-1)}3
=\mathbb E E_n-\frac23 k(n-k).
\]
Multiplying by \(\Pr(A_k)\), subtracting \(\Pr(A_k)\mathbb E E_n\), and summing over all cuts proves the finite covariance identity. Every summand is strictly positive for \(n\ge2\), proving strict negativity.

**3. Edge-count variance.** For any interval with endpoints \(0\le a<b\le1\) after the probability-integral transformation, the conditional probability that another interval intersects it is \(g(a,b)=1-a^2-(1-b)^2\). The density of \((a,b)\) on that triangle is \(2\), yielding
\[
\mathbb E g=\frac23,\qquad \mathbb E g^2=\frac{22}{45},\qquad
\operatorname{Var}(g)=\frac2{45}.
\]
For distinct graph edges, the indicators are independent when they have no vertex in common; when they share one vertex, their covariance is \(2/45\). Each edge indicator has variance \(2/9\), and there are \(3\binom n3\) unordered pairs of different edges sharing a vertex. Therefore
\[
\operatorname{Var}(E_n)=\frac29\binom n2
+2\cdot3\binom n3\frac2{45}
=\frac{n(n-1)(2n+1)}{45}.
\]

**4. Component-count moments and limiting rate.** Write \(S_n=\sum_{k=1}^{n-1}p_{n,k}\). For \(1\le j<k\le n-1\), conditional independence of the left matching given \(A_k\) gives
\[
\Pr(A_j\cap A_k)=p_{n,k}p_{k,j}.
\]
Thus the exact component variance is
\[
\operatorname{Var}(C_n)=S_n+2\sum_{1\le j<k\le n-1}p_{n,k}p_{k,j}-S_n^2.
\]
The ratio \(p_{n,k+1}/p_{n,k}=(2k+1)/(2n-2k-1)\) shows that \(p_{n,k}\) decreases up to the middle and is symmetric in \(k,n-k\). Its endpoint terms satisfy \(p_{n,1}=1/(2n-1)\); the next terms are \(p_{n,2}=O(n^{-2})\), \(p_{n,3}=O(n^{-3})\), and \(p_{n,4}=O(n^{-4})\). Bounding each interior half by its first term gives
\[
S_n=\frac1n+O(n^{-2}),\qquad
\sum_{k=1}^{n-1}k(n-k)p_{n,k}=1+O(n^{-1}).
\]
For the second assertion, separate \(k=1,2,3\) and their reflected terms; all remaining terms are bounded by \(O(n)\) terms of size at most \(n^2p_{n,4}=O(n^{-2})\). The first bound also implies \(S_m=O(m^{-1})\) uniformly over integers \(m\ge2\). Therefore
\[
\sum_{1\le j<k\le n-1}p_{n,k}p_{k,j}
=\sum_{k=2}^{n-1}p_{n,k}S_k=O(n^{-2}),
\]
by splitting at \(n/2\): on the left use the \(k=2\) term and the bound \(p_{n,k}\le p_{n,3}\) for \(k\ge3\); on the right use \(S_k=O(n^{-1})\) and \(\sum_kp_{n,k}=O(n^{-1})\). It follows that \(\operatorname{Var}(C_n)=n^{-1}+O(n^{-2})\). Bonferroni's inequalities and the same two-cut estimate yield \(\Pr(C_n>1)=n^{-1}+O(n^{-2})\). The covariance limit follows from the weighted sum, and dividing by the square root of both variances gives \(n\operatorname{Corr}(C_n,E_n)\to-\sqrt{10}\).

## Verification

Run \(\texttt{python3 check.py}\) with Python 3.9 or later. The self-contained script exhaustively enumerates uniform perfect matchings of \(2n\) ordered endpoints for every \(2\le n\le7\), calculates the component count and intersection-edge count directly, and compares their mean, variance, and covariance with the exact formulas using rational arithmetic. It also evaluates the formulas at selected larger sample sizes as numerical diagnostics. For instance \(\operatorname{Cov}(C_2,E_2)=-2/9\) and \(\operatorname{Cov}(C_7,E_7)=-464/429\). The asymptotic claims are established by the estimates in the proof, not by finite enumeration.

## Relationship to prior work

Scheinerman established the random interval-graph model and its high-probability connectivity and edge-density behavior. The accessible full text of Iliopoulos's *Random Interval Graphs* describes the uniform endpoint-order representation and the mean edge count; the inspected text does not evaluate component–edge covariance. Diaconis, Holmes and Janson discuss dense interval-graph limits and cite the almost-sure connectivity behavior of this model. Earlier work on maximum disjoint interval families and alternative service-system interval graphs addresses different observables or models. The present exact covariance uses the **joint** dependence of a global topological statistic and a global edge statistic, not merely their separate expectations or limiting connectivity. A historical-priority comparison with Scheinerman's original 1988 article remains limited by unavailable full text.

## Limitations

The theorem is about an endpoint-pairing interval graph, not proper interval graphs, Poisson-service interval graphs, circle-graph crossing adjacency, or arbitrary intersection graphs. It gives a covariance and its correlation rate, not the full joint law of components and edges. The finite exact checks do not certify asymptotics; independent mathematical validation has not been carried out. Although the accessible literature and research-record searches did not identify an equivalent published formula, complete historical priority is not established.

## References

1. V. Iliopoulos, *Random Interval Graphs*, master's thesis (2005), public arXiv posting 2015-07-22, [arXiv:1507.06275](https://arxiv.org/abs/1507.06275); full-text HTML: https://ar5iv.labs.arxiv.org/html/1507.06275.
2. E. R. Scheinerman, *Random interval graphs*, Combinatorica **8** (1988), 357–371, https://doi.org/10.1007/BF02189092.
3. S. Boucheron and W. Fernández de la Vega, *On the independence number of random interval graphs*, Combinatorics, Probability and Computing **10** (2001), 385–396, https://doi.org/10.1017/S0963548301004813.
4. P. Diaconis, S. Holmes and S. Janson, *Interval graph limits*, Annals of Combinatorics **17** (2013), 21–34, [arXiv:1102.2841](https://arxiv.org/abs/1102.2841).
