# Exact scattered \(\mathtt{abbab}\) avoidance in every binary Parikh-matrix class

## Finding

Let \(A,B\) be nonnegative integers and \(0\le C\le AB\). For a binary word \(u\) on the ordered alphabet \(\{a,b\}\), write \(|u|_a\), \(|u|_b\) for its letter counts and \(\binom{u}{ab}\) for its number of scattered \(ab\) subsequences. Define the nonempty binary Parikh-matrix class
\[
L_{A,B,C}=\bigl\{u:|u|_a=A,\ |u|_b=B,\ \binom{u}{ab}=C\bigr\}.
\]
Let \(N(A,B,C)\) denote the number of words in this class *avoiding* the scattered pattern \(\mathtt{abbab}\) (also written \(\mathtt{01101}\) under \(a=0,b=1\)). Then, for all indicated parameters,
\[
\boxed{N(A,B,C)=\begin{cases}
1,&C=0,\\[2pt]
\min(A,C)-\left\lceil C/B\right\rceil+1,&1\le C\le AB.
\end{cases}}
\tag{1}
\]
In particular \(N(A,B,C)\ge1\): no nonempty binary Parikh-matrix class forces this particular five-letter scattered pattern.

For fixed \(A,B\ge1\), the *complete inversion-refined avoidance polynomial* is
\[
\boxed{F_{A,B}(z)=\sum_{C=0}^{AB}N(A,B,C)z^C
=1+\sum_{r=1}^{A}\sum_{c=r}^{rB}z^c
=1+\frac{1}{1-z}\sum_{r=1}^{A}\bigl(z^r-z^{rB+1}\bigr).}
\tag{2}
\]
The final quotient is interpreted by its finite polynomial expansion. If \(A=0\) or \(B=0\), \(F_{A,B}(z)=1\).

For \(A,B\ge1\), the total number of avoiders and the sharp largest single-class avoidance count are
\[
\boxed{\sum_{C=0}^{AB}N(A,B,C)=1+A+\frac{(B-1)A(A+1)}2,}
\qquad
\boxed{\max_{0\le C\le AB}N(A,B,C)=A-\left\lceil A/B\right\rceil+1,}
\tag{3}
\]
with the maximum attained at \(C=A\). For \(A=0\) or \(B=0\), both counts are one.

Because the class size is the Gaussian-binomial coefficient
\[
|L_{A,B,C}|=[z^C]\begin{bmatrix}A+B\\A\end{bmatrix}_z,
\]
the exact probability that a uniformly sampled class member *contains* \(\mathtt{abbab}\) is
\[
\boxed{\Pr(\mathtt{abbab}\preceq U\mid U\in L_{A,B,C})
=1-\frac{N(A,B,C)}{[z^C]\begin{bmatrix}A+B\\A\end{bmatrix}_z}.}
\tag{4}
\]
For example, \((A,B,C)=(4,4,8)\) gives three avoiding words among eight class members, so the containment probability is \(5/8\). For \(1\le C\le\min(A,B)\), the avoiding count is exactly \(C\).

## Assumptions and scope

All words are finite, **linear**, and over the labeled alphabet \(\{a,b\}\). Embeddings are scattered subsequences; the five letters need not be adjacent. Distinct words are counted separately, but different embeddings of the same pattern in one word do not increase its weight. Parameters \(A,B,C\) are integers, \(A,B\ge0\), \(0\le C\le AB\). The boundary cases with a zero letter count have a single word and \(C=0\). The word of length zero is included. All probabilities condition on a nonempty class, as guaranteed by the range of \(C\).

## Proof

**1. The exact partition encoding.** Assume \(A\ge1\). Label the \(a\)'s in a word \(u\) from left to right. For each \(1\le i\le A\), let \(\lambda_i\) be the number of \(b\)'s *after* the \(i\)-th \(a\). This yields a weakly decreasing integer sequence
\[
B\ge\lambda_1\ge\cdots\ge\lambda_A\ge0,
\qquad \sum_{i=1}^{A}\lambda_i=\binom{u}{ab}=C.
\tag{5}
\]
Conversely, given such a sequence, the word is uniquely recovered as
\[
u=b^{B-\lambda_1}a\,b^{\lambda_1-\lambda_2}a\cdots
b^{\lambda_{A-1}-\lambda_A}a\,b^{\lambda_A}.
\tag{6}
\]
Here \(B-\lambda_1\) counts the initial \(b\)'s, and successive differences count the internal gaps. Hence words in \(L_{A,B,C}\) are in bijection with partitions of area \(C\) in the \(A\)-by-\(B\) rectangle. In particular their number is the Gaussian coefficient appearing in (4).

**2. Exact containment criterion.** An embedding of \(\mathtt{abbab}\) chooses two copies of \(a\), indexed \(i<j\), with at least two \(b\)'s between them and at least one \(b\) after the second. The first number is \(\lambda_i-\lambda_j\), and the second is \(\lambda_j\). Therefore
\[
\mathtt{abbab}\preceq u
\quad\Longleftrightarrow\quad
\exists\,1\le i<j\le A:\ \lambda_i-\lambda_j\ge2\ \text{and}\ \lambda_j\ge1.
\tag{7}
\]
If \(C>0\), let \(r\) be the number of positive parts. All positive parts are the initial segment \(\lambda_1,\dots,\lambda_r\). If \(r=1\), the pattern is absent. If \(r\ge2\), monotonicity makes the maximum difference between two positive parts precisely \(\lambda_1-\lambda_r\). Equation (7) therefore says that \(u\) avoids the pattern **if and only if** the positive parts differ by at most one:
\[
\boxed{\lambda_1-\lambda_r\le1.}
\tag{8}
\]
The equivalence remains valid for \(r=1\), with difference zero.

**3. One avoider per feasible positive-part count.** Fix \(C>0\) and \(r\ge1\). A nonincreasing partition of area \(C\) with exactly \(r\) positive parts satisfying (8) is uniquely determined: if \(C=qr+t\) with \(q=\lfloor C/r\rfloor\), \(0\le t<r\), then the first \(t\) positive parts are \(q+1\), the remaining \(r-t\) equal \(q\), and all later parts are zero. Positivity and the rectangle constraint are equivalent to
\[
1\le r\le\min(A,C),\qquad
\left\lceil C/r\right\rceil\le B.
\tag{9}
\]
For positive \(B\), the last condition is exactly \(r\ge\lceil C/B\rceil\). Thus the valid integers \(r\) constitute the interval
\[
\left\lceil C/B\right\rceil\le r\le\min(A,C),
\]
whose length is formula (1). The interval is nonempty because \(C\le AB\) and \(B\ge1\). When \(C=0\), the only partition is the all-zero partition, corresponding to \(b^Ba^A\) (including degenerate cases), which avoids the pattern. This proves (1) including every boundary.

**4. Generating polynomial, extremum, and probability.** For each positive-part count \(r\in\{1,\ldots,A\}\), the balanced partitions have precisely one representative at each area \(c=r,r+1,\ldots,rB\), yielding (2) by reversing the two finite summations. Evaluation at \(z=1\) gives
\[
1+\sum_{r=1}^{A}(rB-r+1)
=1+A+(B-1)A(A+1)/2.
\]
On \(1\le C\le A\), the expression \(C-\lceil C/B\rceil+1\) is nondecreasing in \(C\); on \(A\le C\le AB\), the expression \(A-\lceil C/B\rceil+1\) is nonincreasing. Thus the maximum occurs at \(C=A\), with value (3). Finally the ordinary bounded-partition enumerator gives the denominator in (4), so counting avoidance as the complement of containment gives the stated probability. All identities hold for arbitrary valid parameters, not just the verified finite cases.

## Verification

Two standalone Python scripts are supplied. Run `python3 check_bruteforce.py` and `python3 check_dynamic.py` with standard Python 3, without third-party packages.

The first enumerates all \(48{,}619\) binary words across the \(81\) letter-count pairs \(0\le A,B\le8\), detects the five-letter scattered pattern by an explicit greedy scan, directly accumulates \(ab\)-pairs, and verifies (1) in \(1{,}377\) nonempty Parikh classes. It prints `BRUTEFORCE_OK words 48619 classes 1377`.

The second independently counts labeled paths in a six-state greedy pattern automaton, tracking letter counts and exact \(ab\) count during word extension, and separately computes all class sizes by a Gaussian recurrence. For all \(169\) compositions \(0\le A,B\le12\), it checks (1), the Gaussian denominator, the total, and the maximum in \(6{,}253\) classes. It prints `DYNAMIC_OK classes 6253 compositions 169`.

Both tests were run and passed on the delivered source text. Their finite scope is not substituted for the unbounded combinatorial proof.

## Relationship to prior work

Fazekas, Huang, and Mercaş (first public manuscript dated 2026-10-05) introduced fixed-subsequence containment probabilities in binary Parikh-matrix languages. Their full manuscript proves a general additive approximation scheme and a factoring-related obstruction for the different pattern \(\mathtt{abab}\); it does **not** give (1)–(4) for \(\mathtt{abbab}\). The present result determines an exact closed numerator and probability for one nontrivial five-letter pattern, and shows that this pattern is avoidable in every class, in contrast with the harder divisibility structure of \(\mathtt{abab}\).

Richomme (first public preprint 2025-10-08) develops the rectangle-partition correspondence, which is explicitly used as known background here; the new step is criterion (7) and its balanced-positive-part enumeration. The published inversion-refined classification of all six balanced length-four scattered patterns includes a divisor-type formula for \(\mathtt{abab}\), but its hypotheses and conclusions do not enumerate avoidance of the five-letter pattern here. The published sandwich-subsequence counts for patterns \(ab^t a\) likewise lack the required final \(b\); they do not imply the positive-parts condition (8) or the explicit count (1). All comparisons are by mathematical coverage, rather than wording alone.

## Limitations

The result addresses only one fixed five-letter scattered pattern and the binary alphabet. It does not claim exact simple formulas for arbitrary five-letter patterns or arbitrary larger alphabets. The denominator in (4) is a Gaussian-binomial coefficient; (4) gives an exact rational probability, not a claim that evaluating the denominator for huge binary-encoded parameters has bitlength-polynomial complexity. The partition bijection, general approximation scheme, and shorter-pattern enumerations are established background, not claimed as new. An unindexed equivalent enumeration could exist; no independent external audit or mathematical priority certification has been performed.

## References

1. S. Z. Fazekas, X. Huang, and R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717, first public 2026-10-05, https://arxiv.org/abs/2610.06717.
2. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159, first public 2025-10-08, https://arxiv.org/abs/2510.07159.
3. *Inversion-refined avoidance spectra for all balanced four-letter scattered patterns*, published 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-inversion-refined-avoidance-spectra-for-all-balanced-four-letter--e75590ea1e11/RESULT.md.
4. *Exact sandwich-subsequence profiles within binary Parikh-matrix classes*, published 2026-11-02, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-sandwich-subsequence-profiles-within-binary-parikh-matrix--b40371a80999/RESULT.md.
5. *Exact Parikh-class avoidance of two-ended runs and the sharp five-letter extremum*, published 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-parikh-class-avoidance-of-two-ended-runs-and-the-sharp-fiv--3ca5f597072a/RESULT.md.
