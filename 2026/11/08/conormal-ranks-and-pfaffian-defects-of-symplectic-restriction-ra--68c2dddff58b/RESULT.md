# Conormal ranks and Pfaffian defects of symplectic restriction-rank loci

## Finding
Let \((V,\omega)\) be a complex symplectic vector space of dimension \(2m\), let \(2\leq k\leq m\), and let \(0\leq s<\lfloor k/2\rfloor\). In the ordinary Grassmannian \(G=\operatorname{Gr}(k,V)\), consider the reduced rank locus
\[
X_{k,s}=\{L\in G: \operatorname{rank}(\omega|_L)\leq 2s\}.
\]
Set \(d=k-2s\ge2\). The variety \(X_{k,s}\) is irreducible of codimension \(\binom d2\), with smooth locus exactly the planes for which \(\omega|_L\) has rank \(2s\). At every such plane, let \(K=\ker(\omega|_L)\subset L\), of dimension \(d\). The ordinary Grassmannian conormal fiber identifies with \(\bigwedge^2K\), and, as a subspace of \(\operatorname{Hom}(V/L,L)\), every conormal covector has the same rank as its corresponding skew-symmetric \(d\times d\) matrix. Consequently its generic conormal rank in the sense of Pratt (2026) is
\[
\boxed{\operatorname{crk}_G(X_{k,s})=2\lfloor d/2\rfloor.}
\]
On the projectivized conormal bundle over the smooth locus, the rank-at-most-\(2j\) subvariety for \(1\le j<\lfloor d/2\rfloor\) is a relative irreducible Pfaffian variety, of codimension \(\binom{d-2j}{2}\), whose singular locus is the next lower rank stratum (empty for \(j=1\)). The first rank defect is absent for \(d=2,3\); for even \(d\ge4\) it is a hypersurface of degree \(d/2\) in each projective conormal fiber; and for odd \(d\ge5\) it has codimension three and fiber degree
\[
\boxed{\frac{d(d^2-1)}{24}.}
\]
This provides the same sharp parity change in all symplectic restriction-rank orbit closures, not merely the totally isotropic Grassmannians \(s=0\).

## Assumptions and scope
All geometry is over \(\mathbb C\); \(k\le m\) ensures that each indicated generic rank \(2s\) occurs. The conormal rank of an irreducible subvariety of a Grassmannian is the maximum matrix rank of conormal covectors above its smooth locus, equivalently the rank attained generically on the conormal variety. Conormal covectors are maps \(V/L\to L\) via the canonical identification \(T_L^*G=\operatorname{Hom}(V/L,L)\). Projectivization discards the zero covector. The degrees in the theorem are *fiber degrees*, with respect to \(\mathcal O_{\mathbb P(\bigwedge^2K)}(1)\), and not intersection numbers on the entire projective conormal bundle.

## Proof
**1. Strata, codimension, and a local normal slice.** The symplectic group acts transitively on \(k\)-planes with fixed rank of the restricted form: choose a symplectic basis for the nondegenerate part of the restriction, extend a basis of its radical to a symplectic basis of \(V\), and invoke the elementary symplectic basis-extension theorem. All ranks \(0,2,\ldots,2s\) occur since \(k\le m\). In local trivializations of the universal subbundle \(S\) on \(G\), the restricted form \(F=\omega|_S\) is a skew matrix. A plane \(L\) of rank \(2t\) has a decomposition \(L=U\oplus K_t\), where \(\omega|_U\) is nonsingular and \(K_t\) is its radical, of dimension \(k-2t\). Near \(L\), the restriction matrix has block form
\[
\begin{pmatrix}J+A&B\\-B^{\mathsf T}&C\end{pmatrix}
\]
with \(J\) nonsingular alternating of size \(2t\). By an invertible block congruence, the restriction rank condition becomes the condition that the alternating Schur complement \(C+B^{\mathsf T}(J+A)^{-1}B\) have rank at most \(2(s-t)\).

The map from a Grassmannian chart to the entries of that Schur complement is submersive at the chosen plane: restriction of \(\omega\) gives a surjective linear map \(q_{K_t}:V/L\twoheadrightarrow K_t^*\), because \(K_t\subset L^\perp\), and varying the graph of \(L\) makes the first-order \(K_t\times K_t\) skew block arbitrary. Thus a local product with the generic skew-matrix rank variety describes \(X_{k,s}\) near every rank-\(2t\) point. For \(t=s\), this is a smooth codimension-\(\binom{k-2s}{2}\) condition. Rank-\(2s\) planes occur and are one homogeneous irreducible orbit, and all lower ranks are its limits under these submersive local rank deformations. Therefore \(X_{k,s}\) is irreducible with the asserted codimension. When \(t<s\), the local Pfaffian variety is singular at its zero matrix: its first nontrivial equations have degree at least two because \(d\ge2\). Hence the singular locus is exactly the lower-rank locus \(X_{k,s-1}\) for \(s\ge1\); when \(s=0\), the variety is smooth.

**2. The conormal fiber is the skew space of the radical.** At a smooth rank-\(2s\) point \(L\), the nondegenerate \(U\)-block can be removed by the Schur complement. The normal derivative on \(\phi\in T_LG=\operatorname{Hom}(L,V/L)\), evaluated on \(u,v\in K\), is
\[
(dF)_L(\phi)(u,v)=q_K(\phi(u))(v)-q_K(\phi(v))(u),\qquad q_K:V/L\twoheadrightarrow K^*.
\]
Since \(q_K\) is onto, the normal space is \(\bigwedge^2K^*\) and the conormal is \(\bigwedge^2K\). Under trace duality the conormal element \(A\in\bigwedge^2K\) maps to
\[
V/L\xrightarrow{q_K}K^*\xrightarrow{A}K\hookrightarrow L.
\]
Both outside arrows are full-rank, so this composite has exactly the skew-matrix rank of \(A\). Every complex alternating \(d\times d\) matrix has even rank, and the maximum is \(2\lfloor d/2\rfloor\). The conormal rank follows.

**3. Relative rank strata and parity.** The radical \(K\) is a vector bundle on the smooth rank-\(2s\) orbit, and the projective conormal bundle is \(\mathbb P(\bigwedge^2K)\). Rank-at-most-\(2j\) is the relative Pfaffian locus cut out by the \((2j+2)\)-Pfaffians. On a fiber of dimension \(\binom d2-1\), choose the \((d-2j)\)-dimensional kernel and a nondegenerate form on the quotient; the resulting rank-\(2j\) locus is irreducible of codimension \(\binom{d-2j}{2}\). At an exact-rank point, the Schur complement gives smooth coordinates; when rank falls to \(2j-2\), all the first derivatives of the defining Pfaffians vanish. This proves the singular-locus statement.

If \(d=2r\ge4\), the first rank defect is the irreducible degree-\(r\) Pfaffian hypersurface. If \(d=2r+1\ge5\), it is the codimension-three scheme defined by the \(d\) submaximal Pfaffians of degree \(r\). For the generic alternating matrix, the classical Buchsbaum--Eisenbud codimension-three Pfaffian complex is exact. With \(R\) the polynomial ring on \(\binom d2\) entries and \(I\) the submaximal-Pfaffian ideal, its graded resolution is
\[
0\to R(-2r-1)\to R(-r-1)^d\to R(-r)^d\to R\to R/I\to0.
\]
The ideal has height three by the preceding dimension calculation. The Hilbert numerator \(P(t)=1-dt^r+dt^{r+1}-t^{2r+1}\) has a triple zero at \(t=1\), and differentiation gives its degree
\[
-P'''(1)/6=\frac{r(r+1)(2r+1)}6=\frac{d(d^2-1)}{24}.
\]
For \(d=2,3\), the only lower alternating rank is zero, so no projective rank-defect points exist. This proves every assertion.

## Verification
The included pure-Python `verify.py` checks exact alternating-matrix ranks and the injective conormal-composition rank identity in sample dimensions, Pfaffian-determinant identities, and the odd-degree Hilbert numerator. These checks test finite examples of algebraic steps; the general result follows from the local symplectic normal-slice argument and the standard codimension-three Pfaffian free resolution. Reproduce using `python3 verify.py` from the extracted package.

## Relationship to prior work
Pratt (2026) defined and investigated conormal rank for Grassmannian subvarieties, including Schubert, positroid, and torus-orbit-closure cases. The assertion being assessed here is a complete conormal-rank and first-Pfaffian-defect classification for all symplectic restriction-rank orbit closures \(X_{k,s}\). Xu--Zhang (2022/2024) studied equations of type-C Grassmannian and Schubert varieties in type-A embeddings, not these ordinary-Grassmannian conormal rank profiles. Kohn--Mathews (2019/2020) analyzed rank-one coisotropy and a different tangent-space isotropy condition. Classical symplectic orbit linear algebra and generic Pfaffian determinantal resolutions are explicitly used as prior inputs, not claimed as new. Search and accessible primary-source comparisons did not uncover the full conormal classification, but publication priority is not independently certified.

## Limitations
The claims concern complex \(k\)-planes with \(k\le m\), the reduced rank loci, their smooth conormal bundles, and fiberwise degrees; they do not cover the scheme-theoretic conormal closure over lower-rank singular strata or all positive-characteristic cases. The recent motivating paper's abstract, introduction, definitions and selected theorem/proof sections were read, but complete line-by-line reinspection was not available in the comparison session. A general Pfaffian free-resolution theorem is used; finite checks are not its proof. Independent mathematical audit has not been performed.

## References
- Elizabeth Pratt, *Conormal Rank of Subvarieties of Grassmannians*, arXiv:2609.24694v1, first public 2026-09-21, https://arxiv.org/abs/2609.24694 .
- Jiajun Xu and Guanglian Zhang, *Symplectic conditions on Grassmannian, flag, and Schubert varieties*, arXiv:2204.05589, https://arxiv.org/abs/2204.05589 .
- Kathlén Kohn and James Mathews, *Isotropic and Coisotropic Subvarieties of Grassmannians*, arXiv:1901.06584, https://arxiv.org/abs/1901.06584 .
- David A. Buchsbaum and David Eisenbud, *Algebra structures for finite free resolutions, and some structure theorems for ideals of codimension 3*, American Journal of Mathematics **99** (1977), 447–485, DOI: 10.2307/2373926 .
