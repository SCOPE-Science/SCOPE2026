# The ternary penalty and quaternary recovery for the four-dimensional Fourier cube

## Finding

Let \(q\in\{2,3,4\}\), \(\zeta_q=e^{2\pi i/q}\), and consider every sixteen-coefficient Fourier polynomial
\[
 P_a(z_1,z_2,z_3,z_4)=\sum_{x\in\{0,1\}^4} a_x\prod_{j=1}^4 z_j^{x_j},\qquad a_x\in\{\zeta_q^r:0\le r<q\}.
\]
With normalized Haar measure on \(\mathbb T^4\), its fourth moment has the **sharp minima**
\[
\min M_4(a)=
\begin{cases}
 336 & q=2,\\
 384 & q=3,\\
 336 & q=4.
\end{cases}\qquad M_4(a)=\int_{\mathbb T^4}|P_a(z)|^4\,dm(z).
\]
The binary value is included as an already known comparator; **the ternary and quaternary values, their exact optimizer classifications, and their strict next-level gaps are the finding.** After quotienting by all global and coordinate-character phases, the ternary equality set has exactly \(240\) elements and the quaternary equality set exactly \(24\). Hence their full equality sets have \(58{,}320\) and \(24{,}576\) arrays, respectively. Within each alphabet, every nonminimizer has fourth moment at least \(396\) for \(q=3\) and at least \(368\) for \(q=4\), and both bounds are attained.

More precisely, each equality set comprises **two symmetry orbits** under coordinate permutations, coordinate inversions, complex conjugation, global phase, and coordinate-character phases. After the canonical normalization specified below, the ternary orbit sizes are \(48\) and \(192\), and the quaternary orbit sizes are \(12\) and \(12\). Read each sixteen-digit word in index order \(x=0,1,\ldots,15\) as the exponent array \(a_x=\zeta_q^{t_x}\). Canonical orbit representatives are:

| Alphabet | Canonical exponent representative | Normalized orbit size |
|---|---|---:|
| \(q=3\) | `0000001201022110` | 48 |
| \(q=3\) | `0000001202102120` | 192 |
| \(q=4\) | `0000002202022002` | 12 |
| \(q=4\) | `0001013303133110` | 12 |

The full optimizer sets are exactly the symmetry images of these four representatives under the specified alphabet, with no other equality cases. The lists `q3_optimizers.txt` and `q4_optimizers.txt` give all canonical normalized arrays explicitly. The binary minimum \(336\) is attained by \(384\) binary arrays, as established in prior work.

## Assumptions and scope

The frequency support is the **integer cube** \(\{0,1\}^4\subset\mathbb Z^4\), not the Boolean group under modular coordinate addition. Moments use continuous normalized Haar measure and are not periodic autocorrelation energies on \((\mathbb Z/2\mathbb Z)^4\). The coefficient alphabet comprises the **exact** \(q\)-th roots of unity, and each coefficient has magnitude one. This theorem quantifies only over the three specified alphabets. It makes no claim that the quaternary optimum is globally optimal over arbitrary complex phases, nor that these values apply to other dimensions or frequency supports.

Index \(x\in\{0,1\}^4\) by \(x=\sum_{j=1}^4 2^{j-1}x_j\). The free gauge group multiplies \(a_x\) by \(\zeta_q^{c+\sum_j b_jx_j}\), with \(c,b_j\in\mathbb Z/q\mathbb Z\); this preserves the fourth moment. Every orbit of this gauge group has exactly one representative with \(a_0=a_{1}=a_{2}=a_{4}=a_{8}=1\), so it has \(q^5\) members. Coordinate inversions mean exchanging the two levels \(x_j=0\) and \(x_j=1\), which corresponds to reversing the corresponding polynomial coordinate up to a monomial. Inversion, permutation, and conjugation preserve fourth moment.

## Proof

**Exact autocorrelation identity.** For \(d\in\{-1,0,1\}^4\) define
\[
 R_d(a)=\sum_{\substack{x\in\{0,1\}^4\\x+d\in\{0,1\}^4}}a_{x+d}\overline{a_x}.
\]
Fourier orthogonality gives, without approximation,
\[
 M_4(a)=\sum_{d\in\{-1,0,1\}^4}|R_d(a)|^2.
\]
In particular, \(R_0(a)=16\), so the nonzero-shift sum is exactly \(M_4(a)-256\). Multiplication by an affine character multiplies each \(R_d\) by a unit scalar, proving gauge invariance.

**Exact cyclotomic arithmetic.** Write \(a_x=\zeta_q^{t_x}\) and let \(c_r(d)\) count those autocorrelation summands having phase \(\zeta_q^r\). The squared norms have integral expressions:
\[
\begin{aligned}
q=2:\quad&|R_d|^2=(c_0-c_1)^2;\\
q=3:\quad&|R_d|^2=c_0^2+c_1^2+c_2^2-c_0c_1-c_0c_2-c_1c_2;\\
q=4:\quad&|R_d|^2=(c_0-c_2)^2+(c_1-c_3)^2.
\end{aligned}
\]
Thus there are no floating-point comparisons or unproved number-field predicates in the exhaustive minimization.

**Exhaustive, logically complete minimization.** Fix \(t_0=t_1=t_2=t_4=t_8=0\). The remaining eleven exponents range independently through \(\{0,\ldots,q-1\}\). The bundled `checker.cpp` loops through every radix-\(q\) integer from zero to \(q^{11}-1\), decodes each digit bijectively, calculates all \(81\) shifts with the preceding integer formulas, and retains the complete equality set and the strict second-smallest value. Its exhaustive counts are:

| \(q\) | Canonical candidates | Minimum | Next value | Canonical minimizers |
|---|---:|---:|---:|---:|
| 2 | 2,048 | 336 | 400 | 12 |
| 3 | 177,147 | 384 | 396 | 240 |
| 4 | 4,194,304 | 336 | 368 | 24 |

Complete coverage follows from the independent digit range and free gauge normalization. For **every** minimizing word, the same program independently recomputes the fourth moment by ordered-pair Fourier convolution: \(C_t=\sum_{x+y=t}a_xa_y\) for \(t\in\{0,1,2\}^4\) and \(M_4=\sum_t|C_t|^2\), and confirms equality with the autocorrelation value. This second calculation is independent of the shift-pair construction. The checker returns failure if any expected optimum, next value, or equality count differs.

**Complete orbit classification.** The bundled `orbit_checker.py` applies all \(4!\) coordinate permutations, all \(2^4\) coordinate inversions, and conjugation, canonically removes the affine \(q\)-phase gauge after each operation, and forms the resulting finite orbits of each listed minimizer. It checks that each orbit lies within the exhaustive equality list and partitions that list into exactly two disjoint orbits with sizes \((48,192)\) and \((12,12)\), respectively. Their listed canonical representatives reconstruct every minimizer. Multiplication by \(q^5\) then gives the stated full counts. These are exhaustive finite proofs, not statistical evidence or extrapolations.

## Verification

From the artifact directory, compile `g++ -O3 -std=c++17 checker.cpp -o checker`, then execute `./checker 2`, `./checker 3`, and `./checker 4`. Each prints `CHECK_PASS`, with the exact counts in the proof, and for the latter two prints the full canonical equality list. The files `q3_optimizers.txt` and `q4_optimizers.txt` contain exactly those lists (one sixteen-character exponent word per physical line). Execute `python orbit_checker.py 3 q3_optimizers.txt` and `python orbit_checker.py 4 q4_optimizers.txt`; both print `ORBIT_CHECK_PASS` with the specified two orbit sizes and representatives. The exact source files were compiled and executed after copying into the delivered artifact directory; all checks passed. A separate \(3^4\)-sample FFT quadrature evaluated the two first orbit representatives as \(384\) and \(336\), agreeing with exact enumeration; quadrature serves only as a supplementary consistency test.

## Relationship to prior work

The published four-dimensional **binary** cube classification already proves the \(q=2\) value \(336\), with exactly twelve gauge classes; it explicitly does not cover ternary or quaternary coefficients. The new alphabet-wise minima, two-orbit classifications, and exact gaps are not logical consequences of that binary theorem: binary signs are not contained in the ternary alphabet, and the quaternary alphabet admits additional nonbinary optimizers. Other existing sharp alphabet results concern different supports, notably the eight-tone three-dimensional cube, twelve-tone rectangular prism, and planar four-by-two rectangle. Their values and orbit lists do not imply the present sixteen-tone four-dimensional classification.

Pai and Chen's generalized Boolean-function path construction (Theorem 12 and conclusions) concerns **pairs** whose aperiodic autocorrelations cancel when summed; it does not optimize the fourth moment of an individual four-dimensional ternary or quaternary array. Zhang, Fan, and Mesnager's 2021 paper similarly develops two-dimensional \(q\)-ary **Z-complementary pairs** rather than a complete single-array energy minimization. Searches for alternate formulations using aperiodic integrated sidelobe level, PSK alphabets, polyphase cube arrays, and existing small-array tables did not identify an equivalent classification. Inaccessible or unindexed older array-design tables remain a bibliographic priority risk; search absence is not a proof of historical priority.

## Limitations

All sharp bounds here are for fixed sixteen-tone support and finite alphabets \(q=2,3,4\). The results do not determine the unrestricted complex-phase minimum, nor arbitrary \(q\), arbitrary-dimensional cubes, or families of complementary **pairs**. The optimizer proof is finite computer-assisted exact enumeration with complete source, rather than a short closed-form noncomputational inequality. Historical priority cannot be certified exhaustively, and independent mathematical audit has not been performed.

## References

1. C.-Y. Pai and C.-Y. Chen, *Two-Dimensional Golay Complementary Array Sets from Generalized Boolean Functions*, arXiv:2102.04043v1, first posted February 8, 2021, https://arxiv.org/html/2102.04043v1. Material inspected: introduction, Theorem 12, complementary correlation construction, conclusions.
2. H. Zhang, C. Fan, and S. Mesnager, *New constructions of q-Ary 2-D Z-Complementary Array Pairs*, arXiv:2107.11599v1, first posted July 24, 2021, https://arxiv.org/html/2107.11599v1. Material inspected: abstract, Theorems 1–2, conclusions.
3. *Sharp binary fourth moments on the four-cube and quadratic path rigidity through seven variables*, public mathematical record dated October 11, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-binary-fourth-moments-on-the-four-cube-and-quadratic-path--280918c7a8c9. The full RESULT.md was inspected for the exact binary antecedent and exclusions.
4. *Exact phase-alphabet fourth moments on a twelve-mode Fourier prism*, public mathematical record dated November 1, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-phase-alphabet-fourth-moments-on-a-twelve-mode-fourier-pri--6f89708f4d4b. Distinct frequency support and dimension.
