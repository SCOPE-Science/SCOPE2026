# Independent mathematical audit

## correctness

PASS

With y=1−x the normalized rate is (1−a)y^{1/2}−(2−a)y^{3/2}+y^{5/2}; its third x-derivative is −[3(1−a)+3(2−a)y+15y²]/(8y^{5/2})<0. Thus f' is strictly concave and the mean derivative of the symmetric gap is negative in the open feasible interval; continuity and interior strict decrease give strict order also at both endpoints. At m=1−d the warm term vanishes and f(1−2d)/f(1−d)<√2, making the gap negative. At m=a+d the gap divided by d is the difference of two nonnegative terms, whose squared difference is −d[7d²+(9a−3)d+a(3a−2)]. At a≥2/3 this bracket is positive for d>0. Below 2/3 the bracket has exactly one positive zero, the stated radical, strictly below (1−a)/2 because its value there is (1+a)²/4. The endpoint signs and strict decrease settle uniqueness, including equality only at m=a+d at the critical amplitude. Differentiating the radical gives d_*'<0 and continuity gives the two limiting values. The physical scale factor is positive, so it preserves signs. In the scope prose, ‘largest half-amplitude admitting a positive gap’ should read ‘supremum’: strict benefit is not attained at the ceiling, as the theorem correctly specifies. A separate bisection reproduces m_*=0.5247407404111 at a=.2,d=.1 and the cutoff 0.3033078030247. Frozen CHECK.py was inspected, not executed; those grid tests are diagnostic.

## originality

PASS

Nonlinear rate summation, Brière fitting and curvature-dependent effects of variable temperature are prior. The closest retrieved primary paper uses a local mean-variance approximation, with separate Brière fits to empirical data. Neither it nor the compared exact Lactin-2 result yields the finite-amplitude Brière-I quadratic sign criterion and unique all-mean crossover. This is bounded to inspected evidence, with full-text gaps identified below.

## value

PASS

For a standard empirical arthropod development law, the question whether there is any feasible mean at which finite symmetric excursions help is a motivated global invariant, not a small-variance or one-parameter numeric example. The exact amplitude ceiling, unique below-ceiling crossover, and calibrated-scale ratio threshold provide comparisons meaningful to rate-summation modelers. The result is restricted to equal-duration in-range temperatures and instantaneous development; it does not establish a population response, biological memory effect or field validation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
