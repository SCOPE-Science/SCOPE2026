# Exact subsequence-universality distribution of reverse-complement symmetric words

## Finding
Let \(q=2m\ge 2\), let \(\Sigma\) be a labeled alphabet of size \(q\), and let \(\theta:\Sigma\to\Sigma\) be a fixed-point-free involution. For \(v\in\Sigma^n\), put \(W_\theta(v)=v\theta(v^R)\), where \(v^R\) is reversal and \(\theta\) acts letterwise. Let \(\iota(w)\) be the largest \(j\ge0\) for which every word in \(\Sigma^j\) occurs as a (not necessarily contiguous) subsequence of \(w\). Define
\[
c_q(n,j)=\#\{v\in\Sigma^n:\iota(W_\theta(v))=j\}.
\]
This count is independent of the choice of fixed-point-free involution. Define the rational functions
\[
B_s(z)=\frac{s!z^s}{\prod_{h=1}^{s}(1-hz)},\qquad B_0(z)=1,
\]
\[
A_q(z)=\frac{q!z^q}{\prod_{h=1}^{q-1}(1-hz)},\qquad
T_q(z)=\sum_{s=0}^{q-1}\binom qs B_s(z),
\]
and
\[
R_q(z)=\sum_{s=m}^{q-1}\binom m{s-m}2^{q-s}B_s(z).
\]
Then the **complete exact length-index distribution** of reverse-complement symmetric words is
\[
\boxed{\sum_{n,j\ge0}c_q(n,j)z^nu^j
=\frac{T_q(z)+(u-1)R_q(z)}{1-u^2A_q(z)}.}
\]
The variable \(z\) records the *half-length*: the corresponding word \(W_\theta(v)\) has length \(2n\). In the four-letter case, including the Watson–Crick involution on the DNA alphabet, this simplifies to
\[
\boxed{\sum_{n,j\ge0}c_4(n,j)z^nu^j=
\frac{1-2z-5z^2+6z^3+8uz^2}
{1-6z+11z^2-6z^3-24u^2z^4}.}
\]
A second, sharp enumeration concerns the shortest possible \(j\)-universal words in this symmetry class. For every \(j\ge1\), their minimum length is \(qj\), and the number at that minimum length equals
\[
\boxed{\begin{cases}
(q!)^{j/2},&j\text{ even},\\
(q!)^{(j-1)/2}\,2^m m!,&j\text{ odd}.
\end{cases}}
\]
For four symbols, the first four positive-index minimum-length counts are \(8,24,192,576\), at respective word lengths \(4,8,12,16\).

More precisely, if \(v=a_1\cdots a_k r\) is its greedy *arch factorization* (defined below), with each \(a_i\) containing every symbol and \(r\) missing at least one symbol, then
\[
\boxed{\iota(W_\theta(v))=2k+
\mathbf 1_{\{\operatorname{alph}(r)\cup\theta(\operatorname{alph}(r))=\Sigma\}}.}
\]
This exact identity supplies the structural characterization behind both counts.

## Assumptions and scope
The alphabet \(\Sigma\) is fixed, labeled and has even cardinality \(q\ge2\); the letter permutation \(\theta\) consists of \(m=q/2\) disjoint two-cycles, with no fixed symbols. A reverse-complement symmetric word means a word \(w\) satisfying \(w=\theta(w^R)\). Such words necessarily have even length and are represented uniquely as \(W_\theta(v)\). All subsequence-universality tests use the entire fixed alphabet, even when a word omits some letters. The empty word has index zero. Indices \(n,j\) are nonnegative integers; minimum-length assertions concern \(j\ge1\). Products with no factors equal one, and a binomial coefficient outside its natural range is zero.

A greedy arch is the shortest nonempty prefix of the remaining word containing all \(q\) letters. Repeating this cut gives a unique decomposition \(v=a_1\cdots a_k r\), where \(r\) lacks some letter. Write \(\operatorname{alph}(r)\) for the set of letters occurring in \(r\).

## Proof
**1. Arch count equals universality index.** Every arch contains the full alphabet. Thus \(k\) arches provide, by choosing a desired symbol from each successive arch, every length-\(k\) word as a subsequence. Conversely, let \(b_i\) be the final letter of arch \(a_i\), which is absent earlier within that arch, and take a symbol \(a\) absent from the remainder \(r\). The word \(b_1\cdots b_ka\) cannot occur as a subsequence: the earliest placement of \(b_i\) after the earliest placement of \(b_{i-1}\) is at the end of arch \(a_i\), inductively, and \(a\) does not occur after the last arch. Therefore \(\iota(v)=k\). Equivalently, \(k\) is the maximum number of pairwise disjoint, ordered, full-alphabet intervals in \(v\). Greedy arch endpoints are no later than the endpoints of any other collection of \(k\) such intervals.

**2. Reverse-complement midpoint criterion.** Since \(\theta\) permutes the alphabet, \(\iota(\theta(v^R))=\iota(v)=k\). Splitting the word at its midpoint, any family of disjoint full-alphabet intervals has at most \(k\) wholly on either side, and at most one crossing the midpoint. Hence
\[
2k\le\iota(v\theta(v^R))\le2k+1.
\]
The lower bound uses the \(k\) arches of \(v\) and the \(k\) full-alphabet reversed-complement blocks on the other side. If \(\operatorname{alph}(r)\cup\theta(\operatorname{alph}(r))=\Sigma\), the central factor \(r\theta(r^R)\) is also a full-alphabet block, giving \(2k+1\) disjoint blocks.

For necessity, suppose there are \(2k+1\) disjoint full-alphabet intervals. Exactly \(k\) are wholly left, \(k\) wholly right, and one crosses the midpoint. The left \(k\) intervals must finish at or after the \(k\)-th greedy arch endpoint in \(v\). Consequently the crossing interval can use only a suffix of \(r\) on the left. Reversing and applying \(\theta\) to the right intervals gives \(k\) full-alphabet intervals in \(v\), so the crossing interval uses only a prefix of \(\theta(r^R)\) on the right. Its alphabet is therefore contained in \(\operatorname{alph}(r)\cup\theta(\operatorname{alph}(r))\). Being full-alphabet forces the asserted union condition. This proves the structural identity for every \(v\) and every permitted \(\theta\).

**3. Exact enumeration of arches and remainders.** A word of length \(\ell\) uses all letters of one prescribed set of cardinality \(s\) if and only if it represents a surjection from \(\{1,\ldots,\ell\}\) onto that set. Their ordinary length generating function is
\[
\sum_{\ell\ge0}s!\left\{\begin{matrix}\ell\\s\end{matrix}\right\}z^\ell
=\frac{s!z^s}{\prod_{h=1}^{s}(1-hz)}=B_s(z),
\]
where braces denote Stirling numbers of the second kind (and \(B_0=1\)). For an arch, the final letter is one of \(q\) possibilities, is new within that arch, and all the previous letters use each of the other \(q-1\) letters. Its generating function is therefore \(qzB_{q-1}(z)=A_q(z)\).

Every arch remainder has an alphabet \(S\subsetneq\Sigma\). Choosing its precise letter set and requiring every selected letter to occur gives \(T_q(z)\). The midpoint raises the universality index precisely when \(S\cup\theta(S)=\Sigma\). For each of the \(m\) involution pairs, such a set selects either one or both letters. If \(|S|=s\), exactly \(s-m\) pairs contribute both, and \(q-s\) pairs contribute exactly one; hence there are
\[
\binom m{s-m}2^{q-s}
\]
such sets. The full alphabet is excluded because \(S\) is an arch remainder; therefore \(s\le q-1\). The remainder generating function for midpoint-raising sets is exactly \(R_q(z)\).

A word is a unique sequence of \(k\) arches followed by one remainder. Each arch contributes \(u^2A_q(z)\) to the reverse-complement universality index, while the remainder contributes \(T_q(z)-R_q(z)+uR_q(z)\). Summing the geometric series in \(k\ge0\) gives the boxed rational generating function. At \(q=4\), substitute \(T_4=1+4B_1+6B_2+4B_3\), \(R_4=4B_2+4B_3\) and \(A_4=24z^4/((1-z)(1-2z)(1-3z))\); clearing denominators gives the displayed four-letter rational function.

**4. Sharp minimum-length counts.** Every \(j\)-universal word on \(q\) symbols must contain each letter at least \(j\) times (consider each constant-symbol subsequence), so its length is at least \(qj\). For \(j=2k\), equality in the reverse-complement class requires a half-word of length \(qk\) with \(k\) minimal arches of length \(q\) and empty remainder. Each arch is an arbitrary permutation of the alphabet, yielding \((q!)^k\) words. For \(j=2k+1\), equality requires \(k\) such arches and a middle-half remainder of length \(m\) that meets all \(m\) involution pairs. It must choose exactly one letter from every pair, in any order: \(2^m m!\) choices. Both constructions attain the respective lower bounds; no shorter word can be \(j\)-universal. No word of length \(qj\) has index greater than \(j\). The exact formulas follow.

## Verification
Run `python3 verify.py` using Python 3 without external dependencies. The included program enumerates all half-words in alphabets of size \(2,4,6,8\) through respective half-lengths \(12,8,6,5\). It compares direct greedy indices of complete reverse-complement words against the midpoint formula and independently computes all coefficient counts from surjection inclusion-exclusion and the rational identity. For small instances it also checks subsequence universality against the defining requirement by enumerating target words. Exact shortest-length coefficients are compared with the factorial formulas. Its successful output ends with

`VERIFY_OK halfwords=189008 nonzero_cells=124 direct_subsequence_cases=368 shortest_profiles=20`

These finite diagnostics are checks of the implementation and small cases, not the proof of the infinite formulas.

## Relationship to prior work
Barker, Fleischmann, Harwardt, Manea and Nowotka (2020) develop arch factorization and prove related universality-index identities for ordinary palindromes and concatenations involving alphabet permutations (their Section 4, Propositions 3 and 4). These ingredients motivate the midpoint argument, but they do not state the reverse-complement symmetry enumeration over arbitrary paired alphabets or the exact shortest-word counts here. Adamson, Fleischmann, Huch, Koß, Manea and Nowotka (2023) give powerful generic counting algorithms for universal words in regular languages. Their Section 4 does not specialize to the nonregular language of all reverse-complement symmetric words or supply the rational distribution above. An existing published record, *Closed-form law for binary subsequence universality*, treats all unconstrained binary words and its exact generating function differs from the involutive-symmetry distribution. Fleischmann, Höfer, Huch and Nowotka (2023) investigate Simon's congruence and a two-sided arch factorization, a related but distinct counting problem.

The new claim is the exact all-even-alphabet symmetry-class distribution, its four-letter closed form, and its minimal-length enumeration; it is not a claim to have discovered the underlying arch method. Searches of reverse-complement, antipalindromic, involutive and subsequence-universal formulations found no stated equivalent, but they cannot establish absolute bibliographic uniqueness.

## Limitations
The result is for fixed-point-free involutions on even-sized alphabets. Involutions with fixed letters permit odd-length symmetric words and require separate treatment. The word-count generating function is rational for each \(q\) but its coefficients are not simplified to a single general binomial expression. No assertion is made about contiguous-factor universality, error-correcting quality or experimentally measured DNA properties. Finite verification does not prove all-length statements; the proof above does. An undiscovered equivalent characterization or tabulation is the remaining originality risk.

## References
1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, first publicly available 2020-03-10, arXiv:2003.04629, https://arxiv.org/abs/2003.04629 .
2. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, D. Nowotka, *k-Universality of Regular Languages*, first publicly available 2023-11-17, arXiv:2311.10658, https://arxiv.org/abs/2311.10658 .
3. P. Fleischmann, J. Höfer, A. Huch, D. Nowotka, *Alpha-Beta-Factorization and the Binary Case of Simon's Congruence*, first publicly available 2023-06-25, arXiv:2306.14192, https://arxiv.org/abs/2306.14192 .
4. *Closed-form law for binary subsequence universality*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37 .
