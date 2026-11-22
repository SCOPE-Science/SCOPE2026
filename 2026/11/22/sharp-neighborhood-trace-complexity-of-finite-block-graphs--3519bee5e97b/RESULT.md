# Sharp neighborhood-trace complexity of finite block graphs

## Finding

For every integer \(m\geq0\), let \(\pi_{\mathcal B}(m)\) be the maximum, over finite nonempty simple undirected block graphs \(G\) and marked subsets \(A\subseteq V(G)\) with \(|A|=m\), of the number \(|\{N_G(v)\cap A:v\in V(G)\}|\) of **distinct open-neighborhood traces**. Then
\[
\boxed{\pi_{\mathcal B}(0)=1,\quad\pi_{\mathcal B}(1)=2,\quad\pi_{\mathcal B}(2)=4,\quad\pi_{\mathcal B}(3)=8,\quad \pi_{\mathcal B}(m)=3m-2\ (m\ge4).}
\]
Consequently the class of all finite block graphs has open-adjacency VC dimension exactly \(3\), and its open-adjacency VC density is \(1\), with exact leading coefficient \(3\) for the shatter function. These are bounds on all possible graph sizes, with marked and unmarked vertices both eligible as neighborhood centers.

## Assumptions and scope

A *block graph* is a finite simple undirected graph in which every maximal biconnected block is a clique. It may be disconnected; an isolated vertex is permitted. The open neighborhood \(N_G(v)\) excludes \(v\). Each edge belongs to one maximal clique block; the bipartite incidence graph between original vertices and nontrivial maximal clique blocks is a forest (the block-cut incidence forest). The induced graph on any vertex subset of a block graph is again a block graph. Empty marked sets are permitted if the ambient graph is nonempty.

## Proof

**Trace bound via marked connected components.** Fix a graph \(G\), a marked set \(A\) of size \(m>0\), and the connected components \(H_1,\ldots,H_c\) of \(H=G[A]\). Write \(t_i=|V(H_i)|\), \(b_i\) for the number of nontrivial clique blocks of \(H_i\), and \(u_i\) for the number of vertices of degree at least two in \(H_i\). We bound the types of all traces by the following exhaustive, possibly overlapping categories.

First, at most \(m+1\) traces are empty or singletons. Second, a marked vertex with at least two marked neighbors gives one of at most \(\sum_i u_i\) traces. Third, let an unmarked vertex \(v\) have at least two marked neighbors and suppose all of them lie in one connected component \(H_i\). They must lie in a single nontrivial clique block of \(H_i\). Indeed, let \(T\) be the vertex–clique incidence forest of \(G\). For two marked neighbors \(a,b\) of \(v\), there exists a path between \(a\) and \(b\) using only marked vertices and clique nodes of \(T\), since they lie in the same component of \(G[A]\). But if \(a\) and \(b\) were joined to \(v\) through distinct incident clique nodes, there would also be a different simple \(a\)-to-\(b\) path in \(T\) passing through \(v\), impossible in a forest. All its marked neighbors are therefore in the same original clique, which induces a nontrivial clique block of \(H_i\). Moreover, since \(v\) is adjacent to every marked member of that original clique, its trace equals precisely the marked intersection of the clique. Hence these traces provide at most \(\sum_i b_i\) types.

Fourth, consider unmarked vertices whose marked neighbors meet at least two different \(H_i\)'s. For each \(i\), take in \(T\) the marked vertices of \(H_i\), together with all clique nodes incident to them. This is a connected subtree \(D_i\). The subtrees are disjoint: a common clique node would contain marked vertices of both components, joining those components in \(H\). Contract each \(D_i\) to a terminal, then retain the unmarked vertex nodes and suppress intermediate clique nodes as necessary. The resulting incidence connections are a forest; each unmarked vertex connected to at least two marked components has degree at least two among its terminal-neighbor connections. In a forest on \(c\) terminal vertices and arbitrary additional vertices, at most \(c-1\) nonterminal vertices can have at least two distinct terminal adjacencies (more generally, prune other leaves and use the tree edge count). Thus this fourth type accounts for at most \(c-1\) traces. We obtain
\[
|\{N_G(v)\cap A:v\in V(G)\}|\le (m+1)+\sum_i u_i+\sum_i b_i+(c-1)
=m+\sum_i(u_i+b_i+1).\tag{1}
\]

**A block-tree deficit.** Let \(H_i\) have \(t=t_i\) vertices. Define \(\ell\) as the number of vertices of degree at most one in \(H_i\), and \(\delta=\sum_B(|B|-2)\), summing over its nontrivial clique blocks. The block-incidence tree identity gives \(t=1+\sum_B(|B|-1)\), while \(u=t-\ell\) and \(b=t-1-\delta\). Therefore
\[
u+b+1=2t-(\ell+\delta).\tag{2}
\]
If \(t=1\), then \(\ell+\delta=1\). If \(t\ge2\) and \(\delta=0\), the connected graph is a tree and has at least two leaves. If \(\delta=1\), it has exactly one triangular block and every other block is an edge; unless it consists of just that triangle, it has a degree-one vertex. If \(\delta\ge2\), no further argument is needed. Thus \(\ell+\delta\ge2\) except for the one-vertex graph and the triangle, in which cases it equals one.

Set \(e\) to be the number of \(H_i\) that are single vertices or triangles. Equations (1)–(2) show
\[
|\mathcal N(G,A)|\le3m-2c+e.\tag{3}
\]
For \(m\ge4\), if \(c=1\), the unique component cannot be a single vertex or triangle, so \(e=0\) and (3) is \(3m-2\). If \(c\ge2\), then \(e\le c\), giving at most \(3m-c\le3m-2\). For \(m\le3\), the elementary \(2^m\) bound suffices.

**Sharpness.** For \(m\ge4\), form a marked path \(a_1-\cdots-a_m\). For each path edge \(a_i a_{i+1}\), attach a new vertex \(b_i\) to both ends, making a triangular block. Add for each \(a_i\) a new unmarked pendant vertex \(p_i\), and add one isolated unmarked vertex \(w\). This graph is a block graph. Its distinct traces are \(\varnothing\) (from \(w\)), all \(m\) singletons (from the \(p_i\)), all \(m-1\) adjacent marked pairs (from the \(b_i\)), and all \(m-2\) distance-two marked pairs (from the internal \(a_i\)); the latter two pair families are disjoint for \(m\ge4\). Hence it attains \(1+m+(m-1)+(m-2)=3m-2\). For \(m=3\), take a marked triangle and a fourth vertex completing \(K_4\); add one pendant at each marked vertex and one isolated vertex. The marked vertices realize the three two-subsets; the fourth clique vertex realizes the three-subset; the pendants and isolated vertex realize singletons and the empty trace: all eight subsets. For \(m=2\), a marked edge with a common unmarked neighbor, two unmarked pendants and one isolate realizes all four subsets. For \(m=1\), one marked vertex with a pendant and an isolate realizes both subsets; for \(m=0\), any nonempty graph has exactly the empty trace. This concludes the proof.

## Verification

The accompanying standalone Python file `verify.py` uses only the standard library. It independently detects clique biconnected blocks with Tarjan's algorithm, enumerates every labelled simple graph through six vertices, checks every marked subset of every block graph against the claimed upper bound, tests explicit sharpness witnesses for every size up to 18, and tests seeded random block graphs. Run `python3 verify.py`. Its output is a finite cross-check; the all-size proof is the preceding incidence-forest argument.

## Relationship to prior work

Dreier–Mählmann–McCarty–Pilipczuk–Toruńczyk (2026) prove almost-linear neighborhood complexity in monadically dependent graph classes. Their general result concerns growth exponents and does not imply an optimal coefficient or finite additive constant for a specified block-graph class. Benediktsson–Macpherson–Adler (2020) calculate VC dimension and density of open adjacency in Johnson and Hamming graphs, different graph families. Chakraborty–Foucaud–Parreau–Wagler (2018) investigate separating and domination-based codes in block graphs, not the exact maximum over all distinct open-neighborhood traces. Existing block-graph results on neighborhood-complex homotopy, induced convexity, and color refinement concern different invariants. This result claims the class-wide sharp numerical shatter function above, not novelty of the standard incidence-tree representation, the VC definitions, or generic almost-linear bounds.

## Limitations

The result is restricted to **open adjacency** of ordinary finite block graphs; it does not establish analogous formulas for closed neighborhoods, arbitrary chordal graphs, higher-distance neighborhoods, or other first-order formulas. The data in `verify.py` independently cross-check only finite cases; they do not replace the proof. Although targeted searches and full-text comparisons found no covering result, an equivalent bound could occur under alternative names or in inaccessible literature; historical priority is not independently audited.

## References

1. Jan Dreier, Nikolas Mählmann, Rose McCarty, Michał Pilipczuk, and Szymon Toruńczyk. *Neighborhood Complexity and Radius-1 Merge-Width in Monadically Dependent Graph Classes* (first public 2026-07-12), https://arxiv.org/abs/2607.10941.
2. Bjarki Geir Benediktsson, Dugald Macpherson, and Isolde Adler. *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs* (2020), https://arxiv.org/abs/2007.16042.
3. Dibyayan Chakraborty, Florent Foucaud, Aline Parreau, and Anita Wagler. *On three domination-based identification problems in block graphs* (2018), https://arxiv.org/abs/1811.09537.
4. Jan Dreier, Nikolas Mählmann, and Szymon Toruńczyk. *First-Order Model Checking on Monadically Dependent Graph Classes* (2026), https://arxiv.org/abs/2611.08143.
