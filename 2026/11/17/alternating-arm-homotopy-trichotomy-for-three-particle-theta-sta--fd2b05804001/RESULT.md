# Alternating-arm homotopy trichotomy for three-particle theta state complexes

## Finding
For every integer \(m\geq3\), let \(\Theta_m^{[4]}\) be the graph consisting of two distinct poles joined by \(m\) internally vertex-disjoint paths, each having four edges. Let \(D_3(\Theta_m^{[4]})\) be the **unordered Abrams cubical discretized configuration space** of three particles: a \(k\)-cell is an unordered triple of open vertices or edges, with exactly \(k\) edges and pairwise disjoint closures. The alternating group \(A_m\) permutes the paths and fixes both poles. Its ordinary geometric orbit space satisfies

\[
\boxed{
\left|D_3(\Theta_m^{[4]})\right|/A_m\simeq
\begin{cases}
S^1,&m=3,\\
S^2,&m=4,\\
\{\mathrm{point}\},&m\geq5.
\end{cases}}
\]

In particular, the parity-preserving arm-quotient changes from a circle to a sphere and then becomes contractible at the sharp threshold of five arms. The theorem is about the specified **compact cubical** state complexes and their actual orbit spaces, not merely rational homology or a presumed equivariant deformation retraction of unrestricted continuous configuration spaces.

## Assumptions and scope
The graph has two distinct vertices \(P,Q\), and on arm \(a\in\{0,\ldots,m-1\}\) three distinct internal vertices \(v_{a,1},v_{a,2},v_{a,3}\) and four edges \(e_{a,j}\) with \(j\in\{0,1,2,3\}\). The endpoints of an edge are the vertices at positions \(j\) and \(j+1\), with positions zero and four identified with \(P\) and \(Q\) across all arms. A configuration cell is exactly an unordered triple of cells in the graph whose closed supports are pairwise disjoint. The action does not swap \(P\) and \(Q\) or label the particles; \(A_3\) is the cyclic group of order three. All quotients are **ordinary geometric** orbit spaces, not homotopy/Borel quotients.

## Proof
**1. A regular equivariant cell model.** Each configuration cell is a product of at most three graph edges and remaining vertices, so it is a cube. Its immediate faces are obtained by replacing any selected edge by one of its endpoints, subject to disjoint closure. This gives the entire finite face poset. Barycentric subdivision turns each strict chain \(c_0<\cdots<c_d\) of cells into a simplex. Arm permutations preserve cell rank, hence any element stabilizing one chain fixes each member and its barycentric vertices. Consequently, the geometric quotient is described without a freeness hypothesis by **orbits of strict face chains**, with the inherited alternating simplicial incidences. This description also allows distinct orbit simplices to have the same endpoint orbits; the enumeration retains simplices as *chain orbits*, not merely as sets of orbit vertices.

**2. Finite elementary-collapse certificates.** The accompanying standalone verifier explicitly generates the graph, all valid configuration cells, all face relations, the complete face chains, and their orbits under the requested finite permutation group. It then repeatedly chooses a codimension-one face with exactly one remaining coface and deletes that face together with its coface. Each deletion is a valid elementary collapse; the routine checks every incidence and does not use a homology-only rank test. The exact chain-orbit cell counts (dimensions zero through three), followed by the remaining cells, are:

| Group | Initial orbit cells | Elementary collapse pairs | Residual cells |
|---|---|---:|---|
| \(S_3\) | \((211,1098,1624,736)\) | \(1834\) | \((1,0,0,0)\) |
| \(A_3\) | \((352,2040,3160,1472)\) | \(3500\) | \((12,12,0,0)\) |
| \(A_4\) | \((246,1444,2288,1088)\) | \(2460\) | \((26,72,48,0)\) |

For \(A_3\), the residual graph is connected and each vertex has degree two, hence is a 12-cycle, homeomorphic to \(S^1\). For \(A_4\), the residual two-complex is connected, each edge belongs to precisely two triangles, and every vertex link is one cycle. Thus it is a connected closed surface; its Euler characteristic is \(26-72+48=2\), forcing \(S^2\). The \(S_3\) quotient collapses to a vertex. The verifier checks these local manifold and graph properties directly; no assumption that homology alone determines homotopy is used.

**3. Infinite stabilization.** Every original configuration cell uses at most three distinct arm labels. Every face of that cell, and every strict chain terminating at it, still uses at most these three labels. Thus a group orbit of a face chain depends only on the action of the arm-permutation group on injective ordered assignments of at most three distinct labels. The full symmetric groups \(S_m\) are three-transitive for every \(m\geq3\), and the alternating groups \(A_m\) are three-transitive for every \(m\geq5\): if a permutation matching up to three prescribed labels is odd, interchange two of at least two unused labels to make it even. Hence the orbit-chain face-poset quotients for all \(A_m\), \(m\geq5\), are canonically incidence-isomorphic to the \(S_3\)-orbit complex already collapsed to a point. This proves the result for every \(m\), rather than just sampled examples.

## Verification
Run `python3 three_particles.py` with Python 3.10 or later. It uses only the standard library, enumerates **all** configuration cubes and face-chain orbit cells at the three finite cases needed by the proof, performs the elementary collapses, verifies the residual cycle/surface local-link conditions, and prints exact counts and SHA-256 fingerprints of its deterministic collapse sequences. The provided `verification_output.txt` records the successful run. The independent universal ingredient is the proved three-arm support and alternating-group three-transitivity, not an extrapolation from the finite computation.

## Relationship to prior work
The cubical discretized configuration complex is the classical Abrams model, and Prue–Scrimshaw (first public version 2009) prove ordinary stabilization/deformation results for graph configurations. These are credited as foundational definitions; **ordinary non-equivariant deformation equivalence is not used to identify the orbit space of the unrestricted continuous configuration space**. Previously published work on the *continuous* three-particle four-arm theta graph reports a sphere for its \(A_4\)-quotient. The middle case here is therefore a comparison and cross-check, not a separate novelty claim. The new distinction is the sharp all-arm cubical trichotomy, especially the three-arm circle and the infinite contractible range via three-transitivity and exact collapse. Relevant previous work on two-particle theta representations, on symmetric quotients of complete-graph configurations, and on ordered particles on stars concerns different configuration objects and does not imply this finite-state orbit classification.

## Limitations
The result is a homotopy classification, not a homeomorphism classification of the original orbit spaces. It does not assert that an arbitrary known deformation retraction from the unrestricted continuous graph configuration space onto the Abrams discretization is equivariant under arm permutations. No result is claimed for non-alternating intermediate subgroups or for four or more particles. The irreducible finite checks are exact but computer-assisted; the explicit code is supplied so each enumerated incidence and collapse can be independently replayed. Unindexed equivalent results remain a possible originality risk.

## References
1. A. Abrams, *Configuration Spaces and Braid Groups of Graphs*, University of California, Berkeley, Ph.D. thesis (2000), https://math.berkeley.edu/publications/configuration-spaces-and-braid-groups-graphs .
2. P. Prue and T. Scrimshaw, *Abrams's Stable Equivalence for Graph Braid Groups*, first arXiv version 2009-09-30, https://arxiv.org/pdf/0909.5511 .
3. D. Farley and L. Sabalka, *Discrete Morse Theory and Graph Braid Groups*, Algebraic & Geometric Topology 5 (2005), 1075–1109, https://doi.org/10.2140/agt.2005.5.1075 .
4. *Full symmetry and alternating-group branching of the three-particle genus-three theta surface*, publicly indexed research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-full-symmetry-and-alternating-group-branching-of-the-three-parti--f511e085ba03 (indexed summary checked; full text not accessed).
