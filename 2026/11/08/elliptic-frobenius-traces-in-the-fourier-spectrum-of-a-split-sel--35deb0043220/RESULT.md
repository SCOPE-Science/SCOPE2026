# Elliptic Frobenius traces in the Fourier spectrum of a split self-adjoint nilpotent cone

## Finding
For every odd prime power \(q\), the additive Fourier transform of the indicator of the rank-at-most-one square-zero locus in the four-dimensional split orthogonal self-adjoint algebra is an **integer**, exactly determined by rational point counts on bidegree-\((2,2)\) divisors of a split quadric. On the smooth-divisor locus these coefficients are precisely the integers
\[
-q(t+1),\qquad t\in\mathcal W_q,\quad q+1-t\ge 2,
\]
where \(\mathcal W_q\) denotes the elliptic Frobenius traces allowed by Waterhouse's theorem. In particular, the trace \(t=-1\) occurs for every odd \(q\), so this natural convolution operator is **singular** for every such field. At least \(q(q-1)\) distinct frequency matrices are Fourier zeros.

## Assumptions and scope
Let \(q=p^f\) with odd prime \(p\), and let \(k=\mathbb F_q\). Choose coordinates \(z=(z_0,z_1,z_2,z_3)^T\) on \(W=k^4\) and define
\[
Q(z)=z_0z_3-z_1z_2,\qquad G_{03}=G_{30}=1/2,\quad G_{12}=G_{21}=-1/2,
\]
all other entries of \(G\) being zero. Thus \(Q(z)=z^TGz\) and \(G\) is invertible and symmetric. Set
\[
S_G=\{A\in M_4(k):A^TG=GA\},\quad
\mathcal N_G=\{X\in S_G:\operatorname{rank}X\le1,\ X^2=0\}.
\]
The additive group \(S_G\) has size \(q^{10}\). Its trace pairing \((A,X)\mapsto\operatorname{tr}(AX)\) is nondegenerate since \(p\ne2\). Fix any nontrivial additive character \(\psi:k\to\mathbb C^\times\) and use the **unnormalized** Fourier convention
\[F(A)=\sum_{X\in\mathcal N_G}\psi(\operatorname{tr}(AX)).\]
Let \(\Sigma=\{[z]\in\mathbb P^3_k:Q(z)=0\}\cong\mathbb P^1_k\times\mathbb P^1_k\), via
\[
([s:t],[u:v])\mapsto[su:sv:tu:tv].
\]
The quadratic polynomial \(P_A(z)=z^TGAz\) restricts to a section of \(\mathcal O_{\Sigma}(2,2)\). Let \(C_A\) be its zero divisor; if this section is identically zero, define its rational point count as \(|\Sigma(k)|=(q+1)^2\). Define \(\mathcal W_q\) **externally** as the set of integer Frobenius traces of elliptic curves over \(k\), characterized explicitly by Waterhouse's classification, reproduced in Humphries, Lemma 3.2 [2].

## Proof
**(1) Cone parametrization.** If \(X\in S_G\) is nonzero of rank one, write \(X=zw^T\). Then \(GX=(Gz)w^T\) is symmetric, so \(w=cGz\) for a unique nonzero scalar once \(z\ne0\) is fixed. Hence \(X=czz^TG\). As \(X^2=c^2Q(z)zz^TG\), its square vanishes precisely when \(Q(z)=0\). Choosing a representative of each \([z]\in\Sigma(k)\), the cone decomposes disjointly as the zero matrix and \(q-1\) nonzero scalar multiples of \(zz^TG\) for each \([z]\). It has \(1+(q-1)(q+1)^2\) elements.

**(2) Exact character transform.** Because \(\operatorname{tr}(Azz^TG)=z^TGAz\), character orthogonality gives \(\sum_{c\in k^\times}\psi(cP_A(z))=q-1\) if \(P_A(z)=0\), and \(-1\) otherwise. Summing over the \((q+1)^2\) rational points on \(\Sigma\) yields
\[
F(A)=1- (q+1)^2+q|C_A(k)|=q\bigl(|C_A(k)|-q-2\bigr).
\]
This formula includes the zero section, for which \(F(A)=1+(q-1)(q+1)^2\). It is exact for every frequency and is independent of the chosen nontrivial additive character.

**(3) Every bidegree-\((2,2)\) divisor is represented.** The map \(A\mapsto GA\) bijects \(S_G\) with the ten-dimensional space of symmetric matrices, hence \(A\mapsto P_A\) with all homogeneous quadrics on \(W\), because \(p\ne2\). The exact sequence \(0\to\mathcal O_{\mathbb P^3}\xrightarrow{\cdot Q}\mathcal O_{\mathbb P^3}(2)\to\mathcal O_\Sigma(2,2)\to0\), and \(H^1(\mathbb P^3,\mathcal O)=0\), show that restriction is onto, with kernel precisely the one-dimensional space \(kQ\). Thus each bidegree-\((2,2)\) section has exactly \(q\) frequency lifts.

**(4) Smooth case and elliptic trace.** The adjunction formula on \(\mathbb P^1\times\mathbb P^1\) gives arithmetic genus \((2-1)(2-1)=1\). Any smooth divisor \(C_A\) is a geometrically integral genus-one curve; the Weil bound implies \(|C_A(k)|\ge q+1-2\sqrt q>0\) for every odd \(q\ge3\), so it has a rational origin and is an elliptic curve. Write \(t=q+1-|C_A(k)|\). The formula in (2) becomes \(F(A)=-q(t+1)\). Necessarily \(t\in\mathcal W_q\). Also \(|C_A(k)|\ge2\), because the two degree-two projections give **distinct** rational divisor classes of degree two. Indeed, if they coincided, their complete pencils would differ only by a target automorphism, making their combined map factor through a one-dimensional graph, contradicting a divisor of bidegree \((2,2)\) being embedded. Therefore \(q+1-t\ge2\).

**(5) Realizing every allowed elliptic trace with at least two points.** Let \(t\in\mathcal W_q\) and \(q+1-t\ge2\). Choose a corresponding elliptic curve \(E/k\), its rational origin \(O\), and another rational point \(P\ne O\). The degree-two complete linear series \(|2O|\) and \(|O+P|\) yield finite maps \(f_1,f_2:E\to\mathbb P^1\), each of degree two. Their deck involutions are respectively \(x\mapsto -x\) and \(x\mapsto P-x\). Since \(P\ne O\), no two geometric points are identified by both maps. Moreover their ramification loci are disjoint: the first requires \(2x=O\), the second \(2x=P\). Consequently \((f_1,f_2):E\hookrightarrow\mathbb P^1\times\mathbb P^1\) is a closed immersion with smooth bidegree-\((2,2)\) image. Surjectivity in (3) produces a frequency \(A\) cutting out this image. Thus **every** \(t\) in the specified set is attained. This argument also handles the exceptional small-field possibility of an elliptic curve with only one rational point by explicitly excluding it from the assertion.

**(6) Universal zeros and multiplicity lower bound.** For every odd prime power \(q\), the integer \(t=-1\) satisfies \(|t|<2\sqrt q\) and \(p\nmid t\). Waterhouse's ordinary case [2] guarantees an elliptic curve with this trace and \(q+2\ge5\) rational points; by (5) it yields a smooth bidegree-\((2,2)\) equation \(P\) and a Fourier zero. Its \(q-1\) distinct nonzero scalar multiples have the same zero locus, and each has exactly \(q\) frequency lifts by (3). They produce \(q(q-1)\) distinct zeros. Fourier diagonalization of additive convolution on \(S_G\) proves non-injectivity.

## Verification
The proof above is for every odd prime-power field, not inferred from computation. The standalone checker `check_elliptic_modes.py` evaluates explicit bidegree-\((2,2)\) equations over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\), verifies exactly \(q+2\) rational points, and checks that the associated binary-quartic discriminants are squarefree. They therefore supply smooth genus-one zero-mode examples with computed Fourier value \(q(|C(k)|-q-2)=0\). The code requires Python 3 and SymPy; it is a finite check and does not replace Waterhouse's existence theorem or the all-fields proof.

## Relationship to prior work
Iosevich–Koh [1] develop finite-field Fourier analysis and exact character methods for quadratic hypersurfaces, but not the Fourier spectrum of the orthogonal self-adjoint square-zero rank-one cone. The Waterhouse trace classification, available as Lemma 3.2 in Humphries [2], is an **explicitly used prior theorem** giving existence of curves with each trace; it is not a new trace classification. Schmidt [3] establishes translation association-scheme eigenvalues for rank strata of symmetric bilinear forms. This cone is instead cut out inside the rank-one symmetric locus by isotropy against the fixed split form; its smooth-section spectrum depends on genus-one point counts. The Gurevich–Kazhdan paper [4] concerns harmonic analysis of a cone over a nonarchimedean local field in a representation-theoretic setting; its abstract alone cannot resolve detailed priority for the present finite-field statement. Earlier results could imply portions through reductions not found in this bounded comparison.

## Limitations
The result classifies the distinct values on **smooth** bidegree-\((2,2)\) frequency sections, not their frequencies' exact multiplicities, not the singular-section eigenvalues, and not the complete global convolution rank. Independent mathematical validation has not been performed. This bounded literature comparison does not certify novelty against all possible specializations of older quadratic-form Fourier theory, orthogonal orbital harmonic analysis, or genus-one geometry.

## References
[1] A. Iosevich and D. Koh, “Extension Theorems for Spheres in the Finite Field Setting,” arXiv:0712.1627v1, first posted 2007-12-11, https://arxiv.org/abs/0712.1627.

[2] P. Humphries, “On the Mertens Conjecture for Elliptic Curves over Finite Fields,” arXiv:1209.6087v1, first posted 2012-09-26, Lemma 3.2 reproduces Waterhouse's trace existence classification, https://arxiv.org/abs/1209.6087. Original: W. C. Waterhouse, “Abelian varieties over finite fields,” Ann. Sci. Éc. Norm. Supér. (4) 2 (1969), 521–560.

[3] K.-U. Schmidt, “Quadratic and symmetric bilinear forms over finite fields and their association schemes,” arXiv:1803.04274v1, first posted 2018-03-12, https://arxiv.org/abs/1803.04274.

[4] N. Gurevich and D. Kazhdan, “Fourier transform on a cone and the minimal representation of even orthogonal group,” arXiv:2304.13993v1, first posted 2023-04-27, https://arxiv.org/abs/2304.13993.
