# Sharp field thresholds and critical degeneracies of the snub-cube Ising antiferromagnet

## Finding
On the 24-vertex snub cubical graph with 60 edges, consider the zero-temperature classical Ising antiferromagnet
\[
H_{J,h}(\sigma)=J\sum_{\{u,v\}\in E(G)}\sigma_u\sigma_v-h\sum_{v\in V(G)}\sigma_v,
\qquad J>0,\quad h\in\mathbb R,\quad\sigma_v\in\{-1,+1\}.
\]
The exact ground energy, for \(b=|h|/J\), is
\[
E_{\min}/J=\begin{cases}-28,&0\le b\le1,\\-20-8b,&1\le b\le5,\\60-24b,&b\ge5.\end{cases}
\]
The ground-state multiplicities for the field ranges \(b=0\), \(0<b<1\), \(b=1\), \(1<b<5\), \(b=5\), \(b>5\) are respectively \(18,18,201,3,5302,1\). For \(h>0\), the ground-state total magnetizations are: \(0\) below the first threshold; \(0,2,4,6,8\) with respective multiplicities \(18,72,84,24,3\) at \(h=J\); \(8\) throughout \(J<h<5J\); and \(8,10,12,14,16,18,20,22,24\) at \(h=5J\), with respective multiplicities \(3,48,564,1680,1854,912,216,24,1\). For \(h>5J\) the sole ground state is fully polarized with magnetization \(24\). For \(h<0\), negate all magnetizations while leaving all multiplicities unchanged. These are finite-system zero-temperature level crossings, not thermodynamic phase transitions.

At the first critical field \(|h|=J\), all 201 ground states satisfy two geometric conditions: each of the 32 triangular faces is nonmonochromatic, and no edge of any of the six square faces joins two minority spins (relative to the field). At zero field the 18 ground configurations make all six square faces alternating. The \(5302\) configurations at saturation correspond to independent sets; their count is already implied by previously published snub-cubical independence-set data, and is included here as a necessary, explicitly credited boundary of the complete field diagram rather than an independent novelty claim.

## Assumptions and scope
The underlying graph is the edge graph of one chirality of the snub cube (snub cuboctahedron); the other chirality is graph-isomorphic. It has 24 vertices, 60 edges, degree five, 32 triangles, and six pairwise vertex-disjoint quadrilateral faces covering every vertex. In its exact Cartesian construction, let \(t\) be the real root greater than one of \(t^3=t^2+t+1\). Take permutations of the triple \((1,t^{-1},t)\) and independent signs, retaining the 24 triples in which the parity of positive signs equals the permutation parity. Join exactly those pairs with squared distance \(2+4t-2t^2\). The attached independent verifier builds this graph using exact arithmetic in \(\mathbb Z[t]/(t^3-t^2-t-1)\), not floating-point proximity.

For a spin assignment, define the negative-spin set \(S=\{v:\sigma_v=-1\}\), its size \(q=|S|\), total magnetization \(M=24-2q\), and \(C\) as the number of edges having opposite endpoint spins. Then \(H_{J,h}/J=60-2C-(h/J)(24-2q)\). By global spin reversal, it suffices to minimize at \(h\ge0\) with \(q\le12\): replacing a configuration with negative magnetization by its reversal never increases energy for positive field.

## Proof
**Incidence decomposition.** The exact graph construction shows 32 triangular faces. Of the 60 edges, 36 lie in two triangles and the remaining 24 lie in one triangle. These latter edges form six disjoint squares, so each vertex has precisely two square edges and three nonsquare edges. Denote cut edges of the two types by \(C_2\) and \(C_1\). Every Ising triangle has either zero or two cut edges. Counting cut incidences over the triangles gives
\[
2C_2+C_1\le 2\cdot32=64.
\]
Each square-edge cut has exactly one negative endpoint, and every negative vertex has two square edges, so \(C_1\le2q\). Consequently
\[
C=C_2+C_1\le32+\frac{C_1}{2}\le32+q.
\]
Counting the five incident edges at each negative vertex also gives the independent bound \(C\le5q\), with equality precisely when \(S\) is an independent set of the entire graph. Thus for \(0\le q\le12\),
\[
C\le \min\{5q,32+q\}.
\]
The two bounds cross at \(q=8\). Equality in the second bound is equivalent to all 32 triangles being nonmonochromatic and to the absence of two negative endpoints on any square edge.

**Sharp field envelope.** For \(b=h/J\ge0\), the preceding inequality bounds the energy from below, separately on \(q\le8\) and \(q\ge8\), by
\[
\frac{H_{J,h}}J\ge60-2\min\{5q,32+q\}-b(24-2q).
\]
This is affine in \(q\) on each segment and hence is minimized among \(q=0,8,12\). The three possible lower-bound values are \(60-24b\), \(-20-8b\), and \(-28\). The exact enumerations below establish configurations attaining each value at \(q=0,8,12\) respectively; therefore the lower envelope is the true ground energy for every \(b\). It changes branch only at \(b=1\) and \(b=5\). Strict affine slopes off those values show there are no additional ground-state magnetizations, while at the endpoints equality conditions characterize all coexisting configurations.

**Exact finite multiplicity certificates.** Every square has exactly seven subsets with no selected neighboring square vertices: the empty subset, four singletons and two opposite pairs. Consequently all candidates saturating \(C\le32+q\) are found in the exactly \(7^6=117649\) products of those seven local choices on the six disjoint squares. Keeping precisely those products on which every one of the 32 triangles has both signs gives the complete size histogram
\[
\#\{S:|S|=q,\ C=32+q\}=
\begin{cases}3,&q=8,\\24,&q=9,\\84,&q=10,\\72,&q=11,\\18,&q=12,\\0,&\text{otherwise}.
\end{cases}
\]
Their sum is \(201\); the \(q=12\) term yields all 18 zero-field ground states. The condition \(q=12\) and no adjacent negative square vertices forces precisely two opposite negatives per square, so every square alternates. For \(h=5J\), equality in \(C\le5q\) means \(S\) is an independent set of the whole graph. Filtering the same \(7^6\) candidates by every edge gives the exact size histogram \((1,24,216,912,1854,1680,564,48,3)\) in sizes \(q=0,\ldots,8\), totaling \(5302\). This second histogram matches independently published snub-cubical independence data and is not the novel part of the theorem.

**Independent exhaustive check.** A separate C++17 checker enumerates all \(2^{24}=16777216\) configurations by Gray code, updates their cut values from the exact 60-edge list, and compares the exact magnetization-resolved maximum cuts and multiplicities with the proposed values. This verification is finite and exhaustive. The analytical incidence inequality, not a finite numerical extrapolation, establishes the field dependence for all real \(h\) and all positive \(J\).

## Verification
Using Python 3 standard library only, run `python3 verify_snub.py`. It uses the cubic-number-field quotient to reconstruct the exact 24-vertex graph, checks every edge/triangle incidence and the six squares, then enumerates all \(7^6\) square-compatible candidate sets. The expected terminal output is `VERIFY_EXACT_OK 24_vertices 60_edges 32_triangles 6_squares critical_201 zero_18 saturation_5302`.

Compile the other independent implementation using `g++ -std=c++17 -O3 verify_exhaustive.cpp -o verify_exhaustive` and run `./verify_exhaustive`. This enumerates all \(16777216\) spin states and asserts each fixed-magnetization maximum cut/count. It ends with `VERIFY_EXHAUSTIVE_OK 16777216 configurations`. These programs require no external data or libraries. The proof's graph incidence properties and all final tables are fully reproducible from the attached programs.

## Relationship to prior work
Zhuang and Lannert, *Small-Network Approximations for Geometrically Frustrated Ising Systems* (arXiv:1107.2893v1; first public July 14, 2011), study **the same snub-cube Ising graph** and already observe that its square faces are unfrustrated in zero-field ground states. They compute the zero-field specific heat/partition function for comparison with the infinite triangular lattice. Their full article (especially Sections III, IV.3 and V) does **not** give the nonzero-field energy envelope, the two sharp field thresholds, the 201-state first-boundary census, or its magnetization breakdown. The present claim therefore does not assert the graph, its general frustration, or the unfrustrated-square observation as new; the distinctive contribution is the complete field-dependent classification and its sharp critical multiplicity.

The published October 2026 published-finding corpus *The snub cubical independence complex is a wedge of twenty-six four-spheres* lists 5301 nonempty independent sets and their size histogram on this same graph. It **does** already imply the saturation-boundary degeneracy \(5302\), after counting the empty set, so that part is explicitly credited and not proposed as independent novelty. The independence polynomial alone does not determine the nonzero-interior-field ground states, the 201-way coexistence at \(h=J\), or the zero-field exact minimum cut sector. The broader classical treatment of the 11 infinite two-dimensional Archimedean tilings by Yu (arXiv:1606.08191v1) concerns different, infinite graphs and does not imply the finite snub-cube field classification. General critical-field degeneracy on square/triangular lattices was studied earlier by Metcalf and Yang (1978), but those lattices and limits differ.

## Limitations
Only the finite classical, nearest-neighbor, uniform-coupling Ising graph with a uniform longitudinal field is considered. No finite-temperature singularity, infinite-volume limit, quantum-fluctuation effect, disorder robustness, or physical experimental threshold is inferred. The polynomial and coexisting configurations are exact finite counts, not a thermodynamic phase. An equivalent unindexed maximum-cut, magnetic independence, or complete-field Ising table for the same graph remains a historical-priority risk. An independent external scientific audit has not been performed.

## References
- B. Zhuang and C. Lannert, *Small-Network Approximations for Geometrically Frustrated Ising Systems*, arXiv:1107.2893v1 (first public July 14, 2011), https://arxiv.org/abs/1107.2893.
- U. Yu, *Ising antiferromagnet on the Archimedean lattices*, arXiv:1606.08191v1 (June 27, 2016), https://arxiv.org/abs/1606.08191.
- *The snub cubical independence complex is a wedge of twenty-six four-spheres*, public mathematical record (October 11, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-snub-cubical-independence-complex-is-a-wedge-of-twenty-six-f--d067ae207579.
- B. D. Metcalf and C. P. Yang, *Degeneracy of antiferromagnetic Ising lattices at critical magnetic field and zero temperature*, Phys. Rev. B 18 (1978), 2304, https://doi.org/10.1103/PhysRevB.18.2304.
- E. W. Weisstein, *Snub Cubical Graph*, MathWorld, https://mathworld.wolfram.com/SnubCubicalGraph.html.
