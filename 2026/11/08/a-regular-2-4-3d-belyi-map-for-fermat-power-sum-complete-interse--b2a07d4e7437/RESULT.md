# A regular \((2,4,3d)\) Belyi map for Fermat power-sum complete-intersection curves

## Finding
For every integer \(d\ge 3\) with \(d\ne4\), let \(C_d\subset\mathbf P^3_{\mathbf C}\) be the complete intersection
\[
\sum_{i=0}^{3}x_i^d=\sum_{i=0}^{3}x_i^{2d}=0.
\]
Put \(z_i=x_i^d\), and let \(e_j=e_j(z_0,z_1,z_2,z_3)\) be the elementary symmetric polynomial of degree \(j\). Then
\[
\beta_d:C_d\longrightarrow\mathbf P^1,\qquad
\beta_d=\frac{27e_3^4}{256e_4^3}
\]
is a **regular Belyi map**, with branch values exactly \(0,1,\infty\), respective ramification indices \(4,2,3d\) at **every** point above each value. Its degree and geometric deck group are
\[
\deg\beta_d=24d^3,\qquad
\operatorname{Deck}(\beta_d)=\operatorname{Aut}_{\mathbf C}(C_d)
\cong (\mathbf Z/d\mathbf Z)^3\rtimes\mathfrak S_4.
\]
The fiber cardinalities above \(0,1,\infty\) are respectively \(6d^3,12d^3,8d^2\), and
\[
g(C_d)=1+d^2(3d-4).
\]
In particular \(C_d\) is quasiplatonic: quotienting by its **entire** automorphism group gives a genus-zero orbifold with signature \((2,4,3d)\). The map and curve are defined over \(\mathbf Q\) (the deck group is geometric).

## Assumptions and scope
We work over \(\mathbf C\), in characteristic zero. The integer restriction \(d\ne4\) is used only to invoke the full-automorphism theorem for smooth Fermat complete intersections. The explicit Belyi map and its passport also exist for \(d=4\), but this statement does not claim identification with the entire automorphism group there. The polynomial \(e_3\) is the sum of the four triple products of the \(z_i\), and \(e_4=z_0z_1z_2z_3\). The expression for \(\beta_d\) is the ratio of two homogeneous forms of degree \(12d\); it is interpreted as \([27e_3^4:256e_4^3]\), including at its poles.

## Proof
**1. Smooth cover of a conic.** Set
\[
Q=\{[z_0:\cdots:z_3]:\sum z_i=\sum z_i^2=0\}\subset\mathbf P^3.
\]
The two equations of \(Q\) have independent gradients at every projective point: proportionality forces all \(z_i\) equal, and then the first equation forces all zero. Thus \(Q\) is a smooth conic in the plane \(\sum z_i=0\). The coordinatewise power map \(\pi:C_d\to Q\) is finite of generic degree \(d^3\): over a point with all coordinates nonzero, independent choices of four \(d\)-th roots modulo simultaneous scaling give \(d^3\) points. The curve \(C_d\) is smooth: dependence of its two Jacobian rows at any point implies that all nonzero \(x_i^d\) have the same nonzero value; their sum could then not vanish. As a smooth complete intersection of two surfaces in \(\mathbf P^3\), it is connected and therefore irreducible. The group \(D=(\mu_d)^4/\mu_d\cong(\mu_d)^3\) acts diagonally, and \(C_d/D\cong Q\).

**2. Symmetric quotient and its rational coordinate.** On \(Q\), Newton's identity \(2e_2=e_1^2-\sum z_i^2\) gives \(e_1=e_2=0\). The elementary symmetric theorem and exactness of invariants in characteristic zero give
\[
\bigl(\mathbf C[z_0,z_1,z_2,z_3]/(e_1,e_2)\bigr)^{\mathfrak S_4}
=\mathbf C[e_3,e_4].
\]
Consequently the coarse quotient \(Q/\mathfrak S_4=\operatorname{Proj}\mathbf C[e_3,e_4]\) is \(\mathbf P^1\) with rational coordinate \(e_3^4/e_4^3\), because the two generators have weights \(3,4\). The forms \(e_3,e_4\) never vanish simultaneously on \(Q\): otherwise all coefficients of the monic polynomial \(\prod_{i=0}^3(T-z_i)\) except the leading coefficient vanish, forcing all \(z_i=0\). Hence \(\beta_d\) is a morphism on all of \(C_d\), and the composite \(C_d\to Q\to Q/\mathfrak S_4\) is the stated formula. The coordinate permutations normalize \(D\), so this is a Galois quotient with group \(G=D\rtimes\mathfrak S_4\) of order \(24d^3\).

**3. Complete branch analysis on the conic.** The polynomial whose roots are the \(z_i\) is
\[
P(T)=T^4-e_3T+e_4,
\qquad \operatorname{Disc}(P)=256e_4^3-27e_3^4.
\]
The zero divisor of \(e_3\) on the conic has degree \(6\) and consists of six distinct points: its root sets are (up to scale) the four distinct fourth roots of a nonzero number, with \(4!/4=6\) different projective orderings. Thus \(\beta_d\) has six conic zeros of order \(4\).

The zero divisor of \(e_4\) consists of eight distinct conic points. Indeed exactly one \(z_i\) is zero at each, and the other three coordinates are proportional to \(1,\omega,\omega^2\), where \(\omega\) is a primitive cube root of unity. Each coordinate hyperplane meets \(Q\) in two transverse points. Therefore \(e_4\) has simple zeros at eight points and the quotient map on \(Q\) has poles of order \(3\) there.

Finally \(\beta_d-1=-(256e_4^3-27e_3^4)/(256e_4^3)\). The discriminant locus is the union of the six conic intersections \(z_i=z_j\). For any fixed pair, scale its common coordinate to \(1\); the two remaining coordinates are the distinct roots of \(T^2+2T+3\). There is neither a triple equality nor a pair of distinct double equalities on \(Q\), by the equations \(e_1=e_2=0\). Hence there are \(12\) distinct points, with each difference \(z_i-z_j\) a local parameter. Because the discriminant is \(\prod_{i<j}(z_i-z_j)^2\), \(\beta_d-1\) has order \(2\) at each of those points. The three ramification contributions are \(6(4-1)+8(3-1)+12(2-1)=46\), matching \(2\cdot24-2\) by Riemann–Hurwitz, so there is no additional ramification of \(Q\to\mathbf P^1\).

**4. Pullback ramification and full group.** The map \(\pi\) is étale over points of \(Q\) where all \(z_i\ne0\). At each of the eight points with exactly one \(z_i=0\), the corresponding \(x_i\) is a local coordinate and \(z_i=x_i^d\), so \(\pi\) is ramified with index \(d\). These eight points are exactly the poles of \(\beta\) on \(Q\). Thus composing gives ramification indices \(4,2,3d\) above \(0,1,\infty\). Every point over a given branch value has the stated common index because the map is Galois. Dividing \(24d^3\) by the three indices gives the listed fiber sizes.

The full automorphism theorem of Duque Franco–Liendo–Palomino (Theorem 3.6, arXiv:2607.12139) applies here: \(d\ge3\), \(2d>d\), neither degree is \(4\) when the complete intersection is a curve, and the curve is smooth. Their theorem gives \(\operatorname{Aut}(C_d)=D\rtimes\mathfrak S_4\), so \(\beta_d\) is precisely the quotient by the full group.

**5. Genus cross-check.** Adjunction for a smooth complete intersection of degrees \(d\) and \(2d\) in \(\mathbf P^3\) gives
\[
2g-2=2d^2(3d-4).
\]
The ramification passport independently gives
\[
2g-2=24d^3\left(-2+\left(1-\tfrac14\right)
+\left(1-\tfrac12\right)+\left(1-\tfrac1{3d}\right)\right)
=2d^2(3d-4),
\]
confirming the genus and all branching contributions.

## Verification
The supporting algebraic identities used in the argument can be checked with `python3 verify.py` (requires SymPy). The verifier checks the quartic discriminant symbolically, the elementary symmetric identity imposing \(e_2=0\), the double-coordinate quadratic, and Riemann–Hurwitz/fiber arithmetic over a range of degrees. Its successful output is `CERTIFICATE_OK`. These finite/arithmetic checks are **not** substituted for the all-degree smoothness, invariant-theory, or ramification proof above.

## Relationship to prior work
Duque Franco, Liendo and Palomino establish the smoothness criterion and full automorphism groups for Fermat complete intersections, but do not state the regular Belyi quotient or the passport \((2,4,3d)\) for these curves. The use of \(\mathfrak S_4\) on a conic is classical, as is the quartic-discriminant description of the octahedral quotient; neither underlying principle is claimed as new. The assertion here is their explicit integration with the Fermat power-sum curve into an **all-degree** regular Belyi morphism whose deck group is the **full** automorphism group. Kontogeorgis (2002) concerns automorphism groups of Fermat-like varieties. Terasoma (1988) treats Fermat complete intersections in a more general context; its full text could not be inspected here, so overlap with older special-curve descriptions remains a priority risk.

## Limitations
The result concerns \(d\ge3\), \(d\ne4\), over characteristic zero. The same displayed map is Belyi at the exceptional value \(d=4\), but no assertion about its full automorphism group is included. The theorem does not classify all dessins with this deck group or all Fermat complete intersections of different degrees. Its claim of historical novelty is qualified by the limited accessibility of some older primary material. No independent mathematical audit has been performed.

## References
- J. Duque Franco, A. Liendo, A. J. Palomino, *Automorphism groups of rigid complete intersections*, arXiv:2607.12139v1, first posted 2026-07-13, especially Proposition 3.4 and Theorem 3.6.
- A. Kontogeorgis, *Automorphisms of Fermat-like varieties*, Manuscripta Math. 107 (2002), 187–205, DOI:10.1007/s002290100233.
- T. Terasoma, *Complete intersections of hypersurfaces: The Fermat case and the quadric case*, Japanese J. Math. 14 (1988), 309–384, DOI:10.4099/math1924.14.309.
- N. Elkies, *Computational Techniques in Number Theory and Algebraic Geometry*, course notes (2012), discussion of the octahedral \(\mathfrak S_4\)-action on the anisotropic conic and Belyi maps; https://people.math.harvard.edu/~elkies/M263.12/index.html.
