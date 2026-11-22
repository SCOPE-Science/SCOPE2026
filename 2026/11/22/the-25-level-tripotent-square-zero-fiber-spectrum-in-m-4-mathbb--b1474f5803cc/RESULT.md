# The 25-level tripotent–square-zero fiber spectrum in \(M_4(\mathbb F_2)\)

## Finding

Let \(V=M_4(\mathbb F_2)\), and for every \(A\in V\) define the **decomposition fiber**
\[
 r(A)=\#\{(T,N)\in V^2:T+N=A,\ T^3=T,\ N^2=0\}.
\]
The summands are ordered by their distinct roles and are **not** required to commute. The complete fiber spectrum consists of exactly 25 positive levels. The following table gives the number of *labelled matrices* \(A\) attaining each level:

| \(r(A)\) | Matrices | \(r(A)\) | Matrices | \(r(A)\) | Matrices |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 3 | 1,120 | 5 | 1,344 |
| 7 | 5,760 | 12 | 1,260 | 15 | 2,808 |
| 16 | 2,520 | 21 | 9,120 | 22 | 6,720 |
| 25 | 5,040 | 27 | 6,720 | 28 | 2,730 |
| 30 | 8,512 | 31 | 2,520 | 32 | 1,260 |
| 33 | 105 | 42 | 1,680 | 44 | 105 |
| 48 | 1,120 | 50 | 1,680 | 58 | 2,520 |
| 65 | 210 | 70 | 560 | 162 | 120 |
| 316 | 1 | | | | |

The sharp extremal descriptions are:

* \(r(A)=1\) holds precisely for \(A=0\).
* For \(A\ne0\), one has \(r(A)\ge3\), with equality precisely when \(A\) is similar to \(0_2\oplus C(x^2+x+1)\); this is one similarity class of 1,120 matrices.
* \(r(A)\le316\), with equality precisely for \(A=I_4\).
* For \(A\ne I_4\), one has \(r(A)\le162\), with equality precisely when \(A\) is similar to \(0_1\oplus I_3\), a class of 120 rank-three idempotents.

The complete 34-similarity-class refinement, including a representative and each class size, is in `class_table.csv`. No order above four or field other than \(\mathbb F_2\) is asserted.

## Assumptions and scope

All arithmetic is over the field \(\mathbb F_2\). Matrix addition is bitwise XOR in the specified row-major encoding; multiplication is ordinary matrix multiplication over the field, not Boolean-semiring multiplication. The restrictions \(T^3=T\) and \(N^2=0\) impose no commutativity relation. The result is an exhaustive finite theorem on all \(2^{16}=65,536\) matrices of order four; no asymptotic or unbounded-dimension inference is made.

## Proof

**1. Reducing fibers to a convolution.** Define \(\mathcal T=\{T:T^3=T\}\) and \(\mathcal N=\{N:N^2=0\}\). Since the characteristic is two, each admissible \(N\) determines a unique potential first summand \(T=A+N\). Consequently
\[
 r(A)=\sum_{N\in\mathcal N}\mathbf1_{\mathcal T}(A+N)
 =\sum_{T,N\in V}\mathbf1_{\mathcal T}(T)\mathbf1_{\mathcal N}(N)\mathbf1_{A=T+N}.
\]
Conjugation by an invertible matrix bijects fibers, so \(r\) is constant on similarity classes.

**2. Structural total-count checks.** A square-zero matrix of rank \(j\) has \(j\)-space image included in an \((n-j)\)-space kernel, and the induced map from the quotient by its kernel to its image is invertible. Thus, writing \({n\brack j}_2\) for the Gaussian binomial coefficient,
\[
 |\mathcal N_n|=\sum_{j=0}^{\lfloor n/2\rfloor}{n\brack j}_2{n-j\brack j}_2|\mathrm{GL}_j(2)|.
\]
In dimension four the rank contributions are respectively \(1,105,210\), giving \(|\mathcal N|=316\). Tripotency in characteristic two is the identity \(T(T+I)^2=0\). The primary decomposition has a zero-eigenspace on which \(T=0\) and a complementary generalized-one-eigenspace on which \(T=I+Q\) with \(Q^2=0\). The two complementary invariant subspaces have distinct primary types. Hence
\[
 |\mathcal T|=\sum_{k=0}^{4}{4\brack k}_2 2^{k(4-k)}|\mathcal N_{4-k}|=5317.
\]
As a check, \(\sum_{A\in V}r(A)=5317\cdot316=1,680,172\).

**Elementary endpoint identities.** In the zero fiber, one must have \(T=N\), but \(N^2=0\) forces \(T^3=0\), hence \(T=N=0\) and \(r(0)=1\). In the identity fiber, every square-zero \(N\) gives \((I_4+N)^2=I_4\) and thus a tripotent \(T=I_4+N\); consequently \(r(I_4)=316\) without relying on the exhaustive table.

**3. Exhaustive class and arithmetic certificate.** Primary rational canonical form indexes similarity types of \(V\) by collections of partitions \(\lambda_f\), one for each monic irreducible \(f\in\mathbb F_2[x]\), such that \(\sum_f(\deg f)|\lambda_f|=4\). There are exactly 34 types. A representative is a block diagonal sum of companion matrices \(C(f^j)\) over all parts \(j\) of all partitions. If \(d=\deg f\), \(m_j\) is the multiplicity of the part \(j\), and \(\lambda_f'\) is its conjugate partition, the order of its invertible module centralizer is
\[
 c_f=2^{d\sum_i(\lambda_{f,i}')^2}\prod_{j\ge1}\prod_{s=1}^{m_j}(1-2^{-ds}).
\]
Indeed the endomorphism ring has dimension \(d\sum_i(\lambda_{f,i}')^2\) and its semisimple quotient is a product of \(M_{m_j}(\mathbb F_{2^d})\); counting units gives the displayed formula. The full similarity-class size is \(|\mathrm{GL}_4(2)|/\prod_f c_f\). The program enumerates the 34 types, and their class sizes sum to \(65,536\), so no similarity class is omitted.

For each representative the program tests the polynomial identity \((A+N)^3=A+N\) for **each** of the 316 square-zero \(N\). These 34 exact finite sums and the class-size formula produce the displayed 25-level weighted histogram and the stated unique extremal classes. This is an exhaustive finite computation, not statistical sampling.

**4. Independently exhaustive global identity.** The same program also enumerates all \(65,536\) matrices for \(\mathcal T\) and \(\mathcal N\) and adds one to the output bin indexed by \(T+N\) for every one of the \(1,680,172\) admissible ordered pairs. Separately, it evaluates the convolution via the 16-bit Walsh transform
\[
 r(A)=2^{-16}\sum_{u\in\mathbb F_2^{16}}(-1)^{u\cdot A}\widehat{\mathbf1_{\mathcal T}}(u)\widehat{\mathbf1_{\mathcal N}}(u),
\]
which follows from character orthogonality. The direct-pair, Walsh and class-weighted answers agree **entry by entry or by weighted histogram as appropriate**. Thus the numerical table and uniqueness of each extremal class follow from exact exhaustive operations on explicitly specified finite sets.

## Verification

Run `python3 verify.py class_table.csv` with Python 3 and no third-party packages from the directory containing the files. The program verifies both total-count identities, direct-pair enumeration against a separate integral Walsh-convolution calculation, the 34 primary elementary-divisor classes and their exhaustive sizes, and agreement of weighted canonical fiber counts with the full histogram. It prints `TRIPOTENT_SQUAREZERO_FIBERS_OK 34 65536 25`. It then writes the class table as UTF-8 CSV. The exact CSV distributed with this result is generated by this command; all integer arithmetic is exact.

## Relationship to prior work

Danchev, García and Gómez Lozano (arXiv:2604.15286v1, first public 2026-04-16) established general characteristic-two decompositions using fourth potency over \(\mathbb F_2\), motivating sharper fixed-potency questions. Their earlier work (arXiv:2102.10460) concerns existence of potent-plus-square-zero decompositions, not fiber multiplicity. Phuc and Danchev (arXiv:2611.24594v1, submitted 2026-11-18) subsequently proved the **qualitative** statement that all order-four binary matrices admit a tripotent-plus-square-zero decomposition; this strengthens background existence, but does not give the 25-level pointwise fiber census or sharp unique extrema. The later paper is a comparison source, not the first public motivating source for the present fixed-potency counting question. The present result relies on no unproved assertion from any of these papers.

## Limitations

The theorem is a complete **finite** census only in order four over \(\mathbb F_2\). Exhaustive computation is justified by explicit finite-domain coverage and a reproducible exact checker; it does not supply a dimension-uniform formula. The historical-priority comparison includes accessible published results and indexed mathematical records; specialist unpublished or unindexed enumerations may still exist. Independent mathematical validation has not been performed.

## References

1. P. Danchev, E. García, M. Gómez Lozano, *Matrices over finite fields of characteristic 2 as sums of diagonalizable and square-zero matrices*, arXiv:2604.15286v1 (submitted 2026-04-16), https://arxiv.org/abs/2604.15286.
2. D. V. Phuc, P. V. Danchev, *A cubic obstruction to sums of tripotent and square-zero matrices*, arXiv:2611.24594v1 (submitted 2026-11-18), https://arxiv.org/abs/2611.24594.
3. P. Danchev, E. García, M. Gómez Lozano, *Decompositions of matrices into potent and square-zero matrices*, arXiv:2102.10460v1 (submitted 2021-02-20), https://arxiv.org/abs/2102.10460.
