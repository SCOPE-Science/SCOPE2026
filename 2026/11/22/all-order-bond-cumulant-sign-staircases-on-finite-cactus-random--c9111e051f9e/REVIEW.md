# Independent mathematical audit

## correctness

PASS

In any occupied subgraph, deleting one edge from each fully occupied host cycle removes precisely the independent cycle-space generators. Substitution into k(A)=|V|-|A|+cycle rank gives independent bridge/cycle blocks even when cycles meet at cut vertices. A mixed cumulant across blocks vanishes by additivity of the log MGF. On a common cycle, dividing the MGF numerator by the product of single-edge MGFs leaves log(1+b times a product of one-variable factors), with each factor equal to 1 and derivative 1-u_e at zero. Distinct derivatives therefore give the stated prefactor times (b d/db)^r log(1+b). The denominator is positive for every q>0, including -1<b<0; no probability-mixture argument with a negative weight is used. Starting with Q_2=1 and Q_3=1-b, the recurrence yields alternating derivative signs at the roots, a positive value at 0, and a leading sign opposite the value at the last root; degree then forces one simple root per complementary interval. For q<1 the positive Eulerian coefficients at -b>0 give a negative cumulant, and q=1 gives zero. For q>1 the derivative of b(t) is strictly positive at every finite t and its range is (0,q-1), so each root below q-1 is crossed once and the endpoint equality is not a finite zero. The stated order-four and order-five thresholds follow by factoring the displayed polynomials. An independent exact enumeration on C4 at q=6, all u=1/2, gives kappa_4=-65/64827; it is positive at all u=99/100. The supplied finite checker was inspected, not run, and does not replace the all-order argument.

## originality

PASS

The finite cactus block law and low-order negative correlations are prior. The distinct claim is the all-order distinct-bond sign and sharp shared scale threshold classification, including the signed q<1 case and all r-2 possible reversals at q>1. The same-day hard-core Eulerian staircase is a genuine analog but does not supply this result.

## value

PASS

For a natural finite spin-system representation this identifies which distinct-bond nonlinear responses are identically zero and gives the exact number and common locations of their reversals, independent of the choice of marked bonds on the cycle. Orders with arbitrarily many reversals are realized. This goes beyond pair association and numerical sign examples without suggesting a thermodynamic phase transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
