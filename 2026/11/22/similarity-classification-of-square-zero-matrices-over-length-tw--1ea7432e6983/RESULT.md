# Similarity classification of square-zero matrices over length-two chain rings

## Finding
Let \(R\) be a finite commutative chain ring with a strict ideal chain \(R\supsetneq\pi R\supsetneq0\), \(\pi^2=0\), and \(k=R/\pi R=\mathbb F_q\). For each \(n\ge1\) consider \(\mathcal Z_n(R)=\{X\in M_n(R):X^2=0\}\), with the action of \(\operatorname{GL}_n(R)\) by conjugation.

**Classification.** Every conjugacy orbit contains exactly one normal-form *type* \((r,[B])\), where \(0\le r\le\lfloor n/2\rfloor\), \(s=n-2r\), and \([B]\) is a similarity class of \(s\times s\) matrices over \(k\). In particular a representative, using ordered block sizes \((r,s,r)\), is
\[
X_{r,B}=\begin{pmatrix}0&0&I_r\\0&\pi\widetilde B&0\\0&0&0\end{pmatrix},
\]
where \(\pi\widetilde B\) is independent of the choice of entrywise lifts of \(B\) to \(R\). This matrix satisfies \(X_{r,B}^2=0\) in every residue characteristic. Distinct \(r\) or nonsimilar \(B\) give distinct conjugacy orbits.

**Intrinsic invariant.** Set \(A=\overline X=X\bmod\pi\), \(r=\operatorname{rank}_k A\), and \(H(A)=\ker A/\operatorname{im} A\), which has dimension \(s\). For \(v\in\ker A\), choose a lift \(\widetilde v\in R^n\). Write \(X\widetilde v=\pi\widetilde z\) with \(z\in k^n\); define \(\beta_X([v])=[z]\in H(A)\). This is well-defined, and the similarity class of \(\beta_X\) is the second complete invariant. Changing the chosen generator of the maximal ideal rescales \(\beta_X\) by a nonzero scalar, while leaving the corresponding classification statement relative to that generator unchanged.

**Class count.** If \(c_s(q)\) is the number of ordinary matrix similarity classes over \(\mathbb F_q\), with \(c_0(q)=1\), the number of square-zero similarity classes is
\[
K_n(q)=\sum_{r=0}^{\lfloor n/2\rfloor}c_{n-2r}(q),
\qquad
\sum_{n\ge0}K_n(q)z^n=\frac{1}{1-z^2}\prod_{j\ge1}\frac{1}{1-qz^j}.
\]
Here \(K_0(q)=1\) is a conventional empty-dimensional initial value. Thus \(K_1(q)=q\), \(K_2(q)=q^2+q+1\), and \(K_3(q)=q^3+q^2+2q\), uniformly for equal- and mixed-characteristic length-two chain rings.

## Assumptions and scope
The ring \(R\) is finite, unital, commutative, local, and principal with precisely the displayed three ideals. Accordingly \(\operatorname{ann}_R(\pi)=\pi R\), and \(\pi R\) is canonically one-dimensional over \(k\) after choosing \(\pi\). It need not have a coefficient field (for example \(\mathbb Z/4\mathbb Z\) qualifies). Matrix similarity is *conjugacy* by \(\operatorname{GL}_n(R)\), not Smith equivalence by independent left and right row operations. The classification is of all matrices satisfying exactly \(X^2=0\), including the zero matrix, at every positive size. No classification of higher nilpotency orders, longer chain rings, or non-chain rings is implied.

## Proof
**1. Reduction and the secondary map.** Since \(X^2=0\), \(A^2=0\) and \(r\le n/2\). The induced map \(\beta_X\) is well-defined as follows: changing \(\widetilde v\) by \(\pi\widetilde w\) changes \(z\) by \(Aw\); changing \(v\) by a vector in \(\operatorname{im}A\) permits changing \(\widetilde v\) by \(X\widetilde u\), which does not change \(X\widetilde v\). Moreover \(X^2=0\) implies \(Az=0\). Therefore the target is \(H(A)\), and the construction is independent of choices. Conjugation sends \(H(A)\) isomorphically onto the homology of the conjugate reduction and intertwines the corresponding secondary maps.

**2. Fixed-reduction normal form.** Conjugate \(A\) over \(k\) into \(N\), which on \(k^n=U\oplus H\oplus W\), with dimensions \((r,s,r)\), maps \(W\) identically to \(U\) and kills \(U\oplus H\). The basis change lifts to \(\operatorname{GL}_n(R)\). Take the same zero-one matrix \(N\) over \(R\), so that \(N^2=0\). Every matrix reducing to \(N\) has a unique expression \(X=N+\pi Y\), where the class of \(Y\) in \(M_n(k)\) is uniquely determined. Because \(\pi^2=0\), the equation \(X^2=0\) is equivalent to \(NY+YN=0\) over \(k\), that is,
\[
Y_{WU}=Y_{WH}=Y_{HU}=0,\qquad Y_{WW}=-Y_{UU}.
\]
The free blocks are \(Y_{UU},Y_{UH},Y_{UW},Y_{HW},Y_{HH}\). With \(C\in M_n(k)\), conjugation by \(I+\pi C\) replaces \(Y\) by \(Y+[C,N]\). Its relevant block changes are
\[
[C,N]_{UU}=-C_{WU},\quad [C,N]_{UH}=-C_{WH},\quad
[C,N]_{UW}=C_{UU}-C_{WW},\quad [C,N]_{HW}=C_{HU},\quad
[C,N]_{WW}=C_{WU},\quad [C,N]_{HH}=0.
\]
Choose \(C_{WU}=Y_{UU}\), \(C_{WH}=Y_{UH}\), \(C_{HU}=-Y_{HW}\), and \(C_{UU}-C_{WW}=-Y_{UW}\). These simultaneously kill all free blocks except \(Y_{HH}=B\). The prescribed relation \(Y_{WW}=-Y_{UU}\) kills that block as well. Hence every square-zero matrix is conjugate to \(X_{r,B}\), and \(\beta_{X_{r,B}}\) identifies with \(B\) on \(H\).

**3. Uniqueness of the matrix similarity parameter.** An arbitrary residue centralizer of \(N\) inside \(\operatorname{GL}_n(k)\), in the displayed ordered decomposition, is of block form
\[
\begin{pmatrix}P&Q&S\\0&T&V\\0&0&P\end{pmatrix}
\quad(P\in\operatorname{GL}_r(k),\ T\in\operatorname{GL}_s(k)).
\]
It acts on reduced homology as \(T\). Thus a conjugacy between \(X_{r,B}\) and \(X_{r,B'}\) necessarily induces \(B'=TBT^{-1}\). Conversely, if \(B'=TBT^{-1}\), a block-diagonal lift of \(\operatorname{diag}(I_r,T,I_r)\), using the *same* chosen matrix lift for the middle factor and its inverse, conjugates \(X_{r,B}\) to \(X_{r,B'}\). The same conclusion holds for \(r=0\) or \(s=0\). Hence precisely the pairs \((r,[B])\) index the orbits.

**4. Generating function.** Rational canonical form parametrizes similarity classes of \(m\times m\) matrices over \(k\) by a partition for each monic irreducible polynomial, of total weighted degree \(m\). Therefore
\[
\sum_{m\ge0}c_m(q)z^m
=\prod_{j\ge1}\prod_{\varphi\text{ monic irreducible}}(1-z^{j\deg\varphi})^{-1}
=\prod_{j\ge1}(1-qz^j)^{-1},
\]
using unique factorization of monic polynomials over \(\mathbb F_q\). Summing over \(n=s+2r\), with \(r\ge0\), introduces \((1-z^2)^{-1}\) and yields the asserted all-dimensional count. This completes the proof.

## Verification
The standalone program `verify.py` exhaustively enumerates square-zero matrices and their *actual conjugacy orbits* under elementary invertible matrices for the following finite cases: \(\mathbb Z/4\mathbb Z\) and \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\) through dimension three; \(\mathbb Z/9\mathbb Z\) and \(\mathbb F_3[\varepsilon]/(\varepsilon^2)\) through dimension two. It separately counts each orbit by residue rank, then compares with the rational-canonical class numbers \(c_{n-2r}(q)\), without using the canonical-form proof to partition the candidates. See `verification_output.txt` and run `python3 verify.py` from the extracted package. Finite checks are corroboration, not a proof for all rings or dimensions.

## Relationship to prior work
Prasad, Singla and Spallone [1] reduce arbitrary similarity over local principal rings of length two to actions on extension spaces and give explicit orbit classifications for matrices of size at most four. Their general reduction is credited as the prior conceptual framework; it does **not** itself calculate the square-zero-constrained orbit set for all dimensions. Trishin [6] gives an earlier general reduction for dual-number matrices over an algebraically closed field of characteristic zero, with explicit small-order classifications; neither finite-field class counts nor mixed-characteristic analogues are asserted. Călugăreanu [2] analyzes zero-square similarity over Bézout domains and demonstrates obstacles beyond the rank-one normal form; the finite rings here have nilpotent zero divisors, so its domain hypotheses do not imply this classification. Danchev, García and Gómez Lozano [3] study existence of potent-plus-square-zero decompositions over square-zero-radical rings, rather than orbits of the square-zero summands. Prior finite-chain-ring results [4,5] enumerate labeled square-zero matrices by rank, Smith form, and secondary-map distribution; indeed [5] establishes that every secondary endomorphism occurs, which is expressly credited. The new statement is that the *full conjugacy quotient* has no further data beyond the similarity class of that endomorphism, together with the explicit class-count series. The general extension-orbit theory could furnish an alternative derivation, and historical equivalence under less explicit terminology is a residual priority risk.

## Limitations
The result makes no assertion about individual orbit cardinalities, centralizer orders, or similarity over longer chain rings. The secondary map depends on a chosen uniformizer by an invertible scalar; the orbit parameterization is stated relative to that choice, though the total class count is intrinsic. The generating function counts orbits, not labeled matrices. The formal small-size calculations do not replace the infinite block normal-form proof. An earlier published special classification could exist outside the inspected sources. Independent mathematical validation has not been performed.

## References
[1] A. Prasad, P. Singla and S. Spallone, *Similarity of matrices over local rings of length two*, arXiv:1212.6157, https://arxiv.org/pdf/1212.6157 (full text, introduction and reductions).

[2] G. Călugăreanu, *Similarity for zero-square matrices*, arXiv:2108.12882v1 (first posted 2021-08-29), https://arxiv.org/pdf/2108.12882 (full text).

[3] P. Danchev, E. García and M. Gómez Lozano, *Decompositions of Matrices into Potent and Square-Zero Matrices*, arXiv:2102.10460v1 (first posted 2021-02-20), https://arxiv.org/pdf/2102.10460 (full text).

[4] *Square-zero Smith strata are universal across length-two chain rings*, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-square-zero-smith-strata-are-universal-across-length-two-chain-r--6b8f1c0037a2 (read full RESULT.md).

[5] *Bockstein equidistribution and image-shape counts for square-zero endomorphisms over length-two chain rings*, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-bockstein-equidistribution-and-image-shape-counts-for-square-zer--150f31c550b3 (read full RESULT.md).

[6] I. M. Trishin, *On similar matrices over the dual numbers*, arXiv:0910.0536v1, https://arxiv.org/pdf/0910.0536 (abstract and introduction inspected; over algebraically closed characteristic-zero coefficient fields).
