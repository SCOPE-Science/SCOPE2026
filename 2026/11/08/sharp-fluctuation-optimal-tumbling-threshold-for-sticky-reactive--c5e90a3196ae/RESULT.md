# Sharp fluctuation-optimal tumbling threshold for sticky reactive run-and-tumble walls

## Finding

Consider a one-dimensional run-and-tumble particle on a closed interval with length \(L>0\), speed \(v>0\), independent rate-\(\alpha\) direction reversals in the interior, and identical sticky reactive walls. At either wall an outward-moving particle sticks and undergoes competing exponential events: release in the inward direction at rate \(\gamma>0\) or permanent absorption at rate \(\kappa>0\). The particle starts at the midpoint with either direction chosen with probability \(1/2\). Let \(T\) be its time to permanent absorption.

Put \(h=L/(2v)\), \(a=\alpha h\ge0\), \(k=\kappa h>0\), and \(g=\gamma h>0\). Write \(F(a;k,g)=\operatorname{Var}(T)/(\mathbb E T)^2\) for squared coefficient of variation. Define
\[
 B=1+k+2g,\quad C=1+\frac{k+2g}{3},\quad E=1+\frac{k}{2},
 \quad Q=CB-2kE
 =\frac{4g^2+4gk+8g-2k^2-2k+3}{3}.
\]
Then for every \(a\ge0\),
\[
\boxed{
 F(a;k,g)=1-
 \frac{2k\left(\frac{k a^2}{6}+Ca+E\right)}{(B+ka)^2},
 \qquad
 \mathbb E[T]/h=a+\frac{B}{k}.
}
\]
There is an exact, exhaustive optimality classification.

**If \(Q>0\)**, \(F\) has exactly one global minimizer on \(a\ge0\), attained at the strictly positive tumbling rate
\[
\boxed{
 a_*=\frac{3Q}{2k}
 =\frac{4g^2+4gk+8g-2k^2-2k+3}{2k},\qquad
 F(a_*;k,g)=\frac23-\frac{2}{3(B+ka_*)}.
}
\]
The function is strictly decreasing before \(a_*\) and strictly increasing after it. **If \(Q\le0\)**, \(F\) is strictly increasing on \(a>0\) and is minimized at \(a=0\). Equivalently the interior optimum exists exactly when
\[
 g>\frac{\sqrt{3k^2+6k+1}-k-2}{2}.
\]
In particular, for \(0<k\le(\sqrt7-1)/2\), all positive wall-release rates \(g\) have an interior optimum. In both cases \(F(a;k,g)\to2/3\) as \(a\to\infty\), from below.

The mean absorption time is strictly increasing in \(a\); hence whenever \(Q>0\), the strictly positive rate that minimizes *relative timing fluctuations* is necessarily slower in mean than the ballistic limit \(a=0\). For \(k=g=1\), the exact optimum is \(a_*=15/2\), with \(\mathbb E[T]/h=23/2\), \(\operatorname{Var}(T)/h^2=161/2\), and \(F(a_*)=14/23\).

## Assumptions and scope

All rates are finite. Bulk direction reversals occur at *rate \(\alpha\) per oriented state*: the forward flux-relaxation rate is \(2\alpha\). At the wall, release and killing are independent exponential clocks with rates \(\gamma,\kappa\), and a released particle points into the interval. These are not instantaneous reflecting walls and not a model in which the wall-release rate is forced to equal the bulk reversal rate. The two walls have identical kinetic parameters; the initial position is the midpoint and the initial direction is unbiased. The theorem includes \(a=0\) by continuous extension, with positive wall-release and absorption rates. It does not address unequal wall rates, nonlinear paths, finite wall residence memories, or a noncentral start.

Because the system is a compact-state piecewise-deterministic Markov process and a uniformly positive probability of wall absorption exists within a bounded number of travel/release/reversal attempts, its absorption time has exponential tails at each fixed finite parameter choice. Thus all moments below are finite.

## Proof

Measure time in units \(h\), position in units \(vh=L/2\), and write the centered interval as \([-1,1]\) with speed one. For \(s\ge0\), let \(u_\pm(x;s)=\mathbb E_{x,\pm}[e^{-sT/h}]\). In the open interval the backward equations are
\[
 \pm \partial_x u_\pm+a(u_\mp-u_\pm)=s u_\pm.
\]
At \(x=1\) the outward state is equivalent to the wall-bound state, so the competing exponential clocks give
\[
 (k+g+s)u_+(1;s)=k+g u_-(1;s).
\]
The opposite wall satisfies the reflected relation. Put \(H=(u_++u_-)/2\), \(G=(u_+-u_-)/2\). Then
\[
 G'=sH,\qquad H'=(s+2a)G,\qquad G(0;s)=0.
\]
Writing \(z^2=s(s+2a)\) and using reflection symmetry, \(H(x;s)=H(0;s)\cosh(zx)\), \(G(x;s)=H(0;s)(s/z)\sinh(zx)\), with analytic continuation at \(z=0\). The wall equation reduces to
\[
 (k+s)H(1;s)+(k+2g+s)G(1;s)=k.
\]
Consequently the exact midpoint absorption-time Laplace transform is
\[
 \boxed{
 \mathcal L(s)=\frac{k}{
 (k+s)\cosh z+
 (k+2g+s)\frac{s}{z}\sinh z
 },\quad z^2=s(s+2a).
 }
\]

Expansion at \(s=0\) gives
\[
 \cosh z=1+as+\left(\frac12+\frac{a^2}{6}\right)s^2+O(s^3),
 \qquad
 \frac{s}{z}\sinh z=s+\frac{a}{3}s^2+O(s^3).
\]
The transform denominator therefore equals \(k+A_1s+A_2s^2+O(s^3)\), where
\[
 A_1=B+ka,\qquad
 A_2=\frac{ka^2}{6}+Ca+E.
\]
Using \(\mathcal L(s)=1-s\,\mathbb E[T/h]+s^2\,\mathbb E[(T/h)^2]/2+O(s^3)\) yields
\[
 \mathbb E[T/h]=A_1/k,\quad
 \mathbb E[(T/h)^2]=2(A_1^2/k^2-A_2/k).
\]
Subtracting the mean square proves the displayed \(F\)-formula.

For completeness, independent backward-moment equations reproduce the second moment. Let \(M_j(x)=(m_j^+(x)+m_j^-(x))/2\) and \(G_j(x)=(m_j^+(x)-m_j^-(x))/2\) for the dimensionless \(j\)-th hitting-time moment. They give
\[
 M_1(x)=m-ax^2,\quad G_1(x)=-x,\quad m=a+B/k,
\]
and
\[
 M_2(x)=m_2+(1-2am)x^2+\frac{a^2x^4}{3},
 \qquad
 G_2(x)=-2mx+\frac{2ax^3}{3}.
\]
At the right wall, \(m_1^{\rm wall}=m-a-1=(2g+1)/k\), and
\[
 (k+g)(M_2(1)+G_2(1))
 =2m_1^{\rm wall}+g(M_2(1)-G_2(1)).
\]
Solving for \(m_2=M_2(0)\) gives the same expression as the transform expansion.

Finally, quotient differentiation gives the exact sign formula
\[
 \boxed{
 \frac{\partial F}{\partial a}
 =-\frac{2k}{(B+ka)^3}\left(Q-\frac{2ka}{3}\right).
 }
\]
All denominators are strictly positive. Thus the sign changes once from negative to positive exactly if \(Q>0\), at \(a_*=3Q/(2k)\); otherwise it is strictly positive for every \(a>0\). Simplification at the stationary point yields \(F(a_*)=2/3-2/[3(B+ka_*)]\). Solving the quadratic inequality \(Q>0\) for \(g>0\) gives the stated wall-release threshold. Taking the ratio of leading quadratic coefficients in \(F\) shows the limit \(2/3\). This proves all sign, uniqueness, boundary, and mean-versus-dispersion assertions.

## Verification

Run `python checker.py` using the standalone standard-library checker bundled with this result. It compares the Laplace-expansion second moment to the independently derived backward-generator boundary moment using exact rational arithmetic, checks the derivative polynomial and phase classification, and tests the exact example. The verified run passed 294 exact-rational moment and slope comparisons. Separate high-precision numerical difference tests of the full hyperbolic transform gave absolute second-moment errors below \(2\times10^{-9}\) for three distinct parameter choices. Numerical checks support but do not replace the global analytical argument.

## Relationship to prior work

Bressloff (2023) formulates the same sticky-reactive wall process and derives a Laplace-space solution and the mean absorption time; Angelani (2017, publicly available manuscript posted on arXiv in 2022) and Angelani (2023) give overlapping forward/Laplace first-passage frameworks. Their published transform formulas **already determine the pointwise absorption-time law** and hence the moments by differentiation; the formula for the mean is not new. The present assertion is the *global two-parameter phase classification of the rate minimizing the relative absorption-time variance*, with the sharp wall-release threshold, exactly one interior minimum when it exists, and a mean/relative-dispersion tradeoff. These conclusions were not located as stated theorems in the inspected primary texts.

The earlier exact Laplace transforms are a significant implicit-coverage risk; absence of a verbal claim is not a proof of priority. See the separate review for the distinction and search limitations.

## Limitations

The variance-optimality criterion is coefficient of variation squared, not absolute variance or expected absorption time. The result does not optimize the speed or the wall kinetics jointly, extend to spatially asymmetric walls, or establish empirical optimality for bacteria. It is a self-review, not independently audited scientific validation.

## References

- P. C. Bressloff, *Encounter-based model of a run-and-tumble particle II: absorption at sticky boundaries*, arXiv:2302.01158v1, publicly posted 2023-02-02. https://arxiv.org/abs/2302.01158
- L. Angelani, *Confined run-and-tumble swimmers in one dimension*, J. Phys. A 50 (2017) 325601, DOI 10.1088/1751-8121/aa734c; public arXiv manuscript 2206.03123 (2022-06-07). https://arxiv.org/abs/2206.03123
- L. Angelani, *One-dimensional run-and-tumble motions with generic boundary conditions*, J. Phys. A 56 (2023) 455003, DOI 10.1088/1751-8121/ad009e. https://doi.org/10.1088/1751-8121/ad009e
- L. Angelani, *Optimal escapes in active matter*, Eur. Phys. J. E 47 (2024), article 9. https://doi.org/10.1140/epje/s10189-023-00402-7
