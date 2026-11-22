# Parity rigidity of optimal Euclidean circumspheres in weighted cycle zonotopes

## Finding
For every integer \(n\ge4\) and every positive weight vector \(w=(w_1,\ldots,w_n)\), consider the centered, standard-Euclidean graphical zonotope
\[
Z_n(w)=\sum_{i=1}^n[-w_i/2,w_i/2](e_i-e_{i+1})\subset \mathbf1^\perp\subset\mathbb R^n,\qquad e_{n+1}=e_1.
\]
Set \(T=\sum_i w_i\), and denote by \(R(w)\) the radius of its smallest enclosing Euclidean ball. The unique center is zero, and
\[
4R(w)^2=2\sum_iw_i^2+2\sum_iw_iw_{i+1}-4\mathbf1_{\{n\text{ odd}\}}\min_i(w_iw_{i+1}),\qquad w_{n+1}=w_1.
\]
For even \(n\), exactly two antipodal vertices touch the optimal sphere. For odd \(n\), exactly \(2m\) vertices touch, where \(m\) is the number of cyclic indices attaining \(\min_iw_iw_{i+1}\). Their sign patterns alternate around the cycle, apart from one equal-sign neighboring pair across such a minimum-product edge; the two antipodal choices of each sign pattern are distinct.

With \(T>0\) fixed, the complete equality classification is
\[
\min_{w_i>0,\,\sum_iw_i=T}R(w)^2=
\begin{cases}
T^2/n,&n\text{ even},\\
T^2(n-1)/n^2,&n\text{ odd}.
\end{cases}
\]
When \(n\) is odd, equality holds only at \(w_i=T/n\) for all \(i\). When \(n\) is even, equality holds exactly when \(w_i+w_{i+1}=2T/n\) for every \(i\), equivalently at arbitrary positive alternating weights \(a,b,a,b,\ldots\) satisfying \(a+b=2T/n\). Thus odd cycles are metrically rigid under a fixed generator budget, whereas even cycles possess a one-dimensional family of equally optimal deformations.

For odd \(n\), the rigidity has the explicit quantitative bound
\[
R(w)^2-\frac{T^2(n-1)}{n^2}\ge
\frac{1-(1-2/n)\cos(\pi/n)}2\sum_i\left(w_i-\frac Tn\right)^2.
\]
This is a valid stability bound; no assertion is made that its coefficient is the largest possible constant for the original maximum-radius functional.

## Assumptions and scope
The ambient metric is the Euclidean metric of \(\mathbb R^n\) restricted to \(\mathbf1^\perp\), not an arbitrary affine-invariant metric. Edge generator lengths are \(\sqrt2w_i\); fixing \(T\) therefore fixes their total Euclidean length up to the common factor \(\sqrt2\). All \(w_i\) are strictly positive and \(n\ge4\); degenerate boundary weights and arbitrary non-zonotopal changes of realization are not included. Positive edge rescalings represent the full relative interior of the deformation cone of the cycle graphical zonotope, modulo translations, by the triangle-free deformation theorem of Padrol--Pilaud--Poullot. The metric assertions here are proved independently of that deformation classification.

## Proof
**Unique center.** The zonotope is centrally symmetric about zero. Write \(R_0=\max_{x\in Z_n(w)}\|x\|\). A ball with arbitrary center \(c\) containing the zonotope must contain \(x\) and \(-x\) for a point \(x\) attaining \(R_0\). The identity
\[
\frac{\|x-c\|^2+\|-x-c\|^2}{2}=R_0^2+\|c\|^2
\]
shows that any center \(c\ne0\) requires strictly greater radius. Thus \(c=0\) is the unique optimal center and \(R(w)=R_0\).

**Signed-cycle reduction.** The norm is convex, so its maximum on the image of the cube \([-1,1]^n\) is reached at a sign vector \(s\in\{-1,1\}^n\). The corresponding point is
\[
v_s=\frac12\sum_i s_iw_i(e_i-e_{i+1}),\qquad
4\|v_s\|^2=\sum_i(s_iw_i-s_{i-1}w_{i-1})^2
=2\sum_iw_i^2-2\sum_iw_iw_{i+1}s_is_{i+1}.
\]
Every product \(s_is_{i+1}\) is \(\pm1\), and the product of all such products is \(1\). If \(n\) is even, all may be negative, and the two alternating sign vectors are the only maximizers because all weights are positive. If \(n\) is odd, an odd number of neighboring sign products must be positive. The maximum has exactly one positive bond product, at an index minimizing \(w_iw_{i+1}\), because each additional positive product strictly lowers the value. There are two sign vectors for each chosen bond; their signs are nonconstant and hence expose genuine, distinct zonotope vertices (the only sign choices that are not vertices of a simple cycle zonotope are the two consistently cyclic orientations). The formula and the contact count follow.

**Even cycle optimum.** For even \(n\), rewrite the formula as
\[
4R(w)^2=\sum_i(w_i+w_{i+1})^2\ge \frac1n\left(2\sum_iw_i\right)^2=\frac{4T^2}{n}.
\]
Equality in Cauchy--Schwarz holds precisely when all neighbor sums equal \(2T/n\). Solving those cyclic equations for even \(n\) gives the positive alternating family stated above.

**Odd cycle optimum and stability.** Let \(s^{(j)}\), for cyclic indices \(j\), be the \(n\) sign patterns up to global negation that have precisely one equal-sign bond, at bond \(j\). Let \(Q_j(w)=\|v_{s^{(j)}}\|^2\). Averaging the \(n\) quadratic forms (each neighboring bond is the exceptional one exactly once) gives
\[
R(w)^2\ge H(w):=\frac1n\sum_jQ_j(w)
=\frac12\sum_iw_i^2+\frac12\left(1-\frac2n\right)\sum_iw_iw_{i+1}.
\]
For \(u_i=T/n\), all \(Q_j(u)\) are equal to \(T^2(n-1)/n^2\), so \(R(u)^2=H(u)\). With \(\delta_i=w_i-u_i\) and \(\sum_i\delta_i=0\), the linear terms cancel:
\[
H(w)-H(u)=\frac12\sum_i\delta_i^2+\frac12\left(1-\frac2n\right)\sum_i\delta_i\delta_{i+1}.
\]
The real symmetric cyclic-neighbor quadratic form has eigenvalues \(\cos(2\pi k/n)\), for \(k=0,\ldots,n-1\), relative to the Euclidean norm. For odd \(n\), its least eigenvalue is \(-\cos(\pi/n)\). Therefore
\[
H(w)-H(u)\ge\frac{1-(1-2/n)\cos(\pi/n)}2\|\delta\|_2^2.
\]
The coefficient is strictly positive. Since \(R(w)^2\ge H(w)\) and \(R(u)^2=H(u)\), this proves the strict uniqueness and stability assertion.

## Verification
Run `python3 check_weighted_cycle.py` using the Python standard library. It enumerates all sign choices for all \(3^n\) weight vectors with weights in \(\{1,2,3\}\) for \(4\le n\le7\), as well as deterministic larger random cases through \(n=11\). It verifies the closed squared-radius expression and the full set of farthest sign vectors, plus fixed-budget equality/strict examples. The reproduced output is `WEIGHTED_CYCLE_OUTER_EXACT_PASS 3360`. These finite checks corroborate the formula; the all-dimensional result and stability follow from the proof above.

## Relationship to prior work
Padrol, Pilaud and Poullot established that the deformation cone of a triangle-free graphical zonotope is simplicial and, up to translation, every deformation is an edge-rescaled zonotope; their Example 2.9 treats the four-cycle and Corollary 2.11 identifies the full cone. This supplies the natural deformation family, not its Euclidean circumsphere optimality or equality classification. Pešović and Stojadinović investigate the combinatorial and enumerative passage from graphical zonotopes to graph associahedra, rather than fixed-length Euclidean extremizers. Winter's classification of vertex-transitive and homogeneous zonotopes addresses different metrical rigidity assumptions (all vertices cospherical and all edge lengths equal), not optimization over positive edge rescalings. Unit-weight cycle radii and their antipodal contact patterns are treated as pre-existing special cases, not separately claimed as novel; the contribution is the complete all-positive-weight contact law and, especially, the fixed-budget parity rigidity and stability.

## Limitations
The proof is confined to the specified Euclidean realization, to strictly positive edge coefficients and to the cycle graph. It does not classify circumradius minimizers on general graph deformation cones or the boundary of the cycle cone. It does not prove global historical priority; broad metric classifications or independent unindexed weighted-cycle analyses could subsume some assertions. The quantitative odd-cycle stability constant is guaranteed but is not proved to be globally best possible for \(R(w)^2\).

## References
1. A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, first posted 2021-11-24; *Discrete & Computational Geometry* 73 (2025), 447--465, DOI: https://doi.org/10.1007/s00454-023-00586-x. Particularly Example 2.9 and Corollary 2.11.
2. M. Pešović, T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053, first posted 2022-09-24; *Turkish Journal of Mathematics* 47 (2023), 1362--1373, DOI: https://doi.org/10.55730/1300-0098.3434.
3. M. Winter, *Classification of vertex-transitive zonotopes*, arXiv:1912.10469, first posted 2019-12-22; *Discrete & Computational Geometry* 66 (2021), 1446--1462, DOI: https://doi.org/10.1007/s00454-021-00303-6.
