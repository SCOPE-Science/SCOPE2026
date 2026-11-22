# A central anti-unimodality notch for balanced near-maximal subsequence universality

## Finding
For every integer \(k\ge4\), let \(\mathcal U_k\) be the binary words with exactly \(k+1\) zeros, exactly \(k+1\) ones, and all \(2^k\) binary length-\(k\) words as scattered subsequences. Write \(C(w)\) for the number of ordered index pairs carrying `01`, and define \(F_k(z)=\sum_{w\in\mathcal U_k}z^{C(w)}\). Put \(b_k=\binom{k}{2}\). Then the complete exact Parikh-class enumerator is
\[
\boxed{\begin{aligned}
F_k(z)={}&z^{\binom{k+1}{2}}(1+z)^{k+1}\\
&+z^{b_k}(1+z)^{k-1}\sum_{j=0}^{k-1}\left(z^j+z^{2k+2-j}\right)\\
&+z^{b_k}(1+z)^{k-2}\sum_{d=1}^{k-1}(k-d)\left(z^{k-d+1}+z^{k+d+2}\right).
\end{aligned}}
\]
All coefficients count **distinct indexed binary words**, not embeddings of a pattern. In particular,
\[
F_k(1)=2^{k-2}(k^2+3k+8),\qquad
z^{(k+1)^2}F_k(z^{-1})=F_k(z),
\]
and the exact coefficient support is the uninterrupted interval \(b_k\le C\le(k+1)^2-b_k\).

**Persistent central notch.** Write \(N_k(C)=[z^C]F_k(z)\) and \(c_k=\lfloor(k+1)^2/2\rfloor\). For odd \(k=2m+1\), \(m\ge1\),
\[
\boxed{N_k(c_k-1)-N_k(c_k)=\binom{2m}{m}\frac{3m-1}{2(m+1)}>0.}
\]
For even \(k=2m\), \(m\ge2\),
\[
\boxed{N_k(c_k-1)-N_k(c_k)=\binom{2m}{m}\frac{3(m-1)}{2(m+1)}>0.}
\]
Therefore **the full coefficient sequence is not unimodal for every \(k\ge4\)**: a strict drop immediately before the center must be followed by a rise by reciprocity. The formula also holds at the smaller parameters, but only the uniform \(k\ge4\) result and the all-order notch are asserted as new; the entire \(k=3\) fixed-fiber problem is already covered by an earlier classification.

## Assumptions and scope
The ambient alphabet is the ordered set \(\{0,1\}\). A scattered subsequence retains relative positions, without requiring adjacency. A word is \(k\)-universal if **every** binary word of length \(k\) is a scattered subsequence. The integer \(C(w)\) is the number of distinct index pairs \((i,j)\) with \(i<j\), \(w_i=0\), and \(w_j=1\); it is not the number of occurrences of the contiguous factor `01`. All polynomials are ordinary generating polynomials in a formal variable \(z\). The scope is all integers \(k\ge4\) and the exact balanced composition \((k+1,k+1)\) at total length \(2k+2\). No randomness assumption is needed: dividing a coefficient by the Gaussian binomial coefficient at \(C\) yields the corresponding conditional proportion in a binary Parikh-matrix class.

## Proof
**1. Greedy arches and the exhaustive small-surplus trichotomy.** Greedily remove the shortest remaining prefix containing both binary letters; stop with an empty or monochromatic suffix. Such a complete *arch* has the unique form \(0^r1\) or \(1^r0\), with \(r\ge1\). The number of complete arches equals the subsequence-universality index: selecting one letter from each arch realizes every equally long target, while a target formed from the successive terminal letters and then the letter absent from the suffix fails greedy subsequence matching. This is the standard binary arch characterization.

Every arch needs two positions. A balanced length-\(2k+2\) word with at least \(k\) arches therefore has either \(k\) or \(k+1\) arches. The excess length beyond \(k\) length-two arches is only two. With \(k+1\) arches, every arch has length two and the suffix is empty (family A). With exactly \(k\) arches, balance rules out either a single length-four arch, whose two extra symbols agree, or a two-letter monochromatic suffix. The only possibilities are one length-three arch followed by a one-letter suffix of the opposite repeated symbol (family B), or two length-three arches with opposite repeated symbols and no suffix (family C). A length-three arch is necessarily `001` or `110`. These possibilities are disjoint and exhaust all admissible words. Every described word has at least \(k\) greedy arches.

**2. The three independent enumerators.** For a collection of \(r\) ordinary two-letter arches (`01` or `10`), every earlier arch provides exactly one zero before the one in every later arch. Thus the inter-arch \(01\) count is \(\binom r2\), while each `01` arch contributes one additional internal pair. Family A consequently has polynomial
\[
A_k(z)=z^{\binom{k+1}{2}}(1+z)^{k+1}.
\]
For family B put the exceptional length-three arch at position \(j\in\{1,\ldots,k\}\). Relative to the baseline \(b_k\) from \(k\) ordinary arches, a `110` arch followed by terminal `0` contributes exactly \(j-1\) extra pairs: its extra one sees the \(j-1\) earlier zeros. A `001` arch followed by terminal `1` contributes exactly \(2k-j+3\) extra pairs: one internal pair, \(k-j+1\) pairs from its extra zero, and \(k+1\) pairs from the terminal one. The other \(k-1\) ordinary arch choices contribute \((1+z)^{k-1}\). Replacing \(j-1\) by \(h\in\{0,\ldots,k-1\}\) yields
\[
B_k(z)=z^{b_k}(1+z)^{k-1}\sum_{h=0}^{k-1}(z^h+z^{2k+2-h}).
\]
For family C let the two exceptional arches occupy positions \(i<j\) and put \(d=j-i\). If the earlier exceptional arch is `110` and the later is `001`, the extra one contributes \(i-1\) pairs and the later `001` adds \(k-j+2\) pairs, a total \(k-d+1\) above \(b_k\). In the opposite order the extra zero in `001` contributes \(k-i+1\) pairs and its ordinary internal pair contributes one; the extra one in the later `110` sees \(j\) preceding zeros, for a total \(k+d+2\). There are \(k-d\) choices of \(i\) at fixed \(d\), and \(k-2\) remaining ordinary arches. Hence
\[
C_k(z)=z^{b_k}(1+z)^{k-2}\sum_{d=1}^{k-1}(k-d)(z^{k-d+1}+z^{k+d+2}).
\]
Adding \(A_k+B_k+C_k\) proves the displayed polynomial. Substituting \(z=1\) gives the total \(2^{k+1}+k2^k+\binom{k}{2}2^{k-1}=2^{k-2}(k^2+3k+8)\).

**3. Symmetry and support.** Reversing a word preserves its letter counts and subsequence-universality index. Its \(01\) count becomes \((k+1)^2-C(w)\), giving the reciprocity. The least exponent in the formula is \(b_k\) (the first low term of \(B_k\)); the greatest follows by reciprocity. The low block \((1+z)^{k-1}\sum_{h=0}^{k-1}z^h\), the middle block \(z^k(1+z)^{k+1}\) relative to \(b_k\), and the reciprocal high block overlap or touch for every \(k\ge2\). They cover every integer between these extrema with a strictly positive coefficient.

**4. Exact central coefficient difference.** For \(r\in\mathbb Z\) adopt \(\binom nr=0\) outside \(0\le r\le n\). Let \(\Delta_X=[z^{c_k-1}]X_k(z)-[z^{c_k}]X_k(z)\), for \(X=A,B,C\). For odd \(k=2m+1\), the exponent \(c_k-b_k\) is \(3m+2\); for even \(k=2m\), it is \(3m\). Expanding the three binomial factors, cancelling adjacent coefficient ranges and simplifying gives the following exact table, with \(H_m=\binom{2m}{m}\):

| Contribution divided by \(H_m\) | \(k=2m+1\) | \(k=2m\) |
|---|---:|---:|
| \(\Delta_A/H_m\) | \(-2(2m+1)/((m+1)(m+2))\) | \(-2(2m+1)/((m+1)(m+2))\) |
| \(\Delta_B/H_m\) | \(3m/((m+1)(m+2))\) | \(3m/((m+1)(m+2))\) |
| \(\Delta_C/H_m\) | \((3m+1)/(2(m+1))\) | \((3m-1)/(2(m+1))\) |

For a fully explicit algebraic reduction of the nontrivial entries, the \(B\)-differences are, respectively,
\[
\binom{2m}{m+1}-\binom{2m}{m-2},\qquad
\binom{2m-1}{m}-\binom{2m-1}{m-3}.
\]
For the \(C\)-differences they are, respectively,
\[
2m\binom{2m-1}{m}-(2m+1)\binom{2m-1}{m-2},
\]
\[
(2m-1)\binom{2m-2}{m-1}-2m\binom{2m-2}{m-3}-\binom{2m-2}{m-2}.
\]
These equalities follow from the finite-gap weighted sum after applying
\[
\sum_{d=1}^{r}(r+1-d)(f_d-f_{d+1})=r f_1-\sum_{d=2}^{r+1}f_d
\]
(where the last indexed value is zero in the present applications), together with \(\binom n t=\binom n{n-t}\), then elementary adjacent-binomial ratios. The \(A\)-difference is simply the difference of two consecutive coefficients in \((1+z)^{k+1}\). This supplies finite algebraic certificates of all table entries, rather than reliance on numerical observations. Summing each column produces
\[
\Delta_F=\begin{cases}
H_m(3m-1)/(2(m+1)), &k=2m+1,\\
H_m\,3(m-1)/(2(m+1)), &k=2m.
\end{cases}
\]
Both are strictly positive in the claimed \(k\ge4\) range. Reciprocity forces the coefficients to increase again after this central dip, proving nonunimodality. \(\square\)

## Verification
The standalone `verify_arch_and_polynomial.py` independently exhausts all fixed-balanced words for \(1\le k\le7\), computes greedy arches directly, computes each \(01\) pair count, and compares the exact histogram with the three-sum polynomial. It also checks the strict support, reciprocity, aggregate count, and the closed central-gap identity for every integer \(2\le k\le100\). Its recorded output ends `VERIFY_OK arch_vs_polynomial_k1_to7=7 central_identity_k2_to100=99`.

The separate `verify_direct_subsequences.py` does not use greedy arches to classify the words: for each balanced word and each \(1\le k\le6\) it searches for **every** length-\(k\) binary subsequence using direct subsequence matching, computes the \(01\) count independently, and compares the exact histogram with the formula. It tests 4,704 fixed-composition words across six complete parameter cases and prints `VERIFY_OK independent_semantic_cases=4704`. These finite checks are not proofs of the assertions for unrestricted \(k\); Steps 1–4 establish those assertions.

## Relationship to prior work
Fazekas, Huang and Mercaş [1] (first public October 5, 2026) characterize existence and universal validity of subsequence universality within binary Parikh-matrix classes, and give an additive approximation scheme for fixed-pattern containment probabilities. Their full text does not supply the exact \(01\)-count distribution for balanced, two-surplus-letter near-maximal universality, or a central nonunimodality law. Barker et al. [2] establish the arch framework; arch factorization alone does not imply the three-branch weighted polynomial without the balance and \(01\)-pair analysis.

A prior fixed-composition polynomial [3] concerns \((k+1,k)\), where one symbol is saturated at the universality index and the polynomial is unimodal. The more general saturated-symbol product [4] also assumes that **one** symbol occurs exactly \(k\) times; here *both* multiplicities exceed \(k\). Thus neither product includes the claimed two-surplus regime, and the change from unimodality to a persistent central dip is substantive. A prior balanced unweighted index distribution [5] **already implies the total number** of words at index at least \(k\), so the numerical total \(F_k(1)\) is given for comparison and is not claimed as independently new. A general finite-per-fiber classification at universality order three [6] **already covers every instance with \(k=3\)**, including its central dip; the novelty claim is limited to the uniform all-parameter formula and nonunimodality for \(k\ge4\). The minimal one-deletion-resilient characterization [7] describes the \(k+1\)-arch subfamily, not either of the other two enumerated arch families. A general Parikh-class inversion enumerator and pattern-avoidance results address different marginals and cannot alone give this constrained polynomial. Unindexed equivalent formulas remain a historical-priority risk.

## Limitations
The results are restricted to the ordered binary alphabet, exact equal content \(k+1\) of each symbol, and the two-surplus-letter length \(2k+2\). They do not assert unimodality properties away from the center, or generalize the three-branch formula to three or more surplus symbols. Earlier results cover the aggregate count and the fixed \(k=3\) instance, so neither is presented as a novel theorem. Independent review has not been performed. The literature comparison is detailed but cannot exclude all differently phrased or unindexed prior work.

## References
1. S. Z. Fazekas, X. Huang and R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717v1, first public 2026-10-05, https://arxiv.org/abs/2610.06717.
2. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629, first public 2020-03-10, https://arxiv.org/abs/2003.04629.
3. *A sharp \(01\)-subsequence enumerator for near-shortest binary universal words*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-01-subsequence-enumerator-for-near-shortest-binary-unive--2a5245b16b63.
4. *Exact Parikh-pair distribution of maximally subsequence-universal binary words*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-parikh-pair-distribution-of-maximally-subsequence-universa--5c8faf99c146.
5. *Balanced binary words: exact subsequence-universality spectrum and a Gaussian law*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-balanced-binary-words-exact-subsequence-universality-spectrum-an--307f63e05203.
6. *Exact binary three-subsequence universality counts in every Parikh-matrix class*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-binary-three-subsequence-universality-counts-in-every-pari--561fd2881a94.
7. *One-deletion resilience forces permutation blocks in shortest universal words*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-one-deletion-resilience-forces-permutation-blocks-in-shortest-un--781682eefd3f.
