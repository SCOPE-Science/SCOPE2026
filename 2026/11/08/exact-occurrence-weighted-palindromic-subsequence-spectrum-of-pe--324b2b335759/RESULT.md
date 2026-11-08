# Exact occurrence-weighted palindromic subsequence spectrum of permutation powers

## Finding

For integers \(q\ge3\), \(k\ge1\), and any word \(P=c_0c_1\cdots c_{q-1}\) whose letters are pairwise distinct, put \(W=P^k\). For every \(\ell\ge1\), let \(E_{q,k}(\ell)\) be the number of strictly increasing index tuples \((i_1,\ldots,i_\ell)\) in \(\{1,\ldots,qk\}\) for which \(W_{i_1}\cdots W_{i_\ell}\) is a palindrome. Different position tuples count separately even when they spell the same subsequence word.

Adopt the convention \(\binom ab=0\) unless \(0\le b\le a\) for integers \(a,b\). Then for every integer \(m\ge1\),

\[
E_{q,k}(2m-1)=q\sum_{e=0}^{m-1}\binom{m-1}{e}(q-1)^{m-1-e}\binom{k+m-e-1}{2m-1},
\]

\[
E_{q,k}(2m)=q\sum_{e=0}^{m-1}\binom{m-1}{e}(q-1)^{m-1-e}\binom{k+m-e-1}{2m}.
\]

The complete bivariate ordinary generating function is

\[
\mathcal E_q(z,t)=\sum_{k\ge1}\sum_{\ell\ge1}E_{q,k}(\ell)z^\ell t^k
=\frac{qzt(1-t+zt)}{(1-t)((1-t)^2-z^2t(q-1+t))}.
\]

Consequently, the greatest length of an embedded palindrome is \(2k-1\), and the number of its positional embeddings is precisely \(q(q-1)^{k-1}\). Moreover **each longest palindrome string has one embedding**. The entire length spectrum is unaffected by the ordering of the distinct letters in \(P\).

## Assumptions and scope

The alphabet has \(q\ge3\) distinct letters, each occurring once per period; \(P\) is a finite linear word, repeated \(k\ge1\) times, with positions counted in the linear concatenation. All \(\ell\ge1\) are included. The empty subsequence is excluded. A palindrome means equality with its reversal, and an occurrence is an index tuple, not a distinct subsequence string. The theorem is not a statement about arbitrary periodic run words or the maximal number over all words with the same length.

## Proof

**1. Exact embedding multiplicity of a pattern.** Relabel the letters in the order in which they appear in \(P\) as \(0,1,\ldots,q-1\); relabeling preserves index embeddings and palindromicity. For a nonempty pattern \(v=v_1\cdots v_L\), let
\[
d(v)=\#\{i:1\le i<L,\ v_i\ge v_{i+1}\}.
\]
Every occurrence of \(v\) in \(P^k\) has an associated sequence of period indices \(0\le b_1\le\cdots\le b_L\le k-1\), because each period lists its symbols in increasing order. At each weak descent \(v_i\ge v_{i+1}\), a strict period increase \(b_{i+1}\ge b_i+1\) is mandatory; at a strict ascent, a nonnegative increase is sufficient. These conditions are both necessary and sufficient, because within one period the symbols are unique and strictly ordered. Subtract the compulsory \(d(v)\) period increases from the \(L-1\) gaps. The start slack, remaining gap slacks, and end slack form a weak composition of \(k-1-d(v)\) into \(L+1\) parts. Therefore the exact number of position embeddings is
\[
\operatorname{emb}_{P^k}(v)=\binom{k+L-d(v)-1}{L},
\]
with zero when \(k-1<d(v)\). In particular, this is a statement about **every embedding**, not just greedy embeddability.

**2. Weak descents of palindromes.** Any length-\(2m-1\) palindrome has unique half-word \(x_1\cdots x_m\) and is \(x_1\cdots x_mx_{m-1}\cdots x_1\). Write \(e\) for the number of equal adjacent pairs in its half-word. Every unequal adjacent half-word pair and its reflected pair contribute exactly one weak descent in total, while an equal pair contributes two. Thus \(d(v)=m-1+e\). For a length-\(2m\) palindrome \(x_1\cdots x_mx_m\cdots x_1\), the central equality contributes one more, giving \(d(v)=m+e\).

For each \(e\in\{0,\ldots,m-1\}\), there are exactly \(q\binom{m-1}{e}(q-1)^{m-1-e}\) half-words with precisely \(e\) equal adjacencies: select the initial symbol, the \(e\) equality sites, and at each remaining site one of the other \(q-1\) symbols. Each half determines one palindrome. Substituting the two values of \(d(v)\) into the embedding formula and summing over all halves proves both displayed binomial sums.

**3. Rational generating function.** For integers \(L\ge1\), \(d\ge0\), use the formal-power-series identity
\[
\sum_{k\ge1}\binom{k+L-d-1}{L}t^k=\frac{t^{d+1}}{(1-t)^{L+1}}.
\]
The odd-palindrome series follows by the binomial theorem and a geometric series:
\[
\sum_{k,m\ge1}E_{q,k}(2m-1)z^{2m-1}t^k=
\frac{qzt}{(1-t)^2-z^2t(q-1+t)}.
\]
The even-palindrome series equals this odd series multiplied by \(zt/(1-t)\). Adding gives the claimed rational form as an identity of formal power series in \(z,t\).

**4. Extremal-length statement.** Since \(d(v)\ge m-1\) in odd length and \(d(v)\ge m\) in even length, an embedding in \(k\) periods has \(2m-1\le2k-1\) or \(2m\le2k-2\), respectively. At length \(2k-1\), only the \(e=0\) half-words are possible, so there are exactly \(q(q-1)^{k-1}\) palindrome strings and each has embedding multiplicity \(\binom{2k-1}{2k-1}=1\). Their existence for all \(k\ge1\) follows by selecting any half-word with unequal adjacent letters. No longer palindrome occurs. This completes the proof.

## Verification

The standalone file `palindrome_embedding_verifier.py` exhaustively enumerates index subsets, independently checks palindromicity and counts occurrences by length, and compares them to the closed binomial sums. Executing `python3 palindrome_embedding_verifier.py` gives **36 exhaustive occurrence profiles**, **314 per-length comparisons**, and **2,992 rational generating-function coefficient checks**. The checker also verifies the longest-length formula for those profiles. These computations test finite parameters only; the proof above supplies the unrestricted result.

Examples: for \((q,k)=(3,2)\), the occurrence counts in ascending positive lengths are \((6,3,6)\), whereas the distinct-palindrome-string counts are \((3,3,6)\). For \((q,k)=(3,3)\), the positional counts are \((9,9,27,6,12)\).

## Relationship to prior work

Mahalingam and Pandoh introduced and analyzed the count of **distinct** palindromic scattered subsequence strings and its lengthwise versions. Their general bounds and fixed-alphabet extremal results do not give the occurrence-weighted spectrum of a permutation power; in particular, a support count cannot determine how many index tuples produce each string. Torres-Jimenez, Izquierdo-Marquez, Ramirez-Acuna, and Peralta give a general algorithm counting individual subsequence occurrence multiplicities for arbitrary words, but not a closed, all-period and all-length spectrum of palindromic embeddings in this family. Müllner and Ryzhikov study longest palindromic subsequences under length and letter-count restrictions, not this multiplicity enumerator. The distinct-subsequence spectrum of prefixes of the same periodic word is a related, broader **support** classification but does not imply multiplicities.

## Limitations

The formula requires each of the \(q\) letters to occur exactly once per repeated period. It does not characterize the distribution of multiplicities across individual palindrome strings, only their lengthwise sum. No priority or bibliographic-completeness guarantee is claimed; unindexed equivalent enumeration identities are possible. The numerical checks are finite and are not substitutes for the proof. 

## References

1. K. Mahalingam and P. Pandoh, *Counting Scattered Palindromes in a Finite Word*, arXiv:2108.02729v1 (first public 2021-08-05), https://arxiv.org/abs/2108.02729 . Sections 2, 4, and 5 concern distinct scattered palindromes, lengthwise bounds, and extremal total counts.
2. J. Torres-Jimenez, I. Izquierdo-Marquez, D. Ramirez-Acuna, and R. Peralta, *A Near-Optimal Algorithm to Count Occurrences of Subsequences of a Given Length*, *Discrete Mathematics, Algorithms and Applications* (2017), DOI:10.1142/S1793830917500422, https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=920771 . Generic occurrence-counting algorithm.
3. C. Müllner and A. Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502v1 (2019), https://arxiv.org/abs/1901.07502 . Longest-palindromic-subsequence bounds and related questions.
