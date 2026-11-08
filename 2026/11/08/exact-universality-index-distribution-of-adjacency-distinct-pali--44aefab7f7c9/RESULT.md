# Exact universality-index distribution of adjacency-distinct palindromes

## Finding
Fix a labeled alphabet \(\Sigma_q=\{0,1,\ldots,q-1\}\), where \(q\ge2\). A word is **adjacency-distinct** if consecutive letters differ, and **palindromic** if it equals its reversal. A word is \(k\)-subsequence-universal over the *full, fixed alphabet* \(\Sigma_q\) if it contains every word in \(\Sigma_q^k\) as a scattered subsequence. Its universality index \(\iota(w)\) is the greatest such \(k\), with \(\iota(w)=0\) allowed.

Every nonempty adjacency-distinct palindrome has odd length. Let \(p_q(h,k)\) be the number of those palindromes of length \(2h+1\) with \(\iota(w)=k\), for \(h,k\ge0\). Define the formal power series
\[
F_q(z,u)=\sum_{h,k\ge0}p_q(h,k)z^hu^k.
\]
Put
\[
D_q(z)=\prod_{j=0}^{q-2}(1-jz),\qquad
B_{q,s}(z)=\frac{(q-1)!}{(q-s)!}\frac{z^s}{\prod_{j=0}^{s-1}(1-jz)}\quad(1\le s<q),
\]
and \(\alpha_q=(q-1)(q-1)!\). Then the **entire bivariate distribution**, for every \(q\ge2\), is
\[
\boxed{F_q(z,u)=\frac{q\left(1+(q-1)\sum_{s=1}^{q-1}B_{q,s}(z)+(u-1)B_{q,q-1}(z)\right)}{1-u^2\alpha_qz^q/D_q(z)}.}
\]
All coefficients are nonnegative integers and the formula is an identity of formal power series at \(z=0\). In particular,
\[
F_2(z,u)=\frac{2}{1-uz},\qquad
F_3(z,u)=\frac{3(1+z+2uz^2)}{1-z-4u^2z^3}.
\]

This also determines the **shortest palindromic adjacency-distinct \(k\)-universal words** and counts every shortest witness. For every \(m\ge1\),
\[
\begin{array}{c|c|c}
\text{required index}&\text{shortest total length}&\text{number of shortest words}\\\hline
2m&2mq+1&q!\,\alpha_q^{m-1}(q-1)
\end{array}
\]
and for every \(m\ge0\),
\[
\begin{array}{c|c|c}
2m+1&2(m+1)q-1&q!\,\alpha_q^m.
\end{array}
\]
Here "\(k\)-universal" means index **at least** \(k\); the shortest witnesses have index exactly \(k\). The second length exceeds the unrestricted optimum \(q(2m+1)\) by \(q-1\); the first exceeds the unrestricted optimum \(2mq\) by one.

## Assumptions and scope
All \(q\) alphabet letters are distinct labeled symbols; adjacency-distinct means \(w_i\ne w_{i+1}\) for all applicable indices. Universality is always measured against all \(q\) symbols, even when a word omits some of them. An empty half-word is permitted in the decomposition of a length-one palindrome. The two variables \(z,u\) mark *half-length* and *exact universality index*, respectively, not total length or an at-least index. We do not count empty palindromes. Since an even-length palindrome repeats its middle letter, it cannot be adjacency-distinct.

## Proof
**1. Midpoint index lemma.** Every nonempty adjacency-distinct palindrome is uniquely \(v c v^{\mathrm R}\), where \(v\) is adjacency-distinct and \(c\ne\operatorname{last}(v)\) when \(v\ne\varepsilon\). Greedily split \(v\) into \(a\) shortest complete-alphabet arches and a remainder \(r\) whose alphabet is a proper subset of \(\Sigma_q\). Then
\[
\iota(v c v^{\mathrm R})=2a+\delta,\qquad
\delta=\mathbf1_{\{\operatorname{alph}(r)\cup\{c\}=\Sigma_q\}}.
\]
This is the odd-palindrome case of Barker et al., Proposition 15 (2020), and also follows directly from two-sided greedy-arch bounds. The \(a\) arches and their reflections provide \(2a\) disjoint complete-alphabet blocks, and the middle \(r c r^{\mathrm R}\) provides one more precisely when its alphabet is complete. Conversely, if there are \(2a+1\) disjoint complete-alphabet blocks, shifting the leftmost \(a\) to the greedy left arches and the rightmost \(a\) to their greedy right reflections places the middle complete block inside \(r c r^{\mathrm R}\). The remaining central alphabet must therefore be complete. There cannot be \(2a+2\) complete blocks: the leftmost \(a+1\) would then lie inside \(v\) or the rightmost \(a+1\) inside \(v^{\mathrm R}\), contradicting the definition of \(a\). For \(v=\varepsilon\), the index is zero because \(q\ge2\). In the nonempty case, \(\delta=1\) precisely when \(r\) contains exactly \(q-1\) distinct letters and \(c\) is the unique missing letter.

**2. Counting incomplete arches.** After seeing exactly \(s\) distinct letters, the last letter is one of those seen. To continue an adjacency-distinct word without completing the alphabet, there are \(s-1\) choices from the already-seen set or \(q-s\) choices to add a new symbol. The corresponding geometric factor at level \(s\) is \((1-(s-1)z)^{-1}\). Thus an initial nonempty remainder with exactly \(s\) letters contributes \(qB_{q,s}(z)\), while a remainder immediately following a completed arch contributes \((q-1)B_{q,s}(z)\): its first letter may be any of the \(q-1\) symbols different from the previous arch's last letter.

An initial completed arch has generating function \(q!z^q/D_q(z)\), because it discovers every letter exactly once in its discovery sequence. A later completed arch has generating function \(\alpha_q z^q/D_q(z)\), again by excluding the preceding arch's terminal letter from its first-letter choice. These generating functions encode both the discovery steps and arbitrarily many allowed repeats among already discovered, non-last symbols.

**3. Inserting the center and summing.** Let \(T_q(z,u)=1+(q-1)\sum_{s=1}^{q-1}B_{q,s}(z)+(u-1)B_{q,q-1}(z)\). For the empty half, there are \(q\) possible centers. For every nonempty incomplete half-remainder, there are \(q-1\) center choices, except that the unique missing center letter receives one additional factor \(u\) exactly when the remainder has \(q-1\) distinct symbols. For each *completed* arch, the palindrome receives two universality units, hence a factor \(u^2\). The first completed arch has \(q!z^q/D_q(z)\) possibilities; each subsequent completed arch has \(\alpha_qz^q/D_q(z)\). Since \((q-1)q!=q\alpha_q\), the initial and continuing-arch contributions combine to
\[
F_q(z,u)=qT_q(z,u)\sum_{a\ge0}\left(u^2\frac{\alpha_qz^q}{D_q(z)}\right)^a,
\]
which is the displayed rational function. No state is omitted: every half-word has a unique greedy decomposition, and the center choice uniquely specifies the entire palindrome.

**4. Sharp shortest lengths and counts.** If \(\iota(w)\ge2m\), the left half must contain at least \(m\) arches, so its length is at least \(mq\). Equality forces \(m\) consecutive permutations, with \(q!\) choices for the first and \(\alpha_q=(q-1)(q-1)!\) for each subsequent permutation. There are \(q-1\) admissible centers. This proves the even-index row.

If \(\iota(w)\ge2m+1\), either the half has at least \(m+1\) arches (requiring at least \((m+1)q\) positions) or it has \(m\) arches and the remainder contains \(q-1\) distinct symbols (requiring at least \(mq+q-1\) positions). Equality in the latter case forces \(m\) permutation arches followed by a length-\(q-1\) permutation of distinct letters. If \(m=0\), the half and missing center have \(q!\) possibilities. If \(m\ge1\), each subsequent full arch and the final partial permutation has \(\alpha_q\) possibilities; the center is then uniquely forced. This proves the odd-index row and both attainability statements.

## Verification
A standalone integer-arithmetic script, `verify.py`, computes the numerator polynomial and denominator recurrence, compares the resulting exact coefficients with independent exhaustive palindrome generation, and computes each tested palindrome's universality index by checking **all** length-\(k\) subsequences directly. It also tests the midpoint criterion, both shortest-length counts, and the ternary binomial coefficient specialization. Executed output:

`VERIFY_OK q=2..8 half_length<=56 brute_palindromes=65414 extremal_checks=49 ternary_coefficients=0..50`

Reproduce with `python3 verify.py`; Python's standard library suffices. The exhaustive direct comparisons cover \(q=2\) through \(6\) at their documented bounded half-lengths, whereas coefficient and shortest-length checks extend to \(q=8\). These computations are checks of the proof, not substitutes for its general quantifiers.

For \(q=3\), the coefficient of \(z^hu^{2m+1}\) is exactly
\[
6\cdot4^m\binom{h-2m-2}{m},
\]
using the convention \(\binom nr=0\) if \(n<r\) or \(n<0\). For \(2m\), the coefficient is
\[
3\cdot4^m\left[\binom{h-2m}{m}+\binom{h-2m-1}{m}\right].
\]
In particular, these formulas cover all lengths and all indices, including zero.

## Relationship to prior work
Barker, Fleischmann, Harwardt, Manea and Nowotka (2020), Proposition 15, proved the general midpoint rule for the universality index of a palindrome. That known lemma is explicitly used here, not presented as new. Adamson (2023) gives algorithms for counting unrestricted subsequence-universal words, and Adamson et al. (2023) give algorithmic counting for regular-language constraints. Neither supplies the above closed series for the intersection of the **nonregular palindrome family** with the adjacency-distinct constraint, nor the complete residual-alphabet refinement and shortest-witness multiplicities in the inspected primary text. The new contribution is the explicit, all-alphabet, all-length *distribution* under these simultaneous constraints, rather than the underlying arch or palindrome criterion.

## Limitations
The count concerns labeled alphabets, exact index, odd-length palindromes, and the adjacency-distinct condition; it is not a formula for unconstrained palindromes or for subsequence-**palindromic** factors. No independent validation or exhaustive bibliography is claimed. Existing general midpoint and arch results account for significant portions of the proof. An equivalent specialized enumeration in unindexed work remains a genuine originality risk. The finite verifier checks bounded parameter ranges only.

## References
1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words* (first publicly posted 2020-03-10), arXiv:2003.04629v1, especially Definition 6 and Proposition 15. https://arxiv.org/abs/2003.04629
2. D. Adamson, *Ranking and Unranking \(k\)-subsequence Universal Words* (first publicly posted 2023-04-10), arXiv:2304.04583v1, Sections 1–3. https://arxiv.org/abs/2304.04583
3. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, D. Nowotka, *\(k\)-Universality of Regular Languages* (first publicly posted 2023-11-17), arXiv:2311.10658v1, especially Section 4. https://arxiv.org/abs/2311.10658
