# Fourth-order Fourier sampling ranks distinguish all five abelian groups of order sixteen

## Finding
Let \(G\) range over all abelian groups of order \(16\), and choose the unnormalized character table \(F_G=(\chi_b(a))_{a,b\in G}\). For every pair of **unordered four-element subsets** \(A,B\subset G\), take the complex rank of \(F_G[A,B]\). All \(\binom{16}{4}^2=3{,}312{,}400\) row/column pairs are counted for each group, without restricting to principal or orthogonal submatrices.

The complete rank distribution is:

| Group \(G\) | rank 1 | rank 2 | rank 3 | rank 4 |
| --- | ---: | ---: | ---: | ---: |
| \(C_{16}\) | 16 | 9,728 | 293,888 | 3,008,768 |
| \(C_8\times C_2\) | 48 | 26,592 | 719,872 | 2,565,888 |
| \(C_4\times C_4\) | 112 | 34,464 | 979,968 | 2,297,856 |
| \(C_4\times C_2\times C_2\) | 176 | 58,464 | 1,201,152 | 2,052,608 |
| \(C_2^4\) | 560 | 104,160 | 1,612,800 | 1,594,880 |

Every row sums to \(3{,}312{,}400\). The rank-four totals, and indeed the rank-one totals, are pairwise distinct. Thus the distribution of ranks of fourth-order Fourier restrictions determines the **isomorphism type** of any abelian group of order sixteen. The three intermediate cases \(C_8\times C_2\), \(C_4\times C_4\), and \(C_4\times C_2^2\) supplement the previously available endpoint classifications for \(C_{16}\) and \(C_2^4\).

## Assumptions and scope
Use the fundamental classification of finite abelian groups to write \(G=\prod_j C_{n_j}\), with \(n_j\) powers of two and \(\prod_jn_j=16\). Indices \(a=(a_j)\), \(b=(b_j)\) are represented in the corresponding residue rings. With \(\zeta=e^{2\pi i/16}\), the chosen Fourier matrix is
\[
F_G(a,b)=\zeta^{\sum_j (16/n_j)a_jb_j}.
\]
Relabeling group elements or characters only permutes rows or columns and does not change the rank counts. All ranks are taken over \(\mathbb C\); reduction modulo a prime is used only as an exact rank **certificate**, not as a replacement for complex rank.

## Proof
**1. Exhaustive finite domain.** The five displayed groups exhaust the abelian groups of order sixteen. Each has \(\binom{16}{4}=1{,}820\) unordered row sets and the same number of unordered column sets. The source programs generate all quadruples in increasing element-index order and compute the bilinear exponents in the displayed Fourier formula.

**2. Exact cyclotomic rank test.** Let \(D\) be any \(k\)-by-\(k\) minor with \(1\le k\le4\). Its determinant is a signed sum of at most \(k!\) sixteenth roots of unity. Since \(\zeta^8=-1\), it has the unique canonical expansion
\[
D=\sum_{j=0}^{7}c_j\zeta^j,\qquad c_j\in\mathbb Z,\quad |c_j|\le k!\le24.
\]
Here \(\mathbb Q(\zeta)\) has degree eight, so \(D=0\) precisely when all coefficients vanish. The first verifier computes all coefficients with signed permutation expansion and makes the rank decision by testing all nested minor sizes. Consequently its decisions are exact over \(\mathbb C\), with no floating-point thresholds or probabilistic tests.

**3. Independent finite-field certificate.** The multiplicative group of \(\mathbb F_{97}\) has order \(96\). The element \(8\) has order \(16\), and its eight odd powers are the distinct primitive sixteenth roots of \(X^8+1\). Reduce each determinant polynomial \(\sum_{j=0}^{7}c_jX^j\) modulo \(97\) and evaluate it at all these roots. A polynomial of degree at most seven vanishes at all eight distinct roots only if all coefficients vanish modulo \(97\). Because \(|c_j|\le24<97\), this is equivalent to the original determinant vanishing. Therefore
\[
\operatorname{rank}_{\mathbb C}F_G[A,B]
=\max_{u\in\mathbb F_{97}:\,\operatorname{ord}(u)=16}
\operatorname{rank}_{\mathbb F_{97}} (u^{\sum_j(16/n_j)a_jb_j})_{a\in A,b\in B}.
\]
The second verifier performs Gaussian elimination for these images. It may stop the eight-root loop as soon as full rank is seen. The stopping rule cannot misclassify a singular minor.

**4. Sound reduction of row cases.** Translating \(A\) by \(t\in G\) multiplies column \(b\) by the nonzero scalar \(\chi_b(t)\), so ranks are invariant. The first two verifiers partition the \(1{,}820\) row sets into translation orbits, select the least sixteen-bit mask in each orbit as representative, count the orbit's distinct translates, and weight the enumeration of all \(1{,}820\) column sets by that size. The orbit counts for the five groups in table order are respectively \(116,120,122,128,140\). The third verifier omits this reduction and directly visits all \(3{,}312{,}400\) row/column pairs for each group.

**5. Computed exact totals.** All three verifiers produce precisely the five rank rows stated in the Finding. The direct cyclotomic and modular rank methods agree, as do translated and unreduced enumerations. Their algorithms visit the entire finite domain, and the preceding algebra proves each arithmetic decision agrees with complex rank. This establishes every claimed count and the isomorphism-class distinguishing consequence.

## Verification
The accompanying standalone, standard C++17 files are `checks/fourier16_exact.cpp`, `checks/fourier16_mod97.cpp`, and `checks/fourier16_unreduced.cpp`. Compile any with `g++ -O3 -std=c++17` and run its executable. Each prints the five groups, the four rank counts, and (in the modular implementations) the total number of pairs. The finite computation inputs are determined entirely by the displayed five invariant-factor lists; there are no hidden tables or external dependencies. `data/rank_counts.tsv` gives the expected result. The exact cyclotomic, finite-field/orbit, and finite-field/unreduced executions all completed and agreed on each rank count. The count for each group is independently checked to sum to \(\binom{16}{4}^2\).

## Relationship to prior work
Meshulam's finite-abelian uncertainty inequality supplies a bound on cardinalities of Fourier support; it does not count ranks of specified four-point sampling restrictions. Bella, Olshevsky, and Sakhnovich analyze the binary ranks of Hadamard **exponent** matrices and their pseudo-noise representations, not this complex-rank incidence table. Kolountzakis and Matolcsi classify small **orthogonal** Fourier character configurations in their spectral-set arguments, whereas invertible four-row/four-column restrictions need not be orthogonal. The previously available cyclic-sixteen and Boolean-sixteen fourth-order rank classifications establish the first and last rows, but no implication from these endpoints fixes the other three group types. The claim here is the complete order-sixteen comparison and its separating rank fingerprint, not priority over either endpoint result.

## Limitations
Only abelian groups of order sixteen and fourth-order restrictions are classified. The table does not prove monotonicity for larger powers of two, enumerate all possible determinant magnitudes, or classify nonabelian character tables. The claim is a finite complete classification supported by executable exact arithmetic, not a general infinite-family theorem. Priority is subject to a bounded historical source comparison; an unlocated comprehensive Fourier-minor database or stronger theorem could supersede the contribution. No independent mathematical audit has been performed.

## References
1. Roy Meshulam, *An uncertainty inequality for finite abelian groups*, arXiv:math/0312407 (first made public 22 December 2003); European Journal of Combinatorics 27 (2006), 63–67.
2. Mihail N. Kolountzakis and Máté Matolcsi, *Complex Hadamard matrices and the Spectral Set Conjecture*, arXiv:math/0411512 (first made public 23 November 2004).
3. Tom Bella, Vadim Olshevsky, and Lev Sakhnovich, *Ranks of Hadamard Matrices and Equivalence of Sylvester–Hadamard and Pseudo-Noise Matrices*, Operator Theory: Advances and Applications 179 (2007), 35–46, DOI: 10.1007/978-3-7643-8539-2_3.
