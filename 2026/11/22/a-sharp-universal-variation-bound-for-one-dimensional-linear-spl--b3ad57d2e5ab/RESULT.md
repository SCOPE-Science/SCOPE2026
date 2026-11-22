# A sharp universal variation bound for one-dimensional linear-spline orthogonal projection

## Finding
Let \(a=x_0<x_1<\cdots<x_N=b\) be any finite partition with \(N\ge1\), and let \(P_\Delta\) be the real \(L^2(a,b)\)-orthogonal projector onto continuous functions affine on every interval \([x_i,x_{i+1}]\). For distributional total variation on the open interval, every real \(f\in BV(a,b)\) satisfies
\[
  \operatorname{TV}(P_\Delta f)\le3\operatorname{TV}(f).
\]
The coefficient is **optimal uniformly over all finite positive meshes**:
\[
 \boxed{\sup_{N\ge1}\ \sup_{x_0<\cdots<x_N}\ \sup_{\operatorname{TV}(f)>0}
 \frac{\operatorname{TV}(P_\Delta f)}{\operatorname{TV}(f)}=3.}
\]
The number three is a supremum over mesh families, not an assertion that any particular finite mesh attains it. An explicit central single-jump input on symmetric, increasingly graded meshes approaches three. For each fixed number \(m\ge1\) of extra cells on either side, the limiting amplification is
\[
  3-\frac{3}{2^{m+1}},
\]
so taking \(m\to\infty\) proves sharpness.

## Assumptions and scope
The knots are arbitrary strictly increasing real numbers, with strictly positive (otherwise unrestricted) interval lengths. No quasi-uniformity or mesh-ratio bound is assumed. \(P_\Delta\) uses Lebesgue measure and the complete continuous piecewise-affine spline space, including the constant function. Variation is the total mass of the distributional derivative inside \((a,b)\); endpoint point-values are irrelevant. The result is real-valued and one-dimensional. Finite-dimensional orthogonality makes the projection well-defined on \(L^2\), hence on \(BV(a,b)\).

Write \(h_i=x_{i+1}-x_i\) and \(\phi_i\) for the usual nonnegative nodal hat functions. Their Gram matrix is tridiagonal:
\[
  M_{ii}=(h_{i-1}+h_i)/3,\qquad M_{i,i+1}=h_i/6,
\]
with absent end intervals interpreted as zero. The matrix is positive definite. For a spline with nodal values \(p_0,\ldots,p_N\), its exact variation is \(\sum_{i=0}^{N-1}|p_{i+1}-p_i|\).

## Proof
### 1. Reduction to one jump
For \(t\in(a,b)\), put \(H_t(x)=\mathbf1_{(t,b)}(x)\). A real distributional \(BV\) function has the Stieltjes decomposition \(f=c+\int_{(a,b)}H_t\,d(Df)(t)\) almost everywhere. Since \(P_\Delta\) fixes constants, it is enough to prove \(\operatorname{TV}(P_\Delta H_t)\le3\) for every \(t\). Indeed, finite-dimensionality and integration against the finite signed variation measure permit termwise projection, and Minkowski's inequality for the finite vector of nodal differences gives
\[
 \operatorname{TV}(P_\Delta f)
 \le\int_{(a,b)}\operatorname{TV}(P_\Delta H_t)\,d|Df|(t)
 \le3|Df|((a,b)).
\]
This also includes jumps at knots by choosing either adjacent cell endpoint.

### 2. Exterior alternating tails
Fix \(t=x_k+u h_k\) in a cell, with \(0\le u\le1\), and let \(p_i=(P_\Delta H_t)(x_i)\). On all cells strictly to the left, the input is zero, and on all cells strictly to the right it is one. Thus the hat normal equations, multiplied by six, imply for \(i<k\)
\[
 h_{i-1}p_{i-1}+2(h_{i-1}+h_i)p_i+h_ip_{i+1}=0.
\]
At the left endpoint the equation is \(2p_0+p_1=0\). Hence the values to the left of \(p_k\) alternate in sign, and their absolute values decrease outward by at least a factor of two: if \(\rho_i=|p_i|/|p_{i+1}|\) for nonzero values, then \(\rho_0=1/2\) and
\[
 \rho_i=\frac{h_i}{2(h_{i-1}+h_i)-h_{i-1}\rho_{i-1}}\le\frac12.
\]
When \(p_k=0\), the entire left tail is zero by uniqueness of the homogeneous system. Consequently the variation strictly to the left of the central cell is at most \(3|p_k|\). Applying the same argument to \(p_i-1\) on the right gives a right-tail bound \(3|p_{k+1}-1|\). Empty tails have zero variation. These bounds use no restrictions on the interval lengths.

### 3. The two-cell interface inequality
Put \(s=p_k\), \(t_0=p_{k+1}-1\) and \(H=h_k\). The alternating tail relations give \(p_{k-1}=-\alpha s\), \(p_{k+2}=1-\beta t_0\), where the corresponding quantities are simply omitted at an endpoint, and \(0\le\alpha,\beta\le1/2\). With \(A=h_{k-1}(2-\alpha)\ge0\) and \(B=h_{k+1}(2-\beta)\ge0\), taking \(A=0\) or \(B=0\) at external endpoints, the two remaining normal equations become
\[
 (2+A/H)s+t_0=F(u),\qquad s+(2+B/H)t_0=G(u),
\]
where
\[
 F(u)=2-6u+3u^2,\qquad G(u)=1-3u^2.
\]
Their coefficient matrix is positive definite for all \(A,B\ge0\). The elementary bounds valid on \([0,1]\) are
\[
 F(u)\ge-1,\quad G(u)\le1,\quad F(u)-G(u)\le1,\quad G(u)-F(u)\le\frac12.
\]
These equations imply \(1+t_0-s\ge0\). For completeness, the same four sign cases show simultaneously that
\[
 \boxed{3|s|+(1+t_0-s)+3|t_0|\le3.}
\]
If \(s,t_0\ge0\), then \(s+2t_0=G-(B/H)t_0\le1\), and the boxed left side equals \(1+2s+4t_0\le3\). If \(s\ge0\ge t_0\), subtracting the equations gives \(s-t_0=F-G-(A/H)s+(B/H)t_0\le1\), and the expression equals \(1+2s-2t_0\le3\). If \(s\le0\le t_0\), subtracting in the other order gives \(t_0-s=G-F+(A/H)s-(B/H)t_0\le1/2\), and the expression equals \(1+4(t_0-s)\le3\). Finally, if \(s,t_0\le0\), then \(2s+t_0=F-(A/H)s\ge-1\), and the expression equals \(1-4s-2t_0\le3\). Each sign case also gives \(s-t_0\le1\), proving the asserted central difference sign.

The two tails and the central interval therefore contribute at most
\[
 3|s|+|p_{k+1}-p_k|+3|t_0|
 =3|s|+(1+t_0-s)+3|t_0|\le3.
\]
This proves the universal bound for every jump and hence for arbitrary real \(BV\) data.

### 4. Optimality under symmetric geometric grading
Fix \(m\ge1\) and \(0<\varepsilon<1\). Construct \(2m+1\) cells, with successive lengths
\[
 \varepsilon^m,\varepsilon^{m-1},\ldots,\varepsilon,1,
 \varepsilon,\ldots,\varepsilon^{m-1},\varepsilon^m.
\]
Place a unit jump at the midpoint of the central length-one cell. As \(\varepsilon\downarrow0\), both Schur corrections \(A/H,B/H\) tend to zero, so the central nodal values satisfy \(s\to-1/4\) and \(t_0\to1/4\). The exterior alternating recurrence gives ratios tending to \(1/2\) successively outward, beginning with the exact endpoint ratio \(1/2\). Thus the central cell contributes \(3/2\) to the limiting variation, and each tail contributes
\[
 \frac14\sum_{j=0}^{m-1}\bigl(2^{-j}+2^{-(j+1)}\bigr)
 =\frac34(1-2^{-m}).
\]
The limiting total is \(3-3/2^{m+1}\). First take \(\varepsilon\downarrow0\), then \(m\to\infty\); this proves that no universal constant smaller than three is valid.

## Verification
The standalone standard-library Python file `projection_tv_checker.py` assembles the exact rational Gram matrix and solves it independently. It checked \(8{,}205\) rational step-response cases over all length tuples in \(\{1,2,5\}\) through five cells, including jumps at cell endpoints. It also checked \(55{,}608\) exact rational piecewise-constant inputs over \(\{1,3\}\)-length meshes, with sign-changing data. Finally, it checked the geometric sharpness construction through seven symmetric grading layers at \(\varepsilon=1/1000\). All tests passed. The unrestricted inequalities and the asymptotic limit are proved above, not inferred from finite tests.

Run with `python projection_tv_checker.py` in the same directory. Python 3 standard library is the only dependency.

## Relationship to prior work
Ciesielski's classical linear-spline estimate, reported and explained by Oswald (2006), bounds the different \(L^\infty\to L^\infty\) projector norm by three. Foucart (2006) analyzes the max norm of orthogonal spline projectors under general smoothness and knot assumptions. Neither of these max-norm results implies a bound for the derivative-measure seminorm, because arbitrary mesh grading destroys translation commutation. The present result gives a mesh-uniform **\(BV\to BV\) variation seminorm** with an explicit asymptotically extremizing single jump and no requirement of smooth inputs. The prior graph-affine projection norm theorem likewise establishes \(L^\infty\) stability, not the variation of a projected step. A published isolated-cell spline norm result treats an infinite grid and \(L^\infty\) range amplification, not this theorem. The earlier broken quadratic projection variation calculation treats discontinuous degree-two spaces; its cellwise operator does not imply any result for continuous degree-one splines.

Relevant published records were compared by operator domain, quantity being maximized, admissible meshes, input class, and logical implication, not just by title. Searches and inspections did not identify the same universal variation theorem. This is a best-knowledge originality assessment, not proof of historical uniqueness. Older Franklin-system and spline-variation literature remains a residual priority risk.

## Limitations
The constant three is globally sharp over all finite positive partitions but need not be attained for a fixed mesh. The theorem concerns real functions and *unweighted* total variation on a finite interval. It does not give each individual mesh's exact norm, higher-degree or periodic spline analogues, weighted derivative variation, or multivariate BV estimates. The checker is finite numerical/algebraic supporting evidence, not a substitute for the proof. No independent mathematical audit has been performed.

## References
1. P. Oswald, *A counterexample concerning the \(L^2\)-projector onto linear spline spaces*, arXiv:math/0611573v1, public 2006-11-19: https://arxiv.org/abs/math/0611573 .
2. S. Foucart, *On the value of the max-norm of the orthogonal projector onto splines with multiple knots*, Journal of Approximation Theory **140** (2006), 154–177, author preprint: https://foucart.github.io/publi/SplineProj2.pdf .
3. Z. Ciesielski and A. Kamont, *The Lebesgue constants for the Franklin orthogonal system*, Studia Mathematica **164** (2004), 55–73, DOI:10.4064/sm164-1-4 (historical adjacent literature, full text not inspected here).
