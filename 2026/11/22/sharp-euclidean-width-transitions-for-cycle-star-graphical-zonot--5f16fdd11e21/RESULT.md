# Sharp Euclidean width transitions for cycle–star graphical zonotopes

## Finding

For integers \(m\ge3\) and \(t\ge1\), let \(G_{m,t}\) consist of a simple \(m\)-cycle with \(t\) additional pendant vertices, all adjacent to the same cycle vertex \(v_0\). Put \(N=m+t\), \(h=\min\{m-1,\lfloor N/2\rfloor\}\), and
\[
Z_{m,t}=\sum_{\{i,j\}\in E(G_{m,t})}[e_i,e_j]\subset\mathbb R^N.
\]
In its intrinsic Euclidean affine span, the exact minimum directional width satisfies
\[
\operatorname{width}(Z_{m,t})^2
=N\min\left\{\frac1{N-1},\frac4{h(N-h)}\right\}.
\]
Every minimizing **unoriented** normal is a positive or negative scalar multiple of exactly one of the following centered subset indicators: (a) an individual pendant leaf, if \(h(N-h)\le4(N-1)\); (b) a consecutive interval of vertices among the nonhub cycle vertices, of cardinality \(s\) with \(s(N-s)=h(N-h)\), if \(h(N-h)\ge4(N-1)\). At equality both types minimize; no other directions do.

The transition classification is exact:

- For \(3\le m\le5\), only leaf normals minimize, for every \(t\ge1\).
- At \(m=6\), leaf normals minimize when \(t<15\), both types tie at \(t=15\), and arc normals minimize for \(t>15\).
- At \(m=7\), the corresponding threshold is \(t=9\).
- For \(8\le m\le14\), the threshold is \(t=15-m\), so every such tie occurs at exactly \(N=15\) total vertices.
- For \(m\ge15\), only arc normals minimize for every \(t\ge1\).

## Assumptions and scope

All graphs are finite, simple, unweighted, and connected. The ambient metric is the standard Euclidean metric on vertex-coordinate vectors, restricted to the dimension-\(N-1\) affine hull of \(Z_{m,t}\); this is not the graph-shortest-path metric or a degree-weighted graph norm. The width is the minimum over unit vectors in \(\mathbf1^\perp\) of the difference of opposite support functions. The term *interval* means a nonempty consecutive subset of the path obtained by removing \(v_0\) from the cycle. All integers \(m\ge3,t\ge1\) are covered.

## Proof

For a real normal \(u\in\mathbf1^\perp\), each generating edge segment contributes exactly \(|u_i-u_j|\), so
\[
w_u(Z_{m,t})=\sum_{\{i,j\}\in E}|u_i-u_j|.
\]
For any nonconstant \(u\), order its distinct coordinate levels. Discrete layer-cake decomposition yields
\(u=\sum_j\Delta_j b_{S_j}\), where the \(S_j\) are nonempty proper nested upper level sets, \(\Delta_j>0\), and \(b_S=\mathbf1_S-|S|\mathbf1/N\). By discrete coarea, the numerator equals \(\sum_j\Delta_j|\delta S_j|\), whereas the Euclidean triangle inequality bounds \(\|u\|_2\le\sum_j\Delta_j\|b_{S_j}\|_2\). Consequently
\[
\operatorname{width}(Z_{m,t})
=\min_{\varnothing\ne S\subsetneq V}\frac{|\delta S|}{\sqrt{|S|(N-|S|)/N}}.
\]
If the minimum is attained at a general normal, equality must hold in the Euclidean triangle inequality. Distinct nested proper centered subset indicators are not positively collinear, hence there is a single level jump and the normal is a centered cut indicator. This also establishes completeness of the minimizing directions once the optimal cuts are classified.

A cut may be replaced by its complement, so assume its selected side \(S\) excludes \(v_0\). Write \(s\) for the number of selected nonhub cycle vertices and \(k\) for the number of selected pendant leaves. If \(s=0\), its boundary size is \(k\) and the squared quotient equals \(kN/(N-k)\), which strictly increases with \(k\), so just one leaf is optimal in this class. If \(s>0\), the selected old cycle vertices form \(r\ge1\) runs along the path with \(m-1\) vertices. The boundary has \(k+2r\) edges. For fixed \(s,k\), replacing them by a single interval decreases this boundary unless \(r=1\). For \(r=1\) and \(k\ge1\), removing the selected leaves strictly improves the squared quotient because
\[
(k+2)^2s-4(s+k)=k((k+4)s-4)>0,
\]
and \(N-s>N-s-k\). Thus every optimal cut is either one pendant leaf (boundary one) or a nonhub cycle interval without leaves (boundary two).

The squared leaf quotient is \(N/(N-1)\). An interval of size \(s\), \(1\le s\le m-1\), has squared quotient \(4N/[s(N-s)]\). The concave quadratic \(s(N-s)\) is maximized over this integer range at \(s=h\), with an additional maximizing value \(s=h+1\) precisely when \(N\) is odd and \(h+1\le m-1\). The main formula and exact minimizing normals follow.

To compare the two types, define \(Q=h(N-h)-4(N-1)\): positive means arc only, negative leaf only, zero a tie. At fixed \(m\), the quantity \(h(N-h)/(N-1)\) grows strictly as \(t\) increases. This follows directly for \(h=\lfloor N/2\rfloor\) from \(\lfloor N^2/4\rfloor/(N-1)\), and for \(h=m-1\) from \((m-1)(t+1)/(m+t-1)\); the pieces join monotonically. For \(m\le5\) one has \(Q<0\) always; for \(m=6,7\), in the eventual regime \(h=m-1\), the equality simplifies to \((m-5)t=3(m-1)\), giving \(t=15,9\). For \(8\le m\le14\), equality is at \(N=15\), where \(h=7\) and \(h(N-h)=56=4(N-1)\); strict monotonicity fixes the two sides. For \(m\ge15\), already at \(t=1\), \(N\ge16\) and \(Q>0\), hence it remains positive. This exhausts the phase diagram.

## Verification

The self-contained Python 3 script `bunched_cycle_width_checker.py`, included alongside this document, uses only the standard library and exact rational arithmetic. Run `python3 bunched_cycle_width_checker.py`. It independently enumerates all nontrivial cuts for \(63\) pairs with \(3\le m\le10\), \(1\le t\le8\), \(m+t\le17\), and checks **both** the minimum width and the complete set of minimizing cut normals. It also verifies the displayed threshold classification on \(9800\) further integer parameter pairs \(3\le m\le100\), \(1\le t\le100\). Output: `BUNCHED_CYCLE_WIDTH_EXACT_PASS enumerated_cases=63 phase_checks=9800`.

## Relationship to prior work

Padrol, Pilaud and Poullot [1] give the standard graphical zonotope as a sum of edge segments and analyze its normal fan and deformation cone; their results do not evaluate this family-specific Euclidean minimum width. The general cut-expansion variational characterization for a weighted graphical zonotope [2] already establishes that a cut minimizes the intrinsic width. Accordingly, the cut-reduction step is **not** claimed as new. The result here is instead the complete closed-form evaluation, exhaustive optimal-normal classification, and sharp two-parameter phase diagram for cycle–star graphs. Work on unicyclic graphical-zonotope Euclidean surface area [3] and on the width of cyclohedra [4] treats different metric invariants or different polytopes.

## Limitations

The theorem applies only to an unweighted simple cycle with all pendant leaves at one cycle vertex, not arbitrary unicyclic graphs or weighted edges. The finite checker is corroborating evidence, not an infinite proof. The literature comparison includes the directly relevant full open-access primary article and searchable summaries of related published results; an inaccessible full record or an unindexed equivalent treatment of the same cut optimization remains a historical priority risk. No independent mathematical audit has been performed.

## References

1. A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, first posted 24 November 2021; Discrete & Computational Geometry, DOI: 10.1007/s00454-023-00586-x. https://arxiv.org/abs/2111.12422
2. *Euclidean inradius of weighted graphical zonotopes is a cut expansion constant* (public research record). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-euclidean-inradius-of-weighted-graphical-zonotopes-is-a-cut-expa--cb1eceb082ab
3. *Sharp first and second Euclidean surface-area levels of unicyclic graphical zonotopes* (public research record). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-first-and-second-euclidean-surface-area-levels-of-unicycli--ac23a8023ac7
4. *Sharp Euclidean thickness and a cut-balance transition in the standard cyclohedron* (public research record). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-euclidean-thickness-and-a-cut-balance-transition-in-the-st--773d782a1bb3
