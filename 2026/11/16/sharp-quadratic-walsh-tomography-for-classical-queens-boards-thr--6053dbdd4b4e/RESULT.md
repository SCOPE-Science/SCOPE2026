# Sharp quadratic Walsh tomography for classical queens boards through order twelve

## Finding
Let \(\mathcal Q_n\) be the set of all configurations of \(n\) mutually nonattacking queens on the ordinary, non-toroidal \(n\times n\) board, represented by their binary square-occupancy arrays. Restrict to \(\mathcal Q_n\) all Walsh characters of support size at most two in the ambient group \((\mathbb Z/2\mathbb Z)^{n^2}\).

**For each integer \(7\le n\le11\), this degree-at-most-two character family spans every real-valued function on \(\mathcal Q_n\), whereas degree at most one does not. For \(n=12\), degree at most two does not span every function.** Equivalently, the complete collection of two-square occupancy marginals determines an arbitrary signed measure, hence an arbitrary probability measure, on \(\mathcal Q_n\) for \(7\le n\le11\); at \(n=12\) two distinct probability laws can have exactly the same two-square marginals.

The exact incidence ranks and solution counts are:

| Board order | Configurations | Two-queen incidence rank over \(\mathbb F_2\) | Conclusion over \(\mathbb R\) |
|---|---:|---:|---|
| \(7\) | 40 | 40 | quadratic interpolation |
| \(8\) | 92 | 92 | quadratic interpolation |
| \(9\) | 352 | 352 | quadratic interpolation |
| \(10\) | 724 | 724 | quadratic interpolation |
| \(11\) | 2680 | 2680 | quadratic interpolation |
| \(12\) | 14200 | not needed | rank at most 8712; nullity at least 5488 |

At order eleven, there are 5280 distinct two-queen patterns that occur in at least one complete configuration, and **none occurs in just one**: every occurring pair extends to at least two solutions. Thus full quadratic tomography is not explained by a single pair uniquely labeling each configuration.

## Assumptions and scope
Rows and columns are indexed by \(\{0,\ldots,n-1\}\). A solution is a permutation \(p\) with distinct values of \(i-p(i)\) and \(i+p(i)\) as \(i\) varies, so diagonal attacks and row or column attacks are all excluded. Rotations and reflections are not quotiented out. Write \(x_{i,a}(p)=1\) when \(p(i)=a\), otherwise zero. For a set \(T\) of board squares, the Walsh character is \(\chi_T(x)=(-1)^{\sum_{e\in T}x_e}\), and its degree is \(|T|\). All ranks of real sampling operators are over \(\mathbb R\); finite certificates use \(\mathbb F_2\) only to prove lower bounds for integer incidence matrices. The theorem is limited to orders seven through twelve.

## Proof
**1. Reduction from Walsh sampling to pair incidences.** Define \(B_n\) to have one row for each \(p\in\mathcal Q_n\) and a column for each ordered row pair \(i<j\) and distinct columns \(a\ne b\), with entry \(x_{i,a}(p)x_{j,b}(p)\). Columns corresponding to diagonal-attacking pairs vanish identically; retaining them is harmless. Every product of two occupancy variables is either one of these columns or zero if the two squares share a row or column. On every configuration, for \(n\ge2\),
\[
 x_{i,a}=\frac1{n-1}\sum_{j\ne i}\sum_b x_{i,a}x_{j,b},\qquad
 1=\frac1{\binom n2}\sum_{i<j}\sum_{a,b}x_{i,a}x_{j,b}.
\]
The apparent same-column terms in these sums vanish. Also \(x_e=(1-\chi_{\{e\}})/2\), and \(x_ex_f=(1-\chi_{\{e\}}-\chi_{\{f\}}+\chi_{\{e,f\}})/4\) when \(e\ne f\). Hence the real column span of \(B_n\) equals the space of restricted Walsh polynomials of degree at most two. Therefore complete two-square marginals determine arbitrary signed measures precisely when \(B_n\) has full row rank.

**2. Finite exact rank witnesses for orders seven through eleven.** The standalone file `verify_pair_rank.py` enumerates every permutation satisfying the two diagonal-distinctness constraints. It encodes each binary incidence row as an integer with exactly \(\binom n2\) set bits. A deterministic high-bit Gaussian elimination over \(\mathbb F_2\) returns, respectively, 40, 92, 352, 724 and 2680 different pivot columns. The full sequence of pivot indices for each board size is in `rank_certificate.json`; it is checked against recomputed rows by `check_certificate.py`. That independent checker generates every configuration by the shifted-diagonal-mask recursion instead of the first program's fixed-diagonal-mask recursion, encodes columns in the opposite within-pair order, and separately obtains the same full ranks by low-bit elimination. Since every \(B_n\) is an integer matrix, an \(N\times N\) minor nonzero modulo two is nonzero over the integers. Thus its real row rank is \(N=|\mathcal Q_n|\). The argument uses exhaustive, finite exact arithmetic, not extrapolation from sampled configurations.

**3. Degree-one minimality.** On every permutation matrix, the row and column sums are one. Consequently constant and coordinate functions span a space of dimension at most \(1+(n-1)^2\). For \(n=7,8,9,10,11\), these bounds are 37, 50, 65, 82 and 101, strictly smaller than the respective numbers of solutions in the table. Thus degree one fails for each of those orders, while degree two succeeds.

**4. Failure at twelve and probability-law nonuniqueness.** The pair-incidence matrix has at most \(\binom{12}{2}\cdot12\cdot11=8712\) columns, but the independent exhaustive enumerations find \(|\mathcal Q_{12}|=14200\). Its real left nullspace therefore has dimension at least 5488. Every left-kernel vector has zero coordinate sum, because summing the pair-incidence entries over the placements of the two queens for any fixed pair of rows gives the all-ones column. Perturbing the strictly positive uniform law by a sufficiently small nonzero kernel vector produces two distinct probability measures with identical pairwise marginals. Degree-two Walsh tomography fails.

**5. No isolating pair at eleven.** The exact frequency census of row-and-column-labelled two-queen partial configurations gives 5280 occurring pairs at order eleven, with every positive completion multiplicity at least two. In particular a pair of observed queen squares never singles out a particular full solution, although the complete linear collection of pairwise observations determines every signed measure.

## Verification
With Python 3 and no third-party packages, run `python3 verify_pair_rank.py` and then `python3 check_certificate.py` from a directory containing the embedded files. The first command writes `rank_certificate.json`; the delivered version is an exact pivot witness. `verify_first.json` and `verify_second.json` record the outputs of both successful executions. The second checker re-enumerates the configurations, verifies stored high-bit pivot witnesses row by row, independently computes all ranks by a distinct low-bit pivot algorithm, and checks the two-queen completion counts for order eleven. Every statement needing a finite computation is covered by one or both paths; the real-rank and probability-law deductions are mathematical arguments above. The two programs were executed against the exact files packaged with this claim.

## Relationship to prior work
The classical queens puzzle, the well-known configuration counts, and backtracking enumeration are not asserted to be new. Chaiken, Hanusa, and Zaslavsky, *A \(q\)-Queens Problem. I. General Theory* (arXiv:1303.1879, initial public version March 8, 2013), and *II. The Square Board* (arXiv:1402.4880, initial public version February 20, 2014), develop enumeration via inside-out polytopes; their counting and quasipolynomial results do not evaluate the rank of the pair-incidence matrix on the classical solution set. The count sequence is OEIS A000170. The finite eight-queens reconfiguration result *Five simultaneous queen changes are necessary and sufficient for eight-queen solution mobility* concerns connectivity under moves and Hamming distances, not linear reconstruction of arbitrary distributions from marginals. A separate study of the unrestricted queens lattice gas addresses fluctuations, not the rank of the full hard-constraint solution marginal operator. These distinctions concern implication of the exact statements, not merely differing titles.

## Limitations
This is an exact finite-window theorem for ordinary boards of sizes seven through twelve, not a general all-order phase transition. No claim is made for boards of order thirteen or larger, the sharp smallest nonzero singular value, noisy recovery conditioning, or higher-degree minimality at order twelve. The positive rank statements rely on the supplied exhaustive integer certificate. Unindexed prior numerical tables or unpublished equivalent incidence-rank calculations may exist; independent scholarly assessment has not been performed.

## References
1. S. Chaiken, C. R. H. Hanusa, T. Zaslavsky, *A \(q\)-Queens Problem. I. General Theory*, arXiv:1303.1879, first public March 8, 2013. https://arxiv.org/abs/1303.1879
2. S. Chaiken, C. R. H. Hanusa, T. Zaslavsky, *A \(q\)-Queens Problem. II. The Square Board*, arXiv:1402.4880, first public February 20, 2014. https://arxiv.org/abs/1402.4880
3. OEIS A000170, *Number of ways of placing nonattacking queens on a square board*. https://oeis.org/A000170
4. *Five simultaneous queen changes are necessary and sufficient for eight-queen solution mobility*, available at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-five-simultaneous-queen-changes-are-necessary-and-sufficient-for--ded64631ea3e
