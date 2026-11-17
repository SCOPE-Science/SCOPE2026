# Parity-controlled recurrent orbit counts for synchronous majority on crown graphs

## Finding
Let \(\operatorname{Cr}_n=K_{n,n}-M\) be the crown graph, with \(n\ge3\) matched pairs and the perfect matching \(M\) deleted. Let \(F_n\) be synchronous binary neighbor-majority updating, retaining the old opinion at a tie. Every trajectory is periodic by time three, and its eventual period is one or two.

For even \(n\ge4\), put \(c_n=\binom{n}{n/2}\). Then
\[
\#\operatorname{Fix}(F_n)=c_n+2,\qquad
\#\operatorname{Fix}(F_n^2)=(c_n+2)^2,\qquad
\#\{\text{primitive two-cycles}\}=\frac{(c_n+2)(c_n+1)}2.
\]
The exact maximum first periodic-entry time is one: \(F_n^3=F_n\).

For odd \(n\ge3\), put \(k=(n-1)/2\) and \(c_n=\binom nk\). Then
\[
\#\operatorname{Fix}(F_n)=(n+3)c_n+2,\qquad
\#\operatorname{Fix}(F_n^2)=(n+3)c_n+4.
\]
There is exactly one primitive two-cycle, alternating between all zeroes on one shore and all ones on the other. The identity \(F_n^5=F_n^3\) holds. The maximal first periodic-entry time equals two for \(n=3\), and three for all odd \(n\ge5\).

In particular, the count of primitive two-cycles jumps from exactly one at every odd size to asymptotically \(4^n/(\pi n)\) at every even size.

## Assumptions and scope
There are two labelled shores \(A=(a_1,\ldots,a_n)\) and \(B=(b_1,\ldots,b_n)\), with an edge \(a_i b_j\) precisely when \(i\ne j\). States are bits, and updates are simultaneous. A vertex sets its next bit to one when strictly more than half of its \(n-1\) neighbors are one, to zero when strictly fewer are one, and otherwise retains its old bit. A configuration is periodic when it lies on a temporal orbit; its entry time is the least nonnegative \(t\) with \(F_n^{t+2}(x)=F_n^t(x)\). Theorems concern labelled configurations, with graph automorphisms **not** factored out.

## Proof
Write \(A,B\subseteq[n]\) for the indices currently set to one. A vertex at position \(i\) on shore \(A\) sees exactly \(|B|-\mathbf1_{i\in B}\) one-neighbors, and analogously for \(B\).

**Even sizes.** If \(n=2k\), the degree \(2k-1\) is odd, so the next shore is \(\varnothing\) when the opposite one-count is at most \(k-1\), is \([n]\) when it is at least \(k+1\), and otherwise is the complement of the opposite shore. Thus balanced shores have size \(k\). Every image of \(F_n\) is one of: two uniform shores; two balanced shores; or one uniform and one balanced shore. All three classes are periodic with period dividing two: two balanced shores evolve by \((A,B)\mapsto(B^c,A^c)\), one balanced/one uniform shore maps to the same class with positions exchanged, and both uniform shores either remain fixed or exchange. Conversely any periodic state must be in the image, and all listed states lie in the image because they are periodic. Consequently the total periodic-state count is \(c_n^2+4c_n+4=(c_n+2)^2\). Fixed states consist of the two unanimous configurations and \(c_n\) complementary balanced pairs. Subtracting fixed states and dividing by two gives the stated orbit count. The state with \(A=\varnothing\), \(B=\{1\}\) shows the one-step bound is attained.

**Odd sizes: exact update formula.** If \(n=2k+1\), the degree is \(2k\). The next \(A\)-shore, according to \(|B|\), is
\[
\varnothing\ (|B|\le k-1),\qquad A\setminus B\ (|B|=k),\qquad A\cup B^c\ (|B|=k+1),\qquad [n]\ (|B|\ge k+2),
\]
and symmetrically for the next \(B\)-shore. A non-unanimous fixed state necessarily has both one-counts in \(\{k,k+1\}\): an extreme count forces the opposite shore to uniform zero or one, which then forces the same unanimous state. For counts \((k,k)\), fixedness is equivalent to \(A\cap B=\varnothing\), giving \((k+1)c_n\) possibilities. For \((k+1,k+1)\), it is equivalent to \(A\cup B=[n]\), again giving \((k+1)c_n\). For each of the two mixed count pairs, fixedness forces \(A=B^c\), giving \(c_n\) possibilities. Together with the two unanimous states, this is \(2(k+2)c_n+2=(n+3)c_n+2\).

**Odd sizes: finite exact symbolic lemma.** The remainder of the theorem follows from a universal rational-polyhedral elimination, implemented in `verify_symbolic.py`; its validity for all \(n\) does not depend on a finite experiment. An initial pair has four index-atom types \((0,0),(0,1),(1,0),(1,1)\), with nonnegative multiplicities \(x_{00},x_{01},x_{10},x_{11}\) summing to the odd number \(n\). Each possible threshold branch depends on whether a shore count lies below \(k\), equals \(k\), equals \(k+1\), or exceeds \(k+1\). Under any fixed sequence of these branches, the current bit pair carried by each original atom is deterministic, and all branch-feasibility conditions are linear inequalities on the four multiplicities.

For clarity, define the linear score of a shore map \(s\) on the four atoms by \(L_s(x)=\sum_{\alpha}(2s(\alpha)-1)x_\alpha=2|s|-n\). Because \(n=2k+1\), the four branches respectively require \(L_s\le-3\), \(L_s=-1\), \(L_s=1\), or \(L_s\ge3\). All valid integer vectors are contained in the rational regions obtained by requiring only \(x_\alpha\ge0\) and \(\sum x_\alpha\ge3\). Exact Fourier–Motzkin elimination, which removes variables by taking every positive/negative coefficient pair and detects contradictory constant inequalities, enumerates the **16, 30, 30, 30, 30** feasible branch strings after steps one through five. In each of the 30 feasible five-step branches, the four atom images at times three and five agree exactly; hence \(F_n^5=F_n^3\) for every odd \(n\ge3\).

To classify period-two states, enumerate every two-step branch pair and every original atom that changes at step one. Require that this atom have positive multiplicity and all atoms whose two-step image differs from their initial pair have zero multiplicity. Exactly **608** candidate linear systems occur. Exact rational elimination finds only two feasible branch/changed-atom combinations: the extreme cases \((\mathrm{low},\mathrm{high})\to(\mathrm{high},\mathrm{low})\) and their reversal. In either case, \(F_n^2(x)=x\) forces \(x\) itself to be the pair of opposite uniform shores. These two states form one primitive two-cycle, proving the odd periodic-state count and completing the classification. The checker uses integer arithmetic only; its complete input-to-claim logic is included in the standalone source.

For \(n=3\), the 64 configurations are directly enumerated by `verify_direct.py`, showing that the maximum entry time is two. For every odd \(n\ge5\), choose \(A=\{1\}\) and \(B=\{1,\ldots,k+1\}\). The successive shore sizes are \((1,k+1)\), \((k+1,0)\), \((0,k)\), \((0,0)\), so the first periodic state occurs at update three; all intermediate states are distinct from their two-step successors. This establishes sharpness.

## Verification
`verify_symbolic.py` recomputes the odd-size universal certificates using exact rational Fourier–Motzkin elimination. Its trace reports 30 feasible five-step branches, 608 two-step nonfixed candidate systems, and only the two extreme feasible systems. `verify_direct.py` independently applies the majority rule to each individual neighbor, exhaustively checks all labelled starting states for \(3\le n\le8\), and compares fixed, primitive two-cycle and first-entry counts. Both programs terminate with `PASS`; corresponding output files are included. The finite experiments corroborate rather than replace the all-size arguments.

## Relationship to prior work
Goles and Olivos (1980) established eventual period at most two for symmetric threshold dynamics, but that result does not give exact graph-dependent cycle counts or constant sharp entry times. Benjamini et al. (initial public preprint May 11, 2014) study majority dynamics primarily on unimodular/infinite and random graphs. Kaaser, Mallmann-Trenn and Natale (initial public preprint August 14, 2015) establish upper bounds on voting time on general graphs. Their full manuscripts were inspected; neither gives the crown-graph parity census or the precise universal symbolic threshold classification. Earlier graph-specific periodicity enumerations on other graph families do not imply this result: neither the edge set nor the majority update is a reduction of those analyses. The exact effect of removing a perfect matching is the structural focus here.

## Limitations
The theorem does not count exact attraction-basin populations or enumerate transients of each duration. The finite symbolic certificate is fully reproducible but is not independent peer review. The 1980 original article was available through bibliographic and abstract information; its full text was not reviewed. Equivalent formulas may exist under different network terminology; historical priority is therefore not asserted absolutely. The graph has two equally sized shores and a deleted *perfect* matching; altering either hypothesis changes the threshold rules.

## References
1. E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* 30 (1980), 187–189, doi:10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, “Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs,” arXiv:1405.2486 (first version May 11, 2014), https://arxiv.org/abs/1405.2486.
3. D. Kaaser, F. Mallmann-Trenn and E. Natale, “On the Voting Time of the Deterministic Majority Process,” arXiv:1508.03519 (first version August 14, 2015), https://arxiv.org/abs/1508.03519.
4. N. Fountoulakis, M. Kang and T. Makai, “Resolution of a conjecture on majority dynamics: Rapid stabilization in dense random graphs,” *Random Structures & Algorithms* 57 (2020), 1134–1156, doi:10.1002/rsa.20970.
5. E. W. Weisstein, “Crown Graph,” *MathWorld*, https://mathworld.wolfram.com/CrownGraph.html (definition; not a majority-dynamics result).
