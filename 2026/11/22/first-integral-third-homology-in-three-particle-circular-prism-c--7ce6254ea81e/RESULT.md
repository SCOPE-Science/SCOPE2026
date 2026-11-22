# First integral third homology in three-particle circular-prism configurations

## Finding

For the circular prism \(P_n=C_n\square K_2\), let \(B_3(P_n)=\operatorname{UConf}_3(|P_n|)\) be the space of unordered triples of distinct particles in the geometric graph. Then
\[
H_3(B_3(P_n);\mathbb Z)\cong
\begin{cases}
0,&n=3,4,5,\\
\mathbb Z^2,&n=6.
\end{cases}
\]
At \(n=6\), the two integral generators are *geometric product tori*: one particle travels around each lateral square in the alternating triples of faces \(\{0,2,4\}\) and \(\{1,3,5\}\). These constitute a primitive integral basis, not only a rational spanning pair.

## Assumptions and scope

The graph \(P_n\) has vertex set \(\{(i,a):i\in\mathbb Z/n,\ a\in\{0,1\}\}\), with edges \((i,a)(i+1,a)\) and \((i,0)(i,1)\). The \(i\)-th lateral square has boundary \((i,0),(i+1,0),(i+1,1),(i,1)\). There is no hard-core metric requirement other than distinct positions. The statement concerns ordinary integral singular homology of the *unordered* configuration space, and only circumferences \(3\le n\le6\).

For the cubical model, subdivide each original graph edge once, producing \(G_n\), homeomorphic to \(|P_n|\). The vertices of original degree three are two edges apart in \(G_n\); nontrivial graph cycles have length at least six (at least eight for \(n\ge4\)). Thus the improved Abrams subdivision criterion for three particles applies: essential-vertex paths have length at least two and noncontractible cycles length at least four [1,2]. The unoriented discretized cubical complex \(UD_3(G_n)\) is homotopy equivalent to \(B_3(P_n)\).

## Proof

A \(k\)-cell of \(UD_3(G_n)\), for \(0\le k\le3\), is an unordered choice of \(k\) open graph edges and \(3-k\) vertices whose *closed* graph cells are pairwise disjoint. Fix an orientation of every subdivided graph edge from the lesser endpoint label to the greater. The cubical orientation uses the increasing tuple of edge indices. Its boundary in dimension three is exactly
\[
\partial_3(e_1,e_2,e_3)
 =\sum_{j=1}^3(-1)^{j-1}(\{v_j^+\}-\{v_j^-\})\times(e_1,\ldots,\widehat{e_j},\ldots,e_3),
\]
with cell reordering understood. There are no four-cells; hence \(H_3\cong\ker(\partial_3:\mathbb Z^{c_3}\to\mathbb Z^{c_2})\).

The standalone `verify_prism_top3.py` enumerates every admissible two- and three-cell and eliminates the *actual boundary matrix over* \(\mathbb F_2\), without probabilistic or floating-point steps. Its exact tuple \((c_2,c_3,\operatorname{rank}_{\mathbb F_2}\partial_3,\dim_{\mathbb F_2}\ker\partial_3)\) is
\[
\begin{array}{c|rrrr}
n&c_2&c_3&\operatorname{rank}_{\mathbb F_2}\partial_3&\dim_{\mathbb F_2}\ker\partial_3\\\hline
3&1386&432&432&0\\
4&3840&1296&1296&0\\
5&8190&2880&2880&0\\
6&14976&5400&5398&2
\end{array}
\]
Each nonzero minor modulo two is nonzero over \(\mathbb Q\). Consequently \(\dim_{\mathbb Q}\ker\partial_3\le0,0,0,2\) respectively. This proves vanishing for \(n=3,4,5\) and an upper bound of two at \(n=6\).

At \(n=6\), the mutually disjoint lateral squares at indices \(0,2,4\) form an embedded three-torus of independent simultaneous particle cycles, giving an integral cellular three-cycle \(T_e\). Likewise \(1,3,5\) gives \(T_o\). Each is the signed cubical product of three length-eight subdivided square boundaries, with exactly \(8^3=512\) nonzero three-cell coefficients. The checker reconstructs both signed cycles and verifies their entire integer boundaries vanish.

Select the cubical three-cell formed by the first subdivided top-rim edge in each face indexed \(0,2,4\); its signed coefficient is \(1\) in \(T_e\) and \(0\) in \(T_o\). The analogous cell for faces \(1,3,5\) has coefficients \((0,1)\). Thus the two coordinate evaluations give the identity matrix, proving \(T_e,T_o\) are linearly independent and their integral span is primitive. Since \(\dim_{\mathbb Q}\ker\partial_3\le2\), every integral three-cycle has a unique rational expression \(aT_e+bT_o\). Applying the two *integer-valued* coordinate evaluations forces \(a,b\in\mathbb Z\). Hence every integral three-cycle is in their span, establishing the claimed integral basis and exact \(\mathbb Z^2\).

## Verification

Run `python3 verify_prism_top3.py` with Python 3.10 or newer. The script specifies graph vertices and edges, constructs the cellular boundary, obtains the four exact finite ranks over \(\mathbb F_2\), forms the two 512-term signed product tori, tests both integer boundaries, and tests the displayed determinant-one evaluation matrix. It prints `PRISM_THREE_POINT_TOP_HOMOLOGY_OK` on success. The full computation requires neither external packages nor a network connection. The mod-two matrix alone proves the *rational upper bound*, not the integral basis; the two explicit integral tori and identity coordinate minor close that separate gap.

## Relationship to prior work

The sufficiently subdivided graph-cubical model rests on the classical theorem of Abrams and the extension by Prue–Scrimshaw [1,2]. Maciążek–Sawicki [3] study higher homology and product cycles of graph configuration spaces, including wheel and complete-bipartite examples; the present result isolates the three-particle circular-prism first-appearance threshold and primitive three-torus classes. Published two-particle prism calculations address a different particle number and homological degree. The precise claim was not located in the inspected sources; this is not a claim of exhaustive literature novelty.

## Limitations

No homology groups of degrees zero, one, or two are computed here. No assertion is made for circumferences greater than six, nor is a full cup-product or homotopy type classification offered. Enumeration and exact modular rank are finite certificates for the stated four graph sizes; they cannot justify an infinite-family extrapolation. An independently audited proof and exhaustive literature-priority search remain outstanding.

## References

[1] P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511 (first posted 2009-09-30), subsequently *Topology and its Applications* 178 (2014), 136–145. https://arxiv.org/abs/0909.5511

[2] A. Abrams, *Configuration spaces and braid groups of graphs*, PhD thesis, UC Berkeley (2000); the precise sufficient-subdivision conditions are also stated in [1].

[3] T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, *Communications in Mathematical Physics* 371 (2019), 921–973. https://doi.org/10.1007/s00220-019-03583-5
