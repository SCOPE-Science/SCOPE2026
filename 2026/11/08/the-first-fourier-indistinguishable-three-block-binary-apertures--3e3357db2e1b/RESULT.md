# The first Fourier-indistinguishable three-block binary apertures

## Finding

Consider the class of subsets of the real line which are unions of exactly three nonempty, pairwise separated intervals with **integer endpoints**. Two such subsets are called Fourier-indistinguishable when their indicator functions have equal Fourier-transform magnitudes at every real frequency. Their **span** is the distance from their smallest to largest endpoint, measured in unit cells.

The minimum span of a Fourier-indistinguishable pair which is not related by translation or reflection is **12**. Up to translating or reflecting either aperture and interchanging the two apertures, exactly one inequivalent pair exists at that span:

\[
\Omega_1=[0,1)\cup[2,8)\cup[10,12),\qquad
\Omega_2=[0,1)\cup[3,6)\cup[7,12).
\]

Equivalently, represent the occupied cells by binary words, indexed from cell 0, with first and last digits 1. Every three-run word of span at most 11 is determined by its entire Fourier magnitude among all three-run words, up to reversal. At span 12, the sole nontrivial ambiguity (up to reversal) consists of

`101111110011` and `100111011111`.

This is a **sharp finite-grid statement**: it does not claim uniqueness for arbitrary real (noninteger) interval endpoints, nor for competitors outside the three-interval class.

## Assumptions and scope

For an integer \(n\ge5\), a three-run word \(w=(w_0,\ldots,w_{n-1})\in\{0,1\}^n\) has \(w_0=w_{n-1}=1\) and exactly three maximal consecutive runs of ones separated by two nonempty zero runs. Define

\[
\Omega_w=\bigcup_{j:w_j=1}[j,j+1),\quad
P_w(z)=\sum_{j=0}^{n-1}w_jz^j,
\quad C_w(d)=\sum_{j=0}^{n-1-d}w_jw_{j+d}\quad(0\le d<n).
\]

The continuous Fourier transform uses the convention \(\widehat{\mathbf1_{\Omega}}(\xi)=\int_\mathbb R\mathbf1_{\Omega}(x)e^{-2\pi i\xi x}\,dx\). All comparisons involve complete magnitudes over **all** \(\xi\in\mathbb R\), not finitely many DFT sample frequencies. Endpoints differing on sets of measure zero are immaterial. The allowed trivial transformations are translations and reflections of subsets of \(\mathbb R\).

## Proof

**Reduction to an exact integer signature.** The elementary unit-cell integral gives

\[
\widehat{\mathbf1_{\Omega_w}}(\xi)=\frac{1-e^{-2\pi i\xi}}{2\pi i\xi}\,P_w(e^{-2\pi i\xi}),
\]

with the continuous value at \(\xi=0\). Thus two words have equal continuous Fourier magnitudes if and only if \(P_w(z)P_w(z^{-1})\) agrees on the unit circle; the latter is a Laurent polynomial with integer coefficients. Its coefficient at \(z^d\), for \(d\ge0\), is precisely \(C_w(d)\). Two normalized three-run words are therefore indistinguishable exactly when their full integer autocorrelation signatures agree. In particular, \(C_w(n-1)=1\); the largest nonzero lag fixes the span, even when the two candidate word lengths were not initially assumed equal.

**Exhaustive lower bound and complete first fiber.** Every normalized three-run word of span \(n\) has a unique positive five-part run-length composition

\[
 n=\ell_1+g_1+\ell_2+g_2+\ell_3,
 \qquad \ell_1,g_1,\ell_2,g_2,\ell_3\ge1.
\]

Equivalently, choose exactly four cuts \(1\le a<b<c<d\le n-1\), and write the word as \(1^a0^{b-a}1^{c-b}0^{d-c}1^{n-d}\). There are exactly \(\binom{n-1}{4}\) words. `CHECK.py` visits **every** such composition for every \(n=5,\ldots,12\) and computes the entire autocorrelation twice by distinct exact-integer algorithms. Each signature is grouped into reversal classes, since normalizing the two extreme occupied cells rules out any additional translation equivalence.

The reproducible finite census is:

| Span | Three-run words | Reversal classes | Distinct autocorrelations | Nontrivial fibers |
| ---: | ---: | ---: | ---: | ---: |
| 5 | 1 | 1 | 1 | 0 |
| 6 | 5 | 3 | 3 | 0 |
| 7 | 15 | 9 | 9 | 0 |
| 8 | 35 | 19 | 19 | 0 |
| 9 | 70 | 38 | 38 | 0 |
| 10 | 126 | 66 | 66 | 0 |
| 11 | 210 | 110 | 110 | 0 |
| 12 | 330 | 170 | 169 | 1 |

At span 12 the unique nontrivial fiber contains precisely the two displayed reversal classes. The enumeration covers \(792\) exact words in total. Completeness is established by the positive-composition bijection, not by a heuristic numerical sample. Because each comparison is a finite integer equality, no floating-point tolerance or infinite extrapolation is involved.

**Explicit witness and algebraic identity.** Set

\[
 C(z)=(1+z+z^2)(1+z^3+z^4),\quad
 R(z)=z^5-z^4+z^2-z+1.
\]

Then the two binary generating polynomials factor as

\[
 P_{\Omega_1}(z)=C(z)R(z),\qquad
 P_{\Omega_2}(z)=C(z)z^5R(z^{-1}).
\]

For every \(|z|=1\), the factors \(R(z)\) and \(z^5R(z^{-1})\) have equal absolute values, so the Fourier magnitudes of the two interval indicators agree at every real frequency. Their shared autocorrelation coefficients for nonnegative lags are

\[
 (9,6,5,5,5,4,3,3,2,1,1,1).
\]

The two words are neither equal nor reversals; hence neither interval union is a translate or reflection of the other. Together with the complete finite census, this establishes the sharp span and uniqueness of the first ambiguity class.

## Verification

Run `python3 CHECK.py` in the directory containing this file. The checker uses only the Python standard library. It regenerates every five-part composition, verifies the run structure, counts reversal classes and autocorrelation fibers, independently compares pair-count and bit-shift autocorrelations, and checks the two exceptional words. The expected final line is `CHECK_OK exact_three_run_words=792 first_span=12 exceptional_unoriented_pair=1`. An independent all-bitmask enumeration of normalized words with four transitions was also performed with the same counts. The analytical reduction and explicit polynomial factorization can be verified by ordinary Laurent-polynomial multiplication.

## Relationship to prior work

Xia and Xu (2026) show that indicator functions of unions of at most two intervals are Fourier phase-retrievable and construct examples of nonuniqueness with three or more intervals. The present result **does not re-claim their nonuniqueness theorem**: it fixes integer endpoints, resolves the smallest possible three-interval span in that lattice model, and identifies the complete first ambiguity fiber. Their Section 5 gives general factor-flipping constructions; the displayed formulas for its individual examples were not fully accessible in the consulted representation, so coincidence of an example is possible. Even such a coincidence would not by itself imply the exhaustive minimal-span and uniqueness assertions here.

Katz, Rahman and Ward (2023) establish a general Laurent-polynomial factorization framework for sequences with equal aperiodic autocorrelation; in particular, factor reversal explains the algebraic witness above. Their primary sequence alphabet for the detailed finite censuses is unimodular (including \(\pm1\)), unlike the indicator-valued three-run subclass considered here. The general factorization is a mathematical input, not a new claim. Prior general homometric-set theory and binary phase-retrieval work are likewise acknowledged. A previously published, unindexed census of this exact three-run restriction remains a residual originality risk.

## Limitations

The sharp threshold is for **unit-grid three-interval indicator sets with integer endpoints** and exact, full continuous-frequency magnitudes. It does not claim minimality among arbitrary real endpoints, uniqueness against competitors having a different number of intervals, recovery from finitely many noisy samples, or a classification beyond span 12. The lower bound and class census are computer-assisted finite proofs: they depend on running and inspecting the complete integer enumeration supplied here, not on sampling a subset of candidate words. No independent external mathematical audit has been performed.

## References

1. Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855 (first submitted 18 June 2026), https://arxiv.org/abs/2606.19855. See Theorems 1.2, 1.7 and Section 5.
2. Daniel J. Katz, Adeebur Rahman and Michael J. Ward, *Sequences with identical autocorrelation functions*, arXiv:2308.07467 (first submitted 14 August 2023), https://arxiv.org/abs/2308.07467. See Theorem 1.1 and the introduction.
3. J. Rosenblatt and P. D. Seymour, *The Structure of Homometric Sets*, SIAM J. Algebraic Discrete Methods 3 (1982), DOI:10.1137/0603035.
4. *Phase retrieval for sparse binary signal: uniqueness and algorithm*, Inverse Problems in Science and Engineering (2017), DOI:10.1080/17415977.2017.1336551.
