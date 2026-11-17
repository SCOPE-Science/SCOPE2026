# A square-root completion scale for partial-permutation polytopes

## Finding
For each integer \(n\ge2\), let \(\mathcal R_n\subset\mathbb R^{n\times n}\) be the convex hull of all \(n\)-by-\(n\) zero-one matrices with at most one one in each row and column, and let \(\mathcal B_n\subset\mathcal R_n\) be its Birkhoff face (the doubly stochastic matrices). All distances are measured by the ambient Frobenius norm.

Let \(M\) be any partial-permutation vertex with exactly \(k\) ones, let \(q=n-k\), and put \(D=n+q(q+1)=k+q(q+2)\). After independent row and column permutations that put the ones of \(M\) in the first \(k\) diagonal positions, the **unique** Frobenius-nearest \(Y\in\mathcal B_n\), for \(1\le k<n\), is the block matrix
\[
Y=\begin{pmatrix}
(1-q/D)I_k & D^{-1}\mathbf1_{k\times q}\\
D^{-1}\mathbf1_{q\times k} & ((q+2)/D)\mathbf1_{q\times q}
\end{pmatrix}.
\]
For \(k=0\), the projection is \(\mathbf1_{n\times n}/n\); for \(k=n\), it is \(M\) itself. In all cases,
\[
\operatorname{dist}_F(M,\mathcal B_n)^2
=\frac{q(q+2)}{n+q(q+1)}.
\]
The \(n+1\) possible values, indexed by \(q=0,1,\ldots,n\), are strictly increasing. The multiplicity at deficit \(q\) is exactly
\[
N_{n,q}=\binom nq^2(n-q)!=n!\frac{\binom nq}{q!}.
\]
The directed and symmetric Hausdorff distances are both
\[
\sup_{X\in\mathcal R_n}\operatorname{dist}_F(X,\mathcal B_n)
=d_H(\mathcal R_n,\mathcal B_n)=1,
\]
with the **zero matrix as the unique farthest point**.

There is a sharp square-root rank-deficiency scale: if \(q_n/\sqrt n\to c\in[0,\infty)\) for a sequence of partial permutations, then their squared distances tend to \(c^2/(1+c^2)\); if \(q_n/\sqrt n\to\infty\), they tend to one. For a uniformly chosen vertex \(M_n\) of \(\mathcal R_n\), writing \(Q_n=n-\operatorname{rank}(M_n)\),
\[
\frac{Q_n-\sqrt n}{n^{1/4}}\ \xrightarrow{\mathrm d}\ N(0,\tfrac12),
\qquad
n^{1/4}\left(\operatorname{dist}_F(M_n,\mathcal B_n)^2-\tfrac12\right)
\ \xrightarrow{\mathrm d}\ N(0,\tfrac18).
\]
The Gaussian rank-deficiency asymptotic is already available in the published literature; the metric conclusion follows from the exact projection formula and the delta method. In particular, the squared distance of a uniform vertex converges in probability to one half.

## Assumptions and scope
The object \(\mathcal R_n\) is the standard complete-bipartite matching polytope (the doubly substochastic polytope); \(\mathcal B_n\) is its perfect-matching face. The zero matrix is admitted as an empty partial permutation. No matrix normalization or dimension-dependent rescaling is used, and an \(n\)-by-\(n\) matrix is identified isometrically with its vectorization in \(\mathbb R^{n^2}\). The limit law concerns a vertex selected uniformly **among all vertices**, not a vertex selected by a random support direction nor a fixed-rank selection.

## Proof
**Projection.** Simultaneously permute the rows and columns of a rank-\(k\) partial permutation to the diagonal form \(M=\operatorname{diag}(I_k,0_q)\). The convex set \(\mathcal B_n\) is compact and Euclidean projection onto it is unique. Simultaneous permutations of the first \(k\) matched indices, independent row/column permutations of the last \(q\) unmatched indices, and transposition fix both \(M\) and \(\mathcal B_n\). Therefore their unique projection is invariant under these symmetries and has matched diagonal \(a\), matched off-diagonal \(b\), two equal cross-block values \(c\), and a constant unmatched block \(d\). The row and column sums impose
\[
a+(k-1)b+qc=1,\qquad kc+qd=1,\]
with nonnegativity of all four parameters. Substitution into the squared Frobenius objective gives
\[
F=k((k-1)b+qc)^2+k(k-1)b^2+2kqc^2+(1-kc)^2.
\]
For every fixed feasible \(c\ge0\), replacing \(b\) by zero remains feasible (it increases \(a\)) and never increases \(F\); it decreases \(F\) if \(k\ge2\) and \(b>0\). Thus \(b=0\) in the projection. We must minimize
\[
F(c)=kq(q+2)c^2+(1-kc)^2
\]
over \(0\le c\le\min\{1/q,1/k\}\). Its unconstrained minimizer is \(c=1/[k+q(q+2)]=1/D\), which belongs to this interval. Consequently \(a=1-q/D\) and \(d=(q+2)/D\), giving the claimed block matrix and the minimum \(q(q+2)/D\). The limiting cases \(k=0\) and \(k=n\) are direct. Uniqueness follows from the strictly convex squared Frobenius objective.

**Distance shells and extremizer.** Rank \(k=n-q\) partial permutation matrices are enumerated by independently choosing their \(k\) occupied rows, \(k\) occupied columns and a bijection, giving \(\binom nk^2k!\). To see that the squared-distance expression strictly increases with \(q\), rewrite it as \(1-(n-q)/(n+q(q+1))\); the subtracted positive fraction strictly decreases as \(q\) increases from zero to \(n\). The squared distance to any closed convex subset is convex as a function of the ambient point. Every point of \(\mathcal R_n\) is a convex combination of its partial-permutation vertices; the unique vertex with squared distance one is zero and every other vertex has squared distance below one. Strict convex-combination comparison then excludes every nonzero point of \(\mathcal R_n\) from attaining squared distance one. The opposite directed Hausdorff term vanishes because \(\mathcal B_n\subset\mathcal R_n\).

**Asymptotic deficiency.** Under uniform vertex sampling, \(\Pr(Q_n=q)\) is proportional to \(w_n(q)=\binom nq/q!\). Its consecutive ratio is exactly
\[
\frac{w_n(q+1)}{w_n(q)}=\frac{n-q}{(q+1)^2},
\]
so the weights are strictly log-concave, concentrate on \(q\asymp\sqrt n\), and have exponentially controlled tails away from the saddle. Uniformly for bounded real \(z\) and integers \(q=\sqrt n+z n^{1/4}+O(1)\), Stirling's formula and the finite product defining \(\binom nq\) give
\[
\log w_n(q)=C_n-z^2+o(1),
\]
where \(C_n\) does not depend on \(z\). Strict log-concavity and the displayed ratio control the complement of growing compact windows in the \(z\) coordinate. Riemann-sum normalization gives the limit density \(e^{-z^2}/\sqrt\pi\), namely \(N(0,1/2)\). Writing \(f_n(q)=q(q+2)/(n+q(q+1))\), Taylor expansion at \(q=\sqrt n\) yields \(f_n(\sqrt n)=1/2+O(n^{-1/2})\) and \(f_n'(\sqrt n)=1/(2\sqrt n)+O(n^{-1})\); the derivative remains uniform on \(O(n^{1/4})\)-windows. Hence the delta method gives the metric fluctuation \(N(0,1/8)\). The deterministic square-root transition follows directly by dividing the formula for \(f_n\) by \(n\).

## Verification
The accompanying script `verify_rook_completion.py` independently checks exact rational feasibility, squared distances, and the projection variational inequality against **every** permutation-matrix vertex for all \(n=2,\ldots,7\) and every possible rank. This gives 33 exact input configurations and 46,230 permutation inequalities. An additional SciPy quadratic-programming solver independently verifies 18 cases through dimension five. Log-weight calculations illustrate concentration and the predicted asymptotic variances through dimension one million. These finite checks corroborate, but do not replace, the exact and asymptotic arguments above.

## Relationship to prior work
Heuer and Striker (first public version 2020-12-17) give the partial-permutation polytope and its vertex enumeration, but not a Frobenius distance-to-perfect-matching-face spectrum. Hu, Im, Li and Wolkowicz (2021) study general numerical nearest-doubly-stochastic projection, rather than this explicit family and its all-rank geometry. Earlier minimal doubly-substochastic completions (Cao, Koyuncu, Parmer) enlarge the matrix and optimize *completion size*, not same-size Frobenius error. Prior work on Gaussian rank deficiencies of uniform partial bijections supplies the rank central limit theorem; it is not claimed as new here. Other published metric studies of partial-assignment inballs and vertex covariance do not imply the projection formula. The new geometric assertion is the **closed-form nearest-point map, complete metric shell distribution, and sharp phase relation between matching deficiency and Euclidean completion error**, not the existence of algorithms for general nearest-doubly-stochastic projection.

## Limitations
This exact projection applies to partial-permutation **vertices**, not arbitrary doubly substochastic real matrices. Its unique farthest-point statement does apply to the full partial-permutation polytope. It uses the Frobenius metric and the square complete-bipartite case, without claims for weighted entry norms, forbidden assignment edges, or rectangular perfect-matchings. The Gaussian rank fluctuation is a known probabilistic input; the geometric transformation is the assessed result. An equivalent rank-stratified projection in older matrix-nearness literature could affect historical priority; independent audit has not been performed.

## References
1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, first posted 2020-12-17; especially Sections 2–3. https://arxiv.org/abs/2012.09901
2. H. Hu, H. Im, X. Li and H. Wolkowicz, *A Semismooth Newton-Type Method for the Nearest Doubly Stochastic Matrix Problem*, arXiv:2107.09631, first posted 2021-07-20. https://arxiv.org/pdf/2107.09631
3. L. Cao, S. Koyuncu and T. Parmer, *A minimal completion of doubly substochastic matrix*, Linear and Multilinear Algebra 64 (2016), 2313–2334. DOI:10.1080/03081087.2016.1155531.
4. *Gaussian deficiencies and Poisson overlap corrections in random rook-monoid products*, published mathematical record (2026-11-02), identifier `2026/11/2/SCOPE-gaussian-deficiencies-and-poisson-overlap-corrections-in-random--c5a891e46186`. Used to acknowledge known rank Gaussian asymptotics; the present proof also gives a direct saddle-point argument.
