# Convex spectral filters on heterogeneous clique windmills have an exact apex-positivity criterion

## Finding
Let \(r\ge1\), let \(p_1,\ldots,p_r\) be arbitrary positive integers, put \(N=\sum_{i=1}^{r}p_i\) and \(n=N+1\), and let \(G=K_1\vee(K_{p_1}\sqcup\cdots\sqcup K_{p_r})\). Give every edge unit weight, let \(L\) be its combinatorial Laplacian, and let \(f:[0,\infty)\to[0,\infty)\) be **convex**, with \(f(0)=1\). For every \(h\ge0\), the symmetric spectral matrix function \(f(hL)\) satisfies the exact equivalence

\[
 f(hL)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad f(nh)\le1.
\]

Thus every such filter has only the central-vertex transition as a possible *necessary* sign obstruction; all entries between distinct noncentral cliques remain nonnegative at every step, and entries within one noncentral clique are at least as large as an apex-to-nonapex entry. The condition includes the cases of a complete graph, a star, friendship graphs, windmills with unequal clique sizes, and their mixtures. No assertion is made for an arbitrary cone over a non-cluster graph.

**Even Taylor consequence.** For any even integer \(p\ge2\), define
\[
 F_p(x)=\sum_{j=0}^{p}\frac{(-x)^j}{j!},
\]
and let \(\beta_p>0\) be the unique positive root of \(F_p(\beta_p)=1\). The completed \(p\)-th order Taylor / linear Runge--Kutta heat step is entrywise nonnegative exactly for \(0\le h\le\beta_p/n\). For \(p=4\), \(\beta_4\approx2.785293563405\); positivity never returns after the sharp threshold.

## Assumptions and scope
The graph is finite, simple, undirected, unweighted, with one distinguished apex joined to every vertex of a disjoint union of complete graphs. Clique sizes need not coincide; the number of cliques can be one. The matrix function is defined by real symmetric spectral calculus. The convex filter is nonnegative on the spectrum, not just at \(0\) and \(nh\). The result concerns the completed endpoint map and coordinatewise nonnegativity; no property of intermediate numerical stages, nonlinear dynamics, weighted edges, or graphs lacking the stated clique-block structure follows.

## Proof
Write \(a=f(h)\), \(b_i=f((p_i+1)h)\), and \(c=f(nh)\). The Laplacian has orthogonal spectral subspaces: the all-ones space, with eigenvalue \(0\); the apex-versus-base direction, with eigenvalue \(n\); the \(r-1\)-dimensional subspace of vectors constant on each base clique and summing to zero over all base vertices, with eigenvalue \(1\); and each base-clique zero-sum subspace, with eigenvalue \(p_i+1\). Empty zero-sum subspaces for singleton cliques cause no difficulty.

Let \(E\) be an apex--base entry, \(D\) an entry between vertices of different base cliques, and \(W_i\) an entry between distinct vertices of base clique \(i\). Orthogonal-projector multiplication gives, when the indicated entry class exists,
\[
 E=\frac{1-c}{n},\qquad
 D=\frac{N+c-na}{Nn},\qquad
 W_i=D+\frac{a-b_i}{p_i}.
\]
The diagonal entries of \(f(hL)\) are strictly positive: every spectral coefficient is nonnegative, and the all-ones projector contributes \(1/n\) to each diagonal.

Convexity at \(h=\frac1n(nh)+\frac{n-1}{n}0\) yields \(na\le c+N\); hence \(D\ge0\), with strict inequality for strictly convex \(f\) and \(h>0\). For \(1\le t\le N\), put
\[
 q_t=\frac{f(h)-f((t+1)h)}{t}.
\]
Secant slopes of a convex function are nondecreasing as their right endpoint increases, so \(q_t\) is nonincreasing in \(t\). In particular \(q_{p_i}\ge q_N\). Direct substitution gives \(D+q_N=E\), so \(W_i=D+q_{p_i}\ge E\). Thus if \(c\le1\), all off-diagonal entries are nonnegative; if \(c>1\), every apex--base entry is negative. This proves both implications, including the endpoints \(h=0\) and equality \(c=1\).

For even \(p\ge2\), Taylor's remainder shows \(F_p(x)>e^{-x}>0\) for \(x>0\), and \(F_p(0)=1\). Moreover \(F_p''(x)=F_{p-2}(x)>0\) for \(x\ge0\). Since \(F_p'(0)=-1\) and \(F_p(x)\to\infty\) as \(x\to\infty\), strict convexity gives exactly one positive crossing of the level \(1\) and gives \(F_p(x)\le1\) exactly on \([0,\beta_p]\). Applying the general equivalence proves the stated sharp Taylor thresholds and permanent loss beyond the crossing.

## Verification
A self-contained Python standard-library exact-rational checker, `verify.py`, builds each graph Laplacian and its degree-\(p\) matrix polynomial by repeated matrix multiplication; independently it evaluates all projector-derived entry formulas. It checks every ordered positive composition with \(N\le7\), even degrees \(p=2,4,6,8\), and normalized test parameters \(nh\in\{1/2,1,2,5/2,3,4,6\}\). All 3,556 full-matrix comparisons, 182,728 entry identities, and 3,556 exact threshold implications passed. The checker validates finite instances; the theorem for arbitrary sizes, filters, and steps is proved above, not inferred from these tests.

To reproduce: `python3 verify.py` in the directory containing this document and the included code. No third-party packages are required.

## Relationship to prior work
Gottlieb, Shu and Tadmor (2001) establish linear strong-stability-preserving Taylor/Runge--Kutta constructions and general sufficient CFL principles, not this clique-block, nonnegative-convex-filter equivalence. Horváth (2005) treats general Runge--Kutta positivity-step restrictions and invariant positive sets rather than this exact spectral graph subclass. Horváth, Song and Terlaky (2014/2015) develop polynomial-root step thresholds on polyhedra; the accessible abstract does not itself establish the present apex-only formula. Kooij (2019) studies Laplacian spectra and other metrics of generalized windmills; the spectral decompositions are antecedent context, while the claimed entrywise positivity and arbitrary-convex-filter criterion is different. Previous graph-specific Taylor positivity formulas for complete multipartite, strongly regular, and bipartite graphs cover degenerate overlaps but do not imply the general heterogeneous windmill theorem on graphs with multiple nontrivial clique blades.

## Limitations
The exact classification requires the clique-block structure, nonnegative convex \(f\), and \(f(0)=1\). It need not extend to arbitrary cones or to odd Taylor orders at large timesteps. Only completed matrix maps are addressed. The claim has not undergone independent mathematical audit; publication priority beyond the inspected and accessible sources has not been certified. A specialist 2014 full manuscript could not be fully retrieved and remains a residual comparison risk.

## References
1. S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89--112, DOI: 10.1137/S003614450036757X. Earliest verified online publication: 2001-02-02. Full text: https://www.math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf.
2. Z. Horváth, *On the Positivity Step Size Threshold of Runge--Kutta Methods*, Applied Numerical Mathematics 53 (2005), 341--356, DOI: 10.1016/j.apnum.2004.08.026.
3. Z. Horváth, Y. Song and T. Terlaky, *Steplength Thresholds for Invariance Preserving of Discretization Methods of Dynamical Systems on a Polyhedron*, arXiv:1406.6755 (first public 2014-06-26), DOI: 10.3934/dcds.2015.35.2997.
4. R. Kooij, *On Generalized Windmill Graphs*, Linear Algebra and its Applications 565 (2019), 25--46, DOI: 10.1016/j.laa.2018.11.025.
