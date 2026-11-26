# All minimum capacity-limited dominating sets of rook graphs

## Finding

Let \(2\le m\le n\), let \(k\ge1\) be an integer, and let \(R_{m,n}=K_m\square K_n\) have labelled cells \([m]\times[n]\). A set \(D\) is **\(k\)-limited dominating** if each cell outside \(D\) is adjacent to a cell of \(D\), and each cell of \(D\) has at most \(k\) adjacent cells outside \(D\). Write \(\gamma_k^{\mathrm L}\) for its minimum size and \(H_{m,n}(k)\) for the number of distinct labelled minimum sets.

Define the explicit positive-integer function
\[
\Phi(a,b,t)=b!\,[x^b]\left(1+\sum_{j=t}^{b}\frac{x^j}{j!}\right)^a,\qquad a,b,t\ge1.
\]
It counts maps from a labelled \(b\)-element set to a labelled \(a\)-element set for which each nonempty fibre has at least \(t\) elements. The following statements also characterize **every** minimum set, not just their numbers.

**Unequal sides, \(m<n\):**

* If \(1\le k<m\), then \(\gamma_k^{\mathrm L}=n(m-k)\) and \(H_{m,n}(k)=\binom mk\). The minimum sets are obtained by omitting precisely \(k\) entire rows.
* If \(m\le k\le n-2\), put \(A=m(n-k)\) and \(T=m+n-1-k\). Then \(\gamma_k^{\mathrm L}=\min\{n,A\}\). Whenever \(A\le n\), one type of minimum set consists of exactly \(n-k\) complete columns, giving \(\binom n{n-k}\) possibilities. Whenever \(n\le A\), the other type has exactly one selected cell in every column; each nonempty row contains at least \(T\) selected cells, giving \(\Phi(m,n,T)\) possibilities. Both types occur when \(A=n\), and they are disjoint. Thus
\[
H_{m,n}(k)=\begin{cases}
\binom n{n-k},&A<n,\\
\binom n{n-k}+\Phi(m,n,T),&A=n,\\
\Phi(m,n,T),&A>n.
\end{cases}
\]
* If \(k\ge n-1\), then \(\gamma_k^{\mathrm L}=m\). Every minimum set has one selected cell in each row and at least \(T=\max\{1,m+n-1-k\}\) cells in each occupied column, and
\[
H_{m,n}(k)=\Phi(n,m,T).
\]

**Square boards, \(m=n=q\):**

* If \(1\le k\le q-2\), then \(\gamma_k^{\mathrm L}=q(q-k)\), \(H_{q,q}(k)=2\binom qk\), and the minimum sets are complements of \(k\) entire rows or of \(k\) entire columns.
* If \(k\ge q-1\), then \(\gamma_k^{\mathrm L}=q\), and every minimum set has exactly one selected cell in each row, or exactly one in each column. In the first case each occupied column must contain at least \(T=\max\{1,2q-1-k\}\) cells; the second case is its transpose. The two classes intersect precisely in permutation matrices when \(k\ge2q-2\). Consequently,
\[
H_{q,q}(k)=2\Phi(q,q,T)-\mathbf1_{\{k\ge2q-2\}}q!.
\]

This is a complete labelled classification for all positive capacities and all rook graphs with both sides at least two. The numerical minimum formula itself and its low-capacity cases are not asserted to be new; the contribution is the **all-regimes characterization and exact enumeration of minimizers**, including the nontrivial transition between row-wise and column-wise families.

## Assumptions and scope

All graphs are finite, simple and undirected. Rows have \(n\) cells and columns have \(m\) cells. Two distinct cells are adjacent exactly when they share a row or column. Every selected cell is counted once, and the board's rows and columns retain their labels; no quotient by automorphisms is taken. Capacities \(k\ge m+n-2\) are allowed: then the extra constraint is vacuous. The class \(m=1\) reduces to an ordinary complete graph and is excluded from the nontrivial theorem.

## Proof

**1. Domination and capacity equations.** For a set \(D\), let \(r_i\) and \(c_j\) be its number of cells in row \(i\) and column \(j\), respectively. A cell \((i,j)\in D\) has precisely
\[
(n-r_i)+(m-c_j)
\]
neighbors outside \(D\). Moreover, \(D\) dominates all omitted cells if and only if either every row or every column meets \(D\). Indeed, an empty row and an empty column intersect in an undominated cell; conversely, an omitted cell in a nonempty row (or column) has a selected neighbor in that row (or column).

**2. The small-capacity optimum and its rigidity.** Suppose \(1\le k<m\). Put \(Z=([m]\times[n])\setminus D\), and let \(a_i=n-r_i\) and \(b_j=m-c_j\). If \(s\ge1\) rows lie entirely in \(Z\), there can be no entirely omitted column; the capacity inequality for any selected cell forces \(s\le k\) and \(a_i\le k-s\) in all other rows. Therefore
\[
|Z|\le sn+(m-s)(k-s)\le kn.
\]
Since \(n\ge m\) and \(s>0\), equality holds only for \(s=k\), in which case the other rows contain no omitted cells.

If instead \(t\ge1\) columns lie entirely in \(Z\), there is no entirely omitted row and similarly \(t\le k\), with \(b_j\le k-t\) for all other columns. Consequently
\[
|Z|\le tm+(n-t)(k-t)\le kn.
\]
The second inequality is strict for \(m<n\); equality when \(m=n\) requires \(t=k\), leaving no other omissions.

Finally suppose that no row or column is entirely omitted. Every row contains a selected cell, so \(a_i\le k\) and \(|Z|\le mk\le nk\). For \(m<n\) this is strict. If \(m=n\) and equality held, every row would have exactly \(k\) omitted cells. Some column contains an omission and, being nonempty in \(D\), also contains a selected cell. That cell has \(k\) omitted neighbors in its row and at least one in its column, contradicting its capacity. Thus equality is again impossible. Omitting \(k\) complete rows attains \(|Z|=kn\); omitting \(k\) complete columns additionally attains it when \(m=n\). All equality cases above give precisely the claimed low-capacity minimizers and counts.

**3. The unequal-side intermediate regime.** Assume \(m<n\) and \(m\le k\le n-2\). If every row meets \(D\), the displayed capacity equation implies \(r_i\ge n-k\) in each row, whence \(|D|\ge A=m(n-k)\). If equality holds, every row contains exactly \(n-k\) selected cells. Each selected cell then has \(k\) omitted neighbors in its row, so its column must contain no omission. Hence \(D\) is exactly a union of \(n-k\) complete columns. Conversely, every such union is admissible.

If a row is empty, all columns meet \(D\), so \(|D|\ge n\). If equality holds, each column contains exactly one selected cell. At a selected cell belonging to a row with \(r_i\) selections, the number of outside neighbors is \(n-r_i+m-1\); the capacity condition is therefore equivalent to \(r_i\ge T=m+n-1-k\). The converse is immediate from the same equation and the fact that every column meets \(D\). Counting such functions from columns to row labels gives \(\Phi(m,n,T)\). A full row and a selection of \(n-k\) full columns realize both possible bounds, yielding the claimed minimum and all three comparison cases, including the disjoint union at \(A=n\).

**4. Large capacities and all square boundaries.** For any rook board with \(m\le n\), domination itself requires at least \(m\) selected cells: either each of the \(m\) rows or each of the \(n\) columns meets \(D\). At \(k\ge n-1\), selecting one full column attains this bound.

When \(m<n\), a minimum set of size \(m\) cannot occupy every column, so it must contain exactly one cell in each row. If column \(j\) contains \(c_j>0\) selected cells, a selected cell there has \((n-1)+(m-c_j)\) outside neighbors. Thus precisely those row-to-column maps with nonempty fibres of size at least \(\max\{1,m+n-1-k\}\) are admissible, giving \(\Phi(n,m,T)\).

For \(m=n=q\), a minimum set of size \(q\) must occupy every row exactly once or every column exactly once. The same capacity calculation gives \(\Phi(q,q,T)\) configurations in either orientation. A configuration has both properties exactly when it is a permutation matrix; its outside degree at each selected cell is \(2q-2\). Thus the two classes intersect if and only if \(k\ge2q-2\), in exactly \(q!\) sets. For \(k\le q-2\) Step 2 applies. This covers all parameters and completes the proof.

**5. Why \(\Phi\) is exact.** For each of \(a\) labelled targets, the exponential generating function for a fibre containing either zero or at least \(t\) labelled source elements is \(1+\sum_{j=t}^{b}x^j/j!\). Multiplication over all \(a\) targets and extraction of \(b![x^b]\) counts every function exactly once, without identifying symmetric assignments.

## Verification

Run `python3 verify.py` with Python 3 and no nonstandard dependencies. The program builds the rook graph's open-neighborhood bit masks directly, exhaustively tests every vertex subset for domination and its **minimum feasible capacity**, computes every optimal cardinality/count for all capacities up to the graph's degree, and independently checks membership in the listed structural families and the coefficient formula for \(\Phi\).

This exhaustive comparison passed on ten labelled boards from \(2\times2\) through \(4\times5\), including \(3\times6\), across 49 distinct positive-capacity parameter cases. In particular, the \(3\times6\) board at capacity \(4\) has exactly 18 minimum sets of size 6 (15 column unions plus 3 single-row sets), and the \(4\times4\) board at capacity \(5\) has exactly 80 minimum sets of size 4. The code establishes only these finite checks; the general classification follows from Steps 1–5 above.

## Relationship to prior work

Božović, Radić, Kovijanić-Vukićević and Tepeh introduced \(k\)-limited domination and gave general inequalities and values for paths, cliques and complete bipartite graphs. Tepeh's subsequent paper on Cartesian products proves bounds and, in Proposition 6 of version 2, the rook-graph special case \(\gamma_k^{\mathrm L}(K_{k+2}\square K_{k+2})=2(k+2)\). The result here treats the **entire family of minimum vertex subsets**, not merely a minimum cardinality in that special square family.

On the regular rook graph of degree \(m+n-2\), the condition for a selected vertex is equivalent to requiring at least \(m+n-2-k\) selected neighbours; this is the usual \((1,t)\)-domination formulation when \(t=m+n-2-k\) is nonnegative. Thus searching only the recently introduced name is insufficient. The cited Cartesian-product paper and targeted searches using the equivalent terminology did not yield this complete optimum-set census.

The numerical minimum in rectangular rook graphs and the lowest-capacity optimum patterns are not a novelty assertion here. A prior classification of cardinality distributions for the two-row case is likewise not new; the present claimed refinement concerns every side length at least three and every capacity, with explicit intermediate-regime fibre-size constraints and counts. Mertens' 2024 rook-graph domination polynomial counts dominating sets without the \(k\)-limited capacity restriction, so its coefficients alone do not determine the asserted restricted minimum-set multiplicities.

## Limitations

The proof is for rook graphs \(K_m\square K_n\) with \(m,n\ge2\), not arbitrary Cartesian products. It does not enumerate all nonminimum \(k\)-limited dominating sets. The intermediate-case number of optimum sets is expressed by an explicit finite coefficient extraction rather than a simplified elementary expression. Exhaustive testing covers only the listed finite boards. Bibliographic priority for the full minimum-set enumerator is assessed against the inspected accessible sources and mathematical search results but cannot be guaranteed; independent review has not yet been performed.

## References

1. D. Božović, G. Radić, Ž. Kovijanić-Vukićević, A. Tepeh, *On \(k\)-limited domination in graphs*, arXiv:2606.22422 (first posted 2026-06-21), https://arxiv.org/abs/2606.22422.
2. A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428, version 2 (2026-10-01; first posted 2026-06-21), particularly Section 4 and Proposition 6, https://arxiv.org/html/2606.22428.
3. S. Mertens, *Domination Polynomial of the Rook Graph*, Journal of Integer Sequences 27 (2024), Article 24.3.7, https://cs.uwaterloo.ca/journals/JIS/VOL27/Mertens/mertens6.html.
