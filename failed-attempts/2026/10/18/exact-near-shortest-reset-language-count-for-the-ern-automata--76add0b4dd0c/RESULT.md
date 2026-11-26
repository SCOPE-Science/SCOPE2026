# Exact near-shortest reset-language count for the Černý automata

## Finding

For every integer \(n\ge3\), the standard binary \(n\)-state Černý automaton has a unique shortest reset word of length \(L=(n-1)^2\). The number of **distinct** reset words of length exactly \(L+1\) is
\[
\boxed{N_n((n-1)^2+1)=(n-2)^2+3=n^2-4n+7.}
\]
All such words are explicitly classified below. This is a count of words, not merely final states or state-set images. It is the first coefficient beyond the optimal length in the reset-language length spectrum.

## Assumptions and scope

Write \(Q=\{0,1,\dots,n-1\}\), identify its elements with residues modulo \(n\), and define the automaton on \(\{a,b\}\) by
\[
a(i)=i+1\pmod n,\qquad
b(i)=\begin{cases}0,&i=n-1,\\i,&0\le i\le n-2.\end{cases}
\]
The word action is from left to right. A reset word maps all of \(Q\) to a singleton. Let
\[
U_n=b(a^{n-1}b)^{n-2},\qquad L=|U_n|=(n-1)^2.
\]
Use \(n\ge3\) throughout. Every reset word of length \(L+1\) is one of the following and conversely every listed word is resetting:

1. The three boundary variants \(aU_n\), \(U_na\), \(U_nb\).
2. For each \(1\le i\le n-2\), take the \(i\)-th run \(a^{n-1}\) of \(U_n\) (counting from the left). Insert one extra \(b\) after exactly \(j\) letters of that run, where \(0\le j\le n-2\) and \(j\ne i\).

These are pairwise distinct and yield \(3+(n-2)^2\) words. In particular, the apparently similar insertion \(j=i\) fails to reset; this excluded position matters to the classification.

## Proof

**Inverse interval dynamics.** A word \(w\) resets to \(t\) if and only if the inverse-image sequence that starts at \(\{t\}\) and processes the letters of \(w\) in reverse order ends at \(Q\). Inverse images of nonempty proper cyclic intervals stay cyclic intervals unless they become empty; an inverse path ending at \(Q\) cannot pass through the empty set. Represent a size-\(k\) cyclic interval by
\[
I(s,k)=\{s,s+1,\dots,s+k-1\}\pmod n,\qquad1\le k<n.
\]
The inverse action of \(a\) replaces \(s\) by \(s-1\) without changing \(k\). The inverse action of \(b\) has three possibilities:
\[
I(0,k)b^{-1}=I(n-1,k+1)\quad\text{(gain)},
\]
\[
I(n-k,k)b^{-1}=I(n-k,k-1)\quad\text{(loss)},
\]
where an empty right-hand set is permitted only on an unsuccessful path; in every other proper-interval configuration \(b^{-1}\) preserves the set (a *no-op*). Both rules follow directly from the fact that \(b\) sends \(n-1\) to \(0\) and fixes all other states. Once the current set is \(Q\), both inverse letters preserve \(Q\).

Every gain requires the interval to begin at residue \(0\). Immediately after any gain, it begins at residue \(n-1\). Losses and no-op occurrences of \(b^{-1}\) do not change the beginning of a nonempty interval; therefore at least \(n-1\) inverse occurrences of \(a\) are needed between consecutive gains. Starting from singleton \(\{t\}\), at least \(t\) inverse occurrences of \(a\) are needed before the first gain. For successful paths, if there are \(g\) gains, \(h\) losses and \(r\) no-op inverse \(b\)-steps, cardinality gives \(g-h=n-1\). Consequently any resetting word of length \(|w|\) obeys
\[
|w|\ge t+(g-1)(n-1)+g+h+r
=(n-1)^2+t+(n+1)h+r.
\tag{1}
\]
This inequality also accounts for possible extra inverse \(a\)-steps, which only increase length.

**The shortest word.** For \(|w|\le L\), (1) forces \(t=h=r=0\), precisely \(n-1\) gains, no useless steps, no \(a\) before the first gain and exactly \(n-1\) rotations between gains. Thus the only shortest inverse word is \(b(a^{n-1}b)^{n-2}\), which is equal to its reversal. It reaches \(Q\), so \(U_n\) is the unique shortest reset word.

**One unit of slack.** For \(|w|=L+1\), (1) forces \(h=0\) and leaves exactly one of three possibilities relative to the just-described rigid inverse path:

* one extra inverse \(a\) before its first gain, necessarily starting at target \(t=1\), giving the forward word \(U_na\);
* one extra inverse \(a\) after its last gain, giving the forward word \(aU_n\);
* one inverse \(b\) which is a no-op, starting at target \(t=0\), with every \(a\)-gap still exactly minimal.

The two \(a\) cases each have only the specified word: within a gap the number of inverse \(a\)-steps between gains is congruent to \(n-1\) modulo \(n\), and an extra single step cannot be placed in such a gap while preserving the gains. Before the first gain, exactly one \(a\) is possible only from target \(t=1\). After the last gain all inverse actions are harmless, and the single extra \(a\) is then unique.

**Classifying the no-op \(b\) insertions.** After inverse gain number \(r\), \(1\le r\le n-2\), the current interval has size \(r+1\) and begins at \(n-1\). Between that gain and the next there are exactly \(n-1\) inverse \(a\)-steps. A \(b^{-1}\) placed after \(j\) of them, \(0\le j\le n-2\), is a no-op except at the **unique** phase \(j=r\), where the interval ends at \(n-1\) and excludes \(0\); at this phase it causes a loss, forbidden by (1). Thus each of the \(n-2\) internal inverse gaps has exactly \(n-2\) permissible no-op insertion positions. A final position after reaching \(Q\) permits one additional no-op \(b\). No other no-op position exists: at the initial target \(0\) a \(b^{-1}\) is productive, and at the endpoint of each internal gap the scheduled \(b^{-1}\) must be productive. There are consequently
\[
(n-2)(n-2)+1=(n-2)^2+1
\]
valid one-no-op insertions.

For completeness, translating this count to the forward-word description: there are \(n-2\) runs \(a^{n-1}\) in \(U_n\); insertion after \(j\) of its letters in run \(i\) is a no-op in the reverse path precisely when \(j\ne i\) (for \(j=0\), it occurs just after a productive inverse gain, or after the final gain, and is harmless). The sole further permissible forward insertion is the trailing \(b\), producing \(U_nb\). These inserted words have distinguishable locations of their extra \(b\), while \(aU_n\) and \(U_na\) contain one extra \(a\), and so none coincide. Counting the \(2\) extra-\(a\) words and the \((n-2)^2+1\) extra-\(b\) words yields \((n-2)^2+3\) as claimed. \(\square\)

## Verification

The included Python standard-library program `artifacts/verify.py` checks the theorem for every \(3\le n\le13\). For each length, it uses independent forward image-subset dynamic programming to determine all reset-word counts through \(L+1\), checks the explicit witness collection against that count, and checks the local inverse nonproductive-step condition. For \(n=3,4,5\), it additionally enumerates all binary words of length \(L+1\), independently verifying the exact set. The observed near-shortest counts are \(4,7,12,19,28,39,52,67,84,103,124\) for successive \(n=3,\ldots,13\). The infinite theorem is established by the inverse-interval proof, not by the finite computations.

## Relationship to prior work

The Černý automata and their quadratic optimal reset length are classical. Rodaro studied the language of minimal reset words and reset languages as ideals, including structural constraints on these languages; the inspected text does not give the exact next-length coefficient for this automaton family. Ferens and Szykuła study completely reachable automata, their subset images and general reaching bounds, but their results do not count words of length one above the Černý reset threshold. Ferens, Szykuła and Vorel investigate extremal avoidance thresholds and give Černý examples; maximum avoidance lengths do not imply the present reset-language coefficient.

Related exact results for the same automaton determine early rank-compression or worst target-avoidance thresholds. Their statements concern minima or maxima over image/target sets, not the multiplicity of full-reset words at \(L+1\). Results counting shortest words for other automata, including Wielandt and deficiency-two families, concern different transition semigroups and therefore do not cover this count. The contribution here is the all-\(n\) exact near-threshold coefficient and complete classification of its witnesses, not the classical reset threshold or the general theory of reset ideals.

## Limitations

The theorem counts words of exactly one more than the shortest reset length, for this precise labeled binary automaton and \(n\ge3\). It does not give a generating function or a formula at greater excess length, nor does it count near-shortest reset words for arbitrary synchronizing automata. The \(n=2\) automaton is excluded. Originality is to the best of inspected literature; an equivalent count in older unindexed sources could exist. Independent external mathematical review has not been performed.

## References

1. E. Rodaro, *Synchronizing automata and the language of minimal reset words*, arXiv:1708.04864, posted August 16, 2017. https://arxiv.org/abs/1708.04864
2. R. Ferens and M. Szykuła, *Completely reachable automata: a quadratic decision algorithm and a quadratic upper bound on the reaching threshold*, arXiv:2208.05956, posted August 11, 2022. https://arxiv.org/abs/2208.05956
3. R. Ferens, M. Szykuła and V. Vorel, *Lower Bounds on Avoiding Thresholds*, MFCS 2021, LIPIcs 202, Article 46. https://doi.org/10.4230/LIPIcs.MFCS.2021.46
4. *Exact k-avoiding thresholds of the Černý automata*, public research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-cerny-k-avoiding-thresholds--5cdbaf373a0f
5. *Exact early deficiency profile of the Černý automata*, public research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-early-deficiency-profile-of-the-ern-automata--766d362d36d3
