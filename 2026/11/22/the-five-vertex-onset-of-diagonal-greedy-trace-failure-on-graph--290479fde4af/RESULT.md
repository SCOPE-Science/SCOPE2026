# The five-vertex onset of diagonal-greedy trace failure on graph Green kernels

## Finding

**Theorem.** Let \(G\) range over connected, undirected, simple, unweighted graphs with \(2\le |V(G)|\le5\). Write \(L_G\) for the combinatorial graph Laplacian and \(K_G=(I+L_G)^{-1}\). Fix a budget of exactly two distinct vertex columns, and define the residual trace \(E_G(S)\) below. Choose the first vertex by the largest diagonal of \(K_G\); after removing its rank-one Cholesky contribution, choose the second by the largest remaining diagonal, allowing every possible tie-breaking choice.

For every \(G\) with at most four vertices, **every** resulting greedy pair minimizes \(E_G(S)\) over all pairs. For five vertices there is exactly **one** isomorphism class where any greedy pair is suboptimal: the diamond graph (two triangles sharing an edge) with a pendant leaf attached to one of the two shared-edge vertices. All greedy tie choices are suboptimal on this graph, and no other connected graph of order five fails.

Label the exceptional graph by \(V=\{0,1,2,3,4\}\) and \(E=\{01,12,13,14,23,24\}\). The unique optimal pair is \(\{0,2\}\), with \(E_G(\{0,2\})=37/39\). Diagonal greed chooses vertex \(0\) first, followed by either \(3\) or \(4\), giving \(E_G=22/23\). Thus the exact residual-trace regret is \(7/897\), and the greedy-to-optimal ratio is \(858/851\).

There are exactly \(728\) connected labelled graphs on five vertices. Exactly \(60\) labelled instances exhibit the failure, all belonging to this one isomorphism class.

## Assumptions and scope

All graphs are connected, simple, undirected, unweighted, and have at least two vertices. The unit-mass regularization \(I\) is fixed, not tuned after seeing a graph. The object is the strictly positive-definite Green kernel \(K_G=(I+L_G)^{-1}\), whose entries are exact rational numbers. The objective is a *two-column Nyström residual trace* (equivalently, integrated vertexwise conditional variance), not determinant maximization, spectral error, or exact low-rank spectral truncation.

For a two-element vertex set \(S\), put
\[
E_G(S)=\operatorname{tr}\!\left(K_G-K_G[:,S]K_G[S,S]^{-1}K_G[S,:]\right).
\]
The pivoted Cholesky rule chooses a largest residual **diagonal**, not a largest **marginal trace reduction**. A claim that all greedy pivots are optimal is understood to quantify over all tie choices at both stages.

## Proof

**1. Positive definiteness and exact objectives.** The Laplacian satisfies \(z^\mathsf{T}L_Gz=\sum_{\{u,v\}\in E}(z_u-z_v)^2\ge0\); consequently \(I+L_G\) is positive definite and every one- and two-column Schur complement is defined. For a first pivot \(u\), the residual is \(R_u=K-K[:,u]K[u,:]/K_{uu}\). A second pivot \(v\ne u\) reduces its trace by
\[
\Delta_v=\frac{\|R_u[:,v]\|_2^2}{(R_u)_{vv}},
\]
whereas the diagonal-greedy rule chooses \(v\) maximizing only \((R_u)_{vv}\). These two orderings need not agree. For \(S=\{u,v\}\), define \(a=K_{uu}\), \(b=K_{uv}\), \(c=K_{vv}\), and \(d=ac-b^2>0\). Then
\[
E_G(S)=\operatorname{tr}K-\sum_{i=1}^{n}
\frac{cK_{iu}^{2}-2bK_{iu}K_{iv}+aK_{iv}^{2}}{d}.
\]
This exact rational formula avoids floating-point ties or comparisons.

**2. Exhaustive finite proof of the minimality and uniqueness assertions.** The attached `green_kernel_checker.py` enumerates all labelled graphs of each order \(n=2,3,4,5\) by every bit mask over the \(\binom n2\) possible undirected edges. Connectivity is checked by a complete traversal. For every connected graph the code constructs \(I+L_G\), inverts it with exact `fractions.Fraction` Gauss–Jordan arithmetic, computes every two-column trace using the preceding closed formula, enumerates **all** first- and second-stage maximizing ties, and compares every greedy pair with the minimum over all \(\binom n2\) pairs. Every graph configuration and every candidate pair in the domain is visited: the result is not a sampling experiment.

The exact connected-graph counts for \(n=2,3,4,5\) are respectively \(1,4,38,728\). The respective counts having **any** suboptimal greedy tie choice are \(0,0,0,60\); the counts having **all** greedy choices suboptimal are also \(0,0,0,60\). On each of the 60 exceptional labelled instances, the checker tests isomorphism by checking all \(5!\) bijections against the six-edge diamond-with-leaf graph. No exceptional instance fails this comparison. Conversely, its invariance under relabelling and the total count \(5!/2=60\) show the whole isomorphism class is represented.

**3. Explicit exact witness.** In the vertex order above, the exceptional matrix is
\[
K=\begin{pmatrix}
7/12&1/6&1/12&1/12&1/12\\
1/6&1/3&1/6&1/6&1/6\\
1/12&1/6&23/60&11/60&11/60\\
1/12&1/6&11/60&9/20&7/60\\
1/12&1/6&11/60&7/60&9/20
\end{pmatrix}.
\]
Its largest diagonal is uniquely at \(0\). After eliminating \(0\), the residual diagonal in vertex order is \((0,2/7,13/35,46/105,46/105)\), so greedy must next select \(3\) or \(4\), not \(2\). The exact residual traces for pairs \(\{0,2\}\), \(\{0,3\}\), and \(\{0,4\}\) are \(37/39\), \(22/23\), and \(22/23\), respectively. The exhaustive two-element comparison makes \(\{0,2\}\) the unique global minimizer. Exact subtraction yields \(22/23-37/39=7/897>0\), and exact division yields the ratio \(858/851\). This completes the finite theorem.

## Verification

Run `python3 green_kernel_checker.py` using Python 3 and its standard library only. The script exits only if its exact checks pass, including the connected labelled graph counts, all greedy tie outcomes, the classification of 60 failures, and the exact two-column witness trace values. It prints the complete-coverage counts and the rational regret and ratio. All arithmetic used for the decisive tests is rational, with no numerical tolerance. The explicit witness matrix and reduced residual above can independently be checked by direct matrix multiplication and Schur complements.

## Relationship to prior work

Harbrecht, Peters and Schneider's pivoted-Cholesky analysis establishes trace-norm error control for generic positive-semidefinite matrices; its discussion distinguishes the computationally inexpensive largest-diagonal rule from the more expensive direct minimization of the next Schur-complement trace. Liu and Matthies (2015) analyze the same diagonal-pivoted approximation mechanism and its kernel-system applications, not the minimal connected graph order at which it fails to minimize final two-column trace.

Ma, Garnett and Schneider (2012) address *true V-optimality marginal-gain greedy selection* on graph Gaussian random fields. That is a different rule from choosing the largest residual diagonal. In the exceptional graph, after the first pivot the true trace gain favors vertex \(2\) while residual-diagonal greed favors \(3\) or \(4\). The sharp small-graph characterization is not a corollary of submodularity's approximate guarantee. Chen, Epperly, Tropp and Webber (2024) give general poor-case matrices for greedy pivoted Cholesky, but not an all-connected-graphs-on-five-vertices Green-kernel classification.

## Limitations

The theorem concerns the unit regularization \(I+L_G\), exactly two selected columns, unweighted simple connected graphs, and at most five vertices. It does **not** claim the same minimum order for arbitrary positive edge weights or diagonal regularization, nor that all larger graphs fail. The failure is quantitatively small (regret \(7/897\)) but combinatorially sharp and tie-independent. Exhaustiveness is a finite computer-assisted proof backed by complete labelled enumeration and exact arithmetic, not a hand classification of every case. Independent mathematical audit and a comprehensive publication-priority determination remain unperformed.

## References

- Y. Ma, R. Garnett, J. Schneider, *Submodularity in Batch Active Learning and Survey Problems on Gaussian Random Fields* (2012), first arXiv posting 2012-09-17, https://arxiv.org/abs/1209.3694.
- H. Harbrecht, M. Peters, R. Schneider, *On the Low-rank Approximation by the Pivoted Cholesky Decomposition*, *Applied Numerical Mathematics* **62** (2012), 428–440, https://doi.org/10.1016/j.apnum.2011.10.001.
- D. Liu, H. G. Matthies, *Pivoted Cholesky decomposition by Cross Approximation for efficient solution of kernel systems* (2015), first arXiv posting 2015-05-21, https://arxiv.org/abs/1505.06195.
- Y. Chen, E. N. Epperly, J. A. Tropp, R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, *Communications on Pure and Applied Mathematics* (first published 2024), https://doi.org/10.1002/cpa.22234.
