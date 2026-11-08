# Witt-type completeness of ordinary zero-divisor graphs of short finite Gorenstein local rings

## Finding
Let \(R\) be a finite commutative local Gorenstein ring with maximal ideal \(\mathfrak m\), residue field \(k=\mathbb F_q\), and \(\mathfrak m^3=0\ne\mathfrak m^2\). Put \(d=\dim_k(\mathfrak m/\mathfrak m^2)\ge3\). Define the *ordinary zero-divisor graph* \(\Gamma(R)\) on nonzero elements of \(\mathfrak m\), with an edge between distinct vertices precisely when their product is zero.

Multiplication induces a nondegenerate symmetric bilinear form \(B\) on \(V=\mathfrak m/\mathfrak m^2\), well-defined up to nonzero scalar. The graph isomorphism type is determined **exactly** by the field order \(q\), dimension \(d\), and the similarity class of \(B\). Moreover, the graph itself recovers those three invariants. Thus, for fixed \(q,d\):

- if \(d\) is odd, there is exactly one possible graph type in every characteristic;
- if \(d\) is even and \(q\) is odd, there are exactly two types (split and nonsplit symmetric forms);
- if \(d\) is even and \(q\) is even, there are exactly two types (alternating and nonalternating forms).

All listed types occur for finite Gorenstein local rings. This gives an if-and-only-if graph-isomorphism classification for arbitrary residue fields, including mixed-characteristic rings and the characteristic-two alternating boundary.

Set \(N=q^d-1\) and let \(\nu\) be the number of nonzero isotropic vectors \(v\in V\), meaning \(B(v,v)=0\). The possibilities are:
\[
\nu=\begin{cases}
q^{d-1}-1,&d\text{ odd (any }q\text{)},\\
q^{d-1}-1+\varepsilon(q-1)q^{(d-2)/2},&d\text{ even},\ q\text{ odd},\ \varepsilon\in\{+1,-1\},\\
q^d-1,&d\text{ even},\ q\text{ even},\ B\text{ alternating},\\
q^{d-1}-1,&d\text{ even},\ q\text{ even},\ B\text{ nonalternating}.
\end{cases}
\]
Here \(\varepsilon=+1\) for a split quadratic space and \(\varepsilon=-1\) for the nonsplit one. The graph has \(q^{d+1}-1\) vertices; the \(q-1\) nonzero socle elements are its unique universal vertices. For the remaining \(qN\) vertices there are exactly \(q\nu\) of degree \(q(q^{d-1}-1)+q-2\) and \(q(N-\nu)\) of degree \(q(q^{d-1}-1)+q-1\). Consequently
\[
|E(\Gamma(R))|=\binom{q-1}{2}+q(q-1)(q^d-1)+\frac{q^2(q^d-1)(q^{d-1}-1)-q\nu}{2}.
\]

## Assumptions and scope
The ring is unital, finite, commutative, local and Gorenstein, with nonzero square and zero cube of its maximal ideal; \(d\ge3\). No coefficient-field embedding in \(R\) is assumed. The isomorphism statement concerns *unlabeled, simple* ordinary zero-divisor graphs. A bilinear form is considered up to multiplication by a nonzero field scalar and a change of basis. All finite field orders \(q\) are prime powers.

## Proof
**(1) Multiplication form.** The nonzero ideal \(\mathfrak m^2\) is contained in \(\operatorname{Soc}R=\operatorname{ann}_R(\mathfrak m)\). Since the Gorenstein socle has dimension one over \(k\), \(\mathfrak m^2=\operatorname{Soc}R\) is a one-dimensional \(k\)-space. Fix a nonzero \(z\) therein. For \(x,y\in\mathfrak m\), their product has the form \(B(\bar x,\bar y)z\), where \(\bar x\) is the image in \(\mathfrak m/\mathfrak m^2\). This is well-defined since \(\mathfrak m^3=0\), symmetric since \(R\) is commutative, and \(k\)-bilinear since scalar lifts act on \(\mathfrak m^2\) by their residues. If \(\bar x\) is orthogonal to all of \(V\), then \(x\mathfrak m=0\), so \(x\in\operatorname{Soc}R=\mathfrak m^2\) and \(\bar x=0\). Thus \(B\) is nondegenerate. Another choice of \(z\) rescales it.

**(2) Graph construction.** Every zero divisor is in \(\mathfrak m\). The socle contains \(q-1\) nonzero elements, each adjacent to every distinct vertex. For each nonzero vector \(v\in V\), exactly \(q\) vertices of \(\mathfrak m\) project to \(v\). Distinct vertices over \(v,w\ne0\) are adjacent precisely when \(B(v,w)=0\); this also describes adjacency inside a fiber (complete if \(B(v,v)=0\), empty otherwise). Therefore a semilinear or linear similarity between forms gives a graph isomorphism.

**(3) Degree recovery.** An outside vertex over \(v\ne0\) has \(q(q^{d-1}-1)\) candidate outside neighbors (the nonzero vectors in \(v^\perp\), each with \(q\) lifts), with one deleted if it itself belongs to its candidate set. Adding \(q-1\) socle neighbors gives degrees \(q(q^{d-1}-1)+q-2\) for isotropic \(v\), and one greater for nonisotropic \(v\). The socle vertices alone have degree \(q^{d+1}-2\), strictly higher for \(d\ge3\). Hence the graph recovers \(q\) from its number of universal vertices, \(d\) from its total number of vertices, and \(\nu\) from the degree multiplicity. Summing degrees proves the edge formula.

**(4) Finite-field classification and separation.** Standard Gram reduction for nonsingular symmetric bilinear forms over finite fields yields one similarity class in odd dimension. In even dimension and odd characteristic there are exactly two, distinguished by the quadratic-space sign \(\varepsilon\), with \(q^{d-1}+\varepsilon(q-1)q^{(d-2)/2}\) zero vectors. In characteristic two, in odd dimension every nonsingular symmetric form is nonalternating and isometric to the standard dot product, while even dimension has precisely alternating and nonalternating types. In the latter case the map \(v\mapsto B(v,v)\) is either identically zero (alternating) or the square of a nonzero linear functional (nonalternating), yielding respectively \(q^d\) or \(q^{d-1}\) zero vectors. Thus \(\nu\) distinguishes the two even-dimensional types, and all odd-dimensional forms are similar. By step (2), equal types give isomorphic graphs; by step (3), different types do not.

**(5) Existence.** For each required nondegenerate symmetric \(B\) on \(k^d\), define the unital commutative algebra \(R_B=k\oplus k^d\oplus kz\), where multiplication of radical elements obeys \((v,az)(w,bz)=B(v,w)z\), the radical-square line kills the radical, and scalars act naturally. Associativity follows because every triple of radical elements multiplies to zero. Its maximal ideal has cube zero, nonzero square, and one-dimensional socle by nondegeneracy of \(B\). Thus it is Gorenstein and realizes the corresponding graph. This completes the if-and-only-if classification.

## Verification
The included standalone program `check.py` builds the nonzero radical elements of explicit short local Gorenstein algebras, tests zero products directly from their multiplication form, independently enumerates graph edges and degrees, and compares them with the formulas. Ten configurations include \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\); odd and even dimensions; alternating and nonalternating characteristic-two spaces; and both odd-characteristic Witt signs. For example, with \(q=3,d=4\), the two types have respectively \(9{,}793\) and \(9{,}811\) edges on \(242\) vertices, and at \(q=2,d=4\) the nonalternating and alternating types have respectively \(233\) and \(225\) edges on \(31\) vertices. The checker output is `verification_output.txt`. Finite enumeration is a check, not a proof of the classification for arbitrary dimension.

## Relationship to prior work
Kadu (2020/2021), Proposition 3.6, **already established** the multiplication/orthogonality correspondence for cube-zero local rings and related the nondegeneracy of the induced form to the Gorenstein property. These foundational facts are not claimed as new. Kadu and Tanpure (2026) compared ordinary, associate-class and annihilator-compressed graphs, characterizing Gorenstein rings via the latter two. Previous short-ring work explicitly classified the two-dimensional case; the present theorem supplies the whole \(d\ge3\) graph-isomorphism classification over every finite field, including the parity-dependent two-type dichotomy and graph-theoretic recovery of the form type. The standard classification of finite-field symmetric forms is also not new. The proposed contribution is their combination into a complete *ordinary graph* classification and explicit degree/edge reconstruction beyond embedding dimension two.

## Limitations
No assertion is made for \(\mathfrak m^4\ne0\), non-Gorenstein rings, or arbitrary finite nonlocal rings. The result classifies graphs, not rings: nonisomorphic rings may have isomorphic graphs. In characteristic two, the induced form need not be the polarization of a quadratic form. The known 2020/2021 orthogonality criterion is a strong prior ingredient, so historical novelty of the assembled complete classification remains a genuine risk pending independent literature assessment. The work has no independent mathematical audit.

## References
1. G. S. Kadu, *On the problem of the finiteness of the compressed zero divisor graphs of Artinian rings*, arXiv:2010.06924 (first public 2020-10-14), Proposition 3.6, Sections 2–3. https://arxiv.org/abs/2010.06924
2. G. S. Kadu and V. Tanpure, *Zero divisors of Gorenstein Rings*, arXiv:2609.36021 (first public 2026-09-28). https://arxiv.org/abs/2609.36021
3. Standard finite-field classification of nonsingular symmetric bilinear forms (Gram/Witt reduction), as stated explicitly and applied in the proof.
