# A skew-forcing lift through independent-fibre blowups and a sparse vertex-transitive exponential family

## Finding

Let \(G\) be any finite simple graph with \(n\ge1\) vertices and let \(m\ge2\). Form \(B_m(G)=G[\overline{K_m}]\), replacing every base vertex by an independent fibre of size \(m\) and every base edge by all \(m^2\) edges between the corresponding fibres. Ordinary zero forcing on \(B_m(G)\) is an exact lift of **skew** zero forcing on \(G\), including the entire collection of inclusion-minimal initial sets.

For a set \(S\subseteq V(B_m(G))\), write \(F(S)\) for the base vertices whose entire fibres are in \(S\). Then

\[
S\text{ ordinarily zero forces }B_m(G)
\quad\Longleftrightarrow\quad
\left(\forall v\in V(G),\ |S\cap(\{v\}\times[m])|\ge m-1\right)
\text{ and }F(S)\text{ skew zero forces }G.
\]

When the displayed fibre condition holds, \(S\) is inclusion-minimal ordinary zero forcing exactly when \(F(S)\) is inclusion-minimal skew zero forcing. If \(\mathcal Z_G(z)\) counts all ordinary zero-forcing initial sets by size, \(\mathcal M_G(z)\) counts inclusion-minimal such sets, and superscript \(-\) denotes the corresponding skew-rule polynomials, the exact substitution identities are

\[
\mathcal Z_{B_m(G)}(z)=(mz^{m-1})^n\mathcal Z^-_G(z/m),\qquad
\mathcal M_{B_m(G)}(z)=(mz^{m-1})^n\mathcal M^-_G(z/m).
\]

In particular, \(Z(B_m(G))=n(m-1)+Z^-(G)\), and \(B_m(G)\) has all its inclusion-minimal ordinary forcing sets of minimum size if and only if all inclusion-minimal skew forcing sets of \(G\) have minimum size.

For every \(n\ge3\), putting \(X_{n,m}=C_n[\overline{K_m}]\), the complete ordinary zero-forcing polynomial is

\[
\mathcal Z_{X_{n,m}}(z)=
\begin{cases}
(z^m+mz^{m-1})^n-(mz^{m-1})^n,&n\text{ odd},\\
\big[(z^m+mz^{m-1})^{n/2}-(mz^{m-1})^{n/2}\big]^2,&n\text{ even}.
\end{cases}
\]

Every inclusion-minimal forcing set is minimum. The minimum size and number of minimum labelled sets are

\[
Z(X_{n,m})=n(m-1)+\begin{cases}1,&n\text{ odd},\\2,&n\text{ even},\end{cases}
\quad
N_{\min}(X_{n,m})=\begin{cases}
nm^{n-1},&n\text{ odd},\\
(n/2)^2m^{n-2},&n\text{ even}.
\end{cases}
\]

**Sparse vertex-transitive consequence.** For \(n\ge5\), \(X_{n,2}\) is a connected, triangle-free, 4-regular vertex-transitive graph on \(2n\) vertices with precisely \(n2^{n-1}\) inclusion-minimal zero-forcing sets when \(n\) is odd, and \((n/2)^2 2^{n-2}\) when \(n\) is even. Thus a bounded-degree connected vertex-transitive family has exponentially many inclusion-minimal zero-forcing sets, answering the existence question raised by Brimkov and Carlson (2022).

## Assumptions and scope

All graphs are finite, simple, undirected and labelled; disconnected bases and isolated vertices are permitted. The ordinary color-change rule allows a **blue** vertex with exactly one white neighbor to force it blue. The skew rule permits a vertex of **either color** with exactly one white neighbor to force that neighbor blue. Each force changes one white vertex blue, and an initial set forces a graph if some finite legal sequence makes every vertex blue. The cycles considered have \(n\ge3\), and all fibre sizes satisfy \(m\ge2\). An inclusion-minimal forcing set admits no proper forcing subset; a minimum forcing set has smallest cardinality. The polynomials count distinct labelled subsets, not isomorphism classes.

## Proof

**1. A false-twin obstruction.** Distinct vertices of one fibre are nonadjacent with identical open neighborhoods. If two vertices of a fibre are initially white, neither can ever become blue: every neighbor of either one is also a neighbor of the other and therefore cannot have exactly one white neighbor while both remain white. The pair is a fort. Hence every ordinary zero-forcing initial set must leave at most one white vertex in each fibre.

**2. Exact simulation of skew forcing.** Assume at most one white vertex per fibre. Because \(m\ge2\), each fibre has a blue vertex at every stage. Write \(W\subseteq V(G)\) for base vertices with a white representative in their fibre. For any blue vertex in the fibre above \(u\), the number of its white neighbors is **exactly** \(|N_G(u)\cap W|\). Therefore a legal ordinary force from the fibre over \(u\) to the unique white vertex over \(v\) exists exactly when \(v\in W\) is the unique member of \(N_G(u)\cap W\). This is the skew color-change rule on the base, whether or not \(u\in W\). Each force reduces \(W\) by the same base vertex. The full fibres initially form \(F(S)\), so the two processes can be simulated step for step in either direction. This proves the displayed equivalence, including empty skew initial sets and isolated base vertices.

**3. Enumerators and minimality.** Fix a skew-forcing base set \(F\). A corresponding ordinary set consists of every vertex above \(F\), and all but exactly one vertex above each \(v\notin F\). There are \(m^{n-|F|}\) labelled choices, each of size \(n(m-1)+|F|\), with no overlap between distinct base sets. Summing gives the first substitution identity. Removing any selected vertex in a partially occupied fibre creates two white false twins and therefore fails. Removing one selected vertex from a fully occupied fibre changes \(F\) to \(F\setminus\{v\}\) while maintaining the at-most-one-white condition. Thus the lifted set is inclusion-minimal exactly when \(F\) is inclusion-minimal under the skew rule. This gives the second identity and all minimum/upper-minimal and well-forced consequences.

**4. Skew forcing on cycles.** Every vertex of \(C_n\) has exactly two neighbors. A skew force is possible whenever one of those neighbors is blue and the other white. Equivalently, a blue site can spread across a distance-two edge \(v\)--\(w\), using the common neighbor as the forcing vertex. Let \(H_n\) connect the vertices of the cycle at cyclic distance two. The components of \(H_n\) are one cycle when \(n\) is odd and the two parity classes when \(n\) is even. A nonempty initial blue set in every component propagates across that entire component. Conversely, no initially all-white component can acquire a blue site: the two neighbors of each vertex of the opposite component remain simultaneously white within that component. Hence a set skew forces \(C_n\) exactly when it meets every component of \(H_n\). This proves

\[
\mathcal Z^-_{C_n}(z)=\begin{cases}(1+z)^n-1,&n\text{ odd},\\((1+z)^{n/2}-1)^2,&n\text{ even},\end{cases}
\quad
\mathcal M^-_{C_n}(z)=\begin{cases}nz,&n\text{ odd},\\(n/2)^2z^2,&n\text{ even}.\end{cases}
\]

Substitution and Step 3 give the asserted cycle enumerator, minimum values, minimality, and counts.

**5. Vertex-transitive sparse family.** For \(n\ge5\), a vertex of \(C_n[\overline{K_2}]\) has four neighbors, two in each adjacent cycle fibre; all degrees are four. Rotation of the base cycle together with independent permutations of the two vertices inside each fibre acts transitively. The graph is connected; any triangle would project to a triangle of the cycle because fibres contain no edges, so the graph is triangle-free. Its \(2n\) vertices support the exact minimum-set counts in the Finding. The counts are exponential in \(2n\), while the edge count is \(4n\). This establishes the claimed bounded-degree connected vertex-transitive existence result.

## Verification

The standalone `verify.cpp` enumerates every ordinary initial set of the independent-fibre graph and every skew initial set of the base, using separately implemented color-change closure rules. It checks the transfer equivalence, both size polynomials, and the inclusion-minimal characterization for all labelled base graphs on up to five vertices with two-vertex fibres (including all \(1024\) labelled five-vertex bases), and all bases on up to three vertices with three-vertex fibres. It separately checks the closed cycle polynomials for two-vertex fibres and cycle lengths five through nine, three-vertex fibres and lengths three through five, and four-vertex fibres at length four. The program completed successfully with `ALL_BASE_GRAPHS_AND_ALL_SUBSETS_OK`, each `CYCLE ... OK`, and `TRANSFER_MINIMAL_AND_CYCLE_CERTIFICATES_OK`. These finite tests are reproducibility checks; Steps 1--5 supply the infinite and all-graphs proofs.

Build with `g++ -O2 -std=c++17 verify.cpp -o verify` and run `./verify`.

## Relationship to prior work

Brimkov and Carlson (2022) introduced the inclusion-minimal zero-forcing-set question and explicitly asked whether *sparse connected vertex-transitive graphs* could have exponentially many such sets (their concluding Section 4; first public preprint April 4, 2022). Their example \(C_5\square K_t\) has increasing degree; it is not the bounded-degree independent-fibre cycle family. The zero-forcing polynomial convention is from Boyer and collaborators (2018). Javaid and collaborators (2016, Section 3) give bounds for zero forcing of lexicographic products, including edgeless fibres, but not this exact bijection, polynomial transform or minimal-set census. Benson and collaborators (2015 preprint, Section 2.1 and Section 3.2) employ skew forcing to obtain a bound for **tensor products with a complete graph**, and treat some lexicographic-product scalar parameters; their tensor graph differs from an independent-fibre lexicographic blowup, and they do not establish the claimed all-set transform. Published calculations on clique-expanded cycles \(C_n[K_m]\) concern *true-twin* (complete) fibres, which have different neighborhoods and forcing dynamics. The skew-zero-forcing classification of cycles is used as an elementary supporting fact, not asserted to be new.

## Limitations

This exact transfer requires independent fibres, each of size at least two. It does not assert an analogous formula for clique fibres, arbitrary inner graphs, or tensor products. Polynomial coefficients count all successful initial sets, not the chronological forcing sequences. The finite verifier does not itself certify the infinite statement, and publication-priority uniqueness has not been independently established; the open-question resolution is understood relative to the specifically inspected earlier literature and indexed comparisons. Independent validation has not been performed.

## References

1. B. Brimkov and J. Carlson, *Minimal Zero Forcing Sets* (first public April 4, 2022), https://arxiv.org/html/2204.01810v2 ; especially Proposition 6 and concluding Section 4.
2. K. Boyer et al., *The zero forcing polynomial of a graph* (first public January 26, 2018), https://arxiv.org/html/1801.08910v1 .
3. I. Javaid et al., *On the zero forcing number of corona and lexicographic product of graphs* (first public July 14, 2016), https://arxiv.org/html/1607.04071v1 ; Section 3.
4. K. F. Benson et al., *Power domination and zero forcing* (first public October 8, 2015; subsequent journal title *Zero forcing and power domination for graph products*), https://arxiv.org/abs/1510.02421 ; Sections 2.1 and 3.2.
5. *Closed zero-forcing polynomials and well-forcedness of clique-expanded cycles* (published indexed finding, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-closed-zero-forcing-polynomials-and-well-forcedness-of-clique-ex--86ad1fa62971 ; a different, true-twin fibre product.
