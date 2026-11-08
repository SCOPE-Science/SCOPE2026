# Exact intrinsic covariance and a five-leaf inertia transition for complete-bipartite graphical zonotopes

## Finding
For every integer \(q\ge3\), the uniform-intrinsic-volume covariance matrix of the centered graphical zonotope of \(K_{2,q}\) is exactly
\[
\operatorname{Cov}(X_q)=\frac{2q-1}{6q}\sum_{j=1}^{q}c_jc_j^{\mathsf T}
+\frac{q(q+1)}{48}dd^{\mathsf T},
\qquad c_j=\frac{e_A+e_B}{2}-e_j,\quad d=e_A-e_B.
\]
Its three intrinsic eigenvalue classes, with multiplicities, are
\[
\frac{2q-1}{6q}\quad(q-1),\qquad
\frac{(2q-1)(q+2)}{12q}\quad(1),\qquad
\frac{q(q+1)}{24}\quad(1).
\]
The unique principal-inertia direction is the aggregate leaf-versus-hubs direction for \(q=3,4\), but the hub-difference direction for every \(q\ge5\). The exact threshold is five leaves. The intrinsic volume and centroidal mean squared radius are, respectively,
\[
\operatorname{Vol}_{q+1}(Z_q)=q2^{q-1}\sqrt{q+2},\qquad
\mathbb E\|X_q\|_2^2=\frac{q^2+13q-6}{24}.
\]
With the convention \(L(Z)^2=(\det\operatorname{Cov}(X)/\operatorname{Vol}(Z)^2)^{1/\dim Z}\), the affine-invariant squared isotropic constant is
\[
L(Z_q)^2=\left[\left(\frac{2q-1}{6q}\right)^q\frac{q+1}{48q4^{q-1}}\right]^{1/(q+1)}.
\]

## Assumptions and scope
The graph \(K_{2,q}\) has two labelled left vertices \(A,B\) and labelled right vertices \(1,\ldots,q\). All edges have weight one. In the standard coordinate vectors of \(\mathbb R^{q+2}\), let
\[
Z_q=\sum_{j=1}^q\left[-\tfrac12(e_A-e_j),\tfrac12(e_A-e_j)\right]
+\sum_{j=1}^q\left[-\tfrac12(e_B-e_j),\tfrac12(e_B-e_j)\right].
\]
This polytope lies full-dimensionally in the zero-sum hyperplane \(H=\{x:\sum_vx_v=0\}\), which carries the *inherited Euclidean metric*. The random vector \(X_q\) has uniform \((q+1)\)-dimensional Euclidean-volume distribution on this polytope; it is **not** obtained by independently sampling the edge coefficients. The endpoint \(q=2\), a single four-cycle, also satisfies the formulas and is used as a boundary check, but the substantive non-cactus family begins at \(q=3\).

## Proof
**1. An exact non-overlapping fiber representation.** Let the edge-segment coefficients for \(A-j\) and \(B-j\) be \(a_j,b_j\in[-1/2,1/2]\). Set \(t_j=a_j+b_j\) and \(s=\frac12\sum_j(a_j-b_j)\). Then the edge sum is
\[
X=\sum_jt_jc_j+sd.
\]
For fixed \(t_j\in[-1,1]\), the parameter \(a_j-b_j\) independently ranges over \([-(1-|t_j|),1-|t_j|]\). Thus, writing \(W(t)=q-\sum_j|t_j|\), the *entire polytope*, with no multiplicity of representation, is the linear image of
\[
D_q=\bigl\{(t,s):t\in[-1,1]^q,\ |s|\le W(t)/2\bigr\}.
\]
The \(q+1\) vectors \(c_1,\ldots,c_q,d\) are linearly independent, so this is a genuine one-to-one Euclidean-volume parametrization. They obey \(c_i\cdot c_j=\delta_{ij}+1/2\), \(d\cdot c_j=0\), and \(\|d\|^2=2\). The Gram determinant is \(q+2\); hence the Jacobian is \(\sqrt{q+2}\).

**2. Uniform-volume moments.** If \(T_j\) are independent uniform variables on \([-1,1]\), then \(1-|T_j|\) are independent uniform variables on \([0,1]\). Consequently
\[
\mathbb E_0 W=q/2,\qquad \mathbb E_0 W^3=q^2(q+1)/8,
\qquad \mathbb E_0(T_j^2W)=(2q-1)/12,
\]
where \(\mathbb E_0\) averages over the parameter cube. Integrating the fibers gives \(\int_{[-1,1]^q}W(t)\,dt=q2^{q-1}\). Uniform volume on \(Z_q\) therefore has \(t\)-density proportional to \(W(t)\) and, conditional on \(t\), the coordinate \(s\) is uniform on \([-W(t)/2,W(t)/2]\). Independent sign symmetries give \(\mathbb E t_j=0\), \(\mathbb E(t_it_j)=0\) for distinct indices, and \(\mathbb E(st_j)=0\). Moreover
\[
\mathbb E(t_j^2)=\frac{(2q-1)/12}{q/2}=\frac{2q-1}{6q},\qquad
\mathbb E(s^2)=\frac{\mathbb E_0 W^3}{12\mathbb E_0W}=\frac{q(q+1)}{48}.
\]
The displayed covariance and volume formulas follow. This also proves the origin is the centroid.

**3. Orthogonal decomposition and the transition.** The leaf-contrast subspace \(\{\sum_jv_jc_j:\sum_jv_j=0\}\) has dimension \(q-1\) and the first listed eigenvalue because the Gram matrix of the \(c_j\) is \(I+J/2\). The aggregate direction \(\sum_jc_j\) has eigenvalue \((2q-1)(q+2)/(12q)\); the orthogonal hub-difference direction \(d\) has eigenvalue \(q(q+1)/24\). For \(q\ge3\), the leaf-contrast eigenvalue is strictly below both scalar eigenvalues. The difference of the latter two has the same sign as
\[
P(q)=q^3-3q^2-6q+4.
\]
Since \(P(4)=-4\), \(P(5)=24\), and \(P'(x)>0\) for \(x\ge4\), there is a unique integer changeover, between four and five leaves. Both principal eigenspaces are one-dimensional; hence the principal direction is unique up to sign.

**4. Trace and affine invariant.** Summing the three eigenvalue classes yields the claimed squared radius. The intrinsic determinant is
\[
\det_H\operatorname{Cov}(X_q)
=\left(\frac{2q-1}{6q}\right)^q\frac{q(q+1)(q+2)}{48}.
\]
Combining this with the squared volume gives the isotropic-constant formula.

## Verification
The analytic proof applies to every integer \(q\ge3\). A separate executable checker uses a different representation: it enumerates edge-box images and triangulates the resulting convex hull to integrate volume and second moments for \(q=2,3,4\). The resulting volume relative errors are below \(6\times10^{-11}\), and the largest covariance-entry discrepancies are below \(2\times10^{-11}\). For \(q=5,8,15\), independent fixed-seed rejection sampling from the exact fiber density checks the predicted moments. Run `python verify_k2q.py` in an environment with NumPy and SciPy. The expected success marker is `K2Q_VOLUME_COVARIANCE_CHECKS_PASSED`. Finite checks do not replace the general proof.

## Relationship to prior work
Padrol, Pilaud and Poullot develop graphical-zonotope realizations and deformation cones; their paper identifies the standard edge-segment construction and its graphic-matroid combinatorics, but not the uniform-volume covariance tensor. Pešović and Stojadinović study a family between graphical zonotopes and graph-associahedra using weighted lattice-point enumerators, not the stated intrinsic covariance. Previously known Euclidean inradius, Löwner-ellipsoid, and circumradius results for related graphical zonotopes concern different optimization measures: an enclosing ellipsoid's shape does **not** determine the inertia tensor under uniform interior volume. For a single cycle, a separate cactus covariance formula applies, but \(K_{2,q}\) with \(q\ge3\) contains overlapping cycles and is not a cactus. The present result is a genuine overlapping-cycle metric computation.

## Limitations
Historical originality remains provisional: a result phrased as the uniform moment tensor of the associated box projection or as its isotropic position might be equivalent without mentioning graphical zonotopes. The formula concerns the precisely normalized *centered unit-edge* realization and intrinsic volume distribution; rescaling edges independently changes the result. The covariance does not itself identify the John or Löwner ellipsoid, and the sampling program supplies only finite corroboration. No independent mathematical audit has yet been performed.

## References
1. A. Padrol, V. Pilaud and G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422v1 (public 2021-11-24); full accessible text: https://arxiv.org/html/2111.12422v2.
2. M. Pešović and T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053v1 (public 2022-09-24); full accessible manuscript: https://www.researchgate.net/publication/363858831_Between_graphical_zonotope_and_graph-associahedron.
