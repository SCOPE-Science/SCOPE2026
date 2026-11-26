# Independent mathematical audit

## correctness

PASS

Start each trial by drawing its eventual mark and duration jointly; record the mark only on completion. First-renewal conditioning gives the displayed PGF. With x=lambda_0, y=lambda_1, a=1-b, c=bx+ay, u=ax, v=by, the transforms are u(s+y)/(s²(s+c)), v(s+x)/(s²(s+c)), and 2uv(s+x)(s+y)/(s³(s+c)²). For the first means the t² terms are u(y-c)/2 and v(x-c)/2; the mixed moment starts at uv t² and its t³ term is uv(x+y-2c)/3. Subtracting yields the stated cubic coefficient. At infinity the mean rates are uy/c and vx/c and the constant terms are u(c-y)/c² and v(c-x)/c². The mixed moment's linear term is 2uv[(x+y)/c²-2xy/c³], so the covariance slope is uv[(x+y)c-2xy]/c³=uv(y-x)(ay-bx)/c³. Negative poles give decaying remainders and continuity; the strict cubic-negative/linear-positive region is exactly the displayed open wedge, establishing existence but not uniqueness. At b=1/2 the cubic vanishes; an independent series gives the positive quartic xy(x-y)²/96. At the upper endpoint the slope vanishes; the wedge claim concerns nonzero leading coefficients, not a classification of crossings at or beyond that endpoint. Independent bounded rational-transform inversion at b=7/10, x=1, y=5 gives covariance -0.0000297696852314 at t=1/20, 0.0201057054623 at t=1 and 2.71805204843 at t=10. The supplied verifier was inspected, not run: it asserts signs at 1/20 and 10 and prints, but does not assert, the t=1 value. Independent worker additivity is immediate; no conditional-on-count assertion is needed.

## originality

PASS

The exact early-versus-late sign regime for this specific observed cross-count statistic survives the inspected comparisons. The model, the marginals, the general two-mark covariance construction and the large-budget slope as a renewal-reward specialization are prior machinery/results, not independent originality claims.

## value

PASS

The sign of a joint fluctuation matters for uncertainty in mixtures assembled from time-censored absorbing simulations. Within the motivating model the theorem identifies a nonempty open regime where mutual exclusivity of a trial's mark gives the wrong intuition about joint counts after a long budget. It is a structural horizon-dependent effect, not merely computation of already-known expected counts or a chosen numerical witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
