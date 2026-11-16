# Fourier interpolation hierarchy and quadratic spectrum of the \(4\times4\) binary two-regular fiber

## Finding
Let \(\mathcal D\) be the 90 binary \(4\times4\) matrices with exactly two ones in every row and column. Let \(H_r\) have one row for every \(X\in\mathcal D\) and one column for every subset \(S\) of the 16 cells of size at most \(r\), with entry \(\chi_S(X)=(-1)^{\sum_{e\in S}X_e}\). For \(0\le r\le4\),
\[
(\operatorname{rank}H_0,\ldots,\operatorname{rank}H_4)=(1,10,39,75,90).
\]
Consequently, degree four is the **least** Boolean Fourier degree sufficient to interpolate every function on \(\mathcal D\). Equivalently, the orbit-harmonics quotient of this finite binary fixed-margin locus has Hilbert series
\[
1+9t+29t^2+36t^3+15t^4.
\]
The positive eigenvalues of \(H_2H_2^{\mathsf T}\) are:

| Eigenvalue | Multiplicity |
|---:|---:|
| 160 | 9 |
| 256 | 9 |
| 320 | 4 |
| 384 | 12 |
| 512 | 4 |
| 650 | 1 |

The remaining 51 eigenvalues of this \(90\times90\) matrix are zero. The \(137\)-column coefficient Gram matrix \(H_2^{\mathsf T}H_2/90\) has rank 39, nullity 98, and the same nonzero eigenvalues divided by 90. Thus the sharp ratio of largest to smallest **positive** eigenvalue is \(65/16\), and the sharp singular-value condition number on the identifiable coefficient quotient is \(\sqrt{65}/4\).

## Assumptions and scope
All matrices and coordinates are labelled; no quotient by row or column permutations is taken. Entry order is row-major, and all coefficient spaces are real. A degree-\(r\) Fourier polynomial is a linear combination of \(\chi_S\) with \(|S|\le r\). Singular values use the unnormalized evaluation matrix \(H_r\); for uniform sampling the matrix is scaled by \(90^{-1/2}\). The kernel is factored out when a condition number is stated. The graph-theoretic equivalent of \(\mathcal D\) is the set of labelled two-regular spanning bipartite subgraphs of \(K_{4,4}\), or the set of Eulerian orientations of \(K_{4,4}\) with a fixed shore-to-shore convention.

## Proof
Every row has one of six two-subsets of the four columns. There are exactly 18 matrices whose bipartite support decomposes into two disjoint four-cycles and 72 whose support is one eight-cycle, giving \(|\mathcal D|=90\) (the counts can also be obtained by direct enumeration of the six row patterns subject to column margins).

For two binary configurations \(X,Y\), put \(d=d(X,Y)\), their Hamming distance. The identity
\[
(H_rH_r^{\mathsf T})_{X,Y}=\sum_{j=0}^{r}K_j(d;16),\qquad
K_j(d;16)=\sum_{a=0}^{j}(-1)^a\binom da\binom{16-d}{j-a},
\]
where out-of-range binomial coefficients vanish, follows by sorting the size-\(j\) subsets by their number of intersections with \(X\triangle Y\). In particular, for \(r=2\),
\[
(H_2H_2^{\mathsf T})_{X,Y}=137-34d+2d^2.
\]
All 90 matrices are deterministically enumerated from the row-pattern criterion, then the characteristic polynomials of the five exact-integer \(90\times90\) matrices above are computed. Their zero-root multiplicities are respectively \(89,80,51,15,0\). For the quadratic matrix the characteristic polynomial is exactly
\[
\lambda^{51}(\lambda-160)^9(\lambda-256)^9(\lambda-320)^4
(\lambda-384)^{12}(\lambda-512)^4(\lambda-650).
\]
The two supplied Python programs compute these identities by independent construction routes: `verify_krawtchouk.py` enumerates six possible row patterns and applies the displayed distance formula, while `verify_direct.py` scans all 65,536 sixteen-bit arrays and directly multiplies their signed-character evaluation matrix. The first checks exact characteristic polynomials for every degree from zero to four, including two explicit algebraic quadratic factors at degrees three and four. The second checks the full quadratic characteristic polynomial independently and all five ranks by exact elimination modulo 65521. No numerical eigenvalue rounding is used in the proof.

Finally, on a binary point set, \(\chi_S(X)=\prod_{e\in S}(1-2X_e)\). Expansion in squarefree monomials is a triangular invertible change of basis preserving total-degree filtration. Hence \(\operatorname{rank}H_r\) is the dimension of polynomial functions of degree at most \(r\) on \(\mathcal D\). Taking successive differences gives \(1,9,29,36,15\), precisely the graded dimensions of the orbit-harmonics quotient defined from the degree filtration on the point-set coordinate ring. The exact spectrum gives the quotient conditioning by comparing its smallest and largest positive eigenvalues.

## Verification
With Python 3 and the packages in `requirements.txt`, run the two attached programs from the same directory:

```text
python verify_krawtchouk.py
python verify_direct.py
```

Both terminate with an explicit success marker. The independent brute-force checker uses 64-bit integer matrix multiplication only for sums of at most 2517 signed units, so those integer products cannot overflow; it uses exact modular elimination and an exact symbolic quadratic characteristic polynomial. The distance checker uses SymPy exact integers. The tests were executed successfully from the attached source files. The complete character-polynomial factorization is stronger than merely measuring floating-point rank.

## Relationship to prior work
Binary fixed-margin matrices and their uniform sampling are classical; Canfield–Greenhill–McKay, Blanchet–Stauffer and Barvinok study enumeration, sampling and typical structure [1–3]. Their theorems do not give this finite-degree Fourier evaluation spectrum. Oh–Rhoades study orbit harmonics of **nonnegative-integer** contingency tables and explicitly pose the separate binary fixed-margin locus as Problem 7.4 [4]. The present result is one exact small binary-locus Hilbert series, not a general solution to their problem. A general identity that a finite point set has an associated graded coordinate ring is standard; the evaluated five-rank hierarchy and quadratic six-level spectrum are the new finite calculations.

## Limitations
This is an exact finite classification for one labelled size and one margin vector. No extrapolation to larger even square tables, no general presentation of their orbit-harmonics ideals, and no higher-degree singular-value claim is made. Originality assessment is bounded by the inspected literature and indexed mathematical records; unindexed computational tables or algebraic results may anticipate these numbers.

## References
1. E. R. Canfield, C. Greenhill and B. D. McKay, *Asymptotic enumeration of dense 0-1 matrices with specified line sums*, arXiv:math/0606496, first publicly posted 2006-06-20, https://arxiv.org/abs/math/0606496.
2. J. Blanchet and A. Stauffer, *Characterizing Optimal Sampling of Binary Contingency Tables via the Configuration Model*, arXiv:1007.1214, first publicly posted 2010-07-07, https://arxiv.org/abs/1007.1214.
3. A. Barvinok, *Matrices with prescribed row and column sums*, arXiv:1010.5706, first publicly posted 2010-10-27, https://arxiv.org/html/1010.5706v1.
4. J. Oh and B. Rhoades, *Zigzags, contingency tables, and quotient rings*, arXiv:2503.19694, first publicly posted 2025-03-25, especially Problem 7.4, https://arxiv.org/html/2503.19694v2.
