# Four-robust square-grid complexes: \(84\) and \(560\) five-spheres and their dihedral characters

## Finding
Let \(G_n=P_n\square P_n\) be the Cartesian product of two \(n\)-vertex paths, and let \(K_n=\mathsf{Cliq}_4(G_n)\) be its four-robust clique complex: a set \(W\) of grid vertices is a simplex if and only if the induced graph \(G_n[W]\) has no independent set of four vertices. Let \(F_n\) be the set of \((n-1)^2\) unit square faces, with the natural action of the dihedral group \(D_4\).

**Theorem (exactly \(n=4,5\)).** The ordinary integral homotopy types are
\[
K_4\simeq \bigvee^{84}S^5,\qquad K_5\simeq\bigvee^{560}S^5.
\]
Moreover the natural **rational**, not asserted integral, homology representations are
\[
\widetilde H_5(K_n;\mathbb Q)\cong_{\mathbb Q[D_4]}
\det_{D_4}\otimes\mathbb Q\!\left[\binom{F_n}{3}\right],
\qquad n\in\{4,5\}.
\]
Here \(\det_{D_4}\) is \(+1\) on quarter-turns and half-turns and \(-1\) on reflections, and \(\binom{F_n}{3}\) denotes all unordered triples of distinct square faces. All other reduced integral homology groups vanish. In particular, using rational transfer for a finite group action, the displayed characters' invariant dimensions give \(\dim_{\mathbb Q}\widetilde H_5(|K_4|/D_4;\mathbb Q)=6\) and \(\dim_{\mathbb Q}\widetilde H_5(|K_5|/D_4;\mathbb Q)=63\); other reduced rational quotient groups vanish.

The ordered character values for \((1,r,r^2,r^3,h,v,d,a)\) — the identity, three rotations, horizontal and vertical mirrors, and the two diagonal mirrors — are
\[
\chi_4=(84,0,4,0,-10,-10,-10,-10),
\qquad\chi_5=(560,0,0,0,0,0,-28,-28).
\]
These two finite grid sizes are the **entire** claimed parameter range; no all-grid theorem is claimed.

## Assumptions and scope
The graph \(G_n\) has vertex set \(\{0,\ldots,n-1\}^2\); vertices are adjacent exactly at Manhattan distance one. The complex is the full abstract simplicial complex on the specified admissible vertex sets. We use reduced integral and rational simplicial homology, and geometric square symmetries act by permuting grid vertices. The group \(D_4\) has eight elements, with the conventions defined in `verify.py`. The grid sizes are only \(n=4\) and \(n=5\).

## Proof
**1. Finite exhaustive face universe.** Every grid is bipartite by checkerboard parity. A vertex subset of size at least seven contains at least four vertices in one color class, forming an independent four-set. Thus every face of \(K_n\) has at most six vertices. The finite face enumeration therefore exhausts all faces by examining subsets of cardinality at most six, rather than truncating a potentially higher-dimensional complex. The program `verify.py` checks admissibility using the exact independence-number recurrence
\[
\alpha(W)=\max\{\alpha(W\setminus\{v\}),
1+\alpha(W\setminus(\{v\}\cup N(v)))\},\quad\alpha(\varnothing)=0,
\]
where \(v\) is the smallest-indexed vertex of \(W\). It **independently** tests every four-, five-, and six-vertex subset by checking its four-element subsubsets for independence; the two implementations agree. It enumerates \(4,811\) and \(27,597\) nonempty faces respectively.

**2. Exact discrete-Morse certificate.** On the nonempty face poset, process vertex positions \(v=0,\ldots,n^2-1\) in ascending order. For each currently unmatched face \(a\) in increasing bitmask order, if \(v\notin a\) and \(b=a\cup\{v\}\) is also unmatched, pair \((a,b)\) and remove both. This specifies the complete matching without omitted choices. To prove it is acyclic rather than rely on the visual shape of a matching, the verifier constructs **every** codimension-one Hasse incidence \(b\supset a\ne\varnothing\), directs it downward \(b\to a\) unless it belongs to the matching, and directs matched incidences upward \(a\to b\). Kahn's exact topological-order procedure visits every vertex of this directed graph. It therefore has no directed cycles. The full results are:

| Grid | Nonempty faces | Matching pairs | Critical cells | Hasse incidences | Topologically ordered vertices |
|---|---:|---:|---|---:|---:|
| \(4\times4\) | 4,811 | 2,363 | one 0-cell and 84 5-cells | 21,992 | 4,811 |
| \(5\times5\) | 27,597 | 13,518 | one 0-cell and 560 5-cells | 130,886 | 27,597 |

By the discrete Morse theorem, each simplicial complex has a CW model with exactly one zero-cell, the listed number of five-cells, and no other cells. Every five-cell has a constant attaching map because the lower skeleton is a single point. This gives the claimed **integral homotopy** wedges directly, without assuming rational homology determines homotopy.

**3. Equivariant rational character.** For a grid symmetry \(g\), compute the reduced Lefschetz number by summing \((-1)^{|W|-1}\operatorname{sgn}(g|_W)\) over all nonempty \(g\)-invariant faces \(W\), with an additional \(-1\) from the augmentation (the empty face). This is the signed simplicial-chain trace, and hence the reduced homology alternating trace. The previous step shows that the only nonzero reduced homology degree is five; consequently \(\operatorname{tr}(g|\widetilde H_5)\) is **minus** this reduced Lefschetz number. The verifier calculates all eight values by exact finite enumeration. Independently, it permutes the \((n-1)^2\) geometric square faces, counts invariant unordered triples, and multiplies by the planar orientation determinant. The two eight-value characters agree exactly and have the displayed values. Since finite-dimensional rational representations of finite groups are characterized by their characters in characteristic zero, the stated rational \(D_4\)-module isomorphisms follow. Summing character values and dividing by eight proves the two quotient ranks.

The verifier is a standalone Python program using only the standard library. Each numerical assertion above is checked by its source, not by reading a previously generated log.

## Verification
Run `python3 verify.py` in the directory containing this document. The machine-readable log is `verification_output.txt`, obtained from that exact standalone file. It reports `ALL_VERIFY_OK: n=4,5; 16 characters; exhaustive acyclic Morse matching and independent face test`. These finite certificates are logically exhaustive because of the six-vertex bound, and the program checks the complete directed matching graph rather than estimating homology from a sampled face subset.

## Relationship to prior work
M. Filakovský's arXiv:2602.11365v4, Theorem 1, establishes wedge classifications of \(k\)-robust clique complexes of arbitrary rectangular grids for \(k=2,3\); Corollary 3 extends to arbitrary \(k\) **under edge-only square gluing**. General square grids with three or more rows require corner gluing. Conjecture 5 explicitly proposes that the wedge phenomenon persists for larger \(k\). Our finite \(k=4\) conclusions address this previously open corner-gluing regime for the two specified square grids and add full rational dihedral characters. Earlier computations already treat the smaller \(3\times3\) grid, which is excluded from our claim. A three-robust all-bipartite theorem does not cover \(k=4\).

## Limitations
The result proves only the two finite grid sizes \(n=4,5\). It neither proves Conjecture 5 for general grids nor identifies a canonical integral equivariant basis, an equivariant wedge decomposition, or integer homology of quotient spaces. The character comparison yields a rational, not integral, representation isomorphism. The finite certificate has undergone local execution and direct logical review but not independent mathematical validation. Undetected equivalent literature remains a residual originality risk.

## References
1. M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first posted 2026-02-11, version 4 dated 2026-08-10. https://arxiv.org/html/2602.11365v4 (Theorem 1, Corollary 3, Conjecture 5).
2. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete Morse CW theorem).
3. Standard rational Lefschetz trace formula and Maschke's character criterion for finite group representations.
