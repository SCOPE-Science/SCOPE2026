# Global coordinate straightening and the Cohen–Macaulay threshold for two polynomial-composition loci

## Finding

Fix an odd integer \(m=2d+1\geq5\) and work over \(\mathbb C\). Let
\[
\widetilde{\mathcal P}_{2m}
=\bigl\{t^{2m}+\sum_{j=1}^{2m-2}a_jt^j\bigr\}
\cong\mathbb A^{4d}
\]
be the affine space of monic, centered, zero-constant polynomials. Write \(\mathcal D_{r,s}\) for the reduced composition locus with left and right factor degrees \(r\) and \(s\), and put \(R_m=(\mathcal D_{m,2}\cup\mathcal D_{2,m})_{\mathrm{red}}\).

**Theorem.** There is a *polynomial automorphism of the ambient coefficient affine space* which carries \(R_m\) onto the reduced coordinate-plane union
\[
V\bigl(w_1,\ldots,w_d,\ u_i v_j\ (1\leq i,j\leq d)\bigr)
\subset\mathbb A^{4d}_{z,u,v,w}.
\]
In particular,
\[
\mathbb C[R_m]\cong
\mathbb C[z_1,\ldots,z_d,u_1,\ldots,u_d,v_1,\ldots,v_d]
/(u_iv_j:1\leq i,j\leq d).
\]
The singular support is the smooth \(d\)-plane \(I=V(u_1,\ldots,u_d,v_1,\ldots,v_d)\), corresponding in the original coefficients to \(P=t^2W(t^2)^2\) with \(W\) monic of degree \(d\). The normalization is the disjoint union of the two affine \(2d\)-planes, and its conductor ideal in \(\mathbb C[R_m]\) is \((u_1,\ldots,u_d,v_1,\ldots,v_d)\).

For **every complex point** \(P\in I(\mathbb C)\), the completed local ring is
\[
\widehat{\mathcal O}_{R_m,P}\cong
\mathbb C[[z_1,\ldots,z_d,u_1,\ldots,u_d,v_1,\ldots,v_d]]/(u_iv_j).
\]
It has Krull dimension \(2d\), embedding dimension \(3d\), Hilbert–Samuel multiplicity \(2\), and maximal-ideal Hilbert–Samuel series
\[
\boxed{H_{R_m,P}(q)=\frac{2}{(1-q)^{2d}}-\frac{1}{(1-q)^d}.}
\]
Its depth is **exactly** \(d+1\), so it is not Cohen–Macaulay for any \(m\geq5\). If \(m=p\geq5\) is prime, \(R_p\) is the **entire reduced invariant-Bezoutian reducibility locus** in \(\widetilde{\mathcal P}_{2p}\); thus these full reducibility loci are not Cohen–Macaulay along their entire singular support.

## Assumptions and scope

All schemes and morphisms are over \(\mathbb C\). The union is endowed with its reduced scheme structure, not with the scheme structure of an unspecified Bezoutian coefficient resultant. The automorphism concerns the affine normalized slice, not its projective closure. The local ring statement is at complex closed points. For composite odd \(m\), the full invariant-Bezoutian reducibility locus may possess further composition components; only the indicated two-component union is classified here. The prime case identifies the full reduced locus by the polynomial invariant-Bezoutian criterion of Fried, as cited by Piene–Shapiro.

## Proof

**1. Two polynomially parametrized components.** Put \(S=\widetilde{\mathcal P}_{2m}\). A centered quadratic inner factor is \(t^2\), so \(A=\mathcal D_{m,2}\) is exactly the linear subspace of even polynomials in \(S\). Thus \(A\cong\mathbb A^{m-1}\). Every point of \(B=\mathcal D_{2,m}\) is uniquely expressible as
\[
P(t)=H(t)^2+bH(t),\qquad
H(t)=t^m+\sum_{j=1}^{m-2}h_jt^j,
\]
with \(b,h_1,\ldots,h_{m-2}\in\mathbb C\). Uniqueness follows directly from the successive coefficient recovery below; it agrees with the normalized composition embedding of von zur Gathen–Matera.

**2. The nonlinear component is a polynomial graph over a linear coordinate projection.** Split the coefficients of \(P\) into the \(m-1\) high coordinates \(x=(a_m,a_{m+1},\ldots,a_{2m-2})\) and the \(m-1\) low coordinates \(y=(a_1,\ldots,a_{m-1})\). In \(P=H^2+bH\), the coefficient of \(t^{m+j}\), for \(j=m-2,m-3,\ldots,1\), has the triangular form
\[
a_{m+j}=2h_j+F_j(h_{j+1},\ldots,h_{m-2})
\]
for polynomials \(F_j\) with rational coefficients, because the term \(bH\) has degree \(m\). Recursion recovers each \(h_j\) polynomially from high coordinates. Finally
\[
b=a_m-[t^m]H(t)^2
\]
recovers \(b\) polynomially. Conversely these choices produce every vector \(x\in\mathbb A^{m-1}\), and the remaining coefficients are polynomial functions \(y=\mathsf F(x)\). Consequently \(B\) is globally the graph of a polynomial map \(\mathsf F:\mathbb A^{m-1}\to\mathbb A^{m-1}\).

**3. Parity and simultaneous straightening.** Because \(2m\) is even and \(m\) is odd, the involution \(P(t)\mapsto P(-t)\) preserves \(B\): if \(P=H^2+bH\), then \(P(-t)=\widetilde H^2-b\widetilde H\), where \(\widetilde H(t)=-H(-t)\) is again monic, centered and has zero constant term. On the high and low coefficient spaces the involution negates precisely the odd-indexed coefficients. Since \(B\) is a graph, \(\mathsf F\) is parity-equivariant. Therefore the odd-indexed low coordinates of \(\mathsf F(x)\) vanish whenever all odd-indexed high coordinates of \(x\) vanish.

Apply the polynomial automorphism \(\Phi(x,y)=(x,y-\mathsf F(x))\), whose inverse is \((x,y')\mapsto(x,y'+\mathsf F(x))\). It carries \(B\) to \(\{y'=0\}\). Since \(A\) is defined by the vanishing of every *odd* coefficient, the parity property carries \(A\) to \(\{x_{\mathrm{odd}}=0,\ y'_{\mathrm{odd}}=0\}\). There are \(d\) coordinates in each of the four groups
\[
z=x_{\mathrm{even}},\quad u=x_{\mathrm{odd}},\quad
v=y'_{\mathrm{even}},\quad w=y'_{\mathrm{odd}}.
\]
Thus \(\Phi(A)=V(u,w)\) and \(\Phi(B)=V(v,w)\). Their reduced union is cut out by
\[
(u,w)\cap(v,w)=(w,u_i v_j:1\leq i,j\leq d).
\]
This proves the claimed **global** polynomial-coordinate normal form, without genericity assumptions on \(H\) or \(W\).

**4. Intersection, normalization and conductor.** The two coordinate \(2d\)-planes meet in exactly \(V(u,v,w)\cong\mathbb A^d_z\). By polynomial recovery, points of this intersection are precisely the even members of \(B\), namely \(P=H^2\) with \(H\) odd; equivalently \(P=t^2W(t^2)^2\) for unique monic degree-\(d\) polynomial \(W\). This agrees with Piene–Shapiro Proposition 7.3. The coordinate ring is a fiber product
\[
\mathbb C[z,u]\times_{\mathbb C[z]}\mathbb C[z,v],
\]
whose normalization is \(\mathbb C[z,u]\oplus\mathbb C[z,v]\). An element belongs to the conductor if and only if both restrictions to \(\mathbb C[z]\) vanish, giving precisely the ideal \((u,v)\) inside the fiber-product ring. The singular support is exactly \(V(u,v)\): away from this plane, one smooth component occurs; along it, the local ring has two distinct minimal primes.

**5. Hilbert–Samuel series and depth.** Translating the \(z\) coordinates identifies the completed local ring at any complex point of the intersection with the displayed homogeneous monomial model. The degree-\(n\) monomials in that model are the union of the monomials in \((z,u)\) and in \((z,v)\), with the monomials in \(z\) counted twice. Hence its graded and maximal-ideal Hilbert–Samuel series is \(2/(1-q)^{2d}-1/(1-q)^d\). The leading Hilbert-polynomial term has multiplicity \(2\); the degree-one component has dimension \(3d\). Its dimension is \(2d\).

For the depth, localize at the maximal ideal of a closed intersection point and use the exact sequence
\[
0\longrightarrow\mathcal O_{R_m,P}\longrightarrow
\mathcal O_{A,P}\oplus\mathcal O_{B,P}
\longrightarrow\mathcal O_{I,P}\longrightarrow0.
\]
The middle term has depth \(2d\) and the final term depth \(d\). Since \(2d>d\), the depth lemma (or the associated local-cohomology sequence) gives \(\operatorname{depth}\mathcal O_{R_m,P}=d+1\). For \(d\geq2\), this is strictly less than \(2d\).

**6. Prime-degree identification.** If \(m=p\geq5\) is prime, the only proper ordered factorizations of \(2p\) are \((p,2)\) and \((2,p)\). The invariant Bezoutian of a composite-degree polynomial is reducible precisely on the union of its composition loci (Piene–Shapiro, Theorem 5.3, applying Fried’s criterion; the exceptional Dickson case only occurs in prime degree). Therefore the full *reduced* invariant reducibility locus in the degree-\(2p\) normalized slice equals \(R_p\). This completes the proof.

## Verification

The standalone `verify_composition.py` uses only the Python standard library and exact rational arithmetic. It reconstructs inner and outer factors from high coefficients for degrees \(m=3,5,7,9,11\), tests the parity constraint, checks independent tangent-space ranks at several power and non-power intersection points, and directly counts the allowed monomials for five initial degrees in the model rings at \(d=1,2,3,4\). Run with `python3 verify_composition.py`; its successful final line is `ALL EXACT CHECKS PASS`. These examples are checks, not a proof for arbitrary \(m\); steps 1–6 above establish the universal assertion.

## Relationship to prior work

Piene–Shapiro (2026) prove that the normalized composition components are smooth and identify their intersection as \(\{t^2W(t^2)^2\}\); their discussion of invariant Bezoutians also identifies the reduced singular support for arbitrary composite degree. Von zur Gathen–Matera (2017) establish polynomial recovery of composition factors and provide dimension bounds and an intersection classification; their later interpolation work (2021 preprint, 2024 journal) studies the geometry of individual composition varieties in interpolation. These results are essential foundations, not newly claimed. The **new statement** is simultaneous *ambient polynomial straightening* of both components, with the full ring/conductor/Hilbert–Samuel/depth consequences and the non-Cohen–Macaulay threshold for the full prime-index reducibility locus. In particular, smoothness of two components and smoothness of their set intersection do not alone imply simultaneous straightening or clean intersection.

## Limitations

The result concerns the reduced union, not any scheme defined by a chosen resultant, discriminant or Jacobian presentation of Bezoutian reducibility. The polynomial automorphism need not preserve the original weighted coefficient grading, and no claim is made for the projective closure. For composite odd \(m\), other decomposition types may contribute to the full reducibility locus. The cited literature search cannot exclude every unindexed previous derivation of the same coordinate normal form. The included finite computations do not replace the all-degree proof. No independent audit has been carried out.

## References

1. R. Piene and B. Shapiro, *Composition loci, invariant Bezoutians, and finite-orbit correspondences*, arXiv:2611.16763v1 (first public 12 November 2026), Sections 1.1, 5, 6.4 and 7; https://arxiv.org/html/2611.16763v1.
2. J. von zur Gathen and G. Matera, *Density of real and complex decomposable univariate polynomials*, arXiv:1407.0906v2, *Quarterly Journal of Mathematics* 68 (2017), 1227–1246, Theorems 1.2–1.3; https://arxiv.org/pdf/1407.0906.
3. J. von zur Gathen and G. Matera, *Interpolation by decomposable univariate polynomials*, arXiv:2103.15926v1 (2021), *Journal of Complexity* 85 (2024), 101885; https://arxiv.org/abs/2103.15926.
