# Three diameter-tail regimes and a cusp crossover for time-uniform trochoid pairs

## Finding

Let \(\beta>0\) and consider one complete rolling-circle period of the trochoid
\[
\gamma_\beta(t)=(t-\beta\sin t,\;1-\beta\cos t),\qquad 0\le t\le2\pi.
\]
Let \(T_1,T_2\) be independent uniform variables on \([0,2\pi]\), and set \(Z_\beta=\|\gamma_\beta(T_1)-\gamma_\beta(T_2)\|\). In particular this is **uniform rolling phase, not uniform curve arclength**. Write \(D_\beta=\max_{s,t\in[0,2\pi]}\|\gamma_\beta(s)-\gamma_\beta(t)\|\).

**Exact diameter and maximizing points.** For \(0<\beta\le1\), \(D_\beta=2\pi\), uniquely realized, up to exchanging points, by the two period endpoints. For \(\beta>1\), set \(a_\beta=\arccos(1/\beta)\), \(q_\beta=\sqrt{\beta^2-1}\), and \(\Delta_\beta=2\pi-2a_\beta\). Then
\[
D_\beta=\Delta_\beta+2q_\beta=2(\pi-a_\beta+q_\beta),
\]
uniquely attained, up to exchange, at phases \(a_\beta\) and \(2\pi-a_\beta\). As \(\beta\downarrow1\) from above,
\[
D_\beta-2\pi\sim\frac{4\sqrt2}{3}(\beta-1)^{3/2}.
\]

**Fixed-parameter rare-diameter laws.** For \(\varepsilon\downarrow0\),
\[
\Pr(Z_\beta>D_\beta-\varepsilon)\sim
\begin{cases}
\displaystyle\frac{\varepsilon^2}{4\pi^2(1-\beta)^2},&0<\beta<1,\\[5pt]
\displaystyle C_*\varepsilon^{2/3},&\beta=1,\\[5pt]
\displaystyle\frac1{\pi\sqrt{\beta^2-1}}\sqrt{\frac{D_\beta}{\Delta_\beta}}\,\varepsilon,&\beta>1,
\end{cases}
\]
where
\[
C_*=\frac{6^{2/3}}{2\pi^2}\frac{\Gamma(4/3)^2}{\Gamma(5/3)}.
\]
Thus the three exponents are \(2,2/3,1\), respectively.

**Exact critical-window coefficient and conditional shape.** Fix \(\lambda\in\mathbb R\), put \(\beta_\varepsilon=1+\lambda\varepsilon^{2/3}\), and define
\[
M(\lambda)=\frac{4\sqrt2}{3}(\max\{\lambda,0\})^{3/2},\qquad
S_\lambda=\left\{(x,y)\in[0,\infty)^2:\frac{x^3+y^3}{6}-\lambda(x+y)<1-M(\lambda)\right\}.
\]
The set \(S_\lambda\) is bounded and has strictly positive finite area. Then
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{-2/3}\Pr(Z_{\beta_\varepsilon}>D_{\beta_\varepsilon}-\varepsilon)=\frac{|S_\lambda|}{2\pi^2}.}
\]
Moreover, conditionally on this event, the two endpoint-order branches have equal limiting probability. On the branch with \(T_1\) near zero and \(T_2\) near \(2\pi\), the rescaled pair \((T_1,2\pi-T_2)/\varepsilon^{1/3}\) converges **in total variation** to the uniform law on \(S_\lambda\); the opposite branch is obtained by exchanging the labels. The crossover coefficient satisfies
\[
\frac{|S_\lambda|}{2\pi^2}\sim\frac{1}{4\pi^2\lambda^2}\quad(\lambda\to-\infty),\qquad
\frac{|S_\lambda|}{2\pi^2}\sim\frac1{\sqrt2\pi\sqrt\lambda}\quad(\lambda\to+\infty).
\]

## Assumptions and scope

The rolling circle has unit radius; scaling all coordinates by a fixed positive radius scales all lengths and thresholds accordingly. Only one **closed parameter interval** \([0,2\pi]\) is used, not an infinite periodic trochoid. Its distinct endpoints have the same height but different horizontal coordinates. Uniform phase is a legitimate physical sampling convention for a wheel turning with constant angular speed, and differs from arclength sampling. The parameter \(\beta\) is the tracer's distance from the wheel center divided by wheel radius. \(\beta<1\) is curtate, \(\beta=1\) is the ordinary cycloid, and \(\beta>1\) is prolate. Probabilities refer to two independent phase samples; both pair orders count.

## Proof

**1. Exact two-point reduction and diameter.** For \(0\le t_1<t_2\le2\pi\) put \(\Delta=t_2-t_1\), \(m=(t_1+t_2)/2\). Direct trigonometry gives
\[
\|\gamma_\beta(t_2)-\gamma_\beta(t_1)\|^2
=\Delta^2+4\beta^2\sin^2(\Delta/2)-4\beta\Delta\sin(\Delta/2)\cos m.
\]
For each \(\Delta\in(0,2\pi)\), the admissible midpoint range is \([\Delta/2,2\pi-\Delta/2]\), which contains \(\pi\). Therefore the unique maximizing midpoint is \(m=\pi\), and its distance is \(F_\beta(\Delta)=\Delta+2\beta\sin(\Delta/2)\). Since \(F_\beta'(\Delta)=1+\beta\cos(\Delta/2)\), the unique maximizing gap is \(2\pi\) if \(\beta\le1\), and \(\Delta_\beta=2\arccos(-1/\beta)\) if \(\beta>1\). These give the diameter and pairs stated. Expanding \(2(q_\beta-a_\beta)\) at \(\beta=1+\delta\) gives \((4\sqrt2/3)\delta^{3/2}+O(\delta^{5/2})\).

**2. The three fixed-parameter tails.** The maximizing unordered pair is unique. Thus any almost-maximizing ordered pair is, by compactness, in one of two arbitrarily small neighborhoods of the maximizing pair and its reversal. The joint phase density is \(1/(4\pi^2)\).

If \(0<\beta<1\), write \(t_1=s\), \(t_2=2\pi-u\) with \(s,u\ge0\) small. Here
\[
D_\beta-\|\gamma_\beta(2\pi-u)-\gamma_\beta(s)\|
=(1-\beta)(s+u)+O((s+u)^3).
\]
Consequently the admissible region has area \(\varepsilon^2/[2(1-\beta)^2]+o(\varepsilon^2)\); including both point orders yields \(\varepsilon^2/[4\pi^2(1-\beta)^2]+o(\varepsilon^2)\).

At \(\beta=1\) the linear term cancels. The exact horizontal and vertical differences are
\[
H=2\pi-s-u+\sin s+\sin u,\qquad V=\cos s-\cos u.
\]
For \(s,u\downarrow0\), \(H=2\pi-(s^3+u^3)/6+O((s+u)^5)\), \(V=O((s+u)^2)\), hence
\[
D_1-\sqrt{H^2+V^2}=\frac{s^3+u^3}{6}+O((s+u)^4).
\]
The area of \(\{s,u\ge0:s^3+u^3<6\varepsilon\}\) equals \((6\varepsilon)^{2/3}\Gamma(4/3)^2/\Gamma(5/3)\). Include the two point orders and density \(1/(4\pi^2)\) to obtain \(C_*\).

If \(\beta>1\), expand around the maximizing phase gap \(\Delta_\beta\) and midpoint \(\pi\): with \(v=\Delta-\Delta_\beta\) and \(z=m-\pi\),
\[
D_\beta-\|\gamma_\beta(t_2)-\gamma_\beta(t_1)\|
=\frac{q_\beta}{4}v^2+\frac{q_\beta\Delta_\beta}{D_\beta}z^2+o(v^2+z^2).
\]
The Jacobian of \((m,\Delta)\mapsto(t_1,t_2)\) is one. The ellipse enclosed by the displayed quadratic inequality has area \((2\pi\varepsilon/q_\beta)\sqrt{D_\beta/\Delta_\beta}\). Multiplying by two orders and by \(1/(4\pi^2)\) yields the fixed prolate law.

**3. Moving critical window.** Let \(\beta_\varepsilon=1+\lambda\varepsilon^{2/3}\). The unique maximizing pair converges to the opposite parameter endpoints. On the ordered near-endpoint branch put \(s=\varepsilon^{1/3}x\), \(u=\varepsilon^{1/3}y\). Taylor expansion uniformly for bounded \((x,y)\) yields
\[
\frac{\|\gamma_{\beta_\varepsilon}(2\pi-u)-\gamma_{\beta_\varepsilon}(s)\|-2\pi}{\varepsilon}
=\lambda(x+y)-\frac{x^3+y^3}{6}+o(1),
\]
while \((D_{\beta_\varepsilon}-2\pi)/\varepsilon\to M(\lambda)\). Hence the near-diameter condition tends to the strict sublevel inequality defining \(S_\lambda\). The boundary of \(S_\lambda\) has planar measure zero (it is a nonconstant polynomial level set). The cubic term dominates the linear term outside a fixed scaled compact set. More precisely, the exact pair-gap formula from Step 1, localized near the unique critical maximizing endpoints, gives a uniform lower bound \(D_{\beta_\varepsilon}-Z_{\beta_\varepsilon}\ge c(s^3+u^3)-C|\beta_\varepsilon-1|(s+u)\) for sufficiently small \(s,u\) and fixed positive \(c,C\); this confines the event to \(s+u=O_\lambda(\varepsilon^{1/3})\). Thus bounded convergence of indicator densities, combined with the pair-order factor, proves the stated limit and total-variation marked law. Positivity of \(|S_\lambda|\) follows because the polynomial's minimum is \(-M(\lambda)\), attained at \(x=y=\sqrt{2\max\{\lambda,0\}}\) (or the origin if \(\lambda\le0\)).

**4. Crossover matching.** For \(\lambda=-L\to-\infty\), the inequality in \(S_{-L}\) restricts to \(x+y<1/L+o(1/L)\), giving \(|S_{-L}|\sim 1/(2L^2)\). For \(\lambda\to+\infty\), expand the defining cubic around \(x=y=\sqrt{2\lambda}\): its quadratic rise is \(\sqrt{2\lambda}[(x-x_0)^2+(y-y_0)^2]/2\), so \(|S_\lambda|\sim\sqrt2\pi/\sqrt\lambda\). This matches the two fixed-parameter laws when their respective asymptotic regimes overlap.

## Verification

The attached standalone `verify.py` uses only Python's standard library. It checks the exact two-point distance identity, maximum-pair formula, strict global maximality against deterministic grids, numerical area ratios for the three tail regimes, and finite-threshold critical-crossover region ratios for both signs of \(\lambda\). The tests evaluate the actual curve coordinates, not a recycled analytic approximation. See `VERIFICATION.md` for thresholds and remaining limitations.

## Relationship to prior work

The standard trochoid parameterization and its curtate/cycloid/prolate partition are classical; for example Lockwood (1961), Bronshtein and colleagues' handbook, and Weisstein's MathWorld account treat these as established. They do not supply the phase-uniform two-point near-diameter law in the material inspected. The general polygon distance-distribution literature (e.g. Tong–Ahmadi–Pan, 2013) uses different planar regions and measures. Indexed work on nearly diametral chords of ellipses, polygons and Reuleaux bodies concerns different objects and sampling laws. None of these statements of prior work logically implies the explicit trochoid crossover: the new proof relies on cancellation of both endpoint linear deficits at the cycloidal tracer-radius threshold. The comparison is best-knowledge only; a pertinent locked historical chapter is not certified as non-covering.

## Limitations

The theorem covers one phase period, independent **phase-uniform** sampling, and fixed \(\beta>0\) or fixed \(\lambda\) in the joint window. It does not apply unchanged to arclength-uniform sampling, to multiple periods, or to arbitrary rolling-track curves. The total-variation assertion concerns the rescaled endpoint-mark law at fixed \(\lambda\), not a uniform-in-\(\lambda\) limit. Numerical tests supplement but do not replace the analytic proof. Historical priority and independent mathematical audit are not certified.

## References

1. E. H. Lockwood, *A Book of Curves*, Cambridge University Press, first printed 1961, Chapter 9 and Chapter 17. https://doi.org/10.1017/CBO9780511569340.012 ; publisher first-publication entry https://www.cambridge.org/core/books/book-of-curves/F08B52C8FB0563B2F9866DA186FC87F1
2. I. N. Bronshtein, K. A. Semendyayev, G. Musiol and H. Mühlig, *Handbook of Mathematics*, 2015 English edition, Section 2.13.2 (trochoids). https://djvu.online/file/GdI2fptBUdLpJ
3. E. W. Weisstein, “Prolate Cycloid”, MathWorld. https://mathworld.wolfram.com/ProlateCycloid.html
4. V. Dobrushkin, “Cycloids”, Brown University mathematics tutorial (trochoid parametrization). https://www.cfm.brown.edu/people/dobrush/am33/Mathematica/ch1/cycloid.html
5. F. Tong, M. Ahmadi and J. Pan, “Random Distances Associated with Arbitrary Triangles”, initial public preprint 29 November 2013, https://arxiv.org/abs/1312.2498 .
