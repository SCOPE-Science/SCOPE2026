# Exact peak-sidelobe phase thresholds for the centrally punctured square Fourier aperture

## Finding

Let \(\Lambda=\{0,1,2\}^2\setminus\{(1,1)\}\), let \(q\in\{2,3,4,5,6,7,8\}\), and put \(\zeta_q=e^{2\pi i/q}\). Assign coefficients \(a_{i,j}\in\{\zeta_q^r:0\le r<q\}\) to the eight elements of \(\Lambda\), with zero at its center and outside the square. For each integer displacement define the *aperiodic* autocorrelation

\[
C_a(u,v)=\sum_{(i,j)\in\Lambda\,:\,(i+u,j+v)\in\Lambda}a_{i+u,j+v}\overline{a_{i,j}},
\qquad \mathrm{PSL}(a)=\max_{(u,v)\ne(0,0)}|C_a(u,v)|.
\]

The exact minimum \(\mathrm{PSL}(a)^2\), the number of minimizing arrays up to the modulation equivalence described below, and the number of all labeled minimizing arrays are as follows:

| Alphabet size | Minimum squared peak sidelobe | Normalized minimizing arrays | All minimizing arrays |
|:--:|:--:|--:|--:|
| \(2\) | \(4\) | 20 | 160 |
| \(3\) | \(3\) | 8 | 216 |
| \(4\) | \(2\) | 24 | 1536 |
| \(5\) | \((3+\sqrt5)/2\) | 240 | 30000 |
| \(6\) | \(1\) | 2 | 432 |
| \(7\) | \(4\cos^2(2\pi/7)\) | 28 | 9604 |
| \(8\) | \(2\) | 114 | 58368 |

In particular, the smallest phase alphabet attaining the absolute universal lower bound \(\mathrm{PSL}=1\) has size six, while neither the seven-phase nor the eight-phase alphabet attains it. The quality of these finite alphabets is nonmonotone. The two normalized six-phase minimizers, in the five free-location order defined below, have exponent vectors \((1,4,5,2,0)\) and \((5,2,1,4,0)\). Their associated eight nonzero coefficients form genuinely two-dimensional arrays. This table makes no assertion about phase alphabets of size nine or larger.

## Assumptions and scope

Every coefficient on \(\Lambda\) has unit modulus and belongs to the indicated finite phase alphabet. The center coefficient is exactly zero; this is not a full \(3\times3\) unimodular array, and correlations are **aperiodic**, not circular. We regard two arrays as equivalent if, for some integers \(r,s,t\) modulo \(q\),

\[
a'_{i,j}=\zeta_q^{r+si+tj}a_{i,j}\qquad((i,j)\in\Lambda).
\]

This action preserves the sidelobe magnitudes. It has exactly \(q^3\) elements acting freely: the three locations \((0,0),(0,1),(1,0)\) determine \((r,s,t)\) uniquely. Each orbit contains exactly one array whose phase exponents at these locations are zero. For such a normalized array let its five free exponents, in order, be those at \((0,2),(1,2),(2,0),(2,1),(2,2)\). The file `OPTIMIZERS.json` records **every** normalized minimizer in precisely this order.

Equivalently, \(P_a(z,w)=\sum_{(i,j)\in\Lambda}a_{i,j}z^iw^j\) has \(C_a(u,v)\) as the coefficient of \(z^uw^v\) in \(|P_a(z,w)|^2\) on the two-torus. The optimization is an \(\ell^\infty\) problem for these *nonconstant Fourier coefficients*, not a fourth-moment or sum-of-squares optimization.

## Proof

**1. Exhaustive symmetry reduction.** The transformation displayed above multiplies each correlation at displacement \((u,v)\) by \(\zeta_q^{su+tv}\); its absolute value is unchanged. Solving the three exponent equations at \((0,0),(0,1),(1,0)\) removes one global phase and two coordinate phases uniquely. Thus there are exactly \(q^5\) inequivalent normalized configurations and each corresponds to exactly \(q^3\) labeled configurations. For \(q=2,\ldots,8\) this is

\[
2^5+3^5+4^5+5^5+6^5+7^5+8^5=61775
\]

configurations. Conjugate symmetry \(C_a(-u,-v)=\overline{C_a(u,v)}\) leaves precisely twelve distinct positive-half-plane shifts to test: \((0,1),(0,2)\), the five displacements \((1,-2),\ldots,(1,2)\), and the five displacements \((2,-2),\ldots,(2,2)\). These are generated in `check_psl.py`; no zero-overlap shifts are relevant.

**2. Exact algebraic scoring, without floating comparison.** If the exponent differences at one displacement are \(d_1,\ldots,d_m\), the squared magnitude of its correlation is exactly

\[
\left|\sum_{j=1}^m\zeta_q^{d_j}\right|^2
=m+\sum_{1\le i<j\le m}2\cos\left(\frac{2\pi(d_i-d_j)}q\right).
\]

For \(q=2,3,4,6\), all the required doubled cosines are integers. For \(q=5\), each squared magnitude is uniquely represented as \((A+B\sqrt5)/2\) with integers \(A,B\). For \(q=8\), it is \(A+B\sqrt2\). For \(q=7\), let \(x=2\cos(2\pi/7)\); the seven doubled cosines are

\[
2,\quad x,\quad x^2-2,\quad 1-x-x^2,\quad
1-x-x^2,\quad x^2-2,\quad x.
\]

Thus every squared magnitude is represented by an integer triple \((A,B,C)\) meaning \(A+Bx+Cx^2\). The number \(x\) is the unique root in \((1,2)\) of \(x^3+x^2-2x-1=0\). Exact integer substitution shows

\[
\frac{1246979603717467}{10^{15}}<x<\frac{1246979603717468}{10^{15}}.
\]

The cubic is strictly increasing on \((1,2)\). For every pair of values compared by the certificate, the interval bounds of their difference have the same strict sign, unless their integer coefficient triples are identical. Comparisons in the two quadratic fields are decided exactly by integer sign and comparison of squares; irrationality of \(\sqrt2\) and \(\sqrt5\) eliminates nontrivial equality ties. No rounding or equality tolerance is used. The code implements these formulas directly.

**3. Global minimization and equality counts.** For each normalized five-tuple the certificate takes the largest of the twelve *exact* squared magnitudes and compares it with the current least value. It exhausts the \(q^5\) five-tuples for each \(q\). The resulting minimum representatives in the respective rings are \(4,3,2,(3+\sqrt5)/2,1,x^2,2\). The exact equality counts are \(20,8,24,240,2,28,114\). The equality list is included in `OPTIMIZERS.json`; the checker recomputes and compares the entire list, not just totals. Multiplication by the free action size \(q^3\) yields the final column of the table.

**4. Sharp universal floor and a direct six-phase witness.** The displacement \((2,2)\) pairs only the two corner sites \((0,0)\) and \((2,2)\). Hence \(|C_a(2,2)|=1\) for every allowed unimodular coefficient array, regardless of alphabet. The array of sixth-root exponents

\[
\begin{pmatrix}
0&0&1\\
0&\text{zero}&4\\
5&2&0
\end{pmatrix}
\]

has squared sidelobes zero at displacements \((0,1)\) and \((1,0)\) and exactly one at each of the ten other selected displacements. Thus it attains \(\mathrm{PSL}=1\), and the exhaustive comparisons show all smaller phase alphabets fail. This also independently witnesses the optimal six-phase value without relying on a numerical approximation.

The finitely checked theorem is thereby proved by an exact, reproducible exhaustive argument. It is a statement for the seven specified alphabets, not a claim that a finite search proves a theorem for arbitrary \(q\).

## Verification

Run `python3 check_psl.py --catalog OPTIMIZERS.json` using standard Python 3. Its final two lines are exactly `HOLLOW_SQUARE_PSL_EXACT_PASS cases=61775` and `OPTIMIZER_CATALOG_EXACT_MATCH`. The implementation fixes the support and twelve displacements explicitly, enumerates all exponent vectors, uses exact integer or algebraic-integer comparison rules, checks the seven minima and all equality counts, and matches every stored optimizer. Independently evaluating one representative for each alphabet with ordinary complex arithmetic reproduces the approximate squared peak values \(4,3,2,2.6180339887,1,1.5549581321,2\), but **no** floating calculation enters the certificate.

The checker uses no external data, packages, network access, or tolerance-dependent tests. The algebraic exactness of its scoring formula and completeness of its normalization are proved above; merely rerunning the code is not a substitute for those mathematical steps.

## Relationship to prior work

Pai and Chen define two-dimensional aperiodic autocorrelation and construct complementary *pairs and sets* of arrays; their theorems make no exact claim about minimizing the maximum single-array sidelobe for an eight-site, center-punctured support. Katz and van der Linden study peak sidelobes of recursive one-dimensional Golay–Rudin–Shapiro sequences. Bell, Jedwab, Khatirinejad and Schmidt examine fully occupied three-phase Barker arrays; in particular, the familiar fully occupied \(3\times3\) three-phase Barker example cannot simply be used after deleting its center, and their results do not constitute this punctured-support classification.

Exact fourth Fourier moments of the same eight-site support have also been considered. The fourth moment minimizes the **sum of squared sidelobes**, whereas this theorem minimizes their **largest squared magnitude**. A fourth-moment lower bound alone cannot determine the peak-sidelobe optimizer classes. For example, the five-phase peak criterion has 240 normalized minimizers here, versus four normalized fourth-moment minimizers in that separate computation. The two six-phase minimizers here happen to coincide with the known fourth-moment minimizing pair; that overlap is not presented as a separate novelty claim. The new claim is the complete distinct peak-sidelobe classification and alphabet threshold, including its new cases and equality counts.

## Limitations

An exhaustive exact finite-alphabet computation is not a continuous-phase classification. This result says nothing about all phase alphabet sizes, any nonunit coefficient magnitudes, changing or filling the center, or periodic correlation. Although the listed results are mathematically exact given the stated enumeration, independent external mathematical audit has not occurred. Priority relative to unpublished or obscure specialist tables of sparse two-dimensional aperiodic arrays remains an acknowledged bibliographic uncertainty.

## References

1. C.-Y. Pai and C.-Y. Chen, *Two-Dimensional Golay Complementary Array Sets from Generalized Boolean Functions*, arXiv:2102.04043v1 (2021-02-08), especially Definitions 1–3 and construction theorems. https://arxiv.org/html/2102.04043v1
2. D. J. Katz and C. M. van der Linden, *Peak Sidelobe Level and Peak Crosscorrelation of Golay–Rudin–Shapiro Sequences*, arXiv:2108.07318v1 (2021-08-16), Sections 1–2. https://arxiv.org/abs/2108.07318
3. J. P. Bell, J. Jedwab, M. Khatirinejad and K.-U. Schmidt, *Three-phase Barker arrays*, dated 2013-06-01 (revised 2013-09-17), Sections 1–2. https://www.sfu.ca/~jed/Papers/Bell%20Jedwab%20Khatirinejad%20Schmidt.%203-phase%20Barker.%202015.pdf
