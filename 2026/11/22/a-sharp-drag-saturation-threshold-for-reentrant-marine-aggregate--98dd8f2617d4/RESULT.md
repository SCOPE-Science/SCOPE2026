# A sharp drag–saturation threshold for reentrant marine-aggregate settling

## Finding

A single aggregate's modeled terminal sinking speed can first decrease, then increase, and finally decrease again as buoyant-microplastic loading rises. A sharp parameter-independent condition determines whether this three-phase pattern is possible at all within the following idealized family. For positive \(a,b,c,\eta\) and \(0<\alpha<1\), set
\[
g(x)=a+\frac{bx}{1+x}-cx,\qquad
V_\alpha(x)=\frac{g(x)}{(1+\eta x)^\alpha}.
\]
Here \(x\ge0\) is dimensionless loading; \(a\) is baseline excess downward mass, \(bx/(1+x)\) a saturating aggregate-mass gain, \(cx\) the buoyant plastic contribution, and \(1+\eta x\) relative displaced volume. For a creeping-flow spherical object, terminal speed is proportional to excess downward mass divided by radius, yielding \(\alpha=1/3\) if radius scales as the cube root of displaced volume. These are independent constitutive assumptions, not empirically fitted universal laws.

**Theorem.** On the sinking region \(0<x<x_b\), where \(x_b\) is the unique positive zero of \(g\), the speed \(V_\alpha\) has at most two stationary points. When both exist, they are a strict local minimum followed by a strict local maximum. For fixed \(\alpha,\eta\), some positive choices of \(a,b,c\) realize both if and only if
\[
\eta>\frac{2}{1-\alpha}.
\]
In particular, at the spherical Stokes exponent \(\alpha=1/3\), the sharp frontier is \(\eta>3\).

For a complete *fixed-parameter* test define
\[
H(x)=(1+\eta x)g'(x)-\alpha\eta g(x),\qquad
Q(x)=(1+x)^3H'(x)
=b\bigl((1-\alpha)\eta-2-(1+\alpha)\eta x\bigr)
 -(1-\alpha)\eta c(1+x)^3.
\]
There are two strict interior stationary points if and only if \(H(0)<0\), \(Q(0)>0\), and \(H(z)>0\), where \(z>0\) is the unique root of \(Q(z)=0\) (which exists when \(Q(0)>0\)). Strict equality at the final condition gives a stationary inflection, **not** two extrema.

## Assumptions and scope

The result concerns one fixed, independently suspended spherical-like aggregate and a nonnegative scalar load, not a population-averaged transport simulation. A Stokes-force balance motivates the exponent, but no assertion is made that a natural fractal marine-snow aggregate obeys it. The positive-sinking interval has the unique endpoint
\[
x_b=\frac{b+a-c+\sqrt{(b+a-c)^2+4ac}}{2c};
\]
this follows by multiplying \(g(x)=0\) by \(1+x\) and selecting its positive root. At \(x_b\), terminal sinking ceases; the theorem makes no claim about resuspension, ascent, mixing, or post-buoyancy dynamics. Every quantifier in the threshold is existential in \(a,b,c\) for fixed \(\alpha,\eta\); it is **not** an assertion that all admissible parameter sets above threshold exhibit two turning points.

## Proof

The numerator is strictly concave:
\[
g'(x)=\frac{b}{(1+x)^2}-c,\qquad g''(x)=-\frac{2b}{(1+x)^3}<0.
\]
It starts positive and tends to negative infinity, so its unique positive zero \(x_b\) has \(g'(x_b)<0\). Direct differentiation gives
\[
V_\alpha'(x)=(1+\eta x)^{-\alpha-1}H(x),\quad
H'(x)=\frac{Q(x)}{(1+x)^3}.
\]
For every \(x\ge0\),
\[
Q'(x)=-b(1+\alpha)\eta-3(1-\alpha)\eta c(1+x)^2<0.
\]
Thus \(H\) is strictly decreasing, or rises once then falls once. It has at most two positive roots; if both lie inside the sinking region, then \(H(x_b)=(1+\eta x_b)g'(x_b)<0\) forces a negative–positive–negative sign sequence, giving first a strict minimum and then a strict maximum.

If \(\eta\le2/(1-\alpha)\), then
\[
Q(0)=b((1-\alpha)\eta-2)-(1-\alpha)\eta c<0;
\]
so \(H\) decreases throughout and two extrema are impossible. Conversely, when \(\eta>2/(1-\alpha)\), fix \(c>0\), then select \(b\) large enough that \(Q(0)>0\). This implies \(b>c\), so \(g\) increases near zero. Choose
\[
a=\frac{b-c}{\alpha\eta}+\delta
\]
with \(\delta>0\) sufficiently small. Then \(H(0)=-\alpha\eta\delta<0\), but \(H'(0)>0\) gives a nearby \(x>0\) where \(H(x)>0\). Since \(g>0\) throughout that initial neighborhood and \(H(x_b)<0\), there are exactly two interior roots. This proves sharpness.

For the fixed-parameter criterion, \(Q(0)>0\) gives a unique positive root \(z\). It also implies \(b>c\), hence \(g'\) first vanishes at \(x_0=\sqrt{b/c}-1>0\). At \(x_0\), \(H'(x_0)=(1+\eta x_0)g''(x_0)<0\), proving \(z<x_0<x_b\). Consequently \(H\) strictly rises on \((0,z)\), then strictly decreases on \((z,x_b)\), and is negative at \(x_b\). Exactly two roots exist if and only if the stated three strict inequalities hold.

**Exact existence witness.** With \(\alpha=1/3,\eta=100,a=5,b=100,c=1\),
\[
g(x)=\frac{5+104x-x^2}{1+x},\quad x_b=52+3\sqrt{301},
\]
and the exact stationary-sign polynomial is
\[
3(1+x)^2H(x)=-200x^3-10903x^2+18794x-203=:F(x).
\]
The rational signs \(F(0)=-203<0\), \(F(1/10)=156717/100>0\), and \(F(2)=-7827<0\) certify two different positive roots in \((0,1/10)\) and \((1/10,2)\). Both lie before \(x_b\). The general bound rules out any other sinking-region stationary point. Numerically the local minimum occurs at \(x\approx0.0108698783\) with speed \(\approx4.74551465\), and the local maximum at \(x\approx1.661880219\) with speed \(\approx11.93889155\); these approximations do not enter the proof.

## Verification

The standalone `check_settling.py` script uses exact integer/rational arithmetic for the displayed stationary polynomial, three sign certificates and sharp-threshold boundary checks. It also performs additional seeded numerical consistency tests, which do not prove the infinite-parameter theorem. Run with `python3 check_settling.py`; Python standard library only. The analytic proof above establishes all universal quantifiers.

## Relationship to prior work

Yoshitake, Isobe, Song and Shim (2023) give a marine-snow/microplastic particle-tracking model and explicitly describe two opposing effects of buoyant microplastic incorporation: lowered excess density and increased aggregation. They report that their chosen size-based settling law switches on whether plastics are present without dependence on **total incorporated microplastic mass**, leaving a load-dependent formula for further work. Roberts and colleagues (2024) observe reduced marine-snow settling speed and carbon content in microfiber-amended treatments; these measurements do not assert the present reentrant law. Chajwa and colleagues (2023) examine viscoelastic mucus tails and Stokesian settling, rather than loading-triggered saturated mass gain and a sharp drag-volume threshold. Maggi (2013) develops a more physical drag/fractal-aggregate settling equation. Its accessible full-text sections treat size, density, and fractal geometry rather than the present plastic-loading saturation law, although some central displayed equations are image-rendered and retain an exact-form comparison limitation. Standard Stokes drag and elementary monotonicity differentiation are prior mathematics and are not asserted as new. The assessed new claim is only the *complete sharp trichotomy and threshold within the explicitly assumed load-dependent family*, not the underlying physical mechanisms.

## Limitations

No value of \(a,b,c,\eta\) is inferred from published experiments. The assumed saturating benefit and linear buoyant penalty may fail, and \(\eta=100\) is illustrative rather than measured. Fractal geometry, inertia, turbulent stirring, particle collisions, biofilm growth, dissolution, and biological variability are excluded. Therefore these curves must not be presented as ocean-wide sinking-speed predictions. Priority remains provisional: exact comparison with some image-rendered formulae in broad physical-sedimentation studies, including Maggi (2013), is limited. No independent audit has been performed.

## References

1. M. Yoshitake, A. Isobe, Y. K. Song and W. J. Shim, “A Numerical Model Approach Toward a Settling Process and Feedback Loop of Ocean Microplastics Absorbed Into Phytoplankton Aggregates,” *Journal of Geophysical Research: Oceans* (2023), https://doi.org/10.1029/2022JC018961. First public date: 2023-04-23.
2. C. Roberts and colleagues, “Microplastics may reduce the efficiency of the biological carbon pump by decreasing the settling velocity and carbon content of marine snow,” *Limnology and Oceanography* (2024), https://doi.org/10.1002/lno.12615. First public date: 2024-08-26.
3. R. Chajwa and colleagues, “Hidden Comet-Tails of Marine Snow Impede Ocean-based Carbon Sequestration,” arXiv:2310.01982 (2023), https://arxiv.org/abs/2310.01982.
4. F. Maggi, “The settling velocity of mineral, biomineral, and biological particles and aggregates in water,” *Journal of Geophysical Research: Oceans* (2013), https://doi.org/10.1002/jgrc.20086. Full text not inspected.
