# Complete greedy superstring length spectrum for the binary four-mer universe

## Finding

For the complete binary four-mer instance \(S=\{0,1\}^4\) (sixteen distinct words), let Greedy repeatedly choose an **ordered** pair of distinct currently available strings with maximum suffix-prefix overlap, merge them, and continue. Every tie resolution is permitted. Its complete attainable final-length spectrum is
\[
\{19,20,21,22,23,24,25,26,27\}.
\]
The shortest possible common superstring has length \(19\). Thus the largest length of a legal Greedy output is exactly \(27\), giving ratio \(27/19\) for this particular complete-spectrum instance.

## Assumptions and scope

Strings are ordinary linear words over \(\{0,1\}\), and each input four-mer occurs once in the initial set. Overlap \(o(x,y)\) is the greatest \(d\ge0\) for which the length-\(d\) suffix of \(x\) equals the length-\(d\) prefix of \(y\). The operation replaces \(x,y\) by \(x\) followed by the last \(|y|-o(x,y)\) letters of \(y\). The optimization includes every legal tie-breaking history, including ties at overlap zero. The theorem concerns this one canonical full spectrum, not all subsets of four-mers.

## Proof

**Endpoint lemma, with proof.** Initially each component is one distinct four-mer. Inductively, each live component has a uniquely designated first and last *original* four-mer as its prefix and suffix. For two different components, their respective last and first original four-mers differ because the original inputs are partitioned among components. Therefore their overlap is strictly less than four: an overlap of at least four would equate these two distinct boundary four-mers. Merging two components with overlap at most three preserves the boundary four-mers of the concatenated component. This proves the invariant by induction. Moreover all live-component overlaps depend only on the designated last and first original words. In particular, no component is contained in another, and no intermediate string data beyond these endpoints are needed to decide legal merges or length decrements.

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

Compile the standalone endpoint-state enumerator with `g++ -O3 -std=c++17 spectrum.cpp -o spectrum` and run `./spectrum`: it prints `states=2262207 lengths=27,26,25,24,23,22,21,20,19,`. Independently compile `witness_generator.cpp` similarly and run it to reproduce `witnesses.txt`; run `python3 check_witness.py witnesses.txt` to verify every greedy step in all nine witnesses by actual string operations. Saved output text files report completed runs; they are not substituted for the proof of the recurrence.

## Relationship to prior work

The 2026 work of Chukhin–Kulikov–Mihajlin–Smal (arXiv:2608.20018, first posted 2026-08-20) formulates the equal-length Greedy model, proves the maximum-overlap boundary property, and finds the unrestricted three-mer approximation guarantee, but does not state this *binary full-four-mer input* length spectrum. Shibata's 2026 counterexample (arXiv:2609.01365, first posted 2026-09-01) concerns different, larger instances and asymptotic approximation ratios, not this finite exact spectrum. Nikolaev (arXiv:2102.05579) studies equivalence of tie-breaking versions under transformations of arbitrary inputs; that equivalence does not specify the output spectrum on an unchanged fixed input. The classical de Bruijn bound \(19\) is prior art, not a novelty claim.

## Limitations

This is an exact, finite, complete-spectrum result for a single canonical instance. It gives no uniform formula for arbitrary four-mer subsets, longer binary read lengths, or larger alphabets. The upper bound depends on a replayable exhaustive finite-state recurrence rather than a short hand classification of endpoint states. Literature indexing may omit an equivalent older finite census.

## References

1. N. Chukhin, A. S. Kulikov, I. Mihajlin, A. Smal, *The Greedy Superstring Algorithm Achieves Ratio 2 for Strings of Length 6 Already*, arXiv:2608.20018, first posted 2026-08-20, https://arxiv.org/abs/2608.20018.
2. H. Shibata, *Disproving the Greedy Superstring Conjecture*, arXiv:2609.01365, first posted 2026-09-01, https://arxiv.org/abs/2609.01365.
3. M. Nikolaev, *All instantiations of the greedy algorithm for the shortest superstring problem are equivalent*, arXiv:2102.05579, https://arxiv.org/abs/2102.05579.
4. N. G. de Bruijn, *A combinatorial problem*, 1946; classical de Bruijn sequence construction.
