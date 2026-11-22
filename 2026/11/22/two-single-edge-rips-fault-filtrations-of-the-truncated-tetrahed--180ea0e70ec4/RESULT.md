# Two single-edge Rips fault filtrations of the truncated tetrahedron and primitive integral survival

## Finding

For the truncated-tetrahedral graph \(T\), deleting one edge and recomputing graph distances gives two different complete integral Rips homotopy filtrations. If the deleted edge lies in a triangular truncation face, then
\[
\operatorname{VR}_{\le r}(T-e)\simeq
\begin{cases}
\coprod^{12}\{\mathrm{pt}\},&0\le r<1,\\
\bigvee^3 S^1,&1\le r<2,\\
\bigvee^3 S^2,&2\le r<3,\\
\mathrm{pt},&r\ge3.
\end{cases}
\]
If instead it joins two reversed ordered pairs, then
\[
\operatorname{VR}_{\le r}(T-e)\simeq
\begin{cases}
\coprod^{12}\{\mathrm{pt}\},&0\le r<1,\\
\bigvee^2 S^1,&1\le r<2,\\
\bigvee^2 S^2,&2\le r<3,\\
\mathrm{pt},&r\ge3.
\end{cases}
\]
At scale two there is a further integral statement: inclusion into the unpunctured graph's Rips complex induces **primitive injections**
\[
H_2(\operatorname{VR}_{\le2}(T-e);\mathbb Z)
\hookrightarrow H_2(\operatorname{VR}_{\le2}(T);\mathbb Z)\cong\mathbb Z^5,
\]
with free cokernel \(\mathbb Z^2\) for triangular faults and \(\mathbb Z^3\) for reversal faults. All groups and maps are integral; the homotopy statements are not merely numerical Betti calculations.

## Assumptions and scope

The twelve graph vertices are the ordered pairs \((a,b)\) with \(a,b\in\{0,1,2,3\}\) and \(a\ne b\). Distinct vertices \((a,b)\) and \((c,d)\) are adjacent if and only if \(a=c\) or \((c,d)=(b,a)\). Thus each first-coordinate fiber is a triangle, with twelve triangular edges in all; six reversal edges join different fibers. The graph has eighteen edges. Permuting the four symbols preserves adjacency and acts transitively on each type, so one representative of each type suffices for exhaustive verification. These are different graph-automorphism orbits, because only the triangular edges belong to a graph triangle.

The deleted-edge graph retains all twelve vertices. All distances are **recomputed in that new graph**, rather than inherited from the undamaged graph. At real threshold \(r\ge0\), the inclusive Vietoris–Rips complex contains each nonempty vertex set whose pairwise distances do not exceed \(r\). It is the clique complex of the integer-radius graph power. The natural inclusions into the intact Rips complex exist because deleting an edge cannot shorten any graph distance.

## Proof

**1. Edge orbits and exhaustive finite scope.** The ordered-pair graph has exactly twelve triangular and six reversal edges. Explicitly enumerating the twenty-four symbol permutations verifies that each class is one orbit. Select the triangular edge \(\{(0,1),(0,2)\}\) and reversal edge \(\{(0,1),(1,0)\}\). Breadth-first-search distances give diameters four and five, respectively. All simplices at any radius are checked among the \(2^{12}-1=4095\) nonempty vertex masks, so the calculation is exhaustive for this finite object and is not an extrapolation from a sample.

**2. Radius one.** The two fault types have simplex face vectors \((12,17,3)\) and \((12,17,4)\) in dimensions zero through two. All filled triangles admit elementary simplicial free-face collapses, after which the connected one-dimensional remainders have circle ranks three and two, respectively. The deterministic verifier also removes any additional free leaf pairs. The resulting graphs prove the radius-one homotopy types integrally.

**3. Radius two and fundamental groups.** The triangle-fault Rips complex has face vector \((12,40,42,10)\). Eighteen explicit *algorithmically determined and replayable* elementary free-face collapses leave a two-dimensional simplicial complex of face vector \((12,32,24)\). Choose the deterministic lexicographic spanning tree of its one-skeleton. The resulting fundamental-group presentation has twenty-one generators and twenty-four triangular relators. In a deterministic sequence, each of the twenty-one generators occurs alone (with sign) in a current relator, and is eliminated by setting it equal to the identity; the three remaining relators are empty. This exhibits the trivial fundamental group.

For a reversal fault, the radius-two face vector is \((12,37,38,10)\). Twenty-four elementary free-face collapses leave a two-dimensional complex of face vector \((10,23,16)\). Its spanning-tree presentation has fourteen generators and sixteen triangular relators; all fourteen generators are eliminated by singleton relators, leaving two empty relators. Thus it, too, is simply connected. In both cases the Euler characteristic is, respectively, four and three. A connected simply connected finite two-dimensional CW complex has free integral second homology of rank \(\chi-1\), and is homotopy equivalent to a wedge of that many two-spheres: choose maps representing an integral basis under Hurewicz, then apply the homological Whitehead theorem. This gives the two displayed sphere wedges, without inferring integral homotopy from mod-two ranks.

**4. Radius three and above.** The triangle-fault radius-three complex contains 2303 nonempty simplices and admits 1151 exact elementary free-face collapses to one vertex. For the reversal fault, the radius-three and radius-four complexes have 1087 and 3071 nonempty simplices, respectively; they collapse to a single vertex after 543 and 1535 free-face pairs. At the respective graph diameters four and five, the full simplex appears. Integer graph distances imply no other scale changes. Hence all thresholds from three onward are contractible, even where the graph has not yet reached its diameter.

**5. Primitive integral inclusion.** Orient each simplex by increasing ordered-pair vertex index. For the intact radius-two complex, the signed integer boundary matrices have ranks \(\operatorname{rank}\partial_2=31\) and \(\operatorname{rank}\partial_3=12\); its forty-eight two-faces therefore yield \(H_2\cong\mathbb Z^5\), as also established by the known homotopy classification. For the two fault types the signed \(\partial_2\) and \(\partial_3\) ranks are \((29,10)\) and \((26,10)\), giving free second-homology ranks three and two.

For each fault, exact integer unit-pivot row/column elimination constructs a **saturated integral basis** for \(\ker\partial_2\) inside its two-chain group. Embed those basis cycles in the intact two-chain group and append the columns of the intact \(\partial_3\) matrix. The combined integer matrices have ranks fifteen (triangular fault) and fourteen (reversal fault), and are reduced completely using *only unit pivots*; the residual matrix is zero. Thus their generated sublattices in the intact two-chain group are primitive. Since \(\ker\partial_2\) of the intact complex is itself primitive, the images in intact second homology are primitive as well. Subtracting the intact boundary rank twelve yields image ranks three and two. These equal the fault-group ranks, proving injectivity. The integral cokernel ranks are \(5-3=2\) and \(5-2=3\), with no torsion. The standalone verifier constructs and checks all matrices, the integer changes of basis, and their zero residuals from the graph definition.

## Verification

Execute `python3 verify.py` with Python 3 and its standard library only. The script reconstructs the ordered-pair graph; checks every symbol-permutation automorphism and edge orbit; recomputes all graph distances; enumerates all simplices; verifies each free-face pair against the **current** complex; computes and eliminates the actual fundamental-group relators; cross-checks mod-two boundary ranks; and performs integral row/column unit reductions to verify both primitive inclusion maps. It checks the exact remaining-dimensional cores and all higher-scale contractions. The terminal marker is `EXACT_RIPS_FAULT_VERIFICATION_OK`. The checks apply to the finite fixed graph and each of its two edge orbits, which cover all eighteen possible single-edge faults.

## Relationship to prior work

Saleh, Titz Mite and Witzel (2023) classify graph-metric Rips complexes for the five **Platonic** solids and explicitly identify Archimedean solids as a natural extension, but do not address a graph edge deleted from the truncated tetrahedron. A previously published graph-metric classification of the **intact** truncated tetrahedron gives \(\bigvee^5S^2\) at radius two, but neither edge-fault family nor their actual homology inclusion maps. Published Euclidean-distance results for the same twelve geometric vertices use chordal distances, unlike the recomputed graph metric here. A uniform cyclic-truncation recovery theorem assumes a **triangle-free base graph**; the underlying base here is \(K_4\), so that theorem cannot imply this edge-fault result. The published two-edge-orbit matching-complex classification concerns edge-set independence rather than vertex-set Vietoris–Rips complexes.

## Limitations

This is a complete exact classification for one natural twelve-vertex graph under **single** graph-edge deletions, not an infinite-family theorem. It does not determine homotopy maps between all scale stages, nor give a canonical basis for the primitive inclusion images. Primitive injections are proved only for the radius-two fault-to-intact inclusions. Searches of the inspected mathematical literature and indexed findings cannot exclude all unindexed equivalent calculations; no independent scientific audit has been carried out.

## References

1. N. Saleh, T. Titz Mite, and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1 (first public 2023-02-28), https://arxiv.org/html/2302.14388v1 .
2. W. Chachólski, A. Jin, M. Scolamiero, and F. Tombari, *Homotopical decompositions of simplicial and Vietoris Rips complexes*, *Journal of Applied and Computational Topology* 5 (2021), 215–248, https://doi.org/10.1007/s41468-021-00066-2 .
3. *The graph-metric Rips filtration of the truncated tetrahedron*, published mathematical result, 2026-10-04, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-the-graph-metric-rips-filtration-of-the-truncated-tetrahedron--51e8cc219376/RESULT.md .
4. *Sharp valence-five Rips recovery for cyclic vertex truncations*, published mathematical result, 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-valence-five-rips-recovery-for-cyclic-vertex-truncations--a77b1c9cfc91/RESULT.md .
5. *Euclidean Rips persistence and tetrahedral homology characters of the truncated tetrahedron*, published mathematical result, 2026-10-18, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-euclidean-rips-persistence-and-tetrahedral-homology-characters-o--1eada18dc7cc/RESULT.md .
6. *Edge-orbit matching-complex homotopy of the truncated tetrahedron*, published mathematical result, 2026-10-11, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-edge-orbit-matching-complex-homotopy-of-the-truncated-tetrahedro--f5ae4a359c83/RESULT.md .
