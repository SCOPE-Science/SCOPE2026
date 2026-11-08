# Exactly \(q\) longest Lyndon subsequences of distinct-run powers

## Finding

Let \(q\ge 2\), let \(c_0,c_1,\ldots,c_{q-1}\) be pairwise distinct letters from a totally ordered alphabet, with \(c_0\) the least of these letters, and let \(a_0,\ldots,a_{q-1}\ge 1\) be integers. Define
\[
P=c_0^{a_0}c_1^{a_1}\cdots c_{q-1}^{a_{q-1}},\qquad p=\sum_{i=0}^{q-1}a_i,\qquad W=P^k\quad(k\ge2).
\]
A Lyndon word is strictly lexicographically smaller than every nonempty proper suffix. A subsequence need not occupy consecutive positions.

**Theorem.** The longest Lyndon scattered subsequences of \(W\) have length \(kp-1\). Every such subsequence comes from deleting exactly one position. The complete set of qualifying deletion positions is:

- If \(0\le i<q-1\) and \(c_{i+1}<c_i\), delete any position in run \(i\) of the **first** copy of \(P\).
- If \(0\le i<q-1\) and \(c_i<c_{i+1}\), delete any position in run \(i\) of the **last** copy of \(P\).
- Delete any position in the last run \(i=q-1\) of the **first** copy of \(P\).

No other single-position deletion gives a Lyndon word. Exactly \(p\) deletion **positions** qualify, and their outputs comprise exactly \(q\) **distinct words**. Both counts are independent of \(k\), and the number \(q\) of distinct optimum subsequences is independent of the positive run lengths and the order of the nonminimum letters.

For example, with \(P=0^2 2^3 1^2\) and \(k=3\), the first-copy runs labeled \(2\) and \(1\), and the last-copy run labeled \(0\), are precisely the qualifying deletion runs. There are seven qualifying positions but only three distinct longest Lyndon subsequences.

## Assumptions and scope

The alphabet is totally ordered and only the relative ordering of \(c_0,\ldots,c_{q-1}\) matters. Adjacent runs are of distinct letters, every letter occurs in exactly one run per copy, and \(c_0\) is the minimum. The word \(P\) need not list its other letters increasingly. Position numbers begin at \(1\), and copy numbers run from \(1\) to \(k\). The claim is **not** made for arbitrary repeated-letter base words, for cyclic rotations beginning in a nonminimum run, or for \(k=1\).

## Proof

**Step 1: a sharp upper bound.** The nonempty proper suffix \(P^{k-1}\) is a proper prefix of \(W=P^k\). Consequently \(W\) is not Lyndon, so a Lyndon subsequence has length at most \(kp-1\). Every length-\(kp-1\) subsequence deletes exactly one original position.

**Step 2: the lexicographic comparison at one shortened run.** For \(0\le i\le q-1\), let \(P_i^-\) denote \(P\) with one occurrence of \(c_i\) removed from run \(i\); the result is independent of the chosen position inside that run. For the infinite periodic extensions, compare \(P_i^-P^\omega\) with \(P^\omega\). All symbols agree until the deleted symbol's location. For \(i<q-1\), the former then has \(c_{i+1}\), while the latter has \(c_i\), irrespective of whether the run disappears. For \(i=q-1\), the former then has \(c_0\), while the latter has \(c_{q-1}\). These letters differ. Therefore the shortened first-copy word is smaller precisely when \(i=q-1\), or \(i<q-1\) and \(c_{i+1}<c_i\).

For a shortened **last** copy, compare an intact \(P\) to \(P_i^-\). For \(i<q-1\), the first differing letters are \(c_i\) in \(P\) and \(c_{i+1}\) in \(P_i^-\); thus the intact copy is smaller precisely when \(c_i<c_{i+1}\). If \(i=q-1\), \(P_i^-\) is a proper prefix of \(P\), so the shortened final suffix is smaller than the full word.

**Step 3: no deletion in a middle copy succeeds.** Suppose \(1<b<k\) and the deletion is in copy \(b\). The resulting word still begins with \(P\) and ends with the untouched last copy \(P\). This last \(P\) is a proper suffix equal to a prefix of the whole word, so the resulting word is not Lyndon.

**Step 4: first-copy deletions.** If the first run is shortened, the word begins with fewer than \(a_0\) copies of the minimum letter \(c_0\) (possibly none), whereas the suffix starting at copy \(2\) begins with \(a_0\) copies. The full word is then lexicographically greater than that suffix, so this deletion fails. If a different first-copy run \(i\ge1\) is shortened, the initial \(c_0\)-run remains of length \(a_0\). Any proper suffix beginning in a run with another letter is greater immediately. A suffix beginning strictly inside a \(c_0\)-run has fewer than \(a_0\) leading copies of \(c_0\), hence is greater. The only remaining proper suffixes start at a later complete run of \(c_0\), namely at the starts of copies \(2,\ldots,k\). Each is compared at the first shortened run as in Step 2. Therefore the deleted word is Lyndon exactly when the shortened first-copy periodic comparison is smaller, yielding the stated descending-run and final-run rule.

**Step 5: last-copy deletions.** The full first copy \(P\) remains unchanged. Every proper suffix beginning inside a minimum-letter run, or beginning with a larger letter, is greater for the same initial-run reason. For suffixes starting at complete copies \(2,\ldots,k\), cancel the shared initial full copies: the first difference is between an intact \(P\) and the shortened final \(P_i^-\), or the shortened word is a proper prefix as described in Step 2. Hence all these suffixes are greater exactly when the deleted run is \(i<q-1\) and \(c_i<c_{i+1}\). This establishes the stated rule and excludes every other deletion.

**Step 6: both counts.** Every index \(i<q-1\) is either an ascent or a descent, never both, so exactly one of its two endpoint copies contributes all \(a_i\) positions. The final run contributes all \(a_{q-1}\) positions in the first copy. Thus the total is \(\sum_i a_i=p\). Removing any one position within a fixed run produces the same word. Removing positions carrying different letters produces words with different Parikh vectors. Thus there are exactly \(q\) different qualifying words. At least one exists (the final first-copy run), so the upper bound in Step 1 is attained. \(\square\)

## Verification

Run `python3 verify.py` in the directory containing this document and the source file. The checker independently constructs the complete list of every one-position deletion, tests the Lyndon condition against **all** nonempty proper suffixes, and compares the observed deletion positions and distinct optimum outputs with the formula. It exhaustively considers \(q=2,3,4\), every order with the least letter first, run lengths in \(\{1,2,3\}\), and \(k\in\{2,3,4\}\), giving \(1647\) parameter configurations. It also includes additional reproducible, seeded tests. This finite computation is a check, not a proof of the universal quantifiers.

## Relationship to prior work

Bannai, I, Kociumaka, Köppl and Puglisi introduce general algorithms for the longest Lyndon subsequence problem in their 2022 preprint and 2023 openly available journal article. Their Theorem 5 treats words in which **each symbol appears once**, whereas the present periodic-run family repeats every symbol in each of at least two copies. Their main general algorithm yields the optimum length algorithmically, but does not state this deletion-location classification, the exact \(p\) qualifying positions or the \(q\) distinct optimal outputs for this family. The proof here uses the standard suffix characterization of Lyndon words rather than claiming that characterization as new.

Urabe and collaborators' 2018 result concerns the longest Lyndon **substring** after an edit, not scattered subsequences. Existing classifications of longest Lyndon subsequences in monotone-gap binary words address a different family with one minimum letter recurring at multiple separated runs; no implication of this theorem is known from those statements. Neither titles nor an absence of matching search results establish novelty.

## Limitations

The result characterizes the maximum length and **all** maximizers only for powers of a distinct-letter run cycle starting with its least letter. It does not characterize shorter Lyndon subsequences, arbitrary circular phases, or arbitrary primitive words. Independent bibliographic and scientific review has not been performed; an equivalent result in unindexed literature cannot be ruled out. All checking reported here is finite, separate from the proof.

## References

1. H. Bannai, T. I, T. Kociumaka, D. Köppl, S. J. Puglisi, *Computing Longest (Common) Lyndon Subsequences*, arXiv:2201.06773 (first posted 2022-01-18), https://arxiv.org/abs/2201.06773 . Open full article: *Algorithmica* (online 2023-05-06), https://doi.org/10.1007/s00453-023-01125-z .
2. Y. Urabe, Y. Nakashima, S. Inenaga, H. Bannai, M. Takeda, *Longest Lyndon Substring After Edit*, CPM 2018, https://doi.org/10.4230/LIPIcs.CPM.2018.19 .
3. A. Glen, J. Simpson, W. F. Smyth, *Counting Lyndon Factors*, arXiv:1701.00928 (2017), https://arxiv.org/abs/1701.00928 .
