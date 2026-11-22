# Universal two-axis width-deviation instability and cubic cusp of rhombi

## Finding
For fixed \(t>0\), and real \(s,h\) satisfying \(|s|<1\), \(|h|<t\), let
\[
 Q_{t,s,h}=\operatorname{conv}\{(s-1,0),(s+1,0),(0,h-t),(0,h+t)\}.
\]
Its perpendicular diagonals have **fixed lengths** \(2\) and \(2t\), and its area is always \(2t\). The polygon \(Q_{t,0,0}\) is a rhombus; for generic \(sh\ne0\), \(Q_{t,s,h}\) is not a kite. Let \(W_{t,s,h}\) be its Euclidean width in a Haar-uniform, unoriented direction. Write
\[
 \Delta(t,s,h)=\frac{\operatorname{Var}(W_{t,s,h})}{(\mathbb EW_{t,s,h})^2}.
\]
Set \(R=\sqrt{1+t^2}\), \(I_0(t)=\pi+2(t^2-1)\arctan t+2t\), and \(H(t)=I_0(t)-4t\). For every fixed \(t>0\), with \(\varepsilon=|s|+|h|\to0\), one has the two-parameter, **uniform-in-direction-of-approach** expansion
\[
 \boxed{\begin{aligned}
 \Delta(t,s,h)= {}&\frac{\pi I_0(t)}{8(1+t^2)}-1
 -\frac{\pi H(t)}{8(1+t^2)^3}\bigl(t^2s^2+h^2\bigr)\\
 &+\frac{\pi}{12(1+t^2)^3}\bigl(|ts+h|^3+|ts-h|^3\bigr)
 +O_t(\varepsilon^4).
 \end{aligned}}
\]
Furthermore, \(H(t)>0\) for **every** \(t>0\). Thus each rhombus is a **strict local maximum** of squared directional-width deviation in the entire two-parameter class of orthodiagonal quadrilaterals having its two diagonal lengths, and neither a local minimum of width deviation among arbitrary convex quadrilaterals nor a minimizer along this fixed-diagonal subfamily. The positive cubic term produces a non-smooth third-order response with switching ridges \(h=\pm ts\); the function has a quadratic Taylor expansion but no cubic Taylor polynomial at the rhombus.

For the square, the expansion reads
\[
 \Delta(1,s,h)=\frac{\pi(\pi+2)}{16}-1
 -\frac{\pi(\pi-2)}{64}(s^2+h^2)
 +\frac{\pi}{96}(|s+h|^3+|s-h|^3)
 +O((|s|+|h|)^4).
\]
The mixed skew term, and its two switching ridges, are not determined by considering one-axis kite perturbations separately.

## Assumptions and scope
All bodies are genuine convex quadrilaterals: \(t>0\), \(|s|<1\), \(|h|<t\). Projection width is the difference of maximal and minimal scalar projections onto a direction, not chord length or a random-line section. The direction is uniform modulo \(\pi\). Here \(O_t\) means a bound with a constant that may depend on fixed \(t\), but is uniform over all small pairs \((s,h)\). The theorem is **local** in the two displacements, not a claim of global maximization over the entire orthodiagonal class or optimization among all quadrilaterals. Every nondegenerate rhombus is similar to one of the \(Q_{t,0,0}\), so the instability statement covers all rhombus shapes.

## Proof
**1. Exact support identity.** Put \(c=\cos\theta\), \(z=\sin\theta\) for \(0\le\theta\le\pi/2\). Positive and negative angular quadrants give the widths
\[
 W_\pm(\theta)=\max\{(1+s)c,(t\pm h)z\}+\max\{(1-s)c,(t\mp h)z\}.
\]
The identity \(\max(a,b)=(a+b+|a-b|)/2\) and \((|x+y|+|x-y|)/2=\max\{|x|,|y|\}\) show, without any approximation, that
\[
 W_\pm(\theta)=c+tz+\max\bigl(|c-tz|,|sc\mp hz|\bigr).
\]
The signs do not matter upon summing both angular quadrants. At \(s=h=0\), the common width is \(W_0(\theta)=c+tz+|c-tz|=2\max\{c,tz\}\). Define \(D_\pm=(|sc\mp hz|-|c-tz|)_+\), so \(W_\pm=W_0+D_\pm\). All changes are nonnegative and supported only near the unique crossover \(\theta_0=\arctan(1/t)\).

**2. Local crossover integration, including the cubic term.** Write \(R=\sqrt{1+t^2}\), \(\varepsilon=|s|+|h|\), and \(\xi=\theta-\theta_0\). Near \(\xi=0\),
\[
 c-tz=-R\xi+O_t(\xi^3),\qquad c+tz=\frac{2t}{R}+O_t(\xi),
\]
\[
 sc\mp hz=a_\pm+b_\pm\xi+O_t(\varepsilon\xi^2),
 \quad a_\pm=\frac{ts\mp h}{R},\quad b_\pm=O_t(\varepsilon).
\]
The support of \(D_\pm\) has \(|\xi|=O_t(\varepsilon)\). For the model \(d(\xi)=(|a+b\xi|-R|\xi|)_+\), with \(|b|<R/2\), elementary integration of the two triangles gives, uniformly even as \(a\to0\),
\[
 \int d(\xi)\,d\xi=\frac{a^2}{R}+O_t(\varepsilon^4),\qquad
 \int\xi d(\xi)\,d\xi=O_t(\varepsilon^4),
\]
\[
 \int 2R|\xi|d(\xi)\,d\xi=\frac{2|a|^3}{3R}+O_t(\varepsilon^4),\qquad
 \int d(\xi)^2\,d\xi=\frac{2|a|^3}{3R}+O_t(\varepsilon^4).
\]
For completeness, if \(a\ne0\) the two triangles have positive horizontal extents \(|a|/(R\mp\operatorname{sgn}(a)b)\), so their areas sum to \(a^2R/(R^2-b^2)\); analogous elementary integrals prove the displayed moment formulas. When \(a=0\), the model contribution vanishes for \(|b|<R\). Replacing the model by the actual trigonometric expressions perturbs \(D_\pm\) pointwise by \(O_t(\varepsilon^3)\) throughout its \(O_t(\varepsilon)\)-wide support; the resulting integral error is \(O_t(\varepsilon^4)\). Therefore
\[
 \int_0^{\pi/2}D_\pm\,d\theta
  =\frac{(ts\mp h)^2}{R^3}+O_t(\varepsilon^4),
\]
\[
 \int_0^{\pi/2}(W_\pm^2-W_0^2)\,d\theta
 =\frac{4t(ts\mp h)^2}{R^4}
 +\frac{4|ts\mp h|^3}{3R^4}+O_t(\varepsilon^4).
\]
Here the cubic contribution comes from both \(2|c-tz|D_\pm\) and \(D_\pm^2\); neglecting either produces an incorrect coefficient. Terms odd in \(\xi\) do not produce order-three contributions because the slope \(b_\pm\) is itself order \(\varepsilon\).

**3. Moment normalization.** Directly integrating \(W_0\) on its two angular pieces yields
\[
 \int_0^{\pi/2} W_0\,d\theta=2R,\qquad
 \int_0^{\pi/2}W_0^2\,d\theta=I_0(t).
\]
Put \(Q=t^2s^2+h^2\). Haar averaging of the two quadrants and the previous estimates gives
\[
 \mathbb EW_{t,s,h}=\frac{4R}{\pi}+\frac{2Q}{\pi R^3}+O_t(\varepsilon^4),
\]
\[
 \mathbb EW_{t,s,h}^2=\frac{2I_0(t)}{\pi}
 +\frac{8tQ}{\pi R^4}
 +\frac4{3\pi R^4}\bigl(|ts+h|^3+|ts-h|^3\bigr)
 +O_t(\varepsilon^4).
\]
Substitute into \(\Delta=\mathbb EW^2/(\mathbb EW)^2-1\). Since \(Q=O(\varepsilon^2)\), all products of distinct correction terms start at order four. The result is exactly the boxed formula in the Finding.

**4. Universal strict sign and rigidity.** Let \(H(t)=\pi+2(t^2-1)\arctan t-2t\). If \(0<t\le1\), the bound \(\arctan t\le t\) (with a nonpositive multiplier) gives
\[
 H(t)\ge\pi-4t+2t^3\ge\pi-\frac83>0.
\]
If \(t\ge1\), the bound \(\arctan t\ge\pi/4\) gives
\[
 H(t)\ge\frac\pi2(1+t^2)-2t\ge(\pi-2)t>0.
\]
Thus the quadratic form has negative coefficients in both independently available diagonal-skew modes. The positive cubic correction and order-four remainder cannot reverse the sign sufficiently near the origin. For each fixed \(t>0\), \(\Delta(t,s,h)<\Delta(t,0,0)\) whenever \((s,h)\ne(0,0)\) and \(|s|+|h|\) is sufficiently small. Since \(\Delta\ge0\) and the squaring map preserves the ordering of nonnegative deviation rates, the same strict inequality holds for the deviation rate itself. The restriction \(s=0\) has a nonzero \(|h|^3\) term, so no ordinary cubic Taylor polynomial exists at the rhombus.

## Verification
Run \(\texttt{python3 verify_width.py}\). The dependency-free program computes widths by direct maxima and minima of the four vertex projections and integrates them independently of the support-formula derivation. Its completed output is \(\texttt{ALL_CHECKS_PASSED: 203 numerical regressions}\): it checks symmetric base values, exact one-axis moment integrals, joint non-kite skews including both switching ridges, order-four expansion residual bounds, and strict local decreases at sample parameters. The analytic proof above is necessary for the universal statement; finite quadrature does not certify all \(t,s,h\) or the \(O_t\) remainder.

## Relationship to prior work
Akiyama and Kamae (2022) define and study this width-deviation functional and explicitly leave the four-vertex case open, displaying a numerical asymmetric-kite candidate. They provide general edge-based moment identities and a triangle-truncation variation, but not the two-axis orthodiagonal rhombus expansion or its strictly negative Hessian. A previously published exact random-width density for **all reflection-symmetric kites** determines the one-axis restrictions \(s=0\) and \(h=0\) in principle, and those one-axis calculations are **not claimed as new**. Its results do not apply to the generic quadrilateral \(Q_{t,s,h}\) with both offsets nonzero, hence do not imply the mixed cubic profile \(|ts+h|^3+|ts-h|^3\) or the all-two-axis orthodiagonal conclusion. Prior triangle-truncation width-variation results concern a different three-vertex parent shape. Other width-variance theorems for three-dimensional rhombic dodecahedra and equiangular polygons treat different objects and constraints. The new claim is the coupled fixed-diagonal two-parameter law and the associated full orthodiagonal local instability, not a global solution of the open quadrilateral minimization problem.

## Limitations
The local radius of the strict inequality depends on \(t\); no uniform radius across degenerating rhombi is asserted. The theorem does not claim the rhombus is a global maximum on its fixed-diagonal class (indeed other parameter values need not obey that comparison), nor identify a global minimum among quadrilaterals. The cubic approximation does not determine all fourth-order terms. Publication-priority checks cannot exclude inaccessible or unindexed earlier equivalents. No independent mathematical audit has been performed.

## References
1. S. Akiyama and T. Kamae, *Width deviation of convex polygons*, arXiv:2201.06736v1, publicly posted 2022-01-18; https://arxiv.org/html/2201.06736v1. In particular, introduction, Sections 3 and 7.
2. *Three spectral singularities reconstruct asymmetric kites from random widths*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-three-spectral-singularities-reconstruct-asymmetric-kites-from-r--0fca3299603f. Full RESULT.md inspected for the exact one-axis scope.
3. *Sharp width-variance rigidity for diagonally stretched rhombic dodecahedra*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-width-variance-rigidity-for-diagonally-stretched-rhombic-d--de157683afa4. Different-dimensional comparator.
