# First unexpected Fourier zeros of classical parking-function convolution

## Finding

For each integer \(1\le n\le5\), put \(m=n+1\) and let \(G_n=(\mathbb Z/m\mathbb Z)^n\). Let \(P_n\subset G_n\) be the classical parking functions in zero-based notation: each coordinate belongs to \(\{0,\ldots,n-1\}\), and the sorted coordinates \(b_0\le\cdots\le b_{n-1}\) satisfy \(b_j\le j\) for every \(0\le j<n\). For \(k\in G_n\), write
\[
 F_n(k)=\sum_{a\in P_n}\exp\!\left(\frac{2\pi i}{m}\sum_{j=1}^n k_ja_j\right).
\]
The *forced zeros* are precisely the nonzero frequencies with \(\sum_j k_j=0\pmod m\). The following is an exact classification through length five.

| \(n\) | \(|P_n|\) | \(|G_n|\) | forced zeros | additional zeros | convolution rank |
|---|---:|---:|---:|---:|---:|
| 1 | 1 | 2 | 0 | 0 | 2 |
| 2 | 3 | 9 | 2 | 0 | 7 |
| 3 | 16 | 64 | 15 | 0 | 49 |
| 4 | 125 | 625 | 124 | 0 | 501 |
| 5 | 1296 | 7776 | 1295 | **360** | **6121** |

In particular, **length five is the first appearance of Fourier zeros not explained by the circular-parking diagonal-translation symmetry**. At \(n=5\), the 360 additional zeros form exactly five coordinate-permutation orbits, whose sorted representatives and sizes are

| Sorted frequency \(k\) | Orbit size |
|---|---:|
| \((1,2,3,3,4)\) | 60 |
| \((1,2,3,3,5)\) | 60 |
| \((1,2,3,4,5)\) | 120 |
| \((1,3,3,4,5)\) | 60 |
| \((2,3,3,4,5)\) | 60 |

Thus all additional zeros have every coordinate nonzero modulo six. The convolution rank here means the rank, over \(\mathbb C\) or \(\mathbb R\), of convolution on functions \(G_n\to\mathbb C\) or \(G_n\to\mathbb R\) by \(\mathbf1_{P_n}\).

## Assumptions and scope

All groups are finite, characters are unnormalized, and \(P_n\) consists of ordered preference lists (not parking outcomes, multisets, rooted trees, or quotients by permutation). The frequency convention is positive exponent; conjugation changes no zero sets. The classification is asserted only for \(1\le n\le5\). Its ``first'' language refers to this natural length-indexed family and only to zeros beyond the diagonal-annihilator constraint.

## Proof

**Forced zeros.** Pollak's circular parking argument shows that \(P_n\) contains one representative from each orbit of the free diagonal action \(a\mapsto a+t(1,\ldots,1)\) on \(G_n\). Indeed, park \(n\) cars in \(n+1\) circularly ordered places. There is one empty place, rotated equivariantly by translating every preference. Exactly one translated tuple leaves the last place empty; this is precisely the ordinary linear parking condition. If \(k\ne0\) and \(\sum k_j\equiv0\pmod m\), its character is constant on each diagonal orbit. Its sum over \(P_n\) is therefore \(1/m\) times its sum over \(G_n\), which is zero by character orthogonality. There are \(m^{n-1}-1\) such frequencies.

**Exhaustive classification of the remaining frequencies.** The condition defining \(P_n\) is invariant under all permutations of its \(n\) coordinates. Consequently \(F_n(k)\) depends only on the sorted multiset of residues of \(k\). There are exactly \(\binom{m+n-1}{n}\) such multisets. For each sorted frequency \(k\), define integer counts
\[
 c_j(k)=\#\{a\in P_n:\;\textstyle\sum_{i=1}^n k_i a_i\equiv j\pmod m\},\quad 0\le j<m.
\]
Then \(F_n(k)=\sum_{j=0}^{m-1}c_j(k)\zeta_m^j\), where \(\zeta_m=\exp(2\pi i/m)\). It vanishes if and only if the integer polynomial \(\sum_jc_j(k)X^j\) is divisible by the cyclotomic polynomial \(\Phi_m(X)\). All counts are obtained by the literal bounded loops over the \(n^n\) candidate preference lists and the sorted frequency multisets; no floating point arithmetic is involved. The attached `check_parking.py` implements these loops and reduction modulo \(\Phi_m\) for all five lengths. It certifies all rows of the table and writes the complete 252-row length-five sorted-frequency certificate `parking5_frequency_orbits.csv`. The orbit sizes are the multinomial values \(n!/\prod_j d_j!\), where \(d_j\) are the multiplicities of frequency residues.

For transparent checking of the key six-root cancellation, \(\Phi_6(X)=X^2-X+1\) and
\[
 F_5(k)=[c_0-c_2-c_3+c_5]+[c_1+c_2-c_4-c_5]\zeta_6.
\]
At the first additional-zero representative \(k=(1,2,3,3,4)\), the six residue counts are
\[
 (c_0,c_1,c_2,c_3,c_4,c_5)=(209,220,215,217,212,223),
\]
so both integer coefficients vanish: \(209-215-217+223=0\) and \(220+215-212-223=0\). The full certificate establishes that precisely the five listed sorted representatives vanish outside the forced set; its 252 rows are all the length-five multiset types. In lengths one through four, the same cyclotomic method finds no additional zero type.

**Independent census.** The attached `check_direct.cpp` enumerates all \(7776\) length-five frequencies separately, evaluates all \(1296\) terms in each character sum, and uses only the two displayed integer-coefficient equations. It confirms \(1295\) forced plus \(360\) additional zeros, with the same five sorted frequency types. This program does not use the orbit table or cyclotomic-polynomial reduction code. Finally, complex Fourier diagonalization of finite-group convolution identifies operator rank with the number of nonzero Fourier multipliers. The displayed ranks follow by subtracting the exact zero counts from \(|G_n|\).

## Verification

Run `python3 check_parking.py` in a directory containing the script. It prints five verified rows ending in `PARKING_SIXTH_ROOT_FIRST_EXTRA_ZERO_PASS` and writes the length-five orbit certificate. Independently run `g++ -O2 -std=c++17 check_direct.cpp -o check_direct && ./check_direct`, which prints `PARKING5_DIRECT_CHARACTER_PASS`. No third-party libraries or network access are required. Both programs were executed successfully, and the certificate was checked for 252 sorted frequency types, total orbit weight 7776, and the listed five exceptional types.

## Relationship to prior work

Classical parking enumeration and the circular-parking transversal mechanism imply the \(m^{n-1}-1\) forced zeros but not the absence or occurrence of other zeros. Kostić and Yan (2006) study multiparking functions and the univariate reversed-sum enumerator; their statements do not classify Fourier coefficients with independent weights on each preference coordinate. Rhoades (2012) studies parking-space representations and symmetric-group characters; these are different from additive characters on \((\mathbb Z/m\mathbb Z)^n\). Gorsky, Mazin and Vazirani (2014) study rational parking functions and affine-permutation bijections rather than this root-of-unity spectrum. The accessible introduction and Section 6 material from Kung and Yan's (2003) Gončarov interpolation work treat univariate sum enumerators; the full paper was inaccessible and remains a priority risk. General finite Fourier techniques reduce the question to exact cyclotomic arithmetic but do not supply the 360-zero classification.

## Limitations

This is an exact finite boundary and spectrum-support classification through length five, not an all-length characterization, a full distribution of nonzero multiplier magnitudes, or a statement about general \(G\)-parking functions. A general formula for all \(n\) is not established. Prior-art comparison does not constitute an independent priority certification. The computational certificate is exhaustive for the claimed finite domains; independent mathematical review has not been performed.

## References

- D. Kostić and C. H. Yan, *Multiparking Functions, Graph Searching, and the Tutte Polynomial*, arXiv:math/0607602, first posted 2006-07-24. https://arxiv.org/abs/math/0607602
- B. Rhoades, *Parking Structures: Fuss Analogs*, arXiv:1205.4293, first posted 2012-05-19. https://arxiv.org/html/1205.4293v2
- E. Gorsky, M. Mazin, and M. Vazirani, *Affine permutations and rational slope parking functions*, arXiv:1403.0303, first posted 2014-03-03. https://arxiv.org/html/1403.0303v1
- J. P. S. Kung and C. H. Yan, *Gončarov polynomials and parking functions*, Journal of Combinatorial Theory, Series A 102 (2003), 16–37. https://doi.org/10.1016/S0097-3165(03)00009-8
