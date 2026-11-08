# Exact vertex-inertia spectrum and square-root anisotropy of complete-graph matching polytopes

## Finding

Let \(n\ge4\) be an integer and \(P_n\subset\mathbb R^{\binom n2}\) be the convex hull of the edge-indicator vectors of **all** matchings of the complete graph \(K_n\), including the empty matching. Choose a vertex \(X\) uniformly from the distinct vertices and let \(\Sigma_n=\operatorname{Cov}(X)\), in the ambient standard Euclidean edge-coordinate metric. Write
\[
 T_0=T_1=1,\qquad T_j=T_{j-1}+(j-1)T_{j-2}\quad(j\ge2),
 \qquad a_n=\frac{T_{n-2}}{T_n},\quad b_n=\frac{T_{n-4}}{T_n}.
\]
Then \(T_n\) counts all matchings and the **entire covariance spectrum**, in strictly increasing order, is
\[
\boxed{\begin{aligned}
\lambda_{\mathrm{size}}&=a_n+\binom{n-2}{2}b_n-\binom n2 a_n^2,
&&\text{multiplicity }1,\\
\lambda_{\mathrm{star}}&=a_n-(n-3)b_n,
&&\text{multiplicity }n-1,\\
\lambda_{\mathrm{cycle}}&=a_n+b_n,
&&\text{multiplicity }\frac{n(n-3)}2.
\end{aligned}}
\]
These eigenvalues obey \(0<\lambda_{\mathrm{size}}<\lambda_{\mathrm{star}}<\lambda_{\mathrm{cycle}}\) for every \(n\ge4\). In particular, the unique direction of minimum vertex variance is the all-ones edge vector. The maximum-variance eigenspace is the kernel of the unsigned vertex-edge incidence matrix: edge weights whose sum at each graph vertex is zero. The intermediate eigenspace consists of edge weights of the form \(u_{ij}=z_i+z_j\), where \(\sum_i z_i=0\).

The spectral condition number satisfies the sharp asymptotic
\[
\boxed{\frac{\lambda_{\mathrm{cycle}}}{\lambda_{\mathrm{size}}}=2\sqrt n+O(1)\qquad(n\to\infty).}
\]

## Assumptions and scope

Every matching incidence vector is an extreme point of \(P_n\): if a binary vector is a nontrivial convex combination of other binary vectors, coordinatewise extremality forces those vectors to coincide. Therefore vertex-uniform means uniformly over matchings, not uniformly over the volume of \(P_n\) or over fixed-size or perfect matchings. The empty matching and all one-edge matchings make \(P_n\) full-dimensional. All eigenvalues and multiplicities refer to this full-dimensional ambient metric. The assertion is for integer \(n\ge4\); no singular fixed-cardinality slice is included.

## Proof

**1. Matching moments.** By choosing whether vertex \(n\) is unmatched or matched with any of its \(n-1\) neighbors, the number of matchings satisfies the displayed recurrence. Fix an edge \(e\). Exactly \(T_{n-2}\) matchings contain \(e\). If \(e,f\) are distinct and incident, no matching contains both. If they are disjoint, exactly \(T_{n-4}\) matchings contain both. Hence the covariance entries are \(a_n-a_n^2\) on the diagonal, \(-a_n^2\) for distinct incident edges, and \(b_n-a_n^2\) for disjoint edges.

**2. Orthogonal decomposition.** On the \(m=\binom n2\) edges let \(A\) be the adjacency matrix of the line graph of \(K_n\), and let \(J\) be the all-ones matrix. Then
\[
\Sigma_n=(a_n-a_n^2)I-a_n^2 A+(b_n-a_n^2)(J-I-A).
\]
Let \(U_0\) be the line of constant edge weights. Let \(U_1\) be the \((n-1)\)-space of weights \(u_{ij}=z_i+z_j\) with \(\sum_i z_i=0\). Let \(U_2\) be the edge weights satisfying \(\sum_{j\ne i}u_{ij}=0\) for every vertex \(i\). The unsigned incidence matrix has rank \(n\) for \(n\ge3\), so these are pairwise orthogonal, sum to all edge space, and \(\dim U_2=m-n=n(n-3)/2\). The eigenvalues of \(A\) on \(U_0,U_1,U_2\) are respectively \(2(n-2),n-4,-2\). This follows immediately by summing edge weights incident with either endpoint. Substitution yields the three displayed formulas and identifies their complete eigenspaces.

**3. Strict ordering.** Put \(p_j=T_{j-1}/T_j\) for \(j\ge1\). The recurrence implies
\[
a_n=\frac{1-p_n}{n-1},\qquad
b_n=\frac{(1-p_n)(1-p_{n-2})}{(n-1)(n-3)},\qquad
\lambda_{\mathrm{star}}=\frac{(1-p_n)p_{n-2}}{n-1}.
\]
In the random involution corresponding to the matching, let \(F\) be its number of fixed points, or unmatched vertices. Counting one or two specified fixed points gives \(\mathbb EF=np_n\) and \(\mathbb E[F(F-1)]=n(n-1)a_n=n(1-p_n)\), hence \(\mathbb E F^2=n\). Since the matching size is \((n-F)/2\) and the constant-edge mode is its normalized sum,
\[
\lambda_{\mathrm{size}}=\frac{1-np_n^2}{2(n-1)},\qquad
\lambda_{\mathrm{star}}-\lambda_{\mathrm{size}}
=\frac{n(1-p_n)(p_{n-2}-p_n)}{2(n-1)}.
\]
We show \(p_{n-2}>p_n\) for \(n\ge4\). Define \(r_j=1/p_j=T_j/T_{j-1}\). By induction using \(r_j=1+(j-1)/r_{j-1}\),
\[
\sqrt j<r_j<1+\sqrt j\qquad (j\ge2).
\]
Indeed, the upper estimate follows from \(r_{j-1}\ge\sqrt{j-1}\); for the lower estimate use \(r_{j-1}<1+\sqrt{j-1}\) and \(\sqrt j-\sqrt{j-1}<1/(1+\sqrt{j-1})\). Two recurrence steps yield, for \(x=p_{n-2}\),
\[
p_n=\frac{1+(n-2)x}{n+(n-2)x},\qquad
x-p_n=\frac{(n-2)x^2+2x-1}{n+(n-2)x}.
\]
Since \(x>1/(1+\sqrt{n-2})>1/(1+\sqrt{n-1})\), the numerator is strictly positive. This proves the lower inequality. Finally, \(\lambda_{\mathrm{cycle}}-\lambda_{\mathrm{star}}=(n-2)b_n>0\); strict positivity of the lowest eigenvalue follows because \(F\) is nonconstant (the empty and single-edge matchings both occur).

**4. Sharp growth of anisotropy.** We give elementary error control for the required recurrence asymptotics. Define \(R_n=T_n/T_{n-1}\) and \(e_n=R_n-\sqrt n-1/2\). The two-step recurrence is
\[
R_n=H_n(R_{n-2}),\qquad H_n(x)=\frac{nx+n-2}{x+n-2}.
\]
For \(n\ge16\) and \(x\ge\sqrt{n-2}\),
\[
0<H_n'(x)=\frac{(n-1)(n-2)}{(x+n-2)^2}\le1-\frac1{\sqrt n}.
\]
For \(t=\sqrt{n-2}\), direct substitution and rationalizing the difference of square roots show
\[
\left|H_n(t+1/2)-(\sqrt n+1/2)\right|
=\left|\frac{t+3/4}{t^2+t+1/2}-\frac2{t+\sqrt{t^2+2}}\right|
\le \frac{1}{t^2}\le\frac3n.
\]
Indeed, compare both fractions with \(1/t\): their combined deviations are at most \(1/(4t^2)+1/t^3\le1/t^2\) for \(t\ge\sqrt{14}\). The derivative bound follows from \(H_n'(x)\le(t^2+1)/(t+1)^2\) and \((1+1/t)^2<2\). By the mean-value theorem,
\[
|e_n|\le\left(1-\frac1{\sqrt n}\right)|e_{n-2}|+\frac3n.
\]
The rough bound \(0<R_j-\sqrt j<1\) handles \(j=14,15\). Induction gives \(|e_n|\le10/\sqrt n\), using \(\sqrt{n/(n-2)}\le1+2/n\) for \(n\ge16\). Consequently
\[
p_n=\frac1{\sqrt n}-\frac1{2n}+O(n^{-3/2}),\qquad
\lambda_{\mathrm{size}}=\frac1{2n^{3/2}}+O(n^{-2}),
\]
whereas \(\lambda_{\mathrm{star}}=n^{-3/2}+O(n^{-2})\) and \(\lambda_{\mathrm{cycle}}=n^{-1}+O(n^{-3/2})\). Dividing the largest by the smallest proves \(2\sqrt n+O(1)\).

## Verification

The included standalone `verify.py` performs finite, exact-rational enumeration of all matching vertices for sizes \(4\) through \(9\), independently checks every covariance matrix entry and representative vectors from all three eigenspaces, and tests the strict spectral ordering through size \(150\). The checked finite sizes total \(3{,}728\) matching vertices and \(285\) nonconstant eigenspace test vectors. It prints `COMPLETE_MATCHING_COVARIANCE_CHECKS_PASSED` on success. This is a finite corroboration; the four proof steps above establish the infinite statement.

## Relationship to prior work

Matching polytopes and their one-skeleta are standard objects. Abreu, Costa, Nascimento and Patuzzi (2019) characterize minimum skeleton degree and regularity, rather than vertex-uniform second moments. Torres (2023) treats normality of fixed-cardinality matching polytopes of bipartite graphs, a different family and invariant. Other established matching-polytope results concern facets, radii and John ellipsoids; their cited statements do not provide this three-eigenspace vertex-uniform covariance classification. Quitmann (2023) establishes decay of monomer–dimer correlations on lattice regions and does not calculate the present finite-complete-graph covariance spectrum. The edge-incidence representation and complete-graph symmetry used in this proof are standard; only the exact combination of variance eigenvalues, strict all-size ordering and anisotropy asymptotic is asserted as the present finding.

## Limitations

The law is uniform on polytope vertices, not on interior volume; matching size is **not fixed**. This is not a claim about arbitrary graphs, weighted matchings, or ellipsoid-optimality. The \(n\ge4\) restriction avoids collapsed Johnson-scheme components. Standard complete-graph matching models and association-scheme formulas may contain equivalent representations under other terminology; historical priority remains provisional pending expert review.

## References

1. N. M. M. de Abreu, L. M. G. C. da Costa, C. H. P. Nascimento, and L. Patuzzi, “A Note on the Matching Polytope of a Graph,” *Trends in Computational and Applied Mathematics* **20** (2019), 189–196. DOI: 10.5540/tema.2019.020.01.189. First publicly verified article date: 2019-05-20. Full text: https://tema.sbmac.org.br/tema/article/download/1239/881/6725.
2. J. C. Torres, “Normality of \(k\)-Matching Polytopes of Bipartite Graphs,” arXiv:2306.11910, originally posted 2023-06-20. https://arxiv.org/abs/2306.11910.
3. L. Ferrarini and S. Gualandi, “Total Coloring and Total Matching: Polyhedra and Facets,” arXiv:2105.09827, originally posted 2021-05-20. https://arxiv.org/abs/2105.09827. (Different total-matching construction.)
4. A. Quitmann, “Decay of correlations in the monomer-dimer model,” arXiv:2309.13632, originally posted 2023-09-24. https://arxiv.org/abs/2309.13632. (Different lattice-correlation setting.)
