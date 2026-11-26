# Linear-time minimum stabilizer selection for generalized surface-code erasures

## Finding
For the generalized surface codes considered by Matsumoto, fix an erased physical-edge set \(I\subseteq\mathring E\). The exact minimum numbers of **original local** vertex and face stabilizers needed by the paper's sector-wise CSS reduction have closed graph-component formulas.

On the vertex side, let \(G_I=(V_I,I)\) be the graph consisting of the erased edges and their endpoint vertices. Put
\[
V_I^\circ=V_I\cap\mathring V,
\]
and let \(c_Z(I)\) be the number of connected components \(K\) of \(G_I\) for which \(V(K)\subseteq\mathring V\). Then the minimum number of vertex measurements in Section 5.3 of the source is
\[
\boxed{\ell_Z=|V_I^\circ|-c_Z(I)}.
\]

On the face side, let \(F_I\) be the faces incident to at least one erased edge. Build a graph on \(F_I\) by joining the two incident faces for every erased nonboundary edge. Mark a connected component if one of its faces is incident to an erased boundary edge. If \(c_X(I)\) is the number of unmarked components, then the minimum number of face measurements is
\[
\boxed{\ell_X=|F_I|-c_X(I)}.
\]

These minima can be achieved without measuring linear combinations that lose the local vertex/face interpretation. In each component of \(G_I\) contained entirely in \(\mathring V\), omit one arbitrary vertex and measure the remaining vertices; in each component that touches an omitted/open vertex, measure every vertex belonging to \(\mathring V\). Dually, omit one arbitrary face from each unmarked face component and measure every face in each marked component.

Given the endpoint and incident-face lists of each erased edge, the two component decompositions and the minimum measurement sets are computable in \(O(|I|)\) time. This replaces the \(O(n^3)\) Gaussian elimination used by the source for this generalized-surface-code specialization.

## Assumptions and scope
The code is exactly the generalized surface code defined in the source: physical qubits are indexed by \(\mathring E\), measurable vertex stabilizers by \(\mathring V\), and face stabilizers by \(F\). The erased set satisfies \(I\subseteq\mathring E\). The claim concerns the source's sector-wise CSS construction: the smallest number of original vertex stabilizers sufficient for the \(Z\)-erasure sector and the smallest number of original face stabilizers sufficient for the \(X\)-erasure sector.

No claim is made that a more general joint observable outside the original vertex/face stabilizer family cannot reduce a different measurement cost model. The source itself separates the two CSS sectors in this specialization. The linear-time statement assumes the usual surface-cellulation data structure in which the endpoints and one or two incident faces of an edge are available in constant time.

## Proof
Let \(P_I\) denote restriction to erased coordinates. The source's Theorem 5 and its CSS specialization imply
\[
\ell_Z=\dim P_I(C_Z),\qquad \ell_X=\dim P_I(C_X).
\]
The code \(C_Z\) is the row span of vertex-edge incidence vectors for \(v\in\mathring V\), while \(C_X\) is the row span of face-edge incidence vectors for \(f\in F\). Therefore
\[
\ell_Z=\operatorname{rank}_{\mathbf F_2} B_Z(I),\qquad
\ell_X=\operatorname{rank}_{\mathbf F_2} B_X(I),
\]
where each matrix is the corresponding incidence matrix restricted to erased-edge columns.

For the vertex matrix, consider a linear relation among its rows with coefficients \(y_v\in\mathbf F_2\). Each erased edge \(e=uv\) imposes
\[
y_u+y_v=0,
\]
where the coefficient of an endpoint outside \(\mathring V\) is interpreted as fixed to zero because its row is absent. Hence the coefficients are constant on each connected component of \(G_I\). A component entirely contained in \(\mathring V\) contributes exactly one row dependency, namely its all-ones relation. A component touching any omitted/open vertex has no nonzero row dependency because the constant is forced to zero. Thus the left nullity is exactly \(c_Z(I)\), giving
\[
\operatorname{rank} B_Z(I)=|V_I^\circ|-c_Z(I).
\]
The stated vertex selection deletes exactly one row for each and only each dependency, so the retained rows are independent and span the same restricted row space.

For the face matrix, every erased nonboundary edge has two incident face rows and imposes equality of their relation coefficients. Every erased boundary edge has a single incident face row and forces that coefficient to zero. Thus coefficients are constant on each component of the two-face adjacency graph, with a one-dimensional dependency exactly for components containing no erased boundary edge. The left nullity is \(c_X(I)\), hence
\[
\operatorname{rank} B_X(I)=|F_I|-c_X(I).
\]
Deleting one face row from each unmarked component gives a basis; marked components require every face row.

Finally, each erased edge contributes at most two endpoint incidences and at most two face incidences. Building the two local graphs and running depth-first or breadth-first search therefore takes \(O(|I|+|V_I|+|F_I|)=O(|I|)\) time because \(|V_I|,|F_I|\le 2|I|\).

## Verification
The proof is symbolic and does not rely on finite enumeration. The accompanying checker independently generates random finite incidence instances, computes binary ranks by exact Gaussian elimination, and compares them with the component formulas for both the primal restricted-incidence case and the dual half-edge case. It also verifies that the constructive row selections have the claimed ranks. The finalized checker returns `VERIFY_OK`.

## Relationship to prior work
Matsumoto proves that the sector-wise minimum equals the dimension of the erased-coordinate projection and, for generalized surface codes, gives an \(O(n^3)\) Gaussian-elimination procedure that preserves vertex/face observables. The paper explicitly states that a faster alternative is strongly desired. The present result identifies the restricted matrices as graph-incidence matrices and evaluates their ranks exactly by connected components, including open/boundary effects.

Delfosse and Zémor give a linear-time maximum-likelihood erasure decoder for surface codes. Matsumoto explicitly notes that their algorithms use only relevant measurements but do not state a minimum sufficient measurement set. Connolly, Londe, Leverrier, and Delfosse study fast erasure decoding for hypergraph-product codes and assume the stabilizer outcomes used by their decoder; their result does not provide the boundary-aware minimum vertex/face selection proved here. The classical graph-incidence rank theorem itself is standard; the contribution here is its exact application to the newly posed measurement-minimization problem and the resulting local-stabilizer algorithm.

## Limitations
The result applies to generalized surface codes whose stabilizer incidence is the source's binary vertex-edge and face-edge incidence. It does not extend as stated to arbitrary LDPC stabilizer matrices whose columns can have more general support. It minimizes the source's separate original vertex and face stabilizer measurements, not measured-qubit support, circuit depth, noisy-measurement cost, or an unrestricted nonlocal observable model. The linear running time assumes direct access to edge incidence data. No claim is made about erasure patterns that are not correctable by the underlying code.

## References
1. R. Matsumoto, “Reducing measurements in quantum erasure correction by quantum local recovery,” arXiv:2510.22890v1 (first public 2025-10-27); Computational and Applied Mathematics, DOI:10.1007/s40314-026-03881-4.
2. N. Delfosse and G. Zémor, “Linear-time maximum likelihood decoding of surface codes over the quantum erasure channel,” Physical Review Research 2, 033042 (2020), DOI:10.1103/PhysRevResearch.2.033042.
3. N. Connolly, V. Londe, A. Leverrier, and N. Delfosse, “Fast erasure decoder for hypergraph product codes,” Quantum 8, 1450 (2024), DOI:10.22331/q-2024-08-27-1450.
4. R. Matsumoto, “Simultaneous Reduction of Observables and Measured Qudits in Entanglement-Assisted Quantum Local Recovery,” arXiv:2609.23316 (2026).
