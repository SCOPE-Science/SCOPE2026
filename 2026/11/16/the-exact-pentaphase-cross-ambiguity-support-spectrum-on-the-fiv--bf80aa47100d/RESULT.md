# The exact pentaphase cross-ambiguity support spectrum on the five-cycle

## Finding
Let \(\zeta=\exp(2\pi i/5)\) and let \(f,g:\mathbb Z_5\to\mu_5=\{\zeta^j:0\le j<5\}\). Their unnormalized cyclic cross short-time Fourier transform is
\[
V_gf(x,k)=\sum_{t=0}^4 f(t)\overline{g(t-x)}\zeta^{-kt},\qquad (x,k)\in\mathbb Z_5^2.
\]
Its support cardinality is **exactly one of**
\[
\boxed{5,\ 17,\ 20,\ 21,\ 25}.
\]
All five values occur. After removing the two independent global \(\mu_5\) phases by imposing \(f(0)=g(0)=1\), the respective numbers of ordered pairs are
\[
\boxed{125,\ 12500,\ 12500,\ 52500,\ 313000}.
\]
More precisely, write \(z_x=|\{k:V_gf(x,k)=0\}|\) and sort the five integers \((z_0,\ldots,z_4)\). **Exactly six sorted zero-row profiles occur**, with their normalized ordered-pair counts:

| Sorted row-zero counts | Pair count | Total support |
|---|---:|---:|
| \((0,0,0,0,0)\) | 313000 | 25 |
| \((0,0,0,0,4)\) | 2500 | 21 |
| \((0,1,1,1,1)\) | 50000 | 21 |
| \((1,1,1,1,1)\) | 12500 | 20 |
| \((1,1,1,1,4)\) | 12500 | 17 |
| \((4,4,4,4,4)\) | 125 | 5 |

The 125 smallest-support pairs are exactly the normalized matched-curvature quadratic chirps
\[
f(t)=\zeta^{at^2+bt},\quad g(t)=\zeta^{at^2+ct},\qquad a,b,c\in\mathbb F_5.
\]
Every single time-shift row has either zero, one, or four Fourier zeros; the complete normalized census of row-zero profiles is as displayed.

## Assumptions and scope
Indices, polynomial exponents, frequency and time shifts are taken modulo five. Each sequence has all five coefficients nonzero and of modulus one; in fact each coefficient belongs to the *discrete fifth-root alphabet* \(\mu_5\). The count 390625 is for ordered pairs modulo independent scalar fifth roots (not modulo translations, modulations or conjugation). Each unnormalized pair has 25 representatives before this quotient. Support is the exact number of nonzero transform entries, with no floating-point thresholds. This is a finite, exact-scope theorem; it makes no assertion about arbitrary unimodular phases or other cyclic lengths.

## Proof
**Cyclotomic zero test.** Write \(f(t)=\zeta^{a_t}\), \(g(t)=\zeta^{b_t}\), with \(a_t,b_t\in\mathbb F_5\), and normalize \(a_0=b_0=0\). For fixed \((x,k)\),
\[
V_gf(x,k)=\sum_{t=0}^{4}\zeta^{a_t-b_{t-x}-kt}.
\]
Let \(n_j\) be the number of occurrences of the residue \(j\) in the five displayed exponents, so the transform equals \(\sum_{j=0}^{4}n_j\zeta^j\). The minimal polynomial of \(\zeta\) over \(\mathbb Q\) is \(1+X+X^2+X^3+X^4\). Consequently this sum is zero if and only if all \(n_j\) are equal; as their total is five, **each exponent must occur exactly once**. Equivalently, \(t\mapsto a_t-b_{t-x}-kt\) is a permutation of \(\mathbb F_5\). This exact elementary criterion is the sole numerical-zero oracle used by the exhaustive certificate.

**Local structure.** Every normalized exponent word \(v:\mathbb F_5\to\mathbb F_5\) has \(v(0)=0\) and belongs to one of \(5^4=625\) possibilities. Its row-zero number is the count of slopes \(k\) for which \(t\mapsto v(t)-kt\) is a permutation. Affine words \(v(t)=ct\) give four zeros, because all slopes except \(c\) give permutations. A nonaffine graph determines at least four affine directions by the Rédei–Megyesi direction theorem at prime five; the graph already has distinct abscissas, so at most one of the five finite slopes can be a nondetermined direction. Thus a row has only \(0,1,4\) zeros. Independently, for each fixed slope, precisely \(4!=24\) normalized words give a permutation; subtracting the 20 incidences from the five affine words gives 100 one-zero nonaffine words, and the other 520 words have no zeros. The local word census is therefore \(520,100,5\) for \(0,1,4\) zeros.

If two distinct shifts have affine exponent-difference words, their difference shows that a nonzero finite difference of the exponent polynomial of \(g\) has degree at most one. Since every function on \(\mathbb F_5\) has a unique representing polynomial of degree at most four, and a nonzero first difference lowers its degree by exactly one, \(g\) is quadratic and \(f\) has the same quadratic coefficient. All five shifts are then affine. Hence four-zero rows occur either in exactly one shift or in all five; the latter are exactly the 125 matched-curvature quadratic pairs displayed above. The number of four-zero-row incidences equals \(5\cdot625\cdot5=15625\), giving 15000 pairs with a unique four-zero row after subtracting five incidences for each of the 125 all-five pairs. These structural checks corroborate the exhaustive joint census.

**Complete joint census.** The independently reproducible exhaustive calculation enumerates the \(625^2=390625\) pairs of normalized exponent words. For every pair and every shift \(x=0,\ldots,4\), it determines every vanishing frequency using the exact permutation/cyclotomic criterion above, sorts the five row-zero counts, and increments the corresponding integer counter. The standard-library Python implementation `artifacts/verify_pentaphase.py` reproduces the entire six-profile table and checks all five support-count totals. A separate C++ implementation `artifacts/checker.cpp` reconstructs the transform zero predicate by an independent five-bit exponent-occupancy test, and checks the same tables. No approximation, unverified sampling or unbounded mathematical assertion is used. Since global-phase normalization is bijective onto the \(5^8\) ordered exponent choices enumerated, the verified complete loop proves the displayed finite theorem.

## Verification
Run `python3 artifacts/verify_pentaphase.py` using Python 3 with no external packages. The successful output begins `PENTAPHASE_CROSS_STFT_PASS 390625`. Independently, compile the second implementation with `g++ -O2 -std=c++17 artifacts/checker.cpp -o checker` and run `./checker`; its first line begins `PENTAPHASE_CPP_CHECK_PASS 390625`. Both exact methods and the structural single-row counts were checked before packaging. The checker code is part of this self-contained result, rather than a reference to an external run.

## Relationship to prior work
Nicola's prime-cyclic uncertainty and equality classification (2022) gives the general minimum of five and its chirp minimizers, but neither the other four attainable support values for the fifth-root alphabet nor their exact counts. Krahmer, Pfander and Rashkov (2006) give support inequalities for arbitrary signals and windows; their Proposition 4.4 yields only the five-point minimum for two full-support five-point words. The published *four-frequency gap for constant-envelope prime-cyclic spectrograms* proves the stronger general alternative of five or at least seventeen for any constant-envelope pair at prime five; hence the gap from five to seventeen **is not asserted as new**. The contribution here is the exact attainment spectrum, its two distinct support-21 profiles, and the complete integer multiplicities for the matched prime-length/prime-phase alphabet.

The published *phase-only ambiguity support gap beyond quadratic chirps* treats the self-ambiguity subclass, and gives exactly the three self-support levels \(5,17,21\) for the fifth-root alphabet (with 25, 500 and 100 normalized self-pairs), not the full 390625 ordered cross-pairs. Existing five-site six-phase and four-site four-phase cross-ambiguity classifications treat different cyclotomic alphabets and do not imply this matched-five classification. The Rédei direction theorem explains the row-level finite-field permutation obstruction but not its cross-shift coupling multiplicities.

## Limitations
This is an exact finite classification, not an infinite-family theorem or an assertion of historical priority. It does not provide lower bounds on nonzero ambiguity magnitudes, reconstruction stability, or the zero-set locations beyond the stated sorted shift-row profiles. The row-zero geometry reflects fifth-root coefficients and need not persist for unrestricted complex phases. Historical comparison cannot rule out unindexed specialized pentaphase radar-code tables; mathematical checking was performed without independent external validation.

## References
1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176v1, first public 2022-04-29, Theorem 1.2. https://arxiv.org/html/2204.14176v1
2. F. Krahmer, G. E. Pfander, P. Rashkov, *Uncertainty in time–frequency representations on finite Abelian groups and applications*, arXiv:math/0611493v1, 2006, especially Proposition 4.4. https://arxiv.org/pdf/math/0611493
3. G. Somlai, *A new proof of Rédei's theorem on the number of directions*, arXiv:2212.12823v1, 2022, Theorem 1.1, recounting Rédei–Megyesi's earlier direction theorem. https://arxiv.org/abs/2212.12823
4. J. J. Benedetto, R. L. Benedetto, J. T. Woodworth, *Optimal ambiguity functions and Weil's exponential sum bound*, arXiv:1107.1887v1 (2011), sections 1 and 3. https://arxiv.org/pdf/1107.1887
5. *A four-frequency gap for constant-envelope prime-cyclic spectrograms*, 2026, proof and limitations. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-four-frequency-gap-for-constant-envelope-prime-cyclic-spectrog--d3d02e246771/RESULT.md
6. *A phase-only ambiguity support gap beyond quadratic chirps*, 2026, proof and verification. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-phase-only-ambiguity-support-gap-beyond-quadratic-chirps--ccbbfc2c2a80/RESULT.md
