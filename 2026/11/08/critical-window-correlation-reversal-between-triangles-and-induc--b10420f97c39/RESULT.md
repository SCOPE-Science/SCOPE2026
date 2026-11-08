# Critical-window correlation reversal between triangles and induced four-cycles

## Finding
Let \(T_n\) be the number of triangles and \(Q_n\) the number of **induced** (chordless) four-cycles in \(G(n,p)\). Each is counted once per unordered vertex set; a given four-set contributes either zero or one to \(Q_n\). For every integer \(n\ge4\) and \(0<p<1\),
\[
\operatorname{Cov}(T_n,Q_n)=3\binom n3(n-3)p^6(1-p)^2\left[(n-4)-\frac{3n-10}{2}p\right].
\]
Thus for \(n\ge5\) the covariance changes from positive to negative at the unique threshold
\[
p_n^*=\frac{2(n-4)}{3n-10}=\frac23-\frac{4}{3(3n-10)}.
\]
For \(n=4\), the covariance is negative throughout \((0,1)\).

There is a more subtle *correlation* transition. Fix any \(\lambda\in\mathbb R\), and take \(p_n=2/3+\lambda/\sqrt n\), for all sufficiently large \(n\) so that \(0<p_n<1\). Then
\[
\boxed{\lim_{n\to\infty}\operatorname{Corr}_{G(n,p_n)}(T_n,Q_n)
=-\frac{\lambda}{\sqrt{\lambda^2+10/27}}.}
\]
For each fixed \(p\in(0,2/3)\), the correlation tends to \(+1\); for each fixed \(p\in(2/3,1)\), it tends to \(-1\). At \(p=2/3\), the limit is zero, although the finite covariance is strictly negative. This explains the distinction between the sign threshold, displaced from \(2/3\) by order \(1/n\), and the much wider nontrivial correlation window of order \(1/\sqrt n\).

## Assumptions and scope
The random graph has vertex set \([n]\); its \(\binom n2\) edges are independent Bernoulli variables of common parameter \(p\). A triangle is any three-set spanning all three edges, regardless of other vertices. An induced four-cycle is any four-set spanning exactly the four edges of a cycle and lacking its two diagonals. The assertions concern **counts**, covariances and correlations, not a joint central limit theorem. The limiting statement holds pointwise for each fixed real \(\lambda\), with the triangular array of probabilities specified above.

Write \(q=1-p\) and \(h=3p^4q^2\). Define
\[
\begin{aligned}
a&=p^7q^3(2-3p)^2,\\
b&=3p^6q^4(1-3p)^2+9p^7q^5,\\
c&=h(1-h)-6a-4b.
\end{aligned}
\]
Then the following **exact finite variance identities** hold for all \(n\ge4\):
\[
\begin{aligned}
\operatorname{Var}T_n&=\binom n2(n-2)^2p^5q+n\binom{n-1}2p^4q^2+\binom n3p^3q^3,\\
\operatorname{Var}Q_n&=\binom n2\binom{n-2}2^2a+\binom n3(n-3)^2b+\binom n4c.
\end{aligned}
\]
For \(0<p<1\), each variance is positive, so the correlations are well-defined.

## Proof
**1. Covariance by vertex-overlap enumeration.** Expand the covariance into covariances of individual triangle and four-cycle indicators. If the underlying vertex sets have at most one common vertex, their edge sets are disjoint and their indicators independent. With exactly two common vertices, the common edge is required by the triangle. Among the three distinct four-cycle edge patterns on the four-set, two require the common edge and one forbids it. The joint probability is \(2p^6q^2\), whereas the product of marginal probabilities is \(3p^7q^2\); the resulting covariance is \(p^6q^2(2-3p)\). With exactly three common vertices, any induced four-cycle restricts to an open two-edge path on those vertices and hence is incompatible with the triangle. The covariance is \(-3p^7q^2\). For each triangle there are \(3\binom{n-3}2\) four-sets sharing two vertices and \(n-3\) sharing three. Thus
\[
\begin{aligned}
\operatorname{Cov}(T_n,Q_n)
&=\binom n3\left[3\binom{n-3}2p^6q^2(2-3p)-3(n-3)p^7q^2\right]\\
&=3\binom n3(n-3)p^6q^2\left[(n-4)-\frac{3n-10}{2}p\right].
\end{aligned}
\]
The linear factor proves all finite-size signs.

**2. Orthogonal projection and exact variances.** For each graph edge \(e\), let \(\chi_e=(B_e-p)/\sqrt{pq}\), where \(B_e\) is its Bernoulli indicator. Products over distinct edge subsets give an orthonormal basis. On a four-set, an induced-cycle indicator has mean \(h=3p^4q^2\). Its single-edge projection coefficient is \(p^{7/2}q^{3/2}(2-3p)\); its coefficient at either two adjacent edges is \(p^3q^2(1-3p)\); and its coefficient at the three edges of a triangle is \(-3p^{7/2}q^{5/2}\). These follow by summing the three induced-cycle patterns and using independence. Thus the aggregate sums of squared coefficients with support involving precisely two and three vertices are \(a\) and \(b\) respectively, where each three-set has three wedge supports and one triangle support. The sum over four-vertex supports is \(c=h(1-h)-6a-4b\), by Parseval on the four-set.

In the global induced-cycle count, a fixed edge support involving exactly \(s\) vertices is extended to a four-set in \(\binom{n-s}{4-s}\) ways. Orthogonality therefore yields
\[
\operatorname{Var}Q_n=\binom n2\binom{n-2}2^2a+\binom n3(n-3)^2b+\binom n4c.
\]
Similarly, the triangle count has single-edge, adjacent-edge-pair and triangle-edge coefficients \((n-2)p^2\sqrt{pq}\), \(p^2q\) and \((pq)^{3/2}\), respectively. Counting supports gives the displayed variance of \(T_n\).

**3. Critical-window asymptotics.** At \(p_0=2/3\), \(a=0\), \(b=320/59049\), and \(c=784/19683\). Therefore
\[
\operatorname{Var}_{p_0}Q_n
=\binom n3(n-3)^2\frac{320}{59049}+\binom n4\frac{784}{19683},
\]
which has order \(n^5\), rather than the generic order \(n^6\). Substitute \(p_n=2/3+\lambda/\sqrt n\) in the exact formulas. For each fixed \(\lambda\), direct expansion gives
\[
\begin{aligned}
\frac{\operatorname{Var}T_n}{n^4}&\longrightarrow\frac{16}{729},\\
\frac{\operatorname{Var}Q_n}{n^5}&\longrightarrow\frac{16\lambda^2}{6561}+\frac{160}{177147},\\
\frac{\operatorname{Cov}(T_n,Q_n)}{n^{9/2}}&\longrightarrow-\frac{16\lambda}{2187}.
\end{aligned}
\]
The variance limits are strictly positive, giving the claimed correlation limit by division. When \(p\ne2/3\) is held fixed, the first-edge projections of both counts dominate, with relative sign \(\operatorname{sgn}(2-3p)\); equivalently, the leading terms of the exact formulas yield correlation \(+1\) or \(-1\). This completes the proof.

## Verification
Run `python verify.py` in the same directory as this document using Python 3.8 or newer. The verifier independently enumerates all labeled simple graphs through \(n=6\) (all \(2^{15}\) graphs at \(n=6\)), computes exact weighted covariances and variances at three rational probabilities, and compares them with the displayed closed formulas. It also obtains the four-vertex Walsh support variances directly from all 64 graph states, checks critical coefficients and finite sign thresholds at representative sizes, and performs numerical *diagnostics* for the critical correlation profile. It reports 45 successful checks. Finite enumeration and diagnostics are corroboration, **not** a replacement for the proof for arbitrary \(n\).

## Relationship to prior work
Coulson, Gaunt and Reinert (first publicly available September 25, 2015) motivate subgraph-count statistics but address Poisson approximation in regimes distinct from this dense induced-motif crossover. Janson's 1990 functional-limit framework already treats subgraph and induced-subgraph statistics generally. Sah and Sawhney (2020/2022) develop graph-factor decompositions and induced-count local limit theorems away from problematic densities, including the general formulas needed to decompose induced counts. Their work is a closely related method, **not** a claim that those general tools are new here. Sah, Sawhney and Zhu (2024) give joint graph-factor limit theory, also methodologically related. The precise assessed result here is the explicit finite triangle–induced-four-cycle covariance coupled with the *density-varying* \(n^{-1/2}\) correlation profile and constant \(10/27\), which is not stated in the inspected portions of those works. Other exact all-motif coefficient identities could in principle recover it after specialized calculation; independent priority review remains appropriate.

## Limitations
The theorem concerns the independent-edge model \(G(n,p)\), not \(G(n,m)\); it does not assert a central limit theorem or uniform convergence in \(\lambda\). It applies to *induced* four-cycles, not unrestricted four-cycle counts. The critical-window constant is deduced from exact moment identities, not from a limiting-distribution claim. Complete text of Janson (1990) could not be inspected, leaving a literature-priority risk. The result has no independent audit at this stage.

## References
- Coulson, M., Gaunt, R. E., Reinert, G. *Poisson approximation of subgraph counts in stochastic block models and a graphon model*. arXiv:1509.07754v1 (first public September 25, 2015). https://arxiv.org/abs/1509.07754
- Janson, S. *A functional limit theorem for random graphs with applications to subgraph count statistics*. Random Structures & Algorithms 1 (1990), 15–37. https://doi.org/10.1002/rsa.3240010103
- Sah, A., Sawhney, M. *Local limit theorems for subgraph counts*. arXiv:2006.11369 (2020); Journal of the London Mathematical Society 105 (2022), 950–1011. https://doi.org/10.1112/jlms.12523
- Sah, A., Sawhney, M., Zhu, D. G. *Local limit theorem for joint subgraph counts*. arXiv:2412.09535 (2024). https://arxiv.org/abs/2412.09535
