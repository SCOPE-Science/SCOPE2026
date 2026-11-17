# Integral anti-Rips homology and a sharp persistence transition on Boolean cubes

## Finding

Write \(Q_n=\{0,1\}^{n}\) for the binary Hamming cube with metric \(d_H\). For an integer threshold \(t\), let \(K_n(t)=\operatorname{AVR}(Q_n;t)\) be the **inclusive anti-Vietoris–Rips simplicial complex**: a finite subset is a simplex precisely when all its distinct pairs have Hamming distance at least \(t\). The following statements hold for every integer \(n\geq5\).

At the first two thresholds below the diameter, \(K_n(n-1)\hookrightarrow K_n(n-2)\), the complexes are connected and have torsion-free integral homology. The older complex has
\[
K_n(n-1)\simeq\bigvee^{2^{n-1}(n-1)+1}S^1.
\]
The reduced integral homology of the newer complex is exactly
\[
\begin{array}{c|c|c}
n&\widetilde H_1(K_n(n-2);\mathbb Z)&\widetilde H_2(K_n(n-2);\mathbb Z)\\\hline
5&\mathbb Z^{16}&\mathbb Z^{151}\\
6&\mathbb Z^{223}&\mathbb Z^{302}\\
n\ge7&\mathbb Z^{2^{n-1}(\binom n2+n-1)+1}&0
\end{array}
\]
and all other reduced integral homology groups vanish.

The integral first-homology map induced by the threshold inclusion has the following *complete Smith normal form*, where a statement about a free cokernel includes primitivity of its image:

- \(n=5\): \(\mathbb Z^{65}\to\mathbb Z^{16}\) has 15 unit invariant factors; its kernel is \(\mathbb Z^{50}\) and its cokernel is \(\mathbb Z\).
- \(n=6\): \(\mathbb Z^{161}\to\mathbb Z^{223}\) has 161 unit invariant factors; its kernel vanishes and its cokernel is \(\mathbb Z^{62}\).
- Every \(n\ge7\): the map is a primitive injection, with cokernel \(\mathbb Z^{2^{n-1}\binom n2}\).

Thus the inclusion kills exactly 50 integral circle classes at five coordinates, but kills none at six coordinates or in any higher dimension. This is a statement about **homology and its natural inclusion**, not a claim of an integral homotopy wedge decomposition for the two exceptional dimensions.

## Assumptions and scope

The vertex set is the **entire** binary cube, not a constant-weight layer or a code selected inside it. Distances count differing coordinates and the inequality is \(\ge t\), not \(\le t\). Chain groups are oriented simplicial chains over \(\mathbb Z\). Reduced groups are used except for the explicitly described maps on positive-degree homology. We assume \(n\ge5\); smaller cubes can have higher-dimensional simplices and are not classified here. These two adjacent anti-Rips thresholds form part of a *decreasing-threshold* filtration.

## Proof

**Graph connectivity and the older stage.** At threshold \(n-1\), every vertex \(x\) is connected to its antipode \(\bar x\) and to the \(n\) vertices \(\bar x\oplus e_i\). Consecutive steps \(x\to\bar x\to x\oplus e_i\) realize every coordinate flip, so the graph is connected. It has \(2^n\) vertices and \(2^{n-1}(n+1)\) edges. For \(n\ge5\), there is no triangle: in a triple of binary words the sum of the three pairwise Hamming distances is at most \(2n\), whereas three distances at least \(n-1\) would sum to at least \(3(n-1)>2n\). Therefore the anti-Rips complex at this threshold is a connected graph and its first Betti number is \(2^{n-1}(n-1)+1\).

**The infinite range.** The same coordinatewise argument shows that any three binary words have total pairwise distance at most \(2n\). For \(K_n(n-2)\), a triangle would force \(3(n-2)\le2n\), hence \(n\le6\). Consequently for every \(n\ge7\) the newer complex is also a connected graph. Each vertex has \(1+n+\binom n2\) neighbors, yielding \(2^{n-1}(1+n+\binom n2)\) edges and the claimed integral first Betti number. Since only \(2^{n-1}\binom n2\) edges were added and no higher simplices arise, the old graph is a subgraph of the new one, and a spanning-tree basis immediately proves that the induced \(H_1\)-map is a primitive injection with free cokernel of that rank.

**Exact finite exceptions.** The remaining cases are the *complete* finite spaces \(Q_5\) and \(Q_6\), not experimental samples. In the included `verify.py`, two independent enumerators construct every clique through four vertices, and a direct extension test verifies there are no five-cliques. The verified face counts in dimensions zero through three are \((32,256,480,120)\) and \((64,704,960,240)\), respectively. Every triangle lies in exactly one tetrahedron in both cases. Thus \(\partial_3\) is injective over \(\mathbb Z\), of ranks 120 and 240.

Orient all simplices by increasing binary-word integer index, and use the standard alternating boundary \(\partial[v_0,\ldots,v_k]=\sum_j(-1)^j[v_0,\ldots,\widehat v_j,\ldots,v_k]\). The checker builds the *full integer* edge-by-triangle boundary matrix \(\partial_2\) and its projection \(P\partial_2\) onto the newly added edges (those at distance exactly \(n-2\)). The complete integer elimination has the following certified unit-pivot counts, with an identically zero remaining matrix after these pivots:

| Cube dimension | \(\operatorname{rank}\partial_2\) | \(\operatorname{rank}(P\partial_2)\) | \(\operatorname{rank}\partial_3\) |
|---|---:|---:|---:|
| 5 | 209 | 159 | 120 |
| 6 | 418 | 418 | 240 |

Every elimination uses a pivot exactly \(+1\) or \(-1\), along with invertible **integral** elementary row and column operations; a zero residual proves that every nonzero Smith factor is one. This certifies both the ranks and the absence of torsion in the corresponding cokernels, rather than merely checking ranks over selected finite fields. The checker is standalone Python standard-library code and asserts exhaustion, consistent face enumeration, uniqueness of tetrahedral triangle carriers, and zero residuals.

The known rank \(\operatorname{rank}\partial_1=2^n-1\) now gives
\[
\beta_1=f_1-(2^n-1)-\operatorname{rank}\partial_2,
\qquad
\beta_2=f_2-\operatorname{rank}\partial_2-\operatorname{rank}\partial_3.
\]
There are no higher simplices, and \(\partial_3\) is injective, giving precisely the asserted torsion-free groups.

**Integral persistence map.** Let \(C_{\mathrm{old}}\) denote chains supported on edges of distance at least \(n-1\). As each 2-boundary is a cycle, the kernel of the map from old first homology has rank
\[
\operatorname{rank}(\operatorname{im}\partial_2\cap C_{\mathrm{old}})
=\operatorname{rank}\partial_2-\operatorname{rank}(P\partial_2).
\]
The relative complex \((K_n(n-2),K_n(n-1))\) has no relative vertices, and its first homology is the cokernel of \(P\partial_2\) in the group on the newly added edges. The unit-pivot computation therefore proves that the absolute first-homology map has **free** cokernel of rank \(f_{1,\mathrm{new}}-\operatorname{rank}(P\partial_2)\), by the long exact sequence of the pair (both complexes are connected). Substituting the verified ranks yields the integer Smith forms stated above. For \(n\ge7\), this conclusion was already obtained geometrically from graph inclusion.

## Verification

Run `python3 verify.py` in the directory containing the packaged `verify.py`. It requires only Python 3 with `int.bit_count` and the standard library; `verification_output.json` records the expected exact output. Two combinatorially independent face enumerators agree on every face. For \(n=5\) and \(n=6\), the full boundary matrices respectively have 209 and 418 integer unit pivots, while the relative projected matrices have 159 and 418. The maximum absolute integer coefficient occurring during elimination is 2. The reconstructed face counts and rank conclusions are asserted by the program, which exits unsuccessfully on an unmet assertion. The all-\(n\) part is proved by the coordinatewise triple-distance inequality and graph counting, not by finite extrapolation.

## Relationship to prior work

Adams, Elchesen, Mallick and Moy introduced their 2025 treatment of anti-Vietoris–Rips thickenings and recalled the inclusive anti-VR simplicial definition (arXiv:2503.08862, Definitions 4.1–4.2). That paper treats continuous spheres, Borsuk graphs, and general structural properties, not these integer Hamming-cube anti-persistence maps. Engström's earlier theory identifies anti-Rips complexes of graph metrics with independence complexes of graph powers and treats particular line/lattice settings, but the cited results do not provide these cube boundary matrices or the stated rank transition. Bendersky, Elia and Grbić (published online October 22, 2026) and Galetto, Montaño and Wellner (first submitted June 18, 2026) study **ordinary** hypercube Vietoris–Rips complexes at bounded-**above** Hamming distances. That is a different complex; no duality or reduction establishing this anti-Rips result was found in the material inspected. The latter preprint's complete full text was not accessible in this investigation, so the bibliographic comparison is qualified.

## Limitations

This is an integral **homology and inclusion-map** classification, not a fundamental-group, simple-homotopy, or full homotopy classification in dimensions five and six. It does not cover \(n\le4\), nonbinary alphabets, arbitrary Hamming-distance thresholds, or equivariant integral representations. The finite certificates are exhaustive only in the stated exceptional dimensions, while the higher-dimensional range has a separate general proof. Independent external mathematical audit has not been performed. Bibliographic search cannot exclude unindexed equivalent results; one 2026 ordinary-Rips preprint was accessible only through its abstract.

## References

1. H. Adams, A. Elchesen, S. Mallick, M. Moy, *Anti-Vietoris--Rips metric thickenings and Borsuk graphs*, arXiv:2503.08862, first submitted March 11, 2025. https://arxiv.org/abs/2503.08862
2. A. Engström, *Complexes of directed trees and independence complexes*, arXiv:math/0508148, first submitted August 8, 2005; see Section 4. https://arxiv.org/abs/math/0508148
3. M. Bendersky, S. Elia, J. Grbić, *Cohomological properties of the Vietoris–Rips complex of a hypercube graph*, first published online October 22, 2026. https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/cohomological-properties-of-the-vietorisrips-complex-of-a-hypercube-graph/2A4A7A24D30C2C7664FF10AD79007089
4. F. Galetto, J. Montaño, Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784, first submitted June 18, 2026. https://arxiv.org/abs/2606.20784
