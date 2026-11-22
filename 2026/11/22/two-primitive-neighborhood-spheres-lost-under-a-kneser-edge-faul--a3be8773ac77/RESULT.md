# Two primitive neighborhood spheres lost under a Kneser edge fault

## Finding
Let \(K=\operatorname{KG}(6,2)\) have as vertices the fifteen two-element subsets of \(\{1,2,3,4,5,6\}\), with two vertices adjacent exactly when the subsets are disjoint. Let \(e\) be any edge of \(K\), and let \(\mathcal N(G)\) denote the ordinary *open-neighborhood complex* of a finite simple graph \(G\): its nonempty faces are sets of vertices admitting one common neighbor in \(G\).

Then
\[
\mathcal N(K-e)\simeq\bigvee^{17}S^2.
\]
Moreover, the inclusion induced by retaining all faces of \(\mathcal N(K-e)\) in \(\mathcal N(K)\) acts on integral second homology as a **primitive injection**
\[
H_2(\mathcal N(K-e);\mathbb Z)\hookrightarrow H_2(\mathcal N(K);\mathbb Z),
\qquad \operatorname{coker}\cong\mathbb Z^2.
\]
All positive-degree homology groups of the damaged complex other than \(H_2\) vanish, and all its integral homology is torsion-free. The intact complex is known to be \(\bigvee^{19}S^2\) [1]; thus one graph-edge deletion loses precisely two primitive integral two-sphere classes.

## Assumptions and scope
The assertion concerns exactly the 15-vertex graph \(\operatorname{KG}(6,2)\), its **graph-edge deletion** (not vertex deletion), and the ordinary open-neighborhood complex (not the closed-neighborhood or box complex). Graph automorphisms induced by the symmetric group on six labels act transitively on the edges, so without loss of generality choose the deleted graph edge with endpoints \(\{1,2\}\) and \(\{3,4\}\). The simplicial inclusion is literal because deleting an edge cannot create new common graph neighbors.

For reproducibility, number the graph vertices lexicographically by their two labels, beginning \(12,13,14,15,16,23,24,25,26,34,35,36,45,46,56\), and encode a simplicial face by the sum of the corresponding powers of two indexed from zero. The certificate uses deleted graph-edge endpoints at indices \(0\) and \(9\).

## Proof
**1. Exhaustive finite face model.** Each graph vertex \(u\) has an open-neighbor bitmask \(M_u\); the nonempty faces of its neighborhood simplex are precisely the nonzero submasks of \(M_u\). The union of these fifteen submask families is exactly \(\mathcal N(K)\), respectively \(\mathcal N(K-e)\) after removing the selected graph edge. Enumeration, independently reconstructible by `verify.py`, yields face vectors by dimensions zero through five:
\[
 f(\mathcal N(K))=(15,105,260,225,90,15),\qquad
 f(\mathcal N(K-e))=(15,103,244,205,80,13).
\]
The certificate supplies every face pairing as integer bitmasks, not merely a rank log.

**2. Absolute homotopy.** The exact `absolute_free_pairs` sequence in `CERTIFICATE.json` consists of 268 elementary simplicial collapses of \(\mathcal N(K-e)\). Each lower face has exactly one remaining immediate coface, and the checker tests this condition before removal. The remaining simplicial complex has 124 nonempty faces. On it, the 53 pairs in `absolute_morse_pairs` are incident, disjoint and acyclic: reversing matched cover relations in the full directed face Hasse graph leaves a directed acyclic graph. The remaining unmatched cells consist of one vertex, no edges and 17 triangles. Forman's acyclic-matching theorem therefore provides a CW model with one zero-cell, no one-cells and 17 two-cells; every two-cell attaches to the sole zero-cell. This is precisely \(\bigvee^{17}S^2\). In particular this is an integral, not merely mod-two, conclusion.

**3. Integral inclusion and its cokernel.** Write \(X=\mathcal N(K)\), \(Y=\mathcal N(K-e)\). The relative face set \(X\setminus Y\) has 50 simplices: two edges, 16 triangles, 20 tetrahedra, ten four-simplices and two five-simplices. The 22 `relative_free_pairs` cancel cells with a free *relative* coface and preserve the integral relative chain homotopy type. Six cells remain: two edges and four triangles. With the certificate's increasing-bitmask order, the integral boundary \(C_2(X,Y)\to C_1(X,Y)\), after these elementary cancellations, is represented by the four-by-two transpose convention
\[
\begin{pmatrix}-1&-1&0&0\\0&0&-1&-1\end{pmatrix}.
\]
It is onto with unit coefficients, and its kernel is free of rank two. Hence \(H_2(X,Y;\mathbb Z)\cong\mathbb Z^2\), while \(H_1(X,Y;\mathbb Z)=H_3(X,Y;\mathbb Z)=0\), with no other positive relative homology. The known intact classification [1] gives \(H_2(X;\mathbb Z)\cong\mathbb Z^{19}\) and \(H_1(X;\mathbb Z)=0\). The long exact sequence of the pair now gives
\[
0\longrightarrow H_2(Y;\mathbb Z)\longrightarrow\mathbb Z^{19}
\longrightarrow\mathbb Z^2\longrightarrow0.
\]
Thus the inclusion is injective with free cokernel of rank two, hence primitive. The rank 17 also agrees with the independent absolute Morse calculation.

## Verification
The package contains `CERTIFICATE.json` and standalone `verify.py`, requiring only Python 3's standard library. Run `python3 verify.py CERTIFICATE.json` in a directory containing both files. It independently constructs all graph neighborhoods and simplicial faces, checks both face vectors and all 268 absolute free collapses, checks the acyclicity and critical cells of the 53-pair residual Morse matching, then verifies all 22 relative cancellations and the exact signed integral boundary matrix. The verifier was executed successfully on the embedded files. These finite computations are exhaustive for the stated 15-vertex graph; no extrapolation to other parameters is asserted.

## Relationship to prior work
Nilakantan and Singh [1, Theorem 1.3] prove the intact Kneser family, yielding \(\mathcal N(\operatorname{KG}(6,2))\simeq\bigvee^{19}S^2\). Their Section 5 analyzes a larger simultaneous removal of edges between certain unstable Kneser vertices via a subgraph \(S_{2,k}\), but it does not state the one-edge-fault homotopy type or the primitive map for the specific inclusion above. The present complete finite Morse and relative-chain certificates determine that intermediate fault stage. Other work on vertex deletion, neighborhood-complex symmetry, and cut complexes concerns distinct operations or invariants. The exact loss of two primitive integral classes is not inferred merely by subtracting ranks from the two endpoint classifications in [1].

## Limitations
The claim is specific to \(\operatorname{KG}(6,2)\) and one edge deletion. It does not classify one-edge faults for all Kneser parameters, and it is not an independent audit or a proof that no unindexed equivalent statement exists. The originality comparison includes indexed primary literature and related recorded findings, with remaining bibliographic risk described in `AUDIT.json`.

## References
[1] N. Nilakantan and A. Singh, *Homotopy Type of Neighborhood Complexes of Kneser Graphs, \(KG_{2,k}\)*, arXiv:1802.05848v1, first publicly posted 2018-02-16, https://arxiv.org/html/1802.05848v1.

[2] T. Matsushita, *Fundamental Groups of Neighborhood Complexes*, J. Math. Sci. Univ. Tokyo 24 (2017), 321–353, https://www.ms.u-tokyo.ac.jp/journal/abstract_e/jms240302_e.html.
