# The sharp axial convexity window for pedal curves of ellipses

## Finding

**Theorem.** Fix \(a>b>0\) and the noncircular ellipse
\[
E_{a,b}=\{(X,Y):X^2/a^2+Y^2/b^2=1\}.
\]
For an arbitrary point \(M=(d,0)\), \(-a<d<a\), let \(P_d\) be its *pedal curve*: the locus of feet of the perpendiculars from \(M\) to the tangent lines of \(E_{a,b}\). Set
\[
d_+=a-\frac{b^2}{2a},\qquad
 d_-=\begin{cases}
 0,&a\le\sqrt2\,b,\\[3pt]
 a\sqrt{\dfrac{a^2-2b^2}{a^2-b^2}},&a>\sqrt2\,b.
 \end{cases}
\]
Then \(P_d\) is a simple regular real-analytic closed curve, and its enclosed region is convex **if and only if**
\[
\boxed{d_-\le |d|\le d_+.}
\]
At the upper endpoint \(|d|=d_+\), and at the lower endpoint when \(a\ge\sqrt2 b\), curvature is nonnegative with isolated zeros; for \(a<\sqrt2 b\), the center-pedal at the lower endpoint has positive curvature everywhere. In all endpoint cases the set is still strictly convex (no straight boundary segment). At strictly interior levels \(d_-<|d|<d_+\), curvature is everywhere positive. Outside the closed window the curvature is negative somewhere and the region is nonconvex.

If \(a>\sqrt2 b\), the center-pedal is nonconvex, the pedal becomes convex after \(|d|\) reaches \(d_-\), and loses convexity again beyond \(d_+\): a **reentrant convexity interval**. In every noncircular ellipse the focus positions \(|d|=\sqrt{a^2-b^2}\) lie strictly between the applicable thresholds; their pedals are the classical circles. In the thin-ellipse limit, with \(b/a\to0\),
\[
\boxed{d_+-d_-=\frac{5b^4}{8a^3}+O\!\left(\frac{b^6}{a^5}\right).}
\]
This identifies a narrow interval of convex pedals around each focus even when the center pedal is markedly indented.

## Assumptions and scope

All statements concern a **noncircular ellipse**, real semiaxes \(a>b>0\), and an **interior** pedal point constrained to its *major axis* (\(|d|<a\)). Convex means that the compact region bounded by the pedal curve is convex, not necessarily strictly positive pointwise curvature. The polar parameter below is the outward **normal angle** of the generating ellipse, not the usual eccentric-anomaly parameter.

## Proof

For \(u_\theta=(\cos\theta,\sin\theta)\), the support function of the ellipse is
\[
q(\theta)=\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}.
\]
Its tangent at normal \(u_\theta\) is \(X\cdot u_\theta=q(\theta)\). The orthogonal projection of \(M=(d,0)\) onto this line equals
\[
\gamma_d(\theta)=M+p(\theta)u_\theta,\qquad
p(\theta)=q(\theta)-d\cos\theta.
\]
The strict inequality \(p(\theta)>0\) follows because \(|d|<a\) places \(M\) strictly inside the ellipse. Consequently \(\gamma_d\) is a simple star-shaped regular real-analytic polar curve, with \(|\gamma_d'(\theta)|^2=p^2+(p')^2>0\).

The signed curvature numerator (for the counterclockwise polar parametrization) is
\[
N(\theta)=\det(\gamma_d'(\theta),\gamma_d''(\theta))
 =p^2+2(p')^2-pp''.
\]
The curve bounds a convex region exactly when \(N(\theta)\ge0\) for all \(\theta\): the tangent-angle derivative is \(N/(p^2+(p')^2)\), and the simple positively oriented star-shaped boundary makes one full turn. If \(N\ge0\), analyticity and nonidentity of \(N\) ensure isolated zeros and no straight segment.

Reflection in the major axis permits \(d\ge0\). Put
\[
 e=1-\frac{b^2}{a^2}\in(0,1),\qquad z=\frac da\in[0,1),\qquad x=\frac{a\cos\theta}{q(\theta)}\in[-1,1].
\]
A direct differentiation and cancellation gives the exact **global** curvature identity
\[
\frac{N(\theta)}{a^2}=1-2e+2z^2+3e x^2-zx(3+ex^2).\tag{1}
\]
For \(d\ge0\), the expression at \(-x\) is at least that at \(x\ge0\), so all curvature signs reduce to the minimum over \(x\in[0,1]\) of
\[
F_{e,z}(x)=1-2e+2z^2+3ex^2-zx(3+ex^2).\tag{2}
\]
The variable \(x\) sweeps the entire interval \([0,1]\) on the positive-normal semicircle. Differentiate:
\[
F'_{e,z}(x)=3\bigl[2ex-z(1+ex^2)\bigr].\tag{3}
\]
The ratio \(2ex/(1+ex^2)\) increases strictly on \([0,1]\) because \(e<1\). Therefore, if \(0<z<2e/(1+e)\), the unique minimum is attained at the unique interior point \(x\in(0,1)\) satisfying
\[
z=\frac{2ex}{1+ex^2};\tag{4}
\]
if \(z\ge2e/(1+e)\), the minimum lies at \(x=1\). For \(z=0\), the minimum is at \(x=0\), and the same stationary evaluation holds by continuity.

Substituting (4) in (2) factors the interior minimum as
\[
F_{e,z}(x)=\frac{(ex^2-1)^2(ex^2-2e+1)}{(1+ex^2)^2}.\tag{5}
\]
Since \(ex^2<1\), its sign is the sign of \(ex^2-2e+1\). If \(e\le1/2\), this is nonnegative for every \(x\in[0,1]\). If \(e>1/2\), it first becomes nonnegative at
\[
x_-=\sqrt{\frac{2e-1}{e}},\qquad
z_- = \frac{2ex_-}{1+ex_-^2}=x_-.
\]
Returning to \(a,b\) yields \(d_-=a z_-\) from the theorem. Because the stationary \(x\) increases strictly with \(z\), all interior minima are nonnegative exactly when \(z\ge z_-\), or automatically when \(e\le1/2\).

At the boundary minimizer \(x=1\), the expression factors as
\[
F_{e,z}(1)=(1-z)(1+e-2z).\tag{6}
\]
As \(z<1\), the boundary minimum is nonnegative precisely if \(z\le (1+e)/2\). Moreover
\[
\frac{1+e}{2}-\frac{2e}{1+e}
 =\frac{(1-e)^2}{2(1+e)}>0,
\]
so this upper threshold falls in the boundary-minimizer regime. This proves the complete closed interval \(z_-\le z\le z_+=(1+e)/2\) and hence \(d_+=a-b^2/(2a)\), including all equality cases.

The curvature zeros are isolated: the curve is real-analytic and (1) cannot vanish identically because the polynomial in \(x\) is not identically zero. At the lower threshold when \(e>1/2\), there are two zero-curvature normal angles satisfying \(\cos^2\theta=(2e-1)/(2e)\) on the side toward \(M\); at the upper threshold there is one at \(\theta=0\) (and its reflected equivalent for \(d<0\)). At \(e=1/2,z=0\), two zeros occur at the minor-axis normals.

For the focus position \(z_f=\sqrt e\),
\[
 z_f<\frac{1+e}{2},\qquad z_f>\sqrt{\frac{2e-1}{e}}\quad(e>1/2),
\]
because both strict comparisons reduce to \((1-\sqrt e)^2>0\) and \((1-e)^2>0\), respectively. The focus pedal is in fact a circle, consistent with its strict curvature positivity. Finally, let \(\tau=b^2/a^2\downarrow0\). Then
\[
\frac{d_+-d_-}{a}
 =1-\frac\tau2-\sqrt{\frac{1-2\tau}{1-\tau}}
 =\frac58\tau^2+O(\tau^3),
\]
which proves the width asymptotic.

## Verification

The standalone `check.py` uses symbolic differentiation to verify (1), checks the factorization (5) identically, compares the stated interval against a dense curvature-minimum sample at 300 reproducible parameter configurations, and verifies the \(5/8\) coefficient symbolically. Running `python check.py` produces four `_OK` lines. The symbolic identities support the calculation, while the proof of the **all-parameter** conclusion comes from monotonicity and factorization above, not from finite sampling.

## Relationship to prior work

Booth's classical oval is the **center-pedal** of an ellipse; its convexity threshold corresponds to the special case \(d=0\) of this theorem. The fact that the **focus-pedal** is a circle is also classical. Gibbons discusses the focus case in the orbital-hodograph setting. Izumiya and Takeuchi study pedal geometry of quadratic curves, particularly singularities and inverse constructions. Reznik, Garcia and Stachel investigate area-invariant ellipse pedal-like curves. Dana-Picard studies algebraic degrees and singularities of conic pedals. These established results do not by themselves determine whether every intermediate major-axis pedal is convex, nor the two sharp endpoints and their thin-ellipse separation. The 1879 papers of Ameseder are a historical priority risk because only catalog/bibliographic entries, not their full text, could be inspected here.

## Limitations

No off-major-axis characterization is asserted. The region may be convex with zero curvature at a threshold, so 'convex' must not be substituted by 'everywhere positive curvature.' The original oval is assumed noncircular and the pedal point strictly interior; the circle limit has the classical threshold \(|d|\le a/2\) but is not included in the quantified theorem. The identified priority gap is provisional: unexamined historical works may contain equivalent statements. Independent mathematical audit has not been performed.

## References

- J. Booth, *A Treatise on Some New Geometrical Methods*, Vol. II (1877), pp. 163–165, catalogued at https://mathworld.wolfram.com/BoothOval.html .
- G. W. Gibbons, *The fate of Hamilton's Hodograph in Special and General Relativity*, original public preprint September 3, 2015, https://arxiv.org/abs/1509.01286 .
- S. Izumiya and N. Takeuchi, *Pedals and inversions of quadratic curves*, https://arxiv.org/abs/1912.03114 .
- D. Reznik, R. Garcia and H. Stachel, *Area-Invariant Pedal-Like Curves Derived from the Ellipse*, https://arxiv.org/abs/2009.02581 .
- T. Dana-Picard, *Pedal curves of conics: an automated exploration of some cubics, sextics, octics and more*, https://arxiv.org/abs/2503.15135 .
- A. Ameseder, *Ueber Fusspunktcurven der Kegelschnitte* and *Zur Theorie der Fusspunktencurven der Kegelschnitte*, Archiv Math. u. Phys. 64 (1879), bibliographic listings at https://mathworld.wolfram.com/EllipsePedalCurve.html .
