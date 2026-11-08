# Complementary three-chainlink sections preserve Euclidean perimeter and separate facet-length totals

## Finding

Let \(a_1,a_2,a_3\) and \(\ell\) be positive real numbers satisfying \(2\ell\leq\min_i a_i\), and write \(N=a_1+a_2+a_3\). Define the three-coordinate chainlink polytope
\[
K=\{x\in\mathbb R^3:0\leq x_i\leq a_i,\quad x_i-x_{i+1}\leq a_i-\ell\ (i\bmod 3)\}.
\]
For \(0\leq t\leq N\), let \(K_t=K\cap\{x_1+x_2+x_3=t\}\). Use the inherited Euclidean metric on the affine section plane, and let \(P(t)\) denote the polygonal perimeter of \(K_t\), with perimeter zero at the two point sections. Then, for **every real** \(t\in[0,N]\),
\[
\boxed{P(t)=P(N-t).}
\]
More strongly, away from the finite set of section levels containing a nonsimple edge coincidence, the **total Euclidean lengths of the section edges on coordinate box facets**, and **those on the three chainlink difference facets**, are each separately unchanged by replacing \(t\) with \(N-t\). The two totals have explicit profiles below, extending continuously to all section levels.

Here is a complete closed-form evaluation. Put \((u)_+=\max(u,0)\), and define
\[
\begin{aligned}
 g_\ell(u)&=\min\{2\ell,\max(0,u+\ell)\},\\
 k_\ell(u)&=(\ell-|u|)_+,\\
 L_{b,c}(u)&=\bigl(\min\{b,u\}-\max\{0,u-c\}\bigr)_+.
\end{aligned}
\]
The box-section perimeter is
\[
P_B(t)=\sqrt2\sum_{i=1}^3\left[L_{a_{i+1},a_{i+2}}(t)+L_{a_{i+1},a_{i+2}}(t-a_i)\right],
\]
where subscripts are cyclic. Set
\[
\begin{aligned}
 S(t)&=\sum_{i=1}^3\bigl[g_\ell(t-a_i)-g_\ell(t-(N-a_i))\bigr],\\
 T(t)&=\sum_{i=1}^3\bigl[k_\ell(t-a_i)+k_\ell(t-(N-a_i))\bigr].
\end{aligned}
\]
Then the two facet-family length profiles are
\[
\boxed{P_{\mathrm{diff}}(t)=\frac{\sqrt6}{2}S(t),\qquad
P_{\mathrm{coord}}(t)=P_B(t)-\sqrt2 S(t)-\frac{\sqrt2}{2}T(t),}
\]
and \(P(t)=P_{\mathrm{coord}}(t)+P_{\mathrm{diff}}(t)\). Each of \(P_B,S,T\) is separately invariant under \(t\mapsto N-t\).

The sections need not be congruent: with \((a_1,a_2,a_3)=(6,4,5)\), \(\ell=2\), and \(t=5\), the complementary sections at levels \(5\) and \(10\) are both hexagons with different edge-length multisets, although both have perimeter \(6\sqrt2+3\sqrt6\). The restriction on \(\ell\) matters: at \((a_1,a_2,a_3)=(3,4,5)\) and \(\ell=2\), the section perimeters at levels \(5\) and \(7\) differ by \((\sqrt6-\sqrt2)/2>0\).

## Assumptions and scope

The cyclic inequalities are \(x_1-x_2\leq a_1-\ell\), \(x_2-x_3\leq a_2-\ell\), \(x_3-x_1\leq a_3-\ell\). All \(a_i\) and \(\ell\) are real; integrality and rationality are not assumed. The inherited metric, rather than a coordinate-plane metric, fixes the \(\sqrt2\) and \(\sqrt6\) factors. All interior levels have two-dimensional sections; the endpoints are singleton sections. Edge-type totals are literal on generic levels and their continuous extension is intended at exceptional levels. No assertion of congruence, individual edge-length matching, or a higher-dimensional analogue is made.

## Proof

**1. Disjoint corner shavings.** Let \(B=\prod_{i=1}^3[0,a_i]\). Then \(K\) is obtained from \(B\) by cutting off the three open caps \(W_i=\{x\in B:x_i-x_{i+1}>a_i-\ell\}\). The cap \(W_i\) forces \(x_i>a_i-\ell\geq\ell\) and \(x_{i+1}<\ell\). Any two of the three directed edges of the three-cycle have a common index, so their corresponding caps are disjoint when \(2\ell\leq\min_i a_i\). Their intersections with a generic section are therefore disjoint boundary modifications; perimeter corrections add without double counting. Degenerate levels follow by continuity.

**2. One-cap computation.** For cap \(W_i\), let \(j=i+1\), \(k=i+2\) cyclically, and write \(x_i=a_i-u\), \(x_j=v\), \(z=t-a_i\). Its section is the part of the triangle \(u\geq0,v\geq0,u+v\leq\ell\) inside the strip \(0\leq z+u-v\leq a_k\). The edge on \(u+v=\ell\) has Euclidean length \(\sqrt6\,H_{a_k,\ell}(z)/2\), where
\[
H_{b,\ell}(z)=g_\ell(z)-g_\ell(z-b).
\]
Indeed, setting \(v=\ell-u\) gives \(x_k=z+2u-\ell\); the allowed interval of \(u\) has length \(H_{b,\ell}(z)/2\), and the tangent vector in three-space is \((-1,-1,2)\), of length \(\sqrt6\).

The old boundary on the two cap sides \(u=0\) and \(v=0\) has **combined** length \(\sqrt2\,H_{a_k,\ell}(z)\); this follows by intersecting \([0,\ell]\) with \([z-a_k,z]\) and with \([-z,a_k-z]\), respectively. The old boundary on the remaining box faces \(x_k=0\) and \(x_k=a_k\), also lost when shaving, has combined length
\[
\frac{\sqrt2}{2}\Bigl[k_\ell(z)+k_\ell(z-a_k)\Bigr].
\]
For example, on \(x_k=0\) the relation \(v-u=-z\) cuts a segment of parameter length \((\ell-|z|)_+/2\) and Euclidean speed \(\sqrt2\); the upper face is analogous. Hence the **complete** perimeter correction from cap \(W_i\) is
\[
\left(\frac{\sqrt6}{2}-\sqrt2\right)H_{a_k,\ell}(t-a_i)
-\frac{\sqrt2}{2}\bigl[k_\ell(t-a_i)+k_\ell(t-a_i-a_k)\bigr].
\]
This includes all four kinds of removed box-boundary segments, not only the two cap sides.

**3. Sum and complementary symmetry.** Since \(a_i+a_{i+2}=N-a_{i+1}\), summing the new difference-facet lengths over the three caps gives \(\sqrt6 S(t)/2\). Summing removed coordinate-facet lengths gives \(\sqrt2 S(t)+\sqrt2 T(t)/2\). The box section has six possible coordinate-facet edges, with length formula \(P_B(t)\) stated above. This proves both claimed length profiles.

The reflection \(x_i\mapsto a_i-x_i\) sends the box section at \(t\) isometrically onto that at \(N-t\), so \(P_B(t)=P_B(N-t)\). The elementary identities \(g_\ell(-u)=2\ell-g_\ell(u)\) and \(k_\ell(-u)=k_\ell(u)\) show, term by term after pairing the positions \(a_i\) and \(N-a_i\), that \(S(N-t)=S(t)\) and \(T(N-t)=T(t)\). Therefore both facet-type length totals, and hence the complete perimeter, are symmetric at generic levels; continuity extends the equality to every real level.

**4. Noncongruence and a sharp boundary example.** Directly intersecting the nine defining half-planes in the \((x_1,x_2)\) coordinates gives, for \((a_1,a_2,a_3;\ell)=(6,4,5;2)\), the two six-edge squared-length multisets
\[
\begin{aligned}
 t=5:&\quad\{18,27/2,9/2,9/2,6,3/2\},\\
 t=10:&\quad\{25/2,25/2,27/2,2,6,3/2\}.
\end{aligned}
\]
The unequal multisets prohibit a Euclidean congruence, while their perimeter sums are both \(6\sqrt2+3\sqrt6\). If \((a_1,a_2,a_3;\ell)=(3,4,5;2)\), so \(2\ell>a_1\), those same intersections yield the respective perimeters \((9\sqrt6+3\sqrt2)/2\) and \(4\sqrt6+2\sqrt2\) at levels \(5\) and \(7\), proving the stated failure without the half-size hypothesis.

## Verification

The accompanying standalone standard-library script `verify.py` reconstructs section polygons independently from their nine half-plane inequalities using exact rational line intersections. It evaluates intrinsic edge lengths in three-space, checks both proposed facet-family profiles and their complement symmetry in 250 seeded admissible rational instances, confirms the noncongruent hexagon example, and checks the explicit counterexample beyond the hypothesis. Execute `python verify.py`. The full theorem is established by the facet-length proof, not by those finite tests.

## Relationship to prior work

Kantarcı Oğuz, Özel and Ravichandran introduced chainlink polytopes and established Ehrhart-quasipolynomial equality for complementary integer slices, hence equal slice areas at integer levels (arXiv:2211.08382v1, particularly Theorem 1 and §3). Their full accessible preprint also gives facet, vertex, and volume information (§6); it does not state the present perimeter/edge-family formulas. The present result concerns inherited **Euclidean length**, extends to arbitrary real parameters and levels, and separately matches the two metrically inequivalent facet-direction families. Equal Ehrhart quasi-polynomials alone control lattice-normalized boundary quantities, not these two Euclidean totals or their real-height profiles.

A related publicly indexed chainlink result determines Euclidean inradii of the **unsliced** polytopes through cyclic interval barriers; this controls neither section perimeters nor edge lengths. The journal version of the source article was available only as an abstract/preview, while the first public preprint was inspected in full. Priority against inaccessible expansions and differently phrased literature remains provisional.

## Limitations

The disjoint-cap argument is specific to three cyclic coordinates. In larger cycles nonadjacent shaved caps can overlap, and the asserted perimeter symmetry is **not** proved there. The half-size assumption is necessary for the stated universal theorem, as demonstrated explicitly, although individual out-of-range parameter triples can retain symmetry. No pointwise pairing of edges, congruence, or equality of higher-order metric shape descriptors is claimed. Independent validation has not been performed.

## References

1. E. Kantarcı Oğuz, C. Y. Özel, M. Ravichandran, *Chainlink Polytopes and Ehrhart-Equivalence*, arXiv:2211.08382v1, publicly posted 2022-11-15; https://arxiv.org/abs/2211.08382 .
2. E. Kantarcı Oğuz, C. Y. Özel, M. Ravichandran, *Chainlink Polytopes and Ehrhart Equivalence*, *Annals of Combinatorics* **28** (2024), 1141–1166; https://doi.org/10.1007/s00026-023-00683-x .
3. E. Kantarcı Oğuz, C. Y. Özel, M. Ravichandran, *Chainlink Polytopes*, *Séminaire Lotharingien de Combinatoire* **89B** (2023), article 67; https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2023/67.html .
