# A torus phase for two-pair avalanches on directed cycles

## Finding
Let \(d\ge3\) and \(n\ge2d+3\) be integers. On the forward directed cycle \(\overrightarrow C_n\), initialize parallel chip firing with one grain at each of the four vertices \(\{0,1,d,d+1\}\subseteq\mathbb Z/n\mathbb Z\) and zero elsewhere. Write \(\mathcal A_{n,d}\) for the avalanche complex: its faces are all subsets of firing sets occurring at any nonnegative time. Then \(\mathcal A_{n,d}\) admits exactly \(2n\) explicitly specified elementary simplicial collapses onto a connected, oriented triangulated torus. Consequently
\[
|\mathcal A_{n,d}|\simeq S^1\times S^1,\qquad
H_k(\mathcal A_{n,d};\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,2,\\
\mathbb Z^2,&k=1,\\
0,&\text{otherwise}.
\end{cases}
\]
Its integral cohomology ring has two degree-one generators with nonzero product generating degree two. The lower bound is one-sided sharp: at \(n=2d+2\), the same two-pair configuration has avalanche-complex Euler characteristic \(d+1\), so it is not homotopy equivalent to a torus. No classification for smaller \(n\) is claimed.

## Assumptions and scope
The cycle has distinct vertices \(\mathbb Z/n\mathbb Z\) and exactly the arcs \(i\to i+1\pmod n\). Parallel firing occurs whenever the chip count is at least the outdegree, which equals one; each firing vertex sends one grain along its sole outgoing arc. The initial vector is binary, with precisely four ones at \(0,1,d,d+1\). For the torus assertion the integer parameters satisfy \(d\ge3\) and \(n\ge2d+3\), and the contrast at the immediately preceding value \(n=2d+2\) is separately stated. All geometric realizations and homology groups are unreduced unless marked otherwise.

## Proof
**1. Exact firing sets.** Every occupied vertex fires simultaneously, sends exactly one grain to its successor and becomes empty. Therefore the new binary occupied support is the old one translated by one. By induction, at time \(i\) the firing set is
\[
F_i=\{i,i+1,i+d,i+d+1\}\pmod n.
\]
The family is periodic modulo \(n\); hence \(\mathcal A_{n,d}\) is exactly the downward closure of the tetrahedral facets \(F_i\) for \(i\in\mathbb Z/n\mathbb Z\). In the asserted ranges each orbit facet is distinct. For example, the two consecutive edges within a facet are separated by unequal cyclic gaps, and no nonzero rotation preserves this pair pattern.

**2. Two families of elementary collapses.** Throughout \(d\ge3\), \(n\ge2d+2\), the unoriented edge lengths \(1,d-1,d,d+1\) are distinct (interpreting lengths modulo \(n\) up to sign); the length \(d-1\) is strictly below \(n/2\). Each edge
\[
e_i=\{i+1,i+d\}
\]
therefore belongs to the unique tetrahedron \(F_i\). The triangle \(a_i=\{i,i+1,i+d\}\) is a free codimension-one face of \(F_i\). Remove the pair \((a_i,F_i)\) for every \(i\), in any order. After these \(n\) collapses, \(e_i\) occurs in precisely the one remaining triangle \(b_i=\{i+1,i+d,i+d+1\}\). Remove each pair \((e_i,b_i)\). These are \(2n\) valid elementary collapses; the resulting two-dimensional complex \(L_{n,d}\) has exactly the triangles
\[
A_i=\{i,i+1,i+d+1\},\qquad
B_i=\{i,i+d,i+d+1\}
\quad(i\in\mathbb Z/n\mathbb Z).
\]
Every lower-dimensional face is retained when contained in one of these triangles, and no other face remains. Thus \(\mathcal A_{n,d}\searrow L_{n,d}\), preserving simple-homotopy type.

**3. The stable range is a torus.** Assume \(n\ge2d+3\). The three unoriented edge-length classes \(1,d,d+1\) of \(L_{n,d}\) are pairwise distinct and strictly below \(n/2\). Their sets each contain \(n\) edges; the \(2n\) displayed triangles are pairwise distinct. Therefore
\[
(f_0,f_1,f_2)=(n,3n,2n),\qquad \chi(L_{n,d})=0.
\]
More strongly, the link of vertex \(i\) is the six-cycle with successive neighbors
\[
i+1,\ i+d+1,\ i+d,\ i-1,\ i-d-1,\ i-d
\]
(all indices modulo \(n\)). These six neighbors are distinct because \(d\ge3\) and \(n\ge2d+3\). Consequently \(L_{n,d}\) is a closed triangulated surface. In fact, these are exactly the facets of the previously studied weakly regular torus \(T_{n,1,d}\) in Datta–Upadhyay, Example 1, not a newly discovered surface triangulation. It is connected because it contains all cycle edges \(\{i,i+1\}\). Orient its triangles consistently by giving \(A_i\) the order \((i,i+1,i+d+1)\) and \(B_i\) the order \((i,i+d+1,i+d)\). Every edge occurs twice with opposing induced directions: for length \(1\), compare \(A_i\) with \(B_{i-d}\); for length \(d\), compare \(B_i\) with \(A_{i-1}\); for length \(d+1\), compare \(A_i\) and \(B_i\). Thus the surface is orientable. Classification of connected closed orientable surfaces and \(\chi=0\) give \(|L_{n,d}|\cong S^1\times S^1\). Elementary collapse preserves homotopy type and integral cohomology rings, proving the torus result and the nonzero cup product.

**4. The boundary contrast.** At \(n=2d+2\) the same elementary collapse proof applies, but the edge class of length \(d+1=n/2\) contains only \(n/2\) edges. The other two edge classes contain \(n\) edges each, while the \(2n\) triangles remain distinct. Hence
\[
\chi(\mathcal A_{2d+2,d})=\chi(L_{2d+2,d})
=n-\left(2n+\frac n2\right)+2n
=\frac n2=d+1.
\]
For \(d\ge3\), this differs from the torus Euler characteristic zero. This proves the claimed one-sided sharpness, without asserting a full boundary homotopy classification.

## Verification
Execute `python3 verify.py` with Python 3.10 or later, using no third-party dependencies. The script regenerates all simultaneous firing sets for sampled cycles, enumerates the entire original face poset, performs the prescribed \(2n\) collapses with explicit free-face incidence checks, and compares the surviving complex to the two displayed triangle families. It verifies every residual vertex link, opposite edge orientations, face counts, Euler characteristics, and exact mod-two boundary ranks in representative cases. Its recorded output in `verification_output.txt` is:

`ALL_VERIFY_OK torus_cases=575 boundary_cases=23 dynamics_cases=49 homology_cases=49 d_range=3..25 n_range_each=2d+2..2d+27`

The finite experiments are checks, not the proof of the universal parameter statement. The proof above establishes all integer cases in the stated domains.

## Relationship to prior work
Riihimäki and Smith (2026, arXiv:2606.26786, first public 2026-06-25) introduce avalanche complexes and prove cycle classifications for consecutive occupied blocks and certain three-grain supports (especially their Theorem 3.32 and Proposition 3.34 in version 2); their Question 3.36 asks for homotopy-type stratification by initial configuration. The separated two-pair four-grain configuration and the present torus collapse are not among those inspected classifications. The argument here uses their avalanche-complex definition but derives the firing sets and all subsequent topology directly.

The surviving triangulation is **exactly** \(T_{n,1,d}\) of Datta and Upadhyay (arXiv:math/0403433, Example 1), whose torus topology was already established. That two-dimensional result is acknowledged as a known target, not claimed as new. Jevtić and Živaljević (arXiv:2002.09184, Definition 1.3 and Theorem 1.5) study the larger complexes formed by all permutations of a length vector and obtain higher-dimensional tori for generic vectors. Our four-grain complex takes a single translation orbit with cyclic gaps \((1,d-1,1,n-d-1)\), a nongeneric vector with two repeated lengths; their generic theorem does not imply this simple-homotopy collapse. Relevant full-text sections of both papers and the original avalanche paper were inspected. A different unindexed equivalence remains a possible priority risk. The new point is the explicit \(2n\)-step collapse of the three-dimensional firing-orbit complex to the known cyclic torus and the sharp change at the antipodal boundary.

## Limitations
The theorem assumes four binary grains in precisely two adjacent occupied pairs, a forward directed cycle, and parallel threshold-one firing. It does not classify arbitrary four-grain supports, arbitrary directed graphs, avalanche persistence, or the full topology of the boundary case. The one-sided threshold is sharp only relative to the immediately preceding \(n=2d+2\) configuration, not a claim about all smaller cycle lengths. Independent mathematical audit has not been performed.

## References
1. H. Riihimäki and J. P. Smith, *Avalanche homology of digraphs via sandpile dynamics*, arXiv:2606.26786, first public 2026-06-25. https://arxiv.org/abs/2606.26786 ; accessible full text https://www.researchgate.net/publication/408106934_Avalanche_homology_of_digraphs_via_sandpile_dynamics
2. B. Datta and A. K. Upadhyay, *Degree-regular triangulations of torus and Klein bottle*, arXiv:math/0403433 (2004). https://arxiv.org/abs/math/0403433
3. F. D. Jevtić and R. T. Živaljević, *Generalized Tonnetz and discrete Abel-Jacobi map*, arXiv:2002.09184 (2020). https://arxiv.org/abs/2002.09184
