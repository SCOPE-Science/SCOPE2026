# A golden-ratio covariance transition for height and leaves of Bernoulli recursive trees

## Finding
Consider a random rooted tree on the labeled vertices \(1,\ldots,n\). Begin with the edge \(1\! -\! 2\), rooted at \(1\). Independently for each \(k\ge3\), attach vertex \(k\) to \(k-1\) with probability \(p\), or to \(k-2\) with probability \(q=1-p\), where \(0<p<1\). Let \(H_n\) denote its graph-theoretic height (maximum root-to-vertex distance, in edges), and let \(L_n\) count vertices with no children.

**Theorem.** As \(n\to\infty\), the vector process
\[
\left(\frac{H_{\lfloor nt\rfloor}-nt/(1+q)}{\sqrt n},\ \frac{L_{\lfloor nt\rfloor}-ntpq}{\sqrt n}\right)_{0\le t\le1}
\]
converges in distribution in the Skorokhod space \(D([0,1],\mathbb R^2)\) to a centered two-dimensional Brownian motion with covariance per unit time
\[
\Sigma(q)=
\begin{pmatrix}
\dfrac{pq}{(1+q)^3} & \dfrac{pq(q^2+q-1)}{(1+q)^2}\\[6pt]
\dfrac{pq(q^2+q-1)}{(1+q)^2} & pq(1-3pq)
\end{pmatrix}.
\]
For indices below the initial two-vertex tree, set \(H_m=L_m=0\); this convention affects no limit. The covariance matrix is positive definite for every \(0<p<1\), with
\[
\det\Sigma(q)=\frac{p^2q^4(1+q-q^2)}{(1+q)^4}>0.
\]
In particular, \(\operatorname{Cov}(H_n,L_n)/n\) converges to its off-diagonal entry. Its sign changes **exactly once**, at
\[
q_* = \frac{\sqrt5-1}{2},\qquad p_* = \frac{3-\sqrt5}{2}.
\]
It is positive when \(0<p<p_*\), zero to leading order when \(p=p_*\), and negative when \(p_*<p<1\). This is a sign transition in the covariance, not a statement of finite-size independence.

## Assumptions and scope
Every parent choice is independent of all other choices. The initial root has depth zero, and depth is measured in edges. Height and leaves are statistics of the *finite induced growth tree* \(T_n\), not of the limiting infinite tree. Both probabilities \(p,q\) are strictly between zero and one; at the deterministic endpoints, the covariance matrix is degenerate and the stated nondegenerate Gaussian conclusion is not asserted. No random-walk trajectories or collision events are involved.

For all \(n\ge3\), exact means are
\[
\mathbb E H_n=\frac{n-1}{1+q}+\frac{q\{1-(-q)^{n-1}\}}{(1+q)^2},\qquad
\mathbb E L_n=1+q+(n-3)pq.
\]
Consequently the linear centerings in the theorem differ from the exact means by uniformly bounded quantities.

## Proof
Let \(A_k\in\{0,1\}\) indicate attachment of \(k\) to \(k-1\), with \(\Pr(A_k=1)=p\) for \(k\ge3\), and set \(A_2=1\). Write \(D_k\) for the depth of vertex \(k\), with \(D_1=0,D_2=1\), and \(Y_k=D_k-D_{k-1}\). If \(Y_{k-1}\in\{0,1\}\), then
\[
Y_k=\begin{cases}1,&A_k=1,\\1-Y_{k-1},&A_k=0.\end{cases}
\]
Induction gives \(Y_k\in\{0,1\}\) for every \(k\), hence depths are nondecreasing in the arrival label and **\(H_n=D_n=\sum_{k=2}^nY_k\)** exactly.

When a new vertex attaches to the most recent vertex, it replaces that leaf and leaves the leaf count unchanged. When it attaches to the penultimate vertex, it creates an additional leaf precisely if the immediately preceding arrival attached to its immediate predecessor. Thus, with \(C_k=A_{k-1}(1-A_k)\),
\[
L_n=1+\sum_{k=3}^n C_k
\]
exactly. The \(C_k\) for \(k\ge4\) are stationary Bernoulli-word indicators with \(\mathbb EC_k=pq\), and their dependence has range one. The two exact mean identities follow from \(\mathbb EY_k=1-q\mathbb EY_{k-1}\), \(\mathbb EY_2=1\), and the preceding formula for \(L_n\).

Pass to a stationary two-sided version of the process; this is legitimate because the evolution of \(Y_k\) forgets its initial state at its first occurrence of \(A_k=1\), a geometrically bounded coupling time. The binary Markov chain \(Y_k\) has transition matrix (states \(0,1\))
\[
P=\begin{pmatrix}0&1\\q&p\end{pmatrix},
\qquad \Pr(Y_k=1)=\mu=\frac1{1+q},\qquad
\operatorname{Cov}(Y_0,Y_j)=\frac{q}{(1+q)^2}(-q)^{|j|}.
\]
Its covariance series gives the first diagonal entry of \(\Sigma\):
\[
\sum_{j\in\mathbb Z}\operatorname{Cov}(Y_0,Y_j)
=\frac{q}{(1+q)^2}\frac{1-q}{1+q}
=\frac{pq}{(1+q)^3}.
\]
Since neighboring indicators \(C_k\) cannot both equal one and indicators at distance two or more are independent,
\[
\sum_{j\in\mathbb Z}\operatorname{Cov}(C_0,C_j)
=pq(1-pq)-2p^2q^2=pq(1-3pq).
\]

For the cross-covariance, note that \(C_s=1\) forces \(A_{s-1}=1,A_s=0\), hence \(Y_{s-1}=1,Y_s=0\). In stationarity,
\[
\operatorname{Cov}(Y_{s-1},C_s)=pq(1-\mu)=\frac{pq^2}{1+q},\qquad
\operatorname{Cov}(Y_s,C_s)=pq(0-\mu)=-\frac{pq}{1+q}.
\]
For \(t\le s-2\), \(Y_t\) is independent of \(C_s\). For \(t>s\), the binary transition kernel multiplies the covariance by \((-q)^{t-s}\). Therefore the bilateral covariance sum equals
\[
\sum_{t\in\mathbb Z}\operatorname{Cov}(Y_t,C_s)
=\frac{pq^2}{1+q}-\frac{pq}{1+q}\sum_{j=0}^\infty(-q)^j
=\frac{pq(q^2+q-1)}{(1+q)^2}.
\]
All covariance series converge absolutely, and the initial-state correction has bounded total contribution. In particular the finite-sample covariance divided by \(n\) converges to this expression.

For the joint functional limit, use the finite-state Markov chain \(S_k=(Y_k,A_k)\), with possible states \((0,0),(1,0),(1,1)\). For \(0<p,q<1\) this chain is irreducible and aperiodic (there is a self-loop at \((1,1)\)). Both centered increments \(Y_k-\mu\) and \(C_k-pq\) are bounded transition rewards. Solving the finite-state Poisson equation produces a bounded coboundary plus a square-integrable martingale difference for each reward. The vector martingale functional central limit theorem, and the negligible coboundaries and initial transient, establish the joint functional limit, with the asymptotic covariance given by the absolutely convergent covariance sums above. This argument uses standard finite-state Markov-chain and martingale limit theory; it does not assume independence of height and leaf count.

Elementary algebra yields
\[
\det\Sigma(q)=\frac{p^2q^4(1+q-q^2)}{(1+q)^4}>0
\]
for \(0<q<1\). Finally \(q^2+q-1\) is strictly increasing, and its unique root on \((0,1)\) is \((\sqrt5-1)/2\); substituting \(p=1-q\) proves the sharp sign classification.

## Verification
Run the bundled standard-library Python file `verify.py` with `python3 verify.py` in the directory containing the extracted package. It independently constructs each finite tree by its parent array, computes depth and child counts, and compares those statistics against the two exact attachment-sequence recurrences. It then enumerates all attachment strings for sizes \(3\le n\le12\), for five rational choices of \(p\), checking exact means and moments. Independent finite-state moment recursions, including six examples with \(n=3000\), check the three asymptotic covariance entries. The standalone script executed successfully with 288 asserted comparisons. Finite computations do **not** prove a functional limit, an infinite-sample covariance formula, or originality; those conclusions rest on the proof and source comparisons.

## Relationship to prior work
Tang, Wang and Wu [1] introduce precisely this latest-or-penultimate-vertex attachment model and prove its unique infinite end and infinite random-walk collisions. Their Sections 2 and 3 analyze trunk/branch geometry, including a branch-length law; the accessible complete article does not give the bivariate finite-tree height/leaf functional limit, the exact covariance matrix, or the sign-change threshold. The present proof uses elementary attachment choices, not their collision theorem.

The standard Markov-additive invariance principle is an established general tool, rather than a novel ingredient. The substantive specific result is the *jointly computed* finite-tree shape fluctuations, the exact nondegenerate covariance matrix, and its golden-ratio sign transition. Results on uniform random recursive trees [2] and scaled-attachment trees [3] concern different parent-choice distributions and do not give this model's covariance. No claim is made that generic Markov-chain central limit theory itself is new.

## Limitations
Only two-back independent homogeneous attachment, \(0<p<1\), is treated; the theorem does not concern arbitrary recursive-tree models, attachment with memory, or limits with \(p\) varying with \(n\). The vanishing linear covariance at the critical parameter does not imply independence, zero finite-size covariance, or a better convergence rate. The exact finite-size covariance is not simplified here. A general Markov-additive formula might permit another derivation of this special covariance; the full extent of earlier unpublished or differently formulated literature cannot be established solely by search.

## References
[1] J.-s. Tang, F. Wang and X.-Y. Wu, *Infinite collisions of simple random walks on random recursive trees generated by Bernoulli sequences*, arXiv:2607.02916v1 (first public version 2026-07-03), full-text reproduction at https://www.researchgate.net/publication/408520405_Infinite_collisions_of_simple_random_walks_on_random_recursive_trees_generated_by_Bernoulli_sequences.

[2] M. Isaev, A. Southwell and M. Zhukovskii, *Distribution of tree parameters by martingale approach*, Combinatorics, Probability and Computing (2022), https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/distribution-of-tree-parameters-by-martingale-approach/32DFE2BAD7DFC3309F3FAD131FEFC451.

[3] L. Devroye, O. Fawzi and N. Fraiman, *The height of scaled attachment random recursive trees*, DMTCS Proceedings (2010), https://dmtcs.episciences.org/en/articles/2788.
