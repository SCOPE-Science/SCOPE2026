# Independent mathematical audit

## correctness

PASS

Functional calculus at x≥0 reduces the normalized error to [L(z)−a tanh(z)]/4 with z=h(lambda+x)/4 and a=w−1. Differentiation gives sech²(z)(J(z)−a). Re-expanding the stated hyperbolic quotient in z² cancels the constant and linear terms and gives positive denominator coefficients b_n and numerator ratios 4^n/[(2n)(2n−1)]−1 for n≥2. The ratios strictly increase, so cross-multiplying the series derivative and pairing indices gives strictly positive terms (m−n)b_m b_n(r_m−r_n) for m>n. Thus J increases from 1/3 to infinity. For 1/3<a<1, the error falls from 0 to one negative minimum then rises to 1−a; the height of the negative minimum is continuous and strictly increasing in a, and crosses 1−a exactly once. To prove the global minimax immediately, every Re(a)<a_* worsens the limit at infinity and every Re(a)>a_* worsens the finite negative contact, regardless of imaginary part. At Re(a)=a_* a nonzero imaginary part already worsens the modulus at infinity. These contacts are available in essential supremum on the multiplication model whenever h*lambda/4≤z_*, including equality by continuity in x. For all other spectra only the universal upper bound is asserted. At w=4/3 the real error is increasing to 2/3 in scalar units, giving exactly h/6 on the unbounded model. Independent Decimal bisection reproduces the displayed z_*, w_*, C_* and improvement ratio (python3 /workspace/reviews/evidence/reproduce.py, output 4); the uploaded diagnostic was read but not executed. The analytic proof, not finite sampling, covers the whole half-line.

## originality

PASS

The trapezoid correction, Langevin representation and first-order phenomenon already appear in Castillo. The distinct same-day Schatten–Weyl work analyzes an exact member of this blend family: 2Q_{h/2}−Q_h=2P_{h/2}−P_h=R_h(2), since the corrections cancel. It does not optimize the weight and does not dominate the audited result. The supported contribution is the exact unique full-spectrum uniform operator-norm weight and sharp constant with its contact model, not a new grid-sampling identity or first-order rate.

## value

PASS

Smooth-vector cancellation and full-spectrum operator error are competing objectives for a natural, already used two-grid rule. The sharp universal constant and uniqueness quantify that distinction: the optimum improves the classical unbounded-spectrum error constant by a factor about 2.61 without promising a higher rate. The fixed continuous-spectrum model explains which scales force the optimum. The guarantee does not address finite time truncation, sampling noise or general nonnormal semigroups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
