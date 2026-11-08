# A square-root migration law for optimal noise-free leaders on balanced split networks

## Finding
Let \(G_n=K_n\vee\overline{K_n}\), the simple unweighted graph consisting of an \(n\)-vertex clique joined to an \(n\)-vertex independent set. For \(n\ge2\) and an integer leader budget \(1\le k<n\), each noise-free leader set \(S\) of size \(k\) leaves a grounded Laplacian \(L_{FF}\), where \(F=V(G_n)\setminus S\). Minimize the total follower variance proxy \(\mathcal C_n(S)=\operatorname{tr}(L_{FF}^{-1})\), equivalent (up to a constant factor) to noisy consensus coherence under isotropic unit-intensity follower disturbances.

Write \(a=|S\cap V(K_n)|\) for the number of clique leaders. For every feasible \(a\in\{0,\ldots,k\}\), all sets with that count have the same objective, exactly
\[
C_{n,k}(a)=\frac{n-a-1}{2n}+\frac{n-k+a-1}{n}+\frac{2n+a}{nk+a(n-k+a)}.
\]
Consequently the optimal count and value are obtained by comparing only \(k+1\) explicitly given rational numbers, rather than searching \(\binom{2n}{k}\) sets.

There is a sharp *square-root budget migration*. Fix \(c>0\), let \(k_n=\lfloor c\sqrt n\rfloor\), and choose any optimal count \(a_n\) for all sufficiently large \(n\). Then
\[
\lim_{n\to\infty}\frac{a_n}{\sqrt n}
=\begin{cases}
c,&0<c\le1,\\
2-c,&1<c<2,\\
0,&c\ge2.
\end{cases}
\]
Moreover, for each fixed \(c\in(0,1)\), **every** optimal set eventually consists solely of clique leaders (\(a_n=k_n\)). For each fixed \(c>2\), **every** optimal set eventually consists solely of independent-set leaders (\(a_n=0\)). If \(1<c<2\), every optimal count satisfies \(a_n=(2-c)\sqrt n+o(\sqrt n)\), so neither extreme is asymptotically optimal.

A finite strict non-nesting witness occurs at \(n=20\): the unique optimal **count** is \(a=4\) for \(k=4\), with objective \(8/5\), but \(a=0\) for \(k=7\), with objective \(381/280\). Hence no optimal four-leader set is a subset of any optimal seven-leader set on this graph.

## Assumptions and scope
All graph edges have conductance one. The system has exactly \(2n\) vertices, with the two parts both of size \(n\). Leaders are perfectly pinned (noise free); follower noise is independent, identically scaled, and the linear drift is the negative grounded combinatorial Laplacian. The proxy \(\mathcal C_n\) differs from total stationary follower variance by the fixed factor \(1/2\) under unit covariance; optimizing either is identical. The finite formula and exact comparison algorithm hold for all integers \(n\ge2\) and \(1\le k<n\). The asymptotic statements require fixed \(c>0\) and sufficiently large \(n\) so \(1\le k_n<n\). No claims are made for different graph weights, noisy leaders, or leader budgets growing linearly in \(n\).

## Proof
**1. Reduction by symmetry.** The automorphism group permutes clique vertices freely and independently permutes independent-set vertices. Any two \(k\)-element leader sets with the same clique count \(a\) are automorphic. Thus the optimum is the minimum over \(0\le a\le k\). Put \(u=n-a\) and \(v=n-k+a\); both are positive because \(k<n\).

**2. Exact inverse trace.** With clique followers first and independent-set followers second,
\[
L_{FF}=\begin{pmatrix}2nI_u-J_u&-J_{u,v}\\-J_{v,u}&nI_v\end{pmatrix}.
\]
The \((u-1)\)-dimensional clique contrast subspace has eigenvalue \(2n\), and the \((v-1)\)-dimensional independent contrast subspace has eigenvalue \(n\). The orthonormal vectors constant on each follower part span the remaining two-dimensional invariant space, on which \(L_{FF}\) has matrix
\[
B=\begin{pmatrix}n+a&-\sqrt{uv}\\-\sqrt{uv}&n\end{pmatrix}.
\]
Its determinant and trace are respectively
\[
D=nk+a(n-k+a)>0,\qquad\operatorname{tr}B=2n+a.
\]
The determinant is positive because grounding at any nonempty leader set in this connected graph yields a positive-definite grounded Laplacian. For a positive-definite two-by-two matrix, \(\operatorname{tr}(B^{-1})=\operatorname{tr}(B)/\det B\). Adding the contrast contributions gives the displayed formula for \(C_{n,k}(a)\). Exact enumeration of its \(k+1\) rational values is therefore globally valid.

**3. Scaled limit and sharp thresholds.** Algebra separates the terms independent of \(a\):
\[
C_{n,k}(a)=\frac32-\frac{k}{n}-\frac{3}{2n}
+\frac{a}{2n}+\frac{2n+a}{n(k+a)+a(a-k)}.
\]
For \(k=k_n\), set \(s=a/\sqrt n\). On the compact domains \(0\le s\le k_n/\sqrt n\), the rescaled \(a\)-dependent expression converges uniformly to
\[
\sqrt n\left(C_{n,k_n}(a)-\frac32+\frac{k_n}{n}+\frac{3}{2n}\right)
\longrightarrow f_c(s)=\frac s2+\frac2{c+s},\qquad 0\le s\le c.
\]
Indeed \(k_n/\sqrt n\to c>0\), \(a(a-k_n)=O(n)\) uniformly, while \(n(k_n+a)=\Theta(n^{3/2})\) uniformly; the denominator stays bounded away from zero after scaling by \(n^{3/2}\). The continuous function \(f_c\) is strictly convex, with
\[
f_c'(s)=\frac12-\frac{2}{(c+s)^2},\qquad f_c''(s)=\frac4{(c+s)^3}>0.
\]
Its unique minimizer on \([0,c]\) is the projection of \(2-c\) onto that interval, giving the three regimes. Uniform convergence, mesh size \(1/\sqrt n\to0\), and strict uniqueness imply convergence of **every** discrete optimum count.

**4. Eventual exact endpoint regimes.** Treat \(a\) temporarily as real in \([0,k_n]\). Direct differentiation gives
\[
\frac{\partial C_{n,k_n}}{\partial a}
=\frac1{2n}-\frac{a^2+4an-3k_nn+2n^2}
{\bigl(n(k_n+a)+a(a-k_n)\bigr)^2}.
\]
Uniformly for \(0\le a\le k_n\), writing \(s=a/\sqrt n\),
\[
n\frac{\partial C_{n,k_n}}{\partial a}
=\frac12-\frac2{(c+s)^2}+o(1).
\]
For \(c<1\), the limiting derivative is strictly negative throughout \([0,c]\), so for large \(n\) the rational objective is strictly decreasing on the full feasible interval and only \(a=k_n\) can minimize. For \(c>2\), it is strictly positive and only \(a=0\) minimizes. For \(1<c<2\), the strict interior minimizer in step 3 forces a mixed allocation. The endpoint cases \(c=1,2\) are covered by the uniform argmin limit, without claiming exact finite endpoint allocations there.

**5. Finite non-nesting.** Substitution into the exact rational formula at \(n=20\) shows \(C_{20,4}(4)=8/5\) and \(C_{20,4}(a)>8/5\) for each \(0\le a<4\). Similarly \(C_{20,7}(0)=381/280\) and \(C_{20,7}(a)>381/280\) for each \(1\le a\le7\). These are exhaustive comparisons over the possible counts, not over guessed configurations. The two classes of optimal leader sets have disjoint permitted vertex parts; inclusion is impossible.

## Verification
Run `python3 verify.py` using only the Python standard library. It independently builds the \(2n\)-vertex graph, deletes designated leader rows and columns, performs exact rational Gauss-Jordan inversion, and compares trace values to the formula for every leader set with \(2\le n\le5\), \(1\le k<n\). The recorded run passed 502 independent exact-rational inversions and checked the two strict \(n=20\) optimizer witnesses. This finite replay corroborates the matrix algebra and numerical examples; the general large-\(n\) theorem relies on the analytic argument above.

## Relationship to prior work
Fitch and Leonard [1] develop general joint-centrality formulas for leader choice and discuss non-nesting; the inspected results concern general graph invariants and explicit path/cycle cases, not a balanced split-network exact count formula or a square-root core-to-periphery transition. Clark, Bushnell and Poovendran [2] give a supermodular approximation framework rather than these exact optimizers. Patterson, McGlohon and Dyagilev [3] give polynomial exact leader selection on weighted paths and rings; these are distinct topologies. Patterson, Yi and Zhang [4] give resistance-based expressions and exact solutions on paths, cycles and certain trees, but not the present complete split-graph allocation. The new contribution is the **evaluated** optimal allocation and the asymptotic thresholds, not the previously known general identity connecting coherence to grounded Laplacians.

## Limitations
The graph is a homogeneous balanced split graph, with unweighted edges and exactly noise-free leaders. The thresholds concern the square-root leader-budget scale; they do not identify all finite-budget phase boundaries or apply automatically to arbitrary split graphs. The source comparison establishes no mathematical independence or exhaustive publication priority; unpublished or differently named graph-specific analyses could cover some statements. The exact finite witness and analytical limit theorem have not undergone external validation.

## References
1. K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first publicly posted 2014-07-07), https://arxiv.org/abs/1407.1569.
2. A. Clark, L. Bushnell and R. Poovendran, *A Supermodular Optimization Framework for Leader Selection under Link Noise in Linear Multi-Agent Systems*, arXiv:1208.0946 (2012), https://arxiv.org/abs/1208.0946.
3. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (2014), https://arxiv.org/abs/1412.6595.
4. S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (2017), https://arxiv.org/abs/1708.06873.
