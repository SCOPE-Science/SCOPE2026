# A sharp two-letter factor cutoff for cyclic repeated-letter substitutions

## Finding

For all integers \(q\ge3\) and \(r\ge2\), define the constant-length substitution on \(\mathbb Z/q\mathbb Z\)
\[
\sigma_{q,r}(a)=a^r(a+1),\qquad s=\lim_{j\to\infty}\sigma_{q,r}^{j}(0),\qquad B=r+1,\quad L=(r+1)(r+2).
\]
Addition in letters is modulo \(q\), and an exponent on a finite word denotes concatenation repetition. Let \(\mathcal F_n(s)\) be the set of distinct **contiguous** factors of length \(n\), and put \(m(n)=\min_{u\in\mathcal F_n(s)}|\operatorname{alph}(u)|\).

**Theorem.**
\[
m(n)=\begin{cases}
1,&1\le n\le r+1,\\
2,&r+2\le n\le L,\\
\ge3,&n\ge L+1.
\end{cases}
\]
At the last two-letter length \(L\), the complete set of factors using at most two distinct symbols consists of precisely the \(q\) words
\[
E_a=a\big(a^r(a+1)\big)^{r+1}(a+1)^r,
\qquad a\in\mathbb Z/q\mathbb Z.
\]
Hence the exact first window length that forces at least three distinct symbols is \(L+1\), independently of \(q\).

## Assumptions and scope

All words are over the labeled cyclic alphabet \(\mathbb Z/q\mathbb Z\). This is an ordinary one-sided fixed point (which exists because the image of zero begins in zero). Every occurrence is a contiguous substring; no scattered-subsequence or circular-factor interpretations are used. The claims hold for every pair of integers \(q\ge3\) and \(r\ge2\), every positive factor length, and every alphabet position. The number of distinct letters can eventually exceed three; the theorem makes no exact claim in that range.

## Proof

**Run lemma.** Every constant-symbol run in \(s=\sigma_{q,r}(s)\) has length at most \(r+1=B\). Inside each first-level block \(\sigma_{q,r}(d)=d^r(d+1)\), the initial run has length \(r\) and the terminal letter has length one; an across-block matching run can add at most this one terminal letter to the next block's initial run, so no run exceeds \(r+1\). The factor \(a^{r+1}\) occurs, because \((a-1)a\) is a factor of \(s\) (it occurs inside \(\sigma_{q,r}(a-1)\)) and its substituted image contains \(a^{r+1}\). All symbols \(a\) occur: successive substitution of a symbol creates its successor, starting from zero.

**Block bound.** Consider a factor \(u\) containing at most two distinct symbols, and decompose its occurrence in \(s=\sigma_{q,r}(s)\) into a suffix of one substituted block, \(k\) complete consecutive substituted blocks, and a prefix of the next substituted block. Either partial block has length at most \(B-1=r\). If \(k=0\), then \(|u|\le 2r<L\). If \(k\ge1\), the complete block \(\sigma_{q,r}(c)\) contains both \(c\) and \(c+1\), so these must be precisely the two letters of \(u\). For \(q\ge3\), the unordered pair \(\{c,c+1\}\) determines \(c\) uniquely among cyclic directed-neighbor pairs, except when \(q=2\), which is expressly excluded. Thus every complete block in \(u\) has the same source letter \(c\). The run lemma gives \(k\le r+1\).

If \(k\le r\), then \(|u|\le kB+2r\le r(r+1)+2r=L-2\). If \(k=r+1\), the two neighboring source letters (if present) are different from \(c\), again by the run lemma. Among substituted blocks of letters different from \(c\), the only nonempty suffix over \(\{c,c+1\}\) can be the final singleton \(c\) in \(\sigma_{q,r}(c-1)\); its length is at most one. Similarly the only nonempty prefix over \(\{c,c+1\}\) is a prefix of \(\sigma_{q,r}(c+1)\), which is \((c+1)^r\) with length at most \(r\). It follows that
\[
|u|\le 1+(r+1)B+r=(r+1)(r+2)=L.
\]
If equality holds, each block and both partial boundaries must attain its maximum, forcing exactly \(u=E_c\), and the \(q\) choices are distinct. This proves the upper bound and the uniqueness portion of the theorem.

**Attainment.** For every \(c\), the neighboring pair \((c-1)c\) occurs in \(s\), so \(\sigma_{q,r}((c-1)c)\) contains the three-run factor \((c-1)c^{r+1}(c+1)\). Applying the substitution again shows that \(s\) contains a suffix \(c\) of \(\sigma_{q,r}(c-1)\), followed by \(r+1\) full copies of \(\sigma_{q,r}(c)\), followed by the initial \(r\) symbols of \(\sigma_{q,r}(c+1)\). This is \(E_c\) of length exactly \(L\). The run lemma proves \(m(n)>1\) for \(n>r+1\); factors of length at most \(r+1\) with one symbol occur. Prefixes of \(E_c\) furnish factors with exactly two letters at all lengths \(r+2\le n\le L\); the upper bound excludes two-letter factors at all larger lengths, since any longer factor contains a length-\(L+1\) subfactor. This completes the proof.

## Verification

Two standalone Python 3 programs accompany this result. Run `python3 verify_factors.py` and `python3 verify_prefix.py`. The first independently constructs complete finite factor sets by a three-factor substitution closure and checks the extremal lengths for all \(3\le q\le9\) and \(2\le r\le8\), with 245 exact factor-length checks over 49 parameter pairs. The second enumerates actual prefix windows for \(3\le q\le5\) and \(2\le r\le5\). Recorded standard outputs are provided in `verify_factors.out` and `verify_prefix.out`. These checks support the proof but, being bounded finite computations, do not replace its universal argument.

## Relationship to prior work

Allouche, Rampersad, Rigo, Shallit and Stipulanti (2026) introduce the three-letter, three-repeat cyclic substitution and study the abelian complexity of a binary coding. Their Remark 4 proposes variations in repetition and alphabet size, but the inspected article does not classify the **maximum length of factors restricted to two alphabet symbols**. Two published studies of nonregular abelian complexity of analogous three-letter morphisms with more repetitions address a distinct statistic, and general cyclic-run factor or minimal-absent-word results concern periodic words rather than the substitution fixed points at issue. The new theorem is an exact support-cardinality cutoff and complete extremal-factor classification, not a consequence asserted by those statements. Unindexed earlier equivalences have not been ruled out.

## Limitations

The classification is deliberately confined to whether factors require one, two, or at least three symbols; it does not enumerate every larger-alphabet support level or all factors of a given length. The alphabet size two is excluded, because directed-neighbor unordered pairs then no longer identify unique source letters. The originality comparison is based on inspected relevant articles and indexed summaries, with residual risk from inaccessible full historical texts and unindexed literature. No independently conducted audit has been performed.

## References

1. J.-P. Allouche, N. Rampersad, M. Rigo, J. Shallit and M. Stipulanti, *An example of an automatic sequence with non-regular abelian complexity*, arXiv:2610.03837v1, first public 2026-10-02. https://arxiv.org/html/2610.03837v1
2. B. Espinoza, P. Popoli and M. Stipulanti, *Factor-balancedness, linear recurrence, and factor complexity*, arXiv:2602.03746v1, first public 2026-02-03. https://arxiv.org/html/2602.03746v1
3. *An infinite nonregular abelian-complexity family with interval-valued power-scale limits*, public record: https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-an-infinite-nonregular-abelian-complexity-family-with-interval-v--7b09e62adf22
4. *An infinite ternary-morphism family with nonregular binary abelian complexity*, public record: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-an-infinite-ternary-morphism-family-with-nonregular-binary-abeli--f292807a24e1
