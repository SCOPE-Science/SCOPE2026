# Complete balanced-cut entanglement census of the Heawood graph state

## Finding — crossing-edge refinement

Let \(H\) be the point–line incidence graph of the Fano plane. Prepare its pure fourteen-qubit graph state by applying one controlled-\(Z\) gate per edge to \(\lvert+\rangle^{\otimes14}\). Among cuts into two seven-vertex shores, the cuts with maximal entropy (seven bits) have **exactly eleven or thirteen crossing edges**. Each crossing-edge count occurs for exactly 336 labeled seven-vertex shores, counting a shore and its complement separately (168 unordered cuts per edge count). Both shores of every such cut contain points and lines. In contrast, the point-versus-line cut crosses all 21 edges but has only four entanglement bits.

The new claim considered here is the crossing-edge refinement of the maximal-entropy class, not the marginal histogram of entropies. For context, the associated integral Smith census [2] already yields the marginal counts \(100,980,1680,672\) for entropy \(4,5,6,7\) respectively by reduction modulo two and doubling to count labeled shores. These give mean entropy \(5021/858\) bits.

## Assumptions and scope

Points and line normals are the seven nonzero vectors of \(\mathbb F_2^3\), on two separate labeled vertex shores. Incidence is \(p\cdot\ell=0\). The state is pure, all edges have unit weight, no edges are deleted, and both cut shores contain seven vertices. The statement is about this particular graph state, not all incidence graphs.

## Proof

**Entropy and binary rank.** If \(C\) is the cross-adjacency block of a cut \(A\mid B\), within-shore controlled-phase gates are local unitaries. After removing them, basis amplitudes are \(2^{-7}(-1)^{a^{\mathsf T}Cb}\). The trace over \(B\) gives \(\rho_A(a,a')=2^{-7}\mathbf1_{C^{\mathsf T}(a+a')=0}\). With \(r=\operatorname{rank}_{\mathbb F_2}C\), the cosets of the kernel give \(2^r\) nonzero eigenvalues \(2^{-r}\), so the entropy is \(r\) bits, also for every positive-order Rényi entropy. This is the standard graph-state cut-rank rule [1].

**Reduction to two bases.** Write \(P_A\) and \(L_A\) for the point and line sets in \(A\), and similarly for \(B\). The two nonzero cross blocks, up to transpose, are \(M[P_A,L_B]\) and \(M[P_B,L_A]\), where \(M_{p,\ell}=1+p\cdot\ell\) is the Fano incidence matrix over \(\mathbb F_2\). Its rank is four: \(M\) factors through the four coordinates of \((1,p)\) and \((1,\ell)\), and the four coordinate functions are independent on the nonzero vectors on either side. Thus any block of size at least five rules out rank seven. Up to interchanging cut shores, the only possible sizes are \(|P_A|=|L_B|=3\), \(|P_B|=|L_A|=4\).

For the four-by-four block the two feature matrices with rows \((1,p)\) and \((1,\ell)\) are square. Such a matrix for four distinct indices is singular exactly when the sum of the four vector indices is zero: any nontrivial dependence has even support, and support two would repeat a vector. The seven nonzero vectors sum to zero, so the four-by-four block is invertible exactly when the two complementary triples \(P_A,L_B\) are both bases of \(\mathbb F_2^3\). This also explains why the pure-shore cut, which crosses all 21 incidence edges, has entropy four.

**Counting the full-rank cuts.** There are \(\binom73-7=28\) unordered choices for the point basis \(P_A\). Fix an ordering of its three column vectors in the matrix \(P\). As the ordered line basis matrix \(L\) ranges over \(\mathrm{GL}(3,2)\), the matrix \(N=P^{\mathsf T}L\) ranges once over that group. The three-by-three incidence block is \(N+J\), where \(J=\mathbf1\mathbf1^{\mathsf T}\). The determinant lemma gives \(\det(N+J)=\det(N)(1+\mathbf1^{\mathsf T}N^{-1}\mathbf1)\). For uniform \(N\), the vector \(N^{-1}\mathbf1\) ranges uniformly over the seven nonzero vectors. Three have even weight, so \(168\cdot3/7=72\) of the ordered bases give rank seven.

For these 72 choices, every row of \(N+J\) has one or two ones, since neither \(N+J\) nor its entrywise complement \(N\) can have a zero row. If there are three ones in total then \(N+J\), being invertible, is a permutation matrix and \(N\) has even row sums, a contradiction. Six ones are excluded by the same argument with the matrices interchanged. Thus the incidence block has four or five ones. The involution \(N\mapsto N+J\) on the 72 choices exchanges these cases, leaving 36 each. Dividing by \(3!\) leaves six unordered line bases per case for each point basis.

If the three-by-three block has \(e\) ones, the opposite four-by-four incidence block has \(21-9-9+e=3+e\): each point and each line has degree three. The cross-cut edge count is therefore \(3+2e\), equal to 11 or 13. For each value there are \(28\cdot6=168\) cut shores having three points. Complementation doubles this for the labeled-shore count, giving 336 per value.

## Verification

The proof of the crossing-edge refinement is analytic. The accompanying `verify_direct.py` independently exhausts the 3432 labeled seven-vertex subsets, and its output line `DIRECT_RANK7_EDGES=[(11, 336), (13, 336)]` checks the refinement. `verify_blocks.py` separately checks the contextual entropy counts. No conclusion about noise, larger planes or experimental resources is drawn from this finite classification.

## Relationship to prior work and limitations

The entropy/rank rule is established in [1]. The same-date associated qudit record [2] gives an integral Smith histogram and explicitly checks the binary marginal. That table does not record crossing-edge counts for the full-rank binary class. Its date alone does not determine precedence between the records. The incidence-matching result [3] already gives the canonical four-bit baseline at the fixed point-versus-line cut; here the comparison is with **all** maximum-entropy balanced cuts of the undeleted graph. The minimum arrangement/cutwidth result [4] treats edge boundaries, not the edge distribution conditioned on full binary rank. The database in [5] covers at most twelve qubits. The proof above classifies the conditional crossing-edge counts, without claiming historical priority beyond the examined sources or extensions to other graph states.

## References

1. M. Hein, J. Eisert and H. J. Briegel, *Multi-party entanglement in graph states*, Proposition 3, https://arxiv.org/abs/quant-ph/0307130 .
2. *Characteristic-three entanglement defects in the Heawood qudit graph state*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-characteristic-three-entanglement-defects-in-the-heawood-qudit-g--970e77e34ed4 .
3. *Sharp incidence-matching fault threshold for graph-state entanglement on even-order projective planes*, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-incidence-matching-fault-threshold-for-graph-state-entangl--0f1e8bff6768 .
4. *All optimal linear arrangements of the Heawood graph*, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-all-optimal-linear-arrangements-of-the-heawood-graph--dc3e824375f5 .
5. *Database of Entanglement in Graph States*, Introduction, https://www.codetables.de/larsed/entanglement/ .
