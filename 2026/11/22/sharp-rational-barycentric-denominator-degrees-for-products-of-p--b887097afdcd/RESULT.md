# Sharp rational barycentric denominator degrees for products of polygons with separated residual intersections

## Finding
Let \(P=P_1\times\cdots\times P_k\subset\mathbb R^{2k}\), where each \(P_i\) is a full-dimensional convex polygon with no consecutive collinear sides and one of the following properties: it is a quadrilateral; it is centrally symmetric; or no two of its side lines are parallel. Let \(m_i\) denote the number of sides, and define
\[
\delta_i=\begin{cases}
m_i-4,&P_i\text{ centrally symmetric},\\
1,&m_i=4\text{ and }P_i\text{ is not a parallelogram},\\
m_i-3,&\text{no two sides of }P_i\text{ are parallel}.
\end{cases}
\]
The cases cover all eligible factors (a triangle has \(\delta_i=0\)). Among **all nonnegative rational generalized barycentric coordinates** on the product, the least possible total polynomial degree of a common denominator is
\[
\boxed{\deg_{\mathrm{GBC}}(P)=\sum_{i=1}^k\delta_i.}
\]
This remains true after any invertible affine change of coordinates. In particular, for any \(k\ge1\), the product of \(k\) non-parallelogram convex quadrilaterals has minimum denominator degree exactly \(k\), regardless of how many parallel-side pairs its factors have. Such products have dimension \(2k\) and exactly \(4k\) facets; thus the general lower-bound expression \(m-2d\) equals zero here while the exact minimum is \(k\). The result concerns *minimum possible common denominator degree*, not merely the degree of the Wachspress denominator.

## Assumptions and scope
For a full-dimensional polytope \(P\subset\mathbb R^d\) with vertex set \(V\), rational generalized barycentric coordinates are rational functions \(\alpha_v=p_v/q\), with real polynomials \(p_v,q\), \(q\not\equiv0\), whose quotients are defined on a dense interior open set and admit bounded continuous extensions to \(P\), such that for every \(x\in P\)
\[
\alpha_v(x)\ge0,\qquad \sum_{v\in V}\alpha_v(x)=1,\qquad
\sum_{v\in V}v\,\alpha_v(x)=x.
\]
Their **common denominator degree** is \(\deg q\) in the ambient coordinates. We minimize over all such coordinate systems and all representations by common polynomial denominators, including reduced ones. Here and below, a polygon side is a maximal facet, and all its vertices are the corners of the polygon. Factor variables occupy disjoint pairs of coordinate positions. No integrality or rationality of the polygon vertices is assumed.

For a polygon \(Q\), let \(\mathcal R(Q)\) be the finite set of intersections of nonadjacent supporting side lines that are not parallel. Define \(I(Q)\subset\mathbb R[x,y]\) as the ideal of polynomials vanishing on \(\mathcal R(Q)\). For an empty residual set, use the whole polynomial ring as the ideal, with minimum nonzero degree zero.

## Proof
**1. Polynomial denominators vanish on residual cylinders.** The identities \(\sum p_v=q\) and \(\sum v p_v=xq\) hold as polynomial identities, because they hold throughout the interior. Consider a facet \(F\) with affine supporting form \(\ell_F\). If \(v\notin F\), the nonnegative barycentric coefficients and affine precision force \(\alpha_v(x)=0\) for every \(x\in F\): apply the nonnegative exposing linear functional for \(F\) to \(x=\sum \alpha_v(x)v\). Continuity and the boundedness of \(q\) imply \(p_v=0\) on \(F\), whence \(\ell_F\mid p_v\). This remains valid even if \(q\) vanishes on \(F\).

Fix a factor \(P_i\) and two nonadjacent nonparallel side lines meeting at \(z\in\mathcal R(P_i)\). The corresponding facets of the product are distinct and have no common product vertex. For every product vertex \(v\), at least one of these facets omits \(v\); hence the polynomial \(p_v\) vanishes on the whole affine cylinder \(\{x_i=z\}\times\prod_{j\ne i}\mathbb R^2\). Consequently so does \(q=\sum p_v\). As this holds for every \(z\), the polynomial \(q\) belongs to the extension \(I(P_i)\mathbb R[x_1,y_1,\ldots,x_k,y_k]\) for every \(i\). The last implication follows by expanding \(q\) in monomials in all variables outside the \(i\)-th block: each coefficient must vanish at all residual points.

**2. Minimum degree in each residual ideal.** Write \(\mu(Q)\) for the least degree of a nonzero polynomial in \(I(Q)\). If \(Q\) has \(m\ge3\) sides and no parallel pair, each side line meets exactly \(m-3\) nonadjacent side lines in distinct finite residual points. Distinctness follows because three different edge-supporting lines of a nondegenerate convex polygon cannot meet at a point outside the polygon; any line through such a point supporting the polygon must be an extreme tangent, of which there are at most two. No nonadjacent side line passes through a vertex on the given side. Thus a nonzero polynomial \(f\) of degree smaller than \(m-3\) vanishing on the residual points must vanish identically on each of the \(m\) side lines; their product divides \(f\), contradicting its degree. It follows that \(\mu(Q)\ge m-3\).

If \(Q\) is centrally symmetric with \(m\ge4\) sides, every side has precisely one parallel opposite side and hence \(m-4\) distinct finite intersections with other nonadjacent side lines. The same restriction argument gives \(\mu(Q)\ge m-4\), including the trivial case \(m=4\). If \(Q\) is a non-parallelogram quadrilateral, at least one opposite pair of side lines intersects, and its intersection lies in the residual set. Thus any polynomial vanishing there has degree at least one: \(\mu(Q)\ge1\).

All these inequalities are equalities. Indeed, the polygonal Wachspress adjoint \(a_Q\) vanishes at the residual points and has degree \(m-3\) for a non-centrally-symmetric polygon and \(m-4\) for a centrally symmetric polygon, by the established planar adjoint-degree classification cited below. For the triangle it is a nonzero constant; for the non-parallelogram quadrilateral it is linear. Therefore **for every eligible factor** \(\mu(P_i)=\delta_i\).

**3. Disjoint-variable residual-ideal degree lemma.** Let \(I_i\) be a nonzero ideal in a polynomial ring \(R_i\) on a pair of variables, and let \(\mu_i\) be the minimum total degree of its nonzero elements. If \(0\ne f\in\bigcap_i I_i R\), where \(R=\mathbb R[x_1,y_1,\ldots,x_k,y_k]\), then
\[
\deg f\ge\sum_i\mu_i.
\]
Here is an elementary proof that does not require any ideal-intersection equality. Choose **one monomial of maximum total degree** in \(f\), and let its degree in the variables of the \(i\)-th block be \(b_i\). Expand \(f\) in the monomials of every block other than \(i\). Since \(f\in I_iR\), the coefficient polynomial \(f_i\) of the complementary monomial occurring in our chosen term belongs to \(I_i\). That coefficient is nonzero. Moreover, \(\deg f_i=b_i\): a higher-degree term in \(f_i\) would produce a monomial of \(f\) having strictly larger total degree than the chosen maximum, with the complementary monomial unchanged. By definition of \(\mu_i\), we obtain \(b_i\ge\mu_i\) for every \(i\). As \(\deg f=\sum_i b_i\), the inequality follows. If \(I_i=R_i\), take \(\mu_i=0\).

Applying the lemma to the denominator from Step 1 yields \(\deg q\ge\sum_i\delta_i\), for **every** rational nonnegative generalized barycentric system, without assuming its numerators have Wachspress form.
**4. Attainment.** Choose the polygonal Wachspress coordinates \(\alpha^i_{v_i}=w^i_{v_i}/a_{P_i}\), whose common denominator is positive on the interior and has degree \(\delta_i\). For each product vertex \((v_1,\ldots,v_k)\), set \(\alpha_{(v_1,\ldots,v_k)}(x_1,\ldots,x_k)=\prod_i\alpha^i_{v_i}(x_i)\). They are nonnegative and sum to one, and summing \(v_i\alpha_{(v_j)}\) over the product vertices gives coordinate-wise affine precision. Their common denominator \(\prod_i a_{P_i}(x_i)\) has total degree exactly \(\sum_i\delta_i\), by disjointness of variables and nonvanishing of the leading homogeneous factors. This matches Step 3. Invertible affine substitutions preserve total polynomial degree and rational GBC identities, giving the affine assertion.

## Verification
The companion standalone `verification.py` (Python 3 with SymPy) uses exact rational arithmetic. It constructs nonnegative Wachspress numerator formulas for a parallelogram, a generic quadrilateral, a trapezoid, a generic pentagon and a centrally symmetric hexagon; checks every polygon's polynomial affine-precision identities and its vertex normalization; computes all finite intersections of nonadjacent side lines; and checks by rational interpolation ranks that the minimum degree of a polynomial vanishing at those residual points is respectively \(0,1,1,2,2\). It also checks every affine-precision identity of the 16 product coordinates on a product of two non-parallelogram quadrilaterals, obtaining denominator degree two. These exact computations are diagnostics for examples; they do not substitute for Steps 1–4, which establish the result for arbitrary \(k\) and arbitrary eligible shapes.

## Relationship to prior work
Baumbach and Winter, *Rational barycentric coordinates and low degree adjoints* (arXiv:2611.02110v1, first posted November 1, 2026), define the minimum rational GBC denominator degree, establish residual-flat vanishing (Lemma 2.13), construct product coordinates (Example 2.4) and conjecture a general \(m-2d\) lower bound (Conjecture 4.1). Their examples show that the degree of the Wachspress denominator can exceed the true minimum on other higher-dimensional polytopes. Those results give an upper bound by product coordinates but **not** the lower bound established here.

Baumbach, Freyer, Weigert and Winter, *The canonical form, scissors congruence and adjoint degrees of polytopes* (arXiv:2508.04275v1), prove additivity of the **Wachspress adjoint degree** under Cartesian products (Theorem 3.5(i)) and the exact planar adjoint drop (Corollary 4.6). This determines the degree of the candidate product denominator, but does not establish minimality among all generalized barycentric systems. A published study, *Wachspress denominators have minimum degree on every convex polygon* (2026), establishes that minimality for a **single** polygon. Its statement and proof do not claim tensorization for products, and lower bounds on each factor alone do not imply the sum lower bound. The new content is the residual-ideal argument in Steps 1–3, including the disjoint-variable top-degree-monomial bound, which excludes cancellations among non-product rational representations.

Kohn and Ranestad, *Projective Geometry of Wachspress Coordinates* (2019/2020), and Brüser and Weigert, *Geometry of Adjoint Hypersurfaces for Polytopes* (2025), prove projective interpolation and rigidity statements for adjoint forms under specified residual multiplicities. The present theorem concerns **arbitrary affine rational GBC denominators**, for which only the compulsory residual-cylinder vanishing is used; it does not assume the extra multiplicity conditions of those adjoint characterizations.

## Limitations
The theorem covers products of quadrilaterals and polygons either centrally symmetric or having no parallel side pair, not every product of polygons and not indecomposable higher-dimensional polytopes. For a noncentrally symmetric polygon with multiple parallel side pairs and at least six sides, simple residual-point vanishing may allow a polynomial degree smaller than the Wachspress adjoint degree; the proof does not establish additivity in that case. The residual-ideal lemma applies over \(\mathbb R\) and to exact vanishing, not approximate interpolation. The theorem does not assert unique minimizers, specific optimal numerator degrees, or numerical stability. The primary and published-source comparison supports provisional originality only, not exhaustive historical priority; no independent mathematical audit has been performed.

## References
1. T. Baumbach and M. Winter, *Rational barycentric coordinates and low degree adjoints*, arXiv:2611.02110v1 (posted 2026-11-01), especially Example 2.4, Lemma 2.13 and Conjecture 4.1. https://arxiv.org/abs/2611.02110
2. T. Baumbach, A. Freyer, J. Weigert and M. Winter, *The canonical form, scissors congruence and adjoint degrees of polytopes*, arXiv:2508.04275v1 (2025), Theorem 3.5(i), Corollary 4.6. https://arxiv.org/abs/2508.04275
3. *Wachspress denominators have minimum degree on every convex polygon* (2026), published result on polygonal minimum denominator degrees. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-wachspress-denominators-have-minimum-degree-on-every-convex-poly--7b4aad67706d/RESULT.md
4. K. Kohn and K. Ranestad, *Projective Geometry of Wachspress Coordinates*, Foundations of Computational Mathematics 20 (2020), 1135–1173. https://doi.org/10.1007/s10208-019-09441-z
5. C. Brüser and J. Weigert, *Geometry of Adjoint Hypersurfaces for Polytopes*, arXiv:2511.13537v1 (2025), Theorems 1.3–1.4. https://arxiv.org/abs/2511.13537
