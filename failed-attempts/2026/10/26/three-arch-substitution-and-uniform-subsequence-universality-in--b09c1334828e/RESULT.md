# Three-arch substitution and uniform subsequence universality in the Tribonacci word

## Finding

For the infinite Tribonacci word \(t=\tau^\omega(0)\) over \(\{0,1,2\}\), with \(\tau(0)=01\), \(\tau(1)=02\), and \(\tau(2)=0\), its **entire** greedy three-letter arch decomposition consists of the three words
\[
A=\mathtt{0102},\qquad B=\mathtt{0100102},\qquad C=\mathtt{010102}.
\]
Its sequence of arch types is the morphic fixed point \(\sigma^\omega(A)\), where
\[
\sigma(A)=ABCB,\quad \sigma(B)=ABCBBCB,\quad \sigma(C)=ABCBCB.
\]
For every prefix \(p\) of \(t\), the scattered-subsequence universality index is exactly \(\iota(p)=|p|_2\), the number of occurrences of the letter \(2\). For every nonempty factor \(v\) of \(t\),
\[
\max\{0,|v|_2-1\}\le \iota(v)\le |v|_2.
\]
If \(\lambda>1\) is the real root of \(\lambda^3=\lambda^2+\lambda+1\), then every nonempty factor satisfies the position-uniform bound
\[
\left|\iota(v)-\lambda^{-3}|v|\right|<\frac52.
\]
In particular every sequence of factors whose lengths tend to infinity has universality-index density \(\lambda^{-3}\), independently of their locations. Furthermore, for \(n\ge3\),
\[
\iota\bigl(\tau^n(0)\bigr)=|\tau^{n-3}(0)|.
\]

## Assumptions and scope

The alphabet is exactly \(\{0,1,2\}\). A scattered subsequence deletes positions without reordering. For a finite word \(u\), its universality index \(\iota(u)\) is the largest integer \(k\ge0\) such that all \(3^k\) ternary words of length \(k\) occur as scattered subsequences of \(u\). A **greedy arch** is the shortest nonempty prefix containing every alphabet letter, iterated after deletion of that prefix; an incomplete final suffix is not counted as an arch. We use \(|u|_2\) for the number of occurrences of the letter \(2\), and factors are contiguous finite subwords of \(t\). The balanced-factor estimate \(\bigl||v|_2-\lambda^{-3}|v|\bigr|<3/2\) is an earlier published result, explicitly cited below; the finite-morphism decomposition and its subsequence consequences are proved here.

## Proof

**Greedy arches count the index.** If a word splits into \(k\) complete greedy arches followed by an incomplete suffix, each complete arch supplies an arbitrarily prescribed one-letter subsequence, hence every ternary word of length \(k\) is a subsequence. Conversely, recording the last new letter completed by each greedy arch and then any letter absent from the terminal incomplete suffix produces a length-\(k+1\) word absent as a scattered subsequence (the usual arch-factorization theorem, also stated in Schnoebelen–Veron). Thus \(\iota(u)=k\).

**Finite morphism identities.** Introduce the arch decoder \(d(A)=0102\), \(d(B)=0100102\), and \(d(C)=010102\). Each decoded word has exactly one \(2\), at the last position, and contains both \(0\) and \(1\) before it. Hence any concatenation of these words is already decomposed into greedy arches. The following three *exact free-word identities* hold by applying \(\tau\) three times and concatenating letters:
\[
\tau^3(d(A))=d(ABCB),\quad
\tau^3(d(B))=d(ABCBBCB),\quad
\tau^3(d(C))=d(ABCBCB).
\]
These are finite explicit identities in the free monoid, independently reproduced by the embedded checker; no infinite-word inference is taken from a finite sample. Since \(d(A)=\tau^2(0)\), induction on \(j\ge0\) gives the identity
\[
\tau^{3j+2}(0)=d\!\left(\sigma^j(A)\right).
\]
The lengths of these nested prefixes tend to infinity, and their limit is \(t\). Therefore every greedy arch in \(t\) belongs to \(\{A,B,C\}\) and its arch-type sequence is exactly \(\sigma^\omega(A)\). Each of the three arch types actually occurs, since all occur in \(\sigma(A)\).

**Indices of prefixes and arbitrary factors.** Every arch of the infinite decomposition contains exactly one \(2\), as its final letter. Every prefix \(p\) consequently has one completed arch per occurrence of \(2\), including a possible incomplete terminal arch containing no \(2\), and \(\iota(p)=|p|_2\). Let an arbitrary factor \(v\) contain \(r\) occurrences of \(2\). Every rich arch in any greedy factorization must contain at least one \(2\), so \(\iota(v)\le r\). Between consecutive occurrences of \(2\) in \(t\), the next full arch starts with both \(0\) and \(1\) before its final \(2\). Thus, inside \(v\), each of the \(r-1\) disjoint pieces beginning at one occurrence of \(2\) and ending just before the next contains all \(0,1,2\). Concatenating such complete-alphabet pieces makes \(v\) a supersequence of every ternary length-\(r-1\) word, and therefore \(\iota(v)\ge r-1\); for \(r=0\), the lower bound is zero.

**Uniform limiting density.** The incidence matrix of \(\tau\) has positive dominant eigenvalue \(\lambda\), the real root of \(\lambda^3=\lambda^2+\lambda+1\), and its normalized right frequency vector is \((\lambda^{-1},\lambda^{-2},\lambda^{-3})\). In particular the frequency of \(2\) is \(\lambda^{-3}\). The known Tribonacci balance estimate (Lejeune–Rigo–Rosenfeld, using earlier balance results) states that every factor \(v\) obeys \(\bigl||v|_2-\lambda^{-3}|v|\bigr|<3/2\). The factor inequalities established above immediately yield \(\bigl|\iota(v)-\lambda^{-3}|v|\bigr|<5/2\), uniformly in both length and starting position.

**Morphically generated finite prefixes.** A \(2\) is emitted by \(\tau\) only from a \(1\); a \(1\) only from a \(0\); every input letter emits exactly one \(0\). Therefore for \(n\ge3\), \(|\tau^n(0)|_2=|\tau^{n-3}(0)|\). Apply the prefix formula above.

## Verification

Run the standalone pure-Python program `verify_arch.py` with Python 3.10 or later. It checks all three finite identities directly from \(\tau\) and \(\sigma\), five successive iterate comparisons, all 10,000 prefix lengths, all distinct factors up to length 150 in a 35,000-plus-symbol prefix, independent subsequence tests for short factors up to length 14, and the nested-prefix length formula through level 18. The expected success line is `TRIBONACCI_ARCH_RETURN_MORPHISM_PASS`. The infinite assertions rest on the free-word identities, induction, and the cited factor-count discrepancy theorem, not on sampling.

## Relationship to prior work

Greedy arches and their equality to scattered-subsequence universality were developed for arbitrary words before this result (Schnoebelen–Veron, 2023). The two-balance property and the stronger specific letter-frequency discrepancy bound of the Tribonacci word were also known (Richomme–Saari–Zamboni; Lejeune–Rigo–Rosenfeld). The new, separately identifiable claims here are the explicitly induced three-arch substitution, the exact index-versus-letter-count relation for all Tribonacci prefixes, the one-unit universal interval for arbitrary factors, and the uniform constant-error asymptotic produced by combining them with the previously known discrepancy. These are not claims of new general arch algorithms or newly discovered letter frequencies.

## Limitations

The factor estimate \(5/2\) is a sufficient upper bound, not established sharp. The exact value of \(\iota(v)\) for an individual factor can depend on its endpoints; it need not equal \(|v|_2\). The theorem addresses the classical Tribonacci fixed point and alphabet \(\{0,1,2\}\), not arbitrary Arnoux–Rauzy or substitution words. A semantically equivalent return substitution or index law might exist in unindexed research; the literature comparison below is not a proof of global priority. Independent external mathematical audit has not been performed.

## References

- N. Schnoebelen and I. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932 (first posted 2023-04-24), https://arxiv.org/abs/2304.11932.
- M. Lejeune, M. Rigo, M. Rosenfeld, *Templates for the k-binomial complexity of the Tribonacci word*, 2020 preprint, https://orbi.uliege.be/bitstream/2268/244495/1/version_kronecker.pdf; see the factor-count discrepancy estimate in its balance discussion.
- G. Richomme, K. Saari, L. Q. Zamboni, *Balance and Abelian complexity of the Tribonacci word*, arXiv:0904.2872, https://arxiv.org/abs/0904.2872.
