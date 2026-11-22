# No binary full-spark Gabor window on the seven-cycle

## Finding

**Theorem.** Let \(g:\mathbb Z_7\to\{+1,-1\}\) be any binary phase-only window. Write \(\omega=\exp(2\pi i/7)\) and form its full cyclic Gabor synthesis matrix
\[
G_g(x,(a,b))=\omega^{bx}g(x-a),\qquad x,a,b\in\mathbb Z_7.
\]
There is a set \(\Lambda\subset\mathbb Z_7^2\) of exactly seven distinct time-frequency indices such that \(\det G_g[:,\Lambda]=0\). Consequently **no one of the 128 binary windows gives a full-spark cyclic Gabor frame in dimension seven**. Equivalently, all 64 windows after normalization by a global sign are spark deficient.

The conclusion is proved by a complete nine-class symmetry reduction and nine explicit integer determinant identities. It concerns the full collection of 49 cyclic time-frequency shifts and arbitrary choices of seven columns, not merely a prescribed Gabor sublattice.

## Assumptions and scope

All indices are residues modulo seven. Translation and modulation mean \((T_a g)(x)=g(x-a)\) and \((M_b g)(x)=\omega^{bx}g(x)\), with \(G_g\) having rows in order \(x=0,\ldots,6\). A Gabor frame of 49 vectors in \(\mathbb C^7\) is *full spark* when each of its seven-column submatrices is invertible. We allow no zero or nonbinary entries in \(g\). Normalization \(g(0)=1\) loses no case because multiplication by \(-1\) multiplies every Gabor column by the same scalar.

For \(m\in\{0,\ldots,63\}\), define the normalized sign window \(g_m(0)=1\) and, for \(1\le j\le6\), \(g_m(j)=(-1)^{\lfloor m/2^{j-1}\rfloor\bmod2}\). A column index \(k\in\{0,\ldots,48\}\) encodes \((a,b)=(\lfloor k/7\rfloor,k\bmod7)\). The attached `proof/witnesses.json` fixes this complete indexing convention.

## Proof

**1. Symmetries.** Multiplying \(g\) by \(-1\), translating its coordinates, or reversing them leaves the full-spark property invariant. For a translation, \(M_bT_a(T_sg)=M_bT_{a+s}g\), which reindexes columns. For coordinate reversal \((Rg)(x)=g(-x)\), one has \(M_bT_a(Rg)=R(M_{-b}T_{-a}g)\), giving a fixed invertible row permutation and column reindexing. Thus we may classify normalized binary windows under cyclic shifts and reversal.

The resulting **nine** disjoint classes have the following smallest normalized mask representatives. The third column lists a seven-element time-frequency index set where the corresponding determinant vanishes.

| Mask \(m\) | Number of normalized windows | Seven selected column indices |
|---|---:|---|
| 0 | 1 | 38, 28, 7, 33, 41, 15, 47 |
| 1 | 7 | 31, 47, 45, 15, 17, 19, 33 |
| 3 | 7 | 23, 47, 43, 8, 28, 7, 44 |
| 5 | 7 | 37, 5, 3, 40, 6, 2, 38 |
| 7 | 7 | 35, 34, 2, 5, 6, 28, 30 |
| 9 | 7 | 15, 43, 28, 4, 29, 32, 11 |
| 11 | 14 | 32, 11, 14, 23, 15, 4, 27 |
| 19 | 7 | 13, 11, 43, 12, 27, 48, 8 |
| 21 | 7 | 43, 36, 14, 44, 38, 45, 7 |

The class sizes sum to \(64\). The script `proof/check_exact.py` independently generates these group-action orbits from all 64 normalized masks and checks disjointness, coverage, representatives and sizes; it does not assume orbit completeness from the table alone.

**2. Exact vanishing determinants.** Fix a representative \(m\), its ordered column list \(k_0,\ldots,k_6\), and write \(k_j=7a_j+b_j\). Expanding the determinant across permutations \(\sigma\in S_7\) gives
\[
\det G_{g_m}[:,\Lambda]
=\sum_{\sigma\in S_7}\operatorname{sgn}(\sigma)
\prod_{x=0}^{6}g_m(x-a_{\sigma(x)})\,
\omega^{\sum_{x=0}^{6}b_{\sigma(x)}x}
=\sum_{r=0}^{6}C_r(m,\Lambda)\omega^r,
\]
where the **integer** \(C_r\) is the sum of signed products for permutations satisfying \(\sum_x b_{\sigma(x)}x\equiv r\pmod7\). The 5,040 terms are finite and exactly enumerable. For **each of the nine rows** the seven coefficient sums are all exactly zero:
\[
(C_0,C_1,C_2,C_3,C_4,C_5,C_6)=(0,0,0,0,0,0,0).
\]
No approximate cyclotomic equality is used: even the seven group-algebra coefficients vanish separately. Therefore all nine displayed minors are zero over \(\mathbb C\). Symmetry then supplies a zero minor for every one of the 64 normalized words and hence for every one of the 128 binary words. This proves the theorem.

## Verification

From a directory containing this document and its `proof` directory, execute:

```sh
python proof/check_exact.py
python proof/check_modular.py
```

`proof/check_exact.py` enumerates all normalized sign words, checks the nine-orbit partition, and evaluates the 5,040 determinant terms for each witness using integer arithmetic. `proof/check_modular.py` uses a different matrix/rank implementation: it forms each seven-column matrix over the prime field of size \(998244353\) at all six primitive seventh roots, and verifies singularity by Gaussian elimination. Their recorded successful stdout is included as `proof/check_exact_output.txt` and `proof/check_modular_output.txt`. The exact integer checker, rather than the finite-field replay alone, establishes vanishing over \(\mathbb C\).

## Relationship to prior work

Lawrence, Pfander and Walnut established the generic full-spark theorem for prime cyclic Gabor systems. Malikiosis established all-order generic existence and explicit algebraic constructions, and separately classified a large group of spark-deficient Clifford eigenvectors and all noncyclic-group obstructions. Those statements concern generic complex windows, algebraic constructions, or particular Clifford symmetries, and do not imply this **universal negative statement on the finite binary alphabet in the cyclic group of order seven**. The result is also logically distinct from previously calculated binary full-spark windows on the five-cycle: neither five-point existence nor the general genericity theorem controls seven-point sign windows.

## Limitations

No assertion is made about windows with three or more phases, arbitrary unit-modulus phases, nonbinary real amplitudes, or other cyclic dimensions. The proof shows that at least one seven-column selection fails for each binary window; it does not compute the full spark number, the entire distribution of deficient selections, or conditioning of the nondeficient ones. A search of indexed literature and related mathematical records did not locate an identical binary-seven-cycle classification, but absence from an index does not establish global historical priority. Independent mathematical audit has not been performed.

## References

1. J. Lawrence, G. E. Pfander and D. Walnut, *Linear independence of Gabor systems in finite dimensional vector spaces*, Journal of Fourier Analysis and Applications 11 (2005), 715–726. DOI: 10.1007/s00041-005-5017-6. Author manuscript: https://www.mathematik.uni-marburg.de/~pfander/pubs/finitegabor.pdf.
2. R.-D. Malikiosis, *A Note on Gabor Frames in Finite Dimensions*, arXiv:1304.7709, initially public 2013-04-29. https://arxiv.org/abs/1304.7709.
3. R.-D. Malikiosis, *Spark Deficient Gabor Frames*, arXiv:1602.09012, initially public 2016-02-29. https://arxiv.org/abs/1602.09012.
