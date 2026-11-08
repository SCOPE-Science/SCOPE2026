# Affine occurrence laws and universal return gaps for unbordered factors of generalized period-doubling words

## Finding

For every integer \(b\ge3\) and every integer \(n\ge2\), both unbordered length-\(n\) factors of the generalized period-doubling word have explicitly determined occurrence positions, common natural density, and the same normalized sequence of consecutive return gaps. The two-factor classification itself is due to Goč, Mousavi and Shallit (2012); the assertions proved here concern its occurrence geometry.

Write \(p_b(j)=\nu_b(j+1)\bmod2\), where \(\nu_b(m)=\max\{e\ge0:b^e\mid m\}\), and let \(Z_b=\{j\ge0:p_b(j)=0\}\). Let \(U_n^+\) be the unique unbordered length-\(n\) factor beginning in \(1\) and ending in \(0\), and let \(U_n^-=(U_n^+)^R\). Define \(h_b(1)=0\), and for \(n\ge2\) put

\[
 m=\lceil n/b\rceil,\qquad d=bm-n,\qquad h_b(n)=h_b(m)+1.
\]

Initialize the *virtual* residues \(r_1^+=r_1^-=0\); the length-one seed is not a claim that the two length-one factors coincide. Recursively define

\[
 r_n^+=b r_m^-+b-1,\qquad r_n^-=b r_m^++d.
\]

Then the following are exact equalities of sets, not merely eventual descriptions:

\[
 \operatorname{Occ}_{p_b}(U_n^\pm)
 =\{b^{h_b(n)}j+r_n^\pm:j\in Z_b\}.
\]

Both factors therefore have natural starting-position density

\[
 \boxed{\operatorname{dens}\operatorname{Occ}_{p_b}(U_n^\pm)
       =\frac{1}{(b+1)b^{h_b(n)-1}}.}
\]

Their first occurrences begin precisely at \(r_n^+\) and \(r_n^-\). Enumerate either occurrence set increasingly as \(i_0<i_1<\cdots\). Every consecutive return gap \(i_{j+1}-i_j\) belongs to \(\{b^{h_b(n)},2b^{h_b(n)}\}\). The proportions of short and long gaps among the first \(J\) gaps converge to \(1-1/b\) and \(1/b\), respectively, as \(J\to\infty\). More strongly, dividing the entire ordered gap sequence by \(b^{h_b(n)}\) produces **exactly** the same one-or-two sequence for every \(n\ge2\) and both orientations (the gap sequence of increasing elements of \(Z_b\)).

## Assumptions and scope

Throughout \(b\) is an arbitrary integer at least three, not necessarily prime, \(n\ge2\), and all word positions are zero-indexed. A nonempty word is *unbordered* if no nonempty proper prefix is also a suffix. For a finite word \(u\), \(\operatorname{Occ}_{p_b}(u)=\{i\ge0:p_b(i)\cdots p_b(i+|u|-1)=u\}\). Natural density means the limit of the count in \([0,N)\), divided by \(N\), as \(N\to\infty\). A return gap is the difference between consecutive starting positions, not the full intervening return word.

The base-\(b\) valuation is defined by divisibility by powers of the whole integer \(b\), even when \(b\) is composite. The generalized period-doubling word is the fixed point of

\[
 \varphi_b(0)=0^{b-1}1,\qquad \varphi_b(1)=0^b.
\]

This morphic identity and the fact that precisely two unbordered factors of each positive length occur, as mutual reversals, are Theorems 5.3 and 5.4 of Goč–Mousavi–Shallit (2012). These pre-existing statements are inputs, not claimed new results.

## Proof

**1. The marker rule.** For \(q\ge0\) and \(0\le t<b-1\), \(p_b(bq+t)=0\), while \(p_b(bq+b-1)=1-p_b(q)\), since \(\nu_b(b(q+1))=1+\nu_b(q+1)\). Consequently the only possible positions containing \(1\) are final positions of length-\(b\) substitution blocks. Each such final *marker* is the complement of its parent letter. All other positions within a block are zero. This rule holds at the origin and at every subsequent position.

**2. Explicit factor construction.** Define a virtual \(U_1^+=U_1^-=0\) solely for the induction. For \(n\ge2\), with \(m=\lceil n/b\rceil\) and \(d=bm-n\), define

\[
 U_n^+=\varphi_b(U_m^-)[b-1:]\,0^{b-1-d},
 \qquad U_n^-=\varphi_b(U_m^+)[d:].
\]

Here \([a:]\) means delete the first \(a\) symbols, and the first word's added tail is nonnegative in length. Both words have length \(n\). For \(2\le n\le b\), these formulas give \(U_n^+=10^{n-1}\) and \(U_n^-=0^{n-1}1\), which are unbordered. When \(m\ge2\), the identity \(0^{b-1}\varphi_b(x)^R=\varphi_b(x^R)0^{b-1}\) (Goč–Mousavi–Shallit, Lemma 1) shows the two constructions remain reversals. If \(U_m^+=1x0\) is unbordered, then \(U_n^-=0^{b-d}\varphi_b(x0)\). By Lemma 5 of the same paper this is unbordered for each \(1\le b-d\le b\); reversal preserves unborderedness. For completeness, the critical mechanism in that lemma is that a border of \(0^i\varphi_b(x0)\) must end in \(1\). Marker alignment forces the corresponding prefix/suffix in \(\varphi_b(1x0)\) to have block-aligned length; decoding markers would then give a nonempty border of \(1x0\), a contradiction. Thus the two constructed factors are unbordered for every \(n\). Their uniqueness is exactly Theorem 5.4 of the cited paper.

**3. Exact occurrence-set recursion, including both directions.** Write \(I_n^\pm=\operatorname{Occ}_{p_b}(U_n^\pm)\). Let the virtual \(I_1^+=I_1^-=Z_b\), consistently with the length-one seed \(0\). We claim for every \(n\ge2\)

\[
 I_n^+=bI_m^-+(b-1),\qquad I_n^-=bI_m^++d.
\]

Indeed every occurrence of \(U_n^+\) starts with \(1\), so its start is forced to be \(bj+b-1\) for a unique \(j\ge0\). The factor of length \(n=bm-d\) sees exactly the \(m\) marker positions belonging to parent indices \(j,j+1,\ldots,j+m-1\). These markers encode the complementary parent word, and the only remaining symbols are forced zeros. Therefore the observed factor equals the explicit \(U_n^+\) if and only if the parent length-\(m\) word equals \(U_m^-\). This proves the first equality without losing boundary cases \(d=0\) or \(d=b-1\). Likewise any occurrence of \(U_n^-\) ends in \(1\), so its final position is a block marker and its start residue is forced to be \(d\pmod b\). The same \(m\) markers then show that the word is \(U_n^-\) if and only if its parent word is \(U_m^+\), proving the second equality. These implications hold at the initial position because no negative parent indices are needed.

Since \(m<n\) for \(n\ge2\) and \(b\ge3\), iterating the two equalities to the virtual base \(Z_b\) gives exactly

\[
 I_n^\pm=b^{h_b(n)}Z_b+r_n^\pm,
\]

with the displayed residue recurrences. Induction gives \(0\le r_n^\pm<b^{h_b(n)}\), and \(h_b(n)=\lceil\log_b n\rceil\). Since \(0\in Z_b\), the least starting positions are the residues.

**4. Density and every return gap.** The natural density of indices having \(\nu_b(j+1)\) odd is

\[
 \sum_{q\ge0}\left(\frac{1}{b^{2q+1}}-\frac{1}{b^{2q+2}}\right)
 =\frac{1}{b+1}.
\]

For rigor, the individual divisibility-class frequencies are elementary arithmetic-progression densities, and the density of valuations at least \(T\) is at most \(b^{-T}\); hence the infinite sum correctly determines the natural density. It follows that \(\operatorname{dens}(Z_b)=b/(b+1)\). Affine dilation by \(b^h\) divides natural density by \(b^h\), proving the formula in the Finding.

Because a \(1\) can occur only at a marker position \(bq+b-1\), consecutive \(1\)'s cannot occur for \(b\ge3\). Thus consecutive zeros of \(p_b\) are separated by exactly one or two positions. Every gap of size two contains exactly one \(1\); conversely every \(1\) produces exactly one gap of size two. The ratio of the total number of such gaps to the total number of gaps tends to

\[
 \frac{\operatorname{dens}\{j:p_b(j)=1\}}{\operatorname{dens}(Z_b)}
 =\frac{1/(b+1)}{b/(b+1)}=\frac1b.
\]

All remaining gaps are one. The affine occurrence formulas multiply every zero-position gap by \(b^h\) without otherwise changing its index or order, establishing the full gap-sequence identity and both proportions.

## Verification

The standalone file `verify.py` requires only Python 3. Run `python3 verify.py` from its directory. It computes the binary word directly from divisibility valuations, independently constructs the proposed factors via the substitution, verifies reversal and unborderedness, and compares every predicted occurrence position against direct substring search for bases 2 through 7, lengths 2 through 96 and starts 0 through 11999. For bases 2 through 5 and lengths 2 through 15 it also checks the full set of unbordered factors by enumeration. The actual execution ended with:

`VERIFY_OK occurrence_comparisons= 537764 complete_unbordered_classifications= 56 bases=2..7 lengths=2..96 positions=0..11999`

The finite checks are diagnostics only. The proof above establishes the infinite statements for every base and length in scope. The extra base-two computation is a diagnostic, not part of the claimed new scope.

## Relationship to prior work

Goč, Mousavi and Shallit (2012), Section 5, establish the fixed-point description and the exactly-two unbordered-factor theorem for the **same** generalized base-\(b\) binary words. Their Lemmas 1 and 5 also supply the unbordered-construction mechanism. Thus neither the count nor the reversal symmetry is new. Their classification does not state affine sets of all starts, first occurrences, a common explicit density, or an identical normalized gap sequence across every factor length. The difference in implication is that knowing only the set of distinct factors and their construction does not by itself specify all their occurrence locations; the marker-position if-and-only-if recursions proved here are the additional statement.

Huang and Wen (2016) determine return-word sequences for **all factors of the binary period-doubling word**, which is stronger than the corresponding base-two gap assertion. That is why the new theorem restricts to the genuinely different generalized bases \(b\ge3\), a family not covered by their binary-only statement. Spiegelhofer (2021) investigates occurrence gaps in the Thue–Morse word and motivates asking for a uniform all-length gap law in automatic words, but addresses a different sequence and a different gap behavior. Currie (2023) studies forbidden patterns and an overlap-freeness analogue for the binary period-doubling word, not the present generalized-base occurrence sets.

The originality comparison uses actual same-word full-text statements, not title matching; additional independently rediscovered or unindexed results remain possible.

## Limitations

The exact statements are for integer bases \(b\ge3\) and unbordered factors of lengths \(n\ge2\) only. They do not classify occurrence gaps of arbitrary bordered factors or imply the same gap behavior for every automatic word. The proof relies explicitly on the established 2012 two-factor theorem and unborderedness lemma; it does not assert these prior ingredients as new. The cited 2016 binary return-word classification is not generalized by a source-verified all-factors theorem here. The standalone computation tests only finite windows and does not certify the infinite theorem or bibliographic uniqueness. No independent scientific audit has been performed.

## References

1. D. Goč, H. Mousavi and J. Shallit, *On the Number of Unbordered Factors*, arXiv:1211.1301v1 (first public 2012-11-06), especially Theorems 5.3–5.4 and Lemmas 1, 5. https://arxiv.org/html/1211.1301v1
2. Y. Huang and Z. Wen, *Envelope Words and Return Words Sequences in the Period-doubling Sequence*, arXiv:1606.05150v1 (first public 2016-06-16). https://arxiv.org/abs/1606.05150
3. L. Spiegelhofer, *Gaps in the Thue–Morse word*, arXiv:2102.01018v1 (first public 2021-02-01). https://arxiv.org/abs/2102.01018
4. J. D. Currie, *The analogue of overlap-freeness for the period-doubling sequence*, arXiv:2303.14539v1 (first public 2023-03-25). https://arxiv.org/html/2303.14539v1
