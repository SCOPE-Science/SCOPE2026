# Branch-forest collapse of one-point type spectra over subcubic tree line graphs

## Finding
Let \(T\) be any finite tree with at least two vertices and maximum degree at most three. In the countable homogeneous \(K_4\)-free Henson graph, individually name the vertices of a copy of the line graph \(L(T)\). Let \(f_k(T)\) be the number of complete **nonalgebraic** one-point types adjacent to exactly \(k\) named vertices, and put
\[
F_T(z)=\sum_{k=0}^{m}f_k(T)z^k,\qquad m=|E(T)|.
\]
Let \(B(T)=\{v\in V(T):\deg_T(v)=3\}\), and let \(H=T[B(T)]\) be the forest induced on those branch vertices. For \(W\subseteq B(T)\), write \(e_H(W)\) for the number of edges of \(H\) with both endpoints in \(W\). Then
\[
\boxed{F_T(z)=\sum_{W\subseteq B(T)}(-1)^{|W|}z^{3|W|-e_H(W)}(1+z)^{m-3|W|+e_H(W)}.}
\]
In particular, the **entire** graded one-point type spectrum depends only on the number of edges of \(T\) and the isomorphism type of its induced branch forest \(H\); once direct branch-to-branch adjacencies are fixed, it is insensitive to how the remaining edges are distributed among subdivided connections and pendant arms, except through the total number of edges.

Some branch information is nevertheless recoverable. For \(m\ge3\), with \(b=|B(T)|\),
\[
\boxed{b=\binom m3-[z^3]F_T(z).}
\]
For \(m\ge5\), with \(h=|E(H)|\),
\[
\boxed{h=[z^5]F_T(z)-\binom m5+b\binom{m-3}{2}.}
\]
Thus the spectrum recovers both the number of degree-three vertices and their adjacency count.

The full spectrum distinguishes every pair of nonisomorphic subcubic trees on at most five vertices, and it first fails at **six vertices**. There are exactly four subcubic unlabelled trees on six vertices and exactly one colliding unordered pair: the three-legged spiders with arm lengths \((1,1,3)\) and \((1,2,2)\). Both have
\[
\boxed{F_T(z)=1+5z+10z^2+9z^3+3z^4,\qquad F_T(1)=28.}
\]
Their line graphs are not isomorphic (their vertex-degree multisets differ), so the two pointwise-named parameter structures are genuinely different. More generally, for every integer \(n\ge6\), the nonisomorphic spiders of arm lengths \((1,1,n-3)\) and \((1,2,n-4)\) have identical graded spectra, giving connected examples at every such order.

## Assumptions and scope
Graphs are simple and undirected. The line graph \(L(T)\) has one vertex per edge of \(T\); two such vertices are adjacent exactly when the corresponding edges of \(T\) share an endpoint. Since \(T\) is subcubic, \(L(T)\) is \(K_4\)-free and is an allowed induced parameter graph in the countable homogeneous \(K_4\)-free graph. All parameters are individually named, and only types of a new point distinct from all parameters are counted; if algebraic one-point types are included, they contribute exactly \(m\) additional types. The variable \(z\) counts adjacencies to the named line-graph vertices. Spiders are trees with one degree-three vertex and three positive edge-length arms.

## Proof
**One-point types and linear forests.** In the countable homogeneous \(K_4\)-free graph, the possible adjacency sets of a new point over any named finite \(K_4\)-free base \(G\) are exactly the vertex subsets of \(G\) inducing triangle-free graphs. Indeed, a triangle among the neighbors would form a forbidden \(K_4\) with the new point; conversely, every triangle-free neighborhood specifies a finite \(K_4\)-free one-point extension, which embeds over \(G\). Homogeneity makes each such adjacency pattern a single complete nonalgebraic type. This general criterion is prior work; the result concerns its new structural specialization.

When \(G=L(T)\), an adjacency subset is an edge set \(S\subseteq E(T)\). Three vertices of \(L(T)\) form a triangle precisely when the three corresponding edges of the tree share a common endpoint: a triple of pairwise intersecting edges in a simple graph either shares an endpoint or forms a triangle in that graph, and a tree has no triangles. Therefore \(L(T)[S]\) is triangle-free exactly when \((V(T),S)\) has maximum degree at most two, i.e. is a disjoint union of paths and isolated vertices.

**Branch-forest inclusion–exclusion.** The only constraints on choosing \(S\) occur at degree-three vertices of \(T\). For \(v\in B(T)\) let \(A_v\) be the event that all three edges at \(v\) belong to \(S\). The polynomial for unrestricted choices is \((1+z)^m\). For \(W\subseteq B(T)\), the union of the three-edge stars at vertices of \(W\) has \(3|W|-e_H(W)\) distinct edges: edges joining two branch vertices are counted twice in the initial incidence total, and no other edge is counted twice. Requiring all these edges contributes \(z^{3|W|-e_H(W)}(1+z)^{m-3|W|+e_H(W)}\). Inclusion–exclusion over the events \(A_v\) proves the displayed all-order formula, including its branch-forest invariance.

**Information recovered from the polynomial.** A single forbidden star has three edges. A pair of distinct degree-three stars has a union of five edges if its centers are adjacent, and six edges otherwise. A collection of at least three distinct such stars has at least seven edges: since \(H\) is a forest, its induced subgraph on any \(r\ge3\) selected centers has at most \(r-1\) edges, so their union has at least \(2r+1\ge7\) edges. Consequently the degree-three coefficient is \(\binom m3-b\), and the degree-five coefficient is
\[
[z^5]F_T(z)=\binom m5-b\binom{m-3}{2}+h.
\]
These identities yield the two inverse formulas. The bounds on \(m\) ensure all displayed coefficients and binomial coefficients have their usual meanings.

**Sharp first collision and all-order witnesses.** For at most five vertices, the subcubic trees are the paths on two, three, four, and five vertices and the three-armed spiders of orders four and five. A path has no degree-three vertex, so its polynomial is \((1+z)^m\). A three-armed spider has one such vertex, so its polynomial is \((1+z)^m-z^3(1+z)^{m-3}\), different from the path polynomial for the same \(m\). On six vertices the subcubic trees are exactly the six-vertex path, two spiders with arm triples \((1,1,3)\) and \((1,2,2)\), and the tree with two adjacent degree-three vertices. Their respective spectra are
\[
(1+z)^5,\quad (1+z)^5-z^3(1+z)^2,\quad (1+z)^5-z^3(1+z)^2,\quad (1+z)^5-2z^3(1+z)^2+z^5.
\]
They exhibit exactly the claimed unique first collision. For \(n\ge6\), both stated spider arm triples sum to \(n-1\) and are distinct positive unordered triples. Each gives one branch vertex and \(m=n-1\), so their full polynomials coincide by the same spider formula. These trees, and therefore their line graphs, are nonisomorphic: the distinct arm-length multisets determine the unique degree-three-centered tree, while the two line graphs can be distinguished by their clique and pendant-path structures (or by reconstructing the unique maximal three-edge clique and the three attached arm lengths).

## Verification
The standalone `verify.py` generates every labelled tree on two through six vertices using Prüfer sequences, discards those whose maximum degree exceeds three, canonically identifies unlabelled trees by rooted center codes, and independently enumerates all new-point adjacency subsets by explicitly testing triangle-freeness in the line graph. This direct enumeration is compared coefficientwise against the branch-forest inclusion–exclusion formula, rather than merely reusing its maximum-degree condition. It finds unlabelled subcubic tree counts \((1,1,2,2,4)\) at orders two through six, and distinct spectrum counts \((1,1,2,2,3)\). It checks the unique first collision and the 25 explicit spider pairs at orders six through thirty. A fixed-seed set of 977 additional random subcubic Prüfer trees at orders seven through fourteen tests the polynomial and recovered coefficients. The deterministic run ends in `VERIFY_OK`; `verification_output.txt` records its full output. The all-order proof is inclusion–exclusion, not extrapolation from these finite checks.

## Relationship to prior work
The Henson-graph extension criterion and, in particular, the equality of nonalgebraic one-point type spectra with clique-free induced-subset polynomials, are already established; they are not new claims here. A published account entitled *Exact finite-parameter 1-type counting in Henson graphs is #P-complete* gives this general criterion, plus counting complexity, but no restriction to subcubic tree line graphs, branch-forest collapse, coefficient reconstruction, or sharp first collision. A published study of tree line graphs under color refinement concerns an inequivalent logical invariant: it establishes two-variable counting indistinguishability from a switched comparison graph, not equality of complete one-point type distributions over named parameters. Classical graph theory treats degree-at-most-two edge subsets as linear forests; the terminology and underlying elementary counting framework are not new.

Targeted literature searches for line-graph clique avoidance, Henson one-point type spectra, branch-vertex inclusion–exclusion, subcubic tree linear-forest subgraph polynomials, spiders, and reconstruction did not locate the present joint conclusion. This supports a provisional best-of-knowledge originality assessment, not a guarantee of historical priority.

## Limitations
The formula requires subcubic trees; at degree at least four the line graph contains a \(K_4\) and is not an eligible finite base in the specified Henson graph. The theorem concerns nonalgebraic one-point types and adjacency-count grading, not complete higher-arity type spaces, arbitrary graphs, or isomorphism classes of unlabeled extensions. The branch-forest dependence is a sufficient equality criterion, not a classification of all possible polynomial coincidences: nonisomorphic branch forests might also have equal polynomials. Only the first-collision classification through six vertices is asserted. Historical priority remains subject to further full-text comparison and independent review.

## References
1. C. Ward Henson, *A family of countable homogeneous graphs*, Pacific Journal of Mathematics 38 (1971), 69–83. https://msp.org/pjm/1971/38-1/pjm-v38-n1-p09-p.pdf
2. Gabriel Conant, *Forking and dividing in Henson graphs*, arXiv:1401.1570, first public 2014-01-08; later Notre Dame Journal of Formal Logic 58 (2017), 555–566. https://arxiv.org/abs/1401.1570
3. *Exact finite-parameter 1-type counting in Henson graphs is #P-complete*, published result and full proof. https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-finite-parameter-1-type-counting-in-henson-graphs-is-p-com--7c84dde7c650/RESULT.md
4. *An infinite family of tree line graphs not identifiable by color refinement*, published result and full proof. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-an-infinite-family-of-tree-line-graphs-not-identifiable-by-color--4616f122b987/RESULT.md
