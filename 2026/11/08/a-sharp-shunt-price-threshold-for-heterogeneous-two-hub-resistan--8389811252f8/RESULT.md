# A sharp shunt-price threshold for heterogeneous two-hub resistance networks

## Finding

Fix an integer \(m\ge 2\), strictly positive leaf-pair prices \(c_1,\ldots,c_m\), a strictly positive direct-bridge price \(d\), and a budget \(B>0\). Let \(G\) have hubs \(u,v\), leaves \(z_1,\ldots,z_m\), edges \(uz_i,vz_i\) each priced at \(c_i\) per unit conductance, and an optional edge \(uv\) priced at \(d\). Allocate independent, nonnegative conductances to all \(2m+1\) edges, with total cost at most \(B\), and minimize the Kirchhoff index \(\mathcal K=\sum_{s<t}R_{st}\), where \(R_{st}\) is effective resistance and disconnected designs have infinite cost.

Set
\[
A=\frac{m+1}{2},\qquad C=m+2.
\]
There is a unique number \(\rho>C/\min_i c_i\) satisfying
\[
\sum_{i=1}^m \sqrt{\frac{A}{\rho c_i-C}}=1.
\]
Define the critical bridge price
\[
\boxed{d_{\mathrm{crit}}=\frac{4C}{\rho}}.
\]
The globally optimal allocation is unique. Both edges incident with each leaf \(z_i\) have the same, strictly positive optimal conductance \(x_i\). The direct-bridge optimal conductance \(y\) is **strictly positive if and only if** \(0<d<d_{\mathrm{crit}}\).

When \(d\ge d_{\mathrm{crit}}\), set
\[
\kappa_i=\sqrt{\frac{A}{\rho c_i-C}},\quad
T_0=\frac{B}{2\sum_j c_j\kappa_j}.
\]
Then \(x_i=T_0\kappa_i\), \(y=0\), and
\[
\mathcal K_{\min}=\frac{2\sum_jc_j\kappa_j}{B}\left(A\sum_i\frac1{\kappa_i}+C\right).
\]
When \(0<d<d_{\mathrm{crit}}\), set
\[
 k_i=\sqrt{\frac{Ad}{C(4c_i-d)}},\qquad
 H=\frac12\left(d+\sqrt{\frac{Ad}{C}}\sum_j\sqrt{4c_j-d}\right).
\]
All denominators are positive and \(\sum_i k_i<1\). Then
\[
\boxed{x_i=\frac{Bk_i}{H},\quad y=\frac{B(1-\sum_i k_i)}{2H}},
\qquad
\boxed{\mathcal K_{\min}=\frac{\big(\sqrt{Cd}+\sqrt A\sum_i\sqrt{4c_i-d}\big)^2}{2B}}.
\]
The two formulas agree continuously at the threshold. The critical price is independent of \(B\). In the equal-price case \(c_i=c\), the exact threshold is
\[
\boxed{\frac{d_{\mathrm{crit}}}{c}=
\frac{8(m+2)}{m^2(m+1)+2(m+2)}\sim\frac8{m^2}.}
\]
Thus a directly installed hub-to-hub link is worth funding only below a price window that shrinks quadratically in the number of parallel two-edge routes.

## Assumptions and scope

The graph is simple and undirected, with exactly the described edges; conductances are linear nonnegative decision variables, leaf-pair prices are mirrored between the two hub incidences, and there are no pre-existing conductances or degree limits. Prices and budget are real and strictly positive. The Kirchhoff index is the *unscaled* sum over unordered vertex pairs. The value \(y=0\) means the candidate bridge is not installed, but each leaf must retain a connection to both hubs at the unique optimum. No discrete cardinality constraint is imposed.

## Proof

**1. Existence, uniqueness and forced reflection symmetry.** For a connected conductance vector \(w\), let \(L(w)\) be its weighted graph Laplacian and let \(J=\mathbf1\mathbf1^\top/(m+2)\). Kirchhoff's spectral identity yields
\[
\mathcal K(w)=(m+2)\operatorname{tr}((L(w)+J)^{-1})-(m+2).
\]
The map \(X\mapsto\operatorname{tr}(X^{-1})\) is strictly convex on positive-definite symmetric matrices: for any nonzero symmetric direction \(H\), its second derivative equals \(2\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0\). Distinct edge vectors yield distinct Laplacians because their off-diagonal entries recover each edge weight. Thus the connected-domain objective is strictly convex in all edge conductances. The bounded budget set is compact; as a connected network approaches disconnection, at least one positive Laplacian eigenvalue tends to zero and \(\mathcal K\to\infty\), so a unique connected minimizer exists. The full budget is spent by positive homogeneity: scaling up every weight strictly lowers \(\mathcal K\). Exchanging hubs \(u,v\) preserves prices and the objective. By uniqueness, each pair \((uz_i,vz_i)\) has a common optimal conductance \(x_i>0\).

**2. Exact resistance reduction.** For a reflection-symmetric design, write \(x_i>0\), \(y\ge0\), and \(T=\sum_i x_i+2y\). Decomposing current injections into hub-symmetric and hub-antisymmetric components (or solving Kirchhoff's equations) gives
\[
R_{uv}=\frac2T,\qquad
R_{uz_i}=R_{vz_i}=\frac1{2x_i}+\frac1{2T},\qquad
R_{z_i z_j}=\frac1{2x_i}+\frac1{2x_j}\ (i\ne j).
\]
For example, the hub-antisymmetric Laplacian eigenvalue is \(T\), which yields the \(1/(2T)\) contribution to each hub-to-leaf resistance; in the symmetric sector each leaf-to-hub resistance contribution is \(1/(2x_i)\). Summing the displayed expressions over all pairs gives the exact scalar problem
\[
\boxed{\mathcal K=A\sum_i\frac1{x_i}+\frac C T},\qquad
2\sum_i c_i x_i+dy=B,
\quad T=\sum_i x_i+2y.
\]
This objective is strictly convex on \(x_i>0,y\ge0\): the positive diagonal Hessian from \(A\sum_i x_i^{-1}\), together with the positive rank-one Hessian from \(C/T\), is positive definite in \((x_1,\ldots,x_m,y)\).

**3. The no-bridge solution and its threshold.** Let \(y=0\). With Lagrange multiplier \(\lambda>0\), stationarity in every \(x_i\) reads
\[
\frac A{x_i^2}+\frac C{T^2}=2\lambda c_i.
\]
Set \(\rho=2\lambda T^2\) and \(\kappa_i=x_i/T\). Then \(\kappa_i=\sqrt{A/(\rho c_i-C)}\) and \(\sum_i\kappa_i=1\). The left side of the defining equation is strictly decreasing, continuously from infinity at \(\rho\downarrow C/\min_i c_i\) to zero at infinity, proving uniqueness of \(\rho\) and the no-bridge formula. The one-sided Karush–Kuhn–Tucker condition for \(y=0\) is
\[
-\frac{2C}{T^2}+\lambda d\ge0
\quad\Longleftrightarrow\quad d\ge\frac{4C}{\rho}.
\]
Strict convexity and the Slater condition make this necessary and sufficient for the global optimum.

**4. Activated-bridge formula.** When \(d<4C/\rho\), the no-bridge point violates that condition, so the unique optimizer has \(y>0\). Its bridge stationarity is \(\lambda d=2C/T^2\). Combining with the leaf equations gives
\[
\frac{x_i}{T}=k_i=\sqrt{\frac{Ad}{C(4c_i-d)}}.
\]
To prove the square roots exist and \(\sum k_i<1\), note that \(d_{\mathrm{crit}}=4C/\rho<4\min_i c_i\), and the function \(\sum_i\sqrt{Ad/[C(4c_i-d)]}\) is strictly increasing on \((0,4\min_i c_i)\). At \(d=d_{\mathrm{crit}}\), its terms equal the respective \(\kappa_i\), so their sum is one. The budget then gives \(T=B/H\), and \(y=(T-\sum_i x_i)/2\), proving the displayed formulas. Substitution into \(A\sum_i1/x_i+C/T\) yields the closed square for \(\mathcal K_{\min}\). All KKT conditions hold, so strict convexity proves global uniqueness.

**5. Equal-price limit.** If \(c_i=c\), normalization forces \(\kappa_i=1/m\), hence \(\rho c-C=A m^2\) and \(d_{\mathrm{crit}}=4Cc/(C+A m^2)\), which simplifies to the rational expression above. Dividing numerator and denominator by \(m^3\) proves the stated asymptotic.

## Verification

Run `python verify_design.py` using Python with NumPy, SciPy and SymPy installed. The code reconstructs graph Laplacians from edge lists, computes exact Kirchhoff indices from grounded-matrix inverses, tests the derived symmetric formula for distinct rational conductance patterns, checks budget and KKT equations for positive and zero bridge regimes across heterogeneous price vectors, compares against independently sampled fully asymmetric feasible designs, and checks the equal-price threshold. During preparation it returned `VERIFY_OK 2035`. These finite tests are supporting checks; the proof of all quantifiers and strict uniqueness is analytic above.

Example: for \(m=3\), \((c_1,c_2,c_3)=(1,2,4)\), and \(B=100\), the critical bridge price is approximately \(1.50620825057\). At \(d=0.5\) the unique optimum has \((x_1,x_2,x_3)\approx(11.06159,7.55650,5.25637)\) and \(y\approx11.19974\); at \(d=2\), it has \(y=0\).

## Relationship to prior work

Ghosh, Boyd and Saberi formulate minimization of total effective resistance over edge conductances as a convex problem, establish uniqueness, and provide analytic solutions for trees, wheels and a barbell. Their 2006 conference proceedings and complete 2008 journal paper give the foundational approach. The present contribution is **not** a new generic convexity theorem; it is the previously unidentified evaluated heterogeneous-price solution, including an exact one-dimensional critical-price equation, a complete two-regime allocation, and a closed radical expression on the activated side for the natural \(K_{1,1,m}\) family. Yang's 2012 complete-bipartite Kirchhoff-index bounds address fixed unit weights and extremal graph classes, not conductance-price allocation. Contemporary graph augmentation work treats a fixed weighted base, combinatorial candidate-edge selection and numerical relaxations, rather than this exact all-conductance allocation.

## Limitations

The structural reduction requires equal prices for the two spokes incident to each leaf; distinct prices on those two edges are outside the claim. The inactive-bridge regime requires solving one monotone scalar equation rather than evaluating a general radical expression. The results do not establish publication priority. Searches may miss equivalent results under different graph names or stronger optimization formulations. A 2006 conference version of the focal source is verified to have existed, but its first public-release *day* is not established by the available document (which records the conference interval July 24–28, 2006); February 1, 2008 is the earliest exact **day-verified** release of the inspected complete journal version, and this date is not represented as excluding earlier circulation.

## References

1. Arpita Ghosh, Stephen Boyd and Amin Saberi, *Minimizing Effective Resistance of a Graph*, 17th International Symposium on Mathematical Theory of Networks and Systems, Kyoto, July 24–28, 2006 (conference PDF: https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf); SIAM Review **50** (2008), 37–66, DOI 10.1137/050645452 (author-hosted full text: https://stanford.edu/~boyd/papers/pdf/eff_res.pdf; published electronically February 1, 2008).
2. Y. Yang, *Bounds for the Kirchhoff Index of Bipartite Graphs*, Journal of Applied Mathematics (2012), article 195242, https://doi.org/10.1155/2012/195242.
3. Omkar Bhoite, V. S. Dhuli, Stefan Werner and Kimmo Kansanen, *Budget-Constrained Graph Augmentation for Robust Network Design via Kirchhoff Index Minimization*, arXiv:2609.29790 (2026), https://arxiv.org/abs/2609.29790.
