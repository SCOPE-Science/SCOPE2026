# Signed matching holonomy and color-refinement orbits in tournaments

## Finding
Let \(T=(V,\to)\) be a finite nonempty tournament, interpreted as a structure with one irreflexive binary arc relation and equality. Start directed one-dimensional color refinement with one vertex color, refining each vertex by its old color and the numbers of incoming and outgoing neighbors in every old color. Let \(\mathcal P\) be its stable partition. Suppose every block of \(\mathcal P\) has size at most three.

Every three-vertex stable block is a directed triangle. Choose for each such block \(P\) a cyclic listing \((p_0,p_1,p_2)\) with \(p_0\to p_1\to p_2\to p_0\). For distinct three-vertex blocks \(P,Q\), let \(k(P,Q)\) be the common number of outgoing arcs from any vertex of \(P\) to \(Q\). The value belongs to \(\{0,1,2,3\}\). Make a graph \(\Gamma(T)\) on these three-vertex blocks by joining \(P,Q\) precisely when \(k(P,Q)\) is one or two. In those cases the minority arcs form a perfect matching between the blocks: arcs from \(P\) to \(Q\) when \(k=1\), or arcs from \(Q\) to \(P\) when \(k=2\). This matching determines a bijection \(\pi_{PQ}:P\to Q\). Label its edge by the sign \(\sigma(P,Q)\in\{+1,-1\}\) of the permutation induced by \(\pi_{PQ}\) in the chosen cyclic listings. A different allowed cyclic listing changes the permutation by even rotations, so the sign is intrinsic.

Call a connected component of the signed graph **balanced** if the product of edge signs on every cycle is \(+1\); isolated vertices and tree components count as balanced. Let \(b(T)\) be the number of balanced connected components of \(\Gamma(T)\), including isolated vertices.

**Theorem (complete small-cell orbit criterion).** Under the stated size hypothesis,
\[
\operatorname{Aut}(T)\cong (\mathbb Z/3\mathbb Z)^{b(T)}.
\]
Every singleton stable block is an automorphism orbit. A three-vertex stable block is one orbit if its vertex of \(\Gamma(T)\) belongs to a balanced component; otherwise its three elements form three separate singleton orbits. Consequently **the stable directed color partition equals the automorphism-orbit partition if and only if every component of \(\Gamma(T)\) is balanced.**

The criterion has a sharp boundary: all tournaments of order at most eight satisfying the small-cell hypothesis are refinable, but there is a rigid nonrefinable nine-vertex tournament satisfying it. Such rigid nonrefinable tournaments exist at every order at least nine by adjoining successive dominating vertices.

## Assumptions and scope
A tournament is a finite simple complete orientation: for distinct \(x,y\), exactly one of \(x\to y\) and \(y\to x\) holds, and no loop holds. Refinement uses the initial uniform coloring and records multiplicities of both incoming and outgoing arc colors. The theorem concerns tournaments for which its **actual stable** color classes all have cardinality at most three; it does not purport to classify tournaments with larger stable classes.

The signed graph is defined using only distinct blocks of size three. An edge's sign depends on the induced directed triangles' orientations, not on arbitrary choices of first vertices. Here \(\operatorname{Aut}(T)\) is the full orientation-preserving automorphism group, with no vertex colors additionally fixed: every automorphism already preserves the stable colors intrinsically.

## Proof
**1. Stable block structure.** For a stable block \(P\) of size three, each of its vertices has the same number \(d\) of outgoing neighbors in \(P\). Since its induced tournament has three arcs, \(3d=3\), so \(d=1\). Thus \(P\) induces a directed three-cycle, whose automorphism group is cyclic of order three. A stable block of size two cannot exist, as its induced tournament has one arc and would require equal integral outdegrees at both vertices. Between a three-vertex block and a singleton block, stability forces all three arcs to have the same direction. In particular, these connections impose no restriction on rotating the directed triangle.

**2. Inter-block matching.** Let \(P,Q\) have size three. Stability gives \(k\) outgoing neighbors in \(Q\) for each vertex of \(P\), and a constant outgoing number \(3-k\) from each vertex of \(Q\) to \(P\), by counting the total arcs between the blocks in both directions. The three-by-three \(P\)-to-\(Q\) adjacency matrix consequently has every row sum and every column sum equal to \(k\). For \(k=0,3\) it is uniform. For \(k=1\) it is a permutation matrix; for \(k=2\) its complement is a permutation matrix. Thus all nonuniform inter-block information is the matching \(\pi_{PQ}\).

**3. Compatible rotations.** Each automorphism fixes each stable block setwise. On each three-vertex block \(P\), it must be rotation by an exponent \(t_P\in\mathbb Z/3\mathbb Z\). When \(P,Q\) are joined in \(\Gamma(T)\), preservation of their matching is equivalent to
\[
\pi_{PQ}\,r_P^{t_P}=r_Q^{t_Q}\,\pi_{PQ},
\quad\text{or equivalently}\quad
 t_Q=\sigma(P,Q)t_P\pmod 3.
\]
Indeed, a bijection between oriented triples conjugates the chosen positive three-cycle to either the positive or inverse three-cycle according to the bijection's parity. Uniform inter-block connections and all singleton connections give no further constraints. Conversely, any compatible system of rotations preserves every arc, hence is an automorphism.

**4. Signed holonomy.** In each connected component, an exponent at one vertex determines all exponents by transporting along paths and multiplying edge signs. The transport is path independent for arbitrary initial exponent exactly when all cycle-sign products are positive. A negative cycle forces \(t=-t\pmod3\), hence \(t=0\), throughout its connected component. Consequently each balanced component gives one independent cyclic factor of order three and each unbalanced component gives none. This proves the group decomposition. A nonzero component rotation moves all three vertices in every member block, so balanced blocks are individual three-element orbits; unbalanced blocks are pointwise fixed. Singletons are fixed. This proves the orbit criterion.

**5. Sharp boundary and witness.** A simple signed graph with fewer than three vertices cannot have a negative cycle. Thus an unbalanced \(\Gamma(T)\) requires at least three blocks of size three, or at least nine original vertices. To attain nine, form directed triangles \(A_i,B_i,C_i\), with \(i\in\{0,1,2\}\) interpreted cyclically. Between the triangles, let
\[
 A_i\to B_j\iff j=i,\qquad B_i\to C_j\iff j=i,\qquad A_i\to C_j\iff j=\tau(i),
\]
where \(\tau\) interchanges zero and one and fixes two; every opposite cross-arc points the other way. Each \(A_i\) has outdegree three, each \(B_i\) outdegree four, and each \(C_i\) outdegree five. These degree classes form a stable partition: inside each class every vertex has one outgoing neighbor, and each vertex has the same outgoing count to each other class. Hence the actual stable blocks are exactly \(A,B,C\). The matching triangle has signs \(+1,+1,-1\), so it is unbalanced. The theorem makes the entire automorphism group trivial although the stable partition consists of three blocks of size three. Adjoining any number of new vertices in order, each dominating every earlier vertex, preserves the old stable blocks, makes each new vertex a singleton stable block, and leaves the tournament rigid and nonrefinable. This proves the claimed sharpness and infinite tail.

## Verification
The self-contained standard-library program `verify.py` tests all \(14^3=2744\) ways of connecting three named directed triangles by blockwise biregular arc patterns. Of these, \(2310\) have stable colors of size at most three; the signed criterion predicts \(1662\) balanced and \(648\) unbalanced instances. For each eligible instance the program independently enumerates all feasible within-block directed-triangle rotations, tests each for arc preservation, calculates actual automorphism orbits, and compares the full partition and group order with the theorem. It also checks the explicit nine-vertex witness, a four-triangle mixed-component example, and rigid dominating-vertex extensions through order thirteen. Its recorded output ends in `VERIFY_OK`.

The exhaustive finite test family is **not** a proof for all tournaments. The general result is established by Steps 1–4; the tests corroborate the nonstandard sign bookkeeping and the boundary examples. The nine-vertex witness can additionally be checked directly from its three block outdegrees and matching permutations.

## Relationship to prior work
Arvind, Köbler, Rattan and Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, introduced and studied refinability for undirected graphs and its relation to counting logic. Kiefer, Schweitzer and Selman, *Graphs Identified by Logics with Counting*, studied \(C^2\)-identifiability of general relational structures, including directed edge colors and directed triangles. The theorem here gives an **exact automorphism-group and orbit-partition criterion** within the separate class of tournaments with small stable cells; it is not a restatement of an identifiability criterion. In particular, the negative signed-cycle obstruction concerns automorphisms inside a given structure, not merely the existence of an equivalent nonisomorphic structure.

## Limitations
The theorem requires every stable color class to have size at most three and uses a single uncolored complete oriented graph relation. It does not classify larger stable cells, undirected graphs, or arbitrary directed graphs. The nine-vertex cutoff is sharp within the stated small-cell class, not a claimed minimum for arbitrary forms of nonrefinability in tournaments. The historic priority of the signed-graph criterion is based on the inspected sources and searches, not an exhaustive proof of global novelty. The proof and executable checks have not been independently audited.

## References
1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, first arXiv posting 2015-02-04, https://arxiv.org/abs/1502.01255 .
2. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, first arXiv posting 2015-03-30, https://arxiv.org/abs/1503.08792 .
