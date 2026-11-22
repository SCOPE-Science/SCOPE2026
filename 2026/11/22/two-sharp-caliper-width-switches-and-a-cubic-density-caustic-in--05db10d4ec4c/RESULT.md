# Two sharp caliper-width switches and a cubic density caustic in parabolic segments

## Finding
For each \(a>0\), the Euclidean parabolic segment
\[
K_a=\{(x,y)\in\mathbb R^2:-a\le x\le a,\ x^2\le y\le a^2\}
\]
has an exact directional-width law and three ordered aspect-ratio thresholds. The segment has half-chord \(a\), rise \(a^2\), and after a similarity its rise-to-half-chord ratio is exactly \(a\). For a Haar-uniform unoriented unit normal, write its caliper width as \(W_a\). Let
\[
P_a(t)=t^3+(2-4a^2)t+4a,
\qquad b_a=\arctan(2a).
\]
For \(0\le\theta\le\pi/2\), put \(t=\tan\theta\) and
\[
w_a(t)=\begin{cases}
\dfrac{at+a^2+t^2/4}{\sqrt{1+t^2}},&0\le t\le2a,\\[4pt]
\dfrac{2at}{\sqrt{1+t^2}},&t\ge2a.
\end{cases}
\]
The law of \(W_a\) is the pushforward of \((2/\pi)d\theta\) on \([0,\pi/2]\) by \(w_a(\tan\theta)\). In particular,
\[
F_a(v)=\frac2\pi\int_0^\infty\frac{\mathbf1_{\{w_a(t)\le v\}}}{1+t^2}\,dt.
\]
This is an *exact algebraic-arctangent algorithm* for the complete CDF: split at \(t=2a\); on the first branch determine the sign intervals from the real nonnegative roots of
\[
(at+a^2+t^2/4)^2-v^2(1+t^2)=0,
\]
and on the upper branch use its strictly increasing inverse \(t=v/\sqrt{4a^2-v^2}\), wherever \(0<v<2a\). The integral of every sign interval is an arctangent difference.

Two distinct *global* transitions occur:
\[
a_M=\sqrt{\frac{11+5\sqrt5}{8}}=1.66509533839278\ldots,
\]
and \(a_m=\sqrt{s_m}=1.92532470080679\ldots\), where \(s_m\) is the unique positive root of
\[
16s^3-56s^2-12s-1=0.
\]
When \(a>\sqrt2\), let \(0<t_-(a)<t_+(a)<2a\) be the positive roots of \(P_a\). Then the *global maximum* is \(2a\) for \(a\le a_M\) and \(w_a(t_-)\) for \(a\ge a_M\); the *global minimum* is \(a^2\) for \(a\le a_m\) and \(w_a(t_+)\) for \(a\ge a_m\). At the equality cases the two listed direction families coexist. For \(a\le\sqrt2\) no strict interior stationary directions exist; at \(a=\sqrt2\) they merge into one horizontal-inflection level.

At the birth aspect ratio \(a=\sqrt2\), put \(w_*=3\sqrt3/2\) and \(c=3\sqrt6/4\). Then
\[
\Pr(|W_{\sqrt2}-w_*|\le\varepsilon)
\sim\frac4\pi c^{-1/3}\varepsilon^{1/3},
\qquad\varepsilon\downarrow0.
\]
On either side of \(w_*\) the density satisfies
\[
f_{\sqrt2}(v)\sim\frac{2}{3\pi}c^{-1/3}|v-w_*|^{-2/3}.
\]
The emerging pair of stationary-width values has the sharp splitting law
\[
w_{\sqrt2+\delta}(t_-)-w_{\sqrt2+\delta}(t_+)
\sim \frac{4\,2^{3/4}}{3\sqrt3}\,\delta^{3/2},
\qquad\delta\downarrow0^+.
\]
These are interior distribution singularities, not endpoint large-deviation tails.

## Assumptions and scope
All widths use ordinary Euclidean distances between parallel supporting *lines*. Directions are uniform modulo antipodes, with no orientation-dependent reweighting. The body is the full closed convex parabolic segment, including its chord. The parameter \(a\) measures Euclidean shape up to similarity; all assertions are quantified for every \(a>0\). The asymptotics apply to the specified limits, not uniformly to unrelated double limits.

## Proof
**Support calculation.** For a unit normal with nonnegative coordinates \((u_x,u_y)\), \(u_x^2+u_y^2=1\), the positive support equals \(a u_x+a^2u_y\), since the upper chord is at \(y=a^2\). The opposite support maximizes \(-u_xs-u_ys^2\) over \(-a\le s\le a\) on the lower parabola. The quadratic vertex is admissible precisely when \(u_x\le2a u_y\). If admissible its value is \(u_x^2/(4u_y)\); otherwise the maximizing endpoint yields \(a u_x-a^2u_y\). Sum these values, substitute \(t=u_x/u_y=\tan\theta\), and obtain the displayed two branches; the formulas join continuously at \(t=2a\). Reflection across the vertical axis and \(w(u)=w(-u)\) give the factor \(2/\pi\) for a uniform acute normal angle. The CDF formula follows, and the quartic root recipe is exhaustive because each sign interval is bounded by a root or branch endpoint.

**Stationary directions.** The upper branch \(2at/\sqrt{1+t^2}\) increases strictly with \(t\). On \(0<t<2a\), direct differentiation gives
\[
\frac{dw_a}{dt}=\frac{P_a(t)}{4(1+t^2)^{3/2}}.
\]
For \(a\le1/\sqrt2\) the polynomial is increasing on \([0,\infty)\). For larger \(a\), its positive stationary minimum occurs at \(t_0=\sqrt{(4a^2-2)/3}\). The sign of this minimum changes precisely when
\[
(4a^2-2)^3=108a^2.
\]
Writing \(s=4a^2\), the difference factors as \((s-8)(s+1)^2\); hence the only positive threshold is \(a=\sqrt2\). At equality
\[
P_{\sqrt2}(t)=(t-\sqrt2)^2(t+2\sqrt2).
\]
For \(a>\sqrt2\), \(P_a(0)>0\), its positive minimum is negative, and \(P_a(2a)=8a>0\); thus exactly two roots satisfy \(0<t_-<t_+<2a\). The first is a strict local maximum of width and the second a strict local minimum. The only remaining global candidates are \(w_a(0)=a^2\) and \(\lim_{t\to\infty}w_a(t)=2a\). As \(w_a(t_-)>a^2\) and \(w_a(t_+)<w_a(2a)<2a\), the maximum compares \(w_a(t_-)\) with \(2a\) and the minimum compares \(w_a(t_+)\) with \(a^2\).

**Uniqueness of both global switches.** At either stationary root the envelope theorem applies. For \(t<2a\),
\[
\frac{w_a(t)}a=\frac{t+a+t^2/(4a)}{\sqrt{1+t^2}},
\qquad
\partial_a\frac{w_a(t)}a=\frac{1-t^2/(4a^2)}{\sqrt{1+t^2}}>0.
\]
Consequently \(w_a(t_-)/a\) grows strictly from \(3\sqrt3/(2\sqrt2)<2\) at the fold to infinity as \(a\to\infty\); it equals the horizontal comparator \(2\) once. Similarly,
\[
\frac{w_a(t)}{a^2}=\frac{(1+t/(2a))^2}{\sqrt{1+t^2}},
\qquad
\partial_a\frac{w_a(t)}{a^2}
=-\frac{t(1+t/(2a))}{a^2\sqrt{1+t^2}}<0,
\]
so \(w_a(t_+)/a^2\) falls strictly from \(3\sqrt3/4>1\) to zero, and equals the vertical comparator \(1\) once. Eliminating the stationary root between \(P_a(t)=0\) and \(w_a(t)=2a\) produces the nontrivial factor \(16a^4-44a^2-1\). Eliminating it between \(P_a(t)=0\) and \(w_a(t)=a^2\) produces \(16a^6-56a^4-12a^2-1\). Extraneous resultant factors are powers of \(a\) and \(4a^2+1\), which are nonzero for \(a>0\). Existence and uniqueness proved above select the displayed positive roots. The strict order \(\sqrt2<a_M<a_m\) follows either from the polynomial brackets or from the exact expressions.

**Interior cubic caustic.** At \(a=\sqrt2\), \(t_*=\sqrt2\) and \(\theta_*=\arctan\sqrt2\) are interior to the first width branch. Direct differentiation gives \(w_*=3\sqrt3/2\), zero first and second \(t\)-derivatives, and \(d^3w/dt^3=\sqrt6/6\) at \(t_*\). Since \(dt/d\theta=1+t_*^2=3\),
\[
w_{\sqrt2}(\tan\theta)-w_*=
\frac{3\sqrt6}{4}(\theta-\theta_*)^3+O((\theta-\theta_*)^4).
\]
The acute normal angle has density \(2/\pi\), and the width is strictly increasing except for this isolated stationary angle, so the interval \([w_*-\varepsilon,w_*+\varepsilon]\) corresponds to an angular interval of length \(2(\varepsilon/c)^{1/3}(1+o(1))\). Multiplying by \(2/\pi\) proves the mass coefficient. Differentiating the local inverse on either side gives the density coefficient. No smooth preimage can change the leading singularity.

**Fold unfolding.** Put \(a=\sqrt2+\delta\), \(t=\sqrt2+\eta\). The stationary polynomial expands as
\[
P_a(t)=3\sqrt2\,\eta^2-12\delta+O(|\eta|^3+|\eta|\delta+\delta^2).
\]
Thus \(t_\pm=\sqrt2\pm2^{3/4}\sqrt\delta+O(\delta)\). Integrate \(-dw_a/dt\) between these roots using \(4(1+t^2)^{3/2}=12\sqrt3+o(1)\). This yields
\[
w_a(t_-)-w_a(t_+)
=\frac{4\,2^{3/4}}{3\sqrt3}\delta^{3/2}+o(\delta^{3/2}).
\]
All remainder estimates are uniform on the shrinking root interval by analyticity near the fold.

## Verification
The accompanying `parabolic_segment_width_check.py` independently maximizes linear functionals over the chord and parabola, checks polynomial/resultant identities in exact symbolic arithmetic, and compares global extrema, Cauchy's mean-width consistency, the critical mass law and the splitting constant. The reproduced execution passed 50,331 numerical checks and its symbolic assertions. These finite diagnostics are not substitutes for the parameter-uniform derivative and monotonicity proof. Cauchy's formula independently gives the non-claimed classical mean-width check
\[
\mathbb E W_a=\frac{2a+a\sqrt{1+4a^2}+\tfrac12\operatorname{arsinh}(2a)}\pi.
\]

## Relationship to prior work
Classical parabolic-segment geometry includes exact area, arc length, centroid and optimal inscribed-triangle facts; these do not give a distribution of directional widths. The direct comparison with Finch's 2011 width-distribution paper finds explicit examples for triangles, squares, tetrahedra and cubes, not the curved parabolic segment or an aspect-parameter cubic stationary merger. The elementary planar Cauchy formula determines only the mean, not the cubic caustic, the two global switch ratios or the complete root-based distribution. Broader three-dimensional polytope width-density frameworks operate on a different class of bodies and do not explicitly imply the listed curved-boundary equalities. This literature comparison supports originality provisionally; it does not establish definitive historical priority.

## Limitations
The exact distribution is an algebraic-root/arctangent prescription rather than a single elementary expression on all parameter strata. The singularity is for the stated unoriented uniform direction model; it does not assert a universal exponent for unrelated shapes. The fold-splitting law concerns \(a\downarrow\sqrt2\) from above. Primary-source coverage is incomplete for one older journal article available only by abstract and one later general width study available only by abstract; this uncertainty remains relevant to historical priority. No independent mathematical validation has been performed.

## References
1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, initial public arXiv posting 2011-10-04, https://arxiv.org/abs/1110.0671.
2. E. W. Weisstein, *Parabolic Segment*, Wolfram MathWorld, https://mathworld.wolfram.com/ParabolicSegment.html (page inspected; publication day not asserted).
3. M. H. Thibodeaux, *Arc Lengths and Curvature of Parabolic Segments*, *Journal of the Pipeline Division* **90** (January 1964), https://doi.org/10.1061/JPLEAZ.0000062 (abstract inspected; full text inaccessible).
4. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, https://arxiv.org/abs/2609.26202 (abstract inspected; three-dimensional polyhedral framework).
