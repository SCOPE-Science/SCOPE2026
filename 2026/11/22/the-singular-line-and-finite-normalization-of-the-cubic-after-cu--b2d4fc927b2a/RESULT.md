# The singular line and finite normalization of the cubic-after-cubic composition threefold

## Finding
Let \(W=\langle t,t^2,t^3,t^4,t^5,t^6,t^7,t^9\rangle_{\mathbb C}\), and let \(X\subset\mathbb P(W)\) be the projective closure of the locus of normalized degree-nine polynomials \(G\circ H\), where the right factor is cubic and centered and the left factor is cubic with zero constant term. The variety \(X\) is an irreducible projective threefold of degree six, as established by Piene and Shapiro. Define
\[
N=\mathbb P_{\mathbb P^1}\bigl(\mathcal O(-1)\oplus\mathcal O(-2)\oplus\mathcal O(-3)\bigr),\qquad
\nu:N\longrightarrow X,\quad (H,[c_1:c_2:c_3])\longmapsto[c_1H+c_2H^2+c_3H^3],
\]
where \([H]=[a t^3+b t]\in\mathbb P^1\), and the expression is understood with its standard bundle transition weights.

**Theorem.** The morphism \(\nu\) is finite and birational, and is therefore the normalization of \(X\). The complete reduced singular locus is the line
\[
\operatorname{Sing}(X)_{\mathrm{red}}=L:=\mathbb P\langle t,t^3\rangle.
\]
For every \([\beta t+\alpha t^3]\in L\) with \(\alpha\ne0\), the normalization has exactly two distinct preimages. The two smooth local branches have projective tangent spaces of dimension three meeting precisely along the tangent line to \(L\). Above \([t]\), the normalization has exactly one preimage, and its differential has a one-dimensional kernel. Moreover, \(\nu^{-1}(L)_{\mathrm{red}}\) consists of two smooth rational curves meeting once, over \([t]\).

## Assumptions and scope
All schemes and tangent spaces are over \(\mathbb C\). The singular locus assertion concerns the reduced support, not the defining scheme structure of the Jacobian ideal or conductor. The map \(\nu\) and the degree-six assertion are inherited from the projective-bundle construction of Piene--Shapiro. The new content is finiteness/normalization and the exact singular and branch loci, their fibers, and their tangent behavior. No statements are made about other factorization pairs, other components, or positive characteristic.

## Proof
Write \(H=a t^3+b t\). Its image \(F=c_1H+c_2H^2+c_3H^3\) has coefficients, in the order \(t,t^2,t^3,t^4,t^5,t^6,t^7,t^9\),
\[
(c_1b,\ c_2b^2,\ c_1a+c_3b^3,\ 2c_2ab,\ 3c_3ab^2,\ c_2a^2,\ 3c_3a^2b,\ c_3a^3).
\tag{1}
\]
The three nonzero polynomials \(H,H^2,H^3\) are linearly independent, so this is everywhere a well-defined morphism from the smooth projective bundle \(N\) to its image \(X\). Its birationality and the identification with the projective composition closure are also given by the composition-bundle construction in the cited article.

**Finite fibers.** If \(a\ne0\), scale \(H=t^3+b t\). A polynomial \(F\) of degree nine has \(c_3\ne0\) and recovers \(b=[t^7]F/(3[t^9]F)\). A polynomial of degree six has \(c_3=0,c_2\ne0\) and recovers \(b=[t^4]F/(2[t^6]F)\). A polynomial of degree three has \(c_2=c_3=0\), so its line \([F]\) determines \([H]\). Thus each point has at most one preimage with \(a\ne0\). If \(a=0\), then \(H=t\) and \(F\in\mathbb P\langle t,t^2,t^3\rangle\), with its outer coefficients uniquely determined. Overlap between these cases occurs exactly on \(L\setminus\{[t]\}\); at \([t]\), the preimages coincide. Therefore every geometric fiber is finite. Properness and quasi-finiteness make \(\nu\) finite. As \(N\) is smooth and \(\nu\) is birational, it is the normalization.

**Immersion away from one source point.** On the chart \(a=1\), use \(H=t^3+b t\). The tangent directions in coefficient space are spanned by \(H,H^2,H^3\) and by \(t(c_1+2c_2H+3c_3H^2)\). The six columns \(H,H^2,H^3,t,tH,tH^2\), evaluated in rows corresponding to powers \(t,t^3,t^4,t^6,t^7,t^9\), have determinant exactly \(1\), independent of \(b\). Hence the fourth direction is independent of the first three for every nonzero \((c_1,c_2,c_3)\), and \(\nu\) is immersive there.

On the chart \(b=1\), take \(H=t+a t^3\). At \(a=0\), the base-direction derivative is
\[
\left.\partial_a F\right|_{a=0}=c_1t^3+2c_2t^4+3c_3t^5.
\]
Modulo the fiber tangent span \(\langle t,t^2,t^3\rangle\), it vanishes precisely when \(c_2=c_3=0\). Thus \(\nu\) is immersive except at the unique source point above \([t]\), where its differential has rank two instead of three.

**Exact singular support.** Every \(F\notin L\) has a unique normalization preimage at which \(\nu\) is immersive. In local rings, injectivity of the tangent map makes the image cotangent map surjective; consequently \(\mathfrak m_B=\mathfrak m_A B\) for the finite local extension \(A\subset B\). Since the residue fields agree, Nakayama's lemma gives \(A=B\). Hence \(\nu\) is locally an isomorphism and \(X\) is smooth off \(L\). Each point of \(L\setminus\{[t]\}\) has two normalization preimages and is therefore nonnormal and singular. The point \([t]\) is also singular, because at its sole normalization preimage \(\nu\) is not immersive, whereas normalization of a smooth point is an isomorphism. Therefore the reduced singular locus is precisely \(L\).

**Double-branch tangents.** Fix \(F=\beta t+\alpha t^3\), \(\alpha\ne0\). One preimage has \(H=t\), and the other has \(H=F\) and the outer factor linear. The corresponding ambient vector tangent spaces are
\[
T_A^{\mathrm{vec}}=\langle t,t^2,t^3,t^5\rangle,\qquad
T_B^{\mathrm{vec}}=\langle t,t^3,F^2,F^3\rangle.
\]
The coefficient matrix of \(t,t^2,t^3,t^5,F^2,F^3\) in powers \(t,t^2,t^3,t^5,t^6,t^9\) has determinant \(\alpha^5\ne0\). Therefore the vector tangent spaces meet exactly in \(\langle t,t^3\rangle\), and their projectivizations meet along \(L\).

**The exceptional point.** In the affine chart \(H=t+a t^3\) and outer coordinates \((1,\lambda,\mu)\), the map becomes
\[
[t+\lambda t^2+(a+\mu)t^3+2a\lambda t^4+3a\mu t^5+a^2\lambda t^6+3a^2\mu t^7+a^3\mu t^9].
\tag{2}
\]
In this chart the reduced inverse image of \(L\) has equations \(\lambda=0\) and \(a\mu=0\). Globally its two components are \(\{a=0,c_2=0\}\simeq\mathbb P^1\) and \(\{c_2=c_3=0\}\simeq\mathbb P^1\); they intersect only where \(a=\mu=0\), above \([t]\). This also verifies the asserted unique differential rank drop.

## Verification
The accompanying `verify_composition_33.py` uses exact polynomial arithmetic over \(\mathbb Z\) to check identity (1), the constant determinant \(1\), the transverse-tangent determinant \(\alpha^5\), the differential on the \(a=0\) chart, and expression (2). Execute `python verify_composition_33.py` with Python 3 and SymPy. These algebraic certificates support the proof; finite numerical sampling is not used to establish the theorem. The finiteness and local-ring arguments are proved mathematically rather than inferred from the script.

## Relationship to prior work
Piene--Shapiro, *Composition loci, invariant Bezoutians, and finite-orbit correspondences*, Theorem 1.1 and Section 6.1, give the birational bundle model and the degree-six numerical invariant for the cubic-after-cubic component. Their final discussion identifies singularities at infinity as a separate question. The present theorem specifies its complete reduced singular locus and the finite normalization geometry, neither implied merely by a birational projective-bundle parameterization. Von zur Gathen--Matera develop the affine decomposable interpolation locus, whose affine regularity does not determine the projective boundary singularities.

## Limitations
No scheme-theoretic conductor, embedded Jacobian structure, completed local equations at the exceptional point, characteristic-dependent behavior, or higher-degree analogous case is claimed. The novelty assessment is limited to inspected sources and research-record searches; a less directly indexed classical projection or normalization result could contain an equivalent statement. An independent mathematical audit has not been performed.

## References
1. Ragni Piene and Boris Shapiro, *Composition loci, invariant Bezoutians, and finite-orbit correspondences*, arXiv:2611.16763v1, first public 2026-11-12, https://arxiv.org/abs/2611.16763; particularly Theorem 1.1, Section 6.1, and the closing discussion of singularities at infinity.
2. Joachim von zur Gathen and Guillermo Matera, *Interpolation by decomposable univariate polynomials*, arXiv:2103.15926, https://arxiv.org/abs/2103.15926 (affine decomposition/interpolation comparison).
