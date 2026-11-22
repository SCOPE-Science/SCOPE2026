# Sharp all-or-nothing exchange connectivity among labelled Turán extremizers

## Finding

Fix integers \(s\ge2\) and \(n\ge s+1\), and write \(n=sq+r\) with \(0\le r<s\). Among simple graphs on the fixed labelled vertex set \([n]\), let \(\mathcal T_{n,s}\) be those with the maximum number of edges under the constraint of containing no \(K_{s+1}\). By the classical equality case of Turán's theorem, these are precisely the balanced complete \(s\)-partite graphs, with \(r\) parts of size \(q+1\) and \(f=s-r\) parts of size \(q\).

For a positive integer \(b\), the *batch-exchange graph* \(\mathcal R_b(n,s)\) has vertex set \(\mathcal T_{n,s}\); two distinct graphs are adjacent when one can be changed into the other by removing and replacing at most \(b\) edges, while keeping the edge count maximal at both endpoints. Intermediate subgraphs within one batch are not required to be extremal.

**Theorem.** All graphs \(\mathcal R_b(n,s)\) are edgeless for \(b<b_*\), and connected for \(b\ge b_*\), where
\[
b_*(n,s)=\begin{cases}q,&r>0,\\2(q-1),&r=0.\end{cases}
\]
At the first connected threshold, the graph is regular of degree
\[
d_*(n,s)=\begin{cases}
r\bigl(2f+\binom f2\bigr),&q=1,\\
3rf+2\binom f2,&q=2,\ r>0,\\
(q+1)rf,&q\ge3,\ r>0,\\
2\binom s2,&q=2,\ r=0,\\
q^2\binom s2,&q\ge3,\ r=0.
\end{cases}
\]
There are precisely
\[
N_{n,s}=\frac{n!}{(q!)^{f}((q+1)!)^{r}f!r!}
\]
vertices in \(\mathcal R_b(n,s)\). The enumeration of balanced partitions is classical context, not a separate novelty claim.

**Exact exchange metric.** For the partitions \(P=\{A_1,\ldots,A_s\}\) and \(Q=\{B_1,\ldots,B_s\}\) associated with two extremizers, the number of edges to replace is
\[
\delta(P,Q)=\sum_{i=1}^s\binom{|A_i|}{2}-\sum_{i,j=1}^s\binom{|A_i\cap B_j|}{2}.
\]
This expression is independent of the choices of part ordering.

For the triangular graph \(L(K_n)\), the established characterization of its maximum mutual-visibility sets as \(K_4\)-free root-edge maximizers makes the case \(s=3\) a visibility-reconfiguration corollary: with \(n=3q\ge6\) the threshold is \(2(q-1)\); with \(n=3q+1\) or \(3q+2\) it is \(q\).

## Assumptions and scope

All graphs are finite simple undirected graphs on the same *labelled* ground set. Two extremal graphs that are isomorphic but have different edge sets are treated as distinct. Exactly \(s\) nonempty independent parts occur because \(n\ge s+1\). The batch size is the number of deleted (equivalently inserted) edges, not the symmetric-difference size. A batch operation is atomic, so feasibility is required at its endpoints only. The case \(n=s\), where the only extremizer is \(K_s\), is excluded.

## Proof

**1. Structural starting point.** Turán's equality theorem says every \(G\in\mathcal T_{n,s}\) is complete multipartite with block sizes \(q\) and \(q+1\). Its missing-edge set is exactly the disjoint union of the cliques \(K_{|A_i|}\) on its independent blocks. This also gives the displayed count \(N_{n,s}\).

**2. Exchange distance.** Both edge sets have the same cardinality. Count pairs that lie inside one block of \(P\) but not inside one block of \(Q\). The total inside-block pairs for \(P\) are \(\sum_i\binom{|A_i|}{2}\), and those inside blocks for both \(P\) and \(Q\) are \(\sum_{i,j}\binom{|A_i\cap B_j|}{2}\). Their difference is \(|E(Q)\setminus E(P)|=|E(P)\setminus E(Q)|\), proving the metric formula.

**3. Lower bound on nonzero exchange distance.** Call an old block *split* if its vertices occur in more than one new block. A split block of size \(t\) contributes at least \(t-1\) to \(\delta\): among its \(\binom t2\) pairs, at most \(\binom{t-1}2\) survive together in one new block. For \(r=0\), if only one old block were split, the other \(s-1\) intact \(q\)-blocks would fill \(s-1\) distinct new \(q\)-blocks, forcing the last block to remain intact too. Hence at least two blocks split and \(\delta\ge2(q-1)\). If \(r>0\) and \(q\ge2\), any split old block of size \(q+1\) gives \(\delta\ge q\). Otherwise only size-\(q\) blocks split. At least two must do so: with exactly one split size-\(q\) block, all other intact blocks occupy distinct new blocks, since \(2q>q+1\); the last new block would have to equal the purported split block. Two split small blocks yield \(\delta\ge2(q-1)\ge q\). For \(q=1\) any two distinct edge sets differ by at least one edge.

**4. Sharp moves and connectivity.** If \(r=0\), transpose one vertex from each of two \(q\)-blocks. This exchanges exactly \(2(q-1)\) edges. Such transpositions generate all labelled equipartitions of the given block sizes, hence the threshold graph is connected. If \(r>0\), move one vertex from a \((q+1)\)-block to a \(q\)-block. The sizes exchange roles and precisely \(q\) edges are replaced. These moves also connect all balanced partitions. To see this, temporarily label the parts, and note that all balanced assignments with the same labelled size pattern are related by element transpositions. A transposition between a large part and a small part is achieved by two allowed moves (move the first element from large to small, then move the second back). Between two large parts, use a small part as a buffer for three moves; between two small parts, use a large part as a buffer for four moves. A different assignment of the labels to the large/small sizes can be reached by a single allowed move from a large part to a small part. Thus all labelled balanced assignments, hence all underlying edge sets, are connected. The lower bounds in step 3 show that no exchange graph with smaller batch size has any edges.

**5. Degrees at the first threshold.** At \(r=0,q\ge3\), equality in step 3 requires splitting exactly two blocks, each into sizes \(q-1\) and \(1\); it is precisely a cross-block transposition, giving \(q^2\binom s2\) distinct neighbors. At \(r=0,q=2\), the old blocks are pairs in a perfect matching; choosing two old pairs allows exactly two replacement pairings, so the degree is \(2\binom s2\). At \(r>0,q\ge3\), only one large block can split at distance \(q\); the unique permitted move transfers one of its \(q+1\) vertices to one of the \(f\) small blocks, giving \((q+1)rf\) neighbors. At \(r>0,q=2\), these \(3rf\) moves remain, but two old size-two blocks may also be re-paired in two ways, giving \(2\binom f2\) additional neighbors. Finally, for \(q=1\), an extremizer's nonedge set is a matching with \(r\) edges and \(f\) unmatched vertices. To replace exactly one nonedge, choose one of the \(r\) matched pairs, then a new pair from its two endpoints and the unmatched vertices, other than the original pair: there are \(2f+\binom f2\) choices. The listed cases exhaust all possible equality patterns in the bound from step 3, proving the degrees.

## Verification

Two independent executable tests are supplied. `verify_turan.py` enumerates balanced unlabeled partitions for \(4\le n\le10\), \(2\le s\le\min(5,n-1)\). It constructs the full extremal edge-set masks and explicitly checks the minimum pair distance, connectivity at the predicted threshold, and regular degrees. `verify_visibility_turan.py` separately enumerates *all* \(2^{\binom n2}\) root-edge subsets for \(n=4,5,6\), filters those without a \(K_4\), selects the maxima, and checks their exact first-exchange connectivity. Both return success tokens when their assertions pass. They test finite ranges; the theorem for arbitrary \(n,s\) follows from the symbolic argument above.

## Relationship to prior work

Turán's original theorem determines the extremal edge count and uniqueness up to isomorphism; it already implies the balanced multipartite description. Cicerone, Di Stefano, Klavžar and Yero (2024), Theorem 3.2, independently establish that the maximum mutually visible sets of \(L(K_n)\) are exactly these three-partite extremizers. Neither result is newly claimed. Korándi, Roberts and Scott (2021) study an exact Turán *stability* question for nearly extremal graphs; their comparison is to the property of multipartiteness, not to pairwise movement between labelled exact extremizers. The new contribution is the exact edge-replacement metric, first nonzero exchange threshold, connectivity at that same threshold, and its exceptional regular-degree formulas over all \(s\).

## Limitations

The statement concerns exact Turán extremizers on one labelled vertex set and atomic batch exchanges. It does not describe exchanges among near-extremizers, or sequences constrained to remain feasible during the interior of one batch. The visibility interpretation only uses the known equivalence for \(L(K_n)\) and \(s=3\); arbitrary \(s\) are posed as extremal clique-free reconfiguration, not as an unidentified visibility graph. Independent mathematical validation and comprehensive publication-priority clearance have not been performed.

## References

1. S. Cicerone, G. Di Stefano, S. Klavžar, I. G. Yero, *Mutual-visibility problems on graphs of diameter two*, European Journal of Combinatorics **120** (2024), 103995, Theorem 3.2, DOI: 10.1016/j.ejc.2024.103995. First arXiv submission: 2024-01-04. https://arxiv.org/abs/2401.02373
2. D. Korándi, A. Roberts, A. Scott, *Exact stability for Turán's theorem* (2021 preprint), Introduction and Theorem 1.2. https://people.maths.ox.ac.uk/scott/Papers/turanstability.pdf
3. P. Turán, *Egy gráfelméleti szélsőértékfeladatról*, Matematikai és Fizikai Lapok **48** (1941), 436–452 (classical extremal equality theorem, cited as prior art).
