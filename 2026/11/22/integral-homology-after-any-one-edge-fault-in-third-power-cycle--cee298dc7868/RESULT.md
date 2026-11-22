# Integral homology after any one edge fault in third-power cycle neighborhood complexes

## Finding
For every integer \(n\ge13\), write \(G_n=C_n^{(3)}\) for the graph on \(\mathbb Z/n\mathbb Z\) with edges of cyclic distance \(1,2,3\). Let \(e\) be **any** graph edge and put
\[
X_n=\mathcal N(G_n),\qquad Y_{n,e}=\mathcal N(G_n-e),
\]
where \(\mathcal N\) is the **open** Lovász neighborhood complex. Then
\[
\widetilde H_j(Y_{n,e};\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=1,\\
\mathbb Z^2,&j=2,\\
0,&j\ne1,2.
\end{cases}
\]
More precisely, the natural inclusion \(Y_{n,e}\hookrightarrow X_n\) induces an isomorphism on integral first homology, and
\[
H_j(X_n,Y_{n,e};\mathbb Z)\cong
\begin{cases}\mathbb Z^2,&j=3,\\0,&j\ne3.\end{cases}
\]
For even \(n\), the fundamental integral three-class of \(X_n\) maps to a primitive rank-one subgroup of the relative \(\mathbb Z^2\). For odd \(n\), the relative \(\mathbb Z^2\) injects with index two into \(H_2(Y_{n,e};\mathbb Z)\). Thus every one-edge fault removes the top class in the even case and eliminates the order-two torsion in the odd case. **No homotopy-equivalence to a wedge of spheres is asserted.**

## Assumptions and scope
Graphs are finite, simple and undirected; all neighborhoods exclude their center. The vertex set is the residue ring \(\mathbb Z/n\mathbb Z\). The edge \(e\) has one of three cyclic-distance types \(d\in\{1,2,3\}\); by dihedral symmetry it suffices to delete \(\{0,d\}\). A face is a set of vertices contained in some six-element open neighborhood \(\{i-3,i-2,i-1,i+1,i+2,i+3\}\) before deletion; after deletion the neighborhoods of the two incident vertices lose one member each. Statements concern reduced **integral** simplicial homology and the homology of the indicated inclusion, not mod-two homology alone.

## Proof
**1. Known intact topology, and the chain-pair reduction.** The established sphere-bundle calculation for this exact six-regular circulant family gives \(X_n\simeq S^2\times S^1\) for even \(n\), and the mapping torus of a degree-minus-one self-homeomorphism of \(S^2\) for odd \(n\) [2,3]. Therefore \(H_1(X_n;\mathbb Z)=\mathbb Z\); the only other positive integral groups are \((H_2,H_3)=(\mathbb Z,\mathbb Z)\) for even \(n\), and \((\mathbb Z/2,0)\) for odd \(n\).

Set \(R_d=X_n\setminus Y_{n,\{0,d\}}\) (the set of removed faces, *not* a subcomplex). The relative simplicial chain groups have the following numbers of generators, independently of \(n\):

| Edge distance \(d\) | Degree 1 | Degree 2 | Degree 3 | Degree 4 | Degree 5 |
|---|---:|---:|---:|---:|---:|
| 1 | 0 | 8 | 18 | 10 | 2 |
| 2 | 0 | 6 | 16 | 10 | 2 |
| 3 | 2 | 10 | 18 | 10 | 2 |

Use the oriented simplicial differential, discard any boundary term belonging to \(Y\), and repeatedly cancel the first entry of magnitude one in the boundary matrices, processing dimensions from five downward and rows/columns in sorted face order. For a unit entry \(u\) in row \(i\), column \(j\), the remaining matrix is transformed by the exact integral Schur complement \(a_{rs}\mapsto a_{rs}-a_{rj}a_{is}/u\), omitting the canceled row and column, with induced corresponding chain-basis changes in adjacent degrees. There are respectively \(18,16,20\) such unimodular cancellations. In every case precisely **two degree-three free generators remain with zero differential**. The explicit face enumeration, signed matrices, cancellation steps, and \(\partial^2=0\) checks are reproducible in `verify.py`.

The relative calculation is genuinely uniform: all removed faces have integer lifts within \([-3,d+3]\). Possible common neighbors deciding their membership lie in a bounded window \([-6,d+6]\). For \(n\ge25\), no unintended modular identifications or additional common-neighbor coincidences occur, so the entire relative based chain complex is the same fixed signed-offset complex up to orientation signs. The twelve boundary cases \(13\le n\le24\) are checked separately by exact enumeration. Consequently the preceding integral cancellations establish \(H_3(X_n,Y_{n,e};\mathbb Z)=\mathbb Z^2\) and all other relative groups zero for **every** stated \(n\), not merely the tested orders.

**2. The faulted complex has vanishing degree-three integral homology and cohomology.** The published ten cyclic families of elementary collapses reducing \(X_n\) to the five tetrahedral templates
\[
(0,1,2,6),\ (0,1,5,6),\ (0,2,3,4),\ (0,2,4,5),\ (0,2,5,6)
\]
are applied to \(Y_{n,e}\) whenever both faces remain and the purported free face is still free [2]. All translations away from the deleted edge are unaffected. The finitely many exceptions are reconstructed explicitly by `verify.py`. After these operations, the following additional local free-face pairs complete the reduction to a three-dimensional complex (entries are integer offsets modulo \(n\)):

| \(d\) | Free face \(\sigma\) | Unique coface \(\tau\) |
|---|---|---|
| 1 | \((-2,2,4)\) | \((-2,2,3,4)\) |
| 2 | none | none |
| 3 | \((-3,-2,1,2)\) | \((-3,-2,-1,1,2)\) |
| 3 | \((1,4,6)\) | \((1,4,5,6)\) |
| 3 | \((-3,-2,1)\) | \((-3,-2,-1,1)\) |
| 3 | \((-2,-1,1)\) | \((-2,-1,1,2)\) |

The resulting complex \(K_{n,d}\) contains exactly \(5n-6\) tetrahedra. Each triangle is incident to at most two tetrahedra, and the number of triangles incident to exactly one is \(14,14,12\) for \(d=1,2,3\), respectively. The tetrahedral dual-adjacency graph is connected to these boundary triangles: every tetrahedron is reached from an exposed triangle by crossing shared triangular faces. These claims reduce to the five periodic tetrahedron templates away from a fixed defect window and finitely many local checks. In the periodic region, template types numbered \(0,\ldots,4\) have dual adjacencies
\[
0_i\!\sim\!1_i,1_{i+1},2_{i-2},4_i;\qquad
1_i\!\sim\!0_{i-1},0_i,3_{i+1},4_i;\qquad
2_i\!\sim\!0_{i+2},3_{i-2},3_i,4_{i-2},
\]
with the remaining edges given by symmetry or the five tetrahedral templates. In particular, the \(0_i,1_i\) cells form a consecutive backbone, and each other unaffected template connects to that backbone. The local exceptional cells also connect to its exposed-boundary component; for \(n\ge25\) this is a finite offset check followed by insertion of unaffected backbone periods, and for \(13\le n\le24\) it is checked directly. The verifier reconstructs the full dual graph for \(13\le n\le48\), checks each free-face operation and all local exceptional patterns; these finite runs supplement rather than replace the periodic-backbone argument.

For any finite three-complex having these two incidence properties, its top signed boundary \(\partial_3\) admits a full set of unit pivots: root a spanning tree of the tetrahedral dual graph at any exposed triangular face and eliminate tetrahedra away from that root. Thus \(\partial_3\) is injective and \(\partial_3^\mathsf T\) is surjective over \(\mathbb Z\). It follows that both \(H_3(K_{n,d};\mathbb Z)\) and \(H^3(K_{n,d};\mathbb Z)\) vanish. The elementary collapses give the same conclusion for \(Y_{n,e}\).

**3. Integral homology from exact sequences.** The long exact sequence of the pair, using the relative computation, gives \(H_1(Y_{n,e})\cong H_1(X_n)=\mathbb Z\) and an exact segment
\[
0\to H_3(X_n)\to\mathbb Z^2\to H_2(Y_{n,e})\to H_2(X_n)\to0,
\]
where \(H_3(Y_{n,e})=0\) by step 2. Universal coefficients identify the torsion subgroup of \(H_2(Y_{n,e})\) with \(\operatorname{Ext}(H_2(Y_{n,e}),\mathbb Z)\subseteq H^3(Y_{n,e};\mathbb Z)=0\). Hence \(H_2(Y_{n,e})\) is free. Its rank is exactly two in both parity cases: for even \(n\) the sequence is \(0\to\mathbb Z\to\mathbb Z^2\to H_2(Y)\to\mathbb Z\to0\); for odd \(n\) it is \(0\to\mathbb Z^2\to H_2(Y)\to\mathbb Z/2\to0\). All other reduced groups vanish. The same exact sequences yield the primitive-image and index-two conclusions. This proves the theorem.

## Verification
Run `python3 verify.py` with Python 3 standard library. It constructs both open-neighborhood complexes from first principles for each \(13\le n\le48\) and each of the three edge types; validates the integral relative chain condition \(\partial^2=0\), all unit cancellations, all prescribed elementary free-face collapses, and the exposed-boundary-connected dual graph. Independent exact mod-two elimination checks the final Betti ranks at selected orders. The script prints `VERIFY_OK` when every assertion succeeds. The mathematical extension beyond those orders uses the bounded local face patterns and the periodic dual-backbone argument in the proof, not numerical extrapolation.

## Relationship to prior work
Shukla's neighborhood-complex classification [1], first publicly posted in 2018, handles degree-at-most-three graphs and **four-regular** circulants, not this six-regular faulted family. The complete published intact-third-power calculation [2] supplies the five tetrahedral templates and parity-sensitive sphere-bundle topology; it has **no edge-deletion conclusion**. A broader published stable-cycle-power mapping-torus classification [3] subsumes the intact homotopy conclusion, but likewise assumes no missing edges. Neither determines relative homology or the disappearance of torsion after an edge fault. Related results on single faults in squared cycles and other graph families concern different complexes or different graph powers; their statements do not imply this all-order, all-three-orbits integral answer.

## Limitations
This is an integral homology and relative-homology classification, **not** an integral homotopy classification. A homotopy wedge splitting, the induced full \(\pi_1\) map, and behavior under multiple simultaneous faults are not established. No assertion is made for \(n<13\). The dual-backbone proof uses an explicit finite local verification and a periodic extension, not an external infinite proof checker. Literature discovery cannot rule out every unindexed equivalent theorem. There has been no independent scientific audit.

## References
[1] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first public 2018-02-13; *Electron. J. Combin.* 26 (2019), P2.4. https://arxiv.org/html/1802.04526v2

[2] *Third-power cycle neighborhood complexes collapse to parity-twisted sphere bundles*, public mathematical research record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-third-power-cycle-neighborhood-complexes-collapse-to-parity-twis--5e7bfbfa5a7e

[3] *Sphere mapping-tori in neighborhood complexes of every stable cycle power*, public mathematical research record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sphere-mapping-tori-in-neighborhood-complexes-of-every-stable-cy--a2339801b688
