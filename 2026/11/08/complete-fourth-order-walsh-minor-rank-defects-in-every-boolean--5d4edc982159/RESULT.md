# Complete fourth-order Walsh minor rank defects in every Boolean dimension

## Finding

Let \(d\ge3\), \(V=\mathbb F_2^d\), and \(N=2^d\). Write the unnormalized Walsh character matrix as
\[
H=( (-1)^{a\cdot b})_{a,b\in V}.
\]
For each four-element row set \(A\subset V\) and four-element column set \(B\subset V\), let \(H[A,B]\) be their \(4\times4\) complex (equivalently real) submatrix. Its rank is one of \(1,2,3,4\), and its determinant has absolute value either \(0\), \(8\), or \(16\).

There are exactly two affine classes of four-point row sets: **planes**, for which \(\sum_{a\in A}a=0\), and **tetrahedra**, for which \(\sum_{a\in A}a\ne0\). Their respective numbers are
\[
P=\frac{N(N-1)(N-2)}{24},\qquad
T=\frac{N(N-1)(N-2)(N-4)}{24}.
\]

The following table is the **exact number of column sets \(B\) for each fixed row set \(A\)**. The columns of the table label the rank of \(H[A,B]\); the last column separates the two possible nonzero absolute determinant values.

| Row type | Rank 1 | Rank 2 | Rank 3 | Rank 4, \(\lvert\det\rvert=8\) | Rank 4, \(\lvert\det\rvert=16\) |
|---|---:|---:|---:|---:|---:|
| Plane | \(\frac{N(N-12)(N-8)(N-4)}{1536}\) | \(\frac{N^2(N-4)(7N-44)}{512}\) | \(\frac{3N^3(N-4)}{128}\) | \(0\) | \(\frac{N^4}{256}\) |
| Tetrahedron | \(\frac{N(N-24)(N-16)(N-8)}{12288}\) | \(\frac{7N^2(N-8)(7N-88)}{12288}\) | \(\frac{3N^3(N-7)}{128}\) | \(\frac{7N^4}{512}\) | \(\frac{N^4}{2048}\) |

Every entry is a nonnegative integer for the stated dimensions. Each row sums to \(\binom N4\). If \(p_r(N)\) and \(t_r(N)\) denote the respective row entries aggregated by rank, **the number of ordered pairs \((A,B)\) of any prescribed rank \(r\)** is exactly
\[
\mathcal R_r(N)=Pp_r(N)+Tt_r(N),\qquad r=1,2,3,4.
\]
In particular, the rank-two and rank-three singular cases remain distinguished, rather than being aggregated into a single zero-minor count. The number of maximal-determinant minors is \(PN^4/256+TN^4/2048\), while \(7TN^4/512\) have determinant magnitude \(8\).

For \(N=16\), the **global** rank frequencies are \(560,104160,1612800,1594880\), in ranks \(1,2,3,4\) respectively. The singular total is \(1717520\), matching the earlier numerical Hadamard-minor table for this specific matrix. For \(N=8\), the rank frequencies are \(0,84,1344,3472\) among \(4900\) ordered pairs.

If a row set and a column set are chosen independently and uniformly among all four-point subsets, then as \(d\to\infty\), the probabilities of ranks \(1,2,3,4\) converge respectively to
\[
\frac1{512},\qquad\frac{49}{512},\qquad\frac{288}{512},\qquad\frac{174}{512}.
\]
Thus the limiting nonsingularity probability is exactly \(87/256\), and the limiting probability of a rank defect is \(169/256\). This is the real-rank distribution of a uniformly random \(3\times3\) zero-one matrix.

## Assumptions and scope

All vector-space operations in the labels \(a,b\) are over \(\mathbb F_2\), but matrix rank and determinant of \(H[A,B]\) are over \(\mathbb R\) or \(\mathbb C\), not over \(\mathbb F_2\). Subsets are unordered, and \((A,B)\) is an ordered row/column pair. There is no normalization of the character matrix. Every formula applies for all integer dimensions \(d\ge3\); no assertion about arbitrary, non-Sylvester Hadamard matrices is made.

## Proof

**Affine row classification.** Translate a four-point row set to \(\{0,a_1,a_2,a_3\}\). Distinctness makes the three nonzero differences distinct. They span dimension two precisely when \(a_3=a_1+a_2\), and otherwise span dimension three. The affine group acts transitively on each of the two types. The plane count is the number of two-dimensional subspaces times their cosets, namely
\[
\frac{(N-1)(N-2)}6\,\frac N4=P;
\]
subtracting this from \(\binom N4\) gives \(T\).

**Reduction to three-bit incidence.** After independently multiplying rows and columns of \(H[A,B]\) by signs, both its first row and its first column consist of ones. Subtract the first row from the other three rows. The lower-right block becomes \(-2M\), where
\[
M_{ij}=a_i\cdot(b_j-b_0)\pmod 2\in\{0,1\},\qquad1\le i,j\le3.
\]
Consequently,
\[
\operatorname{rank}_{\mathbb R}H[A,B]=1+\operatorname{rank}_{\mathbb R}M,
\qquad|\det H[A,B]|=8|\det M|.
\]
This is an exact real-rank identity. For a plane normalize \((a_1,a_2,a_3)=(e_1,e_2,e_1+e_2)\); for a tetrahedron normalize to \((e_1,e_2,e_3)\).

**Counting all projected column triples.** Put \(r=2\) for a plane and \(r=3\) for a tetrahedron, and \(h=N/2^r\). Every projection of a column into \(\mathbb F_2^r\) has exactly \(h\) preimages. Fix an ordered base point \(b_0\) and let \((v_1,v_2,v_3)\in(\mathbb F_2^r)^3\) be the projections of \(b_j-b_0\). If \(k_v\) is the number of occurrences of \(v\) in the projected triple, the number of lifts to distinct \(b_1,b_2,b_3\), different from \(b_0\), equals
\[
w(v_1,v_2,v_3)=\prod_{v\in\mathbb F_2^r}
 (h-\mathbf1_{\{v=0\}})_{k_v},
\]
where \((z)_k=z(z-1)\cdots(z-k+1)\), and \((z)_0=1\). All four-point column sets are counted \(24\) times by the ordered choice of their four elements; the base point has \(N\) choices. Hence the count of any fixed rank/determinant class equals
\[
\frac N{24}\sum_{(v_1,v_2,v_3)\in(\mathbb F_2^r)^3}
 w(v_1,v_2,v_3)\,\mathbf1_{\{\text{class of the projected }3\times3\text{ matrix}\}}.
\]
This formula alone is a finite, closed, reproducible expression for each entry of the theorem.

**The finite exact evaluation.** For plane rows, each projected column \((u,v)\) gives the column \((u,v,u\mathbin{\mathrm{xor}}v)\), while for tetrahedral rows a projected column is its own three-bit vector. Evaluate the \(4^3=64\) and \(8^3=512\) ordered projected triples, classifying real rank by determinants of all minors. The resulting weighted polynomials in \(h\), separated by \((\text{rank},|\det H|)\), are:

| Type | Rank 1 | Rank 2 | Rank 3 | Rank 4, magnitude 8 | Rank 4, magnitude 16 |
|---|---:|---:|---:|---:|---:|
| Plane | \((h-1)(h-2)(h-3)\) | \(3h(h-1)(7h-11)\) | \(36h^2(h-1)\) | \(0\) | \(6h^3\) |
| Tetrahedron | \((h-1)(h-2)(h-3)\) | \(7h(h-1)(7h-11)\) | \(36h^2(8h-7)\) | \(168h^3\) | \(6h^3\) |

The small finite enumeration is not a numerical extrapolation: the indicated sum has precisely \(64\) or \(512\) terms, each term is an exact integer polynomial of degree at most three, and its rank is decided by integer minors. The attached dependency-free `verify_walsh.py` recomputes every term using exact arithmetic, verifies the polynomial identities at six distinct values of \(h\) (four already suffice to prove equality of cubic polynomials), and separately checks physical Walsh submatrices. Substituting \(h=N/2^r\) and multiplying by \(N/24\) gives the first table.

**Asymptotic distribution.** Tetrahedral sets have asymptotic proportion one among all four-point row sets. As \(N\to\infty\), independently sampled column projections become uniformly distributed among the \(512\) three-bit triples. Exactly \(1,49,288,174\) of these give real ranks \(0,1,2,3\), respectively, for the normalized incidence block, so the limiting rank distribution is as stated.

## Verification

Run `python3 verify_walsh.py` using Python 3 and only its standard library. The checker exhausts the \(64\) and \(512\) projection triples and independently verifies all formulas for \(h=1,\ldots,6\). It then enumerates all column four-sets for one representative of each affine row type in Boolean dimensions three, four, and five, testing exact rank and determinant. In dimensions three and four it also verifies rank and determinant from the original \(4\times4\) Walsh matrix by a separate direct integer-minor routine. It checks the Cauchy–Binet second-moment identity and the previously tabulated \(N=16\) singular count. The actual execution concluded `ALL_FOURTH_WALSH_MINOR_CHECKS_OK`.

## Relationship to prior work

Brent and Osborn, *Bounds on minors of binary matrices* (arXiv:1208.3330), prove a universal squared-minor moment identity for Hadamard matrices and formulae for zero minors of orders two and three. Their subsequent *On minors of maximal determinant matrices* (arXiv:1208.3819) tabulates the order-16 Sylvester-related zero count \(1717520\), but does not provide this all-dimensional affine-type rank-defect census. Earlier four-point Walsh orthogonal-spectrum results determine maximal-determinant submatrices, not the rank-one, rank-two and rank-three defect frequencies. Accordingly this result does not claim priority for the order-16 zero count, the general moment identity, or existing orthogonal-basis enumerations.

## Limitations

Only fourth-order minors of the additive-character matrix of \(\mathbb F_2^d\) are classified. It is not a theorem about arbitrary Hadamard matrices of order \(2^d\), complex Fourier matrices of odd order, higher-order minors, or a universal determinant-rank law for all \(\{\pm1\}\)-matrices. Published literature may contain an equivalent all-dimensional rank-refined census under different language; the historical originality comparison is bounded. No independent mathematical audit has been performed.

## References

1. R. P. Brent and J.-A. H. Osborn, *Bounds on minors of binary matrices*, arXiv:1208.3330, first public version 2012-08-16; §§2–3.
2. R. P. Brent and J.-A. H. Osborn, *On minors of maximal determinant matrices*, arXiv:1208.3819, first public version 2012-08-19; §§1–4 and order-16 tables.
3. Y. Li, J. Zi, Y. Liu, X. Zhang, *A note of values of minors for Hadamard matrices*, arXiv:1905.04662 (2019); accessible abstract describes near-full-size minor values, not a fixed fourth-order rank census.
