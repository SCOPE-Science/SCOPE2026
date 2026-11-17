# Order-nine torsion and an exceptional fundamental group in the nine-gon associahedral rotation quotient

## Finding
Let \(K_9\) be the simplicial complex whose vertices are the twenty-seven diagonals of a regular nine-gon and whose simplices are collections of pairwise noncrossing diagonals. Let \(C_9\) act by rotating the polygon. Its **ordinary geometric** quotient \(Y=|K_9|/C_9\) has
\[
\pi_1(Y)\cong\mathbb Z/3,\qquad
H_i(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,5,\\
\mathbb Z/3,&i=1,\\
0,&i=2,4,
\end{cases}
\]
while \(H_3(Y;\mathbb Z)\) has **exactly nine elements** and fits into an exact sequence
\[
0\longrightarrow\mathbb Z/3\longrightarrow H_3(Y;\mathbb Z)
\longrightarrow\mathbb Z/3\longrightarrow0.
\]
In particular this is a rational homology five-sphere with distinct nonzero three-primary torsion in degrees one and three. This theorem does **not** resolve whether the order-nine group in degree three is cyclic or split.

## Assumptions and scope
The polygon is regular, its symmetries are literal cyclic rotations of all nine vertices, and the quotient is the orbit space of the entire geometric realization, not the naive quotient of the abstract vertex set. All homology is singular homology over the indicated coefficients. The exact model is the unit sphere in the six-real-dimensional representation \(V=\mathbb C_2\oplus\mathbb C_3\oplus\mathbb C_4\), where a generator of \(C_9\) multiplies the \(j\)-th factor by \(\exp(2\pi i j/9)\).

## Proof
**Equivariant spherical model.** The secondary polytope of the convex regular nine-gon is a six-dimensional simple associahedron: all its triangulations are regular, and its face poset is dual to the noncrossing-diagonal complex. Its GKZ vectors are permuted under polygon rotations. They lie in the affine subspace determined by the sum-of-coordinates constraint and the two planar moment constraints. This subspace has translation representation the orthogonal complement of the constant and first Fourier harmonics in \(\mathbb R^9\). Its Fourier decomposition is precisely \(V=\mathbb C_2\oplus\mathbb C_3\oplus\mathbb C_4\). The invariant barycenter of the full-dimensional convex polytope lies in its interior. Radial projection from it is an equivariant homeomorphism from the secondary-polytope boundary to \(S(V)\). The face-lattice correspondence identifies this boundary equivariantly with \(|K_9|\). These are standard secondary-polytope facts; sources are listed below.

**The two-piece cover.** Set \(U=\mathbb C_2\oplus\mathbb C_4\), \(W=\mathbb C_3\), \(G=C_9\), and \(H=\langle g^3\rangle\cong C_3\). Since the weights two and four are units modulo nine, \(G\) acts freely on \(S(U)\). The kernel of the action on \(W\) is exactly \(H\). Cover \(S(U\oplus W)/G\) by the closed invariant halves \(A\) and \(B\) defined by \(\|u\|\ge\|w\|\) and \(\|w\|\ge\|u\|\); they retract respectively onto
\[
A\simeq S(U)/G=L(9;2,4),\qquad B\simeq S(W)/G\cong S^1.
\]
Their intersection retracts onto \(E=(S(U)\times S(W))/G\), which fibers over \(S(W)/G=S^1\) with fiber \(F=S(U)/H\), an orientable three-dimensional lens space with \(\pi_1(F)=H\cong C_3\). Monodromy is induced by a generator of \(G\), hence preserves the orientation class and acts trivially on \(H_1(F;\mathbb Z)=C_3\) by abelianity.

**Intersection and Mayer–Vietoris.** From the Wang exact sequence for this mapping torus,
\[
H_0(E)=\mathbb Z,\ H_1(E)=\mathbb Z\oplus\mathbb Z/3,\ H_2(E)=\mathbb Z/3,\ H_3(E)=\mathbb Z,\ H_4(E)=\mathbb Z.
\]
The restriction of \(E\to A\) to a fiber is the three-sheeted covering \(F\to L(9;2,4)\). On \(H_1\), it embeds \(C_3\) as the unique order-three subgroup of \(C_9\); on \(H_3\), it multiplies the fundamental class by three. Moreover \(H_1(E)\to H_1(B)=\mathbb Z\) maps the free quotient isomorphically onto \(\mathbb Z\). Consequently \(H_1(E)\to H_1(A)\oplus H_1(B)\) is injective, with cokernel \(C_9/C_3\cong C_3\). Mayer–Vietoris gives \(H_1(Y)=C_3\) and \(H_2(Y)=0\). The segment in degrees three and four gives \(H_4(Y)=0\) and
\[
0\longrightarrow\operatorname{coker}(\mathbb Z\xrightarrow{\times3}\mathbb Z)
\longrightarrow H_3(Y)
\longrightarrow H_2(E)=\mathbb Z/3\longrightarrow0.
\]
Thus \(|H_3(Y)|=9\). The top-degree segment gives \(H_5(Y)=H_4(E)=\mathbb Z\); connectedness gives \(H_0(Y)=\mathbb Z\). There is no homology in degrees above five.

**Fundamental group.** The covering sphere \(S^5\) is simply connected. The only nontrivial point stabilizers of the \(G\)-action occur on \(S(W)\) and equal \(H=C_3\). Armstrong's orbit-space fundamental-group theorem, or van Kampen on the same two-piece cover, therefore gives \(\pi_1(Y)=G/H\cong C_3\).

## Verification
A standalone standard-library script `nonagon_verifier.py` enumerates all noncrossing diagonal faces by direct nonintersection tests. It confirms exactly 27 diagonals, 429 maximal triangulations, the complete face counts \((27,225,825,1485,1287,429)\), rotational orbit counts \((3,25,93,165,143,49)\), and twelve individual faces with stabilizer order three (all others have trivial face stabilizer). It also checks the character weights and point-isotropy orders. These finite checks corroborate the concrete model; the infinite topological deductions are proved by the secondary-polytope model and the exact sequences above, **not** by enumerating faces. The recorded output is embedded in `nonagon_check.txt`.

## Relationship to prior work
Fomin and Zelevinsky prove the type-\(A\) noncrossing-diagonal associahedral sphere and identify polygon rotations. Herrmann explains the GKZ secondary-polytope construction and its triangulation face poset. Previous rotation-quotient calculations for **odd prime** polygon sizes produce free weighted lens spaces; they do not entail the isotropy or the order-nine torsion found here at the first odd composite size. General theory of finite cyclic linear sphere actions supplies useful background, but an equivalent composite-size homology calculation may exist outside inspected sources.

## Limitations
The isomorphism type of \(H_3\) within its proved order-nine extension is **not** determined: this result does not distinguish \(\mathbb Z/9\) from \((\mathbb Z/3)^2\). It makes no claim about a homeomorphism to a manifold or a formula for all composite polygon sizes. Published novelty is assessed against accessible sources and may be affected by an undiscovered general computation. No independent audit has been performed.

## References
1. S. Fomin and A. Zelevinsky, *Y-systems and generalized associahedra*, arXiv:hep-th/0111053v1 (first submitted 6 November 2001), especially Proposition 3.14 and the type-\(A\) polygon discussion: https://arxiv.org/abs/hep-th/0111053.
2. S. Herrmann, *On the Facets of the Secondary Polytope*, arXiv:0908.2537v1 (18 August 2009), Section 2.2 on GKZ vectors and the subdivision face poset: https://arxiv.org/abs/0908.2537.
3. F. Santos, C. Stump and V. Welker, *Noncrossing Sets and a Grassmann Associahedron*, arXiv:1403.8133v1 (March 2014), for polygonal noncrossing complexes: https://arxiv.org/abs/1403.8133.
