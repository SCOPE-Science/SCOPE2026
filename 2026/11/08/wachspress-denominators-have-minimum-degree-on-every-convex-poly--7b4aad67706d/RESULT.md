# Wachspress denominators have minimum degree on every convex polygon

## Finding
Let \(P\subset\mathbb R^2\) be a full-dimensional convex polygon with exactly \(m\ge3\) sides and distinct consecutive supporting lines. Let \(\delta(P)\) be the smallest degree of a **common polynomial denominator** among rational nonnegative generalized barycentric coordinates at all vertices of \(P\). Let \(a_P\) be a Wachspress adjoint denominator, defined up to a nonzero scalar. Then
\[
\boxed{\delta(P)=\deg a_P=\begin{cases}m-4,&P\text{ centrally symmetric},\\m-3,&P\text{ not centrally symmetric}.\end{cases}}
\]
The first branch can occur only for \(m\ge4\); for triangles the second gives degree zero. Moreover, if \(m\ge4\) and a rational generalized barycentric representation has a reduced denominator \(q\) of degree at most \(m-4\), then \(q\) is a nonzero scalar multiple of \(a_P\). In particular, such a representation exists only for centrally symmetric polygons. This establishes the conjectural \(m-2d\) denominator-degree lower bound in dimension \(d=2\), and identifies the exact answer rather than only a bound.

## Assumptions and scope
Write the vertices in counterclockwise order as \(v_0,\ldots,v_{m-1}\), with indices modulo \(m\). Consecutive edges are not collinear. A rational generalized barycentric representation consists of rational functions \(\alpha_i=p_i/q\) regular on the polygon interior, with polynomial \(p_i,q\) over \(\mathbb R\), such that \(\alpha_i\ge0\) on \(P\), \(\sum_i\alpha_i=1\), and \(\sum_i v_i\alpha_i=x\). At a boundary point their continuous restrictions are understood; equivalently it is enough for the proof that the numerator of each vertex not on a facet vanishes on that facet. One common nonzero polynomial denominator is required. Multiplication or cancellation of common polynomial factors does not change the underlying coordinates; the degree is minimized over such representations.

For a side \(E_i=[v_i,v_{i+1}]\), put \(e_i=v_{i+1}-v_i\) and \(\ell_i(x)=\det(e_i,x-v_i)\). These are nonnegative inside the counterclockwise polygon. Put \(k_i=\det(e_{i-1},e_i)>0\), and define
\[
 w_i(x)=k_i\prod_{j\notin\{i-1,i\}}\ell_j(x),\qquad
 a_P(x)=\sum_{i=0}^{m-1} w_i(x).
\]
This is a convenient positive normalization of the Wachspress denominator; replacing the side forms by positive multiples only changes its overall scalar. Its degree is at most \(m-3\), even though each displayed numerator has degree \(m-2\).

## Proof
**1. Reduction of any denominator.** The normalization and affine-precision identities hold polynomially:
\[
 q=\sum_i p_i,\qquad xq=\sum_i v_i p_i.
\]
Cancel a greatest common polynomial factor of the numerators (which also divides their sum \(q\)). Positivity on a facet \(E_i\) implies \(\ell_i\mid p_j\) for every vertex \(v_j\notin E_i\). We claim \(\ell_i\nmid q\). Otherwise, restricting both polynomial identities to \(E_i\) leaves
\[
 p_i+p_{i+1}=0,\qquad v_i p_i+v_{i+1}p_{i+1}=0.
\]
Since \(v_i\ne v_{i+1}\), both remaining numerator restrictions vanish; hence \(\ell_i\) divides **every** numerator, contradicting reduction. Therefore \(q|_{\ell_i=0}\) is a nonzero univariate polynomial on every side line. This argument does not assume a pre-existing minimal-denominator theorem.

**2. Residual intersections and a lower degree bound.** If side lines \(\ell_i=0\) and \(\ell_j=0\) are nonadjacent, then they have no common polygon vertex. At any finite intersection \(z\), every numerator \(p_h\) is divisible by at least one of \(\ell_i\) or \(\ell_j\), since no vertex lies on both sides. Thus \(p_h(z)=0\) for every \(h\), and \(q(z)=0\).

On a fixed side line, the \(m-3\) nonadjacent supporting lines are either intersecting or parallel to it. At most one can be parallel: a given edge direction permits only the two opposite support lines of a convex polygon. Their finite intersections are pairwise distinct. Indeed, three distinct supporting lines of a nondegenerate convex polygon cannot pass through a common point outside the polygon, since an exterior point admits at most two distinct supporting lines (the two extreme tangents); and a nonadjacent supporting line cannot pass through a point of the side itself. Consequently, the nonzero restriction of \(q\) to any side line has at least \(m-4\) distinct roots, and has \(m-3\) roots if that side has no parallel mate. Hence \(\deg q\ge m-4\) for \(m\ge4\), strengthened to \(\deg q\ge m-3\) if some side has no parallel mate.

**3. Exact side restriction of the Wachspress denominator.** On the line of side \(E_i\), only \(w_i\) and \(w_{i+1}\) survive. Their common factor is the product over all nonadjacent side forms. The remaining factor is the constant \(k_i k_{i+1}\): the affine function \(k_i\ell_{i+1}+k_{i+1}\ell_{i-1}\) has the same value \(k_i k_{i+1}\) at both endpoints of \(E_i\). Thus
\[
 \boxed{\left.a_P\right|_{\ell_i=0}=
 k_i k_{i+1}\left.\prod_{j\notin\{i-1,i,i+1\}}\ell_j\right|_{\ell_i=0}.}
\]
In particular, \(a_P(v_i)=w_i(v_i)>0\), and \(a_P|_{\ell_i=0}\) has exactly the distinct residual roots from Step 2, with univariate degree \(m-3\) if there is no parallel mate and degree \(m-4\) otherwise. If some side has no parallel mate, then \(\deg a_P=m-3\). Together with Step 2 this proves \(\delta(P)=\deg a_P=m-3\) in that case.

**4. Rigidity of a hypothetical lower denominator.** Suppose every side has a parallel mate and a reduced denominator satisfies \(\deg q\le m-4\). By Step 2, \(\deg q=m-4\) and each nonzero line restriction \(q|_{\ell_i=0}\) has exactly the same \(m-4\) roots as \(a_P|_{\ell_i=0}\). The latter has degree \(m-4\) by Step 3. Hence on each side line
\[
 q|_{\ell_i=0}=\lambda_i a_P|_{\ell_i=0}
\]
for some nonzero scalar \(\lambda_i\). At each common vertex \(v_{i+1}\), the adjacent restrictions agree and \(a_P(v_{i+1})>0\), so \(\lambda_i=\lambda_{i+1}\). All are one scalar \(\lambda\). The polynomial \(q-\lambda a_P\) vanishes identically on all \(m\) distinct side lines. Since \(\deg(q-\lambda a_P)\le m-3<m\), these \(m\) distinct affine linear factors force \(q=\lambda a_P\) identically. Thus no denominator has degree smaller than \(\deg a_P\), including in the fully parallel-paired case.

**5. Complete classification.** Wachspress coordinates achieve denominator \(a_P\), so Steps 3–4 give \(\delta(P)=\deg a_P\) for all polygons, with the elementary triangle case giving zero. The established planar adjoint-degree theorem of Baumbach–Freyer–Weigert–Winter (their Corollary 4.6, based on Theorem 4.5) states that \(\deg a_P=m-4\) exactly for centrally symmetric polygons and \(m-3\) otherwise. Substitution proves the displayed formula. Notice that merely pairing all side directions is not equivalent to central symmetry: a six-gon can have three parallel side pairs with unequal lengths. Step 4, not just the root count, rules out a smaller denominator on those noncentrally symmetric configurations.

## Verification
The companion standalone `verification.py` performs **exact symbolic computations**, with rational coordinates throughout, on a triangle, a parallelogram, a trapezoid, a pentagon, a centrally symmetric hexagon and a noncentrally symmetric hexagon with three parallel side pairs. It checks affine precision, vertex normalization, strict convexity, the exact edge-restriction formula above, vanishing at every finite residual intersection, and the predicted degrees \(0,0,1,2,2,3\). For the two hexagons, it also computes the rank of the six-point conic interpolation matrix: respectively \(5\) and \(6\). These examples are supplementary diagnostics; the arbitrary-\(m\) proof is Steps 1–5, not an inference from finite tests. Run `python verification.py` with SymPy installed.

## Relationship to prior work
Baumbach and Winter, *Rational barycentric coordinates and low degree adjoints* (arXiv:2611.02110v1, first posted 2026-11-01), formulate the general inequality \(\delta(P)\ge m-2d\) as **Conjecture 4.1**, prove residual-flat vanishing and facet nonvanishing statements (Lemmas 2.12–2.13), and distinguish minimum denominator degree from minimum numerator degree. Their text gives no polygon-wide resolution of the denominator conjecture. The present result proves the planar case and the stronger exact identity \(\delta(P)=\deg a_P\).

Baumbach–Freyer–Weigert–Winter, *The canonical form, scissors congruence and adjoint degrees of polytopes* (arXiv:2508.04275v1), already classify the **degree of the Wachspress adjoint** in polygons: the degree drops by one precisely for centrally symmetric polygons. That result alone does not exclude another rational generalized barycentric system of strictly lower denominator degree; the exclusion is the content of Steps 1–4. Kohn and Ranestad, *Projective geometry of Wachspress coordinates* (arXiv:1904.02123v3), prove a projective uniqueness statement for adjoints under a simple-hyperplane-arrangement hypothesis. In special generic situations this may already force the minimal-denominator conclusion when combined with residual vanishing; their stated theorem does not cover the parallel-paired and nongeneric polygons addressed here. Related comparisons include Romanowska–Smith–Zamojska-Dzienio, *The inverse problem of convex polygon coordinates* (arXiv:2308.11634), whose primary focus is barycentric representation and coordinate comparison, not the minimum denominator degree over all rational systems.

## Limitations
The assertion is confined to convex **polygons**, not higher-dimensional polytopes. In dimension three and higher, rational generalized barycentric coordinates may have smaller denominator degree than the Wachspress adjoint (examples appear in arXiv:2611.02110). The proof uses nonnegative coordinates and **one common polynomial denominator**; it does not classify arbitrary signed rational affine-precision formulas. The degree-one/drop dichotomy for the adjoint in Step 5 is cited from prior work, while the new minimality and rigidity statements are proved directly. No claim of an exhaustive survey of historical alternative terminology is made. The proof has not undergone independent mathematical review.

## References
1. M. Winter and T. Baumbach, *Rational barycentric coordinates and low degree adjoints*, arXiv:2611.02110v1 (2026-11-01), Sections 2–4, especially Conjecture 4.1. https://arxiv.org/abs/2611.02110
2. T. Baumbach, A. Freyer, J. Weigert and M. Winter, *The canonical form, scissors congruence and adjoint degrees of polytopes*, arXiv:2508.04275v1 (2025), Theorem 4.5 and Corollary 4.6. https://arxiv.org/abs/2508.04275
3. K. Kohn and K. Ranestad, *Projective geometry of Wachspress coordinates*, arXiv:1904.02123v3 (2019), Theorem 1.5 and discussion of residual arrangements. https://arxiv.org/abs/1904.02123
4. A. B. Romanowska, J. D. H. Smith and A. Zamojska-Dzienio, *The inverse problem of convex polygon coordinates*, arXiv:2308.11634 (2023; revised 2026). https://arxiv.org/abs/2308.11634
