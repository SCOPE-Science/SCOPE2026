# A square discriminant and twenty-four paired-node degenerations in the Eckardt pencil

## Finding
Let \(V\) be a four-dimensional complex vector space and let \(F\in\operatorname{Sym}^3(V^*)\) define a smooth cubic surface \(S\subset\mathbb P(V)\). Write \(D_S\) for an irreducible homogeneous equation of its projective dual \(S^\vee\subset\mathbb P(V^*)\), with any nonzero normalization. For \(\ell\in V^*\), put
\[
G_\ell(x,u)=F(x)+u^2\ell(x),\qquad [x:u]\in\mathbb P(V\oplus\mathbb C).
\]
The discriminant of this homogeneous cubic in five variables satisfies the polynomial identity
\[
\boxed{\operatorname{Disc}_5(G_\ell)=c_F D_S(\ell)^2},\qquad c_F\in\mathbb C^\times.
\]
Here \(\operatorname{Disc}_5\) denotes the standard nonzero projective cubic discriminant under any fixed normalization; \(c_F\) changes with that normalization. In particular the restricted discriminant is a *double*, not a reduced, dual surface in the affine four-space of \(\ell\)-coefficients.

Now let \(W\) have dimension two and let \(q\in V^*\otimes\operatorname{Sym}^2 W^*\) have rank-three coefficient map. Assume the cubic fourfold \(Y=\{F(x)+q(x,z)=0\}\subset\mathbb P(V\oplus W)\) is smooth and the induced conic \(c_q:\mathbb P(W)\to\mathbb P(V^*)\), \([t]\mapsto[q(-,t)]\), intersects \(S^\vee\) transversely in its smooth locus. Then the Eckardt family \(T_t=\{G_{q(-,t)}=0\}\) has exactly \(24\) distinct singular parameters. Each such cubic threefold has **precisely two ordinary double points** and no other singularities; the involution \([x:u]\mapsto[x:-u]\) exchanges these nodes. The binary cubic-threefold discriminant has degree \(48\) and is the exact square of a degree-\(24\) binary form with \(24\) simple zeros. The incidence total space of the pencil is smooth.

These conditions hold for \(q\) in a nonempty Zariski-open subset, for every fixed smooth complex cubic surface \(S\).

## Assumptions and scope
Everything is over \(\mathbb C\), in characteristic zero. A discriminant is the polynomial vanishing precisely on singular projective cubic hypersurfaces, with its usual resultant multiplicities; it is not the reduced equation of its support. Rank three means that the linear coefficient map \(\operatorname{Sym}^2W\to V^*\) is injective, so \(q(-,t)\neq0\) for nonzero \(t\). The transversality assumption applies to the embedded conic and the *smooth* part of the dual hypersurface. The claims about exactly \(24\) singular fibers and their types are generic, not claims about special symmetric conics or rank-two coefficient maps.

## Proof
**1. Singular-support reduction.** For \(\ell\neq0\), the partial derivatives of \(G_\ell\) are
\[
\partial_uG_\ell=2u\ell(x),\qquad \partial_xG_\ell=dF_x+u^2\ell.
\]
If \(u=0\), projective singularity would require \(dF_x=0\) at a nonzero \(x\), contrary to smoothness of \(S\). At \(x=0\), the \(x\)-gradient is \(u^2\ell\neq0\). Every singularity therefore has \(u\neq0\), \(x\neq0\) and satisfies \(\ell(x)=0\), \(dF_x=-u^2\ell\). Euler's identity \(3F(x)=dF_x(x)\) gives \(F(x)=0\), and \(\ell=0\) is tangent to \(S\) at \([x]\). Conversely, any tangent plane has \(dF_p=\lambda\ell\) with \(\lambda\neq0\); solving \(u^2=-\lambda\) yields a singular point. Hence the zero set of the specialized discriminant is precisely the affine cone over \(S^\vee\), including its vertex. This is the set-theoretic criterion of Li Bassi, Lemma 2.1.

**2. The exact polynomial multiplicity.** For homogeneous cubics in five variables, the discriminant transforms by
\[
\operatorname{Disc}_5(G\circ A)=(\det A)^{48}\operatorname{Disc}_5(G)
\]
for every invertible linear change of coordinates \(A\). For \(a\in\mathbb C^\times\), the change \(u\mapsto\sqrt a\,u\) sends \(G_\ell\) to \(G_{a\ell}\); its determinant is \(\sqrt a\). Therefore \(P(\ell):=\operatorname{Disc}_5(G_\ell)\) is a homogeneous polynomial of degree exactly \(24\) in \(\ell\). It is nonzero, since for a nontangent \(\ell\) the cubic is smooth. The dual of a smooth cubic surface is an irreducible degree-\(3(3-1)^2=12\) hypersurface. Because \(P\) has exactly its irreducible zero support, unique factorization gives \(P=c_FD_S^m\); comparing degrees forces \(m=2\). This proves the identity as a polynomial, including at special tangencies.

**3. Singularities over a simple dual point.** At a smooth point \([\ell]\) of \(S^\vee\), the plane has one ordinary quadratic tangency with \(S\). Let \(p\) represent its unique tangency point, and write \(dF_p=\lambda\ell\). The singular points of \(G_\ell\) are exactly the two distinct projective points obtained by solving \(u^2=-\lambda\) with \(x=p\); equivalently, in the chart \(u=1\), \(x=\pm p/\sqrt{-\lambda}\). In local homogeneous coordinates where \(p=[1:0:0:0]\) and \(\ell=x_3\), the cubic has linear term \(x_0^2x_3\), while the quadratic form on the tangent plane \(x_3=0\) is nondegenerate in its two transverse coordinates. The full four-by-four Hessian of \(F\) at \(p\) is therefore nondegenerate: its \((x_0,x_3)\)-block has nonzero off-diagonal term, and the remaining tangent block is nondegenerate. The Hessian of the affine equation \(G_\ell(x,1)\) at either singular point is a nonzero scalar multiple of this matrix. Both singularities are ordinary threefold nodes \(A_1\); no third singularity exists by the tangency correspondence. Since \([x:u]\mapsto[x:-u]\) is equivalent to \(x\mapsto-x\) in the \(u=1\) chart, it swaps the nodes.

**4. The twenty-four parameters.** The rank-three coefficient map makes \(c_q\) a closed Veronese conic in the dual three-space, with \(c_q^*\mathcal O(1)=\mathcal O_{\mathbb P^1}(2)\). Consequently \(D_S(q(-,t))\) is a binary form of degree \(12\cdot2=24\). By the stated transversality, all its roots are simple and correspond to smooth points of the dual, so Step 3 applies at each and all remaining fibers are smooth. Step 2 shows that the actual cubic-threefold discriminant is its square, of degree \(48\).

The transversality condition is nonempty and Zariski open: general plane conics avoid the proper singular locus of the dual and meet its smooth locus transversely. The auxiliary exact computation in `checker.py` exhibits one rank-three conic with \(24\) distinct intersections for the Fermat cubic surface. Independently, Li Bassi's Lemma 2.4 proves the smooth rank-three fourfold condition is nonempty Zariski open for any fixed smooth \(S\). Two nonempty opens in the irreducible coefficient space meet.

**5. Smooth total space.** The incidence variety \(\mathcal T=\{(y,t):y\in T_t\}\) of this hyperplane pencil is the blow-up of smooth \(Y\) along its base locus \(S=Y\cap\mathbb P(V)\), which is smooth. Hence \(\mathcal T\) is smooth. Thus the double-node fibers are actual transverse nodal degenerations, not singularities of the total incidence space.

## Verification
Run `python checker.py` with SymPy. It constructs the Fermat cubic surface's dual polynomial by multiplying its eight signed square-root tangency equations, verifies degree \(12\), and certifies that the following rank-three quadratic coefficient map has a degree-\(24\) squarefree pullback:
\[
\begin{pmatrix}-1&-1&2\\2&3&3\\-2&2&-2\\2&-2&3\end{pmatrix}
\begin{pmatrix}s^2\\st\\t^2\end{pmatrix}.
\]
The exact polynomial gcd check confirms a concrete nonempty transverse locus. This finite symbolic check is a witness only; Steps 1–5 prove the infinitely many cases and the discriminant multiplicity.

## Relationship to prior work
Li Bassi (2026), Lemma 2.1, proves the *set-theoretic* characterization of smooth Eckardt members by hyperplane transversality; equation (2.3) describes their parameter set via the dual surface, and Section 2.2 identifies the rank-three conic. The paper expressly notes that this set-based description retains no multiplicity information. The present contribution identifies the full discriminant polynomial as an exact square and determines the generic boundary multiplicities, number of singular fibers, node pairing and smooth incidence total space. Marquand (2022), Lemma 4.7, establishes a different paired-node phenomenon for hyperplanes through the fixed line of an involution, not this Eckardt pencil or the square-discriminant identity. The dual-degree formula and discriminant covariance are classical ingredients, not claimed as new.

## Limitations
The statement is over \(\mathbb C\). Special coefficient maps can meet singular points of \(S^\vee\), producing different singularities or collision multiplicities; neither every rank-three pencil nor the rank-two family is claimed to have \(24\) distinct two-node members. The square identity holds without genericity, but the node census requires it. This result does not describe the compactified intermediate-Jacobian fibers at the special parameters, which generally lie beyond the one-node locus.

## References
1. L. Li Bassi, *Cubic fourfolds with a symplectic involution from finite Prym data*, arXiv:2611.14747v1 (first public 2026-11-10), especially Lemmas 2.1 and 2.4, Sections 2.2 and 6.3. https://arxiv.org/html/2611.14747v1
2. L. Marquand, *Cubic Fourfolds with an Involution*, arXiv:2202.13213 (2022), especially Lemma 4.7 and Proposition 4.9. https://arxiv.org/abs/2202.13213
3. A. Dimca and G. Ilardi, *On the duals of smooth projective complex hypersurfaces*, arXiv:2301.06952 (2023), for context on dual singularities and multiple tangencies. https://arxiv.org/abs/2301.06952
