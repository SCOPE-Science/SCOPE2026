# Integral arm-pair homology of the four-arm theta configuration space

## Finding
Let \(\Theta_4\) be the graph consisting of two poles joined by four internally disjoint paths, each of length three, and let \(B_2(\Theta_4)\) be the space of unordered pairs of distinct points of its geometric realization. Its automorphism group \(G=S_4\times C_2\) permutes the four arms and optionally exchanges the poles. Write \(P_4=\mathbb Z^4\) for the integral arm-permutation lattice and \(\varepsilon\) for the nontrivial integral sign character of the pole-interchange factor. Then

\[
H_1(B_2(\Theta_4);\mathbb Z)\cong \bigwedge^2P_4\otimes\varepsilon
\]

**as integral \(G\)-lattices**, not merely as rational representations. Also \(H_0\cong\mathbb Z\), and \(H_k=0\) for all \(k\ge2\). An explicit integral basis consists of the six exchanges \(z_{ij}\), for \(1\le i<j\le4\), in which the two particles traverse the two-arm circuit in opposite directions, starting and ending at the unordered pole pair. The generators transform as

\[
(\sigma,\iota^s)_*z_{ij}=(-1)^s\,z_{\sigma(i),\sigma(j)},\qquad
z_{ji}=-z_{ij}.
\]

The rational representation splits as \(S^{(3,1)}\oplus S^{(2,1,1)}\), with both summands additionally twisted by \(\varepsilon\). For an arm permutation \(\sigma\) with \(f\) fixed arms and \(t\) transposed pairs in its cycle decomposition, its rational homology character is \((-1)^s(\binom f2-t)\). In particular it has no nonzero \(G\)-invariant vectors.

## Assumptions and scope
All homology is unreduced integral singular homology unless a coefficient ring is shown. The graph \(\Theta_4\) has poles \(u=0,v=1\), and arm \(i\), indexed \(i=0,1,2,3\) in the verifier, has internal vertices \(a_i=2+2i\) and \(b_i=3+2i\). The edges, with chosen orientation, are \(u\to a_i\to b_i\to v\). The pole involution exchanges \(u,v\) and each \(a_i,b_i\); arms can independently be permuted. Since the only vertices of valence four are the poles, these are all automorphisms.

The open collision-free unordered configuration space is \(B_2=\{\{x,y\}:x,y\in|\Theta_4|,x\ne y\}\). By the sufficiently-subdivided graph configuration theorem (Farley–Sabalka, Theorem 3.1, citing Abrams), it deformation retracts onto the finite unordered cubical discretization \(UD_2\). Every path joining the two essential poles has three edges, and every nontrivial closed path has at least six; both are more than the required thresholds for two particles. The discretization is preserved by all \(48\) automorphisms.

## Proof
Construct \(UD_2\) directly. Its 0-cells are unordered pairs of distinct vertices; its 1-cells consist of an oriented graph edge together with a nonincident vertex; its 2-cells consist of unordered pairs of graph edges having no common endpoint. Thus the cell counts in degrees zero through two are respectively \((45,96,46)\). The oriented boundary of \((e,x)\), for \(e=(a,b)\), is \(\{b,x\}-\{a,x\}\). If \(e_i=(a,b)\), \(e_j=(c,d)\), with \(i<j\), the 2-cube boundary is

\[
\partial(e_i,e_j)=(e_j,b)-(e_j,a)-(e_i,d)+(e_i,c).
\]

The complete integer boundary data are regenerated and checked by the accompanying `theta4_verifier.py` (standard-library Python). There is a sequence of 46 elementary collapses each pairing a square with a then-free boundary edge; these remove **every** square. Each free-face test is performed on the remaining incidence relation, and each corresponding boundary coefficient is \(\pm1\). The remaining CW complex is a connected graph with 45 vertices and 50 edges; a spanning tree has 44 edges, leaving six chords. This establishes the complete integral homology calculation, including absence of torsion.

For each \(i<j\), set \((a,b)=(a_i,b_i)\) and \((c,d)=(a_j,b_j)\). Define the closed six-step 1-chain \(z_{ij}\) using the unordered vertex-pair sequence

\[
\{u,v\}\longrightarrow\{a,v\}\longrightarrow\{a,d\}\longrightarrow\{b,d\}\longrightarrow\{b,c\}\longrightarrow\{v,c\}\longrightarrow\{v,u\}.
\]

Each step moves one particle along one graph edge; the verifier constructs its signed oriented 1-cell chain and checks \(\partial z_{ij}=0\). The 46 collapses give exact integral substitutions for eliminated edges, hence map each \(z_{ij}\) into the remaining graph. Projecting onto its six oriented non-tree chords gives the matrix (rows ordered by the verifier's deterministic chord list and columns \((01),(02),(03),(12),(13),(23)\)):

\[
\begin{pmatrix}
-1&0&0&0&0&0\\
0&-1&0&0&0&0\\
0&0&0&-1&0&0\\
0&0&-1&0&0&0\\
0&0&0&0&-1&0\\
0&0&0&0&0&-1
\end{pmatrix}.
\]

The determinant is \(-1\); thus the six explicitly defined cycles are a **unimodular integral homology basis**, not just linearly independent over a field.

Finally, for every one of the \(24\) arm permutations and both pole-interchange choices, transport each signed 1-chain by the resulting vertex/edge automorphism. The verifier checks that its difference from the claimed signed arm-pair cycle reduces to zero by the same 46 exact substitutions, in all \(48\cdot6=288\) cases. This proves the displayed integral lattice isomorphism and the character formula. All assertions concern this single four-arm graph; no extrapolation to every arm number is used.

## Verification
Run `python theta4_verifier.py` using Python 3 standard library. It checks all incidence matrices, \(\partial_1\partial_2=0\), all cycles, each currently free square/edge pair, the spanning-tree count, the determinant by exact fraction-free integer elimination, and all automorphism actions. The run prints `PASS: vertices=45 one_cells=96 two_cells=46 free_square_collapses=46 graph_chords=6 integral_det=-1 group_maps=288`.

## Relationship to prior work
Farley and Sabalka (2005, originally made public 25 October 2004) supply the graph-braid discrete-Morse framework and the precise cubical deformation-retract theorem, not the present integral action. Barnett and Farber (2009) investigate two **ordered** particles on graphs by intersection methods and do not state this explicit \(S_4\times C_2\) module. The 2019 graph quantum-statistics account illustrates the three-arm two-particle free group and the four-arm **three**-particle surface braid group; these are different assertions from the integral two-particle symmetry lattice here. The six-cycle proof recovers the underlying rank independently and refines it equivariantly.

## Limitations
The claim is for \(\Theta_4\) only. It neither classifies the entire graph braid group nor establishes a natural integral module formula for arbitrary numbers of arms or particles. Novelty assessment is limited by the search and inspected primary literature; equivalent unindexed calculations remain possible. The accompanying finite verifier proves exactly the stated finite-cell claim but is not an external or independent certification.

## References
1. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, Algebraic & Geometric Topology 5 (2005), 1075–1109, arXiv:math/0410539. Public version 25 October 2004. https://arxiv.org/abs/math/0410539
2. K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, Algebraic & Geometric Topology 9 (2009), 593–624, arXiv:0903.2180. https://arxiv.org/abs/0903.2180
3. *Non-abelian Quantum Statistics on Graphs*, Communications in Mathematical Physics (2019), DOI:10.1007/s00220-019-03583-5, especially Example 4. https://doi.org/10.1007/s00220-019-03583-5
