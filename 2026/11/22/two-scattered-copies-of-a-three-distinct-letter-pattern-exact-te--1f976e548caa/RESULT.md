# Two scattered copies of a three-distinct-letter pattern: exact ternary enumeration

## Finding

For every integer \(n\ge 0\), let \(B_n\) be the number of length-\(n\) words over \(\{0,1,2\}\) with exactly two *positional scattered-subsequence occurrences* of \(012\): an occurrence is a strictly increasing index triple carrying letters \(0,1,2\). Then

\[
\sum_{n\ge0}B_nz^n=\frac{z^4(3-z)}{(1-z)^3(1-2z)^2}.
\]

Equivalently \(B_0=0\) and, for every \(n\ge1\),

\[
B_n=\frac{5n-29}{4}\,2^n+n^2+4n+7.
\]

In particular \(B_n\sim\frac54n2^n\), so the probability that a uniformly random ternary word has exactly two scattered \(012\)'s is asymptotic to \(\frac54n(2/3)^n\). Permuting the three alphabet symbols extends this conclusion unchanged to every fixed ordered pattern consisting of three pairwise distinct symbols on a three-letter alphabet.

## Assumptions and scope

Words are linear, not cyclic. Occurrences are counted with their positions, even when different index triples have equal letter sequences. The word may have repeated symbols, and all lengths, including \(n=0\), are included. The claimed enumeration is for the *full* three-symbol alphabet with the pattern using all three symbols; it does not assert the same formula for larger alphabets or patterns with repeated symbols.

## Proof

For any prefix \(u\), write \(p(u)\) for its number of scattered \(01\) pairs. When a symbol \(2\) is appended, it creates exactly \(p(u)\) scattered \(012\) occurrences; symbols \(0\) and \(1\) do not immediately create any. Also \(p(u)\) cannot decrease as a word grows. Consequently, a word with exactly two scattered \(012\)'s has precisely one of the following mutually exclusive histories of positive contributions from its symbols \(2\): a single contribution \(2\), or two contributions \(1,1\). All other symbols \(2\) precede the first scattered \(01\) pair; none can occur after the final positively contributing \(2\).

For each integer \(r\ge1\), denote by \(E_r\) the collection of ternary words whose projection obtained by deleting every \(2\) is \(1^u0^r\) for some \(u\ge0\). The ordinary length generating series of \(E_r\) is

\[
E_r(z)=\sum_{u\ge0}\frac{z^{u+r}}{(1-z)^{u+r+1}}=\frac{z^r}{(1-z)^r(1-2z)}.
\]

Indeed there is one way to choose the binary projection \(1^u0^r\), and the \(u+r+1\) slots before, between, and after its symbols independently receive arbitrary runs of \(2\)'s. Every ternary word with no scattered \(01\) has a binary projection of the form \(1^u0^v\).

Consider the unique first \(1\) which comes after at least one \(0\); it is the first symbol which raises \(p\) above zero. If the word has exactly one contributing \(2\), the pair count immediately preceding that \(2\) must be two. The first contributing \(1\) is then preceded by either (i) two zeros and followed by no further ones before the contributing \(2\), or (ii) one zero and followed by exactly one more one before that \(2\). These alternatives give the following two *unique, disjoint* decompositions:

\[
E_2\,1\,0^*\,2\,\{0,1\}^*,\qquad
E_1\,11\,0^*\,2\,\{0,1\}^*.
\]

Here an expression such as \(E_2\) denotes one word from that language, not a new alphabet symbol. The \(E_r\) part contains all zero-contributing \(2\)'s, since adding even a single \(2\) after the first productive \(1\) would contribute positively. The terminal binary suffix may be arbitrary because no further \(2\) occurs.

If there are two contributing \(2\)'s, both must see exactly one scattered \(01\) pair, so only zeros can lie between them: a \(1\) would create a second \(01\) pair. This yields exactly the third unique disjoint decomposition

\[
E_1\,1\,0^*\,2\,0^*\,2\,\{0,1\}^*.
\]

The three decompositions are exhaustive, as the first positive pair count can only be one or two in the first alternative, and must be one in the second. Their generating functions, using \(0^*\mapsto (1-z)^{-1}\) and \(\{0,1\}^*\mapsto (1-2z)^{-1}\), sum to

\[
\begin{aligned}
G(z)&=\frac{z^2E_2(z)}{(1-z)(1-2z)}
       +\frac{z^3E_1(z)}{(1-z)(1-2z)}
       +\frac{z^3E_1(z)}{(1-z)^2(1-2z)}\\
&=\frac{z^4}{(1-z)^3(1-2z)^2}
  +\frac{z^4}{(1-z)^2(1-2z)^2}
  +\frac{z^4}{(1-z)^3(1-2z)^2}\\
&=\frac{z^4(3-z)}{(1-z)^3(1-2z)^2}.
\end{aligned}
\]

Partial fractions give

\[
G(z)=\frac14-\frac{17}{2(1-2z)}+\frac{5}{4(1-2z)^2}
+\frac4{1-z}+\frac1{(1-z)^2}+\frac2{(1-z)^3}.
\]

Coefficient extraction establishes the stated exact formula and the dominant \(\frac54n2^n\) term, since the remaining terms contribute at most \(O(2^n+n^2)\). A bijective relabeling handles other patterns with three distinct letters.

## Verification

Two separate standard-library programs are supplied. `verification/verify_direct.py` enumerates all \(3^n\) ternary words for every \(0\le n\le11\), computes scattered occurrence counts by a direct prefix scan and checks that all accepted words fall in the two contribution classes. It reports the coefficient values \(3,20,83,276,807,2172,5523,13484\) at lengths \(4\) through \(11\).

`verification/verify_transfer.py` independently propagates the complete bounded prefix-count state \((\#0,\#01,\#012)\), capping the first two coordinates at three and retaining only the target-relevant third-coordinate values at most two. It verifies the first 51 coefficients against the degree-five recurrence obtained by clearing the denominator. The cap is justified because counts are nondecreasing and values at least three have the same effect on all future decisions about attaining exactly two. Both programs ran successfully; outputs are included. These finite tests corroborate, but do not replace, the unbounded decomposition proof.

## Relationship to prior work

Bruda's 2026 treatment of binary scattered-subsequence frequency proves eventual polynomiality for fixed positive frequency and discusses the different polynomial–exponential shape expected over larger alphabets; its stated alphabet-generalization result for frequency one does not give the present explicit all-length frequency-two ternary formula. Menon and Singh's earlier fixed-frequency formulas apply to binary words. Mansour and Shabani study three-position order patterns with at most two distinct letters, whereas the present pattern has three different letters. The distinct-object and exact-frequency comparisons are important: unrestricted ternary input words are not restricted canonical permutations, and counting *contiguous* trigram occurrences does not imply a count for scattered embeddings.

## Limitations

This is an exact enumeration for exactly two embeddings and three distinct symbols, not a general formula for every frequency or larger alphabets. The possibility of an unindexed mathematically equivalent special-case enumeration remains. This proof is a direct combinatorial decomposition; no external formal proof certification or independent scientific audit is claimed.

## References

- Glenn Bruda, *Enumerating binary words restricted by subsequence frequency*, arXiv:2607.02578, first posted June 30, 2026. https://arxiv.org/html/2607.02578
- Krishna Menon and Anurag Singh, *Subsequence frequency in binary words*, arXiv:2306.07870 (2023); *Discrete Mathematics* 347 (2024), 113928. https://arxiv.org/abs/2306.07870
- Toufik Mansour and Armend Sh. Shabani, *Counting occurrences of a pattern of length three with at most two distinct letters in a k-ary word*, *Journal of Automata, Languages and Combinatorics* 21 (2016), 183–201. https://doi.org/10.25596/jalc-2016-183
