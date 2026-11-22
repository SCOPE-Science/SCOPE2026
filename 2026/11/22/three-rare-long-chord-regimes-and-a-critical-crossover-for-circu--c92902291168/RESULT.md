# Three rare-long-chord regimes and a critical crossover for circular segments

## Finding
For \(-1<h<1\), define the Euclidean circular segment
\[
K_h=\{(x,y):x^2+y^2\leq 1,\ y\geq h\},\qquad P_h=2\arccos h+2\sqrt{1-h^2}.
\]
Choose an **unoriented Euclidean-motion-invariant random line**, conditioned to intersect \(K_h\), and let \(L_h\) be the resulting intersection length. Its maximal possible length is
\[
D_h=\begin{cases}2,&-1<h\leq0,\\2\sqrt{1-h^2},&0<h<1.\end{cases}
\]
The following three fixed-shape long-chord tails have exact leading constants, as \(\varepsilon\downarrow0\):
\[
\Pr(L_h\geq D_h-\varepsilon)\sim
\begin{cases}
\dfrac{4\arcsin(-h)}{P_h}\sqrt\varepsilon,&-1<h<0,\\[4pt]
\dfrac{\varepsilon}{\pi+2},&h=0,\\[4pt]
\dfrac{\sqrt{1-h^2}}{4h^2P_h}\varepsilon^2,&0<h<1.
\end{cases}
\]
The singular transition has a complete local crossover: for every **fixed real** \(\lambda\), put \(h=\lambda\sqrt\varepsilon\). Then
\[
\lim_{\varepsilon\downarrow0}\frac{\pi+2}{\varepsilon}
\Pr\!\left(L_{\lambda\sqrt\varepsilon}\geq D_{\lambda\sqrt\varepsilon}-\varepsilon\right)=\Phi(\lambda),
\quad
\Phi(\lambda)=\begin{cases}
-4\lambda,&\lambda\leq-1,\\
(1-\lambda)^2,&-1\leq\lambda\leq0,\\
(\sqrt{1+\lambda^2}-\lambda)^2,&\lambda\geq0.
\end{cases}
\]
The cases \(\lambda=-1\) and \(\lambda=0\) agree from either side. An exact two-dimensional integral also determines the entire chord-length distribution for each shape.

## Assumptions and scope
Lines have invariant measure \(d\alpha\,dt\), where their (unoriented) direction \(\alpha\in[-\pi/2,\pi/2)\) is measured from the horizontal and \(t\) is signed perpendicular offset. The line is \((x,y)=t(-\sin\alpha,\cos\alpha)+s(\cos\alpha,\sin\alpha)\), with \(s\in\mathbb R\). This is **not** the distribution obtained by selecting two uniform boundary points, two uniform interior points, or an invariant random line without conditioning. Boundary-tangent lines have measure zero. The parameter \(h\) belongs to the *open* interval \((-1,1)\). Fixed-shape limits and the fixed-\(\lambda\) crossover are different statements; no uniformity over diverging \(\lambda\) is asserted.

## Proof
**1. Line geometry and normalization.** By reflection across the vertical axis it is enough to consider \(0<\alpha<\pi/2\). Put \(u(t)=\sqrt{1-t^2}\) for \(|t|\leq1\) and \(q_h(\alpha,t)=(h-t\cos\alpha)/\sin\alpha\). The unit disk intersects the parameterized line in \([-u,u]\), whereas the cap inequality requires \(s\geq q_h\). Hence the exact chord length, including empty and truncated chords, is
\[
\ell_h(\alpha,t)=\bigl[u(t)-\max\{-u(t),q_h(\alpha,t)\}\bigr]_+.
\]
At \(\alpha=0\) the length is \(2u(t)\) if \(t\ge h\), otherwise zero. The total line measure intersecting a convex planar body is its perimeter by Cauchy's projection formula, hence \(P_h\). Consequently, for every \(s>0\),
\[
\Pr(L_h\geq s)=\frac{2}{P_h}\int_0^{\pi/2}\int_{-1}^{1}
\mathbf1_{\{\ell_h(\alpha,t)\geq s\}}\,dt\,d\alpha.
\tag{1}
\]
This exact integral is also a reproducible full-distribution specification.

**2. Maximal chord classification.** The diameter of a compact convex body equals the maximum of its chord lengths. For \(h\le0\) the horizontal diameter \([-1,1]\times\{0\}\) survives. If \(h<0\), every unit-disk diameter whose endpoints both have height at least \(h\) survives, an angular family of length \(2\arcsin(-h)\) within the unoriented direction range. For \(h=0\) only the horizontal diameter remains. For \(h>0\), the unique diametral pair is the endpoints \((\pm\sqrt{1-h^2},h)\) of the horizontal base chord, of length \(2\sqrt{1-h^2}\). For two points in the cap with vertical coordinates \(y_1,y_2\ge h>0\), their squared separation is at most \((\sqrt{1-y_1^2}+\sqrt{1-y_2^2})^2+(y_1-y_2)^2=2-2y_1y_2+2\sqrt{(1-y_1^2)(1-y_2^2)}\le4(1-h^2)\), with equality only at the base endpoints. The last inequality follows by writing \(y_j=\cos\theta_j\), \(\theta_j\in[0,\arccos h]\): the squared separation is \(4\sin^2((\theta_1+\theta_2)/2)\), maximized when both angles attain \(\arccos h\).

**3. Fixed negative height.** For each interior direction in the surviving diameter family, a chord close to length \(2\) is a full disk chord with \(|t|\le\sqrt{\varepsilon-\varepsilon^2/4}=\sqrt\varepsilon(1+O(\varepsilon))\). Integrating this offset interval over the angular family of length \(2\arcsin(-h)\) and dividing by \(P_h\) gives \(4\arcsin(-h)\sqrt\varepsilon/P_h\). Outside the closed family, equality with diameter is impossible; boundary-angle neighborhoods have vanishing scaled contribution by bounded convergence (the offset band is globally \(O(\sqrt\varepsilon)\)).

**4. Fixed positive height.** Write \(r=\sqrt{1-h^2}\) and rescale \(\alpha=\varepsilon a\), \(t=h+\varepsilon b\), with \(a\ge0\). All near-diameter chords lie in this bounded scaling region: a length within \(\varepsilon\) of the unique longest horizontal segment forces the offset and angle to approach the base chord, and the disk chord deficit forces \(t-h=O(\varepsilon)\), while the straight-base endpoint constraint forces \(\alpha=O(\varepsilon)\). Here \(u(t)=r-\varepsilon hb/r+O(\varepsilon^2)\) and \(q_h(\alpha,t)=-b/a+O(\varepsilon)\) for \(a>0\). A **truncated** chord cannot be near-diametral unless \(b\ge ra+o(1)\), since otherwise its removed endpoint segment has a strictly positive limiting length \(r-b/a\). In the full-chord region, \(\ell_h=2r-2\varepsilon hb/r+o(\varepsilon)\). Thus the limiting feasible region in the half-plane \(a\ge0\) is \(0\le b\le r/(2h)\) and \(0\le a\le b/r\). Its doubled area equals \(2\int_0^{r/(2h)}b/r\,db=r/(4h^2)\). The area Jacobian is \(\varepsilon^2\); divide by \(P_h\) to obtain the third displayed coefficient. The tiny transition strip with \(b-ra=o(1)\) has vanishing rescaled area.

**5. Critical scaling.** For \(h=\lambda\sqrt\varepsilon\), use \(t=b\sqrt\varepsilon\), \(\alpha=a\sqrt\varepsilon\) with \(a\ge0\). The unit-disk chord deficiency is \(b^2\varepsilon+o(\varepsilon)\). At \(\lambda\le0\), the target is \(2-\varepsilon\); at \(\lambda>0\), it is \(2-\lambda^2\varepsilon-\varepsilon\). The cap inequality for an untruncated full chord becomes \(b-a\ge\lambda+o(1)\). Any cap truncation large enough to matter lowers the chord by order \(\sqrt\varepsilon\), so contributes zero in the limiting rescaled probability region except along its boundary. Thus the limiting admissible region for \(a\ge0\) is \(b\in[-B,B]\), \(0\le a\le b-\lambda\), with \(B=\sqrt{1+(\max\{\lambda,0\})^2}\). Its \((a,b)\)-area, doubled for negative \(\alpha\), is \(\Phi(\lambda)=2\int_{-B}^B(b-\lambda)_+\,db\). Evaluating this elementary integral yields the stated three pieces. Uniform boundedness of the rescaled near-extreme sets permits dominated convergence, while \(P_{\lambda\sqrt\varepsilon}\to\pi+2\).

## Verification
The exact line-intersection expression was evaluated independently against scaled quadrature for negative, zero and positive fixed heights, and for five fixed values of \(\lambda\) including both crossover junctions. Numerical agreement as \(\varepsilon\to0\) supports the analytical limits but is **not** used to replace an asymptotic proof. The standalone `CHECK.py` reproduces deterministic checks and reports its own totals. All directions and offsets are expressed in unit-radius coordinates; conversion back to disk radius \(R\) replaces \(\varepsilon\) by \(\varepsilon/R\).

## Relationship to prior work
Bäsel's 2014 study develops invariant-line chord distributions for regular polygons, not curved circular segments with a straight boundary and a moving diameter-type transition. Gille's 2005 hemisphere chord study is three-dimensional and uses a different body. Published smooth-body long-chord crossover results assume smooth perturbations or higher-dimensional strictly curved diameter neighborhoods, assumptions violated by the semicircle-to-cap corner geometry here. Classical general chord-distribution literature may contain related endpoint-density results; the present three-piece critical boundary-layer statement was not identified among accessible sources.

## Limitations
Only the fixed-height tails and fixed-\(\lambda\) crossover are addressed; there is no claimed uniform error bound for simultaneous parameters outside the square-root window. The exact integral determines the full distribution but is not evaluated in elementary functions. Historical priority has not been independently established. Truncated cap chords are excluded from the leading near-maximum boundary layer by the endpoint constraint, which is explicitly handled in the proof.

## References
- U. Bäsel, *Random chords and point distances in regular polygons*, Acta Mathematica Universitatis Comenianae 83 (2014), 1–18, https://www.iam.fmph.uniba.sk/amuc/ojs/index.php/amuc/article/view/71/18 (public May 14, 2014).
- W. Gille, *Chord Length Distributions of the Hemisphere*, Journal of Mathematics and Statistics 1 (2005), 24–28, https://doi.org/10.3844/jmssp.2005.24.28.
- R. Coleman, *Random paths through convex bodies*, Journal of Applied Probability 6 (1969), https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/random-paths-through-convex-bodies/0F6F86A3BF3C212EE803D38E0AE7E4DF.
- J. Gates, *Some properties of chord length distributions*, Journal of Applied Probability 24 (1987), https://doi.org/10.2307/3214211 (full text not accessible in this investigation).
