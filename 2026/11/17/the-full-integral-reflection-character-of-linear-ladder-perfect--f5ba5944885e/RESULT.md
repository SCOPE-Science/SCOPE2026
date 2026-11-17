# The full integral reflection character of linear-ladder perfect-matching homology

## Finding
For an integer \(n\ge3\), put \(L_n=P_n\square K_2\). Let \(\mathcal P_n\) be the **perfect-matching complex**: its vertices are edges of \(L_n\), and its faces are precisely the subsets of perfect matchings of \(L_n\). Let \(\sigma\) interchange the two rows and \(\rho\) reverse the order of the columns. They generate \(C_2\times C_2\).

The row flip \(\sigma\) is homotopic to the identity on \(\mathcal P_n\). For odd \(n\), \(\mathcal P_n\) is contractible. If \(n=2m\), \(m\ge2\), then \(\mathcal P_n\simeq S^{m-1}\), and its unique nonzero reduced integral homology is a rank-one lattice in degree \(m-1\), with the complete symmetry action
\[
\sigma_*=1,\qquad \rho_*=(\sigma\rho)_*=(-1)^{\binom{m}{2}}.
\]
Thus end reversal preserves top orientation when \(m\equiv0,1\pmod4\) and reverses it when \(m\equiv2,3\pmod4\). Equivalently, the complete integral character at the four group elements \((1,\sigma,\rho,\sigma\rho)\) is \((1,1,\varepsilon_m,\varepsilon_m)\). The reduced rational homology of \(|\mathcal P_n|/(C_2\times C_2)\) is one-dimensional in degree \(m-1\) if \(m\equiv0,1\pmod4\), and vanishes otherwise.

## Assumptions and scope
The path \(P_n\) has \(n\) vertices (the columns); the ladder has \(2n\) graph vertices. Index its vertical rungs by \(a_i\), \(1\le i\le n\), and its horizontal edges in the upper and lower rows by \(b_i,c_i\), \(1\le i<n\). Every edge occurs in some perfect matching. A face of \(\mathcal P_n\) need not itself cover all graph vertices, but must extend to a perfect matching. Homology uses integral coefficients unless explicitly stated otherwise. All equivariance assertions concern the geometric row and column reflections of this finite graph, not arbitrary automorphisms of its simplicial complex.

## Proof
**1. Tiling correspondence and row-flip homotopy.** In any perfect matching, the number of selected edges crossing the cut between columns \(i\) and \(i+1\) is even: the left side contains \(2i\) vertices, each either paired internally or across the cut. Since the cut has exactly the two edges \(b_i,c_i\), either both or neither occur. Thus every perfect matching is uniquely a tiling of the \(n\) columns by singleton vertical rungs \(a_i\) and horizontal doubled pairs \(\{b_i,c_i\}\) occupying consecutive columns.

Let \(K_n\subseteq\mathcal P_n\) be the induced subcomplex on the edges \(a_i,b_i\), and define \(q:\mathcal P_n\to K_n\) by fixing \(a_i,b_i\) and sending \(c_i\) to \(b_i\). For every simplex \(F\), choose a perfect matching \(T\supseteq F\). The tiling correspondence gives \(F\cup q(F)\subseteq T\), so \(q\) is simplicial and \(\operatorname{id}_{\mathcal P_n}\) is contiguous to \(\iota q\), where \(\iota:K_n\hookrightarrow\mathcal P_n\). Moreover \(q\iota=\operatorname{id}_{K_n}\), so \(q\) is a homotopy equivalence. For the row flip, likewise \(F\cup\sigma(F)\subseteq T\), showing that \(\sigma\) is contiguous to the identity. Column reversal permutes \(a_i\mapsto a_{n+1-i}\), \(b_i\mapsto b_{n-i}\), and \(c_i\mapsto c_{n-i}\), so \(q\) is \(\rho\)-equivariant.

**2. Homotopy type.** A simplex in \(K_n\) is an arbitrary disjoint family of singleton tiles \(a_i\) and domino tiles \(b_i\), since every partial tiling extends by placing singleton tiles on uncovered columns. Thus \(K_n=\operatorname{Ind}(H_n)\), where the overlap graph \(H_n\) has one vertex per possible tile and edges for overlapping tiles. For \(n\ge3\), \(N(a_n)=\{b_{n-1}\}\subseteq N(b_{n-2})\). The standard independence-complex fold lemma removes \(b_{n-2}\) by an elementary collapse. In the remaining overlap graph \(N(a_n)=N(a_{n-1})=\{b_{n-1}\}\), so a second fold removes \(a_{n-1}\). What remains is \(H_{n-2}\) disjoint from the edge \(\{a_n,b_{n-1}\}\). Therefore \(K_n\simeq K_{n-2}*S^0\), the suspension of \(K_{n-2}\). Base cases are \(K_1\) (a single point) and \(K_2\) (a three-vertex path's independence complex, homotopy equivalent to \(S^0\)). Induction gives contractibility for odd \(n\) and a sphere \(S^{m-1}\) for \(n=2m\). This reproduces the published nonequivariant classification; only the symmetry actions below are newly claimed.

**3. Exact reversal character.** Work in the reduced augmented oriented simplicial chains of \(K_{2m}\). For a reversal-invariant face \(F\), the permutation of the selected tile-vertices decomposes into orbits of sizes one and two. Its contribution to the reduced alternating simplicial trace is \(-(-1)^{\#\text{selected orbits}}\): a two-cycle contributes a sign \(-1\) to the orientation and two selected vertices to the chain degree. Non-invariant faces contribute zero.

The reversal orbits are: \(m\) pairs of vertical singleton tiles; \(m-1\) pairs of noncentral domino tiles; and the one fixed central domino \(b_m\). Without the central domino, selecting compatible orbits is exactly selecting pairwise disjoint singleton and domino tiles on a length-\(m\) path, with weight \(-1\) per selected tile. Let \(Z_j\) be the signed sum over all such partial tilings of \(j\) sites. Splitting on the first site, the options 'unused' and 'singleton' cancel and the remaining domino contributes \(-Z_{j-2}\). Hence
\[
Z_0=1,\quad Z_1=0,\quad Z_j=-Z_{j-2}\quad(j\ge2).
\]
Choosing the central domino contributes another factor \(-1\) and forbids exactly the last singleton and last domino in the half-path, leaving the signed sum \(Z_{m-1}\). Thus the sum over all reversal-invariant faces weighted by \((-1)^{\#\text{orbits}}\) is
\[
Q_m=Z_m-Z_{m-1}=(-1)^{\lceil m/2\rceil}.
\]
The reduced Lefschetz number is \(\widetilde L(\rho)=-Q_m\). Since the only nonzero reduced rational homology is in degree \(m-1\) and has rank one, its reversal trace (therefore the integral orientation sign) is
\[
(-1)^{m-1}\widetilde L(\rho)=(-1)^{m+\lceil m/2\rceil}=(-1)^{\binom m2}.
\]
The row-flip action is trivial by step 1, so the same sign holds for the combined reversal.

**4. Quotient consequence.** For a finite group acting simplicially, rational homology of the topological quotient identifies with the invariant subspace of rational homology of the original realization. The unique reduced homology line is invariant exactly when the reversal sign is positive. The assertion about the quotient follows; no statement about its integral torsion is made.

## Verification
A standalone Python program `verify_ladder.py` reconstructs perfect matchings from all monomer/domino tilings, enumerates every face, and computes the signed reduced simplicial traces for the identity, row flip, end reversal, and their product for each width \(2\le n\le12\). Independently, exact bit-matrix boundary ranks over \(\mathbb F_2\) confirm the predicted reduced homology through width \(8\). The recorded execution `verify_output.txt` reports 597,868 faces and 44 signed traces checked and ends in `VERIFY_OK`. These bounded calculations are corroboration, not the proof for unbounded width.

## Relationship to prior work
Chandrakar and Singh [1], Theorem 3.3, prove the nonequivariant homotopy types of these precise perfect-matching complexes. Their paper, including its main proof and appendix, was inspected; it does not give the integral actions of row interchange and column reversal. The preceding sphere/contractibility result is therefore credited, not claimed as original. Agarwal and Basak [2] treat Möbius and **circular** ladder perfect-matching complexes, not the linear path-based ladder or its geometric \(C_2\times C_2\) action. Separate work on ordinary matching complexes of linear grids concerns a different simplicial complex. The new contribution is the full integral reflection character, including the mod-eight orientation transition and quotient consequence.

## Limitations
The character formulas apply to the natural geometric symmetry group, not to all simplicial automorphisms. The nonequivariant homotopy types are previously known. The quotient consequence is rational only. The calculations are finite tests; the proof rests on the tiling retraction, fold lemma, and exact Lefschetz recurrence. Equivalently formulated or unpublished earlier equivariant work cannot be excluded solely by bibliographic searches. No independent external audit has been performed.

## References
[1] H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809 (first public 2024-07-08), Theorem 3.3, https://arxiv.org/html/2407.05809v2. Published in *Annals of Combinatorics* (2025), DOI 10.1007/s00026-025-00755-0.

[2] A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601 (2026), https://arxiv.org/html/2608.30601v2.
