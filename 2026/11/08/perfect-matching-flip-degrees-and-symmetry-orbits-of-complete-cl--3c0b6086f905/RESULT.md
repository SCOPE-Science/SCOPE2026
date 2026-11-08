# Perfect-matching flip degrees and symmetry orbits of complete-clique prisms

## Finding
Let \(G_n=K_n\square K_2\), \(n\ge3\), consist of two \(n\)-vertex cliques joined by a fixed perfect matching of corresponding vertices (the *rungs*). A *four-cycle flip* replaces two opposite edges of a perfect matching on any four-cycle with its other two opposite edges; chords of the four-cycle are permitted. Let \(\mathcal F_n\) have all perfect matchings of \(G_n\) as vertices, adjacent by one flip.

For a perfect matching \(M\), let \(k\) be the number of its rungs, write \(2h=n-k\), and let \(A,B\) be the induced perfect matchings of the remaining \(2h\) column labels in the two respective cliques. Each alternating cycle of the two-colored multigraph \(A\cup B\) has length \(2t\), including a doubled common edge when \(t=1\). Let \(\lambda\vdash h\) contain these values \(t\); if \(h=0\), take \(\lambda=\varnothing\). Let \(m_t\) be the multiplicity of \(t\) in \(\lambda\), \(\ell(\lambda)=\sum_t m_t\), and \(z_\lambda=\prod_t t^{m_t}m_t!\). Define \((-1)!!=1\).

**Theorem.** The full automorphism group of \(G_n\) is \(S_n\times C_2\), and its orbits on the perfect matchings are indexed exactly by \((h,\lambda)\) with \(0\le h\le\lfloor n/2\rfloor\) and \(\lambda\vdash h\). The orbit \((h,\lambda)\), where \(k=n-2h\), has cardinality
\[
\binom nk(2h-1)!!\frac{h!\,2^{h-\ell(\lambda)}}{z_\lambda}.
\]
Every vertex in it has degree
\[
d_{h,\lambda}=2h(h-1)+\binom k2+m_1(\lambda).
\]
Consequently the number of symmetry orbits is \(\sum_{h=0}^{\lfloor n/2\rfloor}p(h)\), with \(p(0)=1\), and the complete degree distribution is the sum of the above orbit cardinalities over orbit types of equal degree. In particular, the exact numbers of perfect matchings and edges are
\[
|V(\mathcal F_n)|=\sum_{h=0}^{\lfloor n/2\rfloor}\binom n{2h}\bigl((2h-1)!!\bigr)^2,
\]
\[
|E(\mathcal F_n)|=\sum_{h=0}^{\lfloor n/2\rfloor}\binom n{2h}\bigl((2h-1)!!\bigr)^2\left[h(h-1)+\binom{n-2h}2\right].
\]
Moreover \(\mathcal F_n\) is connected for every \(n\ge3\). This last connectivity fact is contextual, not asserted to be new beyond general switch-chain frameworks; the original claim concerns the explicit orbit-and-degree classification and edge census.

## Assumptions and scope
All graphs are finite, simple, undirected; perfect matchings are unordered sets of undirected edges. A square flip requires all four sides of a four-cycle, not a chordless induced square. The \(S_n\)-action simultaneously permutes column labels in both cliques; \(C_2\) interchanges layers. For \(h=0\), products and partition statistics are defined by their empty values, so the all-rung matching is included. The term \((2h-1)!!\) is the number of one-factors on \(2h\) labeled vertices. No graph of order \(n<3\) is asserted to obey the stated automorphism description.

## Proof
**1. Perfect-matching parametrization.** If one endpoint of a rung is matched vertically, so is the other; let their label set be \(R\). Every other vertex must be matched within its own clique. Thus \(k=|R|\) has the same parity as \(n\), and the matching is uniquely \((R,A,B)\), with \(A,B\) two perfect matchings on the common complement of \(R\). This gives the total vertex formula immediately, since there are \(\binom n{2h}\) complements and \(((2h-1)!!)^2\) ordered pairs \((A,B)\).

**2. Complete symmetry invariants and orbit sizes.** For \(n\ge3\), each horizontal edge belongs to \(n-2\ge1\) triangles, while each rung belongs to no triangle. Thus the rungs are intrinsically characterized as edges lying in no triangle. Any automorphism permutes the rung pairs, and it must carry each layer (a component after deleting rungs) to a layer; consequently it is exactly a simultaneous column permutation, optionally followed by layer exchange. For a fixed rung set, an \(S_{2h}\) relabeling sends every first perfect matching \(A\) to a prescribed reference pairing. The stabilizer of that pairing acts transitively on all second pairings \(B\) with a specified multiset of alternating component lengths: match the alternating cycles componentwise and choose an alternating start and orientation. Hence \(\lambda\) is a complete invariant (layer interchange does not alter it).

To count a prescribed \(\lambda\), first select \(R\) in \(\binom nk\) ways and \(A\) in \((2h-1)!!\) ways. Regard the \(h\) edges of \(A\) as distinguishable blocks. Partition these into unordered groups of \(m_t\) blocks of each size \(t\): \(h!/\prod_t((t!)^{m_t}m_t!)\) possibilities. For any fixed group of \(t\) blocks, there are precisely \(2^{t-1}(t-1)!\) ways to add the \(B\)-edges into a single alternating component: order the \(t\) blocks cyclically and choose endpoint connections, quotienting by reversal; for \(t=1\) this gives exactly the shared \(A\)-edge. Multiplication gives
\[
\frac{h!}{\prod_t((t!)^{m_t}m_t!)}\prod_t\bigl(2^{t-1}(t-1)!\bigr)^{m_t}
=\frac{h!\,2^{h-\ell(\lambda)}}{\prod_t t^{m_t}m_t!}.
\]
This proves the orbit-size formula and, by summing all partitions, the orbit count.

**3. Classification of all flips.** Every four-cycle is either contained in one clique or is the rectangle using exactly two rungs and the two corresponding horizontal edges; there can be no four-cycle crossing layers with another pattern because each vertex has exactly one cross-layer neighbor. In each clique, the \(h\) matched horizontal edges admit, for every unordered pair, two distinct alternative pairings: \(2\binom h2\) moves per layer and \(4\binom h2=2h(h-1)\) in total. A rung rectangle permits a flip from two occupied rungs to two horizontal edges, in exactly \(\binom k2\) ways. In the reverse direction, it permits a flip to two rungs exactly when that horizontal pair is an edge of both \(A\) and \(B\): there are \(m_1(\lambda)\) such shared edges. These three types are disjoint and exhaustive, giving \(d_{h,\lambda}\). In counting global *undirected* flip edges, within-layer moves contribute \(h(h-1)\) per state after division by two. Every rung-changing edge is counted exactly once by its endpoint with more rungs, contributing \(\binom k2\) per state. Summing by \(h\) yields the edge formula.

**4. Connectivity.** First, the graph of perfect matchings of a complete graph under two-edge switches is connected: for any desired pair \(\{a,b\}\) not yet present, the edges currently incident to \(a\) and \(b\) can be replaced by \(\{a,b\}\) and the edge on their former partners, preserving all already-fixed target pairs. This adjusts \(A\) and \(B\) independently whenever \(R\) is fixed. Whenever \(k\ge2\), flip two rungs into parallel horizontal edges to decrease \(k\) by two. Thus every configuration reaches a state with \(k=0\) when \(n\) is even and \(k=1\) when \(n\) is odd. With \(k=0\), the independent clique switches connect every state. With \(k=1\), write \(a\) for the sole rung label and choose any other \(b\) and a third label \(c\). By clique switches, arrange for \(\{b,c\}\) to be matched in *both* layers, then flip that horizontal pair into rungs at \(b,c\), and flip the rungs at \(a,c\) back to horizontal edges. The new sole rung is \(b\). Since \(a,b\) were arbitrary and clique pairings can subsequently be adjusted, all states are connected.

## Verification
Two standalone programs `verify_prism.py` and `verify_formula.py` use different constructions. The first independently builds the \(2n\)-vertex graph and enumerates all perfect matchings from a least-unused-vertex recursion for \(3\le n\le7\); it explicitly generates every legal opposite-edge replacement, all adjacency degrees, the full connected component, and orbit-type counts. The second constructs pairs of clique one-factors directly, classifies their alternating cycles and checks the orbit formulas for \(3\le n\le8\) without constructing the flip graph. Both agree on all overlapping counts. The outputs are supplied as `verification_output.jsonl` and `formula_output.jsonl`. Reproducibility requires only Python 3 standard library. Finite computations corroborate but do not establish the infinite formulas, which follow from the proof above.

## Relationship to prior work
Dyer, Jerrum and Müller studied the switch Markov chain for perfect matchings (arXiv:1501.07725), including conditions for connectivity in a general graph rather than an explicit orbit and degree classification of \(K_n\square K_2\). Dyer and Müller (arXiv:1705.05790) consider perfect-matching counting and switches in broader graph classes. Bonamy and collaborators (arXiv:1904.06184) study perfect-matching reconfiguration and reachability more generally. Standard two-one-factor alternating cycle structure underpins the present orbit indexing and is not claimed as original on its own. The asserted addition is the *complete simultaneous* classification of the perfect-matching flip degree and \(S_n\times C_2\) orbit size, including the characteristic shared-edge term \(m_1(\lambda)\), and the closed full-state edge count. Unlike a study of one-factorizations, the state is one single perfect matching of the two-layer graph, not a decomposition of all graph edges into many one-factors.

## Limitations
This concerns only full perfect matchings of \(K_n\square K_2\) under all four-cycle switches, including cycles with chords. No mixing-time, diameter, or rapidly mixing claim is made. The orbit formulas use conventional one-factor pair classification, so novelty is restricted to their combination with rung-changing flips and the resulting exact graph-specific degree, multiplicity, and edge counts. Searches of accessible mathematical records and research do not establish absolute historical priority; a differently named or unindexed equivalent enumeration remains possible. No independent scholarly review has been performed.

## References
1. M. Dyer, M. Jerrum and H. Müller, *On the switch Markov chain for perfect matchings*, arXiv:1501.07725, first posted 2015-01-30.
2. M. Dyer and H. Müller, *Counting perfect matchings and the switch chain*, arXiv:1705.05790, first posted 2017.
3. M. Bonamy and collaborators, *The Perfect Matching Reconfiguration Problem*, arXiv:1904.06184, first posted 2019.
