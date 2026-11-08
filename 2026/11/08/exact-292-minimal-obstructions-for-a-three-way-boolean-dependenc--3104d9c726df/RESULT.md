# Exact 292 minimal obstructions for a three-way Boolean dependence split

## Finding

Consider the lax splitting-disjunction formula
\[
\Phi=\operatorname{dep}(X,Y)\lor\operatorname{dep}(X,Y)\lor\operatorname{dep}(Y,X),
\]
where \(X=(x_1,x_2)\) and \(Y=(y_1,y_2)\) are disjoint pairs of Boolean variables. On the full space of sixteen valuations \(\{0,1\}^{4}\), there are **exactly 292** teams \(T\) that do not satisfy \(\Phi\) but every proper subteam does. Their cardinality generating polynomial is precisely
\[
\boxed{48z^{11}+4z^{12}+240z^{13}}.
\]

Identifying a team with a set of occupied cells in a \(4\)-by-\(4\) matrix, the minimal counterexamples are exactly these three classes:

1. **Eleven cells:** choose three of the four rows, occupy all four columns, and omit exactly one cell from this \(3\)-by-\(4\) rectangle;
2. **Twelve cells:** choose three of the four columns and occupy their entire \(4\)-by-\(3\) rectangle;
3. **Thirteen cells:** omit three cells from the complete \(4\)-by-\(4\) matrix, with the omissions lying in three distinct rows, and not all lying in one column.

In particular, the largest inclusion-minimal counterexample has thirteen assignments, and the eleven-, twelve-, and thirteen-assignment types are all necessary for the complete forbidden-subteam description. Exactly \(64591\) of the \(65536\) Boolean teams satisfy \(\Phi\).

## Assumptions and scope

A team is a set, not a multiset, of truth assignments to the four named Boolean variables. Each variable ranges independently over \(\{0,1\}\). A dependence atom \(\operatorname{dep}(U,V)\) asserts that any two assignments agreeing on all variables of \(U\) agree on all variables of \(V\). The symbol \(\lor\) is the **lax splitting** disjunction: \(T\models\alpha\lor\beta\) means that \(T=T_1\cup T_2\) for possibly overlapping teams satisfying the respective disjuncts. The displayed formula associates the disjunction in either direction; the two associations are semantically equivalent in this fragment.

Write \(A=B=\{00,01,10,11\}\), and use an occupied cell \((a,b)\in A\times B\) for the valuation \(X=a,Y=b\). A counterexample is inclusion-minimal if deleting any of its occupied cells makes the formula true; downward closure then makes every proper subteam true. Counts distinguish the Boolean values and variable names (no quotient by relabelling).

## Proof

**Capacitated Hall lemma.** More generally, for any finite sets \(A,B\) and team \(T\subseteq A\times B\), the formula \(\Phi\) is true if and only if
\[
|T\cap(U\times V)|\le 2|U|+|V|
\quad\text{for every }U\subseteq A,\ V\subseteq B.\tag{1}
\]
Indeed, overlapping splitting covers can be made disjoint by deleting redundant assignments, because dependence atoms are downward closed. Give each occupied cell three possible distinct slots: \((a,1)\), \((a,2)\), and \((b,3)\). Assigning all cells injectively to slots gives exactly the three-part split, since each of the first two clauses has at most one cell per row and the last clause at most one cell per column. Conversely a split assigns cells injectively. Hall's marriage theorem characterizes the existence of the matching. For a subset \(F\subseteq T\) of cells, its slot-neighborhood has size \(2|U_F|+|V_F|\), where \(U_F,V_F\) are its row and column supports. Hall's inequality for every \(F\) is equivalent to (1): one direction takes \(F=T\cap(U\times V)\), and the other uses \(F\subseteq T\cap(U_F\times V_F)\).

**Possible supports of a minimal failure.** If \(T\) is inclusion-minimal false, some nonempty rectangle \(U\times V\) violates (1). If an occupied cell lay outside that rectangle, deleting it would leave the violation. Thus all cells of \(T\) lie in the rectangle. If their number exceeded \(2|U|+|V|+1\), deleting a cell would again leave the violation. Consequently
\[
|T|=2a+b+1\le ab,
\qquad a=|U|,\ b=|V|,\quad 1\le a,b\le4.\tag{2}
\]
The only pairs \((a,b)\) satisfying (2) are \((3,4)\), \((4,3)\), and \((4,4)\), giving respectively \(11\), \(12\), and \(13\) edges. If there are \(11\) cells, all except one of a \(3\)-by-\(4\) rectangle must be present. If there are \(12\), the entire \(4\)-by-\(3\) rectangle is present. These are minimal failures because every proper subrectangle respects (1), and removing any one cell removes the sole possible violation.

**Thirteen-cell case.** Write the three absent cells of a \(4\)-by-\(4\) team as a missing-cell set \(M\). A violation in a three-row, four-column rectangle would give a proper failing subteam. Since the original has thirteen occupied cells, omitting one row must discard at least three occupied cells. Equivalently, every row contains at most one missing cell; hence the three missing cells lie in distinct rows. Likewise a four-row, three-column rectangle may have at most eleven occupied cells, which is equivalent to every column containing at least two occupied cells, i.e. the missing cells are not all in one column.

These two restrictions are sufficient: any rectangle with at most two rows, or at most two columns, or at most three of each, obeys (1) even at full occupancy. The remaining proper rectangles are exactly three-by-four and four-by-three, controlled by the restrictions. The whole four-by-four rectangle contains thirteen cells and violates the threshold twelve. After deleting any occupied cell, its size becomes twelve while all proper rectangles still satisfy (1); therefore the original is inclusion-minimal false. Conversely any minimal thirteen-cell failure must satisfy the restrictions.

**Exact counts.** For eleven cells choose the missing row (four choices) and the missing cell in the surviving three-by-four rectangle (twelve choices), giving \(4\cdot12=48\). For twelve cells choose the absent column (four choices). For thirteen cells choose the three rows containing omissions (four choices), then choose one missing column in each chosen row (\(4^3\) assignments), excluding the four choices where all three omissions are in the same column. This yields \(4(4^3-4)=240\). The cases are disjoint, so the number of minimal counterexample teams is \(48+4+240=292\).

Every false team contains some inclusion-minimal false subteam, as the valuation domain is finite. The three types therefore constitute a complete minimal-obstruction list. Their maximum size is thirteen. The count of satisfying teams was also obtained by exhaustive finite enumeration using (1), as checked below.

## Verification

Run `python3 checker.py` in a directory containing the accompanying standalone Python file. It checks all \(2^{16}=65536\) teams by the rectangle criterion and compares the resulting minimal-failure histogram with the closed-form proof. A separately coded augmenting-path matching algorithm checks all 292 minimal failures and all their single-cell deletions, 3211 additional deterministically sampled four-by-four teams, and all teams in several smaller rectangles. The checker reports `TRIPLE_DEPENDENCE_RECTANGLE_CLASSIFICATION_OK` and prints the exact counts. This finite execution is a reproducibility check; the exhaustive classification itself follows from the proof above.

A further check compares two teams whose ordinary functional-dependency closure theories are identical but whose \(\Phi\)-truth differs: the full four-row, three-column rectangle fails, whereas the four-by-four matrix with the diagonal removed satisfies \(\Phi\). This distinguishes the splitting problem from ordinary functional-dependency-profile classification.

## Relationship to prior work

Fröhlich, Kolaitis and Meier (first public version August 22, 2025) study splitting disjunctions of **two** dependence atoms; their graph test for the opposite-pair case and the non-idempotence of splitting disjunction are prior work. The present three-clause formula contains **two independently available copies** of one dependence atom and produces asymmetric slot capacities \((2,1)\), not their \((1,1)\) pseudoforest test. Barlag and coauthors (2026) study general coherence and computational boundaries, but their general statements do not provide this first nontrivial four-Boolean-variable minimal-counterteam census. Classical Hall matching and transversal-matroid theory are acknowledged as the proof mechanisms, not claimed as new. The previous enumerative literature on bipartite bicycles counts a different \((1,1)\)-capacity graph family.

## Limitations

The exact polynomial and 292 count apply to four named Boolean variables grouped as two ordered pairs. The classification does not count larger domains or distinct three-dependence-atom signatures. It is a self-review, not independently audited. A historically earlier treatment of the same capacitated transversal-matroid instance could contain equivalent coefficients, so historical priority remains a residual risk. Ordinary functional-dependency closure profiles alone do not determine the three-way splitting formula.

## References

1. N. Fröhlich, P. G. Kolaitis, and A. Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146 (first posted August 22, 2025); CSL 2026, DOI 10.4230/LIPIcs.CSL.2026.10. https://arxiv.org/abs/2508.16146 ; https://drops.dagstuhl.de/storage/00lipics/lipics-vol363-csl2026/html/LIPIcs.CSL.2026.10/LIPIcs.CSL.2026.10.html
2. T. Barlag et al., *Aspects of Coherence in Dependence Logic*, arXiv:2605.31269 (May 29, 2026). https://arxiv.org/abs/2605.31269
3. T. Hasui, T. Shirai, and S. Yabuoku, *Enumeration of Connected Bipartite Graphs with Given Betti Number*, arXiv:2208.03996 (2022); background graph enumeration, not the claimed signature. https://arxiv.org/html/2208.03996v2
4. P. Hall, *On Representatives of Subsets*, J. London Math. Soc. 10 (1935), 26–30 (classical marriage theorem).
