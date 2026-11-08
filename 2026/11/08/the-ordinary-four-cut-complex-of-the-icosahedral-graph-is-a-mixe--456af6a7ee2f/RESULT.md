# The ordinary four-cut complex of the icosahedral graph is a mixed-dimensional sphere wedge

## Finding
Let \(I\) be the twelve-vertex icosahedral graph and \(\Delta_4(I)\) its ordinary four-cut simplicial complex. Then its **integral homotopy type** is
\[
\boxed{\Delta_4(I)\simeq\bigvee^{5} S^{6}\vee\bigvee^{20}S^{7}.}
\]
This complex is pure of dimension seven but not shellable. Its reduced integral homology is \(\mathbb Z^5\) in degree six, \(\mathbb Z^{20}\) in degree seven, and zero in every other degree; in particular, it is torsion-free.

The face counts in dimensions zero through seven are \((12,66,220,495,792,912,720,285)\). All twelve missing six-element simplices are exactly the complements of the twelve closed vertex neighborhoods in \(I\). This identifies a natural, symmetric obstruction to the otherwise complete five-skeleton.

## Assumptions and scope
Use vertices \(N,S,u_i,v_i\), where \(i\in\mathbb Z/5\mathbb Z\). The thirty edges are \(Nu_i\), \(Sv_i\), \(u_iu_{i+1}\), \(v_iv_{i+1}\), \(u_iv_i\), and \(u_iv_{i-1}\), for every \(i\). Thus each vertex has degree five and the graph is the ordinary regular-icosahedron graph. The standalone verifier labels \(N=0\), \(u_i=1+i\), \(v_i=6+i\) and \(S=11\), for indices \(i=0,1,2,3,4\).

By definition, a four-cut facet is the complement in the twelve vertices of a four-element subset \(T\) for which the induced subgraph \(I[T]\) is disconnected. Every face is a subset of one of these eight-element facets. This is the **ordinary** cut complex, not the total cut complex defined using independent four-sets.

## Proof
**Facets and faces.** Exhaustive enumeration of the \(\binom{12}{4}=495\) four-sets yields exactly 285 with disconnected induced graphs. Each produces one distinct eight-vertex facet. Taking all their subsets yields exactly 3503 simplices including the empty face, with the face counts in the finding. A second implementation tests all \(2^{12}=4096\) vertex subsets directly against the complementary four-subset criterion and gives precisely the same set. In addition, each of the twelve six-element nonfaces is the complement of \(\{w\}\cup N(w)\) for one graph vertex \(w\); these are all the missing six-element simplices. Hence the complex contains every face of dimension at most four, but not every face of dimension five.

**Acyclic integral Morse matching.** Represent each face by a twelve-bit mask. In the order \(0,1,\ldots,11\), pair all currently unmatched faces \(\sigma\) not containing the next vertex \(j\) with \(\sigma\cup\{j\}\), whenever both faces remain. This constructs 1738 disjoint pairs. Orient each matched Hasse cover from lower face to upper face and every other cover from upper to lower; a complete topological-sort check on all 3503 faces and 19536 incidences visits every face, so there is no directed cycle. The remaining unmatched faces are six in dimension six and twenty-one in dimension seven; there are no others, including in reduced dimension minus one.

**Integral attaching degrees.** For each matched pair \((a,b)\), the coefficient \([b:a]\) in the simplicial boundary is \(+1\) or \(-1\). To project a degree-six face to the surviving degree-six Morse cells, send an unmatched face to itself, a face paired down to zero, and a lower matched face \(a\) to the negative signed sum of the projections of the other facets of \(b\), divided by \([b:a]\). This recursion terminates because the matching has no directed cycles; all coefficients are integral. Applying the projection to the signed boundaries of the twenty-one critical seven-faces gives a \(6\)-by-\(21\) Morse boundary matrix having exactly **one nonzero column**, with only \(0\), \(+1\), and \(-1\) entries and at least one unit entry. Its Smith normal form therefore has precisely one nonzero invariant, equal to one.

The reduced Morse CW model has only the six six-cells and twenty-one seven-cells, with one primitive attaching map of degree vector generating a direct summand. Since its six-skeleton is a wedge of six six-spheres, the degree vector completely determines the homotopy class of each seven-cell attachment: \(\pi_6(\bigvee^6 S^6)\cong\mathbb Z^6\). Integral unimodular changes of bases reduce the attaching matrix to one identity entry. Its corresponding six/seven cell pair cancels up to homotopy, leaving five six-spheres and twenty seven-spheres wedged at a point. This proves the claimed *homotopy type*, not just its Betti numbers.

**Non-shellability.** The facets all have dimension seven. A pure shellable seven-dimensional simplicial complex has no reduced integral homology below dimension seven. Here \(\widetilde H_6\cong\mathbb Z^5\ne0\), so shellability is impossible.

## Verification
Run `python3 verify.py` with Python 3.9 or later, using only its standard library. The program tests every vertex subset, every matching incidence and the full acyclicity condition, computes the signed Morse differential over the integers, and independently obtains the mod-two simplicial boundary ranks \((11,55,165,330,462,450,265)\) in degrees one through seven. It also constructs a second acyclic Morse matching using the reverse vertex order, yielding the same reduced Betti numbers with an independently recomputed rational Morse rank. Its exact output is given in `verification_output.txt`.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue [1] introduced ordinary cut complexes and proved general results for several graph classes. Their Table 1 does not contain the icosahedron. Theorem 6.1 supplies a useful two-degree homology restriction when the complete next-to-top skeleton is present, but **does not apply here**: in degree six only 720 of the \(\binom{12}{7}=792\) possible faces occur. The sequel [2] treats disjoint unions, squared paths and grids, not the icosahedral graph.

A separate publicly available calculation [3] determines the **three-cut** complex of the same graph, \(\Delta_3(I)\simeq S^7\vee\bigvee^6 S^8\). That is a different simplicial complex. The inclusion \(\Delta_4(I)\subseteq\Delta_3(I)\) does not determine its integral homotopy type: in particular, it does not imply the five six-dimensional and twenty seven-dimensional sphere summands established here. The present computation therefore resolves a distinct natural cut level without invoking a classification for all cut parameters.

## Limitations
The statement concerns only the ordinary four-cut complex of the explicitly defined icosahedral graph. It does not classify other cut levels, all Platonic graphs, homology representations under the icosahedral group, or an equivariant wedge decomposition. It makes no claim that a literature search proves global uniqueness; unindexed equivalent computations remain possible. The finite algorithms check every face and matched incidence but do not constitute a proof of a broader infinite family.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public version 2023-04-26; *SIAM J. Discrete Math.* 38 (2024), 1630–1675.

[2] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first public version 2024-07-11.

[3] *The icosahedral three-cut complex is a mixed-dimensional sphere wedge*, publicly indexed finding dated 2026-10-11, opaque identifier `fb104995d472` (scientific content of `RESULT.md` inspected).
