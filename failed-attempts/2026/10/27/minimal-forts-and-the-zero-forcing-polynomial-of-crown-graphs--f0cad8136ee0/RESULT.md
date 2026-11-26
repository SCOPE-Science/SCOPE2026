# Minimal forts and the zero-forcing polynomial of crown graphs

## Finding
For every integer \(n\ge4\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\), where its labeled bipartition is \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and \(a_i\sim b_j\) precisely when \(i\ne j\). The inclusion-minimal forts are exactly the following three families:

1. All triples of vertices entirely in \(A\).
2. All triples of vertices entirely in \(B\).
3. The matched double-pairs \(\{a_i,a_j,b_i,b_j\}\), for \(1\le i<j\le n\).

Consequently there are exactly \(2\binom n3+\binom n2\) inclusion-minimal forts. A vertex set \(S\) is zero forcing if and only if its omitted indices \(I=\{i:a_i\notin S\}\), \(J=\{j:b_j\notin S\}\) satisfy
\[
|I|\le2,\qquad |J|\le2,\qquad |I\cap J|\le1.
\]
In particular, its complete zero-forcing polynomial (counting all zero-forcing sets by initial cardinality) is
\[
\boxed{\mathcal Z(\operatorname{Cr}_n;z)=z^{2n}+2nz^{2n-1}+n(2n-1)z^{2n-2}+n^2(n-1)z^{2n-3}+\frac{n(n-1)(n-2)(n+1)}4z^{2n-4}.}
\]
Thus \(Z(\operatorname{Cr}_n)=2n-4\), there are \(n(n-1)(n-2)(n+1)/4\) minimum zero-forcing sets, and all such sets are precisely complements of two vertices on each side with at most one matching index repeated.

## Assumptions and scope
All graphs are finite, simple and undirected. A nonempty set \(F\) is a *fort* when every vertex outside it has either zero or at least two neighbors in it. A fort is inclusion-minimal if none of its proper nonempty subsets is a fort. In standard zero forcing, a blue vertex with precisely one white neighbor can color that neighbor blue; a set is zero forcing when some iteration of this rule colors all vertices. The coefficient of \(z^k\) in \(\mathcal Z(G;z)\) counts initially blue zero-forcing sets of cardinality \(k\). We consider integer \(n\ge4\), not arbitrary bipartite graphs with missing edges. The same formula also specializes correctly to \(n=3\), the six-cycle, whose polynomial was known earlier.

## Proof
**Step 1: exact fort criterion.** For any candidate \(F\), write \(P=\{i:a_i\in F\}\) and \(Q=\{j:b_j\in F\}\). Every \(a_i\notin F\) has exactly \(|Q|-\mathbf1_{i\in Q}\) neighbors in \(F\), and every \(b_j\notin F\) has exactly \(|P|-\mathbf1_{j\in P}\). Therefore \(F\) is a fort exactly when these quantities never equal one, respectively for \(i\notin P\) and \(j\notin Q\).

**Step 2: classify minimal forts.** Every triple in one bipartition side is a fort: every vertex outside the triple has either zero, two or three neighbors in it. No nonempty subset of such a triple is a fort because any one- or two-vertex same-side set leaves some opposite-side vertex with exactly one neighbor. Hence every fort containing at least three vertices of one side contains one of the indicated minimal triples.

Now let a nonempty fort have \(|P|,|Q|\le2\). If \(|P|=2\), then for each \(j\in P\setminus Q\), the outside vertex \(b_j\) has exactly one neighbor in \(F\), forbidden. Hence \(P\subseteq Q\), and consequently \(|Q|=2\) with \(P=Q\). The symmetric argument gives the same conclusion if \(|Q|=2\). If \(|P|,|Q|\le1\), choose an index outside \(P\cup Q\) (possible because \(n\ge4\)); when one side contains a single selected vertex, the opposite vertex at this outside index has exactly one neighbor in \(F\), and when both sides are empty \(F\) is forbidden. Thus the only remaining forts are the two-sided matched double-pairs \(P=Q=\{i,j\}\). They are indeed forts by the criterion: an outside vertex has two neighbors in \(F\); every proper nonempty subset is smaller than three on each side and cannot be a fort. This establishes the complete list and its count.

**Step 3: exact zero-forcing criterion.** A set \(S\) is zero forcing exactly when it meets every fort. To prove this equivalence directly, a process that stops with nonempty white set \(F\) has no outside blue vertex with exactly one neighbor in \(F\), hence \(F\) is a fort missed by the initial set. Conversely, if the initial set misses a fort \(F\), no outside vertex can ever force a vertex of \(F\) while all of \(F\) is still white, so the process cannot finish. Since every fort contains a minimal fort, it suffices to meet the three listed families. Missing a same-side triple is equivalent to omitting at least three vertices on that side; missing a matched double-pair is equivalent to omitting two matched index pairs, i.e. \(|I\cap J|\ge2\). Negating these obstructions gives the stated three inequalities.

**Step 4: exact enumeration.** A complement with \(a=|I|\), \(b=|J|\), and \(r=|I\cap J|\) has \(2n-a-b\) blue vertices. For \(0\le a,b\le2\), \(0\le r\le1\), the number of ordered omitted-index pairs is
\[
N_n(a,b,r)=\binom nr\binom{n-r}{a-r}\binom{n-a}{b-r}.
\]
The factors choose common, \(A\)-only, and \(B\)-only indices. Sum over the finite admissible possibilities: for omitted cardinalities \(a+b=0,1,2,3,4\), the counts respectively are
\[
1,\quad 2n,\quad n(2n-1),\quad n^2(n-1),\quad \frac{n(n-1)(n-2)(n+1)}4.
\]
In the final case \(a=b=2\), with overlaps zero or one, the count is \(\binom n2[\binom{n-2}2+2(n-2)]\). The resulting polynomial has positive lowest-degree coefficient for every \(n\ge4\). This proves the minimum, coefficient formula and classification of its sets. \(\square\)

## Verification
The independent direct-definition program `verify.py` enumerates every vertex subset of \(\operatorname{Cr}_n\) for \(3\le n\le7\), computes all forts and their inclusion-minimal elements without relying on the structural criterion, and separately runs the original iterative zero-forcing rule on every initial set. It compares exact sets and each coefficient to the displayed classification and polynomial. All \(21,824\) subsets across these five orders passed; the detailed deterministic output is in `verify_output.txt`. These finite computations test boundary cases, but the quantified infinite theorem follows from the proof above.

## Relationship to prior work
Boyer et al. (2018, arXiv:1801.08910, Section 4 and Proposition 4) determine the zero-forcing polynomial of complete multipartite graphs, including the unmodified complete bipartite graph \(K_{n,n}\), but not the matching-deleted graph \(K_{n,n}-M_n\). The latter has a distinct minimal-fort hypergraph: the same-side smallest forts have size three rather than two, and matched double-pairs add four-vertex minimal forts. Becker et al. (2024, arXiv:2404.05963, Section 4) enumerate minimal forts of complete bipartite graphs and several path-derived and product families, but do not give the crown-graph classification. Cameron et al. (2023, arXiv:2310.17904) provide the general fort-hypergraph context, not this exact family. The six-cycle case \(n=3\) is already covered by the previously published cycle polynomial; the contribution assessed here concerns all \(n\ge4\) and their structural classification.

## Limitations
The theorem uses the standard zero-forcing rule and deletes one complete perfect matching; it does not address arbitrary matching deletions or positive-semidefinite/skew forcing variants. Independent mathematical validation is not supplied. A lack of identified equivalent results in indexed and inspected literature is not a proof of bibliographic novelty; obscure or unindexed prior descriptions remain a possible priority risk.

## References
1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (public 2018-01-26), https://arxiv.org/abs/1801.08910.
2. P. Becker, T. R. Cameron, D. Hanley, B. Ong, J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963v1 (public 2024-04-09), https://arxiv.org/abs/2404.05963.
3. T. R. Cameron et al., *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904v1 (public 2023-10-27), https://arxiv.org/abs/2310.17904.
