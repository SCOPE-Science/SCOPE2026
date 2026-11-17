# An abelian fundamental group born under one stacking of a five-sphere double

## Finding

Let \(X\) be the first nontrivial stacked simplicial five-sphere: start with the boundary of a six-simplex on the vertices \(0,\ldots,6\) and stack a new vertex \(7\) on its facet \(\{0,1,2,3,4,5\}\). For the Lesh–Schreiner–Wahl double, a simplex is a family of pairwise disjoint edges of \(X\) whose union is itself a face of \(X\). Then

\[
\pi_1(|D^2(X)|)\cong\mathbb Z^5,
\qquad
\widetilde H_i(D^2(X);\mathbb Z)=
\begin{cases}
\mathbb Z^5,&i=1,\\
\mathbb Z^{46},&i=2,\\
0,&\text{otherwise}.
\end{cases}
\]

In particular the double is connected but not simply connected, and its fundamental group is abelian. This is an integral statement; no wedge-of-spheres homotopy classification is asserted.

## Assumptions and scope

Write \(V=\{0,\ldots,7\}\), \(B=\{0,\ldots,5\}\). The twelve maximal simplices of \(X\) are precisely \(\{0,\ldots,6\}\setminus\{i\}\) and \(\{7\}\cup(B\setminus\{i\})\), each for \(0\le i\le5\). This defines a triangulated five-sphere by one ordinary facet stacking. All homology groups have integer coefficients, and the double uses distinct underlying edges and the union-face condition, not merely a graph matching complex.

## Proof

**1. Exhaustive cellular model.** The facets above determine the complete face set by downward closure. The vertices of \(D^2(X)\) are the 27 edges of \(X\) (all pairs of \(V\) except \(\{6,7\}\)). Two double-vertices span an edge exactly when the corresponding two edges of \(X\) are disjoint and their four endpoints form a face of \(X\); three double-vertices span a triangle exactly when the six endpoints are distinct and form a face. As every facet of \(X\) has six vertices, no higher-dimensional double-simplex exists. Exact enumeration yields the face numbers \((27,165,180)\); the verification program recomputes them from the twelve facets.

**2. Edge-path presentation and exact reduction.** Choose the lexicographic breadth-first spanning tree in the double's one-skeleton, rooted at its first double-vertex. Collapsing this tree leaves 139 oriented one-cell generators and 180 triangular attaching relators. At each reduction step, select a relator containing some generator exactly once, solve it for that generator, substitute its expression in every other relator, and remove the selected generator and relator. Free and cyclic word reductions preserve the normal closure of the relators. The deterministic selection rule and signed-word operations are implemented without external dependencies in `VERIFY.py`. Exactly 134 such eliminations take place and leave five generators indexed \(48,88,91,95,98\), with 46 relators; 26 are empty words and the remaining 20 have zero exponent sum in every generator. Every elimination is a valid elementary generator–relator cancellation, so it also preserves the homotopy type of the associated two-dimensional CW complex.

**3. Identification of the group.** Name the final generators \(a=48\), \(b=88\), \(c=91\), \(d=95\), \(e=98\). The retained relators include direct commutators for all six pairs among \(b,c,d,e\). The relator \(eac e^{-1}c^{-1}a^{-1}\), together with \([e,c]=1\), forces \([e,a]=1\); the analogous \(dacd^{-1}c^{-1}a^{-1}\) forces \([d,a]=1\). The relator \(dc^{-1}ac d^{-1}a^{-1}\), using these commutations, forces \([a,c]=1\). Finally the relator \(eb^{-1}ac e^{-1}bc^{-1}a^{-1}\) forces \([a,b]=1\). These ten pairwise commutation relations imply the quotient is abelian. Conversely, all 46 remaining relators have zero exponent sum in each of the five generators. Consequently there are **no further relations in the abelianization**, and the presented group is exactly \(\mathbb Z^5\).

**4. Integral homology.** After the 134 cellular cancellations, the reduced CW complex has one zero-cell, five one-cells and 46 two-cells. Each of the remaining attaching words has zero abelian exponent sum, so the integral cellular boundary from dimension two to dimension one is identically zero. The dimension-one boundary is also zero. Hence the integral homology is exactly as claimed. There is no higher chain group and no room for torsion.

## Verification

Running `python3 VERIFY.py` with the Python standard library recomputes every simplex and performs the full signed free-group word reduction, including assertions on the final relator count and exponent sums. The complete retained nonempty relators are printed for independent reconstruction of the pairwise-commutativity deductions; no reliance on previously generated files, symbolic-algebra software, or floating-point arithmetic is needed.

## Relationship to prior work

Lesh, Schreiner and Wahl introduced the double and established general connectivity bounds, but their published theorem does not determine this stacked sphere's fundamental group. The double of the unstacked simplex boundary \(\partial\Delta^6\) is the usual matching complex of the seven-vertex complete graph, known to be simply connected; its second Betti number is 20. The present classification demonstrates that a single stacking can create five essential commuting loops. A separate known five-sphere example, the join of two tetrahedral boundaries, has a double with free fundamental group of rank 15, rather than the abelian group here. A prior classification of \(r\)-tuplings of stacked \((2r-1)\)-spheres for \(r\ge3\) applies to **triplings and higher**, not the doubling studied here.

## Limitations

The claim concerns a single canonical eight-vertex stacked five-sphere. It does not classify doubles of arbitrarily iterated stacked spheres or assert a full homotopy type beyond the exact fundamental group and integral homology. The argument is a finite, exact computation supported by the complete reproducible cancellation algorithm, not a general-stacking theorem. No independent mathematical audit has been performed.

## References

- Kathryn Lesh, Bridget Schreiner, Nathalie Wahl, *The double of a simplicial complex*, first public June 12, 2025, arXiv:2506.10436, https://arxiv.org/html/2506.10436v2.
- Related classification: *A sharp double-connectivity example on a five-dimensional simplicial sphere*, https://github.com/published-finding corpus/2026.
