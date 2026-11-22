# Complete binary convolution-rank census on the five-by-five affine plane

## Finding

Let \(G=\mathbb F_5^2\) under addition. For every subset \(S\subseteq G\), let \(T_S\) be the complex linear convolution operator
\[
 (T_Sf)(z)=\sum_{s\in S}f(z-s),\qquad f:G\to\mathbb C.
\]
Among all \(2^{25}=33{,}554{,}432\) subsets, the complete rank distribution is

| \(\operatorname{rank}_{\mathbb C}T_S\) | Number of subsets \(S\) |
|---:|---:|
| 0 | 1 |
| 1 | 1 |
| 5 | 180 |
| 13 | 4,000 |
| 17 | 51,000 |
| 21 | 1,122,600 |
| 25 | 32,376,650 |

In particular, ranks \(9\) and \(2,3,4,6,7,8,10,11,12,14,15,16,18,19,20,22,23,24\) do not occur. The missing rank-nine obstruction is independently known in the language of special directions; the **new claim** is the complete rank-by-weight multiplicity census below, not priority for that obstruction alone.

The complete nontrivial weight refinement is:

| Support weight | Rank 5 | Rank 13 | Rank 17 | Rank 21 | Rank 25 |
|---:|---:|---:|---:|---:|---:|
| 5 or 20, each | 30 | 0 | 1,500 | 15,600 | 36,000 |
| 10 or 15, each | 60 | 2,000 | 24,000 | 545,700 | 2,697,000 |

At support weight zero, rank is zero; at weight 25, rank is one. For every other weight (not divisible by five), **all** \(\binom{25}{w}\) subsets have rank 25. Every positive entry denotes an attained value for a concrete support, not an asymptotic probability.

## Assumptions and scope

All subsets are labelled; points of \(G\) are the 25 ordered pairs \((x,y)\) with \(x,y\in\mathbb F_5\). Indicators take values in \(\{0,1\}\); no weighting of the selected points is allowed. The Fourier transform is unnormalized:
\[
 \widehat{1_S}(a,b)=\sum_{(x,y)\in S}\zeta_5^{-(ax+by)},\qquad \zeta_5=e^{2\pi i/5}.
\]
Convolution is diagonalized by this transform, and its complex rank equals the number of nonzero Fourier multipliers. There are six directions (projective one-dimensional character subspaces) and six corresponding pencils of five parallel affine lines.

For each pencil \(d\), say that \(S\) is *balanced* in \(d\) when each of its five affine lines contains exactly \(|S|/5\) points. Let \(k(S)\) count balanced pencils. For nonempty \(S\), the convolution rank is \(25-4k(S)\). This criterion is specific to integer-valued indicators and the prime fifth roots of unity.

## Proof

**1. Exact Fourier-zero criterion.** Fix \((a,b)\ne(0,0)\). Let \(n_j\) be the number of points of \(S\) on the affine level line \(ax+by=j\), for \(j\in\mathbb F_5\). Then
\[
 \widehat{1_S}(a,b)=\sum_{j=0}^4n_j\zeta_5^{-j}.
\]
Because the minimal polynomial of \(\zeta_5\) over \(\mathbb Q\) is \(1+X+X^2+X^3+X^4\), this sum vanishes **if and only if** \(n_0=n_1=\cdots=n_4\). All four nonzero frequencies on one projective character line vanish together, and no others do. The zero frequency equals \(|S|\). Hence the rank criterion above follows, including the zero and full mask exceptions. Balance is impossible unless \(5\mid |S|\).

**2. Counting simultaneous balanced pencils.** For \(w=5,10\), denote by \(N_t(w)\) the number of \(w\)-element subsets balanced in each member of any fixed \(t\)-element family of the six pencils. This number is independent of the chosen family: \(\operatorname{PGL}(2,5)\) acts sharply triply transitively on the six directions and therefore transitively on their \(t\)-subsets for every \(0\le t\le6\). Exact values are

| \(w\) | \(N_0\) | \(N_1\) | \(N_2\) | \(N_3\) | \(N_4\) | \(N_5\) | \(N_6\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 53,130 | 3,125 | 120 | 15 | 10 | 5 | 0 |
| 10 | 3,268,760 | 100,000 | 2,040 | 130 | 20 | 10 | 0 |

Here \(N_0(w)=\binom{25}{w}\) and \(N_1(w)=\binom5{w/5}^5\). For two pencils, make them the rows and columns of a \(5\times5\) matrix. At weight five the valid matrices are permutation matrices: \(N_2(5)=5!=120\). At weight ten they are two-regular bipartite graphs. A 10-cycle contributes \(5!4!/2=1440\) matrices; a disjoint 6-cycle and 4-cycle contribute \(\binom52^2\cdot6=600\), hence \(N_2(10)=2040\).

For three pencils, transform them to rows, columns and wrapped diagonals \(x+y=j\). Choose in each row a subset \(R_x\subseteq\mathbb F_5\) of size \(h=w/5\). The exact number is the following finite integer sum, with no numerical tolerance or approximation:
\[
 N_3(5h)=\sum_{(R_0,\ldots,R_4)\in\binom{\mathbb F_5}{h}^{5}}
 \prod_{j=0}^4 \mathbf1\!\left\{\sum_x\mathbf1\{j\in R_x\}=h\right\}
 \prod_{j=0}^4 \mathbf1\!\left\{\sum_x\mathbf1\{j-x\in R_x\}=h\right\}.
\]
The complete direct evaluation has \(5^5=3125\) row assignments for \(h=1\) and \(10^5=100000\) for \(h=2\). The standalone `line_incidence_checker.py` implements exactly these finite sums and independently obtains \(15\) and \(130\). In particular, this is an exhaustive finite computation rather than an extrapolation from sampled masks.

For four balanced pencils, the Fourier transform is supported on at most two one-dimensional character subspaces. After an invertible linear change of coordinates, Fourier inversion gives \(1_S(x,y)=u(x)+v(y)\). A \(\{0,1\}\)-valued additively separable function must have \(u\) or \(v\) constant: otherwise a nonzero row difference and a nonzero column difference would yield four binary values \(c,c+\alpha,c+\beta,c+\alpha+\beta\) with both \(\alpha\) and \(\beta\) nonzero, which is impossible. Consequently, a nonconstant binary mask with four balanced pencils must in fact be a union of \(h\) parallel lines and is balanced in five pencils. Given four specified balanced pencils, there are two choices for the exceptional direction and \(\binom5h\) unions per choice. Thus
\[
 N_4(5h)=2\binom5h,\quad N_5(5h)=\binom5h,\quad N_6(5h)=0
\]
for \(h=1,2\), completing the count table.

**3. Binomial inversion.** Let \(F_w(k)\) be the number of \(w\)-point masks with exactly \(k\) balanced pencils. Double counting pairs consisting of a mask and a \(t\)-subset of its balanced pencils gives
\[
 \sum_{k=t}^6\binom ktF_w(k)=\binom6tN_t(w).
\]
Therefore
\[
 F_w(k)=\sum_{t=k}^6(-1)^{t-k}\binom tk\binom6tN_t(w).
\]
Substitution yields for weight five the counts \((36{,}000,15{,}600,1{,}500,0,0,30,0)\) for \(k=0,1,\ldots,6\), and for weight ten \((2{,}697{,}000,545{,}700,24{,}000,2{,}000,0,60,0)\). Complementation preserves all nonzero-frequency vanishing conditions and, for proper nonempty masks, preserves the nonzero zero-frequency multiplier. Therefore weights twenty and fifteen have the respective same rank tables. All weights not divisible by five are full rank, except that the empty mask has rank zero. Summation gives the asserted complete spectrum and counts.

## Verification

The standalone pure-Python `line_incidence_checker.py` enumerates row choices for a fixed pair/triple of pencils, checks the numerical intersection counts, performs binomial inversion and verifies the final \(2^{25}\) total. It uses only the standard library.

The independent C file `full_direct_check.c` runs through **all 33,554,432** labelled masks, directly constructs six pencils, compares exact line populations, records every rank and weight, and asserts the claimed totals. It makes no use of the binomial-inversion formula or the Python enumerator. Compile with `cc -O3 -std=c11 -Wall -Wextra -Werror full_direct_check.c -o full_direct_check` and run `./full_direct_check`. Both programs were executed successfully on the packaged source; their exact results are recorded in `verification_counts.txt`.

## Relationship to prior work

Meshulam's archived 2003 preprint (published in 2006) proves a general lower bound on Fourier-support size for finite abelian groups; it does not resolve exact multiplicities of binary-mask convolution ranks. Biró and Lev sharpen finite-plane uncertainty inequalities for rational-valued functions but do not enumerate all labelled masks at order five. Kiss and Somlai study *special directions* (directions in which a set is not balanced); their complete structural classification of sets with exactly three special directions covers the existence and geometric form of our rank-13 weight-ten masks, and their no-two-special-directions result already entails the rank-nine obstruction. We therefore do **not** claim either statement as new. The contribution here is the full exact rank-by-weight census across the entire binary mask space, obtained by simultaneous-pencil intersection counting and inversion.

A separate published rank-incidence census of four-row/four-column Fourier restrictions on \(\mathbb F_5^2\) concerns a different operator: rectangular submatrices of the 25-point Fourier matrix, not convolution by all binary masks. Likewise, rank counts for binary circulants on cyclic groups do not imply this elementary-abelian-plane table.

## Limitations

These counts apply only to \(0\)-\(1\) indicators on \(\mathbb F_5^2\), not to arbitrary complex coefficients, other primes, or nonlinear noise stability. Rank measures identifiability, not the least nonzero singular value or conditioning. The complete census is finite; it does not establish an asymptotic law for \(\mathbb F_p^2\). Prior structure results, including the absence of exactly two special directions, must not be counted as independent new discoveries. The originality comparison is bounded by the inspected indexed literature and published research catalog; unindexed equivalent numerical censuses remain possible.

## References

1. Roy Meshulam, *An Uncertainty Inequality for Finite Abelian Groups*, arXiv:math/0312407, first posted 22 December 2003; *European Journal of Combinatorics* **27** (2006), 63–67. https://arxiv.org/abs/math/0312407
2. András Biró and Vsevolod F. Lev, *Uncertainty in finite planes*, arXiv:1808.07424 (2018); *Journal of Functional Analysis* **281** (2021), 109026. https://arxiv.org/abs/1808.07424
3. Gergely Kiss and Gábor Somlai, *Special directions on the finite affine plane*, arXiv:2109.13992 (2021); *Designs, Codes and Cryptography* **92** (2024), 2587–2597. https://arxiv.org/abs/2109.13992
