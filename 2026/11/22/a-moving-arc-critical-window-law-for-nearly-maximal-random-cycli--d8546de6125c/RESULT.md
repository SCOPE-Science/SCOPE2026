# A moving-arc critical-window law for nearly maximal random cyclic triangles

## Finding
Let
\[
L_c=\frac{2\pi}{3},\qquad \gamma=\frac{3\sqrt3}{16},\qquad
\beta=\frac{\sqrt3}{4},\qquad A_*=\frac{3\sqrt3}{4}.
\]
For a fixed real number \(\lambda\) and sufficiently small \(\varepsilon>0\), put \(L_\varepsilon=L_c+\lambda\sqrt\varepsilon\). Sample three independent angles uniformly on the closed interval \([-L_\varepsilon,L_\varepsilon]\); the corresponding points on the unit circle enclose a random (unoriented) triangle area \(T_\varepsilon\). Let \(M(L)\) be the maximum area of three points on that arc, which is exactly
\[
M(L)=F\!\left(\min\left\{2L,\frac{4\pi}{3}\right\}\right),
\quad F(s)=\sin\frac s2\left(1-\cos\frac s2\right),
\qquad 0<L<\pi.
\]
Define
\[
q(\lambda)=1+4\gamma\min(\lambda,0)^2,
\qquad D_\lambda=
\bigl\{(u,v,z):u,v\ge0,\ \gamma(u+v-2\lambda)^2+\beta z^2<q(\lambda)\bigr\}.
\]
Then **the sharp moving-support critical-window law** is
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{-3/2}
\Pr\{T_\varepsilon>M(L_\varepsilon)-\varepsilon\}
=\Psi(\lambda)=\frac{3}{4L_c^3}\operatorname{Vol}_3(D_\lambda).}
\]
The limit is locally uniform for \(\lambda\) in compact real intervals. An explicit one-dimensional representation is
\[
\boxed{\Psi(\lambda)=\frac{3}{2L_c^3\sqrt\beta}
\int_0^\infty w\sqrt{\bigl[q(\lambda)-\gamma(w-2\lambda)^2\bigr]_+}\,dw,}
\]
where \([x]_+=\max\{x,0\}\). It is finite and strictly positive for each finite \(\lambda\). It satisfies
\[
\Psi(0)=\frac{6\,3^{1/4}}{\pi^3},\qquad
\Psi(\lambda)=\frac{4\pi\lambda}{L_c^3}
\quad\left(\lambda\ge\frac1{2\sqrt\gamma}\right),
\]
and its far-subcritical matching law is
\[
\Psi(\lambda)\sim\frac{1}{40L_c^3\gamma^2\sqrt\beta\,\lambda^2}
\qquad(\lambda\to-\infty).
\]

The theorem also gives the **conditional shape law**. Write the ordered sample angles as \(\theta_{(1)}<\theta_{(2)}<\theta_{(3)}\), and set
\[
U_\varepsilon=\frac{\theta_{(1)}+L_\varepsilon}{\sqrt\varepsilon},\quad
V_\varepsilon=\frac{L_\varepsilon-\theta_{(3)}}{\sqrt\varepsilon},\quad
Z_\varepsilon=\frac{\theta_{(2)}-(\theta_{(1)}+\theta_{(3)})/2}{\sqrt\varepsilon}.
\]
Conditional on \(T_\varepsilon>M(L_\varepsilon)-\varepsilon\), the joint law of \((U_\varepsilon,V_\varepsilon,Z_\varepsilon)\) converges **in total variation** to normalized Lebesgue measure on \(D_\lambda\), locally uniformly in \(\lambda\). In particular, the rare-event endpoint deficits and middle-point displacement are of the same \(\sqrt\varepsilon\) order precisely in the critical window.

## Assumptions and scope
The circle has radius one. There are exactly three independent random points sampled with the uniform **angle** distribution on the one connected, oriented arc of length \(2L_\varepsilon\). On a circle this is also uniform boundary arclength. The arc has length less than a complete revolution for all sufficiently small \(\varepsilon\), because \(L_\varepsilon\to2\pi/3<\pi\). The moving-arc parameter \(\lambda\in\mathbb R\) is fixed in the basic theorem; compact-uniform limits are also asserted. All areas are nonnegative ordinary Euclidean areas. The maximum \(M(L_\varepsilon)\), not the constant \(A_*\), is used to normalize the upper tail below the transition. The quantity \(\operatorname{Vol}_3\) means ordinary three-dimensional Lebesgue volume.

## Proof
**1. Exact geometry, global maximization, and the critical span.** Almost surely order the three angles as \(a<b<c\), and introduce their span \(s=c-a\) and midpoint deviation \(d=b-(a+c)/2\). They satisfy \(0<s<2L\), \(|d|<s/2\). The determinant formula for an inscribed triangle yields exactly
\[
T=\frac12\bigl(\sin(b-a)+\sin(c-b)-\sin(c-a)\bigr)
=\sin\frac s2\left(\cos d-\cos\frac s2\right).
\]
For fixed \(0<s<2\pi\), the expression is maximized uniquely at \(d=0\), so its maximum is \(F(s)\). Its derivative is
\[
F'(s)=\frac12\left(1-\cos\frac s2\right)
\left(1+2\cos\frac s2\right).
\]
This derivative is positive until \(s_c=4\pi/3\) and negative thereafter. Hence the exact maximum on any arc \(0<L<\pi\) is the displayed \(M(L)\). For \(L\le L_c\), its ordered maximizing triangle has both arc endpoints and the angular midpoint; for \(L>L_c\), the maximizing triangles are equilateral and may translate within an arc subinterval of length \(2(L-L_c)\). At the critical span the continuum of equilateral locations first appears.

**2. Uniform local expansion.** Put \(s_c=4\pi/3\). Direct differentiation gives \(F(s_c)=A_*\), \(F'(s_c)=0\), \(-F''(s_c)/2=\gamma\), and \(\sin(s_c/2)/2=\beta\). Taylor expansion in a fixed neighborhood gives
\[
A_*-T=\gamma(s-s_c)^2+\beta d^2
+O\!\left(|s-s_c|^3+|s-s_c|d^2+d^4\right).
\]
The positive coefficients imply a local two-sided quadratic bound in \((s-s_c,d)\). Together with uniqueness of the maximizing span and midpoint, compactness of the fixed angular domain implies that whenever \(L_\varepsilon=L_c+O(\sqrt\varepsilon)\) and \(T>M(L_\varepsilon)-\varepsilon\), the quantities \(|s-s_c|\) and \(|d|\) are \(O(\sqrt\varepsilon)\), uniformly for bounded \(\lambda\). In particular, both endpoint deficits are \(O(\sqrt\varepsilon)\), because \(u+v=2L_\varepsilon-s\ge0\). The extra two-dimensional bounds used below are therefore uniform on compact sets of \(\lambda\).

**3. Moving maximum and the scaled limit domain.** When \(\lambda<0\), the available maximal span is \(2L_\varepsilon=s_c+2\lambda\sqrt\varepsilon\). When \(\lambda\ge0\), the equilateral span remains admissible. Consequently,
\[
M(L_\varepsilon)=A_*-4\gamma\min(\lambda,0)^2\varepsilon
+O_K(\varepsilon^{3/2})
\]
for \(\lambda\) in any compact interval \(K\). Make the exact substitution
\[
a=-L_\varepsilon+\sqrt\varepsilon\,u,\quad
c=L_\varepsilon-\sqrt\varepsilon\,v,\quad
b=(a+c)/2+\sqrt\varepsilon\,z.
\]
Then \(s-s_c=\sqrt\varepsilon(2\lambda-u-v)\) and \(d=\sqrt\varepsilon z\). The event condition after division by \(\varepsilon\) converges, locally uniformly, to
\[
\gamma(u+v-2\lambda)^2+\beta z^2<1+4\gamma\min(\lambda,0)^2.
\]
The exact ordered-angle density on \([-L_\varepsilon,L_\varepsilon]^3\) is \(6/(2L_\varepsilon)^3=3/(4L_\varepsilon^3)\), while the Jacobian of the substitution is \(\varepsilon^{3/2}\). The resulting scaled event indicators are supported in one compact box for each compact range of \(\lambda\). Their boundary ellipses have three-dimensional Lebesgue measure zero. Dominated convergence, uniformly with respect to such \(\lambda\) (via uniform Taylor remainders and vanishing volume of thin quadratic boundary neighborhoods), establishes the stated area-tail coefficient. The same argument yields convergence of the conditional scaled **densities in \(L^1\)**, hence the total-variation conditional limit; no finite discretization substitutes for this proof.

**4. Exact profile and crossover ends.** Parameterizing \(w=u+v\) with \(u\in[0,w]\) makes the \((u,v)\)-slice length \(w\). At each \(w\), the admissible \(z\)-interval has length \(2\sqrt{[q-\gamma(w-2\lambda)^2]_+}/\sqrt\beta\), proving the integral representation. At \(\lambda=0\), substitution \(y=\gamma w^2\) evaluates the profile as \(1/(2L_c^3\gamma\sqrt\beta)=6\,3^{1/4}/\pi^3\). For \(\lambda\ge1/(2\sqrt\gamma)\), the entire ellipse in \((w,z)\) lies in \(w\ge0\), and its first \(w\)-moment equals \(2\lambda\) times its area \(\pi/\sqrt{\gamma\beta}\). As \(\sqrt{\gamma\beta}=3/8\), this is exactly \(4\pi\lambda/L_c^3\). Finally set \(\lambda=-t\), \(t\to\infty\). The integrand's squared radical becomes \(1-4\gamma t w-\gamma w^2\), so put \(w=x/t\), apply dominated convergence, and use
\[
\int_0^{1/(4\gamma)}x\sqrt{1-4\gamma x}\,dx=\frac1{60\gamma^2}.
\]
This gives the stated reciprocal-square matching asymptotic. The same integral proves finiteness, positivity and continuity of \(\Psi\).

## Verification
The companion runnable script `verify_critical_arc.py` uses independently computed exact one-dimensional quadrature of the original three-angle probability, compares its near-critical ratios at six negative/zero/positive values of \(\lambda\) to the candidate profile, and tests the closed formulas and large-negative matching asymptotic. Execute using Python 3 with SciPy available:

```bash
python verify_critical_arc.py
```

It reports `MOVING_ARC_AREA_CRITICAL_WINDOW_CHECKS_OK` after all assertions. These are numerical and symbolic consistency checks only; the exact global optimization, compact localization, locally uniform measure convergence, and integral evaluations are established by the proof above.

## Relationship to prior work
The fixed-circle upper-area coefficient in E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360 (first posted January 7, 2013), concerns three circle samples and larger random-polygon extremes. It does not vary the **available sampling arc** jointly with the area deficit. Nikitin and Simarova, *Generalized Limit Theorems for U-max Statistics*, arXiv:2010.04460, treat fixed circle kernels and distributions as the sample size grows, not the moving-support three-point corner-to-interior degeneration quantified here. The published study *A sharp circle-to-threefold-oval crossover for nearly maximal random inscribed triangles* concerns smooth threefold radial deformations of a full convex boundary; its rotational degeneracy is broken by a changed radial shape, rather than by two simultaneously active sampling-arc endpoints. The present result's precise integration domain, two-sided moving-center profile, reciprocal-square negative matching, exact eventually-linear positive branch, and conditional joint endpoint shape law are not statements of those comparisons. A fixed-arc, fixed-parameter tail classification cannot alone yield a limit in which the arc parameter varies on the same scale as the endpoint deficit; the joint estimates above are essential.

## Limitations
This is a critical-window theorem for **three** independent circle-boundary points only, with the arc half-length approaching \(2\pi/3\) at order \(\sqrt\varepsilon\). It does not give an entire distribution, a many-point extreme-value theorem, or uniform estimates when \(|\lambda|\to\infty\) simultaneously with \(\varepsilon\downarrow0\). The matching limits concern the already derived limiting profile, not an interchange of the two limits. The mathematical argument and checker have not been independently audited; literature comparisons do not certify definitive historical priority.

## References
1. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360 (first public version 2013-01-07). https://arxiv.org/abs/1301.1360
2. Ya. Yu. Nikitin and E. N. Simarova, *Generalized Limit Theorems For U-max Statistics*, arXiv:2010.04460 (first public version 2020-10-09). https://arxiv.org/abs/2010.04460
3. *A sharp circle-to-threefold-oval crossover for nearly maximal random inscribed triangles*, publicly accessible research note, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-circle-to-threefold-oval-crossover-for-nearly-maximal-ra--9518dfca4b6c
4. E. W. Weisstein, *Circle Triangle Picking*, MathWorld, https://mathworld.wolfram.com/CircleTrianglePicking.html
