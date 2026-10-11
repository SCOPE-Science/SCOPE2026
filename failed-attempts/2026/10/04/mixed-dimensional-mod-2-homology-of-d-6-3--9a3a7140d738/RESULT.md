# Mixed-dimensional mod-2 homology of \(D_{6,3}\)
## Finding
For the simplicial complex \(D_{6,3}\) of simple graphs on six labeled vertices whose domination number is at least \(3\), the reduced mod-2 homology is \(\widetilde H_4(D_{6,3};\mathbb F_2)\cong \mathbb F_2^{115}\) and \(\widetilde H_5(D_{6,3};\mathbb F_2)\cong \mathbb F_2^{24}\), with all other reduced homology groups zero. Consequently, \(D_{6,3}\) is not homotopy equivalent to a wedge of spheres all having one common dimension.

The unreduced mod-2 Betti vector in dimensions \(0\) through \(6\) is
\[
(1,0,0,0,115,24,0).
\]
Thus the first boundary case singled out in the source after the equidimensional wedge results has homology in two adjacent positive dimensions.

## Assumptions and scope
For a simple graph \(G\) on the fixed vertex set \(\{0,1,2,3,4,5\}\), a set \(S\) of vertices dominates \(G\) when every vertex outside \(S\) has a neighbor in \(S\). The domination number \(\gamma(G)\) is the minimum cardinality of a dominating set. The abstract simplicial complex \(D_{6,3}\) has the fifteen edges of \(K_6\) as its vertices; a nonempty edge set \(E\) is a simplex exactly when the graph \(G_E\) satisfies \(\gamma(G_E)\ge 3\). Coefficients in the finding are the field \(\mathbb F_2\).

The claim is finite and exact. It does not assert the integral homology, simple-homotopy type, or full homotopy type of \(D_{6,3}\), and it does not assert that the space is a wedge of spheres of mixed dimensions.

## Proof
There are \(2^{15}=32768\) simple labeled graphs on six fixed vertices. Exhaustive evaluation of the domination condition gives \(4502\) nonempty simplices in \(D_{6,3}\), with face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6)=(15,105,455,1185,1647,915,180).
\]
The resulting Euler characteristic is \(92\), agreeing with the independent value reported for this complex in the source literature.

Over \(\mathbb F_2\), order the simplices in each dimension by their edge-set bit masks and form the ordinary simplicial boundary maps. Exact binary Gaussian elimination gives
\[
(\operatorname{rank}\partial_1,\ldots,\operatorname{rank}\partial_6)
=(14,91,364,821,711,180).
\]
Therefore
\[
\beta_d=f_d-\operatorname{rank}\partial_d-\operatorname{rank}\partial_{d+1},
\]
with the endpoint ranks interpreted as zero, yields
\[
(\beta_0,\ldots,\beta_6)=(1,0,0,0,115,24,0).
\]
Hence the reduced homology is nonzero precisely in dimensions \(4\) and \(5\), with the ranks stated in the finding. A wedge of spheres all of a single dimension has reduced homology concentrated in that single dimension, so such a homotopy type is impossible for \(D_{6,3}\).

## Verification
`verify_d63.py` uses only the Python standard library. It independently implements the membership condition in two ways: first by searching all vertex subsets for the domination number, and second by directly ruling out dominating sets of cardinality one or two. It checks agreement on all \(32768\) graphs, downward closure, the complete face vector, a canonical SHA-256 digest of all nonempty faces, every mod-2 boundary-square identity, all six boundary ranks, the Betti vector, and the Euler characteristic. A successful replay ends with `VERIFY_OK`.

The canonical digest of the sorted nonempty face masks is `c69ad65ef152dfa4b2ec2a790d2d2bc7290d3aa0ac3a096dd2aac17e7c7f60d7`.

## Relationship to prior work
González and Hoekstra-Mendoza define the same complexes \(D_{n,\gamma}\), prove equidimensional wedge-of-spheres results for \(D_{n,n-2}\), compute \(D_{5,2}\simeq \bigvee^4 S^5\), and explicitly single out \(D_{6,3}\) as the next obstruction to a straightforward extension. Their full text reports only \(\chi(D_{6,3})=92\) and asks whether these graph complexes are wedges of spheres and whether mixed sphere dimensions can occur. It does not state the mod-2 Betti numbers above. The present calculation sharpens their Euler-characteristic evidence: the homology itself already occupies two distinct positive dimensions, so the earlier equidimensional-wedge pattern cannot extend to \(D_{6,3}\).

Exact searches for the notation \(D_{6,3}\), bounded-domination graph complexes, the Betti pair \(115,24\), and equivalent domination-complex descriptions found the source paper but no later statement implying these ranks. This is evidence relative to the checked literature, not an absolute novelty guarantee.

## Limitations
The calculation is over \(\mathbb F_2\). It does not determine torsion over \(\mathbb Z\), attaching maps, or whether \(D_{6,3}\) is homotopy equivalent to a mixed-dimensional wedge such as a wedge containing \(4\)- and \(5\)-spheres. An obscure or unindexed computation of the same finite complex remains a residual literature risk.

## References
1. J. González and T. I. Hoekstra-Mendoza, “On the homotopy type of complexes of graphs with bounded domination number,” arXiv:1901.07130v1, first public 22 January 2019; Contributions to Discrete Mathematics 16(3), 2021, doi:10.55016/ojs/cdm.v16i3.72114.
