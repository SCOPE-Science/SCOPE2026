# Unlabeled Euclidean distances reconstruct every simple-graph cosmological polytope

## Finding

**Theorem (complete midpoint classes and metric reconstruction).** Let \(G=(V,E)\) be any finite undirected simple graph with no isolated vertices and \(m=|E|\ge1\), possibly disconnected. Its standard Euclidean cosmological polytope \(P_G\) has the \(3m\) vertices defined below. From **only the unlabeled matrix of squared Euclidean distances between those vertices**, one can reconstruct \(G\) up to graph isomorphism using \(O(m^3)\) arithmetic and exact-equality operations. Neither coordinates, faces, facet incidences, nor the ambient space are supplied to the reconstruction algorithm.

More precisely, among unordered pairs of distinct polytope vertices, every equal-midpoint class of cardinality greater than one is uniquely associated with a graph vertex \(v\) of degree \(d_v\ge2\); the class has exactly \(d_v\) pairs. There are no other repeated-midpoint classes. Two classes intersect in a polytope vertex exactly when their graph vertices are adjacent, and a pair with no member in another class identifies a pendant edge. The remaining edge count identifies all isolated \(K_2\) components.

In particular, for graphs in this domain, the standard cosmological polytopes \(P_G\) and \(P_H\) are intrinsically Euclidean-congruent if and only if \(G\cong H\). The condition excluding isolated graph vertices is necessary for the traditional \(3m\)-generator definition: adding isolated graph vertices does not change that point cloud.

## Assumptions and scope

For each edge \(e=\{u,v\}\), let \(x_w\) (\(w\in V\)) and \(y_f\) (\(f\in E\)) be **mutually orthonormal** standard basis vectors of \(\mathbb R^{|V|+m}\). Define
\[
 p_e=x_u+x_v-y_e,\qquad p_{e,u}=x_u-x_v+y_e,\qquad p_{e,v}=x_v-x_u+y_e.
\]
The polytope is the convex hull of all \(p_e,p_{e,u},p_{e,v}\) over the edges. The vertex assertion and this conventional realization are those of the foundational literature. All the points lie in the affine hyperplane where the coordinate sum is one; distances and congruence are intrinsic to that affine hull. No genericity, regularity, connectivity, or graph-size bound is imposed beyond finite simplicity, absence of isolated graph vertices, and at least one edge.

## Proof

**1. Complete repeated-midpoint classification.** For one edge \(e=\{u,v\}\), its three distinct unordered generator pairs have the following sums:
\[
 p_e+p_{e,u}=2x_u,\qquad p_e+p_{e,v}=2x_v,\qquad p_{e,u}+p_{e,v}=2y_e.
\]
Thus every graph vertex \(v\) has an equal-midpoint class \(\mathcal C_v\) comprising exactly the \(d_v\) pairs \(\{p_e,p_{e,v}\}\) over incident edges. A class is repeated precisely for \(d_v\ge2\).

We show these exhaust all collisions. If a pair of polytope vertices comes from two **different** edges \(e\ne f\), its \(y\)-coordinate support is exactly \(\{e,f\}\), with each coordinate equal to \(+1\) or \(-1\). This distinguishes its sum from all within-edge sums, and fixes the two contributing edge labels and their \(y\)-signs. For a fixed edge with \(y_e=-1\), there is only one possible vertex \(p_e\). For \(y_e=+1\), the two choices \(p_{e,u}\), \(p_{e,v}\) differ by \(2(x_u-x_v)\). Therefore two distinct cross-edge selections with equal sums would imply \(\pm(x_u-x_v)=\pm(x_s-x_t)\) for the distinct edges \(e=\{u,v\}\) and \(f=\{s,t\}\). Linear independence of the vertex-coordinate basis then forces \(e=f\), a contradiction. All cross-edge sums are distinct, and the within-edge sums \(2y_e\) occur once. Hence the repeated classes are exactly \(\mathcal C_v\) for \(d_v\ge2\).

**2. Incidence and the missing leaves.** The class \(\mathcal C_v\) consists of disjoint pairs. Every generator \(p_e\) belongs to the pair of \(\mathcal C_u\) and the pair of \(\mathcal C_v\) when those classes exist; \(p_{e,u}\) belongs only to \(\mathcal C_u\), and \(p_{e,v}\) only to \(\mathcal C_v\). Consequently distinct classes \(\mathcal C_u,\mathcal C_v\) have exactly one common polytope vertex if \(uv\in E\), and no common vertex otherwise. This recovers all edges between vertices of degree at least two.

For each pair in \(\mathcal C_v\) neither of whose endpoints belongs to another repeated-midpoint class, its edge has one endpoint \(v\) of degree at least two and the other of degree one. Conversely each such pendant edge contributes exactly one such pair; attach a new leaf. There cannot be an edge between two unknown degree-one vertices except an isolated \(K_2\) component. As \(m\) is one third the number of input polytope vertices, the number of these components is the number of unaccounted edges. If there are no repeated classes, the entire graph is a disjoint union of \(K_2\) components. This recovers \(G\) canonically up to vertex relabeling.

**3. Extract classes from squared distances alone.** Let \(q_1,\ldots,q_{3m}\) be the unlabelled vertex set, and \(D_{ij}=\|q_i-q_j\|^2\). For an unordered pair \(\{i,j\}\), form the signature
\[
 \sigma_{ij}(k)=2D_{ik}+2D_{jk}-D_{ij}
 =4\left\|\frac{q_i+q_j}{2}-q_k\right\|^2,
 \qquad 1\le k\le3m.
\]
Equal midpoints have equal signatures. Conversely if two signatures agree, the corresponding midpoints are equidistant from every \(q_k\). Subtracting squared-distance equalities at any fixed \(q_1\) shows that the difference between midpoints is orthogonal to every \(q_k-q_1\). It also lies in the span of these differences; it therefore vanishes. Thus signature equality is **equivalent** to midpoint equality. Forming all \(\binom{3m}{2}\) signatures costs \(O(m^3)\) exact arithmetic operations, and grouping them recovers all classes and the incidence data of Step 2 without coordinates or convex-hull computations. This proves the algorithm and complexity.

**4. Congruence.** An intrinsic Euclidean isometry of two polytopes sends vertices bijectively to vertices and preserves all their distances, so it induces an isomorphism of their reconstructed graphs. Conversely every graph isomorphism permutes the mutually orthonormal \(x\)- and \(y\)-coordinates, mapping all generators of \(P_G\) to those of \(P_H\) by an orthogonal map. The polytopes are congruent.

## Verification

The standalone \(CHECKER.py\) constructs the canonical integer-coordinate vertices and then **discards coordinates** before reconstruction, retaining only the integral squared-distance matrix. It checks every simple graph without isolated vertices on two through five labeled vertices (814 cases) and 157 additional seeded random cases on six through eight vertices, including disconnected configurations and multiple \(K_2\) components. It verifies graph isomorphism using an independently coded backtracking comparison. The checker completes with `COSMO_METRIC_GRAPH_RECONSTRUCTION_PASS exhaustive=814 random=157`.

These finite tests are consistency checks, not proof of the theorem for arbitrary graph sizes; Steps 1–4 supply that proof.

## Relationship to prior work

Arkani-Hamed, Benincasa and Postnikov (2017) introduced cosmological polytopes by joining triangle midpoints, and explicitly noted **some** equal-midpoint relations between their generators. These observations are foundational and are *not* claimed as new. Kühne and Monin (2022) identified vertex faces as cross-polytopes centered at graph-vertex coordinates and determined the combinatorial face structure. Lavrov (2025) placed the same realization in the general setting of ternary-relation polytopes. Birkemeyer and collaborators (2026) established dual and canonical-form descriptions.

The result proved here is narrower in objects but stronger in its **unlabeled input and algorithmic conclusion**: it classifies *all* equal-midpoint pair collisions, excludes extraneous collisions, recovers leaves and separate \(K_2\) components, and gives polynomial exact reconstruction directly from the vertex-distance matrix, without an input decomposition into triangles, a graph labeling, or the polytope's face lattice. This does not assert that generic polytope embeddings or arbitrary ternary-relation polytopes have the same rigidity.

## Limitations

Input distances must be exact and known to come from the specified canonical Euclidean realization; the result gives no stability guarantee for noisy distances or arbitrary affine/diagonal deformations. It does not cover loops, parallel edges, or isolated graph vertices, and it does not claim graph recovery from the **multiset** of distances without the pairwise incidence indices. Historical priority of the metric-only algorithm has not been independently certified; in particular, a graph-inverse consequence implicit in earlier combinatorial descriptions is a plausible literature-interpretation risk.

## References

- N. Arkani-Hamed, P. Benincasa, A. Postnikov, *Cosmological Polytopes and the Wavefunction of the Universe* (first public 2017-09-08), arXiv:1709.02813, especially Section 3 and Section 5.
- L. Kühne, L. Monin, *Faces of Cosmological Polytopes* (first public 2022-09-16), arXiv:2209.08069, especially Definition 1.1 and Proposition 3.5.
- A. Lavrov, *Ternary relations and their polytopes* (first public 2025-09-08), arXiv:2509.06811, Sections 1–2.
- A. Birkemeyer, T. Donzelmann, M. Fink, M. Juhnke, *On cosmological polytopes, their canonical forms and their duals* (first public 2026-03-04), arXiv:2603.03894.
