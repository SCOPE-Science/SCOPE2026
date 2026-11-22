# A four–six obstruction dichotomy for splitting independence from dependence

## Finding

Let \(Y,Z\) be finite nonempty labelled sets with \(|Y|=p\) and \(|Z|=q\), and let \(T\subseteq Y\times Z\) be a set of assignments to two named variables. Under ordinary lax team semantics, consider
\[
\Phi=(y\perp z)\lor\operatorname{dep}(y,z).
\]
The first atom means that its subteam is a Cartesian product of its two coordinate projections; the second means that each \(y\)-value is associated with at most one \(z\)-value. Define the set of multiply occupied rows and its shared columns by
\[
H(T)=\{a\in Y:|N_T(a)|\ge2\},\qquad
I(T)=\bigcap_{a\in H(T)}N_T(a),
\]
where \(N_T(a)=\{b\in Z:(a,b)\in T\}\). The intersection is used only when \(H(T)\ne\varnothing\).

**Theorem.** The following exact satisfaction criterion holds:
\[
\boxed{T\models\Phi\quad\Longleftrightarrow\quad
H(T)=\varnothing\ \text{or}\ \max_{a\in H(T)}|N_T(a)\setminus I(T)|\le1.}
\]
Every *falsifying* finite team contains a falsifying subteam of at most six assignments. All inclusion-minimal falsifying teams are, up to permutations of the two labelled alphabets within each coordinate, precisely these two bipartite edge sets:

1. Two disjoint two-edge stars centered at two different \(y\)-vertices, with four different \(z\)-vertices, having four assignments.
2. An induced six-edge cycle between three \(y\)-vertices and three \(z\)-vertices, equivalently the three row neighborhoods \(\{a,b\},\{a,c\},\{b,c\}\), having six assignments.

The exact labelled minimal-falsifier enumerator is
\[
\boxed{M_{p,q}(t)=\binom p2\binom q2\binom{q-2}2t^4+6\binom p3\binom q3t^6,}
\]
with every binomial term understood as zero when its displayed lower argument exceeds the nonnegative upper argument (in particular, the first term vanishes when \(q<4\)). The uniform six-assignment refutation bound is sharp whenever \(p\ge3,q\ge3\). For finite sets of all sizes, the criterion also constructs a satisfying split in time \(O(|T|+p+q)\) using row and column counts.

## Assumptions and scope

All teams are ordinary *sets*, not bags or probabilistic relations. The language has exactly the displayed two variables; the alphabets may be different subsets of one ambient universe. For a team \(S\subseteq Y\times Z\), the independence atom \(y\perp z\) holds if every combination of its observed \(y\)- and \(z\)-values occurs in \(S\). Thus \(S=A\times B\) for its two projections, including the empty-team case. The functional-dependence atom \(\operatorname{dep}(y,z)\) requires \(|N_S(a)|\le1\) for every \(a\). The disjunction holds if there exist subteams \(U,V\subseteq T\), possibly overlapping or empty, with \(T=U\cup V\), \(U\models y\perp z\), and \(V\models\operatorname{dep}(y,z)\).

A *minimal falsifier* is a team that fails \(\Phi\) but whose every proper subteam satisfies it. Because the independence atom is not downward closed, this result is a **one-way local-refutation theorem**, not an equivalence between satisfaction and satisfaction of all bounded-size subteams. No finite uniform alphabet bound is assumed.

## Proof

**1. Exact split normal form.** Suppose \(T=U\cup V\) witnesses the disjunction. Since \(U\models y\perp z\), write \(U=A\times C\subseteq T\), where \(A\subseteq Y\) and \(C\subseteq Z\). Since \(V\) is row-functional, every row of degree at least two in \(T\) must contain at least one assignment in \(U\). Hence \(H(T)\subseteq A\). Because \(U\) is a rectangle, \(C\subseteq N_T(a)\) for every \(a\in H(T)\), so \(C\subseteq I(T)\). Moreover, every assignment of \(T\) outside \(U\) lies in \(V\), which has at most one assignment in each row. Thus each \(a\in H(T)\) has at most one neighbor outside \(C\), hence at most one outside \(I(T)\). If \(U=\varnothing\), the same conclusion follows because \(H(T)=\varnothing\).

Conversely, when \(H(T)=\varnothing\), choose \(U=\varnothing,V=T\). Otherwise put \(U=H(T)\times I(T)\) and \(V=T\setminus U\). By the definition of \(I(T)\), \(U\subseteq T\) and is a Cartesian rectangle. The assumed inequality makes \(V\) row-functional on active rows; inactive rows already have degree at most one. Thus \(U,V\) witness \(\Phi\). This also justifies replacing an overlapping split by the particular disjoint split in the construction; it does **not** use downward closure of independence.

**2. Extract a witness with at most six assignments.** Suppose the criterion fails. Then some active row \(r\in H(T)\) has two distinct neighbors \(a,b\notin I(T)\). Since \(a\notin I(T)\) there is an active row \(u\) missing \(a\); since \(b\notin I(T)\) there is an active row \(v\) missing \(b\). Neither \(u\) nor \(v\) equals \(r\).

If \(u=v\), choose any two distinct neighbors \(c,d\in N_T(u)\). They are different from \(a,b\), so the four edges \((r,a),(r,b),(u,c),(u,d)\) form two disjoint two-edge stars.

If \(u\ne v\), choose any two neighbors of \(u\) and any two neighbors of \(v\); call those two-element sets \(P_u,P_v\), and put \(P_r=\{a,b\}\). The three selected row pairs have empty common intersection because \(a\notin P_u\) and \(b\notin P_v\). Any three two-element sets with empty total intersection either contain two disjoint sets or are pairwise intersecting with empty triple intersection. In the former case, their four corresponding edges form two disjoint two-edge stars. In the latter case, the three sets must be exactly \(\{a',b'\},\{a',c'\},\{b',c'\}\) for three distinct elements \(a',b',c'\), yielding the six-edge alternating cycle. In either case the selected edges form a subteam of \(T\).

**3. These, and only these, are inclusion-minimal falsifiers.** In the disjoint-star team, both occupied rows have degree two but their neighborhoods have empty intersection. In the six-cycle team, all three occupied rows have degree two and their three pairwise-intersecting neighborhoods have empty total intersection. In both cases the criterion fails. Deleting an edge of the disjoint-star team leaves at most one row of degree two, hence satisfies the criterion. Deleting an edge of the six-cycle leaves exactly two rows of degree two, sharing one neighbor; each has exactly one neighbor outside this common column, so the remaining team satisfies the criterion. Moreover, every subteam of each resulting edge-deleted team is also satisfying: there can be at most one active row in the four-edge case; in the six-edge case the only two active rows have neighborhoods of size two and meet in one column, so deleting more edges cannot create a new pair of active rows whose neighborhoods are disjoint. Thus every *proper* subteam of either pattern satisfies the formula, despite the formula's non-downward-closure in general.

Step 2 shows every falsifier contains one of these falsifying patterns. Hence a minimal falsifier must equal one such pattern, proving the classification and the sharp six-edge bound. Three rows and three columns suffice for the cycle, so no smaller universal bound is possible when \(p,q\ge3\).

**4. Exact labelled counts.** To form the four-edge pattern, choose its two distinct rows in \(\binom p2\) ways, two columns for the first row in \(\binom q2\) ways, and two disjoint columns for the other in \(\binom{q-2}2\) ways. Taking the first row to be the earlier one in a fixed ordering counts each labelled team once. For the six-cycle choose three rows and three columns and a bijection assigning to each row its unique *missing* column in the \(3\)-by-\(3\) grid. There are \(3!=6\) bijections. Distinct choices give distinct teams; the patterns have different sizes. These observations yield the displayed polynomial for all positive \(p,q\).

**5. Constructive linear-time test.** One pass over the assignments produces each row's degree and active-row set \(H(T)\). Count, for every \(z\)-value, how many active rows contain it. A column belongs to \(I(T)\) precisely when that count equals \(|H(T)|\); for each active row, check that at most one incident column has a smaller count. This uses \(O(|T|+p+q)\) operations for ordinary indexed incidence input. When it succeeds, Step 1 gives an explicit split. \(\square\)

## Verification

The accompanying standard-library `checker.py` separately implements the original lax-splitting semantics by enumerating candidate independent-rectangle subteams and testing the complement for functional dependence. It compares that direct semantic procedure with the row-intersection criterion on all \(848\) teams from the four rectangles of sizes \(2\)-by-\(2\), \(2\)-by-\(3\), \(2\)-by-\(4\), and \(3\)-by-\(3\). It additionally classifies all inclusion-minimal failures in each of seven rectangles, up to \(4\)-by-\(4\), for a total of \(74{,}576\) team checks. The observed labelled counts \((\#4,\#6)\) are \((0,0),(0,0),(6,0),(0,6),(18,24),(0,24),(36,96)\) for rectangles \((2,2),(2,3),(2,4),(3,3),(3,4),(4,3),(4,4)\), respectively, exactly the polynomial's coefficients. It also checks a satisfying complete rectangle containing a falsifying six-edge cycle, validating the non-downward-closure warning. Run `python3 checker.py` with Python 3 standard library only. The program prints `ALL_OK` after all assertions pass.

These finite checks corroborate the formula and its normalization; they are not a proof for arbitrarily large alphabets. The steps above supply the general proof.

## Relationship to prior work

Fröhlich, Kolaitis and Meier (2025/2026) analyze disjunctions of two **dependence** atoms, including unbounded-minimal-failure behavior in their Theorem 25. Their full open text does not cover the mixed pure-independence/dependence formula here. Barlag et al. (2026) develop coherence criteria for dependence logic; their setting excludes the non-downward-closed pure-independence atom in this theorem. The mixed formula is consequently **not** asserted to be coherent simply because it has bounded-size refutations.

The classical independence atom interprets as rectangularity of a binary team, while a functional-dependence atom interprets as a one-sided partial function. Their conjunction with *splitting disjunction* rather than Boolean disjunction creates a distinct, naturally motivated edge decomposition. Prior results for the inverse-dependence disjunction \(\operatorname{dep}(y,z)\lor\operatorname{dep}(z,y)\) characterize pseudoforests and allow minimal failures of unbounded size as the alphabets grow; that statement neither implies nor follows from the present four/six mixed-atom classification. Graph-partition work on bicliques, matchings and Ferrers subgraphs studies different families of allowable components and partition-number questions, not this specified one-biclique/one-sided-star-forest exact obstruction census. Novelty relative to equivalent formulations elsewhere remains subject to further literature review.

## Limitations

The fixed formula, named coordinate directions, set teams, and lax splitting convention are essential. The two sides of the disjunction have asymmetric roles; exchanging \(y,z\) requires exchanging the direction of the functional dependency as well. The theorem does not count all satisfying teams or apply to arbitrary additional unprojected attributes. Although every falsifier has a falsifying subteam of size at most six, **some satisfying teams contain falsifying subteams**: the full \(3\)-by-\(3\) rectangle satisfies \(y\perp z\) but contains an alternating six-cycle that fails \(\Phi\). Consequently an absence-of-small-falsifiers criterion for satisfaction, or ordinary coherence in the downward-closed sense, is not claimed. Computational checks are finite and no independent mathematical or historical-priority validation has occurred.

## References

1. N. Fröhlich, P. G. Kolaitis and A. Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146v1 (first posted 2025-08-22), *Computer Science Logic* 2026, DOI 10.4230/LIPIcs.CSL.2026.10. Open full text: https://arxiv.org/html/2508.16146v1.
2. T. Barlag, N. Fröhlich, M. Hannula, P. G. Kolaitis, J. Kontinen, A. Meier and J. Väänänen, *Aspects of Coherence in Dependence Logic*, arXiv:2605.31269v1 (first posted 2026-05-29), https://arxiv.org/html/2605.31269v1.
3. L. Győrffy, A. London, G. V. Nagy and A. Pluhár, *Partitions of Graphs into Special Bipartite Graphs*, arXiv:2412.12664v1 (first posted 2024-12-17), https://arxiv.org/abs/2412.12664.
4. J. Kontinen, A. Meier and Y. Mahmood, *A Parameterized View on the Complexity of Dependence and Independence Logic*, *Journal of Logic and Computation* 32 (2022), 1624–1644. Background on mixed-atom model checking; no priority for the exact stated census is claimed.
