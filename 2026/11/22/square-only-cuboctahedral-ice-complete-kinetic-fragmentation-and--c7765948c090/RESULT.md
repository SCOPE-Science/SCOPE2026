# Square-only cuboctahedral ice: complete kinetic fragmentation and weighted spectrum

## Finding

Let \(G\) be the cuboctahedral graph with twelve labelled vertices and twenty-four edges. Let \(\mathcal I\) consist of every orientation of its edges with two incoming and two outgoing edges at each vertex. Fix its six quadrilateral faces \(S_1,\ldots,S_6\), numbered so the opposite pairs are \((S_1,S_2)\), \((S_3,S_4)\), and \((S_5,S_6)\). The only permitted move is reversal of a directed quadrilateral face; **triangular-face reversals are excluded**.

For an ice configuration \(\omega\), let \(A(\omega)\subseteq\{1,\ldots,6\}\) be the set of its flippable square faces. Define the joint flippability polynomial by
\[
P(\mathbf z)=\sum_{\omega\in\mathcal I}\prod_{i\in A(\omega)}z_i.
\]
The complete, labelled result is
\[
\begin{split}
P(\mathbf z)={}&144+24\sum_{i=1}^{6}z_i
+8\sum_{1\le i<j\le6}z_i z_j\\
&+16(z_1+z_2)(z_3+z_4)(z_5+z_6)
+64\prod_{i=1}^{6}z_i.
\end{split}
\]
In particular \(|\mathcal I|=600\), and every individual quadrilateral is flippable in \(192\) configurations; these two *marginal* numbers were reported previously and are not claimed as new. The joint polynomial and its complete square-only kinetic decomposition are the findings.

Each connected component of the legal-move graph is a Boolean cube. Writing \(\mathcal C(\mathbf z)\) for the component generating polynomial, with one monomial \(\prod_{i\in I}z_i\) for every component having flippable-face set \(I\), one obtains
\[
\boxed{\begin{split}
\mathcal C(\mathbf z)={}&144+12\sum_{i=1}^{6}z_i
+2\sum_{1\le i<j\le6}z_i z_j\\
&+2(z_1+z_2)(z_3+z_4)(z_5+z_6)
+\prod_{i=1}^{6}z_i.
\end{split}}
\]
There are exactly \(263\) connected components: \(144\) isolated vertices, \(72\) copies of \(Q_1\), \(30\) of \(Q_2\), \(16\) of \(Q_3\), and one \(Q_6\). There are no components of dimensions four or five. The full resonance graph has \(576\) undirected edges.

For arbitrary strictly positive real couplings \(t_1,\ldots,t_6\), define the square-only kinetic Hamiltonian on \(\mathbb C^{\mathcal I}\) by
\[
H_{\rm kin}|\omega\rangle=-\sum_{i\in A(\omega)}t_i|\operatorname{flip}_i\omega\rangle.
\]
Its complete spectrum, **including multiplicities**, is the multiset
\[
\biguplus_{I\subseteq\{1,\ldots,6\}}
\bigcup_{\epsilon\in\{-1,+1\}^{I}}
\left\{-\sum_{i\in I}\epsilon_i t_i\right\}^{\uplus m_I},
\qquad m_I=[\prod_{i\in I}z_i]\,\mathcal C(\mathbf z).
\]
Here \(\{a\}^{\uplus m}\) means \(m\) copies of the singleton eigenvalue \(a\). The kinetic ground state is unique, its energy is \(-\sum_i t_i\), and the spectral gap above it equals \(2\min_i t_i\). With all couplings equal to one, the spectrum is symmetric and has eigenvalue multiplicities \(1\) at \(\pm6\), \(6\) at \(\pm4\), \(16\) at \(\pm3\), \(45\) at \(\pm2\), \(120\) at \(\pm1\), and \(224\) at zero.

For the corresponding positive square-only Rokhsar--Kivelson operator \(H_{\rm RK}=\sum_i t_i(P_i-T_i)\), where \(P_i\) projects onto configurations in which face \(i\) is flippable and \(T_i\) reverses that face there and acts as zero elsewhere, the zero-energy multiplicity is exactly \(263\). Its smallest positive eigenvalue is \(2\min_i t_i\).

## Assumptions and scope

Vertices are all permutations of \((0,\pm1,\pm1)\), with an edge precisely between two vertices whose squared Euclidean distance is two. Every vertex has degree four. The squares are the six sets of four vertices with a chosen coordinate fixed at \(+1\) or \(-1\), grouped as opposite pairs. Each of the twenty-four edges lies in exactly one square; each vertex lies in exactly two squares. The Hilbert-space basis is labelled by directed-edge assignments satisfying the ice rule, without quotienting by graph symmetry or global arrow reversal. Dynamics is restricted to square faces; the couplings are real and strictly positive. The symbol \(Q_d\) denotes the \(d\)-dimensional hypercube graph.

## Proof

**Step 1: a finite, exact joint-face certificate.** For each square \(S_i\), there are sixteen possible directions for its four edges. Let \(o_i(v,\eta)\in\{0,1,2\}\) count outgoing edges from vertex \(v\) in square-local orientation \(\eta\), and let \(c_i(\eta)\in\{0,1\}\) indicate that its four arrows form a directed cycle. Because the squares partition the edges and each vertex belongs to two squares, the coefficient identity
\[
P(\mathbf z)=\left[\prod_{v\in V(G)}x_v^2\right]
\prod_{i=1}^{6}\left(
\sum_{\eta\in\{0,1\}^{E(S_i)}}
z_i^{c_i(\eta)}\prod_{v\in S_i}x_v^{o_i(v,\eta)}
\right)
\]
is exact: every global choice of the six local orientation words is counted once, and extracting each vertex's outgoing degree two imposes precisely the ice rule. Direct integer evaluation of this explicitly finite product gives the displayed \(P\). The complete evaluation procedure is reproduced by `verify_coordinates.py`, which checks all six local choice tables and enumerates the surviving complete words. A separate enumeration, `verify_line_graph.py`, constructs the graph as the line graph of a cube and branches independently on the twenty-four directed edges, imposing the outgoing-degree conditions. Its joint pattern counts agree exactly. Both enumerations are exhaustive by construction rather than numerical samples.

**Step 2: component structure.** On an oriented directed square, reversal preserves one incoming and one outgoing edge at each of the four vertices, hence the global ice rule. Because different squares have disjoint **edge sets**, reversing \(S_i\) changes no arrow belonging to another \(S_j\). Therefore every other face's flippability is invariant, and all legal square-reversal involutions commute. Given \(\omega\), the set \(I=A(\omega)\) remains constant throughout its component. Different subsets of \(I\) reverse different disjoint edge sets, hence produce distinct configurations. Every component is exactly \(Q_{|I|}\), with \(2^{|I|}\) vertices. Thus its coefficient is \(m_I=[\mathbf z^I]P/2^{|I|}\), yielding the polynomial \(\mathcal C\), all component multiplicities and all \(576\) edges.

**Step 3: weighted quantum spectra.** On the cube of active faces \(I\), choose each bit to record whether that square has been reversed. The kinetic restriction is \(-\sum_{i\in I}t_i X_i\), where \(X_i\) toggles the corresponding bit; the tensor-product Hadamard eigenbasis gives eigenvalues \(-\sum_{i\in I}\epsilon_i t_i\). Summing with the exact component multiplicities proves the multiset statement. Exactly one component has all six active faces. Because all \(t_i>0\), its all-plus eigenvector has strictly lower energy than every other eigenvector, proving the unique kinetic ground state. Every other component has at most three active squares and so lies at least \(3\min_i t_i\) above the ground state. The first excitation *within* the full six-cube lies exactly \(2\min_i t_i\) above it, establishing the sharp gap. On \(Q_{|I|}\), the Rokhsar--Kivelson restriction equals \(\sum_{i\in I}t_i(1-X_i)\), with exactly one zero eigenvector; its least positive eigenvalue, minimized over components, is \(2\min_i t_i\). This proves both Rokhsar--Kivelson conclusions.

## Verification

Run `python3 verify_coordinates.py` and `python3 verify_line_graph.py` from a directory containing the two standalone scripts. No external Python packages or external data are required. The coordinate program independently checks the 600 admissible states, the entire 31-term labelled face-activity support, all coefficient values, the 263-sector count, and the exact isotropic spectral multiplicities and moments. The line-graph program independently enumerates all ice states using an edge-wise degree-pruned search, builds the actual resonance adjacency graph, counts its connected components, verifies 576 transitions and checks that an explicit integer spectral annihilating polynomial kills every one of the 600 coordinate basis vectors. The finite coefficient identity and commuting-orbit argument above are the proof; finite script results are reproducible exhaustive calculations for this specified finite graph, not evidence for an unclaimed infinite family.

## Relationship to prior work

Lieb's 1967 square-ice result supplies foundational statistical-mechanics motivation, while Felsner's 2004 prescribed-outdegree orientation lattice theory provides a structural framework. Crucially, Henry and Roscilde (first public 26 July 2013) study a **square-plaquette-only** quantum-ice ring-exchange Hamiltonian on the planar checkerboard lattice, with no cuboctahedral geometry or finite six-face joint census; this is the archival square-only kinetic framework specialized here to a curved network. Sivaramakrishnan and Ganesh (first public 27 June 2024, subsequently published in 2024) study the cuboctahedral geometry, enumerate 600 ice configurations and report the 192-per-square marginal. Their quantum dynamics includes both triangular and quadrilateral face flips, whereas the present theorem fixes triangle amplitudes to zero and classifies every resulting square-only sector. Those previously known 600 and 192 numbers are not independent novelty claims here. The present joint six-face correlation, exact 263-sector fragmentation, full weighted kinetic spectral data, and Rokhsar--Kivelson nullity are not implied by a single-face marginal or by full-move connectivity. This is a best-knowledge literature comparison, not a certified global novelty assertion.

## Limitations

This is an exact finite twelve-vertex classification for a **restricted** six-square move set. The sector count changes if triangular flips or other loops are permitted. All weighted spectral and gap statements assume strictly positive real face couplings; for zero or negative couplings the stated uniqueness/gap must be reconsidered. The work does not prove asymptotic behavior for larger curved-ice clusters, implementation robustness, experimental accessibility of suppressing triangle flips, or uniqueness in all historical literature. Independent external scientific validation has not been performed.

## References

- E. H. Lieb, "Exact Solution of the Problem of the Entropy of Two-Dimensional Ice," *Physical Review Letters* **18** (1967), 692. DOI: https://doi.org/10.1103/PhysRevLett.18.692 (public 1967-04-24).
- S. Felsner, "Lattice Structures from Planar Graphs," *Electronic Journal of Combinatorics* **11** (2004), R15. DOI: https://doi.org/10.37236/1768 (public 2004-02-14).
- L.-P. Henry and T. Roscilde, "Order-by-disorder and quantum Coulomb phase in quantum square ice," arXiv:1307.7032 (first public 2013-07-26); *Physical Review Letters* **113** (2014), 027204. https://arxiv.org/abs/1307.7032 ; https://doi.org/10.1103/PhysRevLett.113.027204.
- A. Sivaramakrishnan and R. Ganesh, "Ice on curved surfaces: defect rings and differential local dynamics," arXiv:2406.19453 (first public 2024-06-27); *Physical Review B* **110** (2024), 144202. https://arxiv.org/abs/2406.19453 ; https://doi.org/10.1103/PhysRevB.110.144202.
