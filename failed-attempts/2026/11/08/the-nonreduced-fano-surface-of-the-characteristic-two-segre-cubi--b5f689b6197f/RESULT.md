# The nonreduced Fano surface of the characteristic-two Segre cubic: 28 components and a length-six ruling stratum

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). Let \(X\subset\mathbb P^5_k\) be the diagonal Segre cubic defined by
\[
\sum_{i=0}^5X_i=\sum_{i=0}^5X_i^3=0.
\]
The **full scheme** \(F_1(X)\subset\operatorname{Gr}(2,5)\) of lines on \(X\) is pure of dimension two. Its reduced support has exactly \(28\) irreducible components: one smooth cubic surface \(R\cong S\) representing the lines through the unique cone vertex, and \(27\) Plücker-linear projective planes \(P_\ell\cong\mathbb P^2\), one for each line \(\ell\) on \(S\). Each \(P_\ell\) is generically reduced. The ruling component has **generic scheme-theoretic multiplicity six**; after geometric extension of its function field, a completed two-dimensional normal slice has local algebra
\[
\overline{k(S)}[[u,v]]/(u^2,v^3),
\]
of length six and Hilbert function \((1,2,2,1)\). As a two-cycle in the Grassmannian,
\[
[F_1(X)]=6[R]+\sum_{\ell\subset S}[P_\ell],\qquad\deg_{\mathrm{Pl}}F_1(X)=6\cdot3+27=45.
\]
Here multiplicity and the cycle refer to the full nonreduced Hilbert scheme; they do not describe the reduced subscheme alone.

## Assumptions and scope
The field is algebraically closed of characteristic two, and the cubic is the specified homogeneous diagonal form. The Fano scheme is the zero scheme of the universal cubic-restriction section of \(\operatorname{Sym}^3\mathcal U^\vee\) on \(\operatorname{Gr}(2,5)\), not merely the set of its geometric points. Degrees are taken in the Plücker embedding. The local normal-slice assertion is at the geometric generic point of \(R\), disjoint from the other 27 supports. The complete scheme structure at intersection loci of components is not asserted.

## Proof
**1. Reduction to a smooth cubic cone.** Write \(X_i=y_i+t\) for \(0\le i\le4\) and \(X_5=t\). Because the characteristic is two, \(\sum X_i=\sum y_i\); on \(\sum y_i=0\), the mixed terms in \(\sum X_i^3\) vanish and the equation becomes \(\sum_{i=0}^4y_i^3=0\). Eliminating \(y_4=y_0+y_1+y_2+y_3\) gives the cubic surface
\[
S=V(F)\subset\mathbb P^3,\qquad F(y)=\sum_{j=0}^3y_j^3+(y_0+y_1+y_2+y_3)^3.
\]
Its partial derivatives are \((y_j+\sum_i y_i)^2\). If all four vanish, every \(y_j\) equals the sum, and summing gives that sum equals zero, hence every \(y_j=0\). Thus \(S\) is smooth. The threefold \(X\) is the projective cone over \(S\) with vertex \(v\). A smooth cubic surface over an algebraically closed field has exactly 27 lines; in this example they are also exhibited over \(\mathbb F_4\) by the attached exact enumeration.

**2. Exhaustion of irreducible supports.** Each line in \(X\) through \(v\) is the ruling over a unique point of \(S\), giving \(R\cong S\). A line \(L\subset X\) not through \(v\) projects isomorphically from \(v\) onto a projective line \(\ell\subset S\). It lies in the plane \(\Pi_\ell=\langle v,\ell\rangle\subset X\). Conversely every line in any \(\Pi_\ell\) lies in \(X\). The Grassmannian of lines in \(\Pi_\ell\) is a Plücker-linear \(\mathbb P^2\). Since there are 27 distinct lines on \(S\), these give 27 distinct surface components, alongside \(R\). All supports have dimension two.

**3. No additional embedded components.** The Grassmannian \(\operatorname{Gr}(2,5)\) is smooth of dimension six. The cubic-restriction section belongs to a rank-four bundle. Its zero scheme has underlying support of pure dimension two, and thus codimension four everywhere. Four local coefficient equations consequently form a regular sequence in every local regular ring of the Grassmannian. Hence \(F_1(X)\) is a local complete intersection and Cohen–Macaulay, with no embedded associated components.

**4. Multiplicity of the ruling surface.** Fix a point \(P\in S\) not on any of the 27 lines. Work on the Grassmannian chart where a ruling line is spanned by a vertex-direction vector and \(P\); write deformations as the two vectors \((1,a)\) and \((0,b)\), with \(a\in k^3\) and \(b\) in an affine chart of \(\mathbb P^3\) near \(P\). Expand
\[
F(sa+tb)=s^3F(a)+s^2t\,Q_b(a)+st^2\,L_b(a)+t^3F(b).
\]
The linear equation \(L_b(a)=0\) is the tangent-plane equation to the smooth surface \(S\) at \(b\); together with \(F(b)=0\), it eliminates one normal variable \(a\) and one base coordinate \(b\). The remaining transverse completed local algebra is a complete intersection of a homogeneous quadratic \(q\) and a homogeneous cubic \(c\) in two variables. A common nonzero projective zero would give a line through \(P\) on \(S\). By the choice of \(P\), there is none. Hence \((q,c)\) has finite colength \(2\cdot3=6\), with Hilbert series \((1-z^2)(1-z^3)/(1-z)^2=1+2z+2z^2+z^3\). The nonempty open set of suitable points is independently witnessed by the attached explicit exact \(\mathbb F_{256}\) point, where the quadratic has a unique projective root and the cubic is nonzero at that root.

In characteristic two, \(Q_b(a)\) is a sum of squares, so geometrically \(q\) is the square of a linear form. In completed transverse coordinates over the algebraic closure of the generic residue field, write \(q=u^2\); since \(c\) is nonzero on the zero direction of \(q\), its coefficient of \(v^3\) is nonzero. Modulo \(u^2\), a linear change \(v\mapsto v+\lambda u\) removes its \(uv^2\) coefficient, making the ideal \((u^2,v^3)\). This proves the stated geometric generic normal-slice algebra and multiplicity six.

**5. Generic reducedness of planar components.** Let \(L\) be a general line in \(\Pi_\ell\) avoiding the vertex, so its projection is the line \(\ell\subset S\). Normal movements out of the plane induce two sections of \(\mathcal O_L(1)\). Their linearized cubic restriction is the standard normal morphism \(H^0(\ell,N_{\ell/\mathbb P^3})\to H^0(\ell,\mathcal O_\ell(3))\). Its kernel and cokernel vanish because \(N_{\ell/S}\cong\mathcal O_\ell(-1)\) and \(H^0,H^1(\mathcal O_\ell(-1))=0\). Consequently the only infinitesimal line movements are the two-dimensional motions inside \(\Pi_\ell\). The Fano scheme is therefore smooth of dimension two at a general such line, giving multiplicity one on \(P_\ell\).

**6. Plücker cycle.** The reduced ruling component embeds by \(P\mapsto v\wedge P\); its Plücker hyperplane bundle is \(\mathcal O_S(1)\), of degree three. Each \(P_\ell\) has Plücker degree one. The multiplicities established above give the cycle and degree \(6\cdot3+27=45\).

## Verification
The attached script `verify_fano_lines.py` enumerates all \(\mathbb F_2\)- and \(\mathbb F_4\)-rational projective lines on the smooth cubic \(S\) using reduced row-echelon matrices and the four exact coefficients of a restricted cubic. It finds respectively 15 and 27 lines. An independent exact-arithmetic calculation over \(\mathbb F_{256}\) verifies that \(P=(1,2,4,179)\) is a point of \(S\) with no line contained in \(S\) through it: in the chosen two-dimensional tangent basis, the quadratic coefficients are 157 and 67, its unique projective zero has slope 151, and the cubic at that direction is 48, nonzero. The program checks the length-six Hilbert series and reports `ALL_CHECKS_PASSED`. This finite test corroborates the proof but does not replace its geometric arguments. Run with `python3 verify_fano_lines.py` using the standard library alone.

## Relationship to prior work
The characteristic-zero Segre cubic has a very different Fano surface: six degree-five del Pezzo components and fifteen projective-plane components, as described in Dolgachev (2015, §4). Its total Plücker degree is likewise 45. The characteristic-two special fiber is already known to be a cone over a smooth Clebsch cubic, and the 27 planes on it are known geometric context; neither the cone observation nor the planar count is asserted as new. The additional coefficient-level finding here is the scheme-theoretic ruling multiplicity six, the geometric generic normal-slice algebra, and the resulting full 28-component cycle. The characteristic-two cubic-surface work of Kadyrsizova et al. examines smooth cubic-surface line configurations and Frobenius splitting, not the Fano scheme of lines on this cone. No inspected source supplied this cycle or its transverse thickening.

## Limitations
This calculation does not determine the full scheme structure at the 27 intersections between the ruling component and planar components, nor all pairwise planar intersection schemes. Historical priority is provisional: a specialist treatment of cubic-cone Hilbert schemes could contain an equivalent general result even if it was not located by targeted searches.

## References
- I. Dolgachev, *Corrado Segre and nodal cubic threefolds*, arXiv:1501.06432v1, 26 January 2015, especially §2 and §4. https://arxiv.org/pdf/1501.06432
- Z. Kadyrsizova et al., *Cubic surfaces of characteristic two*, arXiv:2007.12018, especially §§4–5 (later corroborating literature). https://arxiv.org/pdf/2007.12018
- Classical 27-line theorem for smooth cubic surfaces (Cayley–Salmon); this is used as established background, not an originality claim.
