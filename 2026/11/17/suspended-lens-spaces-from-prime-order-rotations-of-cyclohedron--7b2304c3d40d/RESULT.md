# Suspended lens spaces from prime-order rotations of cyclohedron boundaries

## Finding

For an integer \(n\ge 5\), let \(C_n\) be the cycle with vertices \(\mathbb Z/n\mathbb Z\). Let \(P_n\) be its graph-associahedron in the canonical coordinate realization described below. Let \(p\ge5\) be an odd prime dividing \(n\), put \(k=n/p\), and let \(H_{n,p}=\langle\rho^k\rangle\cong C_p\), where \(\rho\) cyclically shifts the vertex labels. Set \(X_{n,p}=\partial P_n/H_{n,p}\), an ordinary **geometric** orbit space.

**Theorem.** Let \(L_{p,k}\) denote the generalized lens space of dimension \(k(p-1)-1\) with weights \(1,2,\ldots,(p-1)/2\), each repeated exactly \(k\) times. There is a homeomorphism

\[
X_{n,p}\ \cong\ \Sigma^{k-1} L_{p,k},
\]

where \(\Sigma\) is **unreduced** suspension and \(\Sigma^0\) is the identity. In particular, the complete integral homology is

\[
H_j(X_{n,p};\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=0\text{ or }j=n-2,\\
\mathbb Z/p\mathbb Z,&j=k,k+2,\ldots,n-4,\\
0,&\text{otherwise}.
\end{cases}
\]

Moreover, \(X_{n,p}\) is \((k-1)\)-connected (interpreted as connected when \(k=1\)) and its first nontrivial homotopy group is

\[
\pi_k(X_{n,p})\cong\mathbb Z/p\mathbb Z.
\]

Thus a natural prime-order quotient of a simplicial sphere can create integral torsion in an unbounded collection of dimensions, including a prescribed first nonzero homotopy degree.

## Assumptions and scope

A *tube* is a nonempty subset \(I\subseteq\mathbb Z/n\mathbb Z\) whose induced subgraph in \(C_n\) is connected. Include the full vertex set. Define the coordinate simplex \(\Delta_I=\operatorname{conv}\{e_i:i\in I\}\subseteq\mathbb R^n\) and the invariant Minkowski sum

\[
P_n=\sum_{I\text{ a tube of }C_n}\Delta_I.
\]

This is the standard graph-associahedral realization of a cyclohedron: it is a full-dimensional convex polytope in an affine hyperplane of dimension \(n-1\), with faces indexed by compatible tubings. The action is the **specified** cyclic coordinate action, not an arbitrary homeomorphism of the abstract cyclohedron. The quotient is of the boundary, not of the (contractible) solid polytope and not of an associated toric variety. No claim is made for composite-order rotation subgroups or for \(p=2,3\).

Write a generalized lens space as \(L(p;q_1,\ldots,q_m)=S^{2m-1}/C_p\), for the free action

\[
(z_1,\ldots,z_m)\longmapsto
(e^{2\pi i q_1/p}z_1,\ldots,e^{2\pi i q_m/p}z_m),
\]

where every weight is a unit modulo \(p\). This fixes the conventions for the claimed homeomorphism, not just its homotopy class.

## Proof

**1. A canonical equivariant sphere.** Every \(\Delta_I\) lies in the affine hyperplane of coordinate sum one, so \(P_n\) lies in the hyperplane \(\sum_i x_i=|\mathcal B_n|\), where \(\mathcal B_n\) is the family of tubes. It contains a translate of the full simplex \(\Delta_{\mathbb Z/n\mathbb Z}\), hence is full-dimensional in that hyperplane. It is invariant under the cyclic shift \(\rho\), because shifts permute the tube summands.

The sum of the barycenters of all summand simplices is a point \(c\in P_n\), fixed by every cyclic shift. It is interior: the barycenter of the full simplex is interior in the affine hyperplane and adding a point from each remaining summand gives an interior point of the total Minkowski sum. The only cyclically fixed point of this affine hyperplane is its constant-coordinate point, so \(c\) is the unique such point. Translation by \(c\) identifies its direction space with

\[
V_n=\{(x_i)\in\mathbb R^n:\sum_i x_i=0\}.
\]

For each direction in the unit sphere \(S(V_n)\), its ray from \(c\) meets \(\partial P_n\) at one point, continuously in the direction, by compact convexity and the interior condition. Therefore radial projection

\[
\partial P_n\longrightarrow S(V_n),\qquad
x\longmapsto\frac{x-c}{\|x-c\|}
\]

is a homeomorphism, and it commutes with the entire cyclic coordinate action. In particular it descends to a homeomorphism of orbit spaces by \(H_{n,p}\).

**2. Exact real representation.** The rotation \(\rho^k\) partitions the \(n=kp\) coordinates into exactly \(k\) disjoint orbits of size \(p\). Thus as a real \(C_p\)-module the coordinate representation is the direct sum of \(k\) regular representations. Removing the single all-ones line gives

\[
V_n\cong\mathbb R^{k-1}_{\mathrm{triv}}\oplus
\bigoplus_{a=1}^{(p-1)/2}(\mathbb C_a)^{\oplus k},
\]

where \(\mathbb C_a\) is the real two-plane underlying a complex line on which \(\rho^k\) acts by multiplication by \(e^{2\pi i a/p}\). The decomposition is orthogonal after choosing invariant inner products. A nonidentity element of \(C_p\) has no nonzero fixed vector in the moving part because \(p\) is prime and all its weights are coprime to \(p\).

**3. Sphere joins and orbit spaces.** The unit sphere of an orthogonal direct sum is the spherical join of the unit spheres of its summands. When \(k\ge2\), quotienting by a group acting trivially on the first factor yields

\[
S(V_n)/C_p\ \cong\ S^{k-2}*
\big(S^{k(p-1)-1}/C_p\big)
\ \cong\ \Sigma^{k-1}L_{p,k}.
\]

The middle quotient is precisely the lens space with the weights stated in the theorem. For \(k=1\), the trivial summand is zero, and directly \(S(V_p)/C_p\cong L_{p,1}\). Combining these homeomorphisms with Step 1 proves the topological classification.

**4. Integral homology and first homotopy.** The lens space \(L_{p,k}\) has one cell in every degree from zero through \(k(p-1)-1\). In the standard periodic cellular calculation, the positive even-dimensional integral boundary maps are multiplication by \(p\), while the odd-dimensional ones are zero. (Equivalently, start from the periodic \(\mathbb Z[C_p]\)-resolution with the norm and \(g-1\) maps and tensor with the trivial integral module; the nonzero unit weights leave this calculation unchanged.) Consequently the integral homology of \(L_{p,k}\) is \(\mathbb Z\) in degree zero and its top degree, is \(\mathbb Z/p\mathbb Z\) in odd degrees strictly between them, and vanishes elsewhere.

An unreduced suspension of a connected space shifts positive-degree reduced homology up by one. Repeating \(k-1\) times gives the displayed homology groups, since the first positive odd lens degree is one and the last is \(k(p-1)-3\). The shifted torsion degrees are therefore \(k,k+2,\ldots,kp-4=n-4\), and the top free degree is \(kp-2=n-2\).

If \(k=1\), the lens space has simply connected sphere as universal cover (dimension \(p-2\ge3\)), so its fundamental group is exactly \(C_p\). If \(k\ge2\), \(\Sigma^{k-1}L_{p,k}\) is \((k-1)\)-connected; the Hurewicz theorem therefore gives \(\pi_k\cong H_k\cong\mathbb Z/p\mathbb Z\). These statements prove the homotopy assertion. \(\square\)

## Verification

The independent finite checker `verify_cyclohedron.py` constructs the dual simplicial boundary by enumerating all compatible tube collections. For \(n=5\), it finds \((20,90,140,70)\) nonempty faces by dimensions zero through three and obtains the rotation quotient chain dimensions \((4,18,28,14)\). It constructs oriented quotient boundary operators and verifies all products of consecutive operators vanish. Over \(\mathbb F_5\) the Betti numbers are \((1,1,1,1)\), while over \(\mathbb F_2,\mathbb F_3,\mathbb F_7\) they are \((1,0,0,1)\), in agreement with an order-five lens space. The \(n=7\) face numbers and the character decompositions for additional prime divisors are also checked.

The verifier is corroborative, not a proof for arbitrary sizes. The complete infinite-family proof is the convex-equivariant radial argument followed by the exact representation decomposition and classical lens-space cellular calculation.

## Relationship to prior work

Carr and Devadoss establish the convex graph-associahedron and its tubing face poset, with the cycle graph giving the cyclohedron. Postnikov establishes the cyclic-interval Minkowski-sum realization used here. Lambrechts, Turchin, and Volić study cyclohedra as compactified configuration spaces and certain projections. These are the foundational ingredients, **not** parts of the new claim. The present claim concerns the full geometric boundary quotient by every prime-order rotation subgroup when \(p\ge5\), identifies its specific lens-space suspension homeomorphism, and calculates integral homology and first nonzero homotopy groups. None of the inspected primary source statements supplies this classification.

A radial sphere homeomorphism for an invariant convex body, the real regular representation decomposition, and the homology of a lens space are individually standard. Their combination makes the result concise; the mathematical content asserted here is the natural uniform cyclohedral quotient classification and its explicitly located torsion. A future discovery of the same combined assertion in prior literature would supersede any originality claim.

## Limitations

The theorem uses the explicit positive unweighted Minkowski realization of the graph-associahedron and its coordinate-label rotation action. It does not assert that arbitrary topological actions with the same abstract combinatorial action are equivalent. It does not describe composite-order rotation quotient spaces, arbitrary subgroup quotients, ring structure, Reidemeister torsion, or equivariant stable homotopy. The exact first public date of any still earlier unlocated source is not known. Independent proof validation and definitive publication-priority assessment have not been performed.

## References

1. M. Carr and S. L. Devadoss, *Coxeter Complexes and Graph-Associahedra*, arXiv:math/0407229, first submitted 2004-07-13; especially Section 2 and Theorem 2.6. https://arxiv.org/abs/math/0407229
2. A. Postnikov, *Permutohedra, associahedra, and beyond*, arXiv:math/0507163, first submitted 2005-07-07; especially Sections 6–8, including the cyclic-interval building set. https://arxiv.org/abs/math/0507163
3. P. Lambrechts, V. Turchin, and I. Volić, *Associahedron, cyclohedron, and permutohedron as compactifications of configuration spaces*, arXiv:math/0612591, first submitted 2006-12-20; especially Sections 1, 2, 4, and 5. https://arxiv.org/abs/math/0612591
