# The mismatch-gap basis for common factors of cyclic run words

## Finding

For an integer \(q\ge 2\), pairwise distinct letters \(c_0,\ldots,c_{q-1}\), and two positive integral run profiles \(\mathbf a=(a_0,\ldots,a_{q-1})\) and \(\mathbf b=(b_0,\ldots,b_{q-1})\), set
\[
X=(c_0^{a_0}\cdots c_{q-1}^{a_{q-1}})^\omega,\qquad
Y=(c_0^{b_0}\cdots c_{q-1}^{b_{q-1}})^\omega.
\]
Let \(D=\{i:a_i\ne b_i\}\). Suppose \(D\ne\varnothing\). For every \(i\in D\), let \(j\) be the next element of \(D\) encountered *strictly after* \(i\) in the forward cyclic index order, returning to \(i\) after a full circuit if \(D=\{i\}\). Form the finite word
\[
F_i=c_i^{\min(a_i,b_i)}
\left(\prod_{h\in(i,j)_{\rm cyc}}c_h^{a_h}\right)
 c_j^{\min(a_j,b_j)},
\]
where \((i,j)_{\rm cyc}\) lists the strictly intermediate cyclic indices in their forward order; these have equal run lengths in both profiles. If \(i=j\), the intermediate list has \(q-1\) entries.

**Theorem.** With \(\operatorname{Fac}(Z)\) denoting the finite contiguous factors of \(Z\), including the empty word, one has
\[
\operatorname{Fac}(X)\cap\operatorname{Fac}(Y)
=\bigcup_{i\in D}\operatorname{Fac}(F_i).
\]
The words \(F_i\), for \(i\in D\), are pairwise distinct and are **exactly** the maximal common nonempty factors under the ordinary substring-inclusion order. Hence their number is precisely \(|D|\), and the maximum common-factor length is
\[
L=\max_{i\in D}\left(\min(a_i,b_i)
+\sum_{h\in(i,j)_{\rm cyc}}a_h
+\min(a_j,b_j)\right).
\]
If \(D=\varnothing\), the words \(X,Y\) coincide: their common-factor language is infinite, has arbitrarily long words, and has no maximal finite factor. No finite common-factor basis is claimed in that case.

## Assumptions and scope

All statements concern **contiguous factors**, not scattered subsequences and not one-occurrence alignment records. The two infinite words are purely periodic, with a shared cyclic ordering of \(q\) pairwise distinct letters, and may have unrelated positive run lengths. Factors may start at any offset of either infinite word. The strings \(F_i\) are finite, nonempty, and their factor languages are ordinary sets of distinct words. The same formula applies to both \(q=2\) and larger alphabets, to one mismatch, to adjacent mismatches, and to arbitrarily large lengths.

## Proof

**1. Alignment by transitions.** Because each letter occurs in exactly one run in a fundamental period, an occurrence of a two-letter transition \(c_hc_{h+1}\) fixes the cyclic run index \(h\) in either infinite word (indices taken modulo \(q\)). Thus, once a factor passes any transition, the sequence of letter runs it traverses has the same cyclic index sequence in \(X\) and \(Y\). Every *interior* run of a factor—one preceded and followed within the factor by different letters—is necessarily the entire run of that indexed letter. If the factor is common, the lengths of all such interior runs must agree between the two profiles. Therefore no mismatching run can be an interior run of a common factor.

**2. Construction and commonality.** Fix successive mismatching indices \(i,j\) as defined above. All intermediate cyclic runs have identical length in both words. Take the last \(\min(a_i,b_i)\) copies of \(c_i\), then all intermediate full runs, then the first \(\min(a_j,b_j)\) copies of \(c_j\). This produces the same contiguous word \(F_i\) in both \(X\) and \(Y\), even when \(j=i\) and the two endpoint portions lie in consecutive occurrences of the same run type. Hence each \(F_i\) and all its factors occur in both words.

**3. Exhaustion.** Let \(U\) be a nonempty common factor. If \(U\) contains a transition, use step 1 to align all its constituent runs by cyclic index. Its interior run indices are necessarily outside \(D\). Thus any mismatching run touched by \(U\) can occur only at its left or right end. Choose the mismatching run just before or containing its leftmost run and the next mismatching run strictly after it, increasing cyclic index from left to right; the consecutive mismatch interval can be chosen to contain the entire run-index span of \(U\). At either mismatching endpoint, \(U\) uses no more than the shorter run length (as otherwise it could not occur in both words). Its left endpoint part is a suffix whenever followed by a transition; its right endpoint part is a prefix whenever preceded by a transition. Therefore \(U\) embeds contiguously in the corresponding \(F_i\). If \(U\) is a single constant-letter run, that letter appears in at least one \(F_i\): every cyclic index is either mismatching or between two consecutive mismatches, and \(F_i\) contains at least \(\min(a_h,b_h)\) copies of each index it covers. Again \(U\) is a factor of one \(F_i\). This proves the language equality.

**4. Maximality.** The word \(F_i\) contains a transition because \(q\ge2\) and \(i\) is followed by the next mismatch (possibly itself one full circuit later). Consequently its occurrences have the cyclic run phases determined in step 1. The initial \(c_i\)-block is the terminal portion of run \(i\). In whichever of \(X,Y\) has the shorter \(i\)-run, its immediately preceding letter is \(c_{i-1}\); in the other, its preceding letter is \(c_i\). These disagree. Analogously, the final \(c_j\)-block is the initial portion of run \(j\). Its next letter is \(c_{j+1}\) in the word with the shorter \(j\)-run and \(c_j\) in the other. Hence neither a left nor a right extension of \(F_i\) is common. No strictly longer common word can contain \(F_i\), since a one-letter left or right extension of it would then be common. Therefore each \(F_i\) is inclusion-maximal. Conversely, the factor-language equality shows that every inclusion-maximal common word must equal one of the \(F_i\). Finally the first letter of \(F_i\) is \(c_i\), and distinct mismatching indices have distinct letters, proving pairwise distinctness. The count and maximum-length formula follow.

## Verification

Run the standalone Python standard-library program `verify.py` as `python3 verify.py`. It constructs the conjectured basis and independently enumerates factors from both finite prefixes long enough to cover every cyclic starting position through the predicted cutoff plus one letter. It compares the entire computed common-factor set against the candidate union and separately checks the inclusion-maximal elements. The deterministic program passed \(2684\) profile pairs: exhaustive pairs with \(q=2\) and run lengths through \(5\), \(q=3\) through \(3\), \(q=4,5\) through \(2\), plus \(150\) seeded larger trials through \(q=9\). The finite computation tests, but does not establish, the theorem for unbounded parameters; the proof above supplies that quantification.

## Relationship to prior work

Amir and Boneh introduced occurrence-based *locally maximal common factors* for dynamic longest-common-factor algorithms (CPM 2018, DOI below), including a periodic-input algorithm. Those are not the inclusion-maximal common **words** of two infinite cyclic run words classified here. Alzamel and coauthors (2019) treated a longest-common-*circular*-factor problem, permitting a cyclic shift of a finite factor. Charalampopoulos and coauthors (2021) developed fast algorithms for the general finite longest-common-substring problem. Lee and Lin (2023) gave quantum algorithms on run-length-encoded strings. These works supply context and more general algorithmic methods, but their inspected statements do not give the mismatch-gap list of every maximal common word, its exact cardinality, and the associated infinite-periodic cutoff under this symbolic run-order hypothesis. This is a best-knowledge literature comparison, not a guarantee of uniqueness among all possible unpublished or unindexed results.

## Limitations

The theorem does not cover differing permutations of run labels, repeated appearances of one letter within a period, nonperiodic words, approximate matching, or scattered subsequences. Its new content is the exact structure of the common-factor language for the specified natural paired family, not an asymptotically faster algorithm for arbitrary strings. The generated basis has \(|D|\) members, but explicitly writing every letter may require time proportional to the decoded output size; the run-length representation has only \(O(q)\) total run entries if endpoints are stored symbolically. No independent audit has been performed.

## References

- A. Amir and I. Boneh, “Locally Maximal Common Factors as a Tool for Efficient Dynamic String Algorithms,” CPM 2018. https://doi.org/10.4230/LIPIcs.CPM.2018.11 (public 2018-05-18).
- M. Alzamel et al., “Quasi-Linear-Time Algorithm for Longest Common Circular Factor,” arXiv:1901.11305 (first public 2019-01-31). https://arxiv.org/abs/1901.11305.
- P. Charalampopoulos, T. Kociumaka, S. P. Pissis, and J. Radoszewski, “Faster Algorithms for Longest Common Substring,” arXiv:2105.03106 (first public 2021-05-07). https://arxiv.org/abs/2105.03106.
- T.-C. Lee and H.-H. Lin, “A sublinear time quantum algorithm for longest common substring problem between run-length encoded strings,” arXiv:2310.00966 (first public 2023-10-02). https://arxiv.org/abs/2310.00966.
