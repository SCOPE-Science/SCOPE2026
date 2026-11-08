# Planar optimality and radial rigidity for Hilbert-valued Lipschitz variance on weighted spider trees

## Finding
Let \(T\) be a finite weighted spider tree: a central vertex \(o\) and \(m\ge3\) internally vertex-disjoint nonempty path arms with positive edge lengths. Give every vertex strictly positive probability, with total mass one. Write the vertices on arm \(i\) as \(v_{i,1},\ldots,v_{i,n_i}\), their distances from the hub as \(r_{i,j}=d(o,v_{i,j})\), and their probabilities as \(p_{i,j}\). Put
\[
R=\sum_{i,j}p_{i,j}r_{i,j}^{2},\qquad
q_i=\sum_j p_{i,j}r_{i,j},\qquad Q=\sum_iq_i,\qquad
\delta=\max\{0,2\max_iq_i-Q\}.
\]
For every real Hilbert space \(H\) of dimension at least two,
\[
\boxed{\sup_{\operatorname{Lip}(f)\le1}\bigl(\mathbb E\|f(X)\|_H^2-\|\mathbb E f(X)\|_H^2\bigr)=R-\delta^2.}
\]
Here \(X\) has the specified vertex probability law. Every maximizing map, and no other map, is of the form
\[
f(o)=h,\qquad f(v_{i,j})=h+r_{i,j}u_i,
\]
where \(h\in H\), the vectors \(u_i\in H\) have norm one, and \(\|\sum_iq_iu_i\|=\delta\). If \(\delta=0\), this last condition is precisely \(\sum_iq_iu_i=0\). If \(\delta>0\), the unique arm with maximal \(q_i\) points in one direction and every other arm points in the opposite direction.

There is always a maximizing configuration in a two-dimensional subspace. To specify exactly when one dimension suffices, set
\[
\eta=\min_{\varepsilon_i\in\{-1,1\}}\left|\sum_i\varepsilon_iq_i\right|.
\]
The scalar sharp variance is \(R-\eta^2\); a Hilbert-space maximizer admits a one-dimensional affine image if and only if \(\eta=\delta\). Otherwise the least possible affine dimension is exactly two. In particular, when \(\delta=0\), dimension one suffices precisely when the arm moments split into two equal-sum groups.

## Assumptions and scope
The spider is a tree with a designated hub \(o\), and each arm is a finite nonempty simple path from the hub. Vertices other than the hub belong to exactly one arm. Every edge has positive length; the metric is the shortest-path metric. The probability \(p_o\) at the hub and all \(p_{i,j}\) are strictly positive. Functions are maps from the finite vertex set to any real Hilbert space of dimension at least two. A map is one-Lipschitz if every edge displacement has norm at most that edge's length. These edge constraints are equivalent to the global Lipschitz constraint on a tree. No identification of the Hilbert target with a fixed finite-dimensional space is needed.

## Proof
**1. Edge increments and the variance identity.** Translate the map so \(f(o)=0\). Let the \(j\)-th edge of arm \(i\) have length \(a_{i,j}>0\), and write \(z_{i,j}=f(v_{i,j})-f(v_{i,j-1})\), with \(v_{i,0}=o\). Feasibility is exactly \(\|z_{i,j}\|\le a_{i,j}\). Let
\[
P_{i,j}=\sum_{s=j}^{n_i}p_{i,s},\qquad
U_i=\sum_{j=1}^{n_i}P_{i,j}z_{i,j}.
\]
Because \(f(v_{i,s})=\sum_{j\le s}z_{i,j}\), summing the vertex probabilities shows \(\mathbb Ef=\sum_iU_i\), and the centered variance is
\[
\sum_i\sum_{j,k=1}^{n_i}
\bigl(P_{i,\max(j,k)}-P_{i,j}P_{i,k}\bigr)
\langle z_{i,j},z_{i,k}\rangle
-2\sum_{i<l}\langle U_i,U_l\rangle.\tag{1}
\]
This is an algebraic expansion, valid in any real Hilbert space. Every coefficient in the inner sum is strictly positive: for \(j\le k\), it is \(P_{i,k}(1-P_{i,j})>0\), since all masses, including the hub's mass, are positive.

**2. Arm rigidity at every maximizer.** Fix all increments off one arm \(i\), and put \(W=\sum_{l\ne i}U_l\). Up to a constant independent of that arm, (1) equals
\[
F_i(z)=\sum_{j,k}C_{j,k}\langle z_{i,j},z_{i,k}\rangle
-2\left\langle\sum_jP_{i,j}z_{i,j},W\right\rangle,
\qquad C_{j,k}=P_{i,\max(j,k)}-P_{i,j}P_{i,k}>0.
\]
The triangle and Cauchy--Schwarz inequalities imply
\[
F_i(z)\le \sum_{j,k}C_{j,k}a_{i,j}a_{i,k}
+2\|W\|\sum_jP_{i,j}a_{i,j}.\tag{2}
\]
This bound is achieved by setting \(z_{i,j}=a_{i,j}u\) for one unit vector \(u\), chosen opposite to \(W\) when \(W\ne0\) (arbitrary when \(W=0\)). Conversely, equality in (2) forces \(\|z_{i,j}\|=a_{i,j}\) for every \(j\) by the positive diagonal coefficients; positive off-diagonal coefficients force all increments on the arm to have the same unit direction. Thus every global maximizer must be a straight radial map on every arm. A global maximum exists: the finite-dimensional Gram matrices of all edge increments form a compact feasible set, and an explicit maximizing map is constructed below. For any maximizer, replacing one arm by the maximizing choice in (2) cannot improve its value, so equality must hold for that arm. Applying this argument to all arms proves the claimed rigidity.

**3. Reduction to a polygon.** For a radial map \(f(v_{i,j})=r_{i,j}u_i\) with \(\|u_i\|=1\), the first term in its uncentered second moment is exactly \(R\), and its mean is \(\sum_iq_iu_i\). Hence
\[
\operatorname{Var}_H(f)=R-\left\|\sum_iq_iu_i\right\|^2.\tag{3}
\]
The reverse triangle inequality gives \(\|\sum_iq_iu_i\|\ge 2\max_iq_i-Q\), and norm nonnegativity gives \(\ge\delta\). If \(2\max_iq_i>Q\), one dominant arm points along one unit vector and all remaining arms opposite; its resultant has length \(\delta\). Otherwise the positive lengths \(q_i\) form the sides of a closed planar polygon. For completeness, place the longest length last. The norms attainable by the sum of the other vectors vary continuously from their maximum sum down to a minimum no larger than their largest length; the condition \(2\max_iq_i\le Q\) puts the last length in that interval. Rotate the partial resultant to oppose the last vector. Thus a closed polygon exists in a two-dimensional plane. This proves the sharp formula and planar sufficiency.

**4. Complete equality classification and the rank threshold.** Step 2 forces each arm to have a single unit direction at any maximizer, while (3) forces precisely the minimizing vector resultants. For \(\delta>0\), equality in the reverse triangle inequality forces all smaller-arm vectors to be collinear and opposite the unique largest-arm vector. For \(\delta=0\), the equality condition is exactly zero vector sum. A one-dimensional map has \(u_i=\varepsilon_i u\), hence achieves at best \(R-\eta^2\). Since \(\eta\ge\delta\), it attains the Hilbert optimum if and only if \(\eta=\delta\); in the complementary case the planar construction is optimal and no line-valued map is. This completes the proof.

## Verification
The reproducible pure-Python program `check.py` performs exact-rational covariance-expansion checks, finite sign-configuration comparisons, dominance-bound witness tests, and a strict scalar-versus-planar example. It has no nonstandard Python dependencies. Run `python3 check.py` beside this file. Its exact checks cover 270 deterministically generated positive-mass spider instances and 3,240 feasible rational-increment maps; these are finite consistency tests, not substitutes for the argument above.

For the three-leaf unit spider with probability \(1/4\) at every vertex, the formula gives the Hilbert optimum \(3/4\) and scalar optimum \(11/16\). A planar maximizer uses directions spaced by \(120^\circ\), proving the dimension difference occurs already at four vertices.

## Relationship to prior work
Fiedler (1990) establishes an exact tree-variance interpretation of absolute algebraic connectivity for uniformly weighted unweighted trees. Göring, Helmberg and Wappler (2005, Corollary 30) describe the geometry of every optimal unweighted-tree realization and prove the treewidth-based two-dimensional existence bound, so neither the uniform-tree variance relation nor the bare existence of a planar optimum is claimed as new here. Their tree theorem does not state the present arbitrary positive vertex masses and edge lengths, formula in weighted radial moments, or the exact line-versus-plane cutoff. Göring, Helmberg and Reiss (2011 preprint, Table 1) allow positive vertex weights and arbitrary edge lengths in their general spectral/SDP realization framework; their §4 supplies separator structure and dimension bounds but does not state the weighted-spider formula or full equality configuration. Sun, Boyd, Xiao and Diaconis (2006) formulate maximum variance unfolding as an SDP dual of fastest mixing, with the **same edge-distance inequality** but uniform vertex weights; their formulation permits general high-dimensional targets and graphs. Sections 4.1--4.7 give the general optimization and rank conditions, not the exact arbitrary-weighted-spider value, universal arm rigidity, or rank-one-versus-rank-two criterion proved here. Addario-Berry, Janson and McDiarmid (2009) study scalar graph spread under uniform weights, including general principles and random graph bounds, rather than Hilbert-valued variance on weighted spiders. Lee, Naor and Peres (2007) analyze tree-to-Hilbert bi-Lipschitz distortion and Markov convexity, a different extremal objective.

A closely related scalar weighted-spider calculation gives a signed-partition objective for real-valued functions. The current Hilbert-valued theorem is not a specialization of the scalar statement: permitting noncollinear arm directions replaces a discrete signed-partition residual by a polygon residual, and the new equality condition determines the least required target dimension. These comparisons do not rule out equivalent results in unindexed literature.

## Limitations
The result assumes finite path arms, strictly positive vertex probabilities and edge lengths, and Hilbert targets. It does not establish the same formula for trees with additional branching below the hub, for general Banach targets, or for probability laws with negative weights. Its novelty assessment is literature-limited; it has not undergone independent mathematical audit. The finite program does not independently certify all real-parameter instances.

## References
1. M. Fiedler, *Absolute algebraic connectivity of trees*, Linear and Multilinear Algebra 26 (1990), 85--106, DOI: 10.1080/03081089008817967 (1990 print publication; exact public day not established).
2. F. Göring, C. Helmberg, M. Wappler, *Embedded in the Shadow of the Separator*, 2005 preprint dated September 2, 2005, https://optimization-online.org/wp-content/uploads/2005/09/1202.pdf.
3. F. Göring, C. Helmberg, S. Reiss, *On Minimizing the Spectral Width of Graph Laplacians and Associated Graph Realizations*, 2011 preprint, https://www.tu-chemnitz.de/mathematik/preprint/2011/PREPRINT_04.pdf.
4. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681--699, DOI: 10.1137/S0036144504443821, https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf (public online November 2, 2006).
5. L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156 (first submitted February 6, 2009), https://arxiv.org/pdf/0902.1156.
6. J. R. Lee, A. Naor, Y. Peres, *Trees and Markov convexity*, arXiv:0706.0545 (first submitted June 4, 2007), https://arxiv.org/pdf/0706.0545.
