# Minimal forts and the zero forcing polynomial of fully subdivided complete graphs

## Finding

**Theorem.** Let \(n\geq 3\), put \(m=\binom{n}{2}\), and let \(H_n\) be obtained from \(K_n\) by replacing each edge \(uv\) by \(u-e_{uv}-v\), where each \(e_{uv}\) is a new vertex. Denote the original-vertex set by \(O\) and the subdivision-vertex set by \(D\).

The inclusion-minimal forts of \(H_n\) are exactly:

1. \(O\);
2. the \(n\) sets \((O\setminus\{v\})\cup\{e_{uv}:u\in O\setminus\{v\}\}\), one for each \(v\in O\);
3. the sets \(\{e_{uv}:uv\in E(C)\}\) for all simple cycles \(C\) of \(K_n\).

Consequently, a set \(S=U\cup\{e_{uv}:uv\in B\}\), with \(U\subseteq O\) and \(B\subseteq E(K_n)\), is an ordinary zero forcing set if and only if the following three conditions hold: \(U\neq\varnothing\); \(E(K_n)\setminus B\) is a forest; and, when \(U=\{v\}\), at least one edge of \(B\) is incident with \(v\).

The complete cardinality-generating polynomial is
\[
\boxed{\mathcal Z(H_n;z)=z^{m-n+1}\big((1+z)^n-1\big)T_{K_n}(1+z,1)-n z^{m-n+2}},
\]
where \(T_{K_n}\) is the ordinary Tutte polynomial. In particular,
\[
Z(H_n)=m-n+2,\qquad
[z^{m-n+2}]\mathcal Z(H_n;z)=n\big(n^{n-2}-1\big).
\]
The numerical value of \(Z(H_n)\) was established earlier; the claim here is the fort classification, the characterization of every forcing set, the full polynomial and the exact minimum-set multiplicity.

## Assumptions and scope

All graphs are finite, simple and undirected. Each original vertex \(u\) is adjacent only to the subdivision vertices \(e_{uv}\) for \(v\neq u\). Each subdivision vertex \(e_{uv}\) has precisely the two neighbors \(u,v\). A **fort** is a nonempty vertex set \(F\) for which no vertex outside \(F\) has exactly one neighbor in \(F\). Inclusion-minimal means containing no smaller nonempty fort. Under ordinary zero forcing, a blue vertex with exactly one white neighbor can turn that neighbor blue. Write \(\mathcal Z(G;z)=\sum_{S\text{ zero forcing}} z^{|S|}\).

A spanning forest is an acyclic edge subset on all \(n\) original vertices, allowing isolated vertices. The Tutte polynomial convention is
\[
T_G(x,y)=\sum_{A\subseteq E(G)}(x-1)^{r(E)-r(A)}(y-1)^{|A|-r(A)},
\]
where \(r(A)=|V(G)|-c(V(G),A)\). We use \(T_{K_n}(1+z,1)=\sum_{F\text{ spanning forest}}z^{n-1-|E(F)|}\).

## Proof

**1. Characterization of forts.** Any vertex subset is uniquely \(F=A\cup\{e_{uv}:uv\in Q\}\), for \(A\subseteq O\) and \(Q\subseteq E(K_n)\). At a subdivision vertex outside \(F\), exactly one neighbor lies in \(F\) precisely if its underlying edge has exactly one endpoint in \(A\). Thus the fort condition requires \(\delta(A)\subseteq Q\), where \(\delta(A)\) is the edge cut of \(A\). At each original vertex \(v\notin A\), its neighbors in \(F\) correspond to edges of \(Q\) incident with \(v\), so it further requires \(\deg_Q(v)\neq 1\). These two conditions, with nonemptiness, are necessary and sufficient.

If \(A=\varnothing\), the condition says that the nonempty edge set \(Q\) has no degree-one vertices. Such an edge subgraph must contain a simple cycle: otherwise it is a nonempty forest and hence has a degree-one vertex. Conversely, the edge-vertices of any simple cycle form a fort. Hence precisely those cycle-vertex sets are inclusion-minimal among forts with no original vertex.

If \(A=O\), the set \(O\) alone is a fort, and no proper nonempty subset of \(O\) is a fort: every nontrivial cut would require a subdivision vertex. Hence \(O\) is minimal, while adding subdivision vertices makes a nonminimal fort.

Suppose \(\varnothing\subsetneq A\subsetneq O\). For \(2\leq |A|\leq n-2\), \(Q\) contains all edges of the complete bipartite cut, hence contains the four edges of a simple four-cycle. The corresponding subdivision-only cycle fort is properly contained in \(F\), so \(F\) is not minimal. If \(A=\{a\}\), all \(n-1\) edges incident with \(a\) lie in \(Q\). Every other original vertex then has at least one edge of \(Q\); because it cannot have degree one, \(Q\) includes an edge \(uv\) with \(u,v\neq a\). The three edges \(au,av,uv\) yield a subdivision-only triangle fort properly contained in \(F\). Finally, if \(A=O\setminus\{v\}\), the cut is precisely the star \(\delta(\{v\})\), and \((O\setminus\{v\})\cup\{e_{uv}:u\neq v\}\) is a fort. It is minimal: a smaller set with no original vertex cannot contain a cycle within its subset of star edges, while a smaller set with nonempty proper original part \(A'\subsetneq O\setminus\{v\}\) violates the cut condition on an edge from \(A'\) to \((O\setminus\{v\})\setminus A'\). With all \(O\setminus\{v\}\) retained, every star edge is required. This proves the complete classification.

**2. Fort transversals and forcing.** A blue initial set meets every fort if and only if it is zero forcing. Indeed, a fort disjoint from the blue set cannot receive the first force, since every blue vertex has either zero or at least two neighbors inside it. Conversely, if all permissible forces have been performed and white vertices remain, the remaining white set is a fort disjoint from the initial blue set. Since every fort contains a minimal fort, it suffices to meet all minimal forts. Meeting \(O\) means \(U\neq\varnothing\). Meeting all subdivision-only cycle forts means \(B\) meets every cycle of \(K_n\), equivalently \(E(K_n)\setminus B\) is a forest. Meeting the star fort indexed by \(v\) is automatic if \(U\) contains some original vertex other than \(v\); if \(U=\{v\}\), it holds precisely when some edge of \(B\) meets \(v\). Thus the three conditions characterize exactly every forcing set.

**3. Enumeration.** For each spanning forest \(R\subseteq E(K_n)\), choose the subdivision vertices indexed by \(B=E(K_n)\setminus R\). Their weight is \(z^{m-|R|}\). A nonempty original subset \(U\) contributes \((1+z)^n-1\). Over all forests, the only exceptions to the characterization are the \(n\) choices \(U=\{v\}\) and \(R=\delta(\{v\})\), i.e. the complete star on all \(n\) vertices. Each such forbidden initial set has size \(1+(m-(n-1))=m-n+2\). The Tutte expansion for a connected graph at \(y=1\) gives
\[
\sum_{R\text{ forest}}z^{m-|R|}=z^{m-n+1}T_{K_n}(1+z,1).
\]
Multiplying by \((1+z)^n-1\) and subtracting the \(n\) exceptions proves the boxed identity.

**4. Minimum term.** Every forest has at most \(n-1\) edges and every forcing set contains at least one original vertex; consequently its size is at least \(m-n+2\). For minimum size, the unused subdivision edges form a spanning tree and \(U\) is a singleton. Cayley's formula supplies \(n^{n-2}\) spanning trees and there are \(n\) possible singleton originals. Exactly \(n\) pairs consist of a star centered at the selected original and are excluded, giving \(n(n^{n-2}-1)\) minimum sets, strictly positive for \(n\geq3\).

## Verification

A standalone Python verifier (`verify.py`) implements the forcing process directly, independently tests the forest criterion, and checks the complete polynomial for every vertex subset of \(H_3,H_4,H_5\) (respectively \(64,1024,32768\) initial sets). It exhaustively identifies inclusion-minimal forts using the literal fort definition and a proper-subset test for these three orders. At \(n=6\) it also tests 25,000 seeded random initial sets against direct forcing; these finite checks do not establish the arbitrary-order theorem.

The polynomial coefficient vectors, listed as \((\text{exponent},\text{coefficient})\), are
\[
\begin{aligned}
n=3:&\ (2,6),(3,18),(4,15),(5,6),(6,1);\\
n=4:&\ (4,60),(5,156),(6,178),(7,116),(8,45),(9,10),(10,1);\\
n=5:&\ (7,620),(8,1800),(9,2575),(10,2225),(11,1230),(12,445),(13,105),(14,15),(15,1).
\end{aligned}
\]
Run `python verify.py` with Python 3.8 or later. The final line is `VERIFICATION_OK`.

## Relationship to prior work

Cameron, Hogben, Kenter, Mojallal and Schuerger develop forts and their relationship with zero forcing, including fractional formulations. Barrett and collaborators previously determined the minimum zero forcing number for complete subdivision graphs, thereby covering the **minimum numerical value** in this theorem. Boyer and collaborators define and study the zero forcing polynomial for various families. Menon and Singh investigate zero forcing set counts under graph operations and for several structural families. In the inspected material these works do not assert the complete minimal-fort description for \(H_n\), the if-and-only-if forcing-set criterion, or its Tutte-polynomial enumeration. A previously unpublished or unindexed equivalence remains possible, especially through general zero-forcing results for subdivisions or graphic-matroid transversals.

## Limitations

The theorem applies only to the full single-edge subdivision of the simple complete graph and to ordinary zero forcing. It does not classify forts or enumerate forcing sets of arbitrary subdivisions of arbitrary base graphs, does not calculate fractional zero forcing, and makes no independent novelty or priority certification. All proofs are mathematical arguments for all \(n\geq3\); the finite reproducibility checks are supplementary. The minimum zero forcing number is known prior work rather than a newly claimed result.

## References

1. Cameron, Hogben, Kenter, Mojallal and Schuerger, “Forts, (fractional) zero forcing, and Cartesian products of graphs”, arXiv:2310.17904, initial public version 2023-10-27; https://arxiv.org/abs/2310.17904 .
2. Barrett, Butler, Catral, Fallat, Hall, Hogben and Young, “The Maximum Nullity of a Complete Subdivision Graph is Equal to its Zero Forcing Number”, *Electronic Journal of Linear Algebra* **27** (2014); https://journals.uwyo.edu/index.php/ela/article/download/1381/1381/ .
3. Boyer et al., “The zero forcing polynomial of a graph”, arXiv:1801.08910 (2018); https://arxiv.org/abs/1801.08910 .
4. Menon and Singh, “Exploring the Influence of Graph Operations on Zero Forcing Sets”, arXiv:2405.01423 (2024); https://arxiv.org/abs/2405.01423 .
