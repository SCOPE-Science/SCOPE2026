# Two singular strata and varying simple-elliptic transverse types in Cox spaces of Jacobian elliptic surfaces

## Finding
Let \(\pi:X\to\mathbb P^1_{\mathbb C}\) be a relatively minimal semistable Jacobian elliptic surface with \(\chi=\chi(\mathcal O_X)\ge3\), Picard number \(\rho(X)=2\), and reduced Weierstrass discriminant. Write its short Weierstrass coefficients as \(A\in\mathbb C[u,v]_{4\chi}\), \(B\in\mathbb C[u,v]_{6\chi}\), with \(\Delta=4A^3+27B^2\), and put \(T=\operatorname{Spec}\operatorname{Cox}(X)\). Then \(T\) is a normal, Gorenstein affine fourfold whose **reduced singular locus is exactly** the union of the affine plane \(P=V(x,y,z)\) and the affine line \(L=V(u,v,x,y)\), meeting only at the origin in the Weierstrass-Cox coordinates of the proof.

At each point \((u_0,v_0,0,0,0)\in P\) with \(\Delta(u_0,v_0)\ne0\), the canonical normal slice obtained by fixing \(u=u_0,v=v_0\) is a simple-elliptic surface singularity of type \(\widetilde E_8\): its minimal exceptional curve is the smooth elliptic fiber over \([u_0:v_0]\), has self-intersection \(-1\), and its Milnor number equals \(10\). The elliptic modulus of that slice is
\[
j([u:v])=1728\,\frac{4A(u,v)^3}{4A(u,v)^3+27B(u,v)^2}.
\]
It is nonconstant; hence these normal slices form infinitely many analytic isomorphism classes despite their constant Milnor number.

At each point of \(L\setminus\{0\}\), the canonical slice fixing \(z\ne0\) is an isolated weighted-homogeneous threefold hypersurface singularity with Milnor number
\[
\mu_L=2(6\chi-1)^2.
\]
The result describes the complete *set-theoretic* singular locus and these two open transverse strata, not the scheme structure of the Jacobian ideal or the singularity at the intersection origin.

## Assumptions and scope
Everything is over \(\mathbb C\). The surface is smooth, projective, relatively minimal and has a chosen zero section \(S\) and fiber class \(F\). Semistability means all singular fibers are multiplicative; Picard number two forces them all to be irreducible \(I_1\) fibers. The reduced discriminant is a binary form with \(12\chi\) distinct zeroes on \(\mathbb P^1\), so \(\Delta\not\equiv0\). The Picard group is \(\mathbb Z S\oplus\mathbb Z F\), and the free-graded Cox ring is the direct sum of spaces of sections of these divisors. The August 2026 construction of Laface--Li--Liu supplies such Picard-number-two families. The hypothesis of reduced discriminant is explicit throughout; no claim is made for nonsemistable degenerations.

## Proof
**1. Cox coordinates.** Put \(H=S+\chi F\). The Weierstrass pole-order filtration along the zero section has a basis of monomials \(x^i y^j\) with \(i\ge0\), \(j\in\{0,1\}\), of pole order \(2i+3j\). For every \(a\ge0\), \(b\in\mathbb Z\), projection to the base gives
\[
H^0(X,\mathcal O_X(aS+bF))\simeq
\bigoplus_{\substack{i\ge0,\,j\in\{0,1\}\\2i+3j\le a}}
\mathbb C[u,v]_{b-\chi(2i+3j)}z^{a-2i-3j}x^iy^j,
\]
where a homogeneous space of negative degree is zero. For \(a<0\) no sections exist, as their restriction to the generic elliptic fiber would have negative degree. This follows directly by filtering \(\pi_*\mathcal O_X(aS)\) by pole order: the successive graded pieces are \(\mathcal O_{\mathbb P^1}\) for order zero, and \(\mathcal O_{\mathbb P^1}(-n\chi)\) for each admitted order \(n\ge2\), with missing pole order one. The Weierstrass monomials split the filtration. Picard number two and the absence of reducible fibers imply there are no additional divisor degrees.

Consequently, with \(\deg u=\deg v=F\), \(\deg z=S\), \(\deg x=2H\), and \(\deg y=3H\), we have
\[
\operatorname{Cox}(X)\simeq
\frac{\mathbb C[u,v,z,x,y]}
{(f)},\qquad f=y^2-x^3-A(u,v)xz^4-B(u,v)z^6.
\]
Indeed the displayed monomials give every graded component and, since the Weierstrass relation is monic in \(y^2\), they give unique polynomial normal forms; hence there are no additional relations. This presentation also appears as a theorem in the later work of Laface--Li (arXiv:2611.24570, first public 18 November 2026); it is **not claimed as new** here.

**2. Entire reduced singular locus.** The hypersurface has dimension four. The partial derivatives with respect to \(x,y,z\) are
\[
f_x=-3x^2-Az^4,\quad f_y=2y,\quad
f_z=-4Axz^3-6Bz^5.
\]
Every point with \(z=0\) and all partial derivatives zero has \(x=y=0\); conversely \(P=V(x,y,z)\) consists of singular points because the remaining derivatives carry factors \(z^4\) or \(z^6\).

On \(z\ne0\), put \(X'=x/z^2\) and \(Y'=y/z^3\). The hypersurface is the product of \(\mathbb G_m\) with
\[
W=V\bigl(Y'^2-X'^3-A(u,v)X'-B(u,v)\bigr)\subset\mathbb A^4.
\]
The point \(u=v=X'=Y'=0\) is singular, giving precisely \(L\setminus\{0\}\). There are no other singular points of \(W\): if \((u,v)\ne(0,0)\), a singular point would be a repeated-root point of the Weierstrass cubic and also a singular point of the total Weierstrass family over the affine base. For a simple zero of \(\Delta\), the repeated root \(r\) is nonzero and obeys \(A=-3r^2\), \(B=2r^3\). In a local base coordinate \(t\), differentiation gives \(\partial_t\Delta=108r^3(r\partial_t A+\partial_t B)\). Thus \(\partial_t\Delta\ne0\) forces a nonzero base partial derivative of the cubic. Away from discriminant zero the fiber is smooth. This proves \(\operatorname{Sing}(T)_{\mathrm{red}}=P\cup L\). Since this has codimension two in the fourfold hypersurface, Serre's \(R_1+S_2\) criterion shows \(T\) is normal; being a hypersurface, it is Gorenstein.

**3. The plane stratum.** Fix a point \((u_0,v_0)\ne(0,0)\) with \(\Delta(u_0,v_0)\ne0\). The section by these two base-coordinate equations is the isolated weighted-homogeneous surface germ
\[
y^2=x^3+A(u_0,v_0)xz^4+B(u_0,v_0)z^6,
\qquad \mathrm{wt}(z,x,y)=(1,2,3),\quad d=6.
\]
Its weighted projectivization \(E\subset\mathbb P(1,2,3)\) is the smooth Weierstrass elliptic curve. It avoids the two ambient orbifold coordinate points. The weighted blowup of the vertex restricts to a smooth resolution whose entire exceptional set is \(E\), with normal bundle \(\mathcal O_E(-1)\). Since \(\deg\mathcal O_E(1)=6/(1\cdot2\cdot3)=1\), its self-intersection is \(-1\), so this is the minimal resolution of a degree-one simple elliptic (\(\widetilde E_8\)) singularity. Isolatedness and weighted homogeneity yield
\[
\mu_P=\left(\frac61-1\right)\left(\frac62-1\right)\left(\frac63-1\right)=5\cdot2\cdot1=10.
\]
The exceptional curve's analytic isomorphism class is an invariant of the singular germ. It has the same \(j\)-invariant as the original smooth elliptic fiber, namely the rational function in the Finding. Because \(\Delta\) is reduced, it has a simple zero at which \(A\ne0\) (a common zero of \(A,B\) would make \(\Delta\) multiple). Therefore \(j\) has a genuine pole and is nonconstant; its values on the smooth-fiber open subset are infinite. This proves nonconstant analytic type with constant \(\mu_P\).

**4. The line stratum.** On \(z\ne0\), the product isomorphism above shows that a transverse slice is the germ at the origin of \(W\). It is quasihomogeneous for the positive integral weights
\[
\mathrm{wt}(u,v,X',Y')=(1,1,2\chi,3\chi),\qquad d=6\chi.
\]
Step 2 shows it has an isolated singularity. Its four partial derivatives consequently form a regular sequence in the polynomial local ring, and the weighted Jacobian-algebra Hilbert-series calculation gives
\[
\mu_L=\left(6\chi-1\right)^2\left(\frac{6\chi}{2\chi}-1\right)\left(\frac{6\chi}{3\chi}-1\right)=2(6\chi-1)^2.
\]
This number is independent of the coefficients provided the discriminant remains reduced. The case \(\chi=3\) has \(\mu_L=578\). The four steps prove the statement.

## Verification
The supplied standalone symbolic check constructs a binary Weierstrass example with \(\chi=3\), verifies that its degree-36 discriminant is squarefree, checks two distinct smooth-fiber \(j\)-values, and evaluates the two weighted Milnor formulas. These computations test the hypotheses and signs but **do not replace** the universal geometric and commutative-algebra proofs above. The characteristic-zero deductions use the ordinary derivative, so no assertion about positive characteristic is made.

## Relationship to prior work
The paper *Mori dream Jacobian elliptic surfaces of Kodaira dimension one* (arXiv:2608.09002, first public 10 August 2026), especially its Picard-number-two construction, provides the natural class of surfaces and establishes their Mori-dream property. Its proofs concern cones and semiampleness, not the full reduced singular locus or the distinct transverse analytic types of the Cox spectrum.

A later paper, *Cox rings of Jacobian elliptic surfaces of Kodaira dimension one* (arXiv:2611.24570, first public 18 November 2026), independently gives the exact Cox-ring presentation used in Step 1. The present theorem does **not** claim that presentation, Cox finite generation, or the standard classification of simple elliptic cones as discoveries. The new combined assertion is the global \(P\cup L\) singular-locus decomposition, the two explicit transverse Milnor invariants, and recovery of the varying elliptic \(j\)-modulus from an open singular stratum of this particular Cox space. Familiar classifications of isolated weighted cones alone do not assert that family-wide Cox-geometric conclusion.

The classical literature on simple elliptic hypersurfaces and elliptic exceptional curves supplies comparison models, while work on rational singularities of Cox rings of del Pezzo surfaces concerns a different surface class. Search-based novelty is necessarily qualified; an unindexed previous computation or an implicit consequence of a stronger theorem remains possible.

## Limitations
The singular-locus equality is **reduced and set-theoretic**. There is no assertion about Jacobian-scheme multiplicities, the analytic germ at \(P\cap L\), degeneration strata over \(\Delta=0\) inside \(P\), or normal slices chosen by arbitrary alternative coordinates. The line-stratum Milnor number applies to its stated isolated three-dimensional slice, not to the nonisolated fourfold germ itself. The analytic nonisomorphism statement compares the specified canonical slices. No claim of independent validation is made.

## References
- A. Laface, S. Li and J. Liu, *Mori dream Jacobian elliptic surfaces of Kodaira dimension one*, arXiv:2608.09002, first public 10 August 2026, https://arxiv.org/html/2608.09002v2 .
- A. Laface and S. Li, *Cox rings of Jacobian elliptic surfaces of Kodaira dimension one*, arXiv:2611.24570, first public 18 November 2026, https://arxiv.org/html/2611.24570v1 .
- *I-surfaces from surfaces with one exceptional unimodal point*, https://onlinelibrary.wiley.com/doi/full/10.1002/mana.202300218 (for classification context only).
- O. N. Popov, *The Cox Ring of a Del Pezzo Surface Has Rational Singularities*, arXiv:math/0402154, https://arxiv.org/abs/math/0402154 (contrast only).
