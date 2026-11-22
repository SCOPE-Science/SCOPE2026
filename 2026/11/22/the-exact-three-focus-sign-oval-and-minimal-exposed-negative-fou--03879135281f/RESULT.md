# The exact three-focus sign oval and minimal exposed-negative four-point microscopic weighting

## Finding
Let \(a_1,a_2,a_3\) be three noncollinear points of the Euclidean plane. Let \(v=(v_1,v_2,v_3)\) and \(\lambda\) be the unique solution of
\[
 \sum_{j=1}^3 \|a_i-a_j\|v_j=\lambda\quad(i=1,2,3),
 \qquad \sum_{j=1}^3v_j=1.
\]
Every \(v_i\) is strictly positive. Set
\[
 \Phi(y)=\sum_{i=1}^3v_i\|y-a_i\|,
 \qquad \Omega=\{y\in\mathbb R^2:\Phi(y)<\lambda\}.
\]
For every \(y\notin\{a_1,a_2,a_3\}\), the normalized microscopic weighting on the four-site Euclidean metric space \(\{a_1,a_2,a_3,y\}\) has weight at \(y\) that is negative, zero, or positive according as \(\Phi(y)\) is less than, equal to, or greater than \(\lambda\). Its exact weight is given below in terms of the unique zero-sum solution of a three-by-three linear system.

The set \(\Omega\) is bounded, open, nonempty and strictly convex. Its boundary is a strictly convex Jordan curve, smooth and real analytic except possibly at the three triangle vertices, which lie on that boundary. The entire open triangle and every relative interior of a triangle edge lie in \(\Omega\), and \(\Omega\) extends beyond all three edges. Thus points \(y\) at an **exposed vertex** of the four-site convex hull may have **negative** microscopic mass. Four is the smallest cardinality of a Euclidean planar point set admitting a negative microscopic weight at an exposed vertex.

For example, put \(a_1=(0,0)\), \(a_2=(2,0)\), \(a_3=(1,\sqrt3)\), \(y=(1,-1/10)\). These four points are the vertices of a strictly convex quadrilateral; the microscopic weight of \(y\) is negative.

## Assumptions and scope
All distances are ordinary Euclidean distances, not squared distances. The points are distinct; in the four-point theorem the original three foci are noncollinear. The microscopic weighting is the mass-one gauging of the distance matrix, which equals the small-scale microscopic weighting for finite Euclidean metric spaces by Roff and Willerton [1]. Signed coefficients are allowed. Boundary points of \(\Omega\) coinciding with an original focus are **not** four-distinct-site configurations and are not assigned four-site weights.

Write \(D=(\|a_i-a_j\|)_{i,j=1}^3\), \(r_i=\|y-a_i\|\), and \(\mathbf1=(1,1,1)^{\mathsf T}\). Let \(q\) be the unique vector satisfying
\[
 Dq+r=\Phi(y)\mathbf1,\qquad \mathbf1^{\mathsf T}q=0.
\]
Then
\[
 Q(y)=2\Phi(y)-\lambda-r^{\mathsf T}q>0,
 \qquad \boxed{\widehat w_y=\frac{\Phi(y)-\lambda}{Q(y)}}.
\]
This is an exact inverse sign formula valid for every fourth location other than the three original sites, including locations outside the original triangle.

## Proof
**1. Positive three-site masses.** Put \(d_{ij}=\|a_i-a_j\|\) and define the three strict triangle-inequality limbs
\[
 \ell_1=\frac{d_{12}+d_{13}-d_{23}}2,\quad
 \ell_2=\frac{d_{12}+d_{23}-d_{13}}2,\quad
 \ell_3=\frac{d_{13}+d_{23}-d_{12}}2.
\]
All are positive, and \(d_{ij}=\ell_i+\ell_j\). Setting \(T=\sum_i\ell_i^{-1}\) gives
\[
 v_i=\frac12\left(1-\frac1{T\ell_i}\right)>0,
 \qquad \lambda=\frac12\left(\sum_i\ell_i-\frac1T\right)>0.
\]
The displayed vector sums to one and satisfies \(Dv=\lambda\mathbf1\). Uniqueness follows because \(D\) is strictly negative definite on the subspace of vectors summing to zero (Step 2). In particular, \(\Phi(a_i)=\lambda\) for all three foci.

**2. A strict conditional-negative-definiteness fact.** For any distinct planar points \(z_1,\ldots,z_m\) and any nonzero real \(c=(c_i)\) with \(\sum c_i=0\),
\[
 \sum_{i,j}c_ic_j\|z_i-z_j\|<0.
\]
One direct proof uses the standard Fourier integral representation of Euclidean distance: for a positive absolute constant \(C\),
\[
 \sum_{i,j}c_ic_j\|z_i-z_j\|
 =-C\int_{\mathbb R^2}\frac{|\sum_jc_je^{\mathrm i\xi\cdot z_j}|^2}{\|\xi\|^3}\,d\xi.
\]
The integral converges near the origin because \(\sum c_i=0\), and at infinity by boundedness. It is strictly positive before the minus sign: distinct-site exponentials are linearly independent, so their nonzero finite sum cannot vanish almost everywhere. This also proves strict concavity and uniqueness of mass-one distance-energy maximizers in the two configurations.

**3. Exact added-site mass.** The equation \(Dq+r=\Phi\mathbf1\) has a unique zero-sum solution: for the negative-definite restriction of \(D\) to the zero-sum subspace, the associated bilinear form uniquely solves the projected equation; compatibility of its scalar constant follows by pairing with \(v\), because \(v^{\mathsf T}Dq=\lambda\mathbf1^{\mathsf T}q=0\). The constant must be \(v^{\mathsf T}r=\Phi\).

Let \(\widetilde D\) be the four-by-four distance matrix. On the affine hyperplane of total mass one, fix the fourth mass to \(t\). Strict concavity on the three-site zero-sum subspace makes the maximizing first three masses uniquely
\[
 u(t)=(1-t)v+tq.
\]
Indeed \(Du(t)+tr=[(1-t)\lambda+t\Phi]\mathbf1\), the first-order optimality condition. The full mass-one energy of \((u(t),t)\) is therefore exactly
\[
 E(t)=\lambda+2(\Phi-\lambda)t-Q(y)t^2,
\]
where \(Q(y)=2\Phi-\lambda-r^{\mathsf T}q\). To check its strict positivity, set \(h=(q-v,1)\). Since \(\mathbf1^{\mathsf T}h=0\), \(h\ne0\) and all four sites are distinct, Step 2 gives
\[
 -h^{\mathsf T}\widetilde D h=Q(y)>0.
\]
Thus the unique global mass-one maximizer has \(t=(\Phi-\lambda)/Q(y)\). By the finite-Euclidean existence/identification theorem of [1], this maximizing signed mass-one vector is the microscopic weighting. Its fourth-coordinate sign is therefore exactly the sign of \(\Phi-\lambda\), with no asymptotic or numerical qualification.

**4. Geometry of the sign region.** The function \(\Phi\) is continuous and coercive because its coefficients are positive and sum to one. It is strictly convex: for distinct \(x,z\), equality in every weighted Euclidean triangle inequality along their connecting segment would require each focus \(a_i\) to lie on the line through \(x,z\); three noncollinear foci prevent that. Since \(\Phi(a_i)=\lambda\), strict convexity shows \(\Phi<\lambda\) on the interior of their triangle and on each open edge. Consequently the bounded sublevel \(\Omega\) is nonempty, open, strictly convex and contains an open ball crossing each edge to the exterior. Its compact convex closure has nonempty interior and boundary a Jordan curve with no straight segments. Away from the foci, \(\Phi\) is real analytic; its gradient cannot vanish on level \(\lambda\), since a vanishing gradient would identify the unique global minimum, which lies strictly below \(\lambda\). The implicit-function theorem gives the asserted smoothness away from the three foci.

**5. Explicit exposed negative weight and sharp cardinality.** For the equilateral example, \(v=(1/3,1/3,1/3)\), \(\lambda=4/3\), and
\[
 3\Phi(y)=\frac{\sqrt{101}}5+\sqrt3+\frac1{10}<4.
\]
The inequality is rigorous, for instance using \(\sqrt{101}<101/10\) and \(\sqrt3<7/4\), giving \(3\Phi<387/100<4\). The point \(y=(1,-1/10)\) lies strictly below the base segment, with horizontal coordinate in its relative interior, so all four listed points are exposed vertices. Step 3 gives \(\widehat w_y<0\).

For cardinality one, the mass is one; for cardinality two, each mass is \(1/2\). For three noncollinear points, Step 1 gives all masses positive. For three distinct collinear points, the two extreme points have masses \(1/2\) each and the middle point has mass zero, by direct substitution into the gauging equations (and uniqueness from Step 2). Therefore no smaller Euclidean configuration has a negative microscopic mass at any point, exposed or otherwise. Four is sharp.

## Verification
The independent program `verify.py` solves the normalized gauging equations directly, separately computes the three-site potential and Schur-complement expression for \(\widehat w_y\), checks the explicit four-exposed-vertex witness, and checks randomly generated nondegenerate triangles and fourth points. It also verifies negative sign on sampled open edges. Running with Python 3 standard library prints `PASS`. These finite floating-point tests are consistency checks only; Steps 1–5 establish the statements for all configurations.

## Relationship to prior work
Roff and Willerton [1] introduce microscopic weighting, establish its existence on Euclidean finite sets and identify it as the signed distance-energy maximizer. Their general results furnish the well-defined analytic starting point but neither locate the negative mass region of a moving fourth site around an arbitrary fixed triangle nor supply a minimal convex-position exposed-negative example. The Schoenberg polytope interpretation in their Section 5 describes signs abstractly through circumcenter barycentric coordinates; the present result converts that criterion into an exact three-focus Euclidean-plane oval.

A published result on two staggered regular polygons [2] exhibits negative microscopic weights at exposed vertices with \(2n\ge8\) points. Its special multi-polygon geometry and lower bound on its number of sites do not imply the four-site minimum or the sign-oval classification. Related central-attachment constructions for symmetric or spherical rims place the negative site in the interior of the convex hull, rather than at an exposed vertex.

The generalized ellipse \(\sum_i v_i\|y-a_i\|=\lambda\) and its convexity are familiar tools of Euclidean geometry; **not** claimed as newly invented curves. The new claim is their exact identification with the four-site microscopic-weight sign locus, the universal strict curvature-free topological description, and the sharp four-site exposed-negative phenomenon.

## Limitations
The theorem concerns the weight of the *new* site relative to a fixed noncollinear triple. It does not classify simultaneous signs of all four masses across all labeled quadrilaterals, non-Euclidean metrics, or collisions of sites. The threshold relation uses exactly ordinary Euclidean distance; it need not hold with squared distance. No priority claim is made against all unindexed historical work on finite distance-energy maximizers, and no external independent mathematical audit has been performed.

## References
[1] E. Roff and S. Willerton, *The microscopic weighting on a metric space*, arXiv:2607.05349 (first public version, 6 July 2026; revised 4 November 2026), https://arxiv.org/abs/2607.05349 . In particular Sections 2, 4, 5.

[2] *Negative microscopic weights at exposed vertices of staggered regular polygons*, publicly indexed 1 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-negative-microscopic-weights-at-exposed-vertices-of-staggered-re--9ce6bbdc7f59 .
