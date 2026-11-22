# Exact hexagon Walsh recovery and optimal projection for the Möbius–Kantor graph

## Finding

Let \(G=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph, with \(16\) vertices and \(24\) edges. Let \(\mathcal H\) be the set of **all** unoriented simple cycles of length six, each represented by its edge-incidence vector in \(\mathbb F_2^{24}\). There are exactly \(24\) such cycles. Define unnormalized convolution on functions on \(\mathbb F_2^{24}\) by
\[
(Tf)(x)=\sum_{C\in\mathcal H} f(x+\mathbf1_{E(C)}).
\]
The complete signed Walsh eigenvalue distribution of \(T\) is

| Eigenvalue | Multiplicity |
|---:|---:|
| \(-8\) | 1,081,344 |
| \(-4\) | 5,505,024 |
| \(0\) | 5,242,880 |
| \(4\) | 3,145,728 |
| \(8\) | 983,040 |
| \(12\) | 786,432 |
| \(24\) | 32,768 |

Consequently the exact rank is \(11,534,336\), the exact nullity is \(5,242,880\), the smallest nonzero singular value is \(4\), and the nonzero-spectrum \(\ell^2\) condition number is \(6\). Let \(W=\operatorname{ran}T\). Among **all** (not necessarily translation-invariant) real or complex linear projections onto \(W\), the sharp endpoint norms are
\[
\min_{Q^2=Q,\ \operatorname{ran}Q=W}\|Q\|_{\ell^1\to\ell^1}
=\min_{Q^2=Q,\ \operatorname{ran}Q=W}\|Q\|_{\ell^\infty\to\ell^\infty}
=\frac{123}{16}.
\]
The orthogonal Fourier-range projector is an explicit convolution with a kernel supported in the nine-dimensional binary cycle space, whose coefficient counts are given below.

## Assumptions and scope

The graph has vertices \(u_i,v_i\), with \(i\in\mathbb Z/8\mathbb Z\). Its undirected edges are \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), for all eight indices in each family. Index edges lexicographically by their sorted endpoint pairs, with \(u_i=i\), \(v_i=8+i\). A hexagon means a simple unoriented six-edge cycle, not just a face of one topological embedding or one symmetry-selected orbit. Each is counted exactly once. All transforms are **unnormalized** character sums; \(\ell^p\) norms are counting-measure norms on \(\mathbb F_2^{24}\).

For a frequency \(s\in\mathbb F_2^{24}\), define
\[
\lambda(s)=\sum_{C\in\mathcal H}(-1)^{\langle s,\mathbf1_{E(C)}\rangle}.
\]
Here the pairing and all additions in exponents are modulo two. The claims concern this one fixed graph and this specific shortest-cycle convolution. They do not assert analogous values for arbitrary cubic graphs, nor for other cycle lengths.

## Proof

**1. Complete enumeration of the codebook.** The graph is connected, simple and bipartite. For six selected edges, the condition that all sixteen selected-subgraph vertex degrees lie in \(\{0,2\}\) is equivalent to being a simple six-cycle: any selected component is a cycle, every cycle in a bipartite simple graph has at least four edges, and six edges cannot support two components. Exhausting the \(\binom{24}{6}=134,596\) six-element edge subsets therefore exhausts the hexagons without overcounting. The exact enumerator in `verify.py` yields \(24\), independently matching a vertex-simple-path enumeration. Every edge lies in exactly six hexagons. An independent construction from eight nonzero points in \(\mathbb F_3^2\) and eight affine lines avoiding zero is explicitly isomorphic to this graph, and generates the identical cycle set after transporting edges.

**2. Reduction to nine binary variables.** Since the graph has \(24\) edges, \(16\) vertices and is connected, its binary cut space has dimension \(15\), and its binary cycle space has dimension \(24-16+1=9\). Every hexagon is orthogonal to every cut. Accordingly \(\lambda\) is constant on cut-space cosets. Fix a spanning tree \(S\) of \(G\). Each cut-space coset has a unique representative zero on its fifteen tree edges: solve the vertex-switching equations on the tree, up to a global switch. Thus the \(2^{24}\) frequencies reduce **without approximation** to all \(2^9=512\) choices of signs on the nine chords, and every reduced frequency appears exactly \(2^{15}=32,768\) times. Projecting each hexagon onto its chord coordinates is injective on the cycle space; the twenty-four chord vectors span \(\mathbb F_2^9\), as verified by exact binary elimination.

**3. Signed spectrum certificate.** For each chord frequency \(a\in\mathbb F_2^9\), evaluate
\[
L(a)=\sum_{c\in\mathcal H_{\rm chord}}(-1)^{a\cdot c}.
\]
The complete histogram over the \(512\) values is

| \(L(a)\) | Number of \(a\) |
|---:|---:|
| \(-8\) | 33 |
| \(-4\) | 168 |
| \(0\) | 160 |
| \(4\) | 96 |
| \(8\) | 30 |
| \(12\) | 24 |
| \(24\) | 1 |

The supplied exact-integer verifier evaluates all \(512\) signed sums directly and independently computes the nine-variable Walsh–Hadamard transform of the \(24\)-point chord-codebook indicator; all \(512\) values agree, not merely their histograms. The separate affine-configuration model produces the same histogram. Multiplying counts by \(2^{15}\) gives the claimed ambient signed spectrum. The extrema \(4\) and \(24\) of the nonzero magnitudes give the condition number \(24/4=6\).

**4. The range projection and its endpoint norm.** Let \(P\) be the Fourier multiplier \(\mathbf1_{\{\lambda\ne0\}}\). Its convolution kernel is the inverse Walsh transform of this indicator. Since the multiplier is cut-invariant, its kernel is supported on the binary cycle space. Under the nine-chord identification, define the integer numerator
\[
K(c)=\sum_{a\in\mathbb F_2^9}\mathbf1_{\{L(a)\ne0\}}(-1)^{a\cdot c},\qquad p(c)=2^{-9}K(c).
\]
The complete certified numerator distribution is

| \(K(c)\) | Count |
|---:|---:|
| \(-24\) | 30 |
| \(-16\) | 12 |
| \(-8\) | 100 |
| \(0\) | 216 |
| \(8\) | 102 |
| \(16\) | 24 |
| \(24\) | 24 |
| \(32\) | 3 |
| \(352\) | 1 |

It follows exactly that \(\sum_c|K(c)|=3,936\), so
\[
\|P\|_{\ell^1\to\ell^1}=\|P\|_{\ell^\infty\to\ell^\infty}
=2^{-9}\sum_c|K(c)|=\frac{123}{16}.
\]
For \(\ell^1\) the equality follows by applying convolution to a delta function; for \(\ell^\infty\), choose a sign function aligning with a kernel row. Finally, for any linear projection \(Q\) onto \(W\), average \(Q\) over all binary translations. Translation conjugation is isometric for \(\ell^1\) and \(\ell^\infty\), preserves \(W\), and the average remains a projection onto \(W\). The only translation-equivariant projection with range \(W\) is \(P\), by one-dimensional Fourier character spaces. Thus \(\|P\|\le\|Q\|\), proving optimality without a symmetry assumption on \(Q\).

## Verification

Run `python3 verify.py` in an ordinary Python 3 environment; it requires no packages beyond the standard library and uses exact integer or rational arithmetic. The verifier independently constructs the generalized Petersen and affine-configuration models and checks an explicit graph isomorphism; enumerates all simple hexagons by vertex paths and by all six-edge subsets; checks each of the \(24\) edges lies in six hexagons; reduces by an actual spanning tree; checks binary rank nine; evaluates all \(512\) signed character sums directly and via an independent fast Walsh–Hadamard transform; compares both graph models; inverts the exact support indicator; and checks all displayed tables and rational norms. Finite enumeration is an exhaustive finite proof here because the search spaces and exhaustive loops are explicit, not a sampling experiment.

## Relationship to prior work

Lijnen and Ceulemans (first available online on 18 August 2004) studied symmetry-distinct oriented two-cell embeddings of the same graph; their abstract is available, but their full article was inaccessible in this assessment. Zhou and Feng (available online on 15 October 2011) give the canonical \(\operatorname{GP}(8,3)\) graph model and its edge-transitive automorphism groups. Kutnar, Marušič, Miklavič and Šparl (first available 9 October 2023) study consistent cycles of cubic symmetric graphs, including this graph's girth and its eight- and twelve-cycles. Those are graph-theoretic structure and cycle-action results rather than a signed Walsh diagonalization of the hexagon counting convolution. The classical binary cut/cycle orthogonality and translation-averaging argument are standard tools and are not asserted to be new. The assessed contribution is the particular **complete signed character histogram, exact recoverable range and globally sharp endpoint projection constant** for the all-hexagon codebook.

## Limitations

The findings are finite and specific to \(\operatorname{GP}(8,3)\). Invertibility does not hold: \(5,242,880\) of \(2^{24}\) characters are invisible. No claim is made about an infinite family or human-independent proof review. This is a reproducible self-review, not an independent audit. A full-text comparison with Lijnen–Ceulemans was unavailable (the institutional route reported disconnected); thus hidden equivalent calculations in that article or other unindexed literature remain a bounded priority risk. An unrelated published graph-adjacency-spectrum discussion reports a different shortest-cycle count; the present all-simple-cycle enumeration is independently and exhaustively verified in both graph models, and no count from that discussion is used in the argument.

## References

1. E. Lijnen and A. Ceulemans, *Oriented 2-Cell Embeddings of a Graph and Their Symmetry Classification: Generating Algorithms and Case Study of the Möbius-Kantor Graph*, Journal of Chemical Information and Computer Sciences 44 (2004), 1552–1564, DOI: https://doi.org/10.1021/ci049865c (first online 2004-08-18; abstract inspected).
2. J.-X. Zhou and Y.-Q. Feng, *Edge-transitive cyclic regular covers of the Möbius–Kantor graph*, European Journal of Combinatorics 33 (2012), 139–147, DOI: https://doi.org/10.1016/j.ejc.2011.09.034 (first online 2011-10-15; full reproduced text inspected at https://www.academia.edu/92081984/Edge_transitive_cyclic_regular_covers_of_the_M%C3%B6bius_Kantor_graph).
3. K. Kutnar, D. Marušič, Š. Miklavič and P. Šparl, *On the structure of consistent cycles in cubic symmetric graphs*, Journal of Graph Theory 105 (2024), 337–356, DOI: https://doi.org/10.1002/jgt.23041 (first online 2023-10-09; complete open HTML inspected).
4. A. E. Brouwer, *Möbius–Kantor graph*, https://aeb.win.tue.nl/drg/graphs/MoebiusKantor.html (graph identity and background; undated online source).
