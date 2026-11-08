# The shortest-run law for two-shift pseudoperiods of distinct-run cycles

## Finding

Let \(q\ge 2\), let \(c_0,\ldots,c_{q-1}\) be pairwise distinct symbols, and let \(a_0,\ldots,a_{q-1}\) be positive integers. Define the one-sided infinite periodic word
\[
X=(c_0^{a_0}c_1^{a_1}\cdots c_{q-1}^{a_{q-1}})^\omega,
\qquad p=\sum_{j=0}^{q-1}a_j,\qquad m=\min_j a_j.
\]
For integers \(1\le u<v<p\), say \((u,v)\) is a *proper two-shift pseudoperiod* if
\[
\forall n\ge0,\quad X[n]=X[n+u]\ \text{or}\ X[n]=X[n+v].
\]
Then the **complete classification** is
\[
(u,v)\text{ is a proper two-shift pseudoperiod}
\quad\Longleftrightarrow\quad
u\ge1,\ d:=p-v\ge1,\ u+d\le m.
\]
Equivalently, all the pairs are exactly \((u,p-d)\) with positive integers \(u,d\) satisfying \(u+d\le m\). There are exactly
\[
\boxed{\binom{m}{2}}
\]
such pairs; they exist if and only if \(m\ge2\). The normalized feasible pairs \(u,p-v\) and their number depend solely on the shortest run, independently of the number and ordering of distinct run letters and the other run lengths; the absolute value of \(v\) necessarily changes when the period \(p\) changes.

For arbitrary positive shifts, reduce both shifts modulo \(p\). If either residue is zero, the pseudoperiod condition is automatic. If both residues are nonzero and distinct, sort the residues and apply the classification above. Two equal nonzero residues do not form a pseudoperiod, because no shift strictly between zero and \(p\) is an ordinary period of \(X\).

## Assumptions and scope

The symbols label mutually different letters: no symbol occurs in two different runs within one period, including the first and last run. In particular, the infinite cyclic word consists of distinct-symbol blocks of positive lengths. A period is \(p\); it is primitive because \(q\ge2\) and the symbols are distinct. Shifts are positive integers, and the principal count concerns the \(\binom{p-1}{2}\) ordered numerical choices \(1\le u<v<p\) (not shift pairs with a zero residue). This distinction is important: any shift divisible by \(p\) is an ordinary period, so including it in a two-shift pair would be trivial.

## Proof

**Necessity.** Choose any shortest run, of length \(m\), with letter \(c\), beginning at position \(s\) within the periodic extension. Since \(c\) occurs in exactly this run modulo \(p\), a forward shift \(t\), with \(1\le t<p\), matches \(c\) at its *first* position \(s\) exactly when \(1\le t\le m-1\). Thus the two-shift condition at \(s\) forces \(u\le m-1\) (because \(u<v\)).

At the *last* position \(s+m-1\) of that run, the shifts in \(1,\ldots,p-1\) that match \(c\) are exactly \(p-m+1,\ldots,p-1\). Consequently \(v\ge p-m+1\), and \(d=p-v\) satisfies \(1\le d\le m-1\). This uses only \(p\ge2m\), which follows from the presence of at least two runs, each of length at least \(m\); hence the low and high shift ranges cannot overlap.

Finally consider the position \(i=s+m-u\), which is inside this run because \(1\le u\le m-1\). The short shift \(u\) leads to the first symbol of the following (different-letter) run and does not match. Therefore the long shift \(v=p-d\), equivalent to a backward shift by \(d\), must match. Since \(1\le d\le m-1\), this backward position is in the same \(c\)-run precisely when \(s+m-u-d\ge s\). Hence \(u+d\le m\).

**Sufficiency.** Suppose positive \(u,d\) satisfy \(u+d\le m\) and set \(v=p-d\). Take any position of \(X\), say offset \(t\in\{0,\ldots,\ell-1\}\) within a run of length \(\ell\ge m\). If \(t+u<\ell\), the forward shift \(u\) stays in that run. Otherwise \(t\ge\ell-u\), so
\[
t-d\ge\ell-u-d\ge\ell-m\ge0.
\]
Thus the backwards shift \(-d\), and equivalently the forward shift \(v=p-d\), remains in the same run and matches. This covers every position, proving the required pseudoperiodicity.

**Counting.** For each \(u\in\{1,\ldots,m-1\}\), there are exactly \(m-u\) choices \(d\in\{1,\ldots,m-u\}\), giving
\[
\sum_{u=1}^{m-1}(m-u)=\frac{m(m-1)}2=\binom m2.
\]
Distinct \((u,d)\) give distinct pairs \((u,p-d)\), since \(u<m\le p/2\) and \(p-d>p-m\ge p/2\). This proves the classification and count.

For the arbitrary-positive-shift corollary, periodicity makes the matching conditions depend only on residues modulo \(p\). A zero residue always matches. If both residues equal a nonzero \(r\), they match everywhere only if \(r\) is a period. At the first and last positions of a shortest run, any matching shift would have to be simultaneously at most \(m-1\) and at least \(p-m+1\), impossible when \(p\ge2m\). Thus no such \(r\) exists.

## Verification

A standalone standard-library script, `verify.py`, computes the literal cyclic word for each vector of run lengths and tests every candidate pair \(1\le u<v<p\) against every position in the period. It independently computes the predicted pairs from the shortest-run inequality and asserts exact set equality. The exhaustive parameter range is \(2\le q\le6\), with every run length in \(\{1,2,3,4,5\}\), a total of \(19{,}525\) distinct run profiles. It returns `PASS 19525 exhaustive run profiles (q=2..6, lengths=1..5)` on execution. This finite computation supports the theorem but is not used as its proof; the preceding argument covers all positive run lengths and all alphabet sizes \(q\ge2\).

## Relationship to prior work

Meleshko, Ochem, Shallit and Shan introduced and studied this existential-shift definition of pseudoperiodicity (arXiv:2207.10171, first posted July 20, 2022; journal 2023). Their Definition 1, Propositions 2–4 and Theorem 5 give general existence, run-length and alphabet-size facts, and later sections study automatic sequences, repetition thresholds and hardness. These results do not state the above complete two-shift residue spectrum for distinct-letter run cycles. Their automata-based decidability results can in principle test each individual periodic example but do not imply the stated shortest-run invariant or its triangular count without additional analysis.

Desmeules, Blondin Massé, Hallé and Gaboury, *Multipseudoperiodic Words* (2013), treat permutations acting on letters as pseudoperiods, a different definition. The distinction is explicit in the later paper and is checked in the earlier preprint's Definition 3. A search of related indexed mathematical records, equivalence terminology (two-shift cover, cyclic return to same letter) and literature did not locate a matching formula. These are best-knowledge comparisons, not a proof of priority.

## Limitations

The classification assumes each run letter occurs exactly once per period. It does not apply directly to cyclic words in which a symbol reappears in multiple separated runs, or to arbitrary nonperiodic words. There is no new complexity-theoretic claim, and no classification of shift sets of cardinality three or greater. Inaccessible and unindexed literature may contain equivalent results. No independent scientific audit has been performed.

## References

1. J. Meleshko, P. Ochem, J. Shallit, and S. L. Shan, *Pseudoperiodic Words and a Question of Shevelev*, arXiv:2207.10171, first posted July 20, 2022, *Discrete Mathematics & Theoretical Computer Science* 25:2 (2023). https://arxiv.org/html/2207.10171v3 ; https://doi.org/10.46298/dmtcs.9919.
2. S. Desmeules, A. Blondin Massé, S. Hallé, and S. Gaboury, *Multipseudoperiodic Words*, *International Journal of Foundations of Computer Science* 24 (2013), 1153–1166. https://doi.org/10.1142/S0129054113400364 ; repository preprint https://archipel.uqam.ca/8434/1/Blondin-Mass%C3%A9-2013c-preprint.pdf.
