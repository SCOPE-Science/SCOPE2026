# Exact greedy two-step Steiner inertia contraction of an equilateral triangle

## Finding
Let \(T\) be a nondegenerate equilateral Euclidean triangle, and let
\[
I(K)=\int_K\|x-c_K\|^2\,dx
\]
denote the centroidal polar area moment of a planar convex body. Perform two ordinary Steiner symmetrizations about lines through the current centroid, selecting at **each** step a line that minimizes the resulting inertia. The first-step optimal lines are exactly the three unoriented lines parallel to the sides of \(T\).

After any such first step, rotate the coordinates and scale \(T\) to circumradius one. The first symmetral is the rhombus
\[
D=\operatorname{conv}\{(\pm\sqrt3/2,0),(0,\pm3/4)\}.
\]
There are exactly **two** second-step optimal unoriented axes, given by angles
\[
\boxed{\theta=\frac\pi2\pm\arctan\left(\frac{\sqrt3}{2}\alpha\right)\pmod\pi,}
\]
measured from the long diagonal of \(D\), where \(\alpha\in(0,1)\) is the unique real root in this interval of
\[
\boxed{36\alpha^5-23\alpha^4+112\alpha^3-48\alpha^2+80\alpha-44=0.}
\]
Numerically \(\alpha=0.5195378919586\ldots\), and the two axes are \(24.22455\ldots\) degrees to either side of the short diagonal. Exactly six ordered first/second axis choices attain the greedy two-step optimum (three first axes times two second axes). The sharp fraction of the original inertia lost is
\[
\boxed{\frac{I(T)-I(T_2)}{I(T)}=\frac18\left(1+
\frac{\alpha^2(33-29\alpha+18\alpha^2-18\alpha^3)}{(1+\alpha)^3(4+3\alpha^2)}\right)
=0.165522118304\ldots.}
\]
Here \(T_2\) denotes a symmetral after the two greedy steps. The second step alone removes \(0.0131599439500\ldots\) units of inertia for the circumradius-one reference triangle. This is a *sequential greedy optimization*, not an assertion of globally optimal simultaneous choices of two axes.

## Assumptions and scope
Steiner symmetrization \(S_HK\) about a line \(H\) replaces every segment of \(K\) on a line perpendicular to \(H\) with a centered segment of equal length. The axis \(H\) is required to pass through \(c_K\). This preserves area and the centroid \(c_K\), as the longitudinal first moment is unchanged and the transverse first moment becomes zero. The inertia is integrated over area with uniform density, not over the boundary. Scale and Euclidean rotation change the unnormalized inertia but not the maximizing axis configurations or the relative contraction. Every angle is an unoriented line modulo \(\pi\).

## Proof
**1. Exact triangular chord identity and the first greedy step.** Let \(A\) be the area of a triangle, \(e\) a unit vector along the candidate symmetrization axis, and \(w\) the length of the orthogonal projection of the triangle onto \(e\). At position \(s\) along \(e\), the perpendicular chord length \(\ell(s)\) is a two-sided linear tent with maximal value \(2A/w\). Consequently
\[
\int\ell(s)^3\,ds=\frac{2A^3}{w^2}.
\]
A centered segment of length \(\ell\) has transverse second moment \(\ell^3/12\). Thus, for a uniform point \(X\) of the original triangle,
\[
I(S_eT)=A\operatorname{Var}(e\cdot X)+\frac{A^3}{6w^2}.
\tag{1}
\]
For the circumradius-one equilateral triangle, \(A=3\sqrt3/4\), \(I(T)=3\sqrt3/16\), and \(\operatorname{Var}(e\cdot X)=1/8\) in every direction. Hence the loss \(I(T)-I(S_eT)\) increases strictly with the projection width \(w\). That width is at most the diameter \(\sqrt3\), attained exactly along the three edge directions. The corresponding first loss is \(3\sqrt3/128=I(T)/8\). The projected vertices along an optimal edge direction are \(-\sqrt3/2,0,+\sqrt3/2\). Their chord-length tent is symmetric about zero and has peak \(3/2\). Therefore its symmetral is precisely \(D\) as stated.

**2. Complete second-step angular profiles.** For a rhombus \(D_{a,b}=\operatorname{conv}\{(\pm a,0),(0,\pm b)\}\), orient an axis at angle \(\theta\in[0,\pi/2]\) to the first diagonal. Put \(t=\tan\theta\). In unnormalized orthogonal projection coordinates, obtained by multiplying the true coordinates by \(\sqrt{1+t^2}\), the four vertices have projected pairs
\[
(a,-at),\quad(bt,b),\quad(-a,at),\quad(-bt,-b).
\]
For \(0\le t\le a/b\), write \(s\) for the first projected coordinate. On \([0,bt]\), the chord endpoints in the second coordinate lie respectively on the edges joining left-to-top and bottom-to-right; on \([bt,a]\) they lie on top-to-right and bottom-to-right. The endpoints in each interval are linear interpolants of the displayed vertex coordinates. With endpoint functions \(L(s),U(s)\), the exact inertia loss is
\[
\Delta_{a,b}(\theta)=\frac{2}{(1+t^2)^2}\left[
\int_0^{bt}(U-L)\left(\frac{U+L}{2}\right)^2ds
+\int_{bt}^{a}(U-L)\left(\frac{U+L}{2}\right)^2ds\right].
\tag{2}
\]
The factor two comes from central symmetry and the denominator from converting both projected axes to unit length. The same calculation with \(a,b\) interchanged and \(t\) replaced by \(t^{-1}\) covers \(t\ge a/b\). All integrands are cubic polynomials on their respective intervals, so this is an exact elementary integration rather than an approximation.

Specialize to \(a=\sqrt3/2\), \(b=3/4\). In the branch \(0\le\tan\theta\le a/b\), set \(z=(b/a)\tan\theta\in[0,1]\). Formula (2) reduces to
\[
\Delta_{\mathrm{long}}(z)=\frac{3\sqrt3}{128}
\frac{z^2(19-15z+32z^2-32z^3)}{(1+z)^3(3+4z^2)}.
\tag{3}
\]
For the remaining branch let \(z=(a/b)\cot\theta\in[0,1]\). Its profile is
\[
\Delta_{\mathrm{short}}(z)=\frac{3\sqrt3}{128}
\frac{z^2(33-29z+18z^2-18z^3)}{(1+z)^3(4+3z^2)}.
\tag{4}
\]
Both branches agree at \(z=1\), the shared orientation, and both vanish at \(z=0\), where the rhombus is already symmetric about the selected diagonal. The accompanying symbolic checker independently reconstructs (3)--(4) by integrating the four edge equations.

**3. Unique global second-step maximum.** Differentiating (4) gives
\[
\Delta_{\mathrm{short}}'(z)=-\frac{9\sqrt3\,z\,Q(z)}{64(1+z)^4(4+3z^2)^2},
\quad Q(z)=36z^5-23z^4+112z^3-48z^2+80z-44.
\]
For \(0\le z\le1\),
\[
Q'(z)=180z^4-92z^3+336z^2-96z+80
\ge244z^2-96z+80>0.
\]
The final quadratic has negative discriminant and positive leading coefficient. Also \(Q(0)=-44\) and \(Q(1)=113\). Therefore (4) has exactly one interior maximizer \(\alpha\), strictly increasing before and decreasing after it.

It remains essential to compare (4) against **every** orientation in (3), not just its stationary points. Direct exact algebra gives
\[
\Delta_{\mathrm{short}}(1/2)-\Delta_{\mathrm{long}}(z)
=\frac{3\sqrt3}{128}\frac{P(z)}{513(1+z)^3(3+4z^2)},
\]
where
\[
P(z)=17080z^5-14424z^4+10185z^3-7589z^2+1494z+498.
\]
This polynomial is strictly positive on \([0,1]\). Indeed, in its exact degree-12 Bernstein expansion
\[
P(z)=\sum_{j=0}^{12}b_j\binom{12}{j}z^j(1-z)^{12-j},
\qquad b_j=\sum_{k=0}^{\min(j,5)}\frac{p_k\binom jk}{\binom{12}k},
\]
with \((p_0,\ldots,p_5)=(498,1494,-7589,10185,-14424,17080)\), every rational coefficient is positive and the smallest is exactly \(359/44\). The supplied checker recomputes and verifies this certificate. Thus \(\max\Delta_{\mathrm{long}}<\Delta_{\mathrm{short}}(1/2)<\Delta_{\mathrm{short}}(\alpha)\). Since reflection across either diagonal leaves \(D\) fixed, the sole maximizer in the relevant quadrant yields exactly the two angles claimed.

**4. Contraction and counting.** The second loss is (4) at \(z=\alpha\). Divide by the initial inertia \(3\sqrt3/16\) and add the first loss \(1/8\) to obtain the boxed sharp contraction. Exactly three first axes and two second axes for each give six optimizing ordered pairs. No other orientations can attain equality by the strict comparisons just proved.

## Verification
Run `python3 verify.py` (Python 3 standard library) for 13 positive exact rational Bernstein coefficients, 21 exact polynomial identities, the isolated quintic root, and 398 independent chord-endpoint integrations of the rhombus profiles. The independent numerical integrals use two-point Gaussian quadrature on each polygon-vertex projection interval, exact for the cubic chord-center integrands. It also checks the original triangular first loss and the final numerical contraction. Run `python3 verify_symbolic.py` (SymPy 1.12 or later) to derive the two rational profiles directly from the projected polygon edges and verify both the differentiated quintic identity and the comparison identity. These tests supplement the all-angle analytic proof; finite sampling alone does not establish the theorem.

## Relationship to prior work
Basit and Lángi (first public preprint June 9, 2022) give a general geometric Steiner-symmetrization framework for polygonal extremal problems, not an exact greedy inertia-angle classification. Bianchi, Gardner and Gronchi (2016) treat general symmetrization axioms and invariants. The published *Shape-independent angular response and a sharp contraction threshold for triangular \(\lambda\)-Steiner symmetrization* gives a general one-step triangle chord moment identity and an **angular average**. These ingredients explain the easy first step here but do not determine the subsequent optimal angle for the nonrectangular rhombus. An existing exact **rectangle** symmetrization profile and its square optimum apply to rectangles, not to this rhombus of unequal perpendicular diagonals; an anisotropic affine map does not preserve Euclidean inertia or ordinary Steiner symmetrization. The specific new contribution is the exact second-stage two-branch rhombus optimization, algebraic quintic optimizer, strict global comparison and resulting greedy two-step contraction. A search finding no equivalent is not a proof of priority.

## Limitations
Only ordinary centroid-passing planar Steiner symmetrization and the **greedy two-step** procedure starting with an equilateral triangle are treated. There is no claim that this ordered pair is globally optimal over all pairs when the first step is not itself greedy; no bound for later greedy steps or for arbitrary starting triangles is established. The result has a self-review, not independent mathematical validation; historical priority beyond inspected sources remains open.

## References
1. B. Basit and Z. Lángi, *Discrete isoperimetric problems in spaces of constant curvature*, arXiv:2206.04323v1, first posted June 9, 2022; https://arxiv.org/abs/2206.04323 ; full published text https://doi.org/10.1112/mtk.12175, especially §2.1.
2. G. Bianchi, R. J. Gardner and P. Gronchi, *Symmetrization in Geometry*, arXiv:1603.00643, March 2, 2016; https://arxiv.org/abs/1603.00643.
3. D. I. Florentin and A. Segal, *Stability and Rate of Convergence of the Steiner Symmetrization*, arXiv:1505.03550, May 12, 2015; https://arxiv.org/abs/1505.03550.
4. *Shape-independent angular response and a sharp contraction threshold for triangular \(\lambda\)-Steiner symmetrization*, published research result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-shape-independent-angular-response-and-a-sharp-contraction-thres--3b93c794f8bf/RESULT.md.
5. *Sharp one-step Steiner inertia contraction of a square and the full rectangle directional law*, an accessible mathematical manuscript (publication status not independently verified).
