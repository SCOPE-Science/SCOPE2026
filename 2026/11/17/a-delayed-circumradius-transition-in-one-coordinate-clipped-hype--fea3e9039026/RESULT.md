# A delayed circumradius transition in one-coordinate clipped hypersimplices

## Finding
For integers \(m\ge2\), \(1\le k\le m-1\), and a real parameter \(0<t<1\), consider the \(m\)-dimensional Euclidean polytope
\[
Q_{m,k,t}=\{(x_1,\ldots,x_m,z)\in[0,1]^m\times[0,t]:x_1+\cdots+x_m+z=k\}.
\]
This is the ordinary hypersimplex \(\Delta(m+1,k)\) cut by the upper bound \(z\le t\), with its **inherited Euclidean metric**, not the metric of its projection onto the first \(m\) coordinates. Let \(R_{m,k}(t)\) be the radius of its unique minimum enclosing Euclidean ball. Set \(t_0=(m-k)/m\).

The exact squared circumradius is
\[
\boxed{R_{m,k}(t)^2=\frac{k(m-k)}m+\frac{[\max\{0,mt-(m-k)\}]^2}{m(m+1)}.}
\tag{1}
\]
The unique optimal center is
\[
\boxed{c_{m,k,t}=\left(\frac{k-u_*}{m}\mathbf1_m,u_*\right),\qquad
u_* =\frac{\max\{0,mt-(m-k)\}}{m+1}.}
\tag{2}
\]
The polytope has precisely two vertex orbits under permutations of its first \(m\) coordinates:

* \(A\): \(\binom mk\) vertices with \(z=0\) and exactly \(k\) ordinary coordinates equal to one;
* \(B\): \(m\binom{m-1}{k-1}\) vertices with \(z=t\), exactly \(k-1\) ordinary coordinates equal to one, one equal to \(1-t\), and all others zero.

For \(0<t<t_0\), the minimum sphere meets precisely the \(A\)-vertices. The \(B\)-vertices lie strictly inside, each by the **squared radial clearance**
\[
\boxed{R_{m,k}(t)^2-\|b-c_{m,k,t}\|^2=2t(t_0-t)>0\qquad (b\in B).}
\tag{3}
\]
At \(t=t_0\), and for all \(t_0<t<1\), **every vertex** lies on the minimum sphere. Thus the number of contacts changes from \(\binom mk\) to \(\binom mk+m\binom{m-1}{k-1}\) at the exact threshold. The squared circumradius is constant for \(t\le t_0\), is continuously differentiable at \(t=t_0\), but has a second-derivative jump of \(2m/(m+1)\) there. In the limit \(t\uparrow1\) it recovers the ordinary hypersimplex circumball radius \(\sqrt{k(m+1-k)/(m+1)}\).

## Assumptions and scope
The quantifiers are universal over integers \(m\ge2\), \(1\le k\le m-1\), and real \(0<t<1\). The affine hull is the hyperplane with coordinate sum \(k\) in \(\mathbb R^{m+1}\), and all distances are ambient Euclidean distances restricted to that hyperplane. The interval endpoints \(t=0\) and \(t=1\) have vertex collisions or dimension changes; limiting formulas are valid, but the two-orbit multiplicities above are asserted only for the open parameter interval.

The minimum enclosing radius is defined as \(\min_{c\in\mathbb R^{m+1}}\max_{x\in Q_{m,k,t}}\|x-c\|\). It is not the intrinsic inradius, the minimum-volume ellipsoid radius, or an affine-invariant notion. The polytope is full-dimensional inside its affine hull because \(0<k<m\) and \(t>0\).

## Proof
**1. Exhaustive vertex description.** The defining box has \(m+1\) pairs of coordinate bounds and one independent sum equality. At a vertex at most one coordinate can be strictly between its two bounds: if two were interior, the perturbations \(\pm\varepsilon(e_i-e_j)\) would remain feasible. Conversely, any feasible point with at most one free coordinate is a vertex because all other box constraints and the sum equality pin it down.

If \(z=0\), the integer sum \(k\) forces all ordinary coordinates to be at bounds, giving orbit \(A\). If \(z=t\), the ordinary sum is the noninteger \(k-t\). Exactly one ordinary coordinate must then be strictly interior, equal to \(1-t\); exactly \(k-1\) are one, giving orbit \(B\). If \(0<z<t\), all ordinary coordinates would be zero or one, forcing \(z=k-j\) for an integer \(j\), impossible in \((0,t)\subset(0,1)\). This exhausts all vertices and proves the counts.

**2. Reduction to one center coordinate.** The squared covering objective
\[
F(c)=\max_{v\in\operatorname{vert}Q_{m,k,t}}\|v-c\|^2
\]
is strictly convex in \(c\): it is \(\|c\|^2\) plus a maximum of affine functions. Its minimizer is unique and must lie in the affine hull, since orthogonal projection strictly reduces squared distances for centers outside it. The full coordinate-permutation group \(S_m\) preserves \(Q_{m,k,t}\), so uniqueness forces the center to have the form
\[
c(u)=\left(\frac{k-u}{m}\mathbf1_m,u\right),\qquad u\in\mathbb R.
\tag{4}
\]
Within each of the two vertex orbits all squared distances to \(c(u)\) coincide. A direct sum of squares yields
\[
D_A(u)=\frac{k(m-k)}m+\frac{m+1}{m}u^2,
\tag{5}
\]
\[
D_B(u)=(k-1)+(1-t)^2-\frac{(k-t)^2}m+\frac{m+1}{m}(u-t)^2.
\tag{6}
\]
Subtracting gives the exact affine difference
\[
\boxed{D_B(u)-D_A(u)=2t\left(t-\frac{m-k}m\right)-\frac{2t(m+1)}m u.}
\tag{7}
\]
Thus minimization over all centers is exactly the minimization over real \(u\) of \(\max\{D_A(u),D_B(u)\}\).

**3. The two phases and equality cases.** If \(t\le t_0\), (7) implies \(D_B(0)\le D_A(0)\). Since \(D_A(u)\ge D_A(0)\) for every \(u\), the minimum is attained uniquely at \(u=0\). The squared radius is \(k(m-k)/m\); inequality is strict for orbit \(B\) whenever \(t<t_0\), and (7) gives the squared clearance (3).

If \(t>t_0\), the two curves cross at
\[
u_c=\frac{mt-(m-k)}{m+1},\qquad 0<u_c<t.
\tag{8}
\]
For \(u<u_c\), \(D_B(u)>D_A(u)\) and \(D_B\) is strictly decreasing until \(u=t\); therefore the maximum decreases as \(u\) approaches \(u_c\) from the left. For \(u>u_c\), \(D_A(u)>D_B(u)\) and \(D_A\) is strictly increasing for \(u>0\). Hence \(u_c\) is the unique global minimizer. Substituting (8) into (5) proves (1)--(2), and equality of (5)--(6) means that every vertex of both orbits contacts the sphere. At \(t=t_0\), (7) gives equality at \(u=0\), so all vertices contact there too.

Alternatively, the optimal center in the second phase is a convex combination of the two orbit centroids with nonnegative coefficients \(1-u_c/t\) and \(u_c/t\); equality of contact distances then supplies the standard minimum-ball optimality certificate without relying on the minimax derivative argument.

**4. Regularity and full-hypersimplex endpoint.** The excess term in (1) is \(\frac{m}{m+1}(t-t_0)_+^2\), whose second derivative jumps from zero to \(2m/(m+1)\) at \(t_0\). At \(t=1\), (1) tends to
\[
\frac{k(m-k)}m+\frac{k^2}{m(m+1)}=\frac{k(m+1-k)}{m+1},
\]
as claimed. All formulae are exact; no finite experiment is used for their universally quantified proof.

## Verification
The standalone `check_capped_hypersimplex_ball.py` uses exact rational arithmetic. Without assuming the two stated vertex orbits, it enumerates vertices by independently choosing all box-bound constraints, solves the residual sum equation, and deduplicates. It then independently minimizes the maximum squared distance of the enumerated vertices: all distance functions have a common quadratic coefficient, so the minimum must occur at one of their stationary points or an intersection of their affine remainders. It compares the resulting center and radius with (1)--(2), verifies all contacts and strict clearances, and supplies a contact-barycenter certificate.

Successful replay: `CAPPED_HYPERSIMPLEX_BALL_CHECKS_PASSED cases=308 enumerated_vertices=24761 contact_vertices=16802 screened_cases=146 boundary_cases=16 full_contact_cases=146`.

These checks cover \(2\le m\le8\), all \(1\le k<m\), and eleven rational truncation parameters. They corroborate but do not replace the analytical proof for all real \(t\in(0,1)\).

## Relationship to prior work
Ferroni and McGinnis (arXiv:2202.11808, first public 2022-02-23) study rectangular-prism hyperplane slices, connect them to generalized permutahedra and polymatroids, and determine lattice-point and volume invariants. Their Section 2 treats thin and fat slices; the investigated arguments do not determine the minimum enclosing Euclidean ball or its contact phase. Here the special-coordinate capacity varies continuously, which need not yield a lattice polytope.

Manecke, Sanyal and So (arXiv:1812.07491, first public 2018-12-18) treat Boolean rank-selected \(S\)-hypersimplices, face structures, and monotone paths. Their objects generally have vertices in \(\{0,1\}^d\), whereas the new \(B\)-vertices have nonintegral coordinate \(1-t\). Their reported combinatorial results do not imply (1) or the exact Euclidean contact threshold.

A separately indexed exact **inradius** theorem for prism slices does not imply the present **circumradius**, which is determined by vertices rather than facet clearances. A separately indexed minimum-sphere theorem for minimal-matroid base polytopes has a related two-orbit optimization method but a different vertex realization and a discrete rank-corank threshold; neither theorem contains the present real-parameter family. The claim is not a corollary of the hypersimplex endpoint: truncation removes one orbit and introduces fractional vertices, changing its metric. These distinctions follow by comparing the actual objects, measures, and quantifiers, not by titles alone.

## Limitations
This formula uses one (not several) shortened coordinate interval, a fixed integer coordinate sum, and the inherited Euclidean metric. It does not address minimum-volume ellipsoids or inballs. A general-purpose minimum-ball theorem could subsume the computational method; an earlier equivalent special-family statement is not ruled out conclusively by the indexed searches. The proof is self-contained, but historical priority requires independent literature review. Source comparisons to other indexed results were limited to available published texts and the descriptions indicated above.

## References
1. S. Manecke, R. Sanyal, J. So, *\(S\)-hypersimplices, pulling triangulations, and monotone paths*, arXiv:1812.07491 (initial release 2018-12-18); *Electronic Journal of Combinatorics* 27(3) (2020), P3.16, DOI 10.37236/8457.
2. L. Ferroni, D. McGinnis, *Lattice points in slices of prisms*, arXiv:2202.11808 (initial release 2022-02-23); *Canadian Journal of Mathematics* 77 (2025), 1013--1040, DOI 10.4153/S0008414X24000233.
