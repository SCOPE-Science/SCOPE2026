# Prime rotational quotients of associahedral spheres are weighted lens spaces

## Finding
For an odd prime \(p\ge5\), let \(\mathcal A_p\) be the simplicial complex whose vertices are the diagonals of a convex regular \(p\)-gon and whose faces are the families of pairwise noncrossing diagonals. The cyclic group \(C_p\) acts by rotating the polygon by one vertex. With the convention that \(L(p;q_1,\ldots,q_r)\) is the quotient of \(S^{2r-1}\subset\mathbb C^r\) by the simultaneous multiplications \(z_j\mapsto e^{2\pi i q_j/p}z_j\), there is a homeomorphism
\[
|\mathcal A_p|/C_p\ \cong\ L\bigl(p;2,3,\ldots,(p-1)/2\bigr).
\]
The action on the covering sphere is free. For \(p\ge7\), its quotient has \(H_0\cong H_{p-4}\cong\mathbb Z\); for every odd \(1\le j\le p-6\), it has \(H_j\cong\mathbb Z/p\mathbb Z\), and all other homology groups vanish. Its fundamental group is \(C_p\), and the universal cover is \(S^{p-4}\). At \(p=5\) the quotient is \(S^1\), whose fundamental group is infinite cyclic rather than \(C_5\). In particular, the seven-gon quotient is the three-dimensional lens space \(L(7;2,3)\), equivalent under a generator change to \(L(7;1,5)\), and has \(H_1\cong\mathbb Z/7\mathbb Z\). These assertions classify the precise weighted lens-space homeomorphism type, not just its Betti numbers.

## Assumptions and scope
Every polygon is strictly convex, has equally spaced vertices \(a_j=(\cos(2\pi j/p),\sin(2\pi j/p))\), and is labeled modulo \(p\). The simplicial realization uses the usual vertex-permutation action; its geometric quotient is not confused with the simplicial complex on vertex orbits. Only the full order-\(p\) rotation group for odd prime \(p\) is asserted. The dimension of \(|\mathcal A_p|\) is \(p-4\). The lens parameter list contains \((p-3)/2\) entries, so the displayed sphere dimension is \(2((p-3)/2)-1=p-4\).

## Proof
**1. An equivariant convex model.** Let \(Q\) be the regular polygon. For every triangulation \(T\), form its secondary-polytope vector \(\phi(T)\in\mathbb R^p\), whose \(j\)-th coordinate is the sum of the Euclidean areas of triangles of \(T\) incident to vertex \(a_j\). The secondary-polytope theorem for a convex polygon identifies \(P=\operatorname{conv}\{\phi(T)\}\) as a full-dimensional \((p-3)\)-dimensional associahedron in its affine hull, with faces anti-isomorphic to polygonal dissections. This is the standard secondary-polytope construction; no new polytopality assertion is made. The correspondence is equivariant under rotation. Its polar dual has a boundary realization of \(\mathcal A_p\), equivariant under the same rotation group.

**2. The exact ambient representation.** Each triangle contributes its area three times to \(\sum_j\phi_j(T)\), and contributes three times area times its centroid to \(\sum_j a_j\phi_j(T)\). Thus every secondary vertex lies in the affine space determined by the triangulation-independent equations
\[
\sum_j\phi_j(T)=3\operatorname{area}(Q),\qquad
\sum_j a_j\phi_j(T)=3\int_Q x\,dx=0.
\]
The affine hull of \(P\) has dimension \(p-3\), so its difference space is exactly
\[
W_p=\left\{x\in\mathbb R^p:\sum_jx_j=\sum_jx_j\cos(2\pi j/p)=\sum_jx_j\sin(2\pi j/p)=0\right\}.
\]
The permutation action of the one-step rotation preserves these equations orthogonally. By averaging the vertices of \(P\), one obtains a \(C_p\)-fixed point in its relative interior. Taking the polar dual after translating this point to the origin gives a full-dimensional invariant convex polytope in \(W_p\), whose boundary is \(C_p\)-equivariantly homeomorphic, by radial projection, to the unit sphere \(S(W_p)\). Its combinatorial boundary is precisely \(\mathcal A_p\). Hence \(|\mathcal A_p|\cong_{C_p}S(W_p)\).

**3. Fourier weights.** Put \(\omega=e^{2\pi i/p}\). For \(2\le k\le(p-1)/2\), the complex coordinate \(z_k(x)=\sum_{j=0}^{p-1}x_j\omega^{kj}\) identifies one real two-dimensional summand of \(W_p\). The omitted modes are the constant mode and the sine/cosine first modes, exactly those constrained in the definition of \(W_p\). If the rotation sends the coordinate labeled \(j\) to the coordinate labeled \(j+1\), then \(z_k\mapsto\omega^kz_k\). Thus, as orthogonal real \(C_p\)-representations,
\[
W_p\cong\bigoplus_{k=2}^{(p-1)/2}\mathbb C_k,
\]
where \(\mathbb C_k\) is the real plane rotated through \(2\pi k/p\). Rescaling the Fourier coordinates gives an equivariant isometry of unit spheres. Since every weight \(k\) is nonzero modulo the prime \(p\), every nonidentity group element has no nonzero fixed vector; the sphere action is free. By the defining construction, its quotient is the displayed weighted lens space.

**4. Integral topology.** For \(p\ge7\), the sphere has dimension at least three and is simply connected, hence is the universal cover of its free \(C_p\) quotient. The standard integral cellular chain complex of an odd-dimensional lens space has alternating differentials zero and multiplication by \(p\), yielding the stated homology, with the orientation class in degree \(p-4\). At \(p=5\), the covering sphere is a circle, and a finite rotation quotient of a circle is again a circle. The special fundamental-group statement therefore cannot be extended to \(p=5\).

## Verification
The reproducible program `verification/verify_prime_associahedral_quotient.py` constructs the complete noncrossing-diagonal complex for \(p=5\) and \(p=7\), enumerates all face orbits under rotation, constructs the exact signed orbit-cell boundary maps, and verifies that successive boundaries compose to zero. For \(p=7\) it finds quotient face counts \((2,8,12,6)\) in dimensions zero through three. A spanning-tree reduction of the first boundary map reduces first homology to an integer presentation whose nonunit Smith invariant is exactly seven. The third-boundary Smith factors are all units, which additionally verifies that second homology has no torsion. The results agree with the independent representation-sphere argument. The code requires Python and SymPy; these finite cases do not prove the theorem for all primes.

## Relationship to prior work
The established polygonal secondary-polytope construction and the equivariant theory in Victor Reiner, *Equivariant fiber polytopes* (2002), provide the convex equivariant model and classify its invariant **subpolytopes** (particularly Proposition 4.2). Those invariant subpolytopes must not be confused with the orbit-space quotient \(\partial P/C_p\). Fomin and Zelevinsky's publicly available 2001 preprint supplies the standard type-A simplicial associahedron and its sphere property. The lens-space construction and integral homology are standard. The contribution here is the explicit identification of the entire prime rotational **orbit space** as a weighted lens space with the first Fourier mode omitted, yielding precise nontrivial topology of the quotient. Known lens quotients of boundaries of cycle graph-associahedra instead retain the first Fourier mode and have different dimension and lens weights; that result does not entail this identification for the polygonal type-A associahedron.

## Limitations
The classification does not address composite polygon sizes, reflection-containing subgroups, integral cohomology operations, or minimal triangulations of the resulting lens spaces. The underlying secondary-polytope representation, the radial sphere principle and lens-space homology are established tools; the result should not be read as a new general equivariant-polytopal theorem. A closely related consequence of older equivariant-polytope constructions might have been implicit or recorded with different terminology, so bibliographic priority remains subject to broader historical inspection. The explicit homeomorphism is topological; a particular PL-equivalence is not claimed.

## References
- Sergey Fomin and Andrei Zelevinsky, *Y-systems and generalized associahedra*, first publicly posted 2001-11-06, arXiv:hep-th/0111053, especially the classical type-A model and spherical realization. https://arxiv.org/abs/hep-th/0111053
- Victor Reiner, *Equivariant fiber polytopes*, Documenta Mathematica **7** (2002), 113–132, especially Sections 2, 3.2, 4.1 and Proposition 4.2. https://ems.press/content/serial-article-files/25900?nt=1
- *Lens space*, Encyclopedia of Mathematics, entry defining weighted lens spaces and describing the corresponding cyclic sphere actions and topology. https://encyclopediaofmath.org/wiki/Lens_space
