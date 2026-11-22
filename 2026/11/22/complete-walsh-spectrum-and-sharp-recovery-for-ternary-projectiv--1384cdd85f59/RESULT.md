# Complete Walsh spectrum and sharp recovery for ternary projective-plane bases

## Finding

Let \(E=\operatorname{PG}(2,\mathbb F_3)\) be the thirteen projective points, and let \(\mathcal B\) be the \(234\) noncollinear unordered point triples (the bases of its rank-three projective matroid). Embed each triple as its incidence vector in \(G=\mathbb F_2^{E}\). Define unnormalized convolution \(T h=f*h\) on \(\ell^2(G)\), with \(f=\mathbf1_{\mathcal B}\). Every Walsh character indexed by \(S\subseteq E\) is an eigenvector with integer multiplier

\[
\lambda(S)=\sum_{B\in\mathcal B}(-1)^{|B\cap S|}.
\]

The **complete signed spectral multiplicities** are

| Eigenvalues | Multiplicity of each sign |
|:--|--:|
| \(\pm234\) | 1 |
| \(\pm126\) | 13 |
| \(\pm54\) | 78 |
| \(\pm18\) | 611 |
| \(\pm14\) | 234 |
| \(\pm10\) | 1,872 |
| \(\pm6\) | 1,053 |
| \(\pm2\) | 234 |

Here each row means the positive and negative eigenvalues have the stated multiplicity separately. Thus all \(8192\) eigenvalues are nonzero, with exactly \(4096\) of each sign. The **sharp recovery constants** are

\[
\operatorname{rank}(T)=8192,\qquad
\min_S|\lambda(S)|=2,\qquad
\|T^{-1}\|_{2\to2}=\frac12,\qquad
\kappa_2(T)=117.
\]

Every multiplier satisfies \(\lambda(S)\equiv2\pmod4\); consequently the integral convolution matrix has determinant of exact two-adic valuation \(8192\). These are exact finite statements for this projective plane, not claims about arbitrary projective geometries.

## Assumptions and scope

Points are one-dimensional subspaces of \(\mathbb F_3^3\); a line is a two-dimensional subspace, containing four points. Exactly thirteen lines exist, every pair of points lies on one line, and each point lies on four lines. A triple is a basis precisely when it is not contained in a line. Point labels are arbitrary and do not affect the statement. The group \(G\) is thirteen-dimensional over \(\mathbb F_2\), not thirteen-dimensional over \(\mathbb F_3\). Fourier multipliers here are **unnormalized counting** multipliers; for the probability kernel \(f/234\) divide every multiplier by \(234\), retaining condition number \(117\).

## Proof

There are \(\binom{13}{3}=286\) point triples. Since there are thirteen lines and each contains \(\binom43=4\) triples, and a triple cannot lie on two distinct lines, \(|\mathcal B|=286-52=234\). Every point lies in \(\binom{12}{2}-4\binom32=54\) bases. Every pair lies in \(11-2=9\) bases.

For any \(S\subseteq E\), expand the character as \(\prod_{p\in B}(1-2\mathbf1_{p\in S})\) and sum over bases. Writing \(k=|S|\) and \(b(S)=|\{B\in\mathcal B:B\subseteq S\}|\), this gives the identity

\[
\lambda(S)=234-108k+36\binom{k}{2}-8b(S).
\tag{1}
\]

If \(t(S)\) denotes the number of collinear point triples in \(S\), then \(b(S)=\binom{k}{3}-t(S)\), and

\[
\lambda(S)=234-108k+36\binom{k}{2}-8\binom{k}{3}+8t(S),\quad
t(S)=\sum_{\text{lines }L}\binom{|S\cap L|}{3}.
\tag{2}
\]

Thus \(\lambda(S)\equiv234\equiv2\pmod4\) for all \(S\); no Fourier zero is possible. Because every basis has three points, \(\lambda(E\setminus S)=-\lambda(S)\). It remains to classify the possible values and multiplicities. The exact enumeration of the thirteen-point incidence geometry gives, for \(0\le k\le6\), the following complete \((t(S):\text{number of sets})\) counts:

| \(k\) | Collinear-triple-count distribution |
|--:|:--|
| 0 | \(0:1\) |
| 1 | \(0:13\) |
| 2 | \(0:78\) |
| 3 | \(0:234,\ 1:52\) |
| 4 | \(0:234,\ 1:468,\ 4:13\) |
| 5 | \(1:468,\ 2:702,\ 4:117\) |
| 6 | \(2:78,\ 3:936,\ 4:234,\ 5:468\) |

This table is certified **exhaustively** by the attached `verify.py`: it generates the thirteen points from nonzero ternary triples up to scalar multiplication, generates all thirteen lines by dot-product equations, checks the unique-line-through-two-points property, and checks every one of the \(8192\) point subsets. This is a finite exhaustive proof of the table, not an extrapolation. Substituting these values into (2), and using the complement sign relation for \(k\ge7\), yields all sixteen signed levels and multiplicities in the Finding section.

For sharpness of the minimum, sort projective point representatives lexicographically as

```
(0,0,1), (0,1,0), (0,1,1), (0,1,2),
(1,0,0), (1,0,1), (1,0,2), (1,1,0),
(1,1,1), (1,1,2), (1,2,0), (1,2,1), (1,2,2).
```

Take the six points at zero-based indices \(0,1,3,4,5,7\). They contain exactly four collinear triples, so (2) gives \(\lambda(S)=-2\), attaining the lower bound. The trivial character has multiplier \(234\), attaining the maximum absolute value, since every multiplier is a signed sum of 234 unit terms. The Walsh characters form an orthogonal eigenbasis; hence the stated operator norms and condition number follow. Finally, each of the 8192 eigenvalues has exact two-adic valuation one, so the determinant has two-adic valuation 8192.

## Verification

Run `python3 verify.py` with Python 3 standard library. It constructs the basis indicator independently using determinants of every three representative vectors over \(\mathbb F_3\), then computes the entire Walsh transform by exact integer fast Walsh-Hadamard transform. Separately it derives each coefficient from line intersections and the order-three Krawtchouk polynomial. It compares all 8192 entries, the full signed histogram, refined frequency-weight shells, the explicit minimum witness, the modulo-four law, complement symmetry and Parseval. The observed output is provided in `verification_output.txt`. The finite proof depends only on the explicit incidence construction and bounded loops present in the checker; no prior sample, external database, random seed or numerical tolerance is involved.

## Relationship to prior work

The thirteen-point plane and its \(234\) bases are classical. Brändén and González D'León (2009 initial public preprint, 2010 revision) explicitly discuss this matroid and its basis polynomial, proving an analytic weak-half-plane-property obstruction, **not** its evaluations at Boolean sign vectors. Havlicek (2013) uses the same projective plane in the construction of the Witt design, but addresses quadratic configurations rather than Walsh multipliers. A published theorem on complementary bases of Steiner **triple** systems supplies a general dyadic nonvanishing criterion; this projective plane instead has thirteen **four-point lines**, so its 234 rank-three bases and full multiplicity table are not special cases. A separate published theorem for **binary** projective geometries concerns \(\mathrm{PG}(r-1,2)\), not \(\mathrm{PG}(2,3)\). The distinctive result here is the full sixteen-level signed spectrum and sharp recovery constant for the ternary plane, beyond the elementary nonvanishing congruence.

## Limitations

The complete histogram is a finite exact certificate for \(\mathrm{PG}(2,3)\) only. It is not a dimension-uniform spectral classification of projective matroids or a theorem for arbitrary designs. The two-adic nonvanishing follows from elementary degree parity; the sharper multiplicity distribution uses a complete finite incidence census. Historical-priority checks are bounded, and an unindexed earlier equivalent spectrum remains possible. No independent audit has been performed.

## References

1. P. Brändén and R. S. González D'León, *On the half-plane property and the Tutte group of a matroid*, arXiv:0906.1071v1, first publicly posted 2009-06-05, https://arxiv.org/abs/0906.1071 .
2. H. Havlicek, *A Model of the Witt Design W12 based on Quadrics of PG(2,3)*, arXiv:1304.0089v1, first publicly posted 2013-03-30, https://arxiv.org/abs/1304.0089 .
3. N. Gill, N. I. Gillespie, J. Semeraro and C. E. Praeger, *Conway's groupoid and its relatives*, arXiv:1604.04429v1, first publicly posted 2016-04-15, https://arxiv.org/abs/1604.04429 .
4. *Uniform dyadic nonvanishing for the Walsh transform of Steiner matroid bases*, publicly available mathematical result, 2026-11-16, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-uniform-dyadic-nonvanishing-for-the-walsh-transform-of-steiner-m--1a9938b7ebb8 .
5. *Sharp dyadic Fourier divisibility and the first singular rank of binary projective matroid bases*, publicly available mathematical result, 2026-11-16, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-sharp-dyadic-fourier-divisibility-and-the-first-singular-rank-of--417690500a98 .
