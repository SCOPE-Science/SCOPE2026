# Exact parity law for contact colorings of extremal triangular tilings on flat tori

## Finding

Let \(u,v\) be the standard primitive edge vectors of the equilateral triangular lattice. Subdivide every unit equilateral triangular face into three congruent \(30^\circ\)-\(30^\circ\)-\(120^\circ\) triangular cells by joining its center to its vertices. For integers \(m,n\ge5\), quotient this tiling by translations \(mu,nv\). Color the resulting \(6mn\) closed triangular cells so that two distinct cells with any common point receive different colors (contacts at a single vertex count).

**Theorem.** The minimum number of colors is exactly

\[
\chi_{\rm contact}(m,n)=
\begin{cases}
12,&mn\text{ even},\\
13,&mn\text{ odd}.
\end{cases}
\]

The infinite planar subdivided tiling itself needs exactly 12 colors. Thus compactifying the uniquely extremal 21-neighbor tiling on a rectangular triangular-lattice torus imposes **one additional color precisely when the number of original lattice vertices is odd**.

The construction on the \(5\times5\) torus is independently witnessed by an explicit 150-cell, 13-color certificate in `certificate_5x5.json`. It has exactly six color classes of 11 cells and seven of 12 cells.

## Assumptions and scope

The triangular lattice is \(\{iu+jv:i,j\in\mathbb Z\}\), with \(\|u\|=\|v\|=\|u-v\|=1\). The flat quotient has period subgroup \(m\mathbb Zu+n\mathbb Zv\). A contact means any nonempty intersection of *closed* cells, even a singleton; side-sharing alone is not the contact relation. Both periods are at least five, so the six neighbors of any old lattice vertex are distinct and their induced graph is a cycle of length six. The result concerns these two-generator rectangular period subgroups, not arbitrary skew quotients or arbitrary tilings.

Write \(T_{m,n}\) for the undirected graph on \(\mathbb Z_m\times\mathbb Z_n\) with edge differences \(\pm(1,0)\), \(\pm(0,1)\), and \(\pm(1,-1)\). It is a connected, simple, 6-regular graph on \(N=mn\) vertices with \(3N\) edges. Let \(2T_{m,n}\) be the loopless multigraph replacing each edge by two parallel copies. Its maximum degree is 12.

The proof uses two published results exactly as stated: Abdollahi's 1-factorization theorem for connected Cayley graphs of \(Q\times H\) with a nontrivial 2-group \(Q\) and odd-order \(H\), and the Goldberg–Seymour bound for every loopless multigraph \(M\),

\[
\chi'(M)\le\max\{\Delta(M)+1,\lceil\Gamma(M)\rceil\},\qquad
\Gamma(M)=\max_{\substack{S\subseteq V(M)\\ |S|\ge3\ \mathrm{odd}}}\frac{2|E_M(S)|}{|S|-1}.
\]

These two general theorems and the geometric contact-graph description are prior work or standard inputs; the new statement is the exact contact-palette classification for the entire two-parameter torus family.

## Proof

**1. Geometric reduction.** Each old lattice edge is contained in two large triangular faces. Within each face it borders exactly one small triangular cell, so it indexes two small cells in total. Two such small cells meet at an original lattice vertex exactly when the original edges indexing them are incident. The only other possibility for meeting at a large-face center occurs between two of the three small cells of that face; their indexing original edges are likewise incident at a lattice vertex. There are no further contacts. Consequently the small-cell contact graph is canonically the line graph of the doubled-edge multigraph,

\[
C_{m,n}\cong L(2T_{m,n})\cong L(T_{m,n})[K_2].
\]

In particular the color question is the ordinary edge-chromatic-index problem \(\chi_{\rm contact}(m,n)=\chi'(2T_{m,n})\). Each old lattice vertex has twelve incident doubled edges, supplying a clique of size twelve in the line graph. Thus twelve colors are necessary for every \(m,n\ge5\).

**2. Even order.** Suppose \(N=mn\) is even. The graph \(T_{m,n}\) is a connected Cayley graph of the finite abelian group \(\mathbb Z_m\times\mathbb Z_n\), which splits into a nontrivial Sylow 2-subgroup and an odd-order complement. Abdollahi's theorem makes it 1-factorizable. As it is 6-regular, its edges split into six disjoint perfect matchings. Give the two parallel copies of every edge from the \(j\)-th matching the two colors \((j,0)\) and \((j,1)\). This gives an edge coloring of \(2T_{m,n}\) in twelve colors. The local 12-clique proves sharpness.

**3. Odd order: matching-density bound.** Suppose \(N\) is odd; here \(N\ge25\). For an odd vertex subset \(S\), set \(s=|S|\) and let \(e(S)\) denote the number of ordinary edges of \(T_{m,n}\) induced on \(S\). Since every such edge is doubled,

\[
\frac{2|E_{2T}(S)|}{s-1}=\frac{4e(S)}{s-1}.
\]

We prove this is at most 13 for every odd \(s\ge3\):

- If \(s=3\) or \(5\), simplicity gives \(e(S)\le\binom{s}{2}\), hence \(4e(S)/(s-1)\le2s\le10\).
- If \(s=7\), either every induced degree is at most five, yielding \(e(S)\le\lfloor35/2\rfloor=17\), or a vertex has all six of its lattice neighbors in \(S\). In the latter case \(S\) consists of this vertex and its six neighbors. Those neighbors induce exactly a hexagonal 6-cycle, so \(e(S)=12\). Either way \(4e(S)/6\le68/6<13\).
- If \(s=9\) or \(11\), \(S\) is a nonempty proper subset of the connected 6-regular graph. Its edge boundary is nonempty, so \(2e(S)\le6s-1\), whence \(e(S)\le3s-1\). Therefore the corresponding two possible bounds are \(4\cdot26/8=13\) and \(4\cdot32/10=64/5<13\).
- If \(s\ge13\), the degree bound yields \(e(S)\le3s\), so \(4e(S)/(s-1)\le12s/(s-1)\le13\).

Thus \(\Gamma(2T_{m,n})\le13\). The full vertex set is allowed in the odd-subset maximum, and has \(6N\) doubled edges. Hence

\[
\Gamma(2T_{m,n})\ge\frac{12N}{N-1}>12.
\]

Every edge color class is a matching and cannot cover more than \((N-1)/2\) of these \(6N\) edges; equivalently \(\chi'(2T_{m,n})\ge\lceil\Gamma\rceil=13\). The Goldberg–Seymour theorem gives the matching upper bound

\[
\chi'(2T_{m,n})\le\max\{12+1,\lceil\Gamma\rceil\}=13.
\]

This proves the odd-order case and the claimed complete parity law.

**4. Infinite planar benchmark.** Every original edge has one of three directions. In each direction, orient edges consistently and label the two consecutive incident edges at any original vertex by the parity of their oriented tail coordinate. Pair that 2-valued label with one of the two large-face sides of the edge, and retain the direction label. This is a 12-coloring of all small cells: at an old lattice vertex all 12 labels are distinct, and any meeting at a face-center is already covered by a shared old vertex. The twelve small cells incident at an old lattice vertex give the matching lower bound.

## Verification

`certificate_5x5.json` stores a two-element color list for each of the 75 original edges in lexicographic order of \((i,j)\), followed by directions \((1,0),(0,1),(1,-1)\). The two entries color the two small triangles on that edge. Run from a directory containing the files:

```sh
python3 verify_torus_coloring.py certificate_5x5.json
```

The checker uses only Python's standard library. It reconstructs all 25 original vertices, 75 original edges, 50 equilateral faces, and 150 subdivided tiles. It checks that all pairs of touching tiles have different colors, that every tile has 21 neighbors (giving 1,575 contact edges), and that all 13 palette entries occur. The certificate's six color classes of size 11 and seven of size 12 are independently counted.

The finite certificate illustrates the all-odd result at the smallest included square quotient but does not prove the infinite family; that proof uses the exact matching-density inequality and the two cited general theorems. The even and odd cases do not require numerical approximation.

## Relationship to prior work

Yang and Wang (2026) prove the global 21-neighbor maximum and uniqueness of the central-subdivided triangular tiling, which is the geometric starting object. A separate earlier study identified its infinite contact graph as \(L(T)[K_2]\) and determined graph-ball counts; neither statement is newly claimed here. The present computation applies the contact relation to compact rectangular quotients and determines the palette threshold across all period pairs.

Abdollahi (2008) proves the 1-factorization theorem used for every even-order quotient. Chen, Jing and Zang's Goldberg–Seymour theorem (preprint 2019; journal article 2025) is used for the odd-order upper bound. The original contributions are the precise toroidal contact interpretation, the uniform odd-set density verification, and the resulting sharp odd/even coloring classification; neither general edge-coloring theorem is claimed as new. This is a specialized application of powerful existing results, not a new universal edge-coloring theorem.

## Limitations

The theorem is restricted to rectangular translation periods at least five in each primitive edge direction. It does not assert an analogous two-valued parity law for arbitrary skew period lattices, distinct prototiles, unequal local tile weights, edge-only adjacency, or nonperiodic coverings beyond the explicitly discussed infinite-plane case. The construction relies on published general theorems, whose proofs are not reproduced. The exact 5-by-5 certificate is finite evidence only; the universal result is proved analytically assuming those theorems. No independent mathematical audit has been conducted. Historical priority could be affected by equivalent toroidal multigraph-coloring literature that is not indexed under the geometric terminology.

## References

1. Y. Yang and E. Wang, *Convex monohedral tilings: a sharp neighbor bound and rigidity in the equality case*, arXiv:2611.13664v1, 10 November 2026. https://arxiv.org/html/2611.13664v1
2. A. Abdollahi, *1-Factorizations of Cayley Graphs*, Ars Combinatoria 86 (2008), 129–131; original arXiv version 2 May 2007. https://combinatorialpress.com/ars-articles/volume-086-ars-articles/1-factorizations-of-cayley-graphs/
3. G. Chen, G. Jing and W. Zang, *Proof of the Goldberg–Seymour conjecture on edge-colorings of multigraphs*, Journal of Combinatorial Optimization 50 (2025), article 23; preprint arXiv:1901.10316 (2019). https://link.springer.com/article/10.1007/s10878-025-01348-6
4. *Exact graph balls and contact-edge boundaries in the 21-neighbor convex tiling*, earlier contact-graph description; cited solely for its prior isomorphism claim, not for the new coloring result.
