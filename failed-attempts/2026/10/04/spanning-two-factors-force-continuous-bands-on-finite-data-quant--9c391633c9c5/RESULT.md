# Spanning two-factors force continuous bands on finite-data quantum trees
## Finding
Let \(G\) be a finite connected simple graph of minimum degree at least \(2\), not a cycle, and let \(F\subseteq G\) be a spanning two-factor. Thus every vertex of \(G\) has degree exactly \(2\) in \(F\), while \(F\) may have several cycle components.

Endow \(G\) with arbitrary quantum-graph data of the class considered by Anantharaman, Ingremeau, Sabri and Winn: every edge \(e\) has length \(L_e>0\); every oriented edge \(b\) has a real continuous potential \(W_b\) satisfying \(W_{\widehat b}(L_b-x)=W_b(x)\); and every vertex \(v\) has a real \(\delta\)-coupling \(\alpha_v\). Let \(\mathbf T=\widetilde{\mathbf G}\) be the universal-cover quantum tree with the lifted data, and let \(H_{\mathbf T}\) be its Schrödinger operator.

Then every \(L^2\)-eigenvalue of \(H_{\mathbf T}\) is a Dirichlet value, and \(H_{\mathbf T}\) has nonempty bands of purely absolutely continuous spectrum.

This replaces the source's stated assumption that the finite base graph itself contain one Hamiltonian cycle by the strictly weaker assumption that it contain a spanning two-factor.

As a concrete consequence, take the Petersen graph in the standard generalized-Petersen labeling. The cycles \(0-1-2-3-4-0\) and \(5-7-9-6-8-5\) are disjoint and together cover all ten vertices, hence form a spanning two-factor. The conclusion therefore holds for arbitrary admissible edge-dependent quantum data lifted from the Petersen graph, even though the Petersen graph is non-Hamiltonian.

## Assumptions and scope
The finite base graph is connected, simple, has minimum degree at least \(2\), is not itself a cycle, and has a spanning two-factor. These hypotheses place its universal-cover quantum tree under assumption (C1) of the primary source. The statement concerns the unperturbed lifted operator with \(\delta\)-conditions. It does not assert absence of isolated Dirichlet eigenvalues, nor does it extend the random-perturbation theorem to band edges.

A Dirichlet value is a real \(\lambda\) for which \(S_\lambda(L_b)=0\) on at least one edge type, using the fundamental solution notation of the primary source.

## Proof
Let \(p:\widetilde G\to G\) be the universal covering map and put \(\widetilde F=p^-1(F)\). Every vertex of \(\widetilde G\) is incident to exactly two edges of \(\widetilde F\), because \(F\) is spanning and two-regular. Hence every component of \(\widetilde F\) is two-regular. Since \(\widetilde G\) is a tree, \(\widetilde F\) contains no finite cycle. A connected, locally finite, acyclic graph in which every vertex has degree \(2\) is a bi-infinite line. Therefore \(\widetilde F\) is a disjoint union of bi-infinite lines covering every vertex of \(\widetilde G\).

The ensemble \(\widetilde F\) is invariant under every covering transformation: membership of a lifted edge depends only on whether its projection lies in \(F\). With the natural root measure obtained by averaging over base vertices, the root belongs to \(\widetilde F\) with probability \(1\), because \(F\) spans all vertices. Thus \(\widetilde G\) is Hamiltonian in the line-ensemble sense of Definition 4.1 of the primary source.

Inspect Proposition 4.1 of that source. After reducing a non-Dirichlet metric eigenfunction to the weighted discrete equation on vertices, the proof invokes a Hamiltonian cycle only to produce a full invariant line ensemble. The subsequent invariant labeling, von Neumann dimension estimate and induction use only that line ensemble and the fact that every vertex lies on it. Replacing the lifted Hamiltonian cycle there by \(\widetilde F\) leaves every step unchanged. Consequently, if \(\lambda\) is an \(L^2\)-eigenvalue of \(H_{\mathbf T}\), then \(S_\lambda(L_b)=0\) for some edge type \(b\).

Section 4.3 of the primary source proves independently of Hamiltonicity that, for any such finite-data universal cover, the spectral bottom \(a_0=\inf\sigma(H_{\mathbf T})\) satisfies
\[
a_0<\mathcal E_D,
\]
where \(\mathcal E_D\) is the least Dirichlet value. Hence \(a_0\) is not an eigenvalue. Because \(a_0\in\sigma(H_{\mathbf T})\), an isolated \(a_0\) would be an eigenvalue for a self-adjoint operator, so \(a_0\) is not isolated.

Theorem 1.2 of the primary source gives, under (C1), a spectral decomposition into closed bands with purely absolutely continuous interiors plus a discrete set of isolated points. Since the spectral bottom is not isolated, the band part cannot be empty. Therefore \(H_{\mathbf T}\) has a nontrivial band of purely absolutely continuous spectrum.

## Verification
The proof uses three statement-level checks. First, the pullback of a spanning two-factor has degree exactly \(2\) at every lifted vertex, and acyclicity forces each component to be a bi-infinite line. Second, the proof of Proposition 4.1 was checked at the step where the lifted Hamiltonian cycle enters: after that point it uses only a full invariant line ensemble. Third, Section 4.3 proves \(a_0<\mathcal E_D\) without using the Hamiltonian-cycle hypothesis, so the extended eigenvalue obstruction combines with the source's band-plus-discrete theorem exactly as stated.

For the Petersen example, the displayed two cycles are edge-disjoint, vertex-disjoint and cover \(\{0,1,2,3,4,5,6,7,8,9\}\); each is a five-cycle in the standard generalized-Petersen graph \(G(5,2)\).

## Relationship to prior work
Anantharaman--Ingremeau--Sabri--Winn prove the band-plus-discrete structure for universal covers satisfying (C1), but explicitly note that nonempty continuous spectrum is not automatic from that theorem alone. For general edge-dependent quantum data they state nonemptiness under the stronger hypothesis that the finite base graph is Hamiltonian. Their Definition 4.1 is already phrased in terms of invariant line ensembles on the universal cover, and their Proposition 4.1 adapts the line-ensemble method of Bordenave--Sen--Virag.

Bordenave--Sen--Virag prove a general invariant-line-ensemble bound for expected spectral measures of discrete unimodular trees. Their operator is the discrete adjacency operator, not the metric quantum-tree Schrödinger operator considered here. The present statement uses their line-ensemble mechanism only through the quantum-graph reduction already developed in the primary source.

The new point is the graph-theoretic bridge: a spanning two-factor of the finite base supplies exactly the full invariant line ensemble needed by the quantum proof, even when no single spanning cycle exists. This gives a genuinely broader finite-base class and, in particular, an arbitrary-data Petersen example not supplied by the source's alternative realization of a homogeneous regular tree as the cover of another Hamiltonian graph.

## Limitations
A spanning two-factor is only a sufficient condition for the existence of a full invariant line ensemble; no necessity claim is made. The result does not classify all finite bases whose universal covers are Hamiltonian in the invariant-line-ensemble sense. It also does not remove the source's (C1) assumptions or rule out isolated eigenvalues at Dirichlet values.

The originality comparison found no indexed statement of this two-factor weakening, but because the extension is short and uses a natural graph-theoretic construction, an equivalent observation in unindexed literature remains a residual risk.

## References
1. N. Anantharaman, M. Ingremeau, M. Sabri, B. Winn, “Absolutely Continuous Spectrum for Quantum Trees,” arXiv:2003.12765v1; Communications in Mathematical Physics 383 (2021), 537–594, DOI 10.1007/s00220-021-03994-3.
2. C. Bordenave, A. Sen, B. Virag, “Mean quantum percolation,” Journal of the European Mathematical Society 19 (2017), 3679–3707, DOI 10.4171/JEMS/750.
