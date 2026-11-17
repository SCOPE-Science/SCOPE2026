# Exact cone-volume laws and uniform-pyramid classification for cactus graphical zonotopes

## Finding
For the standard centered Euclidean graphical zonotope of **every connected simple cactus graph**, the full normalized facet-cone-volume spectrum is determined by the graph's block lengths. In particular, one gets an exact characterization of all such zonotopes with equally voluminous pyramids from the center to their facets; the characterization includes nonparallelotopes built from any number of same-length cycles glued at cut vertices.

If the graph has \(N\) vertices, \(b\) bridges, and cycle blocks of lengths \(\ell_1,\ldots,\ell_c\), write \(d=N-1\). For a facet \(F\), define \(\mu(F)=\operatorname{Vol}_{d}(\operatorname{conv}(0,F))/\operatorname{Vol}_d(Z_G)\). Then
\[
\mu(F)=\begin{cases}
1/(2d),&\text{if its oriented bond deletes a bridge},\\
1/(d\ell_i),&\text{if its oriented bond deletes two edges of cycle }i.
\end{cases}
\]
There are exactly two bridge-cut facets per bridge, and \(\ell_i(\ell_i-1)\) cycle-cut facets per cycle block. Consequently, the total cone-volume mass is \(1/d\) per bridge and \((\ell_i-1)/d\) per cycle block, with total mass one. All individual facet masses are equal **if and only if** the graph is a tree, or it is bridgeless and every cycle block has one common length. The result includes the single-edge graph and single-cycle graphs.

## Assumptions and scope
A *cactus* is a finite undirected simple connected graph in which any two distinct simple cycles share at most one vertex (equivalently, every edge belongs to at most one cycle). All its blocks are bridges or cycles of lengths at least three. We allow any attachment pattern among these blocks. There are \(N\ge2\) vertices; the graph has \(b\ge0\) bridges and \(c\ge0\) cycles. The identity \(d=N-1=b+\sum_{i=1}^c(\ell_i-1)\) follows by adding blocks along their articulation points.

In \(\mathbb R^N\) with its ordinary Euclidean metric, let \(H=\{x:\sum_{v\in V(G)}x_v=0\}\). The centered graphical zonotope is
\[
Z_G=\sum_{\{u,v\}\in E(G)}[-(e_u-e_v)/2,(e_u-e_v)/2]\subset H.
\]
It is full-dimensional in \(H\) because \(G\) is connected. Volumes are intrinsic Hausdorff–Euclidean volumes in \(H\) and in the facet affine spans; no lattice-normalized volumes are substituted. Its center is the origin, and the \(d\)-dimensional pyramid \(\operatorname{conv}(0,F)\) has volume \(A(F)h(F)/d\), where \(A(F)\) is intrinsic facet area and \(h(F)\) is its support distance from zero.

An oriented *bond* means one of the two orientations of a minimal nonempty edge cut \(\delta(S)\), where both induced graphs \(G[S]\) and \(G[V\setminus S]\) are connected. The theorem concerns **facets**, not arbitrary lower-dimensional faces or uncentered pyramids.

## Proof
**1. Metric lemma for an induced connected cut.** Let \(S\sqcup T=V(G)\) be a nontrivial partition with \(G[S]\) and \(G[T]\) connected, and put \(s=|S|\), \(t=|T|=N-s\), \(k=|\delta(S)|\). All centered generators crossing the cut are fixed at one endpoint of their segments on the maximizing facet for the cut normal, while generators internal to \(S\) or \(T\) remain free. Thus the facet is a translate of the orthogonal product of the two induced graphical zonotopes.

For any connected graph \(J\) on \(m\) vertices, the \((m-1)\)-dimensional Euclidean volume of its standard zonotope is \(\sqrt m\,\tau(J)\), with \(\tau(J)\) the spanning-tree count and \(\tau\) of the one-vertex graph defined as one. Indeed, the zonotope volume formula sums the absolute maximal minors of incidence generators, a nonzero independent set of \(m-1\) incidence columns being exactly a spanning tree; its Gram determinant is \(m\). Since the two induced incidence spaces lie on disjoint coordinate supports, the facet area is
\[
A(F)=\sqrt{st}\,\tau(G[S])\tau(G[T]).
\]
The outward unit normal is \(u=(\mathbf1_S-(s/N)\mathbf1)/\sqrt{st/N}\). Each crossing generator contributes \(\tfrac12|\langle u,e_a-e_b\rangle|=\tfrac12\sqrt{N/(st)}\) to the support. Thus
\[
h(F)=\frac{k}{2}\sqrt{\frac N{st}},\qquad
A(F)h(F)=\frac{k\sqrt N}{2}\tau(G[S])\tau(G[T]).
\]
Writing \(\tau(G)=\prod_{i=1}^c\ell_i\), another application of the spanning-tree zonotope formula gives \(\operatorname{Vol}_d(Z_G)=\sqrt N\,\tau(G)\). Therefore for **any** connected graph and any bond,
\[
\mu(F)=\frac{k\,\tau(G[S])\tau(G[T])}{2d\,\tau(G)}.\tag{1}
\]
The result uses (1) in a situation where every bond and its spanning-tree product can be classified.

**2. Cactus bonds.** Every bridge forms a bond, and every two distinct edges of a single cycle form a bond. Conversely, a bond of a cactus has precisely one of these forms. To see this, contract each 2-connected cycle block to a node in the block–cut tree, retaining its articulation attachments. If a minimal cut has a bridge, its deletion already disconnects the graph, so no second cut edge can be present. If it has no bridge, removing a set of cycle edges that disconnects the graph must remove at least two from some cycle, and removing any two already disconnects; minimality forces exactly those two from a single cycle. This also proves completeness without relying merely on the facet count.

For a bridge, deleting it separates the cactus into two connected subcacti whose cycles partition those of \(G\). Therefore \(\tau(G[S])\tau(G[T])=\prod_i\ell_i=\tau(G)\), and \(k=1\) in (1), giving \(\mu(F)=1/(2d)\).

For two removed edges from a cycle block of length \(\ell\), the two induced subcacti together contain every original cycle **except** that cut cycle; all other cycles are wholly inside one component. Thus \(\tau(G[S])\tau(G[T])=\tau(G)/\ell\), and \(k=2\) in (1), giving \(\mu(F)=1/(d\ell)\).

**3. Counts, normalization and characterization.** A bridge supplies one unoriented bond and hence two facets. A cycle of length \(\ell\) supplies \(\binom\ell2\) unoriented bonds and hence \(\ell(\ell-1)\) facets. Thus the sum of normalized cone volumes is
\[
\frac{2b}{2d}+\sum_i\frac{\ell_i(\ell_i-1)}{d\ell_i}
=\frac{b+\sum_i(\ell_i-1)}d=1.
\]
This proves the block mass identities. If only bridges occur, every mass equals \(1/(2d)\). If only cycles of one length \(\ell\) occur, every mass equals \(1/(d\ell)\). Conversely, a bridge mass cannot equal any cycle mass because \(\ell\ge3\), and two cycle masses are equal only when their lengths agree. The claimed necessary and sufficient condition follows.

## Verification
The included standalone program `checks/cactus_cone_volume_check.py` computes exact Kirchhoff tree counts and exact rational facet-cone-volume masses for eight cactus graphs (trees, single cycles with a bridge, equal and unequal cycle bouquets, chain attachments, and mixed cases). It checks every connected induced cut, the bond type, the theoretical counts, the total normalized mass and uniformity equivalence. For five examples it independently enumerates acyclic orientations, constructs the zonotope vertices and confirms the distinct facets by Euclidean convex hull. Run with Python 3 and `networkx`, `sympy`, `numpy`, `scipy` installed:

```bash
python checks/cactus_cone_volume_check.py
```

The finite computations corroborate the formulas for those graphs; the **proof for all connected cacti** is the bond classification and exact determinant computation above, not an extrapolation of the tests.

## Relationship to prior work
Padrol, Pilaud and Poullot, *Deformed graphical zonotopes* (first public November 24, 2021), develop the relevant graphical-zonotope face and deformation-cone framework. The standard spanning-tree volume identity and connected-cut facet description are used as established ingredients, not claimed as new. Henk and Linke, *Cone-volume measures of polytopes*, analyze cone-volume measures generally; that work motivates this Euclidean facet-cone invariant but does not supply the present cactus block spectrum. Blagojević, Breiding and Heaton, *Facet volumes of polytopes*, study the space of admissible facet-volume vectors, distinct from computing these specific centered cone masses.

The contribution here is the **simultaneous explicit cactus-wide mass formula, block allocation, and sharp uniform-facet-pyramid classification**, not a general theorem about graphical-zonotope facets and not a new proof of the spanning-tree identity.

## Limitations
The result assumes ordinary unweighted graph-incidence segments, the canonical Euclidean metric, and the symmetric center at zero. It does not assert equal facet **areas**, equivalent edge lengths, or uniform cone-volume masses for arbitrary graphs beyond cacti. The general graph-cut formula (1) is known in substance from standard zonotope and matrix-tree methods; these ingredients make independent historical priority assessment important. All graph sizes are proved mathematically, while the attached computational tests cover only specified finite instances.

## References
- Arnau Padrol, Vincent Pilaud, Germain Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422 (first posted 2021-11-24). https://arxiv.org/abs/2111.12422
- Martin Henk and Eva Linke, *Cone-volume measures of polytopes*, arXiv:1305.5335 (first posted 2013-05-23). https://arxiv.org/abs/1305.5335
- Pavle V. M. Blagojević, Paul Breiding, Alexander Heaton, *Facet volumes of polytopes*, arXiv:2112.08437 (first posted 2021-12-15). https://arxiv.org/abs/2112.08437
