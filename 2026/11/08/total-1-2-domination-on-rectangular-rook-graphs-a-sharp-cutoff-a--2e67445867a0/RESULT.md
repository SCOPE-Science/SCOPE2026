# Total \([1,2]\)-domination on rectangular rook graphs: a sharp cutoff and complete enumerator

## Finding
Let \(m,n\geq2\) be integers, and let \(R_{m,n}=K_m\square K_n\) be the rook graph on a labelled \(m\)-by-\(n\) array. A subset \(S\) is *total \([1,2]\)-dominating* if every vertex, including those belonging to \(S\), has one or two neighbors in \(S\). Set
\[
P_{m,n}(z)=\sum_{\substack{S\subseteq V(R_{m,n})\\1\leq |N(v)\cap S|\leq2\ \forall v}}z^{|S|},
\qquad a=\min(m,n),\quad b=\max(m,n).
\]
Every admissible subset has one of the following explicit forms, up to interchange of rows and columns:

1. If \(a=2\), the subset comprises one or two entire columns; or one entire column and a single cell in another column; or one entire row, the last possibility existing only for \(b=2\) or \(b=3\).
2. If \(a=3\), the subset comprises one entire three-cell column, and when \(b=3\) there are additionally the three entire rows.
3. If \(a\geq4\), no admissible subset exists.

Consequently, writing \(\mathbf1_E\) for the indicator of proposition \(E\), the **complete cardinality enumerator** is
\[
\boxed{P_{m,n}(z)=\begin{cases}
\bigl(b+2\mathbf1_{b=2}\bigr)z^2+\bigl(2b(b-1)+2\mathbf1_{b=3}\bigr)z^3+\binom b2 z^4,&a=2,\\[2pt]
\bigl(b+3\mathbf1_{b=3}\bigr)z^3,&a=3,\\[2pt]
0,&a\geq4.
\end{cases}}
\]
In particular, with the standard convention that the minimum is \(+\infty\) when the class is empty,
\[
\gamma_{t[1,2]}(R_{m,n})=\begin{cases}2,&a=2,\\3,&a=3,\\+\infty,&a\geq4.\end{cases}
\]
Thus a two-dimensional complete-graph Cartesian product admits a total \([1,2]\)-dominating set **exactly when one factor has order at most three** (within the stated domain).

## Assumptions and scope
All graphs are finite, undirected and simple. Neighborhoods are **open**: a selected vertex does not count itself. Rows and columns are individually labelled; polynomial coefficients count subsets of the labelled vertex set, not equivalence classes under automorphisms. Graphs with a singleton factor are excluded. The indicators at \(b=2\) and \(b=3\) distinguish genuine small-board boundary families, not artificial corrections.

## Proof
Write \(x_{ij}=1\) if square \((i,j)\) is selected, and \(x_{ij}=0\) otherwise. Let \(r_i=\sum_{j=1}^n x_{ij}\) and \(c_j=\sum_{i=1}^m x_{ij}\). Each square has exactly \(r_i+c_j-2x_{ij}\) selected rook neighbors, because a selected square must be excluded once from its row count and once from its column count. Therefore the defining condition is **equivalent**, with no hidden restriction, to
\[
\tag{1}1\leq r_i+c_j-2x_{ij}\leq2\qquad(1\leq i\leq m,\ 1\leq j\leq n).
\]

**Lemma (the two-small-degrees obstruction).** Assume \(m,n\geq3\), all row counts are at most two, and all column counts are at most two. Then (1) has no solution. Indeed, suppose some row has two selected squares, in columns \(j,k\). Every square of that row in another column is unselected and has at least two selected row neighbors. By the upper inequality, each such other column has count zero. There is at least one zero column because \(n\geq3\). The lower inequality at every square in that column forces **every** row to contain a selection. Both active columns already have one selection in the distinguished row and can have at most one more each. Since \(m\geq3\), necessarily \(m=3\), with the two other rows selecting exactly one square each, in different active columns. Both active columns then have count two. At the unselected crossing of one of these one-selection rows with the other active column, the selected-neighbor count is \(1+2=3\), a contradiction. Hence no row count equals two. Interchanging rows and columns yields no column count equal to two. Every selected square would consequently have row and column counts both one, making its selected-neighbor count \(1+1-2=0\). If there were no selected square, every neighborhood count would also be zero. This proves the lemma.

Now suppose \(m,n\geq3\) and an admissible set exists. The lemma forces a row or column count of at least three. If some row has \(r_i\geq3\), an unselected square in that row would already have at least three selected neighbors, so the **whole** row is selected, with \(r_i=n\). At each selected square in that row, (1) requires \(n+c_j-2\leq2\); because \(c_j\geq1\), this implies \(n\leq3\). As \(n\geq3\), necessarily \(n=3\) and each \(c_j=1\). Hence the selected set is exactly one full row. Conversely a full three-cell row obeys (1): its own cells have two selected neighbors and every other cell has one. Transposing shows that a column of count at least three forces \(m=3\) and the set to be exactly one full three-cell column. Therefore all solutions with \(m,n\geq3\) are exactly those stated above. The column sets number \(n\) when \(m=3\), and there are \(m\) additional row sets when \(n=3\); if both dimensions equal three these are distinct, giving six sets.

It remains to classify \(m=2\), with \(n\geq2\). Describe each column by whether it has zero, one, or two selected squares. First suppose **no column is a singleton**. Let \(t\) be the number of double columns. Every vertex, selected or not, then has exactly \(t\) selected neighbors. Thus (1) is equivalent to \(t=1\) or \(t=2\). These contribute \(n\) sets of cardinality two and \(\binom n2\) sets of cardinality four.

Next suppose there is a singleton column selecting the top row, and let \(r_1,r_2\) be the two row counts. At the selected top square of that singleton column, (1) says \(1\leq r_1-1\leq2\), so \(r_1\in\{2,3\}\). At its unselected bottom square, it says \(1\leq r_2+1\leq2\), so \(r_2\leq1\). A singleton column selecting the bottom row would instead force \(r_2\geq2\), which is impossible. Thus **all** singleton columns have the same orientation.

If there is a double column, the bottom row has \(r_2\geq1\), hence exactly one double column and \(r_2=1\). A selected square in that double column has exactly \(r_1\) neighbors when it lies in the top row, forcing \(r_1\leq2\). Therefore \(r_1=2\), and the set consists of a double column plus a top-row singleton in a different column. All such sets satisfy (1), and, allowing either row as top, they number \(2n(n-1)\), each of cardinality three.

If there is no double column, the bottom row has no selected squares. Any empty column would contain a bottom square with zero selected neighbors, so there are no empty columns. The entire top row is therefore selected, and its selected squares have exactly \(n-1\) selected neighbors. Equation (1) holds precisely when \(n\in\{2,3\}\). There are two choices of selected row, contributing \(2z^2\) when \(n=2\) and \(2z^3\) when \(n=3\). The three cases are mutually exclusive and exhaustive. Adding their contributions gives the asserted polynomial for \(m=2\), finishing the proof.

## Verification
Two standalone, independently constructed programs and their captured outputs accompany this statement. `verify_direct.py` examines every vertex subset, computing open-neighborhood intersections directly from an adjacency bitmask. It checks all boards \((2,n)\) for \(2\leq n\leq8\), all \((3,n)\) for \(3\leq n\leq6\), and \((4,4),(4,5)\). `verify_profiles.py` instead enumerates feasible column masks by a dynamic program conditioned on the eventual row degrees; it checks 19 boards, including \((2,20),(3,12),(4,8),(5,6),(6,6)\). The recorded outputs end in `DIRECT_CHECK_PASS 13` and `PROFILE_DP_PASS 19` respectively. Run each with standard Python 3, without third-party dependencies. The finite tests are corroborative; the proof above establishes every parameter value in the specified infinite family.

## Relationship to prior work
Chellali, Haynes, Hedetniemi and McRae (2013) introduce \([1,2]\)-sets and explicitly pose total \([1,2]\)-domination as a question. Their discussion of \(K_p\square K_2\) concerns *non-total* \([1,2]\)-dominating sets: its conditions apply only to vertices outside the selected set, so it does not imply the present result, where selected squares must also have one or two selected neighbors. Lv and Wu's 2015 preprint (later published in 2018) studies total \([1,2]\)-domination, sharp bounds and generic sufficient nonexistence conditions, not the all-set classification of rectangular rook graphs. Zhang, Shao and Yang (2017) treat toroidal **cycle** products \(C_3\square C_n\) and \(C_4\square C_n\), not the two-parameter family \(K_m\square K_n\). The \((3,3)\) numerical minimum is already implied by their \(C_3\square C_3\) special case; neither that special case nor the other cited statements implies the new general feasibility threshold or the polynomial coefficients. Subsequent work on total \(k\)-domination of products of complete graphs imposes a lower bound on selected neighbors, but no upper bound of two, and likewise does not determine this polynomial. Prior publication of an equivalent full classification has not been ruled out absolutely.

## Limitations
The parameter is fixed to the **open-neighborhood interval** \([1,2]\), and the theorem does not claim a formula for arbitrary intervals, for higher-dimensional Hamming graphs, or for non-total \([1,2]\)-sets. Small-board program checks are not the proof of the all-order zero region. The early literature contains a closely related non-total construction; direct access to the complete publisher version of that source was restricted, and unindexed earlier calculations remain an originality risk. This statement has not received independent scholarly review.

## References
1. M. Chellali, T. W. Haynes, S. T. Hedetniemi and A. McRae, *[1, 2]-sets in graphs*, Discrete Applied Mathematics **161** (2013), 2885–2893, DOI `10.1016/j.dam.2013.06.012`.
2. X. Lv and B. Wu, *Total [1,2]-domination in graphs*, arXiv `1503.04939v1`, posted 2015-03-17; later Acta Mathematicae Applicatae Sinica English Series **34** (2018), 801–812, DOI `10.1007/s10255-018-0792-4`.
3. X. Zhang, Z. Shao and H. Yang, *The [a,b]-domination and [a,b]-total Domination of Graphs*, Journal of Mathematics Research **9** (2017), 38–45, DOI `10.5539/jmr.v9n3p38`.
4. W. Carballosa and J. Wisby, *Total \(k\)-domination in Cartesian product of complete graphs*, arXiv `2001.07850v4`; DOI `10.1016/j.dam.2023.04.008`.
