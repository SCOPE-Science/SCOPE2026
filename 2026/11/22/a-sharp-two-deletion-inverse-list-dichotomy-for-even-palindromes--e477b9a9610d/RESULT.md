# A sharp two-deletion inverse-list dichotomy for even palindromes

## Finding

Let \(\Sigma\) be a labeled alphabet of size \(q\ge2\). For every integer \(m\ge1\), use all length-\(2m\) reversal palindromes as a restricted source family
\[
\mathcal P_{2m}=\{u u^{\mathrm R}:u\in\Sigma^m\}.
\]
For a received word \(z\in\Sigma^{2m-2}\), define its exact-two-deletion inverse list
\[
\mathcal L_m(z)=\{p\in\mathcal P_{2m}:z\text{ is a scattered subsequence of }p\},
\]
where a source palindrome is counted once, independently of how many pairs of deleted positions yield \(z\).

**Theorem (sharp inverse-list dichotomy).** For every \(q\ge2\) and \(m\ge1\):

1. If \(z\) is a palindrome, then \(|\mathcal L_m(z)|=1+m(q-1)\). Its parents are precisely \(v v^{\mathrm R}\), where \(v\) is a distinct one-symbol insertion supersequence of the first half of \(z\).
2. If \(z\) is not a palindrome, then \(|\mathcal L_m(z)|\le2\). Its entire inverse list is obtained by the explicit two-branch reconstruction described in the proof.
3. Thus the exact worst-case inverse-list size is \(1+m(q-1)\), and **exactly** \(q^{m-1}\) distinct received words attain this maximum. For \(m\ge2\) the nonpalindromic bound two is attained, too.

This is a receiver-conditioned statement. No counting of repeated deletion histories, probability law for a random deletion pattern, or claim about arbitrary nonpalindromic source codewords is made.

## Assumptions and scope

Ordinary reversal \(u^{\mathrm R}\) does not complement letters. All sources have length \(2m\), and exactly two arbitrary coordinates, not necessarily adjacent or symmetrically placed, are deleted. Receiver positions and alphabet labels are retained. The empty receiver at \(m=1\) is palindromic. Membership in an inverse list means *existence* of a two-deletion embedding, not a specified deletion pattern.

## Proof

**Lemma 1 (one-deletion rigidity of even palindromes).** An odd-length word has at most one even-length palindromic one-insertion supersequence. Indeed, if it comes from deleting one letter from an even palindrome, the deleted letter is uniquely determined by parity: exactly that letter occurs an odd number of times in the odd-length receiver. For a fixed inserted letter \(a\), two insertions at different positions cannot give different palindromes. Otherwise, between the insertion sites the resulting words are \(aS\) and \(Sa\). If these differ, at their first actual disagreement one palindrome has \(a\) and the other has a non-\(a\) symbol; at their last disagreement the order is reversed. The outermost disagreement indices of two palindromes must be mirror images, which would force the first palindrome to have the same symbol \(a\) at both, a contradiction. If the insertions give the same word there is no ambiguity. Hence at most one distinct parent exists.

**Lemma 2 (symmetric embedding at even length with two omissions).** Let \(p=uu^{\mathrm R}\) be an even palindrome of length \(2m\), and let \(z=xx^{\mathrm R}\) be an even palindrome of length \(2m-2\), where \(m\ge2\). If \(z\preceq p\), then \(x\preceq u\) by a single deletion. To prove this, take any embedding of \(z\) into \(p\), and let \(j\) be the position used for the final letter of its first half \(x\), of length \(m-1\). Since only two positions of \(p\) are omitted, \(j\le m+1\). If \(j\le m\), the first half is already embedded in \(u\). Otherwise \(j=m+1\), and the entire final \(m-1\)-symbol suffix of \(p\) must be used to embed the remaining half \(x^{\mathrm R}\); there are precisely \(m-1\) positions after \(m+1\). This suffix is the reversal of the first \(m-1\) letters of \(u\). Therefore \(x\) equals the first \(m-1\) letters of \(u\), and again \(x\preceq u\). Reflecting any such embedding of \(x\) in \(u\) about the center gives a symmetric embedding of \(z\) in \(p\), omitting a mirror-image pair of coordinates. This lemma is restricted to **even palindromes with exactly two omitted coordinates**; an unrestricted symmetric-embedding assertion for arbitrary palindrome lengths is not needed.

**Palindromic receivers.** Write \(z=x x^{\mathrm R}\), where \(|x|=m-1\). By Lemma 2, a parent \(p=v v^{\mathrm R}\) contains \(z\) precisely when a symmetric pair of coordinates can be removed, equivalently when \(x\) is a one-deletion descendant of \(v\). All such \(v\) arise by inserting one symbol into \(x\). There are \(q m\) insertion histories, and exactly \(m-1\) duplicate histories after identifying adjacent positions across each original letter, leaving \(qm-(m-1)=1+m(q-1)\) distinct inserted words. A direct alternative count starts from the insertion at the end (\(q\) choices) and adds \(q-1\) genuinely new outputs for each of the other \(m-1\) insertion positions. Different halfwords give different full palindromes.

**Nonpalindromic receivers.** Suppose the outer letters of \(z\) agree at a letter \(c\). Every palindrome parent must also start and end with \(c\): if it started and ended with some other letter, both its endpoints would have to be among the exactly two deleted symbols, making the surviving receiver itself a palindrome. Moreover, an embedding can be adjusted to use these matching outer coordinates, so stripping the first and last letters gives a bijection between palindrome parents of \(z\) and those of the shorter receiver. Repeat until the remaining core \(w\) has unequal endpoints \(a\ne b\). (This core is nonempty and even in length.)

A palindrome \(P\) containing \(w\) with exactly two extra letters must begin and end with either \(a\) or \(b\): any third outer letter would consume both deletions and leave a palindromic receiver, contrary to \(a\ne b\). In the branch with outer letter \(a\), its initial \(a\) must be matched to the initial letter of \(w\), and its final \(a\) must be one of the deletions. Thus \(P=aQa\), where \(Q\) is an even palindrome containing the odd word \(w\) with its first letter removed as a one-deletion descendant. Lemma 1 supplies at most one such \(Q\). Similarly the branch with outer letter \(b\) requires \(P=bQ'b\), where \(Q'\) is an even palindrome containing \(w\) with its last letter removed as a one-deletion descendant; Lemma 1 again supplies at most one. Reattaching the stripped symmetric outer shell yields at most two distinct original parents. This is also a complete constructive inverse-list characterization: for each branch, insert the unique odd-multiplicity letter (if it exists) at all positions of the indicated odd word, keep the unique even palindrome if present, then restore the shell and verify subsequence containment.

For sharpness of the nonpalindromic bound, take distinct letters \(a,b\) and the length-\(2m-2\) word \(z=a^{2m-3}b\), for \(m\ge2\). Both palindromes corresponding to halfwords \(ba^{m-1}\) and \(aba^{m-2}\) contain \(z\) after two deletions (for \(m=2\), interpret \(a^{m-2}\) as empty). The two halfwords differ, so the inverse list has two elements by the bound already proved.

Finally, there are exactly \(q^{m-1}\) palindromic receivers of length \(2m-2\). For \(m\ge2\), their list size \(1+m(q-1)\) is at least three, strictly exceeding the nonpalindromic upper bound two. At \(m=1\) the empty receiver is the only receiver and has all \(q\) one-letter halfwords as parents. This proves the maximum and exact number of maximizers for every stated parameter.

## Verification

The standalone `verify.py` implements both exhaustive generation of every two-deletion descendant of every even palindrome and an independent two-branch inverse-list reconstruction. It compares the complete inverse sets for **every** receiver, including receivers with no parents, over alphabet sizes \(2\) through \(5\) and the parameter ranges stated in the script. It also checks the sharp maximum, the exact \(q^{m-1}\) number of maximizers, and attainment of the nonpalindromic bound. Run `python3 verify.py`; the tested package reports `VERIFY_OK cases=22 total_source_words=2609`. Exhaustive finite cases corroborate the general proof rather than replace it.

## Relationship to prior work

Sloane's 2002 survey gives the classical deletion-descendant and deletion-distance definitions and studies single-deletion codes and their run-based geometry. Kulkarni and Kiyavash develop general and constrained-source non-asymptotic code-size bounds; these are bounds on sets of transmitting codewords, rather than complete receiver-specific inverse lists for all even palindromes after exactly two deletions. Earlier work on the one-deletion confusability of palindrome-restricted codebooks proves the even-palindrome one-deletion rigidity used as Lemma 1, but does not cover the present two-deletion inverse-list dichotomy. Results about palindromic *duplication* change the channel operation (inserting a reversed block) rather than restrict the source family to palindromes, and do not automatically imply this theorem.

## Limitations

The theorem does not calculate how many nonpalindromic receivers have lists of size zero, one, or two, nor does it determine the largest two-deletion-correcting subcode of all even palindromes. The decoder's simple insertion scan is quadratic in word length, not claimed optimal. Priority beyond the inspected literature has not been established; an unindexed earlier equivalent remains possible.

## References

1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, arXiv:math/0207197v1, first posted 2002-07-22, https://arxiv.org/html/math/0207197v1, Sections 1 and 5.
2. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128, first posted 2012-11-13, https://arxiv.org/abs/1211.3128.
3. J. Brakensiek, V. Guruswami and S. Zbarsky, *Efficient Low-Redundancy Codes for Correcting Multiple Deletions*, ECCC TR15-116, publicly posted 2015-07-21, https://eccc.weizmann.ac.il/report/2015/116/.
