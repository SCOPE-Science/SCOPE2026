# A sharp four-marker ceiling for palindromic periodicities in gap-distinct binary words

## Finding

Let \(w\) be a nonempty binary word. Call the complete zero-gaps of \(w\) *distinct* if the numbers of zeros between successive occurrences of the symbol \(1\) are pairwise different. A *palindromic periodicity* (in the sense of Fici, Shallit, and Simpson) is a word \(w\) for which there exist possibly empty palindromes \(u,v\), with \(|uv|\ge1\) and \(|uv|\le |w|\), such that \(w\) is a prefix of the periodic word \((uv)^\omega\).

**Theorem (complete classification).** Suppose the complete zero-gaps of \(w\) are pairwise distinct. Let \(m\) be its number of occurrences of \(1\). Then:

1. If \(m\le2\), the word is a palindromic periodicity.
2. If \(m=3\), write \(w=0^a1\,0^b1\,0^c1\,0^e\), with \(b\ne c\) and nonnegative integer parameters. The word is a palindromic periodicity **if and only if**
   \[
   \big(\max(a,e)\le b\le a+e\big)
   \ \lor\ \big(\max(a,e)\le c\le a+e\big)
   \ \lor\ \big(a\le c\ \land\ e\le b\big).
   \]
3. If \(m=4\), write \(w=0^a1\,0^b1\,0^c1\,0^d1\,0^e\), where \(b,c,d\) are pairwise distinct nonnegative integers. Then \(w\) is a palindromic periodicity **if and only if**
   \[
   \max(a,e)\le c\le a+e.
   \]
4. If \(m\ge5\), the word is **not** a palindromic periodicity.

The last bound is best possible: \(0100100010000100\) has four occurrences of \(1\), has distinct complete zero-gaps \(2,3,4\), and is the product of the two palindromes \(010010\) and \(0010000100\).

Consequently the palindromic-periodicity predicate in this class is computable in linear time in the number of explicitly listed gaps, and in constant additional arithmetic time once the distinct-gap promise and the boundary lengths are given.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). The word is nonempty; zero-gaps between successive ones are allowed to have length zero, and the external zero-runs may be empty. No monotonicity, positivity, periodicity, or upper bound is assumed for the complete zero-gaps, only pairwise inequality. The empty palindrome is permitted in the definition, but the period itself must be nonempty. This matches the symmetric-word-period formulation in the cited 2024 treatment. The statement concerns a single finite word, and therefore also applies to any factor of an infinite binary word whose consecutive complete zero-gap lengths are pairwise distinct.

## Proof

We use four elementary facts. **(A)** A word \(z\) is a product of two palindromes if and only if it is a cyclic conjugate of its reverse (a *symmetric word*). The definition immediately says that \(w\) is a palindromic periodicity exactly when it has a symmetric word-period \(z\) of length \(1\le |z|\le|w|\). **(B)** Every word-period of length \(p\) corresponds to a border (equal prefix and suffix) of length \(\ell=|w|-p\); the border can be empty. **(C)** For any binary cyclic word with \(r\) occurrences of \(1\), its consecutive circular zero-gap list has dihedral reflection symmetry if and only if that binary word is symmetric. This follows by considering the action of word reversal on the circular positions of the indistinguishable ones: reverse conjugacy is precisely reversal of the cyclic ordered gap list up to rotation.

**(D) Reflection restrictions.** With \(r\ge3\) ones and pairwise distinct *circular* gaps, symmetry is impossible: every reflection of an \(r\)-cycle transposes at least one pair of gap positions. For \(r\ge5\), any reflection transposes at least two disjoint pairs, so a circular list whose entries are all distinct except possibly one repeated value cannot be symmetric. For \(r=3\), a three-entry gap list is symmetric exactly when some two entries agree. For \(r=4\), a list \((b,c,d,t)\) with pairwise distinct \(b,c,d\) is symmetric exactly when \(t=c\), since the sole allowable transposed pair lies at the two opposite positions occupied by \(c\) and \(t\). These assertions follow by enumerating the possible reflection axes of a triangle or quadrilateral.

Now write the positions of the \(m\) ones in increasing order, the complete zero-gaps as \(g_1,\ldots,g_{m-1}\), and the leading and trailing zero lengths as \(a,e\). For any *proper* word-period of \(w\), the corresponding border cannot contain two occurrences of \(1\). Indeed, the two identical copies of the border would each contain the same complete gap between two successive ones, but at two different positions of \(w\), contradicting pairwise distinct complete zero-gaps. Thus the border contains either zero or one occurrence of \(1\).

**Zero-one border case.** If the border is made entirely of zeros, it has length \(0\le\ell\le\min(a,e)\). The period \(z=w[0..|w|-\ell)\) then contains all \(m\) ones, with circular zero-gaps
\[
(g_1,\ldots,g_{m-1},a+e-\ell).
\]
Conversely every such \(\ell\) gives a genuine border and word-period. The last component varies through every integer in the closed interval \([\max(a,e),a+e]\). Applying (D): for \(m=3\) a symmetric period exists exactly when this interval contains either \(g_1\) or \(g_2\); for \(m=4\) exactly when it contains \(g_2\); and for \(m\ge5\) none exists. All sufficiency assertions use a concrete word-period corresponding to \(\ell=a+e-g_i\).

**One-one border case.** If a proper border contains exactly one occurrence of \(1\), its prefix occurrence must be the *first* one and its suffix occurrence the *last* one. Since the word begins with \(0^a1\) and ends with \(10^e\), the only possible such border is \(0^a1\,0^e\). It exists exactly when \(a\le g_{m-1}\) and \(e\le g_1\) (here \(m\ge2\)). Deleting this suffix leaves a word-period containing \(m-1\) ones whose circular zero-gaps are *exactly* \((g_1,\ldots,g_{m-1})\): its last trailing zero-run plus its initial \(0^a\) has length \(g_{m-1}\). These gaps are pairwise distinct. If \(m\ge4\), fact (D) excludes symmetry. When \(m=3\), the period has exactly two ones; every binary circular word with two ones is symmetric, so the stated inequalities are sufficient and necessary for this case.

Finally, when \(m\le2\), the full word itself is symmetric: with zero or one occurrence of \(1\) its circular word is a single-run pattern, and with two ones reversal only exchanges its two circular gaps, which is a cyclic rotation. This proves all four cases, including both directions and the exact boundaries. \(\square\)

## Verification

The included `verify.py` uses only the Python standard library. Run `python3 verify.py` from the extracted directory. It independently evaluates the literal definition by examining every possible period and every possible split of its root into two palindromes. It checks all qualifying nonempty binary words of lengths at most \(18\), totaling \(19,530\) words, and compares the classification with this direct decision. It also checks \(600\) seeded, gap-distinct random words; for \(150\) of them a second decision routine compares each root to a rotation of its reverse. Explicit sharp four-marker and forbidden five-marker witnesses are also checked. The run printed `PASS: all finite checks complete` and completed successfully. These tests are not substituted for the universal proof above.

## Relationship to prior work

Simpson's 2024 paper introduced palindromic periodicities and studied their interaction with periods and palindrome centers. Fici, Shallit, and Simpson's 2024 preprint (and its 2025 open-access conference version) establishes the equivalence with having a symmetric word-period, studies Sturmian/trapezoidal and automatic-word families, and gives general counting results. Borchert and Rampersad's 2015 paper concerns palindrome pairs themselves, including their factors and minimal non-pairs. The present theorem uses the established symmetric-period characterization, but gives a complete, sharp arithmetic classification for the separate class defined by pairwise unequal full marker gaps; it does not identify a new characterization of palindromic periodicity in arbitrary words. The 2025 paper's results for specific classical infinite sequences and extremal counts do not yield the inequalities above. This comparison is limited to the inspected published texts and does not rule out unindexed equivalent observations.

## Limitations

The distinct-gap hypothesis is essential to the border restriction and the reflection argument. Repeated complete gaps can permit palindromic periodicities with arbitrarily many ones, for example powers of \(01\). The statement gives a decision criterion, not an exact count of distinct palindromic-periodicity factors of each length in a particular infinite sequence. Independent scientific validation has not been carried out.

## References

1. J. Simpson, *Palindromic Periodicities*, first public arXiv version 2024-02-08, https://arxiv.org/abs/2402.05381.
2. G. Fici, J. Shallit, J. Simpson, *Some Remarks on Palindromic Periodicities*, first public arXiv version 2024-07-15, https://arxiv.org/abs/2407.10564. Published as *On Palindromic Periodicities*, CPM 2025, https://doi.org/10.4230/LIPIcs.CPM.2025.11.
3. A. Borchert and N. Rampersad, *Words with many palindrome pair factors*, first public arXiv version 2015-09-17, https://arxiv.org/abs/1509.05396.
