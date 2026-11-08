# Magnetic fingerprints of two cospectral sixteen-site Potts antiferromagnets

## Finding

The Shrikhande graph and the four-by-four rook graph have identical strongly regular parameters \((16,6,2,2)\), and hence identical adjacency spectra, but their three-state antiferromagnetic Potts models have different **complete** zero-temperature magnetic-field diagrams.

For either graph \(G\), put a spin \(\sigma_v\in\{0,1,2\}\) on every vertex and define, for \(J>0\) and arbitrary real \(h\),
\[
H_G(\sigma)=J\sum_{\{u,v\}\in E(G)}\mathbf1_{\sigma_u=\sigma_v}-h\sum_{v\in V(G)}\mathbf1_{\sigma_v=0},\qquad x=h/J.
\]
The normalized ground-state energies are exactly
\[
\begin{aligned}
E_R(h)/J&=\min\{16,\ 8-4x,\ 8-8x,\ 24-12x,\ 48-16x\},\\
E_S(h)/J&=\min\{16,\ 6-4x,\ 6-6x,\ 8-8x,\ 15-10x,\ 24-12x,\ 48-16x\}.
\end{aligned}
\]
Here \(R\) is the rook graph and \(S\) is the Shrikhande graph. The rook graph's critical fields are \(x=-2,0,4,6\), while the Shrikhande graph's are \(x=-5/2,0,1,7/2,9/2,6\). In each open field interval, the unique ground-state favored-color occupancy is the slope's negative; in order of increasing field these occupancies are \(0,4,8,12,16\) for \(R\) and \(0,4,6,8,10,12,16\) for \(S\).

The exact ground-state degeneracies on these open intervals are, respectively,
\[
D_R=(90,10800,216,384,1),\qquad D_S=(42,96,192,96,256,256,1).
\]
At the ordered critical fields, where the competing sectors coexist, the exact total degeneracies are
\[
D_R^{\rm crit}=(46170,90936,11352,1473),\qquad
D_S^{\rm crit}=(138,288,288,352,512,1345).
\]
In particular, at zero field the rook model has monochromatic-edge minimum \(8\) and degeneracy \(90936\); the Shrikhande model has minimum \(6\) and degeneracy \(288\). Thus even their lowest-energy interaction costs, not merely their magnetic responses, differ despite identical adjacency spectra.

## Assumptions and scope

Both graphs have the common vertex set \(V=\mathbb Z_4\times\mathbb Z_4\), with coordinates represented by \(0,1,2,3\). For \(R\), distinct \((a,b)\) and \((c,d)\) are adjacent when \(a=c\) or \(b=d\). For \(S\), they are adjacent exactly when their difference modulo four belongs to
\[
\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}.
\]
Each graph is finite, simple, undirected, and has exactly 16 vertices and 48 edges. Colors are **labeled**. Degeneracy counts individual labeled spin assignments without quotienting by color permutation or graph automorphism. The field singles out color zero; the other two colors remain exchangeable. Energies count equal-spin bonds once, with **positive** antiferromagnetic penalty \(J\). Critical-field degeneracies count all minimizers including intermediate collinear sectors. These are finite-cluster level crossings, not thermodynamic phase transitions.

## Proof

**1. Cospectrality and an independent structural lower bound.** Directly checking the neighbor rules shows every vertex of either graph has six neighbors and every pair of distinct vertices has exactly two common neighbors. If \(A\) is either adjacency matrix, then \(A^2=4I+2\mathbf J\). The all-ones vector has eigenvalue six. The remaining 15 dimensions split into eigenvalues \(2\) (multiplicity six) and \(-2\) (multiplicity nine), because the trace of \(A\) is zero. Hence both have spectrum \(6^1 2^6 (-2)^9\).

For any color partition into three classes of sizes \(n_0,n_1,n_2\), let \(z_c\) be its color-indicator vector. By the lower bound \(-2\) on the spectrum orthogonal to the all-ones vector,
\[
\begin{aligned}
B(\sigma)&=\frac12\sum_{c=0}^2z_c^{\mathsf T}Az_c\\
&\ge\frac12\sum_{c=0}^2\left(\frac{6n_c^2}{16}-2\left(n_c-\frac{n_c^2}{16}\right)\right)
=\frac14\sum_{c=0}^2 n_c^2-16.
\end{aligned}
\]
Since \(n_0+n_1+n_2=16\), the minimum possible sum of squares is 86, so the integer bond cost is at least six. A Shrikhande configuration with exactly six equal-color bonds, given as the following rows in coordinate order, attains this bound:

```text
0 1 0 2
1 2 1 2
1 0 2 0
2 2 1 1
```

It has color sizes \(4,6,6\). By contrast, every row and every column in the four-by-four rook graph induces a \(K_4\). A three-coloring of each \(K_4\) has at least one monochromatic edge. The four row-cliques and four column-cliques have pairwise edge-disjoint edge sets, giving \(B\ge8\). Equality is witnessed by

```text
0 1 1 2
1 0 1 2
1 1 2 0
2 2 0 1
```

Thus the spectral lower bound is sharp on \(S\) but not on its cospectral partner \(R\).

**2. Complete finite certificate for all magnetic fields.** For any vertex subset \(U\), write \(b_G(U)\) for the number of graph edges with both endpoints in \(U\). A coloring corresponds uniquely to an *ordered* triple of disjoint subsets \((S,T,R')\) partitioning \(V\), for colors zero, one and two. Consequently, the exact joint bond-and-occupancy polynomial is
\[
P_G(z,w)=\sum_{S\subseteq V}\sum_{T\subseteq V\setminus S}
 z^{b_G(S)+b_G(T)+b_G(V\setminus(S\cup T))}w^{|S|}.
\]
Define \(m_{G,k}\) to be the smallest exponent of \(z\) in the coefficient of \(w^k\), and \(d_{G,k}\) the coefficient at that smallest exponent. The complete exact values, in order \(k=0,1,\ldots,16\), are:

| \(k\) | \(m_{R,k}\) | \(d_{R,k}\) | \(m_{S,k}\) | \(d_{S,k}\) |
|---:|---:|---:|---:|---:|
| 0 | 16 | 90 | 16 | 42 |
| 1 | 14 | 1440 | 14 | 672 |
| 2 | 12 | 10224 | 12 | 10608 |
| 3 | 10 | 23616 | 9 | 1792 |
| 4 | 8 | 10800 | 6 | 96 |
| 5 | 8 | 44640 | 7 | 3072 |
| 6 | 8 | 30096 | 6 | 192 |
| 7 | 8 | 5184 | 8 | 3456 |
| 8 | 8 | 216 | 8 | 96 |
| 9 | 12 | 2112 | 12 | 1408 |
| 10 | 16 | 5184 | 15 | 256 |
| 11 | 20 | 3456 | 20 | 3456 |
| 12 | 24 | 384 | 24 | 256 |
| 13 | 30 | 768 | 30 | 768 |
| 14 | 36 | 288 | 36 | 288 |
| 15 | 42 | 32 | 42 | 32 |
| 16 | 48 | 1 | 48 | 1 |

These integers result from **two separate exact exhaustive algorithms** included with this result. `verify_subsets.cpp` uses the displayed class-partition identity and recursively precomputes every \(b_G(U)\) using
\[
b_G(U)=b_G(U\setminus\{v\})+|N(v)\cap(U\setminus\{v\})|.
\]
It then visits every ordered disjoint pair \((S,T)\). Independently, `verify_recursive.cpp` assigns one labeled color to each of the 16 vertices in order and increases the bond cost only when a newly colored endpoint matches a previously colored neighbor. Both visit exactly \(3^{16}=43,046,721\) configurations per graph, check every color-zero sector, and reproduce the same `expected.tsv` bytes. Both also check the strongly regular parameters and the total assignment count. Thus every minimum and its degeneracy is a finite exhaustive identity, not a sampling estimate or an infinite extrapolation.

**3. Lower envelopes and coexistence.** At any real \(x=h/J\), the ground state minimizes \(m_{G,k}-xk\) over all \(0\le k\le16\). Taking the lower convex hull of the 17 certified points \((k,m_{G,k})\) gives the rook vertices
\[
(0,16),(4,8),(8,8),(12,24),(16,48),
\]
and the Shrikhande vertices
\[
(0,16),(4,6),(6,6),(8,8),(10,15),(12,24),(16,48).
\]
Successive slopes give precisely the critical-field lists in the finding. On an open interval, only its hull vertex minimizes; the degeneracy is \(d_{G,k}\). At a critical slope, every certified point on the supporting line contributes. Summing its listed \(d_{G,k}\) proves the critical degeneracies stated above, including the collinear intermediate occupancies at \(x=-2,0,4,6\) for \(R\) and at \(x=6\) for \(S\).

## Verification

The package contains `verify_recursive.cpp`, `verify_subsets.cpp`, `expected.tsv`, and `verify.py`. With a C++20 compiler and Python 3.9 or newer, run `python verify.py` in the directory containing these files. Both independent implementations compile, exhaust all labeled configurations for both graphs, and exactly match all 34 sector records in `expected.tsv`. They terminate successfully with equality checks on the 48-edge, degree-six, two-common-neighbor geometry, and the total \(3^{16}\) assignment count. The reported witness matrices can additionally be checked edge-by-edge against the displayed graph rules. No external data files, numerical tolerances, floating-point arithmetic, or independent validation are required for this finite theorem.

## Relationship to prior work

The original Shrikhande graph and the four-by-four rook graph are the classical exceptional pair with the same strongly regular parameters. Their graph-theoretic and spectral relationship is established literature, not new here. Shrock and Xu (arXiv:1009.1182, 2010, particularly Sections I, XI and XII) developed exact general field-dependent Potts partition functions and discussed distinguishing graph pairs, including tree examples. Klazar, Loebl and Moffatt (arXiv:1311.4348, 2013, Section 1 and Section 3) established equivalences involving the general bad-coloring polynomial, which implicitly encodes all finite-graph bond/color statistics. These general frameworks do **not** constitute a prior explicit calculation of the above 17-by-two sector table, the two different magnetic level-crossing lists, or the spectral-bound sharpness separation for the named graph pair. A general state sum is an available method, not an assertion that this particular evaluation is historically new; priority beyond the examined primary texts and database results remains uncertain.

## Limitations

The finding is a complete, exact calculation only for two named 16-vertex graphs, for exactly three labeled colors, uniform positive coupling and a uniform field favoring color zero. It neither implies a thermodynamic transition nor proves anything for larger Doob graphs or arbitrary cospectral strongly regular pairs. A general graph polynomial could contain the same coefficients in an existing unindexed evaluation or table; no claim of comprehensive historical uniqueness is made. The self-review found the result correct, original on the examined evidence, and valuable as a natural two-graph field-response benchmark; independent audit has not been performed.

## References

- R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, arXiv:1009.1182v1 (first public 2010-09-07), https://arxiv.org/abs/1009.1182.
- M. Klazar, M. Loebl and I. Moffatt, *The Potts model and chromatic functions of graphs*, arXiv:1311.4348v1 (first public 2013-11-18), https://arxiv.org/abs/1311.4348.
- S.-C. S. Shrikhande, *The uniqueness of the \(L_2\) association scheme*, *Annals of Mathematical Statistics* **30** (1959), 781–798, https://doi.org/10.1214/aoms/1177706207.
- A. E. Brouwer, *Shrikhande graph*, graph reference (definition, spectrum and comparison), https://jaanos.github.io/tables/graphs/Shrikhande.html.
- E. W. Weisstein, *Shrikhande Graph*, MathWorld (graph/spectrum background), https://mathworld.wolfram.com/ShrikhandeGraph.html.
