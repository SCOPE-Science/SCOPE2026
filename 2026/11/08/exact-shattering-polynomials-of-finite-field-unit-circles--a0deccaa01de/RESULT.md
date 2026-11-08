# Exact shattering polynomials of finite-field unit circles

## Finding
Fix any odd prime power \(q\ge3\), a nonzero field element \(t\in\mathbb F_q^\times\), and the plane \(V=\mathbb F_q^2\). For each center \(c\in V\), define the circle
\[
C_t(c)=\{x\in V:(x_1-c_1)^2+(x_2-c_2)^2=t\}.
\]
The Boolean concept class is \(\mathcal C_{q,t}=\{\mathbf1_{C_t(c)}:c\in V\}\). A support \(S\subseteq V\) is shattered when every labeling \(S\to\{0,1\}\) equals the restriction of some concept. The shattering polynomial is \(\Phi_{q,t}(z)=\sum_{S\text{ shattered}}z^{|S|}\).

Let \(\chi_q\) be the quadratic multiplicative character and set \(\epsilon=\chi_q(-1)\) and \(k=q-\epsilon\). For every nonzero radius parameter \(t\),
\[
\boxed{\Phi_{q,t}(z)=1+q^2z+\frac{q^2k^2}{4}z^2+\frac{q^2k(k-2)(k-4)}6z^3.}
\]
No positive-degree coefficient beyond degree three occurs. The exact geometric classification is: every singleton is shattered; a pair is shattered if and only if some circle contains both points; a triple is shattered if and only if it is contained in one circle and contains no pair of points antipodal about that center. Three distinct points can belong to at most one circle with the prescribed nonzero radius, so the latter center is unambiguous. The VC dimension equals \(2\) when \(q\in\{3,5\}\) and equals \(3\) for every odd prime power \(q\ge7\).

## Assumptions and scope
The field may be a proper extension of its prime field. The quadratic form is exactly \(Q(u)=u_1^2+u_2^2\), the radius *parameter* \(t\) is nonzero, all \(q^2\) possible centers and all \(q^2\) possible query points are available, and shattering is ordinary binary VC shattering. No conclusions are asserted for characteristic two, for the zero-level conic, or for an arbitrary restricted subset of centers or query points. The nonzero-level circles have \(k=q-\chi_q(-1)\) points, and \(k\) is even.

## Proof
**1. Circle size.** If \(-1\) is a square in \(\mathbb F_q\), choose \(i\) with \(i^2=-1\). The invertible linear coordinates \(u=x_1+i x_2\) and \(v=x_1-i x_2\) turn \(Q(x)=t\) into \(uv=t\), with exactly \(q-1\) solutions. If \(-1\) is nonsquare, the same quadratic expression identifies with the norm from \(\mathbb F_{q^2}^\times\) onto \(\mathbb F_q^\times\); the surjective norm has kernel of order \(q+1\), hence the fiber has \(q+1\) points. Thus every circle has exactly \(k=q-\chi_q(-1)\) points. Its points come in \(k/2\) disjoint antipodal pairs under \(x\mapsto 2c-x\), because the characteristic is odd and \(t\ne0\).

**2. Intersection and reflection lemmas.** Distinct circles of prescribed nonzero radius meet in at most two points. Indeed, subtracting their equations places any common point on a nonconstant affine line. Such a line meets \(Q(x)=t\) in at most two points: if its restriction as a degree-at-most-two polynomial were identically zero, the direction \(v\ne0\) would satisfy \(Q(v)=0\), the base point \(p\) would satisfy the polar orthogonality \(p\cdot v=0\), and \(Q(p)=t\ne0\); nondegeneracy in dimension two gives \(v^\perp=\langle v\rangle\) for isotropic \(v\), contradicting \(Q(p)\ne0\). It follows that three distinct points determine at most one center of a radius-\(t\) circle.

For a distinct pair \(a,b\) on \(C_t(c)\), its other possible center is exactly \(c'=a+b-c\): both \(Q(a-c')=Q(c-b)=t\) and \(Q(b-c')=Q(c-a)=t\). The intersection lemma shows no third center exists. The centers \(c,c'\) coincide precisely when \(a+b=2c\), meaning that the pair is antipodal about \(c\). Therefore an antipodal pair belongs to exactly one circle, and each nonantipodal pair in a circle belongs to exactly two.

**3. Singletons and pairs.** Each point belongs to exactly \(k\) circles (translate the circle-center relation); there is at least one circle missing the point, since \(q^2>k\). Thus all \(q^2\) singletons are shattered. A pair must lie on a common circle to realize the double-positive trace. Conversely, if it does, its set of common centers has cardinality at most two, while each point separately belongs to \(k\ge4\) circles. Hence each singleton-positive trace is realized by at least \(k-2\) centers. The all-negative trace is realized because the union of the two center sets has at most \(2k<q^2\) elements (check \(q=3\) directly, and use \(k\le q+1\) for \(q\ge5\)). This proves the pair characterization.

**4. Triples and the VC upper bound.** If a triple is shattered, its all-positive trace places it on a circle \(C_t(c)\). If two of its points are antipodal about \(c\), no center realizes the labeling positive on exactly that pair, by the unique-center property. Hence it is not shattered. Conversely, take three distinct points on \(C_t(c)\) with no antipodal pair. The all-positive trace is given by \(c\). For each pair, its second center \(a+b-c\ne c\) belongs to no circle containing the third point, because three points determine only the original center. This realizes all three pair-positive traces. For each singleton, at most four of its \(k\) incident centers lie on a circle through either of the other two points (two intersections per competing center set). When \(k\ge8\), there is a singleton-positive center. Finally, at most \(3k\) centers cover any of the three points, and \(q^2>3k\) for every odd prime power \(q\ge7\), so the all-negative trace exists. This shatters the triple whenever \(k\ge8\). For \(q=3,5\), one has \(k=4\); every three-element subset of a four-point circle contains one of its two antipodal pairs, so no triple is shattered. These are all odd prime powers, as \(q\ge7\) implies \(k\ge8\).

No four-element support can be shattered: an all-positive trace would place all four points on one circle, whereas a trace positive on precisely three would demand a *different* circle through those three points, contradicting uniqueness. By downward closure, no larger support is shattered.

**5. Enumerating all shattered supports.** For a fixed circle there are \(k/2\) antipodal pairs and \(\binom{k}{2}-k/2\) nonantipodal pairs. The former are counted in exactly one center and the latter in exactly two. Summing over \(q^2\) circles gives the pair coefficient
\[
q^2\left[\frac k2+\frac12\left(\binom k2-\frac k2\right)\right]=\frac{q^2k^2}{4}.
\]
A triple can belong to at most one circle. Exactly \(\binom{k}{3}-(k/2)(k-2)\) triples on each circle avoid antipodal pairs; the bad triples cannot contain two distinct antipodal pairs because they have only three elements. This simplifies to \(k(k-2)(k-4)/6\), giving the triple coefficient. The constant term equals one, and Step 3 gives the singleton coefficient. The formula follows for all nonzero \(t\), with the two small-field exceptions and the asserted VC dimensions.

## Verification
Run the standalone Python 3 file `verify_circle.py` in the same directory. The program independently constructs center-incidence bitsets and tests all eight label traces of all point triples (and four traces of all pairs), using no assumption that the proposed geometric classification is true. It checks every nonzero \(t\) for \(q=3,5,7,9\), plus \(t=1\) for \(q=11,13\); the order-nine field is implemented as \(\mathbb F_3[u]/(u^2+1)\). For each test the program compares exact counts with the theorem, and it ends in `FINITE_FIELD_UNIT_CIRCLE_SHATTER_PASS`. These are finite checks only; the unrestricted mathematical assertion is established by the preceding algebraic proof, not by extrapolation.

## Relationship to prior work
Fitzpatrick, Iosevich, McDonald and Wyman (2021, arXiv:2108.13231v1), Theorems 1.3 and 1.6, establish VC-dimension results for finite-field distance classifiers when the available set of points is sufficiently large. They explicitly establish the general upper bound of three via the uniqueness of a circle through three points. Pham (2023, arXiv:2304.09375v1), Theorem 1.4, improves the density threshold for obtaining VC dimension three, and develops a rhombus-count method. These established scalar dimension and uniqueness facts are not claimed to be novel here. The present exact contribution is the all-field, all-nonzero-radius classification of **every** shattered support and the exact three coefficients, with the \(q=3,5\) exceptions. The search comparisons examined the actual theorem statements and relevant proof sections of both papers; no claim of exhaustive historical priority is made.

## Limitations
The result does not cover even characteristic, the zero-radius conic, restricted point/center sets, or an online/Littlestone dimension. Some geometric ingredients, especially the two-circle intersection bound and the VC-dimension-three ceiling, are standard and explicitly appear in prior literature; only their exact new synthesis into the stated complete shattering polynomial and all-support characterization is proposed as the addition. Previous work under alternative language for finite conics or block designs may contain equivalent counts that were not located. Independent external audit has not been performed.

## References
1. D. Fitzpatrick, A. Iosevich, B. McDonald and E. L. Wyman, *The VC-dimension and point configurations in \(\mathbb F_q^2\)* (2021), arXiv:2108.13231v1, https://arxiv.org/abs/2108.13231.
2. Thang Pham, *Parallelograms and the VC-dimension of the distance sets* (2023), arXiv:2304.09375v1, https://arxiv.org/abs/2304.09375.
3. Thang Pham, S. Senger, M. Tait and N. Thu-Huyen, *VC-dimension and pseudo-random graphs* (2023), arXiv:2303.07878v1, https://arxiv.org/abs/2303.07878 (context for graph-neighborhood VC dimension; only abstract/theorem scope consulted).
