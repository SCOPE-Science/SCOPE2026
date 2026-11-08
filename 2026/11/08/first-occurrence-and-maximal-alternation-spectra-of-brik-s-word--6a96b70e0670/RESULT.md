# First-occurrence and maximal-alternation spectra of Brik's word

## Finding

Let \(B_1=101\), and for every integer \(i\geq1\) define \(B_{i+1}=B_iB_i[i+1..|B_i|]\), using one-based positions and inclusive intervals. Let \(\mathbf b\) be the infinite word having all \(B_i\) as prefixes. For \(k\geq1\), denote by \(r_k\) the first one-based starting position of \((01)^k\) in \(\mathbf b\). Then
\[
r_1=r_2=2,\qquad r_3=38,\qquad
r_k=2^{r_{k-1}-2}+r_{k-1}-1\quad(k\geq4).
\]
In particular, \(r_4=68\,719\,476\,773\). Every alternating binary factor has an explicitly determined first position. For \(k\geq1\), the first occurrences of the four types are
\[
\begin{array}{c|c}
\text{factor}&\text{first one-based position}\\\hline
(01)^k&r_k\\
(10)^k&r_k-1\\
1(01)^k&r_k-1\\
(01)^k0&r_{k+1}.
\end{array}
\]
The one-letter factors \(1\) and \(0\) first occur at positions \(1\) and \(2\), respectively.

Let \(A_i\) be the maximum length of a contiguous alternating factor of the finite word \(B_i\). Set
\[
q_1=1,\quad q_2=2,\quad q_3=7,\quad q_k=r_{k-1}\ (k\geq4),
\qquad K_i=\max\{k\geq1:q_k\leq i\}.
\]
Then for every integer \(i\geq1\),
\[
A_i=2K_i+1.
\]
For example, \(A_1=3\), \(A_i=5\) for \(2\leq i\leq6\), \(A_i=7\) for \(7\leq i\leq37\), and \(A_i=9\) for \(38\leq i<r_4\). These are exact statements for all stages and all alternating factor lengths, not finite-range extrapolations.

## Assumptions and scope

Strings are binary; factors are contiguous, with overlapping occurrences allowed. An alternating string is one whose adjacent symbols differ. All positions here are one-based. For the finite-word maximum \(A_i\), only factors wholly contained in \(B_i\) are counted. Define \(\ell_i=|B_i|\); direct induction gives \(\ell_i=2^{i-1}+i+1\). No assumption is made about probabilistic normality or about the frequency of alternating factors.

## Proof

**Step 1: Basic boundaries.** Each \(B_i\) begins with \(101\), ends with \(01\), and avoids \(00\). These hold for \(B_1\); the appended block is a suffix of \(B_i\), and its join is preceded by a \(1\). Since \(B_3=10101101\) ends in \(1101\), and \(\ell_i-i=2^{i-1}+1\geq5\) for \(i\geq3\), induction also gives that every \(B_i\), \(i\geq3\), ends in \(1101\). These facts pass to \(\mathbf b\), with \(\mathbf b\) starting in \(1\) and containing no \(00\).

**Step 2: The only new crossing site.** Fix \(k\geq3\) and \(i\geq3\). Every length-\(2k\) factor of \(B_{i+1}=B_iB_i[i+1..\ell_i]\) that is wholly inside either block already occurs in \(B_i\). Thus the *first appearance* of \((01)^k\), after stage \(3\), must cross the displayed join. The suffix \(1101\) of \(B_i\) has only one zero in its maximal alternating suffix: that at position \(\ell_i-1\). Consequently the sole possible crossing start of \((01)^k\) is \(\ell_i-1\). The two letters on the left are \(01\), so the crossing occurs precisely when the appended suffix begins with \((01)^{k-1}\), and has at least \(2k-2\) letters available. Equivalently, \(\mathbf b\) has \((01)^{k-1}\) at position \(i+1\) with enough of that occurrence inside \(B_i\). The earlier exceptional joins can be checked directly in \(B_3\), which has no \((01)^3\) or longer alternating even factor starting in \(0\).

**Step 3: Bases.** The first \(01\) in \(B_1\) is at position \(2\). The first \(0101\) is also at position \(2\), in \(B_2=10101\). Direct inspection of

`B6 = 101011010110111010110110101101110101101`

shows no \(010101\). The first occurrence of \(0101\) starting at position at least \(4\) is position \(7\), and \(B_6[7..10]=0101\). Appending the suffix beginning at position \(7\) to \(B_6\), whose length is \(39\), creates \(010101\) at position \(38=39-1\) of \(B_7\). It is the first such factor, establishing \(r_3=38\), with first-containing stage \(q_3=7\).

**Step 4: Induction and exact first position.** Suppose \(k\geq4\) and the first position \(r_{k-1}\) is known. Every possible first appearance of \((01)^k\) at a join with index \(i\geq3\) requires an occurrence of \((01)^{k-1}\) beginning at \(i+1\), hence \(i+1\geq r_{k-1}\). At \(i=r_{k-1}-1\) the required source substring is present: its last position is \(r_{k-1}+2k-3\), whereas \(\ell_i\) is exponentially larger, and \(\ell_i-i=2^{i-1}+1\geq2k-2\). The inequality holds at \(r_3=38,k=4\) and thereafter since the derived \(r_k\) grow strictly faster than \(k\). Thus the first appearance is in \(B_{r_{k-1}}\), at start \(\ell_{r_{k-1}-1}-1\). The length formula gives \(r_k=2^{r_{k-1}-2}+r_{k-1}-1\), and the first-containing stage is \(q_k=r_{k-1}\). This also proves inductively that every \((01)^k\) occurs.

**Step 5: All orientations and parities.** Since \(\mathbf b\) begins with \(1\) and avoids \(00\), every occurrence of \((01)^k\) is preceded by \(1\); every occurrence of \((10)^k\) ends in \(0\) and is followed by \(1\). Therefore occurrences of \((01)^k\) and \((10)^k\) correspond bijectively by shifting the start left by one. The same shifted starts are exactly those of \(1(01)^k\). Finally, each \((01)^k0\) is followed by \(1\), making an occurrence of \((01)^{k+1}\), and the converse follows by truncation. Taking first starts yields the four formulas.

**Step 6: Maximum alternation in finite stages.** Every \(B_i\) begins and ends with \(1\) and avoids \(00\). An alternating factor starting or ending with \(0\) can be extended to the adjacent \(1\), unless it was not maximal. Consequently every longest alternating factor has shape \(1(01)^k\) and length \(2k+1\). Such a factor appears if and only if \((01)^k\) appears, because each occurrence of the latter is preceded by \(1\). The preceding construction shows that the earliest finite stage containing \((01)^k\) is exactly \(q_k\). Maximizing over the attained \(k\) gives \(A_i=2K_i+1\).

## Verification

Run `python3 check_alternation.py` from this package. The checker directly constructs \(B_1,\ldots,B_{19}\), compares literal earliest occurrences for both orientations and all alternating factor lengths at most eight with the proved formulas, independently scans maximal alternating run lengths, and checks the necessary boundary data at \(B_6\) and \(B_7\). It separately checks the huge integer \(r_4\) and its finite source window. It does not try to construct the astronomical word \(B_{38}\), and no finite computation is used as an infinite proof.

## Relationship to prior work

Shallit, *Brik's sequence: a strange recursion* (May 8, 2026), establishes the recursive construction, recurrence and golden-mean factor language, and the first-occurrence positions of constant words \(1^k\). The present result instead derives the full first-occurrence spectrum for *alternating* words, together with the exact maximum alternating length in every finite construction stage. The constant-word recurrence is not a statement about these alternating positions. The OEIS entry A334820 also records the sequence and the first appearances of constant runs, but not the alternating spectrum. No equivalence to a previously proved formula for these alternating positions was identified in the inspected material.

## Limitations

The first-occurrence formulas are specific to alternating binary factors in Brik's word, not arbitrary legal factors and not an exact count of all occurrences. The finite-stage result concerns complete iterates \(B_i\), not arbitrary prefix lengths. The argument is an ordinary mathematical proof with finite computational checks; no independent audit has been performed. Historical priority outside the inspected sources remains a residual risk.

## References

1. J. Shallit, *Brik's sequence: a strange recursion*, arXiv:2605.07542v1, first publicly posted 2026-05-08, https://arxiv.org/html/2605.07542 .
2. N. J. A. Sloane et al., OEIS A334820, *Replication binary sequence*, https://oeis.org/A334820 , consulted for comparison of recorded properties.
3. K. Ryde, *Code for OEIS A334820*, 2020/2021, https://user42.tuxfamily.org/seq-A334820/index.html , context for the original replication sequence.
