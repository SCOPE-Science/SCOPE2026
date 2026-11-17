# Sharp metric–real-\(L^1\) Poincaré separation on the Heawood graph

## Finding
Let \(H\) be the fourteen-vertex Heawood graph (the point–line incidence graph of the Fano projective plane), and assign unit length to each of its 21 edges. Write \(\mathcal P=\{\{u,v\}:u,v\in V(H),u\ne v\}\), so \(|\mathcal P|=91\). For a map \(f:V(H)\to(M,d)\), define
\[
A(f)=\frac1{91}\sum_{\{u,v\}\in\mathcal P}d(f(u),f(v)),\qquad
B(f)=\frac1{21}\sum_{\{u,v\}\in E(H)}d(f(u),f(v)).
\]
The optimal constant in \(A(f)\le\gamma B(f)\) is \(\gamma_{\mathrm{met}}(H)=27/13\) when \(M\) is allowed to be any metric space; for real \(L^1\) targets it is \(\gamma_{L^1}(H)=24/13\). Their ratio is \(9/8\).

The real \(L^1\) equality cuts are exactly the characteristic functions of vertex sets of induced six-cycles and their complements. There are 28 such hexagon vertex sets (and 28 complementary sets). More generally, for any real \(L^1(\Omega,\mu)\)-valued map attaining equality, almost every nontrivial scalar superlevel cut of any measurable coordinate representative is one of these 56 oriented cuts. Conversely, every nonconstant map whose nontrivial level cuts all belong to this family (up to null sets) attains equality.

If ordered pairs, including the zero diagonal, are averaged with weight \(14^{-2}\), as in Polavarapu's definition, all displayed constants are multiplied by \(13/14\): they become \(27/14\) and \(12/7\).

## Assumptions and scope
The Fano plane has seven points and seven lines, three points per line, and one line through each pair of distinct points. A point is adjacent to a line exactly when incident with it. An induced hexagon means the six vertices of a simple length-six cycle, with no additional edges among them. Metric targets have finite nonnegative distances. For real \(L^1\) maps we allow any measure space, and represent the finite family of vectors by jointly measurable real functions. Constant maps satisfy the inequality trivially; equality characterization refers to nonconstant maps. No other exponent than one is asserted.

## Proof
**Metric upper bound and equality.** Each vertex of \(H\) has three vertices at graph distance one, six at distance two and four at distance three. The 91 unordered vertex pairs therefore split into 21 at distance one, 42 at distance two and 28 at distance three, with total graph distance \(21+2\cdot42+3\cdot28=189\). Every incidence flag can be carried to every other by a Fano-plane collineation: the graph is edge-transitive. Choose a shortest path for every unordered vertex pair. By the triangle inequality, \(d(f(u),f(v))\) is bounded by the sum of image-edge lengths along its path. Averaging these 91 inequalities over every graph automorphism makes the coefficient of each edge equal, since the edge set is transitive; the sum of all coefficients is \(189\), hence each coefficient is \(189/21=9\). Therefore
\[
\sum_{\{u,v\}\in\mathcal P}d(f(u),f(v))\le9\sum_{e\in E(H)}d(f(e^-),f(e^+)),
\]
which gives \(A(f)/B(f)\le (21/91)9=27/13\). Taking the target \((V(H),d_H)\) and \(f\) the identity realizes equality, since every edge has distance one.

**Exact cut bound.** For a nonempty proper vertex set \(S\), let \(k=|S|\), \(e(S)\) the number of edges induced by \(S\), and \(b(S)=3k-2e(S)\) its edge boundary. Replacing \(S\) by its complement, assume \(1\le k\le7\). The cut ratio is
\[
\frac{A(\mathbf1_S)}{B(\mathbf1_S)}=\frac{21\,k(14-k)}{91\,b(S)}=\frac{3k(14-k)}{13b(S)}.
\]
We prove \(e(S)\le k-1\) for \(k\le5\) and \(e(S)\le k\) for \(k=6,7\), with equality \(e(S)=6\) at \(k=6\) only for an induced six-cycle. Write \(a\) for selected points and \(b\) for selected lines. By point–line duality we may take \(a\le b\), so \(a\le3\) when \(k\le7\). If \(a\le1\), then \(e(S)\le b\le k-1\). If \(a=2\), only one line contains both selected points, so \(e(S)\le b+1=k-1\). If \(a=3\) and the three points are collinear, only their common line meets more than one chosen point, giving \(e(S)\le b+2=k-1\). If the three points are noncollinear, precisely three distinct pair-lines can meet two selected points, and all other lines meet at most one; hence \(e(S)\le b+\min(b,3)\). For \(k=6\), equality \(e(S)=6\) forces \(a=b=3\), three noncollinear points and exactly their three pair-lines. These six vertices induce a hexagon. Conversely, every such selection is an induced hexagon.

Consequently \(b(S)\ge k+2\) for \(1\le k\le5\), \(b(S)\ge6\) for \(k=6\) and \(b(S)\ge7\) for \(k=7\). Direct integer comparison gives
\[
\frac{k(14-k)}{b(S)}\le8,
\]
with equality precisely for the six-cycle sets. Indeed, for \(k\le5\) the upper bound is \(k(14-k)/(k+2)<8\), at \(k=7\) it is at most \(49/7=7\), and at \(k=6\) it is at most \(48/6=8\). Thus the sharp cut ratio is \(24/13\). Exactly \(\binom73-7=28\) triples of Fano points are noncollinear, proving the number of induced hexagon vertex sets.

**Passing from cuts to \(L^1\).** If \(f(v)\) are real integrable functions, then pointwise for every two vertices the layer-cake identity gives
\[
|f(u)(\omega)-f(v)(\omega)|=\int_{\mathbb R}|\mathbf1_{\{f(u)(\omega)>t\}}-\mathbf1_{\{f(v)(\omega)>t\}}|\,dt.
\]
Tonelli's theorem and the cut inequality imply \(A(f)\le(24/13)B(f)\). The equality deficit is the integral of a nonnegative cut deficit. Since every nontrivial nonhexagon cut has a strictly positive deficit and there are finitely many cuts, equality forces almost every contributing threshold cut to be a six-cycle set or its complement. The same calculation proves the converse. A single hexagon indicator gives equality, so the bound is sharp.

## Verification
The attached standalone `verify_heawood.py` constructs the Fano plane as the nonzero vectors of \(\mathbf F_2^3\), generates its seven lines \(\{a,b,a+b\}\), checks all 14 breadth-first distance distributions, and enumerates every nonempty cut up to complement. All integer ratios are checked with exact rational arithmetic. It outputs `HEAWOOD_EXACT_OK` with metric ratio \(27/13\), maximum cut ratio \(24/13\), exactly 28 hexagon witnesses and cut-boundary profile \((3,4,5,6,7,6,7)\) for sizes one through seven. The structural argument above is a proof independent of relying on an opaque numerical search; the finite enumeration is exhaustive over the graph's \(2^{14}-2\) oriented nontrivial cuts.

## Relationship to prior work
Polavarapu's 2026 result bounds nonlinear Poincaré constants for regular graphs and Banach targets using cotype and spectral expansion; it does not supply these Heawood exact constants or its equality cuts. Altschuler–Dodos–Tikhomirov–Tyros give earlier general nonlinear spectral-gap bounds. The published exact real \(L^1\)-distortion census for small cubic-symmetric graph metrics reports Heawood embedding distortion \(4/3\), including a 28-cut symmetric orbit. Its problem is **different**: it minimizes a simultaneous bi-Lipschitz embedding distortion, rather than maximizing uniform-all-pairs spread relative to edge differences. In particular, its \(4/3\) bound does not by itself identify the claimed \(24/13\) uniform-demand gap or classify its equality cuts. The appearance of the same 28-cut orbit is acknowledged; its existence is not claimed as new.

## Limitations
Only exponent-one distances, the specific Heawood graph, and real \(L^1\) targets are classified. The numerical constants depend on the explicitly declared normalization. The result does not imply a sharp \(L^1\) embedding distortion nor characterize every unrestricted metric equality map. Older equivalent uniform-sparsest-cut or combinatorial-isoperimetric formulas might give an alternate prior route to the cut part; no publication-priority assertion is made beyond the documented comparisons. Independent mathematical validation has not been performed.

## References
1. A. R. Polavarapu, *Linear Cotype Bounds for Nonlinear Spectral Gaps of Scalar Expanders*, arXiv:2611.05649v1 (first public 2026-11-03), https://arxiv.org/abs/2611.05649.
2. D. J. Altschuler, P. Dodos, K. Tikhomirov and K. Tyros, *A Combinatorial Approach to Nonlinear Spectral Gaps*, arXiv:2410.04394, https://arxiv.org/abs/2410.04394.
3. *Exact L1-distortion census for six small cubic-symmetric graphs*, publicly accessible research record, https://github.com/published-finding corpus/2026/blob/main/2026/9/11/SCOPE004/RESULT.md.
