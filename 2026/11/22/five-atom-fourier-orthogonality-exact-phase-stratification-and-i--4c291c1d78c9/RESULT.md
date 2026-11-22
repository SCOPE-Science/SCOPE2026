# Five-atom Fourier orthogonality: exact phase stratification and irrational triples

## Finding

For the positive probability measure
\[
\mu=a(\delta_{-2}+\delta_{2})+b(\delta_{-1}+\delta_{1})+c\delta_0,
\qquad a,b,c>0,\quad 2a+2b+c=1,
\]
let \(\mathcal O(\mu)\) be the largest cardinality of a family of mutually orthogonal functions \(x\mapsto e^{2\pi i\lambda x}\) in \(L^2(\mu)\), with arbitrary real frequencies \(\lambda\). Put
\[
P(u)=4au^2+2bu+c-2a,\quad
x_*\in(-1,-1/2),\quad 4x_*^3-2x_*+1=0.
\]
The number \(x_*\) is the unique real root of the displayed cubic. Define the *resonance locus* \(\mathcal R\) by either
\[
c=a+b,
\]
or, for some \(x\in(x_*,1/2)\), by the simultaneous equations
\[
a=\frac1{8(1-x)^2(1+x)},\qquad
b=\frac{1-2x}{4(1-x)^2},\qquad
c=\frac{1+4x^3-2x}{4(1-x)^2(1+x)}.
\]
The following ordered case distinction is exact (the first applicable case is selected):
\[
\boxed{\mathcal O(\mu)=
\begin{cases}
5,&a=b=c=1/5,\\
4,&(a,b,c)=(1/8,1/4,1/4),\\
3,&(a,b,c)\in\mathcal R,\\
2,&\min_{-1\le u\le1}P(u)\le0,\\
1,&\text{otherwise}.
\end{cases}}
\]
The condition on the fourth line can be evaluated without optimization:
\[
\min_{[-1,1]}P\le0\iff
\begin{cases}
b^2\ge4a(c-2a),&b<4a,\\
b\ge1/4,&b\ge4a.
\end{cases}
\]
Every three-element orthogonal family, after translation of frequencies and reduction modulo integers, is an arithmetic progression \(\{0,t,2t\}\) where
\(P(\cos(2\pi t))=P(\cos(4\pi t))=0\).
The five-character case has the standard fifth-root spectrum. When the *maximum* is exactly four, every four-character family is a coset of the order-four subgroup of \(\mathbb R/\mathbb Z\); at uniform weights, four-character subfamilies of the fifth-root basis also exist.

In particular the rational weights \((a,b,c)=(8/45,10/45,9/45)\) give \(\mathcal O(\mu)=3\) with the explicit orthogonal family
\[
\{0,t,2t\},\qquad t=\frac{\arccos(1/4)}{2\pi}\notin\mathbb Q.
\]
Thus an incomplete maximal orthogonal exponential family for a rational finite atomic measure can contain irrational frequency differences.

## Assumptions and scope

The five support sites are the consecutive integers \(-2,-1,0,1,2\). Weights are strictly positive and symmetric, with outer, inner and central weights \(a,b,c\), respectively; no uniform-weight, integer-frequency or torsion restriction is imposed. Frequencies differing by an integer define the same function on the support and are identified in \(\mathbb T=\mathbb R/\mathbb Z\). A family of size \(m\) means \(m\) pairwise distinct characters in \(L^2(\mu)\). All claims concern these finite measures, not arbitrary support locations or infinite self-similar measures.

## Proof

**1. Fourier zeros.** By symmetry and the double-angle identity,
\[
\widehat\mu(t)=c+2b\cos(2\pi t)+2a\cos(4\pi t)
=P(\cos(2\pi t)).
\]
The polynomial \(P\) is strictly convex, has degree two, and satisfies \(P(1)=1\). Hence its zero set \(S\subset\mathbb T\), excluding zero, contains at most four points. Orthogonality is equivalent to \((\Lambda-\Lambda)\setminus\{0\}\subset S\). Translating \(\Lambda\), assume \(0\in\Lambda\). The other members must lie in \(S\), so \(|\Lambda|\le5\).

**2. Five and four characters.** Five orthonormal exponential characters form a unitary basis of the five-dimensional weighted coordinate space. Each coordinate row of the associated unitary matrix has squared norm \(5w_j\), where \(w_j\) is its atomic weight, hence \(w_j=1/5\). Conversely, the fifth-root Fourier characters are orthonormal for equal weights.

Here is the elementary difference-set fact needed for four characters: if a four-point subset of \(\mathbb T\) has at most four distinct nonzero differences, it is either a coset of the subgroup of order four or a four-element subset of a coset of the subgroup of order five. To prove this, translate the subset to contain zero. Its three nonzero members belong to a symmetric set \(S\) of at most four elements. If the unique involution \(1/2\) is in \(S\), then \(S=\{1/2,u,-u\}\), and the condition that \(1/2-u\in S\) forces \(2u=1/2\); this is the order-four configuration. Otherwise \(S=\{u,-u,v,-v\}\), and three members among these four include an opposite pair. Write the four-point set as \(\{0,u,-u,v\}\). The relation \(2u\in S\) and the further conditions \(v\pm u\in S\) exclude order three for \(u\) and force \(v=\pm2u\); changing its sign if necessary, take \(v=2u\). Now \(3u\in\{\pm u,\pm2u\}\), and the only possibility without an involution is \(5u=0\), giving an order-five subgroup.

If the four-point family lies in an order-five coset, all four nonzero fifth-root frequency differences occur, so the discrete Fourier transform of the five atomic weights vanishes at frequencies \(1/5,2/5,3/5,4/5\). Fourier inversion forces equal weights, already covered by the first case. If it lies in an order-four coset, \(P(0)=P(-1)=0\), so \(b=c=2a\); normalization gives \((a,b,c)=(1/8,1/4,1/4)\). Conversely at these weights \(P(u)=\tfrac12 u(u+1)\), making \(\{0,1/4,1/2,3/4\}\) orthogonal. Four characters are therefore possible only at the stated weights, apart from the five-character case.

**3. Three characters.** If \(\{0,u,v\}\) has pairwise differences in a symmetric set \(S\) of at most four points, then for some nonzero \(t\in S\) also \(2t\in S\). Indeed, in the absence of the involution, the two representatives \(u,v\in S=\{\pm s,\pm r\}\) are either opposite (so their difference is a double) or come from different pairs, in which case \(v-u\in S\) implies one is twice the other. If an involution is present, the only new configuration has \(u=1/2\), \(v\in\{s,-s\}\), and its remaining difference condition forces \(2s=1/2\). In every case the three points are a translate of \(\{0,t,2t\}\). Thus three characters exist exactly when
\[
P(x)=P(2x^2-1)=0\quad\text{for some }x\in[-1,1].
\]
The fixed points of the double-angle map are \(x=1\) and \(x=-1/2\). The first is impossible since \(P(1)=1\); at the second the equation becomes \(c=a+b\), producing a triple of third-root frequencies. In the remaining case the two distinct roots of \(P\) are \(x\) and \(2x^2-1\). Their sum and product give
\[
b=2a(1-x-2x^2),\qquad c=2a(1+4x^3-2x).
\]
Using \(2a+2b+c=1\), these equations reduce to the parametric formulas in the finding. Strict positivity holds precisely when \(x\in(x_*,1/2)\): the expression for \(b\) is positive precisely for \(-1<x<1/2\), and the numerator \(1+4x^3-2x\) of \(c\) has the single real zero \(x_*\) in \((-1,-1/2)\). Conversely, each point on either displayed resonance family gives the triple \(\{0,t,2t\}\), with \(x=\cos(2\pi t)\). This proves the complete three-character locus, subject to the already selected four- and five-character cases.

**4. Two and one characters.** Two characters exist iff \(P\) has a root in \([-1,1]\), equivalently \(\min_{[-1,1]}P\le0\), since \(P(1)=1>0\). The vertex of \(P\) is at \(-b/(4a)\). For \(b<4a\) it lies in the interval and gives \(c-2a-b^2/(4a)\); otherwise the minimum is \(P(-1)=1-4b\). This yields the exact criterion and proves the final two cases.

**5. Irrational triple.** At \((a,b,c)=(8/45,10/45,9/45)\),
\[
45P(u)=32u^2+20u-7=(4u-1)(8u+7).
\]
The double-angle map sends \(1/4\) to \(-7/8\), so the indicated triple is orthogonal. These weights are neither uniform nor the four-character weights, hence \(\mathcal O=3\). If \(t\) were rational, \(e^{2\pi it}\) would be a root of unity, and \(2\cos(2\pi t)=1/2\) would be a rational algebraic integer, hence an integer, a contradiction.

## Verification

A standalone Python checker `checker.py`, relying only on the standard library, verifies exact rational instances of the doubled-root parametrization, the special four- and three-character examples, and the difference-set combinatorial lemma exhaustively for torsion groups of orders \(2\) through \(64\). All exact tests passed. Those finite checks are supplementary; the above argument proves the theorem for all real parameters and all real frequencies.

## Relationship to prior work

Fu and Song (2026) establish rationality of the spectra of *complete* finite Hadamard pairs for integer site sets; Bell (2026, Theorem 6.1 and Appendix A) records and proves the same complete-pair rationality assertion. That result is consistent with the fifth-root case but does not imply rationality for a three-element incomplete orthogonal family in five-dimensional \(L^2(\mu)\). Bell's results for spectral unions of four intervals and finite fiber tilings also require complete spectrality, not the weighted, incomplete optimization solved here. Li and Wang (2026) study maximal orthogonal family sizes for infinite three-dimensional self-affine measures, under different hypotheses. The explicit nonuniform irrational triple and complete five-atom phase stratification are not consequences of these stated theorems.

## Limitations

The support symmetry and strict positivity are essential to the exact quadratic reduction. No classification of non-symmetric five-atom measures, arbitrary real support locations, or higher-dimensional atomic measures is asserted. Independent mathematical validation has not been performed. A literature search cannot establish absolute novelty; in particular, a potentially equivalent older weighted trigonometric quadrature classification could remain unidentified. The Fu–Song original manuscript was not fully accessible for direct inspection, although the specific complete-pair theorem was checked in Bell's full-text reproduction and proof.

## References

1. X.-Y. Fu and Z.-J. Song, *Rational Spectra for Finite Hadamard Pairs and Bounded Spectral Sets on the real line*, arXiv:2607.19858, first publicly posted 2026-07-22. https://arxiv.org/abs/2607.19858
2. A. O. Bell, *Spectral unions of four intervals tile the real line*, arXiv:2610.37975, first posted 2026-10-27, especially Theorems 1.2, 5.8, 6.1 and Appendix A. https://arxiv.org/abs/2610.37975
3. Y.-Q. Li and Z.-M. Wang, *The Number of Orthogonal Exponential Functions of a Class of Self-Affine Measures in* \(\mathbb R^3\), *Axioms* 15 (2026), 563, first published 2026-07-29. https://doi.org/10.3390/axioms15080563
