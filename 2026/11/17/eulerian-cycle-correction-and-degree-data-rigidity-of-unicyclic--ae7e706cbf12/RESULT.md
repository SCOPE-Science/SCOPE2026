# Eulerian-cycle correction and degree-data rigidity of unicyclic zonotope vertex radii

## Finding
Let \(G=(V,E)\) be a finite, connected, simple unicyclic graph, with \(n=|V|=|E|\geq3\), and let \(C\subseteq V\) be its unique cycle of length \(c\geq3\). Form the **centered Euclidean graphical zonotope**
\[
Z_G=\sum_{\{u,v\}\in E}\left[-\frac{e_u-e_v}{2},\frac{e_u-e_v}{2}\right]\subset\mathbb R^V.
\]
Its complete **vertex-radius generating polynomial** is \(R_G(z)=\sum_{x\in\operatorname{Vert}(Z_G)}z^{4\|x\|_2^2}\); the coefficient at \(z^j\) is exactly the number of vertices at squared Euclidean radius \(j/4\).

For nonnegative integers \(d\), set
\[
F_d(z)=2^{-d}\sum_{j=0}^d\binom dj z^{(d-2j)^2},
\]
and for \(d\geq2\), set
\[
B_d(z)=2^{-(d-1)}\sum_{j=0}^{d-2}\binom{d-2}{j}
\left(z^{(d-2j)^2}-z^{(d-2-2j)^2}\right).
\]
Write \(d_v=\deg_G(v)\). Then **for every such graph**, with no restriction on its attached trees,
\[
\boxed{
R_G(z)=\left(\prod_{v\notin C}F_{d_v}(z)\right)
\left[
2^n\left(\prod_{v\in C}F_{d_v}(z)+(-1)^c\prod_{v\in C}B_{d_v}(z)\right)
-2^{n-c+1}\prod_{v\in C}F_{d_v-2}(z)
\right].
}
\]
This is an integer-coefficient polynomial despite the rational intermediate factors. Its value at \(z=1\) is \(2^{n-c}(2^c-2)\), the exact number of vertices.

**Degree-data rigidity:** the full Euclidean radius spectrum depends only on the cycle length \(c\), the **multiset of degrees on the cycle**, and the **multiset of degrees off the cycle**. It depends neither on their cyclic order nor on how the attached trees are arranged. In particular, the two nonisomorphic six-vertex graphs obtained from a four-cycle by attaching one leaf at each of two adjacent cycle vertices, respectively at each of two opposite cycle vertices, have the same exact radius polynomial
\[
2z^4+16z^8+14z^{12}+16z^{16}+6z^{20}+2z^{28}.
\]
They are nonisomorphic because their two degree-three vertices are adjacent in one graph but at distance two in the other.

## Assumptions and scope
All graphs are finite, simple, unweighted, connected, and unicyclic. The Euclidean metric is inherited from the orthonormal coordinate vectors \(e_v\) of \(\mathbb R^V\); the factor \(1/2\) in every generating segment fixes the normalization. The unique cycle has length \(c\), and the graph has \(n\) vertices and exactly \(n\) edges. A product over an empty set equals one. The formulas enumerate **vertices**, not uniformly sampled points in the body or its intrinsic volume. No statement about arbitrary multicyclic graphs follows from the displayed product formula.

## Proof
**1. Orientations and coordinate norms.** Fix an arbitrary reference direction for each edge. Assign a sign \(\sigma_e\in\{-1,1\}\). The corresponding segment-end sum \(x(\sigma)\) has coordinates \(2x_v=\sum_{e\ni v}\eta_{v,e}\sigma_e\), where \(\eta_{v,e}=1\) at the reference head and \(-1\) at the tail (the choice of which endpoint is head does not affect the argument). Thus \(4\|x\|_2^2=\sum_v(\sum_{e\ni v}\eta_{v,e}\sigma_e)^2\). The usual graphical-hyperplane-arrangement correspondence identifies the distinct vertices of the zonotope bijectively with acyclic orientations. In a unicyclic graph the only excluded sign configurations are those with its unique cycle oriented coherently in either of the two directions; there are \(2^{n-c+1}\) such edge-sign assignments.

**2. An exact even-subgraph identity.** For every vertex \(v\), expand the function \(h_v(\sigma)=z^{(\sum_{e\ni v}\eta_{v,e}\sigma_e)^2}\) in the Walsh basis on the incident edge signs. The identity \(h_v(-\sigma)=h_v(\sigma)\) makes all odd-cardinality Walsh coefficients zero. Independence and uniform averaging over edge signs make the product \(\prod_vh_v\) retain only selections in which each edge is selected at either both ends or neither. Hence the surviving selected edges form an **even-degree subgraph**. A connected unicyclic graph has only two even-degree spanning edge subsets: the empty set and its unique cycle.

For the empty subset at \(v\), the local average is \(F_{d_v}(z)\). For a cycle vertex, the coefficient selecting its two incident cycle edges is \(\eta_{v,e_1}\eta_{v,e_2}B_{d_v}(z)\): conditioned on the other \(d_v-2\) independent edge signs, the two selected signs contribute half the difference between a shifted square and an unshifted square. Explicitly this is the displayed formula for \(B_{d_v}\). Every selected cycle edge has opposite incidence signs at its endpoints, so multiplication of these incidence factors contributes \((-1)^c\). Therefore the sum over **all** \(2^n\) edge-sign assignments is exactly
\[
2^n\left(\prod_{v\in V}F_{d_v}(z)+(-1)^c
\prod_{v\in C}B_{d_v}(z)\prod_{v\notin C}F_{d_v}(z)\right).
\]

**3. Remove precisely the nonvertices.** If the cycle is coherently directed, its two incident edge signs cancel in the coordinate sum at each cycle vertex. The remaining edges form a forest with vertex degrees \(d_v-2\) on \(C\), and \(d_v\) off \(C\). Applying the empty-even-subgraph calculation to that forest gives \(2^{n-c}\prod_{v\in C}F_{d_v-2}(z)\prod_{v\notin C}F_{d_v}(z)\) for each prescribed coherent direction. There are two directions. Subtracting their contributions from the all-assignments formula proves the displayed identity.

**4. The rigidity and counterexample.** Every factor in the formula depends only on the degree of its vertex and whether it belongs to the cycle. Multiplication is commutative, establishing the claimed complete radial invariance. For the displayed two graphs, the cycle-degree multiset is \(\{3,3,2,2\}\) and the off-cycle multiset is \(\{1,1\}\). Their two degree-three vertices have different graph distances, hence the graphs are nonisomorphic, while substitution yields the identical polynomial shown. Finally, \(F_d(1)=1\) and \(B_d(1)=0\), which gives the stated vertex count and completes the proof.

## Verification
The included standalone Python 3 checker `check_radial.py` uses only the standard library. Run `python check_radial.py` from the extracted package directory. It independently enumerates directed edge-sign assignments, rejects directed cycles, computes integer squared signed-degree lengths directly, and compares exact shell counts to the rational generating-polynomial formula. It verifies 2,500 attached-tree configurations and 1,168,282 actual zonotope vertices, and separately compares the two six-vertex nonisomorphic graphs. Completion marker: `UNICYCLIC_RADIAL_PASS`. These finite tests corroborate the unrestricted proof but do not replace it.

## Relationship to prior work
The acyclic-orientation/vertex correspondence is classical; see Grujić and Padrol–Pilaud–Poullot. Grujić (2016) computes the face polynomial, including cycles and wedge decompositions, not Euclidean vertex-radius multiplicities. Padrol–Pilaud–Poullot (first posted 2021) study deformation cones, rather than the degree-data collapse of Euclidean vertex-radius spectra. Previously available tree radial-spectrum results depend on degree multiset, but trees have no nonempty even edge subset and thus do not furnish this unicyclic correction. Prior geometric results concerning cycle-zonotope intrinsic volumes and unicyclic Löwner ellipsoids address distinct invariants; neither logically yields this entire discrete radial distribution. The Walsh/Eulerian-subgraph device itself is standard; the unicyclic specialized identity, subtraction of the two excluded orientations, and degree-data rigidity are the claims examined here.

## Limitations
This is a complete result for the specified unweighted unicyclic family only; it is not a classification of Euclidean congruence, nor a uniqueness criterion for graph reconstruction. The two-degree-multiset data are sufficient for equal spectra, not claimed necessary. The formula does not describe continuous volume-radius distributions. Earlier equivalent results under Fourier expansions, random-orientation energy or geometric zonotope nomenclature may exist; historical priority has not been independently established. Independent mathematical audit has not been performed.

## References
- Arnau Padrol, Vincent Pilaud, Germain Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422 (first public version 2021-11-24), https://arxiv.org/abs/2111.12422 ; published in *Discrete & Computational Geometry* 73 (2025), 447–465, DOI:10.1007/s00454-023-00586-x. The relevant mathematical background is the normal fan and acyclic-orientation correspondence.
- Vladimir Grujić, *Counting faces of graphical zonotopes*, arXiv:1604.06931 (first public version 2016-04-23), https://arxiv.org/abs/1604.06931. Relevant portions: Sections 1–2 and 4–5, including the cycle face-polynomial calculation.
