# Universal–isolated peeling classifies two-variable theories of finite graphs

## Finding

Let \(G\) and \(H\) be any **nonempty finite simple undirected graphs**, in the language consisting only of adjacency and equality. Remove all isolated vertices of the current induced graph, if any; otherwise remove all universal vertices, if any; repeat until the graph is empty or has neither an isolated nor a universal vertex. Record the successive block types \(I\) or \(U\) and each block cardinality truncated to \(2\). If a nonempty induced remainder with neither kind of vertex remains, append a terminal symbol \(C\). Treat a one-vertex graph separately as the signature \(S\). Denote the resulting finite word by \(\sigma(G)\).

**Classification.** For every pair \(G,H\) as above,
\[
G\equiv_{\mathrm{FO}^{2}}H\quad\Longleftrightarrow\quad\sigma(G)=\sigma(H).
\]
The equivalence is for **all** counting-free first-order sentences with at most two reusable variables, with no quantifier-rank bound. Every nonempty graph with no isolated or universal vertices has signature \(C\); different such graphs are therefore indistinguishable in this logic.

**Minimum-size spectrum.** Let \(r(n)\) count the distinct two-variable theories of nonempty finite simple graphs whose smallest finite graph representative has exactly \(n\) vertices. Then
\[
R(z)=\sum_{n\ge1}r(n)z^n
=z+\frac{2z^2+z^4(1+z+z^2)}{1-z-z^2}.
\]
For orders \(1\) through \(12\) the coefficients are \(1,2,2,5,8,14,22,36,58,94,152,246\). There are countably infinitely many such theories. The canonical smallest-size *chosen representative* of any signature is obtained by keeping one or two vertices in each peeled block, and, when the terminal symbol \(C\) occurs, choosing the four-vertex induced path as a representative of the core. The smallest representative need not be unique up to isomorphism.

## Assumptions and scope

All graphs are finite, nonempty, loopless, undirected, and have no colors, constants, counting operators, or auxiliary relations. A vertex is isolated in an induced graph if it has no distinct neighbor there, and universal if it is adjacent to every other vertex there. For residual graphs of size at least two, these categories are disjoint. When the residual is a singleton, the entire graph must have been a singleton: any preceding peeled block would contain that final vertex. The two-valued block-size record distinguishes size \(1\) from size at least \(2\); consecutive peeled block signs necessarily alternate. A nonempty residual core with neither isolates nor universals has at least four vertices.

## Proof

**Definability of each layer.** Use only the two variable names \(x\) and \(y\). Set \(D_0(x):=(x=x)\). Given the unary residual formula \(D_j(x)\), let
\[
\begin{aligned}
I_j(x)&:=D_j(x)\wedge\forall y\,[D_j(y)\to (y=x\lor\neg E(x,y))],\\
U_j(x)&:=D_j(x)\wedge\forall y\,[D_j(y)\to (y=x\lor E(x,y))],\\
D_{j+1}(x)&:=D_j(x)\wedge\neg I_j(x)\wedge\neg U_j(x).
\end{aligned}
\]
The formulas on the right are expanded with capture-avoiding substitution; their free variable is the displayed one, and they use only the names \(x,y\). Before termination, exactly one of \(I_j\) and \(U_j\) is nonempty, and it defines the peeled block. The sentence asserting existence of such a block uses \(\exists x\). The sentence asserting at least two vertices in it is \(\exists x\exists y\,[x\ne y\wedge L_j(x)\wedge L_j(y)]\), where \(L_j\) is the applicable layer formula. Also \(\exists x\,D_j(x)\) detects a remaining core; in the terminal case \(\forall x\,[D_j(x)\to (\neg I_j(x)\wedge\neg U_j(x))]\) checks that the remainder is a core. One-variable and two-variable sentences distinguish the singleton case. Consequently different finite peeling signatures admit some separating two-variable sentence.

**Permanent game invariant.** Suppose signatures agree. With up to two pebbles, Duplicator matches each occupied vertex to the *corresponding signed block* or to the terminal core, preserving equality whenever two pebbles occupy the same vertex. If both occupied pebbles are in one block, adjacency is constant: always absent for \(I\) and present between distinct vertices for \(U\). Its recorded truncated size guarantees a distinct response when required. Between different peeled blocks, adjacency is determined by the *outer* block: present for \(U\), absent for \(I\); the same holds between a peeled block and the core. When both pebbles are in the core, adjacency or nonadjacency can always be realized: every core vertex has at least one neighbor and one distinct nonneighbor, since it is neither isolated nor universal. When the target location is the core but the other pebble is outside, the relation is fixed by the outer shell and any core vertex may be used. All atomic equality and adjacency facts are thus preserved after every pebble move. This gives Duplicator a winning strategy for games of arbitrary finite length, and in fact a permanent strategy. The ordinary two-pebble Ehrenfeucht–Fraïssé characterization proves the stated equivalence.

**Realization and minimum order.** An unpeeled core can be chosen as the induced path on four vertices, which has neither isolated nor universal vertices and is smallest possible. Working outward, adjoin a block of \(1\) or \(2\) vertices, as recorded, making each newly added vertex isolated or universal. For a signature without a core and not \(S\), the innermost block must contain at least \(2\) vertices; all other blocks have recorded sizes \(1\) or \(2\). These constructions realize every valid signature and achieve its minimum possible number of vertices.

**Enumeration.** Write \(A(z)=z+z^2\). The singleton contributes \(z\). For signatures with no core, choose one of two terminal signs, give the innermost block size \(2\), and prepend any number of alternating blocks each contributing \(A(z)\); the contribution is \(2z^2/(1-A(z))\). For signatures ending in a core, the empty block sequence contributes \(z^4\); nonempty sequences have two possible outer signs, with each block contributing \(A(z)\), giving \(z^4[1+2A(z)/(1-A(z))]\). Adding these contributions and simplifying proves the rational formula. Every coefficient is finite and block lengths are unbounded, proving countable infinitude.

## Verification

The standalone `verification/verify.py` uses the NetworkX graph atlas containing all \(1253\) unlabeled finite simple graphs on at most seven vertices (including the empty graph, which is excluded from the theorem). It independently constructs all legal zero-, one-, and two-pebble states and computes the greatest stable atomic-preserving back-and-forth refinement. It examines \(76046\) pebble states, stabilizes after six refinements, and obtains \(55\) equivalence classes **including the empty graph**. Those classes match precisely the \(55\) signatures from the atlas, with zero mismatches. For nonempty graph orders one through seven, the empirically obtained minimum-size spectrum is \(1,2,2,5,8,14,22\), agreeing with the rational generating function. `verification/output.txt` records the deterministic output. Run with Python 3 and NetworkX 3 using `python verification/verify.py`. These finite checks are corroboration only; the unrestricted theorem rests on the proof above.

## Relationship to prior work

The two-variable pebble-game characterization is classical and is explained in Pikhurko–Verbitsky's survey of graph logical complexity. The survey also observes the much narrower phenomenon that graphs of the same order without isolated or universal vertices resist counting-free one-dimensional color refinement; that observation does not provide the complete recursive shell signature or minimum-representative enumerator. Grädel–Kolaitis–Vardi and Grädel–Otto investigate general two-variable model theory and satisfiability, rather than an explicitly recovered all-finite-simple-graph shell classification in the materials accessible for this comparison. Classical threshold-graph decomposition covers only the special case of signatures without a terminal core. The present theorem is stated for **all** finite simple graphs, including those with arbitrary terminal cores; no novelty is asserted for the isolated special case of threshold graphs or for the known two-pebble method itself.

## Limitations

The classification is only for counting-free \(\mathrm{FO}^{2}\) over a single irreflexive symmetric adjacency relation, and for finite nonempty graphs. It is not a classification in counting logic, in \(\mathrm{FO}^{3}\), for colored/directed graphs, or for graphs equipped with an order. The canonical chosen representative is minimal in size but need not be the unique minimal graph. General results about two-variable types or color refinement may imply this normal form implicitly, and the full text of Grädel–Otto (1999) was not obtained. Historical novelty therefore remains subject to independent expert bibliographic scrutiny; the checks performed do not prove uniqueness or priority.

## References

1. O. Pikhurko and O. Verbitsky, *Logical Complexity of Graphs: a Survey*, arXiv:1003.4865 (first posted 2010-03-25), https://arxiv.org/abs/1003.4865.
2. E. Grädel, P. G. Kolaitis and M. Y. Vardi, *On the Decision Problem for Two-Variable First-Order Logic*, Bulletin of Symbolic Logic **3** (1997), 53–69, doi:10.2307/421196.
3. E. Grädel and M. Otto, *On Logics with Two Variables*, Theoretical Computer Science **224** (1999), 73–113, doi:10.1016/S0304-3975(98)00308-9. Full paper not inspected.
4. V. Chvátal and P. L. Hammer, *Aggregation of Inequalities in Integer Programming* (1977), for the classical threshold-graph construction; cited only as special-case background.
