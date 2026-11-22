# Four centralizer strata and a saturation law over square-zero local rings

## Finding

Let \(R\) be a finite commutative local unital ring, with nonzero maximal ideal \(\mathfrak m\) satisfying \(\mathfrak m^2=0\), residue field \(k=R/\mathfrak m=\mathbb F_q\), and embedding dimension \(d=\dim_k\mathfrak m\ge2\). For \(A\in M_2(R)\), set \(C(A)=\{B\in M_2(R):AB=BA\}\). The complete element-centralizer cardinality spectrum is

\[
\begin{array}{c|c}
|C(A)| & \#\{A:|C(A)|\text{ has this value}\}\\ \hline
q^{2d+2} & (q^4-q)q^{4d}\\
q^{4d+1} & q\bigl(q^{4d}-q^d-(q^2+q+1)(q^{2d}-q^d)\bigr)\\
q^{4d+2} & q(q^2+q+1)(q^{2d}-q^d)\\
q^{4d+4} & q^{d+1}.
\end{array}
\]

All four sizes are distinct and occur for each \(d\ge2\). The formula holds without assuming that \(R\) contains a coefficient field: mixed characteristic is permitted. In particular, the number of ordered commuting pairs in the full matrix ring is

\[
\boxed{\#\{(A,B)\in M_2(R)^2:AB=BA\}
=q^2q^{8d}+(q^6+q^5-q^3-q^2)q^{6d}.}
\]

Since \(|M_2(R)|=q^{4d+4}\), its commuting probability is
\[
\boxed{\operatorname{cp}(M_2(R))
=q^{-6}+(q^6+q^5-q^3-q^2)q^{-2d-8}.}
\]
For any fixed \(q\), as \(d\to\infty\) the probability tends to the strictly positive constant \(q^{-6}\), and, **conditioned on commutation, both residue matrices are scalar with probability tending to one at rate \(O_q(q^{-2d})\)**. This persists even though the unconditional fraction of matrices with nonscalar reductions is the fixed positive quantity \(1-q^{-3}\), independent of \(d\). It contrasts with growing-length principal chain rings and marks the first nonprincipal radical-dimension regime as a distinct centralizer stratum.

## Assumptions and scope

The ring is commutative, finite, local and unital, with \(\mathfrak m\ne0\), \(\mathfrak m^2=0\). The action of \(R\) on \(\mathfrak m\) factors canonically through the residue field \(k\), making \(\mathfrak m\) a \(k\)-vector space. Hence \(|R|=q^{d+1}\), without a splitting assumption. The theorem concerns all matrices, including scalar ones, and counts centralizers inside the *ring* \(M_2(R)\), not inside its group of units. Its primary new case is \(d\ge2\); the principal case \(d=1\) is already covered by known chain-ring work and is used only as a verification boundary.

## Proof

**1. Matrices with nonscalar reduction.** Fix \(A\in M_2(R)\) and denote its reduction by \(\bar A\in M_2(k)\). Every \(2\times2\) matrix \(A\) has a unique decomposition \(aI+\begin{psmallmatrix}u&v\\w&0\end{psmallmatrix}\), where \(a,u,v,w\in R\). Direct expansion shows that two matrices commute if and only if the three \(2\times2\) minors of their respective triples \((u,v,w)\) and \((u',v',w')\) vanish. If \(\bar A\) is nonscalar, the triple for \(A\) has at least one unit coordinate. Vanishing of the three minors therefore forces the second triple to be a *unique scalar multiple* of the first. Consequently
\[
C(A)=\{sI+tA:s,t\in R\},\qquad |C(A)|=|R|^2=q^{2d+2}.
\]
There are \(q^4-q\) nonscalar residue matrices and \(q^{4d}\) arbitrary radical lifts of each. This proves the first row.

**2. Matrices with scalar reduction.** Suppose \(\bar A=\alpha I\). Choose any scalar lift \(a\in R\) of \(\alpha\), and write \(A=aI+U\), where \(U\in M_2(\mathfrak m)\). Choose a \(k\)-basis \(e_1,\ldots,e_d\) of \(\mathfrak m\), and write \(U=\sum_{i=1}^{d}e_iU_i\) with \(U_i\in M_2(k)\). Because \(\mathfrak m^2=0\), the equation \([A,B]=0\) for \(B\in M_2(R)\) depends only on the reduction \(\bar B\), and is exactly
\[
[U_i,\bar B]=0\quad\text{for each }i=1,\ldots,d.
\]
Each prescribed \(\bar B\) has \(q^{4d}\) lifts. Thus
\[
|C(A)|=q^{4d}\left|\bigcap_{i=1}^{d}C_{M_2(k)}(U_i)\right|.
\]
There are \(q\) choices for \(\alpha\) and \(q^{4d}\) tuples of the \(U_i\) for each \(\alpha\).

**3. The exact three types of common commutants.** Every nonscalar \(T\in M_2(k)\) is cyclic: otherwise every nonzero vector would span a \(T\)-invariant line, forcing \(T\) to be scalar. In a cyclic basis \((v,Tv)\), any commuting operator is determined by its image of \(v\), and both \(I,T\) commute with \(T\). Its centralizer is therefore the two-dimensional commutative algebra \(k[I,T]\), with exactly \(q^2\) elements and \(q^2-q\) nonscalars. Two distinct such algebras intersect in the scalar matrices: if a nonscalar belonged to both, its own centralizer would force the algebras to agree. Therefore the nonscalar matrices partition among exactly
\[
L=\frac{q^4-q}{q^2-q}=q^2+q+1
\]
distinct regular centralizer algebras.

If all \(U_i\) are scalar, the common commutant has cardinality \(q^4\). There are exactly \(q^d\) such tuples. If not all are scalar, the common commutant has size \(q^2\) exactly when all \(U_i\) belong to one regular centralizer algebra. For each of the \(L\) choices there are \(q^{2d}-q^d\) tuples with at least one nonscalar member; there is no double counting. All remaining tuples have common commutant precisely the scalar matrices, of size \(q\). Their count is
\[
q^{4d}-q^d-L(q^{2d}-q^d).
\]
The latter quantity is strictly positive for \(d\ge2\), since one may take two noncommuting matrices as the first two tuple entries; choose any later entries. Multiplying these three counts by \(q\) for the possible residue scalar and by the free-lift factor \(q^{4d}\) for each centralizer gives the last three rows. The four centralizer powers are strictly ordered for \(d\ge2\). Summing row multiplicities yields \(q^{4d+4}\), the total number of matrices.

**4. Independent ordered-pair count.** There are exactly \(q^2\) residue pairs \((\bar A,\bar B)\) in which both matrices are scalar. Every one of their \(q^{8d}\) radical lift pairs commutes, because all mixed terms vanish and products of radical entries are zero. For a residue pair that commutes but is not scalar-scalar, at least one matrix, say \(\bar A\), is nonscalar and \(\bar B=\alpha I+\beta\bar A\). Choose commuting lifts \(A_0\) and \(B_0=aI+bA_0\) of these residues. Every other lift pair is \((A_0+U,B_0+V)\) with \(U,V\in M_2(\mathfrak m)\); the exact commutation equation becomes
\[
[\bar A,V-\beta U]=0.
\]
The \(k\)-linear map \(W\mapsto[\bar A,W]\) on \(M_2(k)\) has rank \(2\), so the displayed equation imposes precisely \(2d\) independent conditions on \(8d\) radical coordinates. Each commuting nonscalar residue pair therefore has \(q^{6d}\) commuting lifts.

For a scalar residue matrix there are \(q^4\) commuting partners, whereas for a nonscalar residue matrix there are \(q^2\). Hence the number of commuting residue pairs is \(q\cdot q^4+(q^4-q)q^2=q^6+q^5-q^3\), of which \(q^2\) are scalar-scalar. Weighting the two kinds of lift gives the claimed ordered-pair formula. Divide by \(q^{8d+8}\) for the probability. The scalar-scalar residue contribution equals \(q^{-6}\), and every other commuting residue pair contributes the strictly positive correction \((q^6+q^5-q^3-q^2)q^{-2d-8}\). Thus the conditional scalar-scalar probability is exactly
\[
\frac{q^{-6}}{q^{-6}+(q^6+q^5-q^3-q^2)q^{-2d-8}}
=1-O_q(q^{-2d}).
\]
This proves the theorem.

## Verification

The standalone standard-library C++17 program `check.cpp` enumerates **all ordered matrix pairs** over the split rings \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\) and \(\mathbb F_2[\varepsilon_1,\varepsilon_2]/(\varepsilon_i\varepsilon_j)\), and independently over the mixed-characteristic ring \(\mathbb Z/4\mathbb Z\). It calculates each element's actual centralizer cardinality and compares the resulting exact frequency map and total commuting-pair count with the formulas. Compile and run with `g++ -std=c++17 -O3 -Wall -Wextra check.cpp -o check && ./check`. Its actual successful output is embedded in `check_output.txt`.

Over \(\mathbb F_2[\varepsilon_1,\varepsilon_2]/(\varepsilon_i\varepsilon_j)\) there are \(4096\) matrices. Their centralizers have respective sizes \(64,512,1024,4096\), with respective multiplicities \(3584,336,168,8\), giving exactly \(606208\) ordered commuting pairs. The direct check enumerates all \(4096^2=16,777,216\) ordered pairs. Finite computations corroborate but do not prove the all-field theorem.

## Relationship to prior work

Prasad, Singla and Spallone [1] establish extension-theoretic similarity methods for local rings of length two. Their Section 10, Theorem 10.3 and Corollary 10.4 explicitly reduce nonprincipal square-zero radical conjugacy to diagonal actions on matrix tuples, showing a general universality depending on \(q,d\); this major structural precursor is credited. They do **not** state an all-\(q,d\) four-stratum element-centralizer census or the saturation and conditional-concentration law. Their matrix-pair orbit classification is intentionally left open, and the present work avoids that classification by using common-commutant dimensions rather than orbit types.

The finite-chain-ring full-matrix commuting-graph classification [2] contains the entire principal length-two case \(d=1\), including its three centralizer sizes and \(6400\) ordered commuting pairs over \(\mathbb Z/4\mathbb Z\). That boundary is not claimed as novel. Its assumption that the coefficient ring is a *chain ring* excludes all nonprincipal \(d\ge2\) cases and their fourth centralizer size. Another related finite-local-ring result [3] gives a four-stratum spectrum for an **affine transformation monoid**, whose algebraic objects and centralizers differ from those of the full matrix ring. The nonprincipal square-zero matrix *power equation* census [4] counts solutions of \(X^2=0\), not solutions of \(XY=YX\) or element-centralizers. Britnell and Wildon [5] investigate similarity types of commuting matrices over fields, giving background on field-level centralizer theory, but not this nonprincipal coefficient-ring spectrum.

## Limitations

The new claim is restricted to \(2\times2\) full matrix rings with **nonprincipal square-zero maximal ideal** (embedding dimension at least two). No classification of conjugacy or centralizer *isomorphism types* is asserted; the result is an element-centralizer size distribution. Finite rings with nonzero radical square or noncommutative coefficient rings are outside scope. The limiting statement fixes \(q\) while \(d\to\infty\), not vice versa. Broader historical ring-similarity or finite-ring commuting results might implicitly imply this numerical spectrum; the examined general results and their exact implication limits are described above. Independent mathematical validation has not been performed.

## References

1. A. Prasad, P. Singla and S. Spallone, *Similarity of matrices over local rings of length two*, arXiv:1212.6157 (first public 2012-12-26), in particular Section 10, Theorem 10.3 and Corollary 10.4. https://arxiv.org/abs/1212.6157
2. *Commuting-graph universality across finite chain-ring matrix algebras*, published result, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-commuting-graph-universality-across-finite-chain-ring-matrix-alg--2870166b051c .
3. *Centralizer spectra of finite affine monoids distinguish local-ring geometry*, published result, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-centralizer-spectra-of-finite-affine-monoids-distinguish-local-r--5531b23a5b4d .
4. *Rank-one escape and exact square-zero census over nonprincipal radical-square-zero local rings*, published result, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-rank-one-escape-and-exact-square-zero-census-over-nonprincipal-r--84eca5cc5573 .
5. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (first public 2010-01-06), https://arxiv.org/abs/1001.0811 .
