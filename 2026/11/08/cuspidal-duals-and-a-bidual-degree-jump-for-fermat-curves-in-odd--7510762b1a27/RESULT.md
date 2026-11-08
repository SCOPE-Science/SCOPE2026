# Cuspidal duals and a bidual degree jump for Fermat curves in odd characteristic

## Finding
Fix an odd prime \(p\), an integer \(e\geq1\), and \(q=p^e\). Put \(d=2q+1\), and let \(k=\overline{\mathbb F}_p\). Let \(C\subset\mathbb P^2_k\) be the smooth Fermat plane curve
\[
C:\quad X^d+Y^d+Z^d=0.
\]
In the dual plane, write the coordinates as \([U:V:W]\). The **reduced projective dual** \(C^\vee\) has the single irreducible equation
\[
G(U,V,W)=U^{2d}+V^{2d}+W^{2d}-2(U^dV^d+U^dW^d+V^dW^d)=0.
\]
It has degree \(2d\). The Gauss morphism \(C\to C^\vee\) has inseparable degree \(q\) and separable degree one. The coordinatewise squaring morphism
\[
\sigma:C\longrightarrow C^\vee,\qquad[X:Y:Z]\longmapsto[X^2:Y^2:Z^2]
\]
is the normalization morphism.

The full geometric singular locus of \(C^\vee\) consists of exactly \(3d\) points: for each coordinate position, put that coordinate equal to zero and require equality of the \(d\)-th powers of the other two coordinates. Each singularity is one-branch with completed geometric local ring
\[
 k[[u,v]]/(v^2-4u^d).
\]
In particular, each has multiplicity \(2\), a unique tangent with intersection multiplicity \(d\), and delta invariant \((d-1)/2\). There are no other singular points, and the normalization genus is \((d-1)(d-2)/2\).

Let \((C^\vee)^\vee\) denote the projective dual of the **reduced** curve \(C^\vee\). The bidual is the image of \(C\) under
\[
[X:Y:Z]\longmapsto[X^{d-2}:Y^{d-2}:Z^{d-2}],
\]
and this map is generically separable and birational onto its image. Thus
\[
\boxed{\deg (C^\vee)^\vee=d(d-2).}
\]
In particular this family is nonreflexive, and its bidual has degree strictly greater than \(d\).

## Assumptions and scope
The base field is algebraically closed of characteristic \(p>2\). The integers satisfy \(e\geq1\), \(q=p^e\), and \(d=2q+1\), so \(d\) is odd and neither \(d\) nor \(d-2\) is divisible by \(p\). Singularities and curve degrees are geometric. The dual is the *reduced* Zariski closure of the Gauss image, not the possibly nonreduced image scheme of a purely inseparable map. The bidual likewise means the reduced dual of that reduced curve. The local-ring statement concerns the completed ring after choosing local coordinates (equivalently after an étale change of local parameters).

## Proof
**1. Smoothness, power maps, and the dual equation.** Since \(p\nmid d\), the gradient of the Fermat equation cannot vanish at a projective point, so \(C\) is smooth and irreducible. Consider the ambient map \(\sigma_2:[X:Y:Z]\mapsto[X^2:Y^2:Z^2]\). It is finite. On the coordinate torus it is étale, since \(2\) is invertible. To prove that \(\sigma_2|_C\) is injective on geometric points, suppose two points with equal squares differ by a diagonal choice of signs. After quotienting by a common global sign, the choices amount to flipping one nonzero coordinate or two nonzero coordinates. Subtracting the two Fermat equations would force the flipped coordinate, or the single unflipped coordinate, to be zero. In either case the two original projective points coincide. Thus \(\sigma_2|_C\) is finite, generically separable, and of degree one; it is finite birational.

Set \(A=X^d\), \(B=Y^d\), and \(E=Z^d\). The identity
\[
A^4+B^4+E^4-2(A^2B^2+A^2E^2+B^2E^2)
=-(A+B+E)(-A+B+E)(A-B+E)(A+B-E)
\]
shows that \(G\) vanishes at every image point \([X^2:Y^2:Z^2]\) of \(C\). A general line in the target pulls back to a quadric on \(C\), of degree \(2d\). As the map has degree one, the image is an irreducible curve of degree \(2d\). Since \(G\) also has degree \(2d\), its zero divisor is exactly that reduced irreducible image. As \(C\) is normal, \(\sigma:C\to V(G)\) is its normalization.

The Gauss map of \(C\) is
\[
[X:Y:Z]\longmapsto[X^{d-1}:Y^{d-1}:Z^{d-1}]=[X^{2q}:Y^{2q}:Z^{2q}].
\]
This is the composition of \(\sigma\) with the \(q\)-power Frobenius map on \(V(G)\), because \(G\) has coefficients in the prime field. Frobenius is surjective on geometric points and has inseparable degree \(q\) on the function field of a curve. The reduced image is therefore \(V(G)\) and the Gauss map has precisely the stated separable and inseparable degrees.

**2. Global singular locus.** Differentiation gives, for example,
\[
G_U=2d\,U^{d-1}(U^d-V^d-W^d),
\]
with analogous formulas in the other two coordinates. At a point with \(UVW\ne0\), simultaneous vanishing of all derivatives would imply \(U^d=V^d+W^d\) and \(V^d=U^d+W^d\), whence \(2W^d=0\), a contradiction. On \(U=0\), the equation becomes \((V^d-W^d)^2=0\); its \(d\) distinct geometric zeros are singular, because all three partial derivatives vanish. The same argument applies to \(V=0\) and \(W=0\). None lies on two coordinate lines, since \(G(0,0,1)=1\). There are exactly \(3d\) singular points and no others.

**3. Analytic singularity and genus.** Work near \(U=0\) on the chart \(W=1\), at a singular point \(V^d=1\). Directly in the local ring,
\[
G(U,V,1)=(V^d-1-U^d)^2-4U^d.
\]
The coordinate change \(u=U\), \(v=V^d-1-U^d\) is étale at the point, since its Jacobian determinant with respect to \((U,V)\) has nonzero factor \(dV^{d-1}\). This yields \(v^2-4u^d\), which is irreducible and unibranch because \(d\) is odd and \(p\ne2\). Its normalization has local parameter \(t\) with \(u=t^2\), \(v=2t^d\), and hence delta invariant \((d-1)/2\). Permuting variables covers all singularities. Since \(C\) is the normalization of \(V(G)\), its genus is the smooth plane-curve genus \((d-1)(d-2)/2\). Independently, the difference between the arithmetic genus of a degree-\(2d\) plane curve and this genus is \(3d(d-1)/2\), exactly the sum of the \(3d\) delta invariants.

**4. The bidual.** At a torus point of \(C\), evaluate the gradient of \(G\) at its normalization image. Using \(X^d+Y^d+Z^d=0\), one obtains
\[
G_U(X^2,Y^2,Z^2)
=4d\,(XYZ)^d X^{d-2},
\]
and the corresponding expressions with \(Y^{d-2}\) and \(Z^{d-2}\). Therefore the reduced dual of \(V(G)\) is the image of \(C\) under the exponent-\((d-2)\) map. Put \(m=d-2\). We have \(p\nmid m\) and \(\gcd(m,d)=1\). The ambient \(m\)-th power map is étale on the torus. A second preimage of a generic torus point would have the form \([\zeta X:\xi Y:Z]\) with \(\zeta^m=\xi^m=1\) and would satisfy
\[
(\zeta^d-1)X^d+(\xi^d-1)Y^d=0.
\]
For generic \([X:Y:Z]\in C\), the ratio \(X^d/Y^d\) is nonconstant, so this forces \(\zeta^d=\xi^d=1\). Coprimality gives \(\zeta=\xi=1\). Thus this restricted power map has generic degree one and is separable. Pulling back a general line gives degree \(md\) on \(C\), so the image degree is \(md=d(d-2)\). This concludes the proof.

## Verification
The standalone script `verify_fermat_dual.py` uses exact arithmetic in \(\mathbb F_9\) and \(\mathbb F_{25}\), testing the cases \((p,q,d)=(3,3,7)\) and \((5,5,11)\). It exhausts the projective rational points of the two planes, compares the Fermat curve with the equation \(G=0\), checks the geometric-point injectivity on these test sets, matches all *field-rational* singular points with the coordinate-axis prediction, and evaluates the gradient identity on torus points. Run with `python3 verify_fermat_dual.py`; the archived output is `verification_output.txt`. These finite checks do not establish the theorem over the algebraic closures or for arbitrary \(e\). The global proof above supplies those steps.

## Relationship to prior work
The Fermat curve and the phenomenon of inseparable Gauss maps in positive characteristic are classical. Hirschfeld, Korchmáros, and Torres give general duality and inseparable-degree formulas for smooth plane curves (Chapter 5, Section 5.11 of *Algebraic Curves over a Finite Field*). These formulas predict the degree \(2d\) here once the inseparable degree \(q\) is known, but they do not by themselves state the displayed discriminant equation, classify its \(3d\) local cusps, or compute this bidual image and degree. Arakelian and Borges (arXiv:1502.05953, first posted February 20, 2015) study a different invariant, Frobenius nonclassicality of Fermat curves with respect to plane cubics. Komeda (arXiv:2002.10691, first posted February 25, 2020) studies Gauss images and singularities for degree \(q^2+q+1\), including a Ballico–Hefez connection for the corresponding Fermat curve. That degree family is different from the present odd-characteristic \(2q+1\) family. These are comparisons of mathematical content, not claims that literature searching proves historical priority.

## Limitations
The result concerns only the specified Fermat degrees in odd characteristic. It does not classify the singularities of the bidual curve or all higher iterated duals; it does not claim a new general Gauss-map theorem. Historical priority is provisional: older unindexed work on explicit Fermat duals or an implicit special case of a broader duality result may exist. The computation covers only two finite-field models and is corroborative, not a proof of the infinite family. No independent scientific validation is claimed.

## References
1. J. W. P. Hirschfeld, G. Korchmáros, F. Torres, *Algebraic Curves over a Finite Field*, Princeton University Press (2008), Chapter 5, Section 5.11, ISBN 9780691096797.
2. N. Arakelian and H. Borges, *Frobenius nonclassicality of Fermat curves with respect to cubics*, arXiv:1502.05953 (2015-02-20 initial submission), https://arxiv.org/abs/1502.05953.
3. K. Komeda, *Singularities of the dual curve of a certain plane curve in positive characteristic*, arXiv:2002.10691 (2020-02-25 initial submission), https://arxiv.org/abs/2002.10691.
