# Cubic angular-gap stability and a logarithmic correction for polygonal boundary-chord means

## Finding

Let \(P\) be a convex polygon inscribed in the unit circle with successive vertex-angle gaps \(\Delta_1,\ldots,\Delta_m\), \(m\ge3\), and put \(\delta=\max_j\Delta_j\). Let \(X,Y\) be independent uniform-arclength points on \(\partial P\), let \(L(P)\) be its perimeter, and write
\[
\mathcal G(P)=\frac{2}{\pi^2}-\frac{\mathbb E\|X-Y\|}{L(P)}.
\]
As \(\delta\downarrow0\), without any restriction on the relative sizes of the gaps or on \(m\),
\[
\boxed{\mathcal G(P)=\frac{1}{24\pi^3}\sum_{j=1}^m\Delta_j^3+O\!\left(\delta^4\log\frac1\delta\right).} \tag{1}
\]
The implicit constant is absolute for \(0<\delta\le1/4\). Thus the first asymptotic defect from the sharp circle upper bound is precisely the cubic angular-mesh energy. Jensen's inequality identifies the equal-gap configuration as the unique minimizer of the **leading energy** at fixed \(m\), but (1) does not claim the regular polygon exactly minimizes the finite-\(m\) defect.

For \(P_n\), the regular \(n\)-gon of circumradius one, there is a finer asymptotic, with an explicit nonzero logarithmic coefficient:
\[
\boxed{\mathcal G(P_n)=\frac{1}{3n^2}-\frac{\pi^2}{90}\frac{\log n}{n^4}+O(n^{-4})\qquad(n\to\infty).} \tag{2}
\]
In particular \(\lim_{n\to\infty}n^2\mathcal G(P_n)=1/3\) and
\[
\lim_{n\to\infty}\frac{n^4}{\log n}\left(\mathcal G(P_n)-\frac1{3n^2}\right)=-\frac{\pi^2}{90}.
\]

## Assumptions and scope

All distances are Euclidean. The polygon is the convex hull of distinct points on one unit circle listed in circular order, with each gap positive, their sum \(2\pi\), and maximum gap at most \(1/4\) for the uniform quantitative estimate. Thus the origin is interior and each radial ray intersects exactly one polygonal side. Boundary sampling uses Euclidean arclength divided by the **actual perimeter**, not uniform angular sampling or uniform vertex sampling. Asymptotic constants in (1) are uniform over all such gap lists; (2) concerns the regular family only. A fixed-radius rescaling leaves \(\mathcal G\) unchanged.

## Proof

**1. Angular parametrization and exact densities.** Put \(\alpha_j=\Delta_j/2\), so \(\sum_j\alpha_j=\pi\), and let \(\eta_j\) be the angular midpoint of side \(j\). For a ray direction \(\phi=\eta_j+t\), \(|t|\le\alpha_j\), its intersection with the side is
\[
R(\phi)e^{i\phi},\qquad R(\phi)=\cos\alpha_j\sec t,
\qquad \frac{ds}{d\phi}=\cos\alpha_j\sec^2t.
\]
Consequently,
\[
L=2\sum_j\sin\alpha_j,\quad
u(d\phi)=w(\phi)\frac{d\phi}{2\pi},\quad
w(\phi)=\frac{2\pi}{L}\cos\alpha_j\sec^2t.
\]
Here \(\nu\) is the normalized arclength law. Set \(u=R-1\), \(v=w-1\), and write \(\langle f\rangle=(2\pi)^{-1}\int_0^{2\pi}f(\phi)d\phi\). The definitions imply
\[
\langle v\rangle=0,\qquad \|u\|_\infty+\|v\|_\infty\le C\delta^2,
\qquad |u(\phi)-u(\psi)|\le C\min\{\delta^2,\delta |\beta|\}, \tag{3}
\]
where \(\beta\in[-\pi,\pi]\) is the shortest signed angular difference. The Lipschitz estimate follows by differentiating \(R\) on each side, \(|R'|=|R\tan t|\le C\delta\), and using continuity at the vertices. Since \(\sum\alpha_j=\pi\), Taylor expansion gives \(L=2\pi+O(\delta^2)\), justifying the bound for \(v\).

**2. A uniform chord expansion.** Put \(s_\beta=|\sin(\beta/2)|\) and abbreviate \(u=u(\phi)\), \(u'=u(\psi)\). The exact squared distance is
\[
D^2=4s_\beta^2(1+u)(1+u')+(u-u')^2. \tag{4}
\]
For small fixed \(\delta\), expansion of the square root, with (3), yields the integrated estimate
\[
D=2s_\beta+s_\beta(u+u')+E,\qquad
|E|\le C\left[s_\beta\delta^4+\frac{(u-u')^2}{s_\beta}\right] \tag{5}
\]
for \(\beta\ne0\), with the diagonal understood by continuity. The singular term is integrable: for \(|\beta|\le\delta\), \((u-u')^2/s_\beta\le C\delta^2|\beta|\); for \(\delta<|\beta|\le1\), it is bounded by \(C\delta^4/|\beta|\), and for larger \(\beta\) by \(C\delta^4\). Thus its normalized double integral is at most \(C\delta^4\log(1/\delta)\).

Let \(M=\mathbb E\|X-Y\|\). The circular kernel \(2s_\beta\) has mean \(4/\pi\). Because \(\langle v\rangle=0\), the linear contributions of \(v\) to the unperturbed chord kernel vanish **exactly**; the \(vv'\) term is \(O(\delta^4)\). Similarly, the terms linear in \(u\) contribute \((4/\pi)\langle u\rangle\), and their terms involving \(v\) are \(O(\delta^4)\). Equation (5) therefore gives
\[
M=\frac4\pi\bigl(1+\langle u\rangle\bigr)
+O\!\left(\delta^4\log\frac1\delta\right). \tag{6}
\]

**3. Evaluating the first defect.** On side \(j\),
\[
\int_{-\alpha_j}^{\alpha_j}u(\eta_j+t)\,dt
=2\cos\alpha_j\log(\sec\alpha_j+\tan\alpha_j)-2\alpha_j
=-\frac23\alpha_j^3+O(\alpha_j^5).
\]
Since \(\sum\alpha_j^5=O(\delta^4)\),
\[
\langle u\rangle=-\frac1{3\pi}\sum_j\alpha_j^3+O(\delta^4),\quad
L=2\pi-\frac13\sum_j\alpha_j^3+O(\delta^4). \tag{7}
\]
Combining (6) and (7) and expanding \(M/L\) shows
\[
\frac2{\pi^2}-\frac ML=\frac1{3\pi^3}\sum_j\alpha_j^3
+O\!\left(\delta^4\log\frac1\delta\right)
=\frac1{24\pi^3}\sum_j\Delta_j^3
+O\!\left(\delta^4\log\frac1\delta\right).
\]
This is (1). Convexity of \(t\mapsto t^3\) yields \(\sum_j\Delta_j^3\ge(2\pi)^3/m^2\), with equality only when all gaps are equal; the latter statement applies only to the leading energy.

**4. Isolating the logarithmic term for regular polygons.** Now \(\alpha=\pi/n\) and all side midpoints are spaced by \(2\alpha\). The functions \(u\) and \(v\) are \(2\alpha\)-periodic in the angular variable, with
\[
 u(\eta+t)=\cos\alpha\sec t-1,\qquad
 w(\eta+t)=\alpha\cot\alpha\sec^2t,
 \quad |t|\le\alpha.
\]
Writing \(z=t/\alpha\), uniformly for \(|z|\le1\),
\[
u=\frac{\alpha^2}{2}(z^2-1)+O(\alpha^4),\quad
v=\alpha^2\left(z^2-\frac13\right)+O(\alpha^4),
\]
so, with respect to uniform *angle*,
\[
\langle u\rangle=-\frac{\alpha^2}{3}+O(\alpha^6),
\qquad \operatorname{Var}(u)=\frac{\alpha^4}{45}+O(\alpha^6). \tag{8}
\]
The stronger error in the mean follows from the exact integral in step 3: the fourth-degree Taylor coefficient cancels.

Retain one more term from (4):
\[
D=2s_\beta+s_\beta(u+u')
+h(\beta)(u-u')^2+\mathcal R,\quad
h(\beta)=\frac{1-s_\beta^2}{4s_\beta}.
\tag{9}
\]
The remainder has integrated size \(O(\alpha^4)\), uniformly in \(n\): expanding the square root as in step 2 bounds it by a constant times
\[
s_\beta\alpha^4+\frac{\alpha^2(u-u')^2}{s_\beta}
+\frac{(u-u')^4}{s_\beta^3},
\]
whose integrals are respectively \(O(\alpha^4)\), \(O(\alpha^6\log(1/\alpha))\), and \(O(\alpha^6)\) by (3). Here and below all expectations are normalized angular integrals.

The \(v(\phi)v(\psi)\) correction to the \(2s_\beta\) term is \(O(\alpha^6)\), not merely \(O(\alpha^4)\): the kernel has Fourier coefficients bounded by \(C/(1+k^2)\), while the mean-zero \(v\) has Fourier support only at nonzero multiples of \(n\), and \(\langle v^2\rangle=O(\alpha^4)\). Its linear corrections vanish. Corrections involving \(v\) in the linear radial term are \(O(\alpha^4)\). Weighting the singular quadratic term by \(w(\phi)w(\psi)\) instead of one changes it by at most \(O(\alpha^6\log(1/\alpha))\). Thus the only order-\(\alpha^4\log(1/\alpha)\) term comes from
\[
Q=\frac1{2\pi}\int_{-\pi}^{\pi}h(\beta)H(\beta)\,d\beta,\qquad
H(\beta)=\left\langle\left(u(\phi)-u(\phi-\beta)\right)^2\right\rangle. \tag{10}
\]
The function \(H\) is even, \(2\alpha\)-periodic, bounded by \(C\alpha^4\), and satisfies \(H(\beta)\le C\alpha^2\beta^2\) near zero. Its mean over any complete period is \(2\operatorname{Var}(u)\). Consequently a primitive of \(H-2\operatorname{Var}(u)\), taken from a period boundary, has sup norm at most \(C\alpha^5\). Integration by parts against \(1/\beta\) gives
\[
\int_\alpha^1\frac{H(\beta)}\beta\,d\beta
=2\operatorname{Var}(u)\log\frac1\alpha+O(\alpha^4). \tag{11}
\]
Indeed, the boundary and derivative terms are bounded by \(C\alpha^5/\alpha\); the interval below \(\alpha\) contributes \(O(\alpha^4)\). Since \(h(\beta)=1/(2|\beta|)+O(|\beta|)\) near zero and is bounded on every interval separated from zero, (10)–(11) imply
\[
Q=\frac{\operatorname{Var}(u)}{\pi}\log\frac1\alpha+O(\alpha^4)
=\frac{\alpha^4}{45\pi}\log\frac1\alpha+O(\alpha^4). \tag{12}
\]
By (8)–(12),
\[
M(P_n)=\frac4\pi\left(1-\frac{\alpha^2}{3}\right)
+\frac{\alpha^4}{45\pi}\log\frac1\alpha+O(\alpha^4),
\qquad L(P_n)=2\pi\left(1-\frac{\alpha^2}{6}+O(\alpha^4)\right).
\]
Dividing, inserting \(\alpha=\pi/n\), and subtracting from \(2/\pi^2\) gives (2). Every error estimate is analytic and uniform; finite computations are not used to infer any limit.

## Verification

The accompanying `verify_chord.py` computes the **independent original Euclidean edge-pair double integrals**, rather than evaluating the angular asymptotic expression. Same-edge integrals are inserted exactly; other edge pairs are evaluated by tensor Gauss–Legendre quadrature. Its regular-polygon checks use \(n=20,40,80,160,320\); in the logarithm-corrected scale
\[
n^4\left(\mathcal G(P_n)-\frac1{3n^2}\right)+\frac{\pi^2}{90}\log n,
\]
values move from approximately \(-0.28125\) at \(n=20\) to \(-0.27716\) at \(n=320\), consistent with the bounded remainder. Nonuniform sinusoidally modulated gap lists for \(n=12,20,40,80\) show leading-cubic relative errors decreasing from approximately \(-2.17\%\) to \(-0.062\%\). Execute `python verify_chord.py` with NumPy installed. The proof above, rather than finite quadrature, establishes the theorems.

## Relationship to prior work

Tokmachev (2022) proved that the disk uniquely maximizes \(\mathbb E\|X-Y\|/L\), and established a still stronger upper bound at every fixed perimeter separation, using Fourier series. Both statements are prior facts and do not themselves supply a sharp, uniform angular-gap coefficient. Shen (2026) supplies the complementary universal sharp lower bound, motivating quantitative understanding of the same normalized mean. A previously stated exact finite-\(n\) expression for regular-polygon boundary distance appears in the public MathBench problem MB14-T4S-P064; that source covers exact regular-\(n\) means, but not arbitrary gap patterns or the explicit uniform cubic-gap law. Its full proposed proof is not included on the problem page; the regular asymptotic coefficient is not claimed as independently novel relative to that exact finite-\(n\) formula. A prior regular-polygon near-diameter chord-tail result studies a distinct rare-event regime and does not imply (1) or (2). We claim neither an exact finite-\(n\) formula nor a full optimization theorem among all \(n\)-gons.

## Limitations

The estimate (1) requires **all** central-angle gaps to shrink and does not cover arbitrary convex polygons or polygons with a macroscopic unrefined arc. The error \(O(\delta^4\log(1/\delta))\) is uniform but is not asserted optimal for every nonuniform mesh. The logarithmic refinement (2) is proved for regular polygons only; there is no claim of a universal logarithmic coefficient for nonuniform partitions. Leading-order Jensen optimality does not establish exact finite-\(n\) maximization. Priority is provisional pending independent literature review, especially unindexed articles and possible consequences of published exact regular-polygon formulas. No independent audit is claimed.

## References

1. E. Shen, *A Sharp Perimeter Inequality for Mean Distances on Convex Curves*, arXiv:2611.21661v1 (7 November 2026), https://arxiv.org/abs/2611.21661 ; full text https://borowiecki.dev/pdf/2611.21661 .
2. A. S. Tokmachev, *Mean distance between random points on the boundary of a convex body*, Zap. Nauchn. Sem. POMI **510** (2022), 248–261; English version J. Math. Sci. **286** (2024), 798–806, https://www.mathnet.ru/znsl7205 .
3. *Distance Formula for Two Boundary Points of a Regular Polygon*, MathBench problem MB14-T4S-P064 (public problem statement; exact finite-\(n\) formula), https://mathbench.ai/en/items/MB14-T4S-P064 .
