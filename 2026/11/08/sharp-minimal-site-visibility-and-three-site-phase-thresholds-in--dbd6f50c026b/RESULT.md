# Sharp minimal-site visibility and three-site phase thresholds in quadratic Voronoi geometry

## Finding
A site-dependent quadratic Voronoi cell need not be convex or visible from its generating site. The following theorem determines precisely when this happens with two sites, and gives **both sharp transitions** throughout a natural three-parameter family of three collinear planar sites.

**Minimal-site visibility theorem.** Fix a dimension \(d\ge2\). For symmetric positive-definite \(d\times d\) matrices \(A,B\), and \(b\ne0\), define
\[
C(A,B;b)=\{x\in\mathbb R^d:x^{\mathsf T}Ax\le(x-b)^{\mathsf T}B(x-b)\}.
\]
This closed two-site cell is star-shaped about the site \(0\) **if and only if** \(A-B\succeq0\); in this case it is also convex. Consequently **no two-site quadratic Voronoi cell can be nonconvex while remaining star-shaped about its own site**.

Now in the plane take sites \(p_0=(0,0)\), \(p_1=(1,0)\), \(p_2=(-s,0)\), equipped respectively with quadratic metrics \(I\), \(\lambda^2 I\), \(\mu^2 I\), with \(\lambda>1\), \(0<\mu<1\), \(s>0\). Define
\[
s_{\mathrm{conv}}=\frac{\lambda(1-\mu)}{\mu(\lambda+1)},\qquad
s_{\mathrm{star}}=\frac{\lambda^2(1-\mu^2)}{\mu\sqrt{\lambda^2-1}\bigl(\mu\sqrt{\lambda^2-1}+\sqrt{\lambda^2-\mu^2}\bigr)}.
\]
Always \(0<s_{\mathrm{conv}}<s_{\mathrm{star}}\). The complete phase diagram for the cell \(V_s\) of the origin is:

- \(0<s\le s_{\mathrm{conv}}\): \(V_s\) is a disk, hence convex.
- \(s_{\mathrm{conv}}<s\le s_{\mathrm{star}}\): \(V_s\) is nonconvex but star-shaped at its generating site.
- \(s>s_{\mathrm{star}}\): \(V_s\) is not star-shaped at its generating site.

The endpoint inclusions are exact. In particular, **three sites are the smallest possible number** in this model for a nonconvex site-star-shaped cell.

## Assumptions and scope
The site distance is \(d_i(x)^2=(x-p_i)^{\mathsf T}M_i(x-p_i)\), with constant symmetric positive-definite \(M_i\). A closed cell consists of all points whose distance to its site is no larger than the distances to all other sites. *Star-shaped at the site* means every segment from that generating site to any point of its cell remains inside the cell; it is not a claim about arbitrary alternative star centers. The ambient domain is all of Euclidean space, not a clipped computational domain. The first theorem is valid in every \(d\ge2\); the exact three-site phase law is planar with precisely the stated collinear positions and metric scales. All comparisons include boundary equality.

## Proof
**1. Two-site rigidity.** Write \(Q=A-B\), \(\ell(u)=b^{\mathsf T}Bu\), \(d_0=b^{\mathsf T}Bb>0\). The defining condition is
\[
f(x)=x^{\mathsf T}Qx+2\ell(x)-d_0\le0.
\]
If \(Q\succeq0\), then \(f\) is convex, so its sublevel set is convex and contains \(0\).

Conversely, assume \(Q\not\succeq0\) and choose \(v\) with \(v^{\mathsf T}Qv<0\), changing its sign if necessary so that \(\ell(v)\ge0\). If \(b^{\mathsf T}Qb<0\), take \(u=b\): then \(q:=u^{\mathsf T}Qu<0\), \(\ell(u)=d_0>0\), and
\[
\ell(u)^2+q d_0=d_0b^{\mathsf T}Ab>0.
\]
Otherwise consider \(u_t=b+tv\), \(t\ge0\). We have \(\ell(u_t)\ge d_0>0\), whereas \(u_t^{\mathsf T}Qu_t\to-\infty\). At the largest nonnegative zero \(t_0\) of this continuous quadratic, its value changes from zero to negative immediately to the right. Choose \(t>t_0\) sufficiently close that \(q=u_t^{\mathsf T}Qu_t<0\) and \(\ell(u_t)^2+q d_0>0\), and put \(u=u_t\). In both cases \(q<0\), \(\ell(u)>0\), and \(\ell(u)^2>-qd_0\).

Along the ray \(x=tu\),
\[
f(tu)=qt^2+2\ell(u)t-d_0.
\]
At \(t_*=-\ell(u)/q>0\), this expression is \(\ell(u)^2/(-q)-d_0>0\), but it equals \(-d_0<0\) at \(t=0\) and tends to \(-\infty\) as \(t\to\infty\). Thus a sufficiently distant point lies in the cell while an intermediate point of its segment to \(0\) lies outside. The cell is not star-shaped. This establishes the equivalence, including indefinite and singular matrix differences.

**2. The three-site cell is an explicit disk with a circular exclusion.** Write \(x=(x_1,x_2)\). Completing squares in the two site-comparison inequalities gives
\[
V_s=D_s\setminus\operatorname{int}H,
\quad D_s=\{(x_1-\kappa s)^2+x_2^2\le\rho^2s^2\},
\quad H=\{(x_1-h)^2+x_2^2\le r^2\},
\]
where
\[
\kappa=\frac{\mu^2}{1-\mu^2},\quad\rho=\frac{\mu}{1-\mu^2},\quad
h=\frac{\lambda^2}{\lambda^2-1},\quad r=\frac{\lambda}{\lambda^2-1}.
\]
The disk \(D_s\) contains the origin strictly. The forbidden open disk \(\operatorname{int}H\) lies entirely to the right of the vertical line \(x_1=a:=h-r=\lambda/(\lambda+1)\). The rightmost point of \(D_s\) has coordinate \(s(\kappa+\rho)=s\mu/(1-\mu)\). Hence \(D_s\) avoids \(\operatorname{int}H\) if and only if \(s\le s_{\mathrm{conv}}=a(1-\mu)/\mu\), proving convexity in the first regime.

For every \(s>s_{\mathrm{conv}}\), the vertical cross-section of \(D_s\) at \(x_1=a\) has positive half-width, whereas that of \(H\) at \(x_1=a\) has zero half-width. Choose \(x_1>a\) sufficiently near \(a\) and \(y>0\) such that \((x_1,\pm y)\in\operatorname{int}D_s\setminus H\) while \((x_1,0)\in\operatorname{int}D_s\cap\operatorname{int}H\). Both endpoints lie in \(V_s\), but their midpoint does not. Thus all later phases are nonconvex.

**3. Exact visibility threshold.** For a unit ray from \(0\) with first coordinate \(c=\cos\theta\), the intersection of \(D_s\) with the ray is the interval \([0,sF(c)]\), where
\[
F(c)=\frac{\mu}{1-\mu^2}\left[\mu c+\sqrt{1-\mu^2+\mu^2c^2}\right].
\]
Set \(c_0=\sqrt{1-\lambda^{-2}}\). No ray with \(c<c_0\) penetrates the open disk \(H\). At \(c=c_0\) the ray is tangent to \(H\), so no radial interval is removed. For \(c>c_0\), the ray intersects \(\operatorname{int}H\) in the nonempty open interval \((t_-(c),t_+(c))\), where
\[
t_\pm(c)=hc\pm\sqrt{r^2-h^2(1-c^2)}.
\]
The cell is star-shaped at \(0\) precisely when no ray first exits and then re-enters, or equivalently when \(sF(c)<t_+(c)\) for **every** \(c>c_0\). Strictness is important: if \(sF(c)=t_+(c)\) for \(c>c_0\), the regained endpoint lies in the closed cell and visibility fails. At the tangent angle \(c=c_0\), such a condition is unnecessary.

For \(c>c_0\), observe
\[
\frac{t_+(c)}c=h+\sqrt{h^2-\frac{h^2-r^2}{c^2}}
\quad\text{strictly increases with }c,
\qquad
\frac{F(c)}c=\kappa+\sqrt{\kappa^2+\frac{\rho^2-\kappa^2}{c^2}}
\quad\text{strictly decreases with }c.
\]
Therefore \(t_+(c)/F(c)\) is strictly increasing on \((c_0,1]\). Its infimum is at the excluded endpoint \(c\downarrow c_0\), where \(t_+(c_0)=\sqrt{h^2-r^2}=\lambda/\sqrt{\lambda^2-1}\). Consequently
\[
s_{\mathrm{star}}=\frac{t_+(c_0)}{F(c_0)}
=\frac{\lambda^2(1-\mu^2)}{\mu\sqrt{\lambda^2-1}\bigl(\mu\sqrt{\lambda^2-1}+\sqrt{\lambda^2-\mu^2}\bigr)}.
\]
If \(s\le s_{\mathrm{star}}\), then \(sF(c)<t_+(c)\) for all \(c>c_0\), so every radial intersection is an initial interval and the cell is star-shaped at \(0\). If \(s>s_{\mathrm{star}}\), some \(c>c_0\) sufficiently near \(c_0\) satisfies \(sF(c)>t_+(c)\); that ray exits the cell across the forbidden-disk gap and then re-enters, proving nonvisibility.

Finally \(s_{\mathrm{conv}}<s_{\mathrm{star}}\): at \(s=s_{\mathrm{conv}}\) all of \(D_s\) has \(x_1\le a=h-r\), while the tangent point of the ray \(c=c_0\) to \(H\) has first coordinate \((h^2-r^2)/h>a\). Thus \(s_{\mathrm{conv}}F(c_0)<t_+(c_0)\), establishing strict separation of the transitions. All three regimes are nonempty.

## Verification
The supplementary standalone script `verify.py` uses Python standard-library exact fractions to check a rational three-site nonconvex star-shaped witness and a two-site nonvisibility witness. It additionally tests the derived disk parameters, separation of thresholds, strict radial threshold monotonicity, and all three visibility regimes on 80 reproducible random metric-scale pairs using finite angular grids. The script prints `QUADRATIC_VORONOI_PHASE_CHECKS_OK 12338`. These tests are diagnostics only; all-parametric and all-dimensional conclusions follow from the analytic proof above.

For a simple exact example, take \(\lambda=2\), \(\mu=1/\sqrt2\). Then
\[
s_{\mathrm{conv}}=\frac{2}{3(1+\sqrt2)},\qquad
s_{\mathrm{star}}=\frac4{3+\sqrt{21}}.
\]
At \(s=1/2\) the cell is nonconvex but star-shaped at the origin. The points \((3/4,1/3)\) and \((3/4,-1/3)\) lie in the cell, while their midpoint \((3/4,0)\) does not: the defining disk expressions are respectively \(-47/144\), \(+1/144\) for each endpoint, and the forbidden-disk expression at the midpoint is \(-5/48\). This example lies strictly inside the second regime.

## Relationship to prior work
Venkovic and Anzt (2026) analyze Minkowski tensors of **already star-convex** anisotropic Voronoi cells, define the star property, and provide contact-function boundary formulas. Their work motivates deciding the star-convexity hypothesis from explicit site data. The present result is a criterion and exact phase classification, not a new tensor formula. Labelle and Shewchuk (2003) prove visibility under a wedged-face condition, including a restricted two-site wedge lemma. That restricted sufficient condition does not state the unrestricted two-site equivalence or the sharp three-site phase law. Held and de Lorenzo (2020) develop constructive algorithms for multiplicatively weighted Voronoi cells and their circular bisectors, but do not give these closed-form star-convexity thresholds. The general fact that weighted cells can be nonconvex or disconnected is established background, not claimed here.

## Limitations
The three-site phase law assumes collinearity and exactly one competitor with quadratic scale above one and one below one. It does not classify arbitrary placements or anisotropic matrix triples. The two-site theorem concerns visibility from the generating site; it does not classify possible unrelated star centers. At a sharp transition, tangencies may require separate regularity checks before applying boundary integration formulas from other work. Scientific priority remains provisional pending independent checking, especially against older weighted-Dirichlet literature. No independent mathematical audit has been performed.

## References
1. Venkovic, N., and Anzt, H., *Minkowski Tensors of Planar Anisotropic Voronoi Diagrams*, arXiv:2610.08656v1 (2026-10-06), https://arxiv.org/html/2610.08656v1.
2. Labelle, F., and Shewchuk, J. R., *Anisotropic Voronoi Diagrams and Guaranteed-Quality Anisotropic Mesh Generation*, SoCG 2003, https://people.eecs.berkeley.edu/~jrs/papers/aniso.pdf.
3. Held, M., and de Lorenzo, S., *An Efficient, Practical Algorithm and Implementation for Computing Multiplicatively Weighted Voronoi Diagrams*, ESA 2020, DOI:10.4230/LIPIcs.ESA.2020.56.
4. Held, M., and Palfrader, P., *On Modeling Coverage Areas of Anisotropic Transmitters by Voronoi-like Structures Based on Star-Shaped Distance Measures*, Computer-Aided Design and Applications 19 (2022), 967–976.
