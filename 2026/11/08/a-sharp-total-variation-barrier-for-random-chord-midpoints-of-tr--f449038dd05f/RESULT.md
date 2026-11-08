# A sharp total-variation barrier for random chord midpoints of triangles

## Finding

Let \(T=\operatorname{conv}\{A,B,C\}\) be any nondegenerate Euclidean triangle of area \(\Delta>0\), with side lengths \(a=|BC|\), \(b=|CA|\), \(c=|AB|\) and perimeter \(P=a+b+c\). Draw \(X,Y\) independently from normalized arclength measure on \(\partial T\), put \(M=(X+Y)/2\), let \(\mu_T\) be the law of \(M\), and let \(\nu_T\) be normalized area measure on \(T\). Write \(p_a=a/P\), \(p_b=b/P\), \(p_c=c/P\), and \(e_2=p_ap_b+p_ap_c+p_bp_c\).

The measure \(\mu_T\) has the following **complete mixed-dimensional law**. Let \((\lambda_A,\lambda_B,\lambda_C)\) denote barycentric coordinates. Partition its interior, up to null boundaries, into the medial triangle \(K=\{\lambda_A,\lambda_B,\lambda_C<1/2\}\) and three corner triangles \(T_A=\{\lambda_A>1/2\}\), \(T_B=\{\lambda_B>1/2\}\), \(T_C=\{\lambda_C>1/2\}\). Each region has area \(\Delta/4\). Relative to planar Lebesgue area, the density of the absolutely continuous part of \(\mu_T\) is

\[
 f(m)=\frac4\Delta\begin{cases}
 e_2,&m\in K,\\
 p_bp_c,&m\in T_A,\\
 p_cp_a,&m\in T_B,\\
 p_ap_b,&m\in T_C.
 \end{cases}
\]

The remaining measure is supported on the original three sides. On \(BC\), parametrized by arclength \(t\in(0,a)\) from \(B\), its one-dimensional density is \(4\min\{t,a-t\}/P^2\), and similarly on the other two sides.

**The total-variation distance has the exact shape formula**

\[
\boxed{d_{\mathrm{TV}}(\mu_T,\nu_T)=\frac34-e_2
=\frac14+\frac12(p_a^2+p_b^2+p_c^2).}
\]

The maximizing measurable set in the definition of total variation can be taken to be \(\partial T\cup K\). Moreover, for every nondegenerate triangle,

\[
\boxed{\frac5{12}\le d_{\mathrm{TV}}(\mu_T,\nu_T)<\frac12.}
\]

Equality in the lower bound holds **if and only if** \(T\) is equilateral. The upper bound is an unattained sharp supremum, approached by triangles with normalized side lengths tending to \((1/2,1/2,0)\). In particular, even the optimally balanced triangle has midpoint law at least \(5/12\) away from area-uniform sampling in total variation.

## Assumptions and scope

The sampling measure is **independent uniform physical arclength on the entire boundary**. The chord is the segment between the two endpoints, not the intersection with a motion-invariant random line. Coincident endpoints and vertices have probability zero. Total variation uses \(\sup_{E\subset T\text{ Borel}}|\mu_T(E)-\nu_T(E)|\), equivalently half the variation norm. The singular boundary component must not be discarded. The theorem covers all nondegenerate Euclidean triangles, including obtuse and arbitrarily thin triangles, but not a degenerate collinear triple.

## Proof

**Step 1: Edge selection and barycentric geometry.** A normalized-arclength point lies on side \(BC\), \(CA\), or \(AB\) with probabilities \(p_a\), \(p_b\), or \(p_c\), respectively. Conditional on choosing an edge, the affine edge parameter is uniform on \((0,1)\). Thus the events that the two endpoints occupy the same side have total mass \(p_a^2+p_b^2+p_c^2\).

For different sides meeting at \(A\), write \(X=A+u(B-A)\) on \(AB\) and \(Y=A+v(C-A)\) on \(AC\), with \(u,v\) independent uniform on \((0,1)\). Their midpoint is

\[
M=A+\frac{u}{2}(B-A)+\frac{v}{2}(C-A).
\]

The map sends the unit square bijectively onto the parallelogram \(Q_A=\{\lambda_B<1/2,\lambda_C<1/2\}\) inside \(T\). Its absolute Jacobian is \(|\det(B-A,C-A)|/4=\Delta/2\). The unordered side-selection event has probability \(2p_bp_c\), and therefore contributes constant area density \((2p_bp_c)/(\Delta/2)=4p_bp_c/\Delta\) on \(Q_A\). The same argument applies at \(B,C\).

**Step 2: Four-region overlap.** Almost every interior point of \(T\) has at most one barycentric coordinate larger than \(1/2\). In the corner region \(T_A\), precisely \(Q_A\) contains the point, so its area density is \(4p_bp_c/\Delta\). In the central medial triangle \(K\), all three parallelograms overlap, so the density is \(4(p_ap_b+p_ap_c+p_bp_c)/\Delta\). Each corner region and \(K\) is a triangle similar to \(T\) at scale \(1/2\), hence has area \(\Delta/4\). Integration yields exact masses

\[
 \mu_T(T_A)=p_bp_c,\quad
 \mu_T(T_B)=p_cp_a,\quad
 \mu_T(T_C)=p_ap_b,\quad
 \mu_T(K)=e_2.
\]

These four interior masses sum to \(2e_2=1-(p_a^2+p_b^2+p_c^2)\), as they must.

**Step 3: The singular part.** If both endpoints lie on \(BC\), their independent positions \(U,V\) measured from \(B\) are uniform on \((0,a)\), and \((U+V)/2\) has density \(4\min\{t,a-t\}/a^2\). Multiplication by the edge event probability \(a^2/P^2\) gives the stated unconditional arclength density \(4\min\{t,a-t\}/P^2\). Its integral equals \(p_a^2\). The other edges are analogous. Different-edge pairs produce an absolutely continuous planar image and contribute no boundary atoms.

**Step 4: Exact Hahn decomposition.** Every side of a nondegenerate triangle is shorter than its other two sides combined, hence \(0<p_a,p_b,p_c<1/2\). Consequently \(4p_bp_c<1\), and analogously for the other corner densities. Also

\[
 e_2=\frac{1-(p_a^2+p_b^2+p_c^2)}2>\frac14,
\]

since \(p_a^2+p_b^2+p_c^2<\max\{p_a,p_b,p_c\}<1/2\). Thus \(\mu_T-\nu_T\) is positive on the singular boundary and has positive area density on \(K\), but has strictly negative area density on each corner region. Up to null sets, \(E=\partial T\cup K\) is a Hahn-positive set and attains total variation. Therefore

\[
\begin{aligned}
 d_{\mathrm{TV}}(\mu_T,\nu_T)
 &=\mu_T(E)-\nu_T(E)\\
 &=\sum_{i\in\{a,b,c\}}p_i^2+e_2-\frac14\\
 &=\frac34-e_2=\frac14+\frac12\sum_i p_i^2.
\end{aligned}
\]

**Step 5: Sharp range.** By Cauchy--Schwarz, \(\sum_i p_i^2\ge1/3\), with equality only if all three side lengths are equal. On the other hand \(\sum_i p_i^2<1/2\) by the strict triangle inequalities as above. The normalized side-length triples \((\frac12-\varepsilon,\frac12-\varepsilon,2\varepsilon)\), \(0<\varepsilon<1/6\), are realizable by nondegenerate isosceles triangles and approach \((1/2,1/2,0)\); their sum of squares tends to \(1/2\). Substitution proves both sharp bounds and all equality statements. \(\square\)

## Verification

The standalone standard-library checker `verify_midpoint.py` verifies the rational mass decomposition, positivity/negativity of the four area-density differences, equality of the integral and Hahn total-variation calculations, side triangular-density normalizations, the equilateral equality and a thin-isosceles near-supremum. An independent barycentric endpoint generator tests the four interior regions and singular edge allocation over 175,000 deterministic pseudorandom samples spanning five triangles. The executed checker output was:

`VERIFY_OK exact_cases=6 exact_mass_relations=7 per_case monte_carlo_trials=35000 total_trials=175000`

This finite computation checks instances of the formulas and implementation; the all-triangle theorem is proved algebraically above, not inferred from simulation.

## Relationship to prior work

Classical random-chord studies distinguish different chord sampling laws. Bäsel (2012, arXiv:1204.2707) derives motion-invariant-line chord length distributions for regular polygons and distances between two interior-uniform points; those results do not state the position law of the midpoint of an independent arclength-endpoint chord. Tong, Ahmadi and Pan (2013, arXiv:1312.2498) treat distance distributions between area-uniform points inside triangles and chords defined by line sampling; their accessible formulations likewise differ. A prior geometric-probability result on second moments of boundary-versus-interior distances for arbitrary triangles concerns a scalar distance moment, not the four-cell midpoint measure or its exact total variation against uniform area. The full historical literature has not been exhaustively inspected; in particular, an inaccessible earlier triangle chord-distribution article could contain an unindexed relevant formula.

## Limitations

The formula is for independent endpoints and full measure-level total variation, including boundary singular mass. It must not be applied to Crofton-random lines, conditional distinct-edge sampling, or midpoint rules chosen uniformly by area. It does not derive analogous sharp laws for quadrilaterals, higher polygons, or smooth curves. Scientific priority is subject to independent literature verification.

## References

- Uwe Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first posted 2012-04-12; see §§1, 3–5. https://arxiv.org/abs/1204.2707
- Fei Tong, Maryam Ahmadi, Jianping Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498, posted 2013-11-29; see §§I–II. https://arxiv.org/abs/1312.2498
- Andrei Duma and Sebastiano Rizzo, *Chord length distribution functions for an arbitrary triangle*, Supplemento ai Rendiconti del Circolo Matematico di Palermo 81 (2009), 141–157. Historical comparator; primary full text not inspected.
