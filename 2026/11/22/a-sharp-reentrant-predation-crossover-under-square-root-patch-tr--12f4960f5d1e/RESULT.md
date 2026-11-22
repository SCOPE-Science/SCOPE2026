# A sharp reentrant predation crossover under square-root patch tracking

## Finding

Consider two equal-area prey patches with fixed mean prey density \(m>0\), local densities \(x_+=m+d\) and \(x_-=m-d\), and clumping contrast \(0\le d\le m\). Let the local dimensionless Holling-II intake of a forager be \(f(x)=x/(K+x)\) with half-saturation density \(K>0\). Assume mobile predators instantaneously occupy the two patches in proportions proportional to \(\sqrt{x_+}\) and \(\sqrt{x_-}\) (an imposed sublinear tracking law, not an equilibrium derived here). Their average per-predator intake is

\[
F(d)=\frac{\sqrt{m+d}\,f(m+d)+\sqrt{m-d}\,f(m-d)}{\sqrt{m+d}+\sqrt{m-d}}.
\]

**Theorem (complete sharp phase diagram).** For every \(m,K>0\), \(F\) is continuous on \([0,m]\). If \(m\le K\), it is strictly increasing on \([0,m]\). If \(m>K\), define

\[
t_*=\sqrt{2K(K+m)}-K,\qquad d_*=\sqrt{m^2-t_*^2},\qquad d_0=\sqrt{m^2-K^2}.
\]

Then \(0<d_*<d_0<m\). The function \(F\) decreases strictly on \([0,d_*]\) and increases strictly on \([d_*,m]\); it has the unique global minimum \(F(d_*)=1-K/(2t_*)\). Moreover,

\[
F(d)<F(0)\quad(0<d<d_0),\qquad F(d_0)=F(0),\qquad F(d)>F(0)\quad(d_0<d\le m).
\]

Thus moderately clumped prey can reduce a mobile predator's intake relative to evenly distributed prey, even though sufficiently extreme clumping increases it; the sole positive crossover is exact.

**Robustness beyond the square-root exponent.** For any \(0<\gamma<1\) replace \(\sqrt{x}\) by \(x^\gamma\) in the patch weights, producing \(F_\gamma(d)\). If \(m>\gamma K/(1-\gamma)\), then \(F_\gamma(d)<F_\gamma(0)\) for all sufficiently small positive \(d\), whereas \(F_\gamma(m)>F_\gamma(0)\). Consequently at least one interior minimum and one nonzero crossing exist. No uniqueness statement is asserted for general \(\gamma\ne1/2\).

## Assumptions and scope

The patches have equal area and fixed prey total \(2m\); local prey density changes only by moving biomass between them. A predator has the same saturating feeding curve in either patch, there is no predator interference or prey depletion during the instantaneous assay, and the total number of predators is fixed. The spatial allocation rule is an assumption about short-term redistribution; it differs from both random predator search and an allocation maximizing individual intake. The two patches do not represent two prey species. All assertions include both \(d=0\) and the completely concentrated boundary \(d=m\), interpreting \(0^\gamma=0\) for positive \(\gamma\). Rates are normalized by the maximal individual feeding rate and could be scaled by an arbitrary positive constant without changing the conclusions.

## Proof

Set \(a=\sqrt{m+d}\), \(b=\sqrt{m-d}\), and \(t=ab=\sqrt{m^2-d^2}\). Then \(a^2+b^2=2m\). Algebra using \(z^3/(K+z^2)=z-Kz/(K+z^2)\) yields

\[
\begin{aligned}
F(d)&=\frac{a^3/(K+a^2)+b^3/(K+b^2)}{a+b}\\
&=1-K\frac{a/(K+a^2)+b/(K+b^2)}{a+b}\\
&=1-K\frac{K+ab}{(K+a^2)(K+b^2)}\\
&=1-\frac{K(K+t)}{K^2+2Km+t^2}.
\end{aligned}
\]

Put \(C=K^2+2Km\). Differentiating with respect to \(t\) gives

\[
\frac{\partial F}{\partial t}=-\frac{K(C-2Kt-t^2)}{(C+t^2)^2}.
\]

The polynomial \(H(t)=C-2Kt-t^2\) is strictly decreasing for \(t\ge0\), with \(H(0)>0\) and \(H(m)=K^2-m^2\). As \(t=\sqrt{m^2-d^2}\) strictly decreases from \(m\) to zero when \(d\) rises, for \(m\le K\) the derivative of \(F\) with respect to \(d\) is strictly positive for interior \(d\) (at \(m=K,d=0\) its limiting derivative is zero). If \(m>K\), \(H\) has precisely one zero in \((0,m)\), namely \(t_*=-K+\sqrt{2K(K+m)}\), so \(F\) first decreases and then increases, with the stated unique minimizer. The root equation \(C+t_*^2=2t_*(K+t_*)\) gives \(F(d_*)=1-K/(2t_*)\).

The exact uniform-comparison identity is

\[
F(d)-F(0)=\frac{K(m-t)(K-t)}{(K+m)(K^2+2Km+t^2)},\qquad F(0)=\frac{m}{K+m}.
\]

Because \(m-t>0\) for every \(d>0\), the sign is exactly the sign of \(K-t\). If \(m>K\), the sole nonzero equality is \(t=K\), equivalent to \(d=d_0\). The inequalities \(0<d_*<d_0<m\) follow from \(K<t_*<m\), which holds strictly when \(m>K\). This also proves the endpoint cases: \(F(m)=2m/(K+2m)>F(0)\).

For the general exponent assertion, define \(x_\pm=m\pm d\), \(w_\pm=x_\pm^\gamma\), and \(F_\gamma=(w_+f(x_+)+w_-f(x_-))/(w_++w_-)\). Ordinary Taylor expansion at \(d=0\), valid for every positive \(m,K\), gives

\[
F_\gamma(d)-F_\gamma(0)=\frac{K\,[\gamma K-(1-\gamma)m]}{m(K+m)^3}d^2+O(d^4).
\]

The coefficient is negative under the stated strict inequality. At \(d=m\) the empty patch has zero weight, so \(F_\gamma(m)=f(2m)>f(m)=F_\gamma(0)\). Continuity gives a positive interior crossing and an interior minimum. This proves the claimed robustness, without asserting the number or uniqueness of such features for other exponents.

## Verification

The exact identities were independently checked by symbolic differentiation and factorization. The standalone Python 3 script `checker.py` uses only the standard library. It verifies the original weighted formula against the closed form for thousands of rational perfect-square patch densities, checks the exact uniform-comparison factorization and sign, tests the monotonicity and crossover classification on sample parameter grids, and tests the weaker general-exponent assertion. Run `python checker.py` from the directory containing that file. The supplied version completed 12,081 assertions. Numerical grids serve as diagnostics only; the proof above supplies the infinite-parameter conclusions.

As a transparent example, \(m=2K\) yields \(t_*=(\sqrt6-1)K\), \(d_*=K\sqrt{4-(\sqrt6-1)^2}\), and \(d_0=\sqrt3 K\). Therefore the average intake first falls below its homogeneous value \(2/3\), crosses it once, and reaches \(4/5\) at complete aggregation.

## Relationship to prior work

Spatial aggregation and predator search are established mechanisms in population functional responses. Nachman (2006, *Journal of Animal Ecology*) develops a broader stochastic prey-distribution and predator-aggregation framework with an aggregate Holling-type response and reports that the benefit of prey clumping changes with abundance. Its published text and appendices do not state the sharp deterministic two-patch square-root reentrance, the exact \(m=K\) boundary, the unique interior minimum, or the crossing \(d_0\) identified above. The general aggregate-response framework motivates the object and could be specialized to obtain its initial weighted expression; the nonmonotonicity and exact thresholds still require the separate analysis given here.

Nachman (2006, *Experimental and Applied Acarology*) estimates feeding from measured patch-level prey/predator distributions and reports qualitative clumping and nonrandom-search effects, not this deterministic threshold. Hossie and Murray (2016) experimentally explore spatial prey distributions with predator interference and a ratio-dependent functional response, which is a different behavioural response and does not directly give the present formula. Relevant published mathematical findings on fixed-predator generalized Type III patch allocations and on prey aggregation versus logistic self-crowding optimize different quantities without the assumed square-root redistribution weights; they do not imply the present fixed-mean predation-intake phase diagram.

## Limitations

This is a mathematically exact statement about an idealized imposed tracking rule, not an empirical statement that any predator follows a square-root patch preference. Spatial transfer costs, delays, imperfect prey localization, within-patch predator interference, handling-time heterogeneity, patch size differences, and prey depletion are excluded and may change thresholds. The robustness argument supplies existence, but not uniqueness, for the wider sublinear-power family. Published prior work has broad population functional-response machinery; despite the comparisons described above, historical-priority claims remain provisional and require independent literature review. The numerical script supplements rather than certifies the proof. No population persistence or ecological management outcome is established.

## References

- Nachman, G. (2006). *A functional response model of a predator population foraging in a patchy habitat*. Journal of Animal Ecology 75, 948–958. First published 23 June 2006. https://doi.org/10.1111/j.1365-2656.2006.01114.x
- Nachman, G. (2006). *The effects of prey patchiness, predator aggregation, and mutual interference on the functional response of Phytoseiulus persimilis feeding on Tetranychus urticae*. Experimental and Applied Acarology 38, 87–111. https://doi.org/10.1007/s10493-006-7209-4
- Hossie, T. J. and Murray, D. L. (2016). *Spatial arrangement of prey affects the shape of ratio-dependent functional response in strongly antagonistic predators*. Ecology 97, 834–841. https://doi.org/10.1890/15-1535.1
- Skalski, G. T. and Gilliam, J. F. (2001). *Functional responses with predator interference: viable alternatives to the Holling Type II model*. Ecology 82, 3083–3092. https://doi.org/10.1890/0012-9658(2001)082[3083:FRWPIV]2.0.CO;2
