# Two-edge deletion shielding for sharp affine projector norms on metric cliques

## Finding
Let \(q\ge1\) be an integer, and let \(G_q\) be the complete graph on \(q+4\) vertices with two **disjoint** edges deleted. Replace each remaining graph edge by a unit interval, give the resulting metric graph arclength measure, and let \(P_q\) denote the real \(L^2\)-orthogonal projection onto continuous functions that are affine on every edge. All four endpoints of the missing edges are equivalent under automorphisms.

Define \(h=q^2+4q+5\) and six positive rational functions
\[
\begin{aligned}
\alpha&=\frac{6q^3+31q^2+57q+35}{2(q+1)(q+2)h},
&\beta&=\frac{q^2+3q+5}{2(q+1)(q+2)h},\\
\gamma&=\frac{2q+5}{2(q+1)h},
&\delta&=\frac1h,\\
D&=\frac{2(3q^2+11q+14)}{(2q+5)h},
&E&=\frac{2(q+1)}{(2q+5)h}.
\end{aligned}
\]
For positive arguments set \(F(u,v)=(u^2+v^2)/(2(u+v))\). Then the exact operator norm is
\[
\boxed{
\|P_q\|_{L^\infty\to L^\infty}=L_2(q)
=2F(\alpha,\gamma)+2F(\beta,\gamma)
+qF(\alpha,\delta)+qF(\beta,\delta)
+q(\gamma+\delta)+\frac{q(q-1)}2\delta.
}
\]
**Exactly the four endpoints of the two deleted edges are norming evaluation points**; all other vertices and all edge interiors have strictly smaller evaluation norms.

Let \(L_0(q)\) be the same operator norm for the full complete graph on \(q+4\) vertices, and \(L_1(q)\) the norm after deleting only one of the two disjoint edges. These previously reducible single-orbit cases equal
\[
L_0(q)=\frac{12(q+2)^2+15(q+2)+5}{3(q+3)(2q+5)},\qquad
L_1(q)=\frac{12(q+2)^2+4(q+2)+1}{3(q+2)(2q+5)}.
\]
The two-deletion graph satisfies the strict, all-orders **shielding inequality**
\[
\boxed{L_0(q)<L_2(q)<L_1(q)\qquad(q=1,2,\ldots).}
\]
Furthermore,
\[
\boxed{\lim_{q\to\infty}q\bigl(L_2(q)-L_0(q)\bigr)=\frac16,\qquad
\lim_{q\to\infty}q^3\bigl(L_1(q)-L_2(q)\bigr)=\frac23.}
\]
Thus the first deleted edge produces a first-order large-graph norm change, while a second disjoint deletion *reduces* the amplification by a third-order amount. This is a strict mathematical comparison between three different projection spaces, not a monotonicity assertion about a fixed projection.

## Assumptions and scope
Here \(G_q=K_{q+4}\setminus\{ab,cd\}\), where \(a,b,c,d\) are distinct. Its \(q\) remaining vertices are called ordinary; no vertex masses are present. A point of each edge is represented by \(t\in[0,1]\). A real \(L^\infty\) input is taken modulo arclength-null sets. The outputs are continuous, so their essential and pointwise maxima agree. The graph is connected for every \(q\ge1\).

## Proof
Let \(\phi_v\) be the continuous nodal hat function at vertex \(v\). On each unit interval with endpoints \(u,v\), its restrictions are \(1-t,t\). The real nodal Gram matrix is
\[
M=\frac16(2\operatorname{diag}(\deg(v))+A_G).
\]
The positive-definite matrix \(M\) has inverse \(M^{-1}=6(2\operatorname{diag}(\deg(v))+A_G)^{-1}\). Its row at \(a\), ordered as \((a,b,c,d,\text{ordinary vertices})\), has entries
\[
(\alpha,\beta,-\gamma,-\gamma,\underbrace{-\delta,\ldots,-\delta}_{q}).
\]
The row at an ordinary vertex \(x\) has entries \(-\delta\) at all four distinguished vertices, \(D\) at \(x\), and \(-E\) at the remaining \(q-1\) ordinary vertices. One verifies both formulas by direct multiplication with \(2\operatorname{diag}(\deg(v))+A_G\); symmetry then gives every row.

For a vertex \(v\), its evaluation kernel is \(K_v=\sum_u(M^{-1})_{vu}\phi_u\), so
\[
\|P_q\|_{L^\infty\to L^\infty}=\sup_x\|K_x\|_{L^1(G_q)}.
\]
If \(u,v>0\), direct integration yields
\[
\int_0^1|(1-t)u-tv|\,dt=F(u,v),\quad
\int_0^1|(1-t)u+tv|\,dt=\frac{u+v}2.
\]
Summing over the six edge-orbit types gives precisely the displayed \(L_2(q)=\|K_a\|_1\). The ordinary-vertex evaluation norm is
\[
L_{\mathrm{ord}}(q)=4\delta+4F(D,\delta)
+2(q-1)(\delta+E)+(q-1)F(D,E)
+\frac{(q-1)(q-2)}2E.
\]
All these expressions are valid at \(q=1\), with empty edge classes contributing zero.

**First exact polynomial certificate.** After substituting the six rational entries and clearing positive denominators, the difference between deleted-edge endpoint and ordinary-vertex norms has denominator
\[
3(2q+3)(2q+5)(q^2+3q+3)h^2(2q^2+8q+11)(2q^3+11q^2+21q+13)
\]
and numerator, in descending powers from degree \(12\) to degree \(0\), with coefficients
\[
(8,168,1730,11306,51503,170927,422275,781907,1077903,1080307,747720,320610,64194).
\]
Every denominator factor is positive and every numerator coefficient is positive when \(q>0\). Therefore \(L_2(q)>L_{\mathrm{ord}}(q)\) for all \(q\ge1\).

For an interior point \(x=(1-t)u+tv\) of an edge, the evaluation kernel is \(K_x=(1-t)K_u+tK_v\), hence \(\|K_x\|_1\le(1-t)\|K_u\|_1+t\|K_v\|_1\). If either endpoint is ordinary, this is strictly smaller than \(L_2(q)\). If both endpoints are distinguished, they belong to different missing-edge pairs. On a sufficiently short initial segment of an edge from the first endpoint to any ordinary vertex, the two evaluation kernels have opposite signs because their coefficients there are respectively \(\alpha>0\) and \(-\gamma<0\). The triangle inequality is then strict on a set of positive arclength. Thus all edge interiors are strictly suboptimal.

**Second and third polynomial certificates.** Substituting the two displayed comparison formulas gives \(L_1(q)-L_2(q)\) with positive denominator
\[
3(q+2)(2q+3)(2q+5)(q^2+3q+3)h^2(2q^3+11q^2+21q+13)
\]
and degree-\(9\) numerator coefficients, descending,
\[
(16,248,1704,6794,17235,28625,30765,20259,7185,975).
\]
Similarly, \(L_2(q)-L_0(q)\) has positive denominator
\[
3(q+3)(2q+3)(2q+5)(q^2+3q+3)h^2(2q^3+11q^2+21q+13)
\]
and degree-\(11\) numerator coefficients, descending,
\[
(4,80,727,3956,14340,36508,67142,90356,88715,61554,27360,5850).
\]
Both are strictly positive for every \(q\ge1\). Comparing leading coefficients and degrees gives the two claimed limits. This completes the universal proof.

## Verification
The standalone `verify_two_deleted_edges_p1.py` requires `sympy>=1.12`; run it in the same directory. It reconstructs all six rational inverse-matrix entries, certifies each polynomial numerator **as a symbolic identity** with strictly positive coefficients, verifies independent exact matrix inversions and direct signed edge-kernel integrals on seven labelled graphs, and checks the two leading-order limits. These finite inverse checks supplement, rather than replace, the three all-parameter polynomial certificates.

## Relationship to prior work
Shadrin's theorem gives knot-independent \(L^\infty\) boundedness of interval spline orthoprojectors, while Passenbrunner calculated periodic linear-spline projection constants. Boman examined weighted \(L^p\) stability estimates of finite-element \(L^2\) projections. These frameworks do not by themselves provide the exact present graph-family formula or the two-edge shielding inequality.

Earlier exact calculations of full cliques, **one-missing-edge complete split graphs**, and *balanced* complete multipartite metric graphs are taken as prior work: their one-defect and full-clique constants appear above only as comparators. The new object \(K_{2,2,1,\ldots,1}\) with \(q\ge1\) is neither complete split nor balanced multipartite. A full-text comparison with Boman (2006) was not possible, which remains an originality limitation.

## Limitations
The result assumes two vertex-disjoint deleted edges, unit remaining-edge lengths, uniform arclength measure, no vertex atoms, and first-degree continuous real splines. It does not prove monotonicity for general edge deletions or arbitrary multipartite graphs. The claim of originality is subject to full literature review and independent mathematical audit.

## References
- A. Yu. Shadrin, *The \(L^\infty\)-norm of the \(L^2\)-spline projector is bounded independently of the knot sequence: A proof of de Boor's conjecture*, Acta Math. **187** (2001), 59–137, DOI:10.1007/BF02392832.
- M. Passenbrunner, *The Lebesgue Constant for the Periodic Franklin System*, arXiv:1103.1950, first posted 2011-03-10.
- M. Boman, *Estimates for the \(L^2\)-projection onto continuous finite element spaces in a weighted \(L^p\)-norm*, BIT **46** (2006), 249–260, DOI:10.1007/s10543-006-0062-3 (full-text comparison unavailable).
