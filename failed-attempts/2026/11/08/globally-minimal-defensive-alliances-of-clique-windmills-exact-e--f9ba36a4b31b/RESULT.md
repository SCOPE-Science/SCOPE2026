# Globally minimal defensive alliances of clique windmills: exact enumeration and a parity cutoff

## Finding

Let \(r\ge 2\) and let \(m_1,\ldots,m_r\ge1\) be integers. Form the clique windmill \(W=K_1\vee\bigl(\bigsqcup_{i=1}^{r}K_{m_i}\bigr)\): one hub \(c\) adjacent to every vertex in disjoint labelled clique petals \(P_i\), with \(|P_i|=m_i\). Put \(N=\sum_i m_i\), \(b_i=\lfloor m_i/2\rfloor\), and \(q=|\{i:m_i\text{ is odd}\}|\).

A nonempty vertex set \(S\) is a *defensive alliance* when, for every \(v\in S\), \(|N(v)\cap S|+1\ge|N(v)\setminus S|\). It is *globally minimal* if no nonempty proper subset is a defensive alliance. This is inclusion minimality, not the separate condition that the alliance dominates the graph.

**Classification.** Every globally minimal defensive alliance is exactly one of the following:

1. A set of \(b_i+1\) vertices within one petal \(P_i\), for one \(i\in\{1,\ldots,r\}\).
2. When \(q\le1\), the hub together with exactly \(b_i\) vertices of *every* petal \(P_i\). This second type does not occur when \(q\ge2\).

In particular, the complete cardinality polynomial is
\[
\mathcal A_W(z)=\sum_{i=1}^{r}\binom{m_i}{b_i+1}z^{b_i+1}
+\mathbf1_{\{q\le1\}}
\left(\prod_{i=1}^{r}\binom{m_i}{b_i}\right)z^{\lfloor N/2\rfloor+1}.
\]
The coefficient at \(z^k\) is the number of globally minimal defensive alliances with exactly \(k\) vertices. Coincident powers have their contributions added.

For the friendship graph \(F_r=K_1\vee rK_2\), \(r\ge2\), this specializes to
\[
\mathcal A_{F_r}(z)=r z^2+2^r z^{r+1}.
\]
Thus, for every \(r\ge3\), its globally minimal alliance cardinalities are exactly \(2\) and \(r+1\), omitting all \(r-2\) intermediate cardinalities \(3,4,\ldots,r\). The omitted interval grows without bound.

## Assumptions and scope

Graphs are finite, simple, undirected, with vertex labels distinguishing subsets. Clique sizes may differ and may equal one. The number of petals is at least two. Minimality means *global/inclusion* minimality among nonempty defensive alliances, not minimum size, not local deletion-minimality, and not a *global defensive alliance* (which additionally dominates). No hypothesis of uniform petal sizes or absence of leaves is imposed.

## Proof

Write \(k_i=|S\cap P_i|\) and \(K=\sum_i k_i\); let \(h=1\) when \(c\in S\) and \(h=0\) otherwise. An outer vertex of \(P_i\) has total degree \(m_i\). If selected, it has \(k_i-1+h\) selected neighbors, so its defensive inequality is equivalent to
\[
2(k_i-1+h)+1\ge m_i
\quad\Longleftrightarrow\quad k_i\ge b_i+1-h.
\]
If the hub is selected, it has total degree \(N\) and \(K\) selected neighbors. Its defensive inequality is
\[
2K+1\ge N
\quad\Longleftrightarrow\quad K\ge\lfloor N/2\rfloor.
\]
These conditions characterize all alliances in \(W\).

**Case 1: \(c\notin S\).** In every occupied petal, \(k_i\ge b_i+1\), and the vertices of that petal alone constitute an alliance. Thus global minimality forces exactly one occupied petal, and its occupancy must equal \(b_i+1\). Conversely, each such choice satisfies the inequalities, and every nonempty strict subset has fewer than \(b_i+1\) vertices in that petal, so is not an alliance.

**Case 2: \(c\in S\).** If \(k_i\ge b_i+1\) for any \(i\), then any \(b_i+1\) selected vertices in that petal form a nonempty defensive alliance strictly contained in \(S\). Therefore a globally minimal \(S\) must have \(k_i\le b_i\) for all \(i\). But every occupied petal must have \(k_i\ge b_i\), by the selected outer-vertex condition. Hence \(k_i\in\{0,b_i\}\), with singleton petals necessarily unoccupied.

Let \(q\) be the number of odd \(m_i\). We have
\[
K\le\sum_i b_i=(N-q)/2,
\qquad
K\ge\lfloor N/2\rfloor=(N-(q\bmod2))/2.
\]
This is possible only for \(q\le1\). When \(q\le1\), equality must hold throughout, so \(k_i=b_i\) in every petal. These choices satisfy all defensive inequalities: every selected outer vertex meets its threshold and the hub is exactly at its threshold. Any proper subset containing the hub has strictly fewer than \(\lfloor N/2\rfloor\) outer vertices and fails the hub inequality. Any nonempty proper subset not containing the hub has at most \(b_i\) vertices in each petal and therefore fails every selected outer vertex's inequality. Thus every such set is globally minimal. This proves necessity and sufficiency.

Counting choices gives \(\binom{m_i}{b_i+1}\) sets of the first type for petal \(i\), and, when \(q\le1\), \(\prod_i\binom{m_i}{b_i}\) of the second type. The first type avoids the hub and the second includes it, so no double-counting occurs. The indicated polynomial follows.

For \(m_i=2\) for all \(i\), we have \(b_i=1\), \(q=0\), \(N=2r\), and \(\binom21=2\), \(\binom22=1\). The friendship formula and missing-cardinality interval follow directly.

## Verification

The self-contained program `verify_alliance.py` independently constructs the original adjacency relations, tests the defensive inequality for every nonempty vertex subset, and tests global minimality against **every** nonempty proper subset, not merely all single-vertex deletions. It compares full coefficient dictionaries with the formula for all \(495\) ordered positive petal profiles with \(2\), \(3\), or \(4\) petals, each petal of size at most \(5\), and total petal size at most \(12\).

Command: `python3 verify_alliance.py`.

Observed output:

`VERIFY_OK profiles=495 examined_subsets=1462825 alliances=501626 globally_minimal=11226 local_not_global=127877 all_polynomials=PASS friendship_gaps=PASS`

The program also checks the two-term friendship polynomial for petal counts from \(2\) through \(29\), and verifies that three locally minimal alliances of \(K_1\vee(K_1\sqcup K_3)\) are not globally minimal. These finite checks do not prove the formula for unrestricted sizes; the proof above does.

## Relationship to prior work

Feng, Fernau and Mann, *Enumerating Minimal Defensive Alliances*, arXiv:2312.11963 (first posted December 19, 2023), distinguish locally from globally minimal defensive alliances and give general enumeration results. Their discussed special families, including trees and complete bipartite graphs, do not supply the clique-windmill cardinality formula. Gaikwad and Maity, *Globally Minimal Defensive Alliances: A Parameterized Perspective*, arXiv:2202.02010 (February 4, 2022), study the optimization/parameterized problem, including neighborhood diversity; the accessible material gives no exact polynomial for this family. Ibrahim, *Defensive alliance polynomial*, arXiv:1811.10089 (first posted November 25, 2018), counts connected induced subsets by size and defensive surplus, and identifies friendship graphs from their singleton coefficients; that polynomial and its friendship-graph characterization do not classify inclusion-minimal alliances. The precise globally minimal classification and sharp hub-parity cutoff above are the claims advanced here.

## Limitations

The finding concerns only the one-hub clique-windmill family and global/inclusion minimality; it does not describe all locally minimal alliances. Indeed, the two notions differ even in \(K_1\vee(K_1\sqcup K_3)\), where the hub, the singleton leaf, and one vertex of the \(3\)-clique form a locally minimal but not globally minimal defensive alliance (the leaf alone is an alliance). No efficient general-graph enumeration algorithm follows from this formula. Finite verification does not replace the proof. Publication priority is provisional: the full text of one relevant optimization paper was not accessible, and unindexed equivalent results cannot be excluded.

## References

1. Zhidan Feng, Henning Fernau, Kevin Mann, *Enumerating Minimal Defensive Alliances*, arXiv:2312.11963, first public 2023-12-19. https://arxiv.org/pdf/2312.11963
2. Ajinkya Gaikwad, Soumen Maity, *Globally Minimal Defensive Alliances: A Parameterized Perspective*, arXiv:2202.02010, first public 2022-02-04. https://arxiv.org/abs/2202.02010
3. Hany Ibrahim, *Defensive alliance polynomial*, arXiv:1811.10089, first public 2018-11-25. https://arxiv.org/pdf/1811.10089
