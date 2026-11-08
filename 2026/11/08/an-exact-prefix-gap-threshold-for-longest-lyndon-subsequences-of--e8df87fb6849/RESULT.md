# An exact prefix-gap threshold for longest Lyndon subsequences of monotone-gap binary words

## Finding

Let \(k\ge1\), \(1\le g_1\le\cdots\le g_k\) be integers, and define the finite binary word
\[
W=1\,0^{g_1}1\,0^{g_2}1\cdots0^{g_k}1.
\]
Use the ordered alphabet \(0<1\). A scattered subsequence is obtained by deleting arbitrary symbols without changing the order of those kept. A nonempty word is Lyndon when it is strictly lexicographically smaller than every nonempty proper suffix. Write \(S_j=\sum_{i=1}^j g_i\), \(S=S_k\), and
\[
t=\min\bigl(\{j\in\{1,\ldots,k\}:S_j>g_k\}\cup\{k\}\bigr).
\]
Then the maximum number of symbols in any Lyndon subsequence of \(W\) is precisely
\[
\boxed{\Lambda(W)=S+k+1-t=|W|-t.}
\]
The minimum deletion count to make \(W\) Lyndon is exactly \(t\). This is a closed-form theorem for every allowed gap vector, not a claim for arbitrary binary words.

## Assumptions and scope

All gaps are positive **integers** and nondecreasing; adjacent equal gaps are permitted. The order on the alphabet is \(0<1\), and subsequences need not be contiguous. A single letter is Lyndon by the vacuous proper-suffix condition. For \(k=1\), the convention in the definition of \(t\) gives \(t=1\). For \(k\ge2\), a qualifying index always exists, because \(S_k>g_k\). The input may be represented by \(k\) run lengths without expanding the word.

## Proof

**Construction.** Remove the first \(t\) occurrences of the symbol \(1\) in \(W\) and keep every other symbol. The resulting word is
\[
V=0^{S_t}1\,0^{g_{t+1}}1\cdots0^{g_k}1.
\]
When \(t=k\), the expression means simply \(V=0^S1\). If \(t<k\), then \(S_t>g_k\ge g_i\) for all later gaps. Therefore the initial zero-run of \(V\) is strictly longer than every subsequent zero-run. Every proper suffix beginning with \(1\) is larger than \(V\); a suffix beginning with \(0\) has a strictly shorter initial zero-run, and is also larger. So \(V\) is Lyndon, of length \(S+k+1-t\).

**Suffix obstruction.** Any binary Lyndon word with at least two occurrences of \(1\) has a nonempty first zero-run \(0^a\), ends in \(1\), and has a final zero-run \(0^c\) directly before the last \(1\), where \(c<a\). Indeed, if \(c>a\), the proper suffix \(0^c1\) is lexicographically smaller; if \(c=a\), this suffix is a proper prefix of the whole word and is therefore lexicographically smaller. A Lyndon binary word with more than one letter must start with \(0\) and end with \(1\), since otherwise a proper suffix consisting of a smaller or equal letter contradicts the Lyndon condition.

**Optimality.** Let \(U\) be an arbitrary Lyndon subsequence, and write \(d\) for the number of symbols deleted. If \(U\) has at most one occurrence of \(1\), then \(|U|\le S+1\), hence \(d\ge k\ge t\). Otherwise number the occurrences of \(1\) in \(W\) as \(0,1,\ldots,k\), and let \(j\ge1\) and \(h>j\) denote the indices of the first and last retained occurrences in \(U\). Since \(U\) starts with \(0\), the first \(j\) occurrences of \(1\) are deleted. If \(j\ge t\), then \(d\ge j\ge t\).

Assume \(j<t\). If \(h=k\), the length \(a\) of the initial zero-run of \(U\) satisfies \(a\le S_j\). The last zero-run \(c\) satisfies \(c\le a-1\). Of the \(g_k\) zeros in the final original gap, at least \(g_k-c\ge g_k-S_j+1\) must have been deleted. Hence
\[
d\ge j+g_k-S_j+1\ge j+S_{t-1}-S_j+1\ge t,
\]
where the second inequality follows from minimality of \(t\) (\(S_{t-1}\le g_k\)) and the third from positivity of the intermediate gaps. This includes the case \(t=k\).

Finally, if \(h<k\), all \(g_k\) zeros in the last original gap and the final \(k-h\) occurrences of \(1\) are absent, so \(d\ge j+g_k+k-h\ge j+g_k+1\). For \(t\ge2\), \(g_k\ge S_{t-1}\ge t-1\), whence \(d\ge t\). If \(t=1\) there is no index \(j<t\), so this case cannot occur. Every Lyndon subsequence therefore requires at least \(t\) deletions; the construction attains this bound.

**Consequences.** When all gaps equal some positive integer, the threshold is \(t=2\) for \(k\ge2\). For triangular gaps \(g_i=i\) and \(k\ge2\), the threshold is the least \(t\) such that \(t(t+1)/2>k\); at \(k=1\) the threshold is one. For geometric gaps \(g_i=2^{i-1}\), the prefix sum before the last gap is smaller than the last gap, so \(t=k\). These families exhibit sharply different deletion counts despite the common monotonicity hypothesis.

## Verification

Run `python3 verify_lyndon.py` with Python 3 and its standard library. The direct enumerator explicitly constructs all distinct scattered subsequences of 201 nondecreasing-gap words of expanded length at most 18, tests the lexicographic Lyndon property by comparison with every proper suffix, and compares the brute-force optimum with the formula. It also checks the proposed witness, plus 72 parameterized pattern instances involving constant, triangular, and geometric gaps. The stated tests are reproducible from the embedded standalone script. The infinite assertion follows from the proof above, not from finite experiments.

## Relationship to prior work

Bannai, I, Kociumaka, Köppl, and Puglisi introduced general algorithms for longest Lyndon subsequences, including a cubic-time approach on uncompressed strings. Their original arXiv paper first appeared on 2022-01-18. Full-text inspection of the open-access journal version (introduction, general and special-case algorithms, results) did not identify this monotone binary zero-gap family, the prefix-sum threshold, or its compressed-input formula. Generic algorithms can calculate the answer for a specific expanded word but do not by themselves state this exact family-wide structural identity. Additional literature and mathematical-record searches for run-length encodings, gap markers, and deletion-to-Lyndon variants identified no exact equivalent; an unindexed equivalent is still possible.

## Limitations

This theorem requires positive nondecreasing gaps and alphabet order \(0<1\). It does not cover arbitrary gap order, the lexicographically smallest optimum, the number of optimum subsequences, or the longest *common* Lyndon subsequence of two inputs. The small-instance program is not an independent scientific audit or an infinite proof. An independent audit has not been performed.

## References

1. H. Bannai, T. I, T. Kociumaka, D. Köppl, and S. J. Puglisi, *Computing Longest (Common) Lyndon Subsequences*, arXiv:2201.06773 (first public 2022-01-18), https://arxiv.org/abs/2201.06773.
2. H. Bannai, T. I, T. Kociumaka, D. Köppl, and S. J. Puglisi, *Computing Longest Lyndon Subsequences and Longest Common Lyndon Subsequences*, Algorithmica 86, 735–756 (2024), open-access article first published 2023-05-06, https://doi.org/10.1007/s00453-023-01125-z.
