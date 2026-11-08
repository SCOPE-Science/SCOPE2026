# Exact four-type trigram avoidance for shortest ternary subsequence-universal words

## Finding

Fix the labeled alphabet \(\Sigma=\{0,1,2\}\). For every integer \(k\ge1\), a word \(w\in\Sigma^{3k}\) is *shortest \(k\)-subsequence-universal* if it contains every length-\(k\) word over \(\Sigma\) as a scattered subsequence. Given a forbidden word \(p\in\Sigma^3\), let \(a_p(k)\) count these shortest universal words that **avoid \(p\) as a contiguous factor** (not as a scattered subsequence). Define \(F_p(z)=\sum_{k\ge1}a_p(k)z^k\).

Every one of the \(27\) possible forbidden trigrams belongs, under permutations of alphabet symbols and reversal, to precisely one of four classes. Their complete counting functions are

| Representative \(p\) | \(F_p(z)\) | \(a_p(1),a_p(2),a_p(3),a_p(4)\) |
|---|---|---|
| `000` | \(\dfrac{6z}{1-6z}\) | \(6,36,216,1296\) |
| `001` | \(\dfrac{6z-2z^2}{1-6z+2z^2}\) | \(6,34,192,1084\) |
| `010` | \(\dfrac{6z-4z^2}{1-6z+4z^2}\) | \(6,32,168,880\) |
| `012` | \(\dfrac{5z+6z^2+2z^3}{1-3z-5z^2-2z^3}\) | \(5,21,90,385\) |

For \(k\to\infty\), the four counts have distinct exponential bases, in decreasing order \(6\), \(3+\sqrt7\), \(3+\sqrt5\), and the unique positive root of \(\lambda^3-3\lambda^2-5\lambda-2=0\), approximately \(4.2780395708\). Hence a forbidden length-three factor has four distinct asymptotic avoidance types among shortest ternary subsequence-universal words, even though these words are unrestricted with respect to their contiguous factors otherwise.

## Assumptions and scope

Universality is with respect to the full, fixed, three-letter alphabet, and subsequences preserve position order but need not be contiguous. Avoidance refers exclusively to contiguous factors. The words are linear and labeled; no quotienting by rotation or word relabeling occurs in the counts. Relabeling and reversal are used solely to classify the forbidden patterns. Only \(k\ge1\) is considered. No statement is made for longer-than-minimal universal words, forbidden factors of another length, or other alphabet sizes.

## Proof

**Step 1: Exact structure of shortest universal words.** In an arbitrary \(k\)-universal word, greedily cut a first arch at the first position completing all three symbols, then repeat. The standard arch characterization says that a word is \(k\)-universal exactly when at least \(k\) arches can be cut. Every arch has length at least three. Thus a \(k\)-universal word of length \(3k\) has exactly \(k\) arches of length three and no remaining suffix: it is a concatenation of \(k\) three-letter permutations. Conversely, any concatenation of \(k\) permutations is \(k\)-universal, since one can choose the \(i\)-th target letter from the \(i\)-th permutation. This also proves the minimum length \(3k\).

**Step 2: Exact finite-state reduction.** Order the six permutations as

`012, 021, 102, 120, 201, 210`.

For a fixed trigram \(p\), define the row vector \(v_p\) by \((v_p)_i=1\) when permutation \(i\) avoids \(p\). Define the \(6\times6\) zero-one matrix \(T_p\) by \((T_p)_{ij}=1\) when the concatenation of permutations \(i\) and \(j\) avoids \(p\), and permutation \(j\) itself avoids \(p\). Because the forbidden factor has length three and every block has length three, every occurrence lies entirely within one block or crosses exactly one adjacent block boundary. Therefore, for every integer \(k\ge1\),

\[a_p(k)=v_pT_p^{k-1}\mathbf1,\qquad F_p(z)=zv_p(I-zT_p)^{-1}\mathbf1.\]

Here the all-ones column \(\mathbf1\) has six entries. To make the transfer completely explicit, write each row of a matrix as a six-character zero-one string, with columns in the displayed permutation order:

| Pattern | \(v_p\) | Rows of \(T_p\) |
|---|---|---|
| `000` | `111111` | `111111 111111 111111 111111 111111 111111` |
| `001` | `111111` | `111111 111111 111111 011111 111111 011111` |
| `010` | `111111` | `111111 111111 111111 110111 001111 110111` |
| `012` | `011111` | `000000 011111 011111 011011 011100 011011` |

**Step 3: Rational-function evaluation.** Put \(M_p=I-zT_p\). The polynomial determinant identity \(\det(M_p+\mathbf1 v_p)=\det(M_p)+v_p\operatorname{adj}(M_p)\mathbf1\) gives the rational generating function without numerical extrapolation. Expanding the six-by-six determinants yields these exact polynomial pairs:

| \(p\) | \(\det(M_p)\) | \(z(\det(M_p+\mathbf1v_p)-\det(M_p))\) |
|---|---|---|
| `000` | \(1-6z\) | \(6z\) |
| `001` | \(1-6z+2z^2\) | \(6z-2z^2\) |
| `010` | \(1-6z+4z^2\) | \(6z-4z^2\) |
| `012` | \(1-3z-5z^2-2z^3\) | \(5z+6z^2+2z^3\) |

The complete integer-arithmetic determinant expansion is reproduced in `verification.py`; the identity is a finite symbolic computation of explicit matrices, and therefore establishes the generating functions for **every** \(k\), rather than only for tested coefficients.

**Step 4: Exhaustion of forbidden trigram types.** A length-three word has either one distinct symbol (`000`), exactly two equal adjacent symbols (`001`, including its reversals/relabelings), equal first and third symbols (`010`), or three distinct symbols (`012`). These alternatives are exhaustive, and any two patterns in one alternative are equivalent under alphabet relabeling and reversal. Such transformations map the shortest-universal set bijectively to itself and preserve contiguous avoidance. The four displayed generating functions are pairwise distinct (already at \(k=2\), except for the `012` type which differs at \(k=1\)), completing the classification.

**Step 5: Growth-rate separation.** All allowed transition graphs, restricted to states reachable from a permitted initial permutation, are primitive: a common permitted state is accessible from every allowed state, has a self-loop, and reaches every allowed state. Perron–Frobenius theory therefore identifies the exponential base with the unique dominant positive eigenvalue. The three nontrivial denominator polynomials give bases \(3+\sqrt7\), \(3+\sqrt5\), and the positive root of the stated cubic. The cubic is negative at \(4\), positive at \(5\), and has exactly one positive root by Descartes' rule of signs. Hence this last base is strictly below \(5\), whereas \(3+\sqrt5>5\); the four bases are strictly ordered.

## Verification

Run `python verification.py` in a directory containing that standalone Python 3 file. It uses only the Python standard library. It constructs each transfer matrix directly from the definition, computes both determinant polynomials by exact integer polynomial arithmetic over all six-column permutations, and checks the claimed numerator and denominator coefficients. It then verifies each of the first 30 coefficients of each rational function against repeated matrix multiplication, and independently enumerates all \(3^3+3^6+3^9=20{,}439\) ternary words of lengths three, six, and nine by literal scattered-subsequence tests. This also checks the 81 pattern-count comparisons for all \(27\) trigrams and \(k\in\{1,2,3\}\).

## Relationship to prior work

Adamson's 2023 ranking/unranking and unrestricted-counting work develops algorithms for \(k\)-subsequence-universal words and the arch decomposition. Adamson–Fleischmann–Huch–Koß–Manea–Nowotka (2023) gives a general DFA-based algorithm for counting \(k\)-universal words subject to any regular-language constraint. A language avoiding one fixed contiguous trigram is regular, so that algorithm can compute each individual number in this result; it does not supply these four symbolic generating functions or the classification of forbidden trigrams. Barker et al. (2020) establishes foundational universality and arch properties but does not provide this restricted enumeration.

The integer sequences for the `001` and `010` rows coincide, after indexing alignment, with OEIS A154244 and A084326 respectively. This finding does **not** assert those sequences or their recurrences were previously unknown; the claimed contribution is their joint interpretation and complete four-type classification for the specified word family. No inspected source supplied an exact table for this restricted family. The possibility of an unindexed equivalent specialization remains open.

## Limitations

The result is restricted to a single fixed forbidden trigram in a shortest ternary subsequence-universal word. It neither characterizes arbitrary-length universal words under forbidden-factor constraints nor supplies a general-alphabet formula. Prior algorithms already compute arbitrary fixed cases, and some numerical sequences predate this application. No independent audit is claimed.

## References

1. Duncan Adamson, *Ranking and Unranking k-Subsequence Universal Words*, arXiv:2304.04583, first posted 2023-04-10, https://arxiv.org/abs/2304.04583.
2. Duncan Adamson, Pamela Fleischmann, Annika Huch, Tore Koß, Florin Manea, Dirk Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658, first posted 2023-11-17, https://arxiv.org/abs/2311.10658.
3. Laura Barker, Pamela Fleischmann, Katharina Harwardt, Florin Manea, Dirk Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629, 2020-03-10, https://arxiv.org/html/2003.04629v1.
4. The On-Line Encyclopedia of Integer Sequences, A154244 and A084326, https://oeis.org/A154244 and https://oeis.org/A084326.
