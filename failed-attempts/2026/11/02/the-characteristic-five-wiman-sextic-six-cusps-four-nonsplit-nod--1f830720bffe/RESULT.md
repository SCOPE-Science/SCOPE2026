# The characteristic-five Wiman sextic: six cusps, four nonsplit nodes, and its generalized Jacobian

## Finding
Let \(C\subset\mathbb P^2_{\mathbb F_5}\) be the reduced degree-six curve obtained by reducing the classical Wiman plane equation
\[
X^6+Y^6+Z^6+(X^2+Y^2+Z^2)(X^4+Y^4+Z^4)-12X^2Y^2Z^2=0.
\]
Then \(C\) is geometrically integral. Its full geometric singular locus consists of six \(\mathbb F_5\)-rational ordinary cusps of type \(A_2\) and four \(\mathbb F_5\)-rational ordinary nodes whose two tangent directions are conjugate over \(\mathbb F_{25}\). The normalization is \(\mathbb P^1_{\mathbb F_5}\). If \(T=\ker(N_{\mathbb F_{25}/\mathbb F_5}:\operatorname{Res}_{\mathbb F_{25}/\mathbb F_5}\mathbb G_m\to\mathbb G_m)\), then
\[
\operatorname{Pic}^0_{C/\mathbb F_5}\cong\mathbb G_a^6\times T^4
\]
as smooth connected algebraic groups over \(\mathbb F_5\).

For every integer \(m\ge1\), setting \(q=5^m\),
\[
\#C(\mathbb F_q)=q+1+4(-1)^{m+1},\qquad
\#\operatorname{Pic}^0_C(\mathbb F_q)=q^6\bigl(q-(-1)^m\bigr)^4.
\]
The Hasse–Weil zeta function of this singular projective curve is
\[
Z(C/\mathbb F_5,U)=\frac{(1+U)^4}{(1-U)(1-5U)}.
\]
In particular, \(C(\mathbb F_5)\) consists of exactly ten points, all singular.

## Assumptions and scope
All geometric singularity statements are over an algebraic closure of \(\mathbb F_5\). The four ordinary nodes are rational as *points* but geometrically split only after the quadratic field extension. The group \(\operatorname{Pic}^0\) is the connected generalized Picard variety of the specified singular, integral plane model; it is not the Jacobian of the smooth characteristic-zero normalization, its Néron model, or a stable-reduction invariant. The zeta function counts points on the singular curve, not its normalization.

## Proof
**1. A characteristic-five equation.** Put \(Q=X^2+Y^2+Z^2\), \(P=XYZ\), and \(\sigma_2=X^2Y^2+X^2Z^2+Y^2Z^2\). Newton identities give, over the integers,
\[
F=2Q^3-5Q\sigma_2-9P^2.
\]
Consequently, in characteristic five the original equation is exactly
\[
F=2Q^3+P^2=0.\tag{1}
\]
Its projective partial derivatives are \(2X(Q^2+Y^2Z^2)\), \(2Y(Q^2+X^2Z^2)\), and \(2Z(Q^2+X^2Y^2)\).

**2. Singular locus.** If one coordinate vanishes at a singular point, (1) forces \(Q=0\), and the other two coordinates cannot vanish. Each coordinate axis therefore contributes two points: for example \([0:1:2]\) and \([0:1:-2]\). All six are distinct and rational over \(\mathbb F_5\). If all coordinates are nonzero, the derivative equations imply \(X^2=Y^2=Z^2\). Conversely, the four points \([\pm1:\pm1:1]\) satisfy (1) and all its derivatives. This exhausts the geometric singular locus.

**3. Local analytic types and arithmetic branch behavior.** At a point of \(P=Q=0\), the functions \(P\) and \(Q\) form a regular parameter system: the coordinate axis and the smooth conic \(Q=0\) cross transversely. Thus (1) has completed local equation \(p^2+2q^3=0\). Since five is prime to both two and three, this is an ordinary \(A_2\) cusp with one rational normalization branch and delta invariant one.

At \([1:1:1]\) use \(Z=1\), \(X=1+u\), \(Y=1+v\). The lowest nonzero homogeneous part is
\[
2u^2+3uv+2v^2.
\]
Its discriminant is \(3\in\mathbb F_5\), a nonsquare. Changing the signs of \(X\) or \(Y\) gives the corresponding form at the other three nodes, with the same nonsquare discriminant. All four are ordinary nodes whose two geometric branches are exchanged by the arithmetic Frobenius. Each has delta invariant one and a single closed normalization preimage of degree two.

**4. Geometric integrality and normalization.** The six cusps are geometrically unibranch and have intersection multiplicity three with their respective coordinate axes, as is clear from \(F|_{X=0}=2(Y^2+Z^2)^3\), and cyclic permutations. Each irreducible component of the reduced curve must therefore meet any coordinate axis at an integral multiple of three, so its degree is divisible by three. Were there two components, each would have degree three and contain exactly one cusp on each of the three axes. These three distinct cusps would give a plane cubic total delta at least three, impossible for an integral cubic of arithmetic genus one. Hence the curve is geometrically integral. Its plane arithmetic genus is ten. The ten singularities contribute total delta ten, so its normalization has genus zero. A rational cusp has a unique rational normalization preimage; hence the smooth genus-zero normalization has an \(\mathbb F_5\)-point and is \(\mathbb P^1_{\mathbb F_5}\).

**5. Point counts and zeta function.** The normalization map is bijective on rational points away from singularities. At each rational cusp, one rational branch maps to one rational point, with no correction. At each of the four nodes, the normalization preimage is a closed point of degree two. If \(m\) is odd, that node contributes one rational point with no rational normalization preimage; if \(m\) is even, its two rational normalization preimages coalesce to one curve point. Hence the correction to \(\#\mathbb P^1(\mathbb F_{5^m})\) is \(+4\) for odd \(m\) and \(-4\) for even \(m\). The stated point formula follows. Applying the normalization zeta identity, each cusp contributes trivial ratio and each rational nonsplit node contributes \((1-U^2)/(1-U)=1+U\). This proves the zeta formula.

**6. Generalized Picard group.** For a geometrically integral projective curve with normalization \(\nu\), the local-units normalization sequence and \(\operatorname{Pic}^0(\mathbb P^1)=0\) identify its connected generalized Picard group with the product of local normalization-unit quotients. An \(A_2\) cusp has completed local ring \(k[[t^2,t^3]]\subset k[[t]]\). Its unit quotient is \(\mathbb G_a\), detected by the coefficient of \(t\). For a rational nonsplit node, the normalization has residue field \(\mathbb F_{25}\), so the unit quotient is \((\operatorname{Res}_{\mathbb F_{25}/\mathbb F_5}\mathbb G_m)/\mathbb G_m\), canonically isomorphic to the norm-one torus via \(a\mapsto a/a^5\). The disjoint singular supports give the direct product \(\mathbb G_a^6\times T^4\). Since \(\#T(\mathbb F_q)=q-(-1)^m\), the group point-count formula follows.

## Verification
The accompanying standalone `verify.py` checks the exact reduction identity in \(\mathbb F_5[X,Y,Z]\), the four nodal tangent discriminants, all six rational cusp supports, the arithmetic genus defect, and all projective point counts over \(\mathbb F_5\) and \(\mathbb F_{25}\) by exhaustive enumeration. Run `python3 verify.py` with SymPy installed. The full geometric assertions for every field extension follow from the displayed proof and do not rely on extrapolating finite enumerations.

## Relationship to prior work
Inoue and Kato, *On the geometry of Wiman's sextic* (preprint in the 2005 Kyoto collection; journal bibliographic record dated 14 July 2006), give the characteristic-zero equation and geometric constructions under an explicit assumption excluding characteristics two, three and five. Giulietti, Kawakita, Lia and Montanucci, *An \(\mathbb F_{p^2}\)-maximal Wiman's sextic and its automorphisms* (arXiv:1805.06317, first posted 15 May 2018), explicitly state that the characteristic-five normalization is rational. The genus-zero conclusion alone is therefore **not** claimed new. The extra assertion here is the complete arithmetic singularity basket, Frobenius splitting of the four nodes, explicit generalized Picard group over the prime field, and all-extension point count and zeta formula. These do not follow merely from knowing that the normalization is rational.

## Limitations
The result does not determine a stable model, the Néron model of the generic Jacobian, or conductor exponents of an arithmetic family. The bibliographic search did not establish global priority against every historical or unindexed source. The first source date is the earliest precisely day-dated public record verified for the 2005-era source; a day-specific date of the earlier preprint was not established. Independent validation has not been performed.

## References
1. N. Inoue and F. Kato, *On the geometry of Wiman's sextic*, Journal of Mathematics of Kyoto University 45 (2005), 743–757, DOI: `10.1215/KJM/1250281655`. Author-preprint text: `https://www.math.kyoto-u.ac.jp/preprint/2005/2inoue.kato.pdf`. Bibliographic date record: `https://portal.mardi4nfdi.de/wiki/Publication:2494637`.
2. M. Giulietti, M. Kawakita, S. Lia and M. Montanucci, *An \(\mathbb F_{p^2}\)-maximal Wiman's sextic and its automorphisms*, arXiv:1805.06317 (2018), published in *Advances in Geometry* 21 (2021), 451–461; Remark 3.1 and Theorem 3.4 discuss characteristic five.
