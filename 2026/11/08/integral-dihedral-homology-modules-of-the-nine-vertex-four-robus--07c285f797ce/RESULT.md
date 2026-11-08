# Integral dihedral homology modules of the nine-vertex four-robust grid and its total-cut dual

## Finding
Let \(G=P_3\square P_3\) be the ordinary nine-vertex square grid, with vertices \((r,c)\), where \(0\le r,c\le2\), and edges between lattice points at Manhattan distance one. Let \(K=\mathsf{Cliq}_4(G)\) be the simplicial complex whose faces are vertex sets containing no independent four-set. Let \(T=\Delta_4^t(G)\) be its combinatorial Alexander dual, whose facets are complements of independent four-sets. Let \(D_4\) act by square symmetries, and let \(\mathcal Q\) be the set of four elementary unit squares of the grid.

**Equivariant theorem.** As integral \(D_4\)-modules,
\[
\widetilde H_5(K;\mathbb Z)\cong \det\otimes\mathbb Z[\mathcal Q],\qquad
\widetilde H_1(T;\mathbb Z)\cong\mathbb Z[\mathcal Q].
\]
Here \(\det\) assigns \(+1\) to rotations and \(-1\) to reflections, and \(\mathbb Z[\mathcal Q]\) is the free integral permutation lattice on unit squares. Equivalently the five-dimensional character of \(K\) is \(\det(g)\,|\mathcal Q^g|\), while the one-dimensional character of \(T\) is \(|\mathcal Q^g|\). The lattice isomorphisms are **integral**, not merely equalities of rational characters. The displayed character formulas follow by tensoring with \(\mathbb Q\).

The complete nonequivariant homotopy type \(K\simeq\bigvee^4S^5\) is also certified below; its numerical rank is **not** claimed as new, since the corresponding total-cut Betti number was already tabulated.

## Assumptions and scope
All complexes are ordinary finite abstract simplicial complexes. The vertex numbering for reproducibility is \(v=3r+c\), with \(0\le r,c\le2\). A nonempty face is encoded by its nine-bit vertex mask; the empty face is not used in the Morse matching. The symmetric group action is the standard dihedral action of the geometric square, not a larger automorphism group. The claimed modules are over \(\mathbb Z\); rational characters are used as checks, not as a substitute for the integral lattice proof. The source publication date for this topic is the first public version of Filakovský's 2026 robust-clique manuscript, rather than its subsequent revisions.

## Proof
**1. Exact face enumeration and homotopy control.** A four-set is forbidden precisely when none of its six vertex pairs is a grid edge. Direct testing of all \(\binom94=126\) four-sets yields exactly six forbidden independent four-sets. Of the \(2^9-1=511\) nonempty subsets, exactly 389 avoid all six. The numbers of faces by increasing dimension are \((9,36,84,120,100,40)\).

The same complex is independently recovered from bipartite maximum matchings: König's theorem and \(\alpha(G[W])=|W|-\nu(G[W])\) give the face condition \(|W|-\nu(G[W])\le3\). The executable compares all 511 subset decisions by these two mathematically distinct tests.

On the nonempty face poset, process vertices \(v=0,1,\ldots,8\). At stage \(v\), pair each still-unmatched face not containing \(v\) with the still-unmatched face obtained by adding \(v\), when both exist. This is a sequence of element matchings. The exact certificate finds 192 pairs and only five critical masks \(1,252,444,492,504\), the first of dimension zero and the remaining four of dimension five. It checks every cover incidence, reverses matching arrows, and topologically sorts the full directed Hasse graph of 389 nodes and 1544 arrows. The graph is acyclic. Forman's theorem therefore produces a CW model with one zero-cell and four five-cells, and no other cells. Thus \(K\simeq\bigvee^4S^5\), over the integers.

**2. The integral homology lattice and its dihedral action.** The standard orientation of each simplex is induced by ascending vertex labels. For every geometric symmetry \(g\), the exact simplicial chain Lefschetz number is
\[
L(g)=\sum_{\substack{\varnothing\ne\sigma\in K\\g\sigma=\sigma}}(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma).
\]
Here \(\operatorname{sgn}(g|_\sigma)\) is the sign of the induced permutation relative to the ascending vertex order. Because all positive reduced homology is concentrated in degree five, \(\operatorname{tr}(g|\widetilde H_5(K;\mathbb Q))=1-L(g)\). For identity, quarter-turns, half-turn, horizontal/vertical reflections, and diagonal reflections, respectively, the trace values are \(4,0,0,0,-2\); the two diagonal reflections each have trace \(-2\). These agree, element by element, with \(\det(g)|\mathcal Q^g|\). This character calculation independently checks the integral claim, but does not by itself establish an integral module isomorphism.

For the integral refinement, enumerate the 36 matched five-simplices and their 36 matched four-dimensional ridges. The corresponding integer boundary submatrix has determinant \(1\), computed by exact fraction-free elimination in `verify.py`. The attached `integral_certificate.json` lists four explicit integral five-cycles, each supported on 16 five-simplices; the checker verifies all 100 signed four-dimensional boundary coefficients vanish and that their four critical top-face coordinates form the identity matrix. Unimodularity of the matched submatrix shows that the critical top coordinates identify the entire integral fifth homology with \(\mathbb Z^4\), making these four cycles an integral basis.

Let \(z_1,z_2,z_3,z_4\) be those cycles and put \(x=-z_1-z_2-z_3-z_4\). If \(r\) is the geometric quarter-turn and \(s\) the main-diagonal reflection, the exact chain action satisfies \(s(x)=-x\), while \(x,r(x),r^2(x),r^3(x)\) has determinant \(-1\) in the integral cycle basis. Thus this orbit is itself a \(\mathbb Z\)-basis. These two generator relations are precisely the determinant-twisted permutation action on the four unit squares (choose one square fixed by the diagonal reflection); hence the first integral isomorphism holds, without a rational-to-integral inference.

**3. Integral character of the dual total-cut complex.** By combinatorial Alexander duality on nine vertices, the sole nonzero reduced integral homology of \(T\) is \(\widetilde H_1(T;\mathbb Z)\cong\mathbb Z^4\). The equivariant Alexander-duality transformation includes the sign of the permutation of the ambient nine vertices, which for these eight symmetries equals \(\det(g)\). Integral equivariant Alexander duality, with the natural perfect dual pairing on free homology, therefore identifies the dual lattice with \(\det\otimes(\det\otimes\mathbb Z[\mathcal Q]^*)\cong\mathbb Z[\mathcal Q]\); the permutation lattice is canonically self-dual over \(\mathbb Z\). To avoid relying solely on that convention, the executable reconstructs all 121 nonempty dual faces independently and directly recomputes their signed Lefschetz numbers. It finds first-homology traces \(4,0,0,0,2\), matching the square permutation character. Complete mod-two chain-rank calculations give reduced Betti ranks four in degrees five and one for \(K\) and \(T\), respectively.

## Verification
Run `python3 verify.py` with the standard Python library. It reconstructs all faces, the exact matching, all 1544 Hasse incidences, all eight signed chain characters, the Alexander dual, and both mod-two Betti vectors. The supplied `verify_output.txt` records a successful run ending in `ALL_VERIFY_OK`. The executable is a complete finite witness: its acyclicity test checks the full directed graph, not a sample. The homotopy conclusion uses the discrete-Morse theorem; the representation conclusion uses the Lefschetz formula and semisimplicity over \(\mathbb Q\), rather than finite extrapolation.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue (2022/2024), Table 2, **already give** the numerical Betti number \(\widetilde\beta_1(\Delta_4^t(P_3\square P_3))=4\). Via Alexander duality and standard connectivity arguments, this data can imply the nonequivariant four-sphere homotopy type of the robust complex. Neither the number four nor that elementary implication is claimed as new.

Chandrakar, Hazra, Rout and Singh (2024/2026) prove the entire total-three-cut grid family, not the total-four-cut equivariant module. Filakovský (first public 2026-02-11) proves two- and three-robust grid homotopy types and higher-robust results for solely edge-glued square sequences. His higher-parameter corner-gluing statement remains a conjecture; the last square in the three-by-three grid requires corner gluing. Carnero Bravo (2026) treats other graph families and Cartesian-grid total-two-cut complexes. The explicitly certified integral dihedral permutation-lattice isomorphisms refine, rather than rediscover, the known scalar Betti number. No claim is made about a general grid family, a general family formula, or an equivariant homotopy equivalence.

## Limitations
This result concerns only \(P_3\square P_3\) at robust threshold four. The action on integral homology is determined, but an equivariant homotopy equivalence is not asserted. The proof does not settle higher-robust grid conjectures generally. Literature searches and inspection of named primary manuscripts cannot rule out all unindexed parallel calculations. The dual homotopy type is not asserted to be a wedge of circles: only its first integral homology and integral symmetry action are determined.

## References
1. Marek Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first submitted 2026-02-11, especially Theorem 1, Corollary 3, Conjecture 5 and Definition 9. https://arxiv.org/abs/2602.11365
2. Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram and Lei Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first submitted 2022-09-27, Table 2, section 5 and Appendix. https://arxiv.org/html/2209.13503v2
3. Himanshu Chandrakar, Nisith Ranjan Hazra, Debotosh Rout and Anurag Singh, *Topology of total cut complexes and cut complexes of grid graphs*, arXiv:2408.07646, first submitted 2024-08-14, Theorem 1.1. https://arxiv.org/html/2408.07646v3
4. Andrés Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, first submitted 2026-02-24, introduction and section on Cartesian products. https://arxiv.org/abs/2602.21427
