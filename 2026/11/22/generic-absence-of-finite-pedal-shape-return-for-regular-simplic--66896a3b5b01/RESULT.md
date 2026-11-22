# Generic absence of finite pedal-shape return for regular simplices in every dimension at least three

## Finding

For every integer \(d\ge3\) and every regular Euclidean \(d\)-simplex \(S\), fix an altitude connecting a vertex to the centre of the opposite facet. For an interior point \(P\) on this altitude, form the **fixed-point facet pedal simplex** by taking the convex hull of the perpendicular projections of \(P\) onto the \(d+1\) facet-supporting hyperplanes; repeat using the same \(P\). Except for a **countable** set of positions \(P\) on that open altitude, **none** of the positive iterates is a regular simplex, hence none is similar to \(S\). All iterates exist, have full dimension, and contain \(P\) in their interiors. No assumption that every foot lies inside its corresponding facet is made.

More quantitatively, the axial shape-position dynamics have a regular-simplex fixed point whose two linearized multipliers are
\[
\lambda_\pm=\frac{-1\pm i\sqrt{d^2-1}}d.
\]
For \(d\ge3\), neither multiplier is a root of unity. For each prescribed positive iterate count \(N\), the regular-shape return function has a nonzero first derivative at the centred position. Thus a sufficiently small nonzero axial displacement avoids return at that particular \(N\).

## Assumptions and scope

Set \(k=d-1\). Let \(w_1,\ldots,w_d\in\mathbb R^k\) be the unit vertices of a regular \(k\)-simplex centred at zero, so \(w_i\cdot w_j=-1/k\) when \(i\ne j\). After translation, put the observation point at the origin, and write every axial-symmetric simplex as
\[
S(R,u,v)=\operatorname{conv}\bigl(\{(Rw_i,u):1\le i\le d\}\cup\{(0,v)\}\bigr),\quad R>0,\quad u<0<v.
\]
The dimensionless variables are \(q=R^2/(v-u)^2>0\) and \(t=-u/v>0\). Holding the *original regular simplex* fixed while moving the observation point along its open altitude holds \(q=q_*=k/(k+2)\) fixed and makes \(t\) range over \((0,\infty)\). The centroid corresponds to \(t_*=1/d\).

A symmetric simplex is regular exactly when its base edges and lateral edges coincide, equivalently \(q=q_*\). The pedal operation refers to the affine supporting hyperplanes, not to closest points constrained to their finite facets. Similarity is unrestricted, so failure of regularity is sufficient to exclude return to the original shape.

## Proof

**1. Invariant two-parameter family.** The facet opposite \((Rw_i,u)\) is contained in
\[
w_i\cdot x-\frac{r}{k}z=-\frac{rv}{k},\qquad r=\frac{R}{v-u}=\sqrt q.
\]
Its perpendicular foot from the origin is
\[
\left(-\frac{vrk}{k^2+r^2}w_i,\ \frac{vr^2}{k^2+r^2}\right).
\]
The foot on the base plane is \((0,u)\). Because \(u<0<v\) and \(r>0\), the new feet are affinely independent: the first \(d\) have a regular base, and the last lies strictly across the origin. Reflecting the new simplex centrally does not change its similarity class, and yields the new parameters
\[
r'=\frac{kr}{k^2t+(1+t)r^2},\qquad t'=\frac{r^2}{t(k^2+r^2)}.
\]
In squared-radius variables this is the **exact rational recurrence**
\[
F_d(q,t)=\left(\frac{k^2q}{\bigl(k^2t+(1+t)q\bigr)^2},\ \frac{q}{t(k^2+q)}\right).
\]
Every denominator is positive on \((0,\infty)^2\); both coordinates stay positive. Therefore every positive pedal iterate is a full-dimensional simplex with the observation point interior, and every finite iterate of \(F_d\) is real analytic on the positive quadrant.

**2. Fixed point and nonresonant linearization.** The regular centred configuration \((q_*,t_*)=(\frac{d-1}{d+1},\frac1d)\) is fixed. Direct differentiation gives
\[
J_d=DF_d(q_*,t_*)=
\begin{pmatrix}
\frac{d-2}{d}&-\frac{2(d-1)d^2}{(d+1)^2}\\
\frac{(d+1)^2}{d^3}&-1
\end{pmatrix},\quad
\operatorname{tr}J_d=-\frac2d,\quad\det J_d=1.
\]
The eigenvalues are \(\lambda_\pm=(-1\pm i\sqrt{d^2-1})/d\). If an eigenvalue were a root of unity, its sum with its inverse, \(-2/d\), would be an algebraic integer. But a rational algebraic integer is an integer; \(-2/d\) is not an integer for any integer \(d\ge3\). Consequently neither multiplier is a root of unity.

Write \(\cos\theta_d=-1/d\), with \(0<\theta_d<\pi\). The Cayley–Hamilton identity applied to the unimodular matrix \(J_d\) gives
\[
(J_d^N)_{12}=(J_d)_{12}\frac{\sin(N\theta_d)}{\sin\theta_d}\ne0
\quad\text{for every integer }N\ge1.
\]
Indeed the ratio can vanish only if \(\lambda_+^{2N}=1\), forbidden above. This proves that for each positive integer \(N\), the analytic function
\[
H_N(t)=\bigl[F_d^N(q_*,t)\bigr]_1-q_*
\]
has nonzero derivative \(H'_N(t_*)=(J_d^N)_{12}\). Hence it is not identically zero, and its zeros in the open interval \((0,\infty)\) form a discrete, therefore countable, subset.

**3. Simultaneous avoidance of every finite return.** The union \(\bigcup_{N=1}^\infty\{t:H_N(t)=0\}\) is countable. For any other axial position, the \(N\)th pedal simplex has \(q_N\ne q_*\) at every positive integer \(N\), hence is never regular and cannot be similar to the initial regular simplex. All operations remain valid by Step 1. For each fixed \(N\), nonzero \(H'_N(t_*)\) additionally gives nonreturn on a punctured neighbourhood of the centred position. \(\square\)

## Verification

The independent, standard-library-only program `verify.py` recomputes exact rational iterates, checks the two-dimensional Jacobian formulas and their Cayley–Hamilton off-diagonal recursion for multiple dimensions and iterate counts, and reproduces the published tetrahedral four-step benchmark. It verifies, in dimension three with \((q,t)=(1/2,1/9)\), the fourth shape coordinate \(q_4=121/50\) and the corresponding squared lateral-to-base edge ratio \(57/121\). These finite checks corroborate algebra, but the full infinite-dimensional-count argument is the analytic proof above, not enumeration.

Reproduce: `python3 verify.py` (Python 3 standard library only).

## Relationship to prior work

Zwierzyński, *When Pedal Shapes Come Back: a Complex Story* (arXiv:2611.01247v1, first public 31 October 2026), Section 3, constructs a single nonreturning fourth pedal of a regular tetrahedron; Section 4 proves two-step returns under concentric in- and circumsphere hypotheses. It does **not** give an all-dimensional map or exclude **every** positive return simultaneously for generic off-centre points. The specific near-centroid tetrahedral fourth-step nonreturn is also established in related prior work; that fourth-step case is not asserted here as new. The present claim is instead the all-dimensional, all-iterate co-countable nonreturn theorem and its non-torsion local spectrum.

Abu-Saris and Hajja, *The Chaotic Behavior of the Sequence of Pedal Simplices* (2009), analyse the **orthic** simplex formed by feet of altitudes dropped from each vertex. That operator is not the fixed-point-to-facets operator studied here; its one-dimensional d-kite recurrence is different. Likewise, fixed-point *farthest-facet* projections and four-step returns for right prisms concern other operators or bodies. These distinctions are mathematical, not just terminological.

## Limitations

The exceptional axial parameter set is shown to be at most countable, not explicitly classified; individual exceptional off-centre points might return. No assertion is made that all projections stay inside their finite facets for every iterate, nor about arbitrary non-axial points or global nonlinear quasiperiodicity. The local eigenvalues lying on the unit circle do not by themselves imply stability. The cited and searched literature does not establish exhaustive global historical priority; independent mathematical audit remains outstanding.

## References

1. Michał Zwierzyński, *When Pedal Shapes Come Back: a Complex Story*, arXiv:2611.01247v1 (first public 2026-10-31), Sections 3–4. https://arxiv.org/html/2611.01247v1
2. Raghib Abu-Saris and Mowaffaq Hajja, *The Chaotic Behavior of the Sequence of Pedal Simplices*, Results in Mathematics **55** (2009), 209–220. https://doi.org/10.1007/s00025-009-0411-z
