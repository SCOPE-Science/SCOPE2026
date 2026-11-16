# Exact Walsh cancellation and sharp range-projection norm for the \(4\times4\) domino square

## Finding

Let \(G=P_4\square P_4\) have one vertex per cell of a four-by-four square and one edge per pair of orthogonally adjacent cells. Regard each of the 36 perfect matchings (domino tilings) as a vector in \(\mathbb F_2^{24}\). For counting convolution by their indicator, the 16,777,216 *unnormalized* Walsh multipliers have the complete distribution

| Absolute multiplier \(a\) | Number of characters with \(|W|=a\) |
|---:|---:|
| 0 | 7,634,944 |
| 4 | 5,799,936 |
| 8 | 2,359,296 |
| 12 | 393,216 |
| 16 | 196,608 |
| 20 | 65,536 |
| 24 | 262,144 |
| 32 | 32,768 |
| 36 | 32,768 |

For each \(a>0\), precisely half the stated multiplicity occurs at \(+a\), and half at \(-a\). Thus the convolution rank is \(9,142,272\), its smallest nonzero multiplier magnitude is \(4\), its Moore--Penrose inverse-on-range norm is \(1/4\), and the ratio of largest to smallest positive singular values is \(9\).

Exactly eight Walsh characters of Hamming weight one vanish: those corresponding to the eight edges incident to corners. Their counts split \(18\) matching incidences to \(18\) exclusions. Every other single-edge character has nonzero multiplier. The orthogonal Fourier range projection \(P\) satisfies the *sharp* endpoint identity
\[
\|P\|_{\ell^1\to\ell^1}=\|P\|_{\ell^\infty\to\ell^\infty}=\frac{1849}{256}.
\]

## Assumptions and scope

The 16 grid vertices are \(v_{r,c}=4r+c\), \(0\le r,c<4\). The edge ordering examines each vertex in increasing \(v\), listing its right edge (when present), followed by its downward edge (when present). There are 24 such edges. The ambient group \(H=(\mathbb F_2)^{E(G)}\) is additive, and for \(s\in H\), the Walsh character is \(\chi_s(x)=(-1)^{\sum_e s_ex_e}\). The convolution is \((Tf)(x)=\sum_{M\text{ perfect matching}} f(x+\mathbf1_M)\) with no normalization. All claimed operator norms use counting measure, not probability measure, on \(H\). No assertion is made for larger squares or arbitrary planar graphs.

## Proof

**Cut-space reduction.** For every vertex \(v\), let \(b_v\) be the incidence vector of its edge star. Every perfect matching meets each vertex exactly once, so \(W(s+b_v)=-W(s)\), where \(W(s)=\sum_M\chi_s(\mathbf1_M)\). The star vectors span the cut space \(B\) of the connected grid, of dimension \(15\): the only relation is the sum of all 16 stars. Consequently each gauge class modulo \(B\) has \(2^{15}\) elements, evenly split between \(+W\) and \(-W\) when \(W\ne0\).

Run Kruskal's spanning-tree algorithm on the stated edge order. Its nine non-tree edges have indices \((7,9,11,14,16,18,21,22,23)\), in zero-based indexing. Any edge-frequency vector is gauge-equivalent to exactly one vector supported on these chords. For chord sign vector \(z\in\mathbb F_2^9\), define the signed dimer sum
\[
F(z)=\sum_{M\text{ perfect matching}}(-1)^{\sum_{j=0}^{8} z_j\mathbf1_{\{e_j\in M\}}}.
\]
The full 24-dimensional Walsh spectrum is therefore reconstructed from only 512 integer values \(F(z)\).

**Exact finite evaluation.** Enumerating matchings by the least-uncovered-vertex recursion gives 36 different tilings. Project each tiling to its nine chord incidences, place a 1 at each of the resulting 36 distinct binary words in a 512-vector, and apply the length-512 unnormalized Walsh--Hadamard transform. This yields the following exhaustive absolute-value histogram:

| \(|F(z)|\) | 0 | 4 | 8 | 12 | 16 | 20 | 24 | 32 | 36 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplicity | 233 | 177 | 72 | 12 | 6 | 2 | 8 | 1 | 1 |

The recurrence and all loops are reproduced in `check_walsh.py`. As an independent computation, `check_kasteleyn.py` builds an \(8\times8\) bipartite Kasteleyn matrix, with a minus sign on vertical edges of even zero-based columns and the additional nine chord signs. Exact integer Bareiss determinants at all 512 sign vectors reproduce the same histogram. The signing makes every determinant matching term have one common sign, so \(|\det K(z)|=|F(z)|\); the implemented signs are normalized using the all-positive frequency, whose absolute value is 36. This is the classical weighted dimer determinant mechanism, used here as a separate finite checker, not a claimed new determinant identity.

**One-edge cancellation and spectral gap.** The exhaustive recursion gives edge-inclusion counts \(6\), \(12\), \(18\), each for exactly eight edges. The count \(18\) occurs exactly on corner-incident edges. Hence the eight weight-one characters there have \(W=36-2\cdot18=0\). For every other edge the coefficient is nonzero. The 512-value histogram has least positive magnitude four and greatest magnitude 36; the gauge reduction preserves magnitudes. Fourier diagonalization of convolution therefore gives the asserted rank, pseudoinverse norm, and condition ratio.

**Sharp endpoint projection.** Write \(h(z)=\mathbf1_{\{F(z)\ne0\}}\). This is the Fourier multiplier of the range projection on the 512-class quotient. The inverse-transform kernel of the full projection vanishes outside the nine-dimensional cycle space \(B^\perp\), because its multiplier is constant on cut-space cosets. Restriction of a cycle vector to the nine chord coordinates is a bijection to \(\mathbb F_2^9\). Writing \(Q(t)=\sum_z h(z)(-1)^{z\cdot t}\), the sum of absolute values of the full projection kernel is exactly
\[
\frac1{512}\sum_{t\in\mathbb F_2^9}|Q(t)|.
\]
The second exact length-512 transform gives \(\sum_t|Q(t)|=3698\); hence the norm is \(3698/512=1849/256\). Convolution's \(\ell^1\) and \(\ell^\infty\) norms equal the \(\ell^1\) norm of its kernel by the triangle inequality and an attaining point-mass or signs choice, respectively. This proves sharpness, not merely an upper bound.

## Verification

`check_walsh.py` and `check_kasteleyn.py` are self-contained Python 3 programs using only standard-library exact integers; run `python3 check_walsh.py` and `python3 check_kasteleyn.py`. The former lists all perfect matchings recursively and performs two integer Walsh transforms; the latter computes all 512 determinants via fraction-free elimination and independently repeats the endpoint calculation. Both check Parseval's identity \(\sum_z F(z)^2=512\cdot36\). The file `CERTIFICATE.json` records the chord set, all 36 chord codes, and both exact histograms so that claimed numbers can be checked without trusting a log. All operations are finite with explicit bounds; neither script relies on floating-point approximation or sampling.

## Relationship to prior work

Kasteleyn's classical dimer method, as explained in Richard Kenyon's *An introduction to the dimer model* (arXiv:math/0310326, sections 2.1 and 2.4), establishes signed determinant evaluations and local dimer statistics, rather than the *evaluated* full 512-gauge-class Walsh zero census or its endpoint Fourier projection norm. Cohn--Kenyon--Propp (arXiv:math/0008220) study variational/asymptotic tiling measures. A detailed four-by-four illustration of the 36 tilings and Kasteleyn signs appears in *Signs that make a determinant count*; that article does not furnish the reported Walsh distribution or projection norm. The standard determinant formulas imply each individual multiplier is computable but do not by themselves state the computed exact distribution.

## Limitations

This is an exact finite classification for the open \(4\times4\) square grid, not a general classification of all rectangular grids or toroidal boundary conditions. The numerical table is established by fully bounded exact enumeration plus two independent evaluation algorithms; it is not a conceptual closed-form expression for arbitrary size. The computations and same-model consistency review are not an independent external mathematical audit. A differently indexed historical signed-partition-function table might contain the same finite numbers; priority is supported only by the specified bounded comparisons.

## References

- R. Kenyon, *An introduction to the dimer model*, arXiv:math/0310326 (first public 2003-10-20), https://arxiv.org/abs/math/0310326.
- H. Cohn, R. Kenyon, and J. Propp, *A variational principle for domino tilings*, arXiv:math/0008220 (first public 2000-08-30), https://arxiv.org/abs/math/0008220.
- *Signs that make a determinant count*, detailed 4-by-4 tiling and determinant illustration, https://www.matpic.com/essays/signs-that-make-a-determinant-count/.
