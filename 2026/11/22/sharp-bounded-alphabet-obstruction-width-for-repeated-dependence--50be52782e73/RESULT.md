# Sharp bounded-alphabet obstruction width for repeated dependence splitting

## Finding

For every integer \(r\geq1\) let \(\Phi_r\) be the lax team-disjunction consisting of \(r\) independently usable copies of \(\operatorname{dep}(x,y)\) and one copy of \(\operatorname{dep}(y,x)\). Suppose a finite team \(T\) has at most \(q\) distinct values of \(y\), with no bound on the number of values of \(x\). Then:

* If \(q\leq r\), every such team satisfies \(\Phi_r\).
* If \(q\geq r+1\), every falsifying team has a falsifying subteam of at most \((r+1)(q+1)\) assignments. The bound is attained by an inclusion-minimal falsifying team of exactly \((r+1)(q+1)\) assignments, for every pair \((r,q)\) in this range.
* Every inclusion-minimal falsifier meeting the upper bound has exactly \(q+1\) distinct \(x\)-values and \(q\) distinct \(y\)-values, with exactly \(r+1\) assignments at each \(x\)-value. If its \(q+1\) row-neighborhoods are viewed as a multiset of \((r+1)\)-subsets of the \(q\)-element \(y\)-set, it is extremal precisely when for every proper subset \(S\) of that set,
  \[
  |\{x:N(x)\subseteq S\}|\leq |S|.
  \]

Here different \(x\)-values can have identical neighborhoods; the multiset convention is essential. For \(r=2\), the formula is a three-way split, and the sharp widths on \(q=3,4,5,\ldots\) values are \(12,15,18,\ldots\). The case \(r=1\) is consistent with previously known two-disjunct results; the all-multiplicity formula and its extremizer criterion are the scope of this finding.

## Assumptions and scope

A team is a finite **set** \(T\subseteq X\times Y\) of ordered assignments, not a multiset. The sets \(X,Y\) of possible values are arbitrary and need not be numerical; only \(|Y|\leq q\) is assumed. The dependence atom \(\operatorname{dep}(x,y)\) asserts that no two assignments with the same \(x\)-value have different \(y\)-values; the reverse atom exchanges the two variables. Lax splitting disjunction allows a cover by subteams. Since dependence atoms are downward closed, any such cover can be made a partition without changing truth. Repeated occurrences of the same atom are separate available partition classes and cannot be collapsed. No equality of cardinalities of \(X,Y\) is assumed. The width bound is about the cardinality of *inclusion-minimal* falsifying subteams and applies to all finite teams in this signature.

## Proof

**Capacitated Hall characterization.** Let \(U\subseteq X\), \(V\subseteq Y\), and put \(e(U,V)=|T\cap(U\times V)|\). The formula \(\Phi_r\) is true exactly when
\[
 e(U,V)\leq r|U|+|V|\qquad\text{for every }U,V. \tag{1}
\]
For the forward direction, color every edge either one of the \(r\) row-functional colors or the single column-functional color. A row may contain at most one edge of each row color, and a column at most one of the column color, yielding (1). Conversely, build a bipartite matching instance with one node for each edge \((x,y)\) and with possible slots \((x,1),\ldots,(x,r),(y,*)\). Hall's inequalities for arbitrary collections of edges are equivalent to (1), since the slot neighborhood of a collection with row support \(U\) and column support \(V\) has size \(r|U|+|V|\). A saturating matching provides the required partition.

**Upper bound.** Let \(C\) be an inclusion-minimal falsifying team. Choose a rectangle \(U\times V\) violating (1). Every edge of \(C\) must lie in that rectangle: otherwise removing an outside edge would retain the violation. Hence the actual row and column supports of \(C\) also violate (1). Write their sizes \(a,b\). By minimality, deleting any one edge makes every Hall inequality true, so the full-support violation has deficit exactly one:
\[
 |C|=ra+b+1.\tag{2}
\]
For each row \(x\), its degree in \(C\) is at least \(r+1\); if the degree were at most \(r\), deleting all edges of that row would leave a matching satisfying (1), and the deleted row edges could be inserted into unused row-specific slots, contradicting failure of \(C\). Thus
\[
 (r+1)a\leq |C|=ra+b+1,
 \qquad a\leq b+1\leq q+1.
\]
Combining these gives \(|C|\leq(r+1)(q+1)\). When \(q\leq r\), every row has degree at most \(r\) and can be assigned entirely to its \(r\) separate row slots, proving universal satisfaction.

**Sharp cyclic construction.** Let \(q\geq r+1\). Use \(q+1\) distinct row labels and column set \(\mathbb Z/q\mathbb Z\). For each \(i\in\mathbb Z/q\mathbb Z\), put
\[
 N(i)=\{i,i+1,\ldots,i+r\}\pmod q,
 \qquad N(*)=N(0),
\]
where \(*\) is the extra row label. This defines exactly \((r+1)(q+1)\) distinct edges. Its full rectangle has one more edge than the Hall capacity \(r(q+1)+q\), so it fails \(\Phi_r\). On any proper column subset \(S\), the number of length-\((r+1)\) cyclic windows contained in \(S\) is at most \(|S|-r\) if any exist (decompose \(S\) into cyclic runs); duplicating the window at zero adds at most one. Thus the number of wholly contained row-neighborhoods is at most \(|S|\). Every other row contributes at most \(r\) edges to \(S\), whence (1) holds for every such rectangle. On the full column set, every proper subset of rows has at most \(q\) members and therefore contributes \((r+1)|U|\leq r|U|+q\). All proper rectangles obey (1). Removing any edge reduces the full-rectangle edge count to the capacity, while it cannot invalidate proper rectangles; the remaining team satisfies the formula. The original is consequently inclusion-minimal false, proving sharpness.

**Equality and converse.** If \(|C|=(r+1)(q+1)\), inequalities above force \(b=q\), \(a=q+1\), and equality in the degree sum. Every row therefore has degree precisely \(r+1\). For each proper \(S\subsetneq Y\), consider all rows whose entire neighborhoods lie in \(S\). Their rectangle has \((r+1)c\) edges, so (1) for this proper rectangle forces \(c\leq |S|\). Conversely, take any \(q+1\) labelled rows with neighborhoods of size \(r+1\) and this support condition. For a proper column set \(S\), at most \(|S|\) rows contribute \(r+1\) edges and all others at most \(r\), giving (1). For the full column set, (1) holds on every proper row subset because \(|U|\leq q\); the full rectangle alone exceeds its capacity by one. It follows that the team is inclusion-minimal false and extremal. This completes the characterization for every allowed parameter pair.

## Verification

Run `python3 checker.py` with the accompanying standalone Python script. It constructs cyclic witnesses for 19 distinct \((r,q)\) pairs with \(1\leq r\leq5\) and \(r+1\leq q\leq\min(8,r+4)\), checks that the full teams fail and every single-edge deletion succeeds, and compares two independently implemented tests: augmenting-path matching versus all Hall rectangles. It also compares the two semantics on every one of the \(2^9\) teams on a three-by-three board for each of the three capacities \(r=1,2,3\), and tests the non-falsifying regime. The expected output begins with `VERIFY_OK` and reports 19 cyclic parameter pairs and 2206 independent checks. The mathematical proof covers infinitely many parameter pairs; the finite tests are corroboration, not an exhaustive infinite certificate.

## Relationship to prior work

Fröhlich, Kolaitis and Meier classify disjunctions of **two** dependence atoms, including the opposite-pair \(r=1\) case; this theorem acknowledges that existing specialization. Barlag and coauthors motivate coherence and first-order rewritability but do not give the present exact \((r,q)\)-parameterized obstruction threshold. A previously published finite four-by-four Boolean-table result for the \(r=2\) three-way split classifies only the 292 minimal obstructions *when both sides are restricted to four value labels*; in particular, its largest minimal failure has thirteen assignments. The present sharp \(r=2,q=4\) example has five row labels and fifteen assignments, and cannot appear in that table. The capacitated matching and Hall criteria are classical ingredients; the all-parameter sharp obstruction width, cyclic extremizers and exact equality condition are the claimed contribution, not the matching theorem itself.

## Limitations

No claim is made for infinite teams, signatures with different dependence patterns, or minimal-falsifier *counts*. The extremal classification is by a Hall-type hypergraph condition, not an enumeration of all isomorphism classes. Historical priority remains provisional: a general treatment of capacitated transversal-matroid circuits could encode equivalent cases under another vocabulary. The result has been checked only in the same review setting; independent mathematical and historical-priority audits have not been performed.

## References

1. T. Barlag, N. Fröhlich, M. Hannula, P. G. Kolaitis, J. Kontinen, A. Meier and J. Väänänen, *Aspects of Coherence in Dependence Logic*, arXiv:2605.31269, first posted May 29, 2026. https://arxiv.org/abs/2605.31269
2. N. Fröhlich, P. G. Kolaitis and A. Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146, first posted August 22, 2025; CSL 2026, DOI: 10.4230/LIPIcs.CSL.2026.10. https://arxiv.org/html/2508.16146v1
3. *Exact 292 minimal obstructions for a three-way Boolean dependence split*, research record (2026), full RESULT.md: https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-292-minimal-obstructions-for-a-three-way-boolean-dependenc--3104d9c726df/RESULT.md
4. *Sharp minimal-falsifier spectra for inverse functional-dependence disjunctions*, research record (2026): https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-minimal-falsifier-spectra-for-inverse-functional-dependenc--2a96c3a15333
5. P. Hall, *On Representatives of Subsets*, Journal of the London Mathematical Society 10 (1935), 26–30 (classical marriage theorem).
