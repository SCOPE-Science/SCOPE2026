# Sharp local four-pedal rigidity at the centre of a regular tetrahedron

## Finding
For a regular tetrahedron, an interior projection point sufficiently close to its centroid restores the initial regular shape after four fixed-point facet-projection steps **only** at the centroid. More precisely, the fourth-pedal edge-length dispersion has a sharp first-order coefficient, independent of the direction of displacement.

Set
\[
K=\operatorname{conv}\{(1,-1,-1)/2,(-1,1,-1)/2,(-1,-1,1)/2,(1,1,1)/2\}.
\]
For \(P\) near \(0\), define \(K_0(P)=K\), and let \(K_{j+1}(P)\) be the convex hull of the perpendicular feet from \(P\) to the four *facet planes* of \(K_j(P)\), for \(0\le j<4\). These are nondegenerate tetrahedra in a neighbourhood of \(0\). Write \(e(P)\in\mathbb R^6\) for the six squared edge lengths of \(K_4(P)\), in a fixed natural facet-label order, and put
\[
m(P)=\frac16\sum_{i=1}^6 e_i(P),\qquad g(P)=\frac{e(P)}{m(P)}-\mathbf1.
\]
The complete sharp infinitesimal law is
\[
\boxed{\|g(P)\|_2=\frac{112\sqrt2}{27}\|P\|_2+O(\|P\|_2^2)\quad(P\to0).}
\]
In particular, \(g(P)=0\) in some neighbourhood of the centroid if and only if \(P=0\). Since all edges of the original tetrahedron agree, \(g(P)=0\) is equivalent to similarity of the fourth-pedal tetrahedron to the original.

## Assumptions and scope
A projection is taken onto the complete affine plane supporting each facet, with the same **fixed** point \(P\) at each step; it is not the orthic operation that drops vertex altitudes. There are exactly four iterations. The normalization specifies a tetrahedron of squared edge length \(2\). Distances for \(P\) use the original Euclidean coordinates. The Euclidean norm on the six normalized squared edge lengths is part of the theorem and fixes its coefficient. No global uniqueness for every interior \(P\) is asserted.

## Proof
**Smoothness and symmetry.** At \(P=0\), the regular tetrahedron is simultaneously inscribed and circumscribed about concentric spheres, so two facet-pedal steps are a positive homothety and the fourth is regular. In fact its circumradius is three times its inradius, giving \(K_4(0)=K/81\). Each foot is the rational smooth function \(P+(b-n\cdot P)n/\|n\|^2\) of the vertices and \(P\), where \(n\cdot x=b\) supports the facet. The four maps and \(g\) are therefore smooth near \(P=0\). Every orthogonal symmetry of \(K\) permutes the four vertex and facet labels, and hence permutes the six edge labels. Thus \(g\) is equivariant under the full tetrahedral symmetry group \(S_4\).

**One exact axial derivative.** For a translated regular tetrahedron with projection point at the origin, write
\[
V(a,b,c)=\operatorname{conv}\{(a,b,b),(b,a,b),(b,b,a),(c,c,c)\}.
\]
Let \(p=a-b\), \(d=a+2b-3c\), \(v=a+2b\), and \(x=d/p,\ y=v/p\). Direct perpendicular-foot calculation gives the projective update
\[
(x,y)\mapsto\left(-\frac{2xy+1}{y-x},\frac1x\right).
\]
Take \(a=c=t\), \(b=t-1\), and \(z=3t-2\). The initial parameters are \((x,y)=(-2,z)\). Four substitutions reduce the signed shape parameter to
\[
 x_4(z)=\frac{2(35z^3-36z^2+30z-2)}{(z+2)(17z^2-16z+8)}.
\]
An equilateral-base tetrahedron with these parameters has squared lateral-to-base edge ratio
\[
 k_4(z)=\frac{x_4(z)^2+2}{6}.
\]
At the centred regular shape \(t=1/2\), thus \(z=-1/2\), exact differentiation gives
\[
x_4(-1/2)=-2,\qquad \frac{dk_4}{dz}(-1/2)=-\frac{224}{81}.
\]
The tetrahedron \(V(t,t-1,t)\) is exactly \(K+(t-1/2)(1,1,1)\). Translation equivariance shows that its four-pedal edge lengths from \(0\) equal those of \(K\) from \(P=(1/2-t)(1,1,1)\). Therefore along \(P=s(1,1,1)\), the fourth-pedal squared lateral-to-base edge ratio satisfies
\[
 k_4(s)=1+\frac{224}{27}s+O(s^2).
\]
The six normalized edge-square deviations are three copies each of \((1-k_4)/(1+k_4)\) and \((k_4-1)/(1+k_4)\). Consequently for \(L=Dg(0)\),
\[
\|L(1,1,1)\|_2=\frac{112\sqrt6}{27}.
\]

**All directions and rigidity.** The natural orthogonal action of the tetrahedral symmetry group on \(\mathbb R^3\) is an irreducible real representation (the sum-zero standard representation of \(S_4\)). Since \(L\) intertwines this action with permutation of edge labels, \(L^*L\) commutes with this irreducible action. As a real symmetric operator it is scalar, by invariance of its eigenspaces. The preceding nonzero axial derivative determines
\[
 L^*L=\frac{2\cdot112^2}{27^2}\,I_3.
\]
Thus \(\|LP\|_2=(112\sqrt2/27)\|P\|_2\) for every \(P\). Smooth Taylor expansion gives \(g(P)=LP+O(\|P\|_2^2)\), with a uniform remainder on a small ball, proving the stated formula. Since the linear coefficient is positive, the norm of \(g(P)\) is strictly positive at all sufficiently small nonzero displacements. \(\square\)

## Verification
The accompanying `check.py` uses exact rational arithmetic to verify the three polynomial identities governing the four-step axial expression and its derivative; it independently computes 472 successive facet-plane perpendicular-foot constructions in \(\mathbb Q^3\) and compares them with the reduced map, including the centered special case. The mathematical extension to non-axial directions follows from the stated symmetry and irreducibility argument, not from sampling. Run `python3 check.py` with the Python 3 standard library.

## Relationship to prior work
Zwierzyński's 2026 paper supplies a correct fixed-point facet-pedal map for equilateral-base tetrahedra, a counterexample to a proposed universal four-step return, and the positive concentric-spheres two-step return theorem. The present result extracts an exact axial derivative and uses full tetrahedral symmetry to establish **sharp three-dimensional local rigidity**, not merely a one-axis formula. Earlier work on axial tetrahedral pedal dynamics describes invariant ovals and rotations of the normalized marked state; that restriction does not address arbitrary small three-dimensional displacement of the fixed projection point. Abu-Saris and Hajja study a different iteration, dropping **vertex altitudes** rather than holding a general projection point fixed. Kostanyan's universal four-step similarity claim is contradicted by Zwierzyński's explicit example and cannot supply this positive local theorem.

## Limitations
The conclusion is local; the size of a maximal uniqueness neighbourhood is not determined. The asymptotic expansion is for this particular normalization of the tetrahedron and its six-dimensional Euclidean edge-square-dispersion norm. The cited 2026 preprint and other primary literature may have subsequently developed; independent historical-priority review remains appropriate. This is an analytic proof with an additional exact arithmetic checker, not an independent audit.

## References
1. M. Zwierzyński, *When Pedal Shapes Come Back: a Complex Story*, arXiv:2611.01247v1 (first publicly submitted 31 October 2026), https://arxiv.org/html/2611.01247v1, especially Sections 3–4.
2. A. Kostanyan, *Pedal Tetrahedrons*, Mathematics in School 6 (119), 92–99 (2026), https://mathinschool.aspu.am/index.php/mathinschool/article/view/58.
3. R. Abu-Saris and M. Hajja, *The Chaotic Behavior of the Sequence of Pedal Simplices*, Results in Mathematics 55 (2009), 209–220, https://doi.org/10.1007/s00025-009-0411-z.
