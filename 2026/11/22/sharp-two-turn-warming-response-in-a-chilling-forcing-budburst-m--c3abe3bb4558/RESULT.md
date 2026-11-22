# Sharp two-turn warming response in a chilling–forcing budburst model

## Finding

An exponential chilling–forcing phenology model with a quadratic cold-exposure curve admits **at most two** reversals of the budburst date as uniform warming increases. There is an exact boundary between strictly advancing budburst and an advance–delay–advance response.

For any \(h>0\), put
\[
y=\frac{1+\sqrt{1+8h}}2,\qquad b_{\mathrm c}(h)=y\exp\!\left(\frac{1+y^{-1}}2\right).\]
If the excess forcing requirement \(b\) is at most \(b_{\mathrm c}(h)\), the predicted date strictly decreases with warming. If \(b>b_{\mathrm c}(h)\), the date has exactly one strict local minimum followed by one strict local maximum, and is strictly decreasing outside the intervening interval. At equality it remains strictly decreasing but has one stationary inflection.

This transition is sharp. The baseline requirement \(h\) raises the critical value \(b_{\mathrm c}(h)\) strictly, and two turning points appear with a square-root separation at the transition.

## Assumptions and scope

All variables below are nondimensional, with an arbitrary reference date \(t_0\). For real warming offset \(w\), real cold-exposure margin \(c\), baseline forcing requirement \(h>0\), and excess forcing requirement \(b>0\), define
\[
 x(w)=(c-w)_+,\quad C(w)=\frac{x(w)^2}{2},\quad H(w)=h+b\exp(-C(w)),
\]
where \((z)_+=\max(z,0)\). The required spring thermal forcing is \(H(w)\). On an ideal linear warming ramp, thermal forcing measured after the growing-degree-day threshold is crossed at \(t=t_0-w\) is \(F(t,w)=\tfrac12(t-t_0+w)^2\) for \(t\ge t_0-w\). Thus the model's budburst date is the unique solution \(F(B(w),w)=H(w)\), namely
\[
 B(w)=t_0-w+\sqrt{2\big(h+b\exp[-(c-w)_+^2/2]\big)}. \tag{1}
\]

The quadratic exposure is realizable for a *finite* linearly tapered winter cold-deficit profile: for \(0\le w\le c=L\), integrating \((u-w)_+\) over \(u\in[0,L]\) gives exactly \((L-w)^2/2\). Outside that temperature range, equation (1) is a specified mathematical continuation and is **not** asserted to describe an entire real winter. The whole-real-line theorem concerns the explicit surrogate (1). Both turning points can occur in the finite-winter interval whenever \(c>x_+\), where \(x_+\) is the larger turning-point cold margin defined below.

This is a deterministic timing model, not a fitted plant physiology model. Temperature, chilling, and forcing have deliberately simplified response curves; a photoperiod floor, frost injury, and organism-to-organism variability are excluded.

## Proof

**1. The derivative and its single maximum.** For \(w<c\), set \(x=c-w>0\), \(v=b e^{-x^2/2}\), and
\[
R(x;b,h)=\frac{xv}{\sqrt{2(h+v)}}.\]
Differentiating (1) gives \(B'(w)=-1+R(x;b,h)\). For \(w\ge c\), the derivative is exactly \(-1\); at \(w=c\), the two one-sided first derivatives agree. Let \(s=v/(h+v)\in(0,1)\). Logarithmic differentiation yields
\[
\frac{\partial}{\partial x}\log R
 =\frac1x-x\left(1-\frac s2\right),\qquad
\frac{ds}{dx}=-xs(1-s).
\]
Therefore \(x^2(1-s/2)\) is strictly increasing from \(0\) to infinity. The derivative of \(\log R\) changes sign **exactly once**, from positive to negative. Also \(R\to0\) as \(x\downarrow0\) and \(x\to\infty\). Hence \(R\) has one strict global maximum and each positive level is crossed at most twice.

**2. The exact critical parameter.** At the sharp threshold, \(R=1\) at its maximum. Write \(z=x^2\) and \(v=b e^{-z/2}\). The equations \(R=1\) and \(\partial_xR=0\) become
\[
zv^2=2(h+v),\qquad z\frac{2h+v}{2(h+v)}=1.
\]
Eliminating \(z\) yields \(v^2=v+2h\). Its unique positive solution is \(v=y=(1+\sqrt{1+8h})/2\), and \(z=1+1/y\). Therefore the only possible tangency has
\[
 x_c=\sqrt{1+1/y},\qquad b_c=y\exp[(1+1/y)/2]. \tag{2}
\]
For every fixed \(x>0\), \(R(x;b,h)\) increases strictly with \(b\), from zero to infinity. Thus the maximum increases strictly and continuously from zero to infinity, proving that (2) is the unique parameter threshold. If \(b<b_c\), then \(B'<0\) everywhere; if \(b=b_c\), the derivative vanishes at the single point \(w=c-x_c\) but is negative elsewhere, so \(B\) is strictly decreasing. For \(b>b_c\), the equation \(R=1\) has exactly two roots \(0<x_-<x_+\); as \(w\) increases, \(x\) decreases, so
\[
B'(w)<0\quad(w<c-x_+),\qquad B'(w)>0\quad(c-x_+<w<c-x_-),\qquad B'(w)<0\quad(w>c-x_-).
\]
The left turning point is a strict local minimum and the right turning point a strict local maximum. There are no other stationary points.

**3. Monotonicity and fold scaling.** From \(h=(y^2-y)/2\), \(y\) increases strictly with \(h\), while \(d(\log b_c)/dy=(2y-1)/(2y^2)>0\). In particular \(b_c(h)\downarrow e\) as \(h\downarrow0\), and \(b_c(h)\sim\sqrt{2eh}\) as \(h\to\infty\).

At \((x,b)=(x_c,b_c)\), set \(g=\log R\). Direct differentiation gives
\[
 g_b=\frac{y}{b_c(y+1)}>0,\qquad g_{xx}=-\frac{2y-1}{y}<0.
\]
Taylor's theorem and the implicit function theorem applied after the change of variable \(u=\sqrt{b-b_c}\) give, as \(b\downarrow b_c\) from above,
\[
 x_\pm=x_c\pm \gamma(h)\sqrt{b-b_c}+O(b-b_c),\quad
 \gamma(h)=y\sqrt{\frac{2}{b_c(y+1)(2y-1)}}. \tag{3}
\]
Thus the two turning points emerge in a nondegenerate square-root fold, not a broad unresolved plateau.

## Verification

The accompanying standard-library Python checker evaluates the critical formula for several baseline requirements; finds both stationary margins by bracketing and bisection; checks derivative sign patterns for subcritical, critical, and supercritical cases; compares analytical derivatives to central differences away from the branch point; and checks the coefficient in (3) against small supercritical perturbations. Run `python3 checker.py` from the extracted directory. Such numerical checks supplement but do not replace the analytical proof above.

For example, take \(h=1\), \(b=8\), and \(c=5\). Then \(y=2\), \(b_c=2e^{3/4}\approx4.234000033225349\). The stationary cold margins are approximately \(x_-=0.583340127587276\) and \(x_+=2.057827342122832\), giving a minimum at warming offset \(w\approx2.942172657877168\) and a maximum at \(w\approx4.416659872412724\). Both lie in the realizable finite winter range \(0\le w\le5\).

## Relationship to prior work

Cannell and Smith (1983) proposed an empirical exponential decrease in the heat required for Sitka spruce budburst with accumulated chill days. Their 1986 climatic-warming analysis established that warming can either advance or delay budburst. Chuine, Cour and Rousseau (1999) compared alternative forcing/chilling formulations. Fu et al. (2012) assessed alternating, sequential, and other phenology models experimentally and described the exponentially chilling-dependent forcing threshold. These motivate the two opposed mechanisms in equation (1).

The present result is specifically the *global sharp analytic phase diagram* of the quadratic cold-exposure / linear spring-temperature surrogate, including the exact forcing-sensitivity boundary, the maximum number and order of turning points, and the square-root onset. The cited biological papers establish mechanisms or evaluate models, not this exact global theorem. General mathematical calculus facts are used in the proof; the analytic threshold is not presented as an empirically measured climate tipping point.

## Limitations

The quadratic chilling law is a deliberately normalized triangular-temperature surrogate, not a universal chill-day law. At very large cold or warm offsets, the whole-real-line continuation can cease to represent a fixed finite winter season. The transition can be observed in a physically restricted warming interval only if that interval contains the relevant turning points. The rate of spring forcing is linear after a threshold, and the model ignores photoperiod, soil moisture, acclimation, genetic variance, saturation of actual chilling capacity, and stochastic weather. The theorem makes no claim that particular species possess parameters in its two-turn regime. Formal external mathematical validation and biological calibration have not been performed. Publication priority remains provisional because the full original 1983 source was not accessible in the present comparison.

## References

- Cannell, M. G. R. and Smith, R. I. (1983), *Thermal Time, Chill Days and Prediction of Budburst in Picea sitchensis*, Journal of Applied Ecology 20, 951–963, DOI: https://doi.org/10.2307/2403139. Abstract and dated bibliographic record inspected; complete text not obtained.
- Cannell, M. G. R. and Smith, R. I. (1986), *Climatic Warming, Spring Budburst and Frost Damage on Trees*, Journal of Applied Ecology 23, 177–191, DOI: https://doi.org/10.2307/2403090. Public abstract inspected.
- Chuine, I., Cour, P. and Rousseau, D. D. (1999), *Selecting models to predict the timing of flowering of temperate trees*, Plant, Cell & Environment 22, 1–13, DOI: https://doi.org/10.1046/j.1365-3040.1999.00395.x. Open full text inspected.
- Fu, Y. H. et al. (2012), *The Impact of Winter and Spring Temperatures on Temperate Tree Budburst Dates*, PLoS ONE 7, e47324, DOI: https://doi.org/10.1371/journal.pone.0047324. Open full text inspected.
