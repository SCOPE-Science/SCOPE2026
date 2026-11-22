# A first cubic-only Walsh blind spot in three-row rectangular Young diagrams

## Finding
For each integer \(n\ge1\), take every Young diagram inside a \(3\times n\) rectangle, encode its individual cell incidences in \(G_n=\mathbb F_2^{3n}\), and form unnormalized counting convolution \(T_n\) by this set. Write
\[
W_n(S)=\sum_{\lambda_1\ge\lambda_2\ge\lambda_3\ge0,\ \lambda_1\le n}(-1)^{\sum_{(r,j)\in S}\mathbf1_{\{j\le\lambda_r\}}},\quad S\subseteq[3]\times[n],
\]
and let \(d_n\) be the smallest cardinality of a character support \(S\) for which \(W_n(S)=0\), or \(\infty\) if no such support exists. The first four widths congruent to two modulo four have
\[
\boxed{d_2=2,\quad d_6=2,\quad d_{10}=3,\quad d_{14}=2.}
\]
In particular, at width ten **none of the thirty weight-one or 435 weight-two characters vanishes, but exactly thirty of the 4,060 weight-three characters vanish**. They form fifteen pairs under the half-turn of the rectangle. The first occurrence of this cubic-only cancellation within all widths \(1\le n\le10\) is \(n=10\); for odd widths there is a singleton cancellation, and at widths divisible by four no Fourier character vanishes.

Here is the complete list of fifteen representatives of the thirty vanishing triples at width ten. A cell \((r,j)\) means row \(r\) from the top and column \(j\) from the left. Apply \((r,j)\mapsto(4-r,11-j)\) to obtain its other member.

| No. | Representative triple |
|---:|---|
| 1 | \((1,2),(1,5),(3,3)\) |
| 2 | \((1,2),(1,8),(3,6)\) |
| 3 | \((1,2),(1,9),(3,1)\) |
| 4 | \((1,3),(1,9),(3,1)\) |
| 5 | \((1,4),(1,9),(2,3)\) |
| 6 | \((1,4),(2,8),(3,2)\) |
| 7 | \((1,5),(1,8),(2,8)\) |
| 8 | \((1,5),(1,8),(3,3)\) |
| 9 | \((1,6),(2,9),(3,3)\) |
| 10 | \((1,7),(2,7),(2,9)\) |
| 11 | \((1,8),(2,5),(2,8)\) |
| 12 | \((1,8),(2,5),(3,3)\) |
| 13 | \((1,8),(2,6),(2,8)\) |
| 14 | \((1,9),(2,2),(3,2)\) |
| 15 | \((1,9),(2,3),(3,1)\) |

## Assumptions and scope
The coordinates are the thirty independent binary cell coordinates, **not** row-length coordinates or area alone. An admissible shape is the triple of row lengths \((a,b,c)\), \(0\le c\le b\le a\le n\). The convolution is \((T_nf)(x)=\sum_{I}f(x+\mathbf1_I)\) on the counting-measure Hilbert space over \(G_n\). Its Walsh eigenvalue at \(S\) is the integer \(W_n(S)\); a character vanishes precisely when that eigenvalue is zero. No assertion is made about arbitrary larger widths, global nullity at width ten, or full signed spectra.

## Proof
**1. A closed, exact low-degree multiplier formula.** Fix any selected cell set \(S\) and a subset \(J\subseteq S\). Let \(A_J,B_J,C_J\) be the maximum selected column in rows one, two, three respectively, taking the maximum of an empty set to be zero. The number of diagrams containing all cells in \(J\) is
\[
N_n(J)=\sum_{b=\max(B_J,C_J)}^n (b-C_J+1)\bigl(n-\max(A_J,b)+1\bigr).
\]
Indeed, choose middle-row length \(b\), choose bottom-row length \(c\) from \(C_J\) through \(b\), and top-row length \(a\) from \(\max(A_J,b)\) through \(n\). The identity \((-1)^x=1-2x\) for binary \(x\) then gives the **exact** inclusion-exclusion certificate
\[
\boxed{W_n(S)=\sum_{J\subseteq S}(-2)^{|J|}N_n(J).}
\]
For \(|S|\le3\), this has at most eight terms, each an explicit sum of at most \(n+1\) integers. This formula involves no unproved probabilistic approximation, floating-point calculation, or truncated infinite computation.

**2. The width-ten exhaustive certificate.** Evaluate this formula on every \(S\subseteq[3]\times[10]\) with \(|S|=1,2,3\), a total of \(30+435+4060=4525\) cases. Grouping by cardinality produces, respectively, \(0,0,30\) zeros. For the 435 pairs the minimum absolute multiplier is two; indeed grouping pairs by row types \((1,1),(1,2),(1,3),(2,2),(2,3),(3,3)\), the respective minimum absolute values are \(4,2,4,10,2,4\) among \(45,100,100,45,100,45\) pairs. All thirty vanishing triples are exactly those in the displayed list and their half-turns. For a check independent of the inclusion-exclusion formula, enumerate all \(\binom{13}{3}=286\) shapes, store the 286 membership bits for each cell, and use parity of the XOR of selected membership masks. The two integer methods agree on **every** sparse character. The attached self-contained `verify_sparse_three_row.py` performs both methods and checks the exact representative table.

**3. Why the sparse threshold first appears here.** There are \(\binom{n+3}{3}\) diagrams; this number is odd whenever \(4\mid n\), by the binary binomial criterion, so no Fourier eigenvalue can vanish at such widths. If \(n\) is odd, the half-turn/complement bijection on diagrams toggles the central cell \((2,(n+1)/2)\). Consequently its singleton Walsh coefficient is zero. The only remaining widths less than ten are \(n=2,6\). Formula 1 gives no zero singleton at either width and gives two and three zero pairs respectively; for example at \(n=2\), \(S=\{(1,1),(3,1)\}\) vanishes, and at \(n=6\), \(S=\{(1,6),(3,1)\}\) vanishes. The same exact formula at \(n=14\) gives no singleton zeros and exactly the two zero pairs \(\{(1,10),(1,14)\}\) and \(\{(3,1),(3,5)\}\). This is the asserted nonmonotone \(2,2,3,2\) sequence.

**4. Half-turn pairing.** For the involution \(\rho(r,j)=(4-r,n+1-j)\), mapping each diagram \(I\) to \(\rho(P\setminus I)\) permutes the diagrams. Hence \(W_n(\rho S)=(-1)^{|S|}W_n(S)\). Thus the thirty zero triples occur as fifteen two-element orbits, and direct comparison of the fifteen representatives with all 4,060 evaluated triples proves the claimed complete classification.

## Verification
Run `python3 verify_sparse_three_row.py` with the Python standard library. It prints the exact row counts and finishes with `PASS`. For widths two, six, ten, and fourteen, it exhausts respectively the weight ranges one–two, one–two, one–three, and one–two. In every case it compares independent bitset signed sums with the polynomial-size inclusion-exclusion certificate and checks all reported zero counts. It verifies the fifteen width-ten orbit representatives, the two width-fourteen pairs, all odd-width central-cell cancellations through thirteen, and the odd cardinality at widths four, eight, and twelve. The certificate proves only these declared finite results and the elementary parity/duality statements; it does not infer an all-order pattern from data.

## Relationship to prior work
Cohn–Larsen–Propp (public 13 January 1998) and Ciucu (public 4 August 1998) establish boxed plane-partition/hexagon-tiling objects and unsigned enumerations, not the low-support cellwise signed transform. Dhand (public 11 March 2013) gives rank decompositions of \(L(m,n)\) and a complement involution, but no cellwise Walsh cancellation classification. De Wolf supplies standard Boolean Fourier conventions. Closely related published two-row Young-diagram results classify all-width signed singularity and Pell-exceptional first supports, but their two-row formulas do not evaluate the **three-row** incidence transform at width ten. A published finite \(2\times3\times4\) boxed-plane-partition spectral census concerns a different \(24\)-cell poset and does not imply the present \(30\)-cell degree-three coefficient list. The polynomial low-degree inclusion-exclusion and the exact width-ten census are the specific new assertions here, under the bounded cited comparison.

## Limitations
The theorem is restricted to the stated sparse characters and finite widths; the nullity at width ten and the first-zero degree beyond fourteen are unknown here. The result is not an all-order Fourier-invertibility classification. Novelty has been compared against accessible primary and published mathematical results, not proven against inaccessible or unindexed literature. Independent validation has not been performed.

## References
1. H. Cohn, M. Larsen, and J. Propp, *The shape of a typical boxed plane partition*, first arXiv public submission 13 January 1998, arXiv:math/9801059, https://arxiv.org/abs/math/9801059.
2. M. Ciucu, *Plane partitions I: A generalization of MacMahon's formula*, first arXiv public submission 4 August 1998, arXiv:math/9808017, https://arxiv.org/abs/math/9808017.
3. V. Dhand, *Rank-unimodality of Young's lattice via explicit chain decomposition*, arXiv:1303.2536v1 (11 March 2013), https://arxiv.org/html/1303.2536v1.
4. R. de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, *Theory of Computing* Graduate Surveys 1 (25 September 2008), https://theoryofcomputing.org/articles/gs001/.
5. *A Pell-exceptional first Walsh cancellation law for two-row Young diagrams*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-a-pell-exceptional-first-walsh-cancellation-law-for-two-row-youn--3420cb34c845.
6. *Fourier invertibility transition and Brownian spectral law for two-row order ideals*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-fourier-invertibility-transition-and-brownian-spectral-law-for-t--ba493bfce7aa.
7. *Exact Walsh spectrum and optimal endpoint projection for \(2\times3\times4\) boxed plane partitions*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-walsh-spectrum-and-optimal-endpoint-projection-for-2-times--009897c7d9c4.
