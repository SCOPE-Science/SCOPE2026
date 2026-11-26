# Complete greedy superstring length spectrum for the binary four-mer universe

## Finding

For the complete binary four-mer instance \(S=\{0,1\}^4\) (sixteen distinct words), let Greedy repeatedly choose an **ordered** pair of distinct currently available strings with maximum suffix-prefix overlap, merge them, and continue. Every tie resolution is permitted. Its complete attainable final-length spectrum is
\[
\{19,20,21,22,23,24,25,26,27\}.
\]
The shortest possible common superstring has length \(19\). Thus the largest length of a legal Greedy output is exactly \(27\), giving ratio \(27/19\) for this instance. The contribution is the full set of attainable lengths, in particular the absence of gaps between its endpoints.

## Assumptions and scope

Strings are ordinary linear words over \(\{0,1\}\), and each input four-mer occurs once in the initial set. Overlap \(o(x,y)\) is the greatest \(d\ge0\) for which the length-\(d\) suffix of \(x\) equals the length-\(d\) prefix of \(y\). The operation replaces \(x,y\) by \(x\) followed by the last \(|y|-o(x,y)\) letters of \(y\). The optimization includes every legal tie-breaking history, including ties at overlap zero. The theorem concerns this one canonical full spectrum, not all subsets of four-mers.

## Proof

**Containment and maximum overlap.** Initially no live string is a substring of another, and the maximum overlap is at most three. Suppose the live strings have no containment and a maximum-overlap merge of \(x,y\) uses overlap \(m\), giving \(u\). The copies of \(x\) and \(y\) cover \(u\) and meet in precisely \(m\) positions. No other live string \(w\) can contain \(u\), since it would already contain \(x\). If \(w\) occurs inside \(u\), its occurrence cannot be contained in either copy, by the original no-containment hypothesis. It must therefore start strictly before the copy of \(y\) starts and end strictly after the copy of \(x\) ends. The part of \(w\) up to the end of \(x\) is then a suffix of \(x\) and a prefix of \(w\) of length greater than \(m\), contradicting maximality. This also works when \(m=0\), with the copies adjacent.

An overlap from \(u\) to an unchanged \(w\), if longer than \(|y|\), would embed the whole suffix copy \(y\) in \(w\), which was forbidden before the merge. Any overlap of length at most \(|y|\) from \(u\) to \(w\) is already an overlap from \(y\) to \(w\). The incoming direction is analogous: an overlap from \(w\) to \(u\) of length greater than \(|x|\) would embed \(x\) in \(w\), and a shorter one (including length \(|x|\)) is already an overlap from \(w\) to \(x\). Unchanged pairs keep their overlaps. Thus no overlap increases the old maximum. By induction the live family stays substring-free and all overlaps have length at most three.

**Endpoint lemma.** Each component starts and ends with the original four-mers at the respective ends of its merge history: this holds at initialization, and a merge retains the whole first string as a prefix and the whole second string as a suffix. Now that all overlaps are bounded by three, the original last four-mer of one component and the original first four-mer of another determine their overlap. No other intermediate string data are needed to decide legal merges or compute length decrements.

Index the original four-mers by their binary integer values \(0,1,\ldots,15\), written with four bits. The state is an unordered family \(E\) of ordered endpoint pairs \((f,l)\), one for each live component. Initially \(E_0=\{(i,i):0\le i\le15\}\). For different components \((f_i,l_i)\) and \((f_j,l_j)\), write \(d(i,j)=o(\operatorname{bin}_4(l_i),\operatorname{bin}_4(f_j))\), and let \(m(E)=\max_{i\ne j}d(i,j)\). The merged state \(E_{ij}\) removes both pairs and inserts \((f_i,l_j)\). Let \(T(E)\) be the set of total future overlap savings along legal Greedy histories. Its exact acyclic recurrence is
\[
 T(E)=\bigcup_{i\ne j,\;d(i,j)=m(E)}\bigl(m(E)+T(E_{ij})\bigr),\qquad T(\{(f,l)\})=\{0\}.
\]
Each merge decreases the number of components, so induction on \(|E|\) proves that this recurrence enumerates *all and only* legal Greedy overlap totals. Two histories with the same endpoint state have identical possible continuations and incremental savings, so memoization does not discard distinctions relevant to the claimed lengths.

The complete exact integer recursion in `spectrum.cpp` visits \(2,262,207\) distinct nonterminal endpoint states and computes
\[
 T(E_0)=\{37,38,39,40,41,42,43,44,45\}.
\]
As the sum of the sixteen original lengths is \(64\), the final spectrum is precisely \(64-T(E_0)=\{19,\ldots,27\}\). The included `witnesses.txt` gives fifteen greedy merge choices for each of the nine lengths; `check_witness.py` recomputes all current literal strings, checks that each selected ordered pair has global maximal overlap, and checks coverage of all sixteen initial four-mers. Thus no member of the computed spectrum is a spurious abstract state.

Every length-\(n\) binary word has at most \(n-3\) length-four windows. Covering sixteen different four-mers therefore forces \(n\ge19\). The explicitly listed length-nineteen witness contains every four-mer, giving the optimum \(19\). This is the standard de Bruijn lower bound and construction; only the complete Greedy length spectrum is advanced here.

## Verification

Compile the standalone endpoint-state enumerator with `g++ -O3 -std=c++17 spectrum.cpp -o spectrum` and run `./spectrum`: it prints `states=2262207 lengths=27,26,25,24,23,22,21,20,19,`. Compile `witness_generator.cpp` similarly and run it to reproduce `witnesses.txt`; run `python3 check_witness.py witnesses.txt` to verify every greedy step in all nine witnesses by actual string operations. Alternatively, `python3 spectrum_replay.py 16 witnesses.txt` evaluates the recurrence with a head-indexed state encoding, including terminal states in its cache, and replays the witnesses using literal strings. Saved output text files report completed runs; they are not substituted for the proof of the recurrence.

## Relationship to prior work

The 2026 work of Chukhin–Kulikov–Mihajlin–Smal (arXiv:2608.20018, Lemma 2.2) formulates the equal-length Greedy model and proves the maximum-overlap boundary property; the argument above gives a self-contained justification. Shibata's 2026 counterexample (arXiv:2609.01365, first posted 2026-09-01) concerns different, larger instances and asymptotic approximation ratios, not this finite exact spectrum. Nikolaev (arXiv:2102.05579) studies equivalence of tie-breaking versions under transformations of arbitrary inputs; that equivalence does not specify the output spectrum on an unchanged fixed input. The classical de Bruijn bound \(19\) is prior art, not a novelty claim.

The [sharp worst-case ratio census for distinct binary four-mers](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-worst-case-greedy-ratio-for-distinct-binary-four-mers--c5782f9cc70b) computes the worst Greedy length for every nonempty subset, including the full set. This already covers the maximal endpoint computationally: its recurrence minimizes savings rather than storing the attainable set of savings. It does not establish which lengths strictly between the extremal endpoints occur. The present spectrum calculation and literal witness family address that question.

## Limitations

This is an exact, finite, complete-spectrum result for a single canonical instance. It gives no uniform formula for arbitrary four-mer subsets, longer binary read lengths, or larger alphabets. The upper bound depends on a replayable exhaustive finite-state recurrence rather than a short hand classification of endpoint states. Literature indexing may omit an equivalent older finite census.

## References

1. N. Chukhin, A. S. Kulikov, I. Mihajlin, A. Smal, *The Greedy Superstring Algorithm Achieves Ratio 2 for Strings of Length 6 Already*, arXiv:2608.20018, first posted 2026-08-20, https://arxiv.org/abs/2608.20018.
2. H. Shibata, *Disproving the Greedy Superstring Conjecture*, arXiv:2609.01365, first posted 2026-09-01, https://arxiv.org/abs/2609.01365.
3. M. Nikolaev, *All instantiations of the greedy algorithm for the shortest superstring problem are equivalent*, arXiv:2102.05579, https://arxiv.org/abs/2102.05579.
4. N. G. de Bruijn, *A combinatorial problem*, 1946; classical de Bruijn sequence construction.
