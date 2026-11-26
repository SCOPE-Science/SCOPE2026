# Exact rank and determinant spectra of four-point Walsh Fourier minors

## Finding
Let \(d\ge3\) be an integer, \(G=\mathbb F_2^d\), and \(N=2^d\). Form the unnormalized Walsh Fourier matrix
\[
H=( (-1)^{a\cdot b})_{a,b\in G}.
\]
For unordered four-point sets \(A,B\subseteq G\), let \(H[A,B]\) denote the corresponding \(4\times4\) submatrix. The only possible absolute determinants are \(0\), \(8\), and \(16\). Among all \(\binom N4^2\) ordered pairs \((A,B)\), their exact multiplicities are
\[
\begin{aligned}
D_{16}(N)&=\frac{N^5(N-1)(N-2)(N+4)}{49152},\\
D_{8}(N)&=\frac{7N^5(N-1)(N-2)(N-4)}{12288},\\
D_{0}(N)&=\binom N4^2-D_8(N)-D_{16}(N).
\end{aligned}
\]
Moreover the real-rank multiplicities, for ranks \(1,2,3,4\), are respectively
\[
\begin{aligned}
R_1(N)&=\frac{N^2(N-8)(N-4)(N-2)(N-1)(N^2-32N+288)}{294912},\\
R_2(N)&=\frac{N^3(N-4)(N-2)(N-1)(49N^2-840N+3872)}{294912},\\
R_3(N)&=\frac{N^4(N-6)(N-4)(N-2)(N-1)}{1024},\\
R_4(N)&=\frac{N^5(N-2)(N-1)(29N-108)}{49152}.
\end{aligned}
\]
These are counts of pairs of index sets, not counts of matrices modulo symmetry. In particular, exactly \(D_{16}(N)\) four-point row-column selections form real Hadamard submatrices, since \(|\det H[A,B]|=16\) is the Hadamard equality condition for a \(4\times4\) sign matrix.

There is also a geometric classification of every minor. A four-point row set is either an affine two-plane or affine-independent. For a row plane, project the four column indices to the dual of its two-dimensional difference space: the rank is the number of distinct projections, and determinant magnitude \(16\) occurs precisely when all four projections are distinct. For an affine-independent row set, project the columns to the eight characters of its three-dimensional difference space. If four projections are distinct, then their affine geometry in \(\mathbb F_2^3\) determines the determinant: magnitude \(8\) for an affine-independent projected quadruple, magnitude \(16\) for one of the two parity tetrahedra, and zero for any of the other twelve affine planes. If fewer than four projections are distinct, the rank equals their number.

## Assumptions and scope
All ranks are over \(\mathbb R\) (equivalently \(\mathbb C\)); determinants are those of the unnormalized sign-valued Fourier matrix. Four distinct rows and four distinct columns are selected, but different columns may have the same restriction to the difference space of the selected rows. The group is exactly \(\mathbb F_2^d\), and the proof applies to every integer \(d\ge3\). It does not assert analogous formulas for cyclic \(2\)-power groups, arbitrary Hadamard matrices, or larger minors.

## Proof
**1. Row-set geometry.** Translate the four rows and apply an invertible linear change of coordinates. Multiplication of columns by signs, permutation of columns, and corresponding dual-coordinate changes preserve ranks and determinant magnitudes. Thus a four-element row set is equivalent to either \(\{0,e_1,e_2,e_1+e_2\}\), an affine plane, or \(\{0,e_1,e_2,e_3\}\), an affine-independent quadruple. The number of affine two-planes is
\[
P=\frac N4\,\frac{(N-1)(N-2)}{6}=\frac{N(N-1)(N-2)}{24},
\]
while the number of affine-independent row quadruples is \(I=\binom N4-P=P(N-4)\).

**2. Local plane model.** For the first row type, the restriction of a column is one of four pairwise orthogonal columns of the order-four Walsh matrix. Every restricted character has \(m_2=N/4\) distinct extensions to \(G\). Consequently the rank equals the number of distinct restricted characters. A nonzero determinant requires one column from each restriction class, giving \(m_2^4\) column sets, all with determinant magnitude \(16\).

**3. Local cube model.** For the second row type, the restricted column vectors are
\[
v(t)=(1,(-1)^{t_1},(-1)^{t_2},(-1)^{t_3})^\mathsf T,
\qquad t\in\mathbb F_2^3,
\]
and each type has \(m_3=N/8\) extensions. Any one, two, or three distinct cube vertices give linearly independent vectors over \(\mathbb R\). If four projected vertices are distinct, translate the projected set so it contains \(0\), normalize signs, and subtract the first row and column. The absolute determinant becomes \(8\) times the absolute determinant of the \(3\times3\) binary matrix whose columns are the three nonzero translated vertices.

Of the \(\binom73=35\) unordered triples of distinct nonzero binary vertices, exactly \(28\) are independent over \(\mathbb F_2\), so their integer determinants are odd and have magnitude \(1\). The other seven triples are the seven two-dimensional linear subspaces minus \(0\). Six lie in ordinary real coordinate or coordinate-equality planes and have determinant zero. The remaining triple \(\{(1,1,0),(1,0,1),(0,1,1)\}\) has determinant magnitude \(2\). Each four-vertex subset has four possible anchor vertices, and all eight translates are symmetric. Hence among the \(\binom84=70\) distinct four-type selections, precisely \(56\) have determinant magnitude \(8\), precisely \(2\) have magnitude \(16\), and precisely \(12\) have determinant zero and rank three. In particular, these twelve are the six pairs of cube faces and their six diagonal rectangles, while the two magnitude-\(16\) sets are the two parity tetrahedra. The same classification gives the rank for repeated restriction types.

**4. Determinant counts.** A fixed plane row set has \(m_2^4\) determinant-\(16\) column selections; a fixed independent row set has \(2m_3^4\) determinant-\(16\) selections and \(56m_3^4\) determinant-\(8\) selections. Multiply by \(P\) and \(I\), respectively, and use \(m_2=N/4\), \(m_3=N/8\), and \(I=P(N-4)\). This gives the displayed formulas for \(D_{16},D_8\); the complement gives \(D_0\).

**5. Rank counts.** For \(k\) restriction classes each containing \(m\) original columns, inclusion-exclusion gives the number of four-element column sets meeting exactly \(r\) classes:
\[
U_r(k,m)=\binom kr\sum_{j=0}^r(-1)^j\binom rj\binom{(r-j)m}{4}
\quad(1\le r\le4).
\]
A plane row has rank-\(r\) column count \(U_r(4,m_2)\). An independent row has counts \(U_1(8,m_3)\), \(U_2(8,m_3)\), \(U_3(8,m_3)+12m_3^4\), and \(U_4(8,m_3)-12m_3^4\), respectively: the additional twelve four-type selections are rank three. Therefore
\[
R_r(N)=P U_r(4,N/4)+I\left(U_r(8,N/8)+12(N/8)^4(\mathbf1_{r=3}-\mathbf1_{r=4})\right).
\]
Expanding and factoring these four expressions gives the polynomials in the finding. Each case is exhaustive by the two affine types and the finite cube geometry.

## Verification
The standalone `checker.cpp` enumerates every pair of unordered four-element index sets for \(N=8\) and \(N=16\). Its rank calculation subtracts a normalized first row and uses exact integer determinants and minors of the resulting \(3\times3\) matrix, with no floating-point operations. It verifies the theoretical rank multiplicities, the determinant histograms, and the total \(\binom N4^2\) for both sizes. Run with `c++ -O2 -std=c++17 checker.cpp -o checker && ./checker`.

The resulting data are:

| \(N\) | Rank 1 | Rank 2 | Rank 3 | Rank 4 | \(|\det|=0\) | \(|\det|=8\) | \(|\det|=16\) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 8 | 0 | 84 | 1344 | 3472 | 1428 | 3136 | 336 |
| 16 | 560 | 104160 | 1612800 | 1594880 | 1717520 | 1505280 | 89600 |

An independent consistency check is Cauchy--Binet: for each fixed four-row set, the sum over all four-column sets of squared minor magnitudes must equal \(N^4\), since \(HH^\mathsf T=NI\). The plane formula yields \(256(N/4)^4=N^4\); the independent formula yields \((2\cdot256+56\cdot64)(N/8)^4=N^4\). The finite checks corroborate, but do not replace, the dimension-free geometric counting proof.

## Relationship to prior work
The 2016 work of Huckle and Kravvaritis investigates the spectra of leading principal submatrices of Sylvester Hadamard matrices. Its accessible abstract does not state the arbitrary four-row/four-column incidence counts proved here; the full text was not available for comparison, so this is a residual bibliographic risk. Herr and Wiegand (2019) establish Hadamard-submatrix compatibility tests for **cyclic** Fourier matrices, using primitive sets of integer differences; their results do not yield the rank-\(1\) through rank-\(4\) profile of the **elementary abelian** Walsh character table.

Carlet, Pastor-Díaz, and Tornero (2022) classify balancing behavior and Walsh-support properties of Boolean functions. Their full text treats transforms and supports but does not give determinant magnitudes or partner-incidence counts for arbitrary four-by-four minors. A published result on four-sparse Walsh support geometry gives affine-type restrictions on Fourier-zero patterns with nonzero coefficients; those patterns alone do not provide the determinant spectrum, the rank strata with vanishing coefficients, or the dimension-free multiplicities of all pairs of row-column sets. An earlier exact determinant-bound computation for the order-eight Sylvester matrix records maxima by minor size, not the global formulas for the distribution of individual four-by-four minors in every dimension.

## Limitations
The result concerns fixed minor size four in the elementary abelian binary family only. It does not assert that the same determinant distribution holds for arbitrary Hadamard matrices or nonisomorphic groups of equal order. Independent bibliographic validation has not been performed. An equivalent formulation could exist in older combinatorial-design or Hadamard-submatrix literature, particularly in the inaccessible full text of Huckle and Kravvaritis.

## References
1. T. K. Huckle and C. D. Kravvaritis, *Properties of submatrices of Sylvester Hadamard matrices*, Linear and Multilinear Algebra 65 (2017), 1629--1642, DOI: 10.1080/03081087.2016.1250863; first publicly online 26 October 2016.
2. J. E. Herr and T. M. Wiegand, *Identifying Complex Hadamard Submatrices of the Fourier Matrices via Primitive Sets*, arXiv:1909.13145, first publicly submitted 28 September 2019.
3. C. Carlet, U. Pastor-Díaz, and J. M. Tornero, *On the Walsh and Fourier-Hadamard Supports of Boolean Functions From a Quantum Viewpoint*, arXiv:2205.09222, first publicly submitted 18 May 2022.
4. *Four-sparse Walsh spectra are controlled by affine dimension on \((\mathbb Z/2\mathbb Z)^d\)*, publicly available mathematical result, 4 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-four-sparse-walsh-spectra-are-controlled-by-affine-dimension-on--1491c27461f4 .
5. *Exact hereditary discrepancy and determinant-bound gap for the canonical order-8 Sylvester Hadamard matrix*, publicly available mathematical result, 9 September 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/9/SCOPE037 .
