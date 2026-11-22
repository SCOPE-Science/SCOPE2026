# Independent mathematical audit

## correctness

PASS

The intrinsic quotient shortest lift uses signed horizontal separation in (-w/2,w/2), independent of heights with density y^-2. An upper-half-plane geodesic arc from endpoints of heights a,b<=H rises past H iff z>sqrt(H^2-a^2)+sqrt(H^2-b^2); the discarded outside-apex case cannot overshoot. Transformation u=sqrt(H^2-a^2), v=sqrt(H^2-b^2) gives the exact triangular double integral with Jacobians u/(H^2-u^2)^(3/2) and v/(H^2-v^2)^(3/2), valid for H>=sqrt(1+(w/2)^2). I independently evaluated its two Dirichlet moments exactly, L^4/120 and L^6/420, giving the asserted w^4/1920 and w^6/17920 coefficients. Fresh scipy double quadrature w=2,H=5,10 yielded 5.426287647211641e-7 and 8.369194605559188e-9; relative error of two-term expansion decreased from 2.81e-4 to 1.76e-5. The marked change (z=Lr,u=z s,v=z t) yields density proportional r^4 s t and hence independent Beta(5,1) and Dirichlet(2,2,1); uniform convergence of compact-domain density factors proves TV O(H^-2), not just weak convergence.

## originality

PASS

Best-of-knowledge PASS for the interior maximum-horocycle event with both endpoints below H and its beta–Dirichlet mark law. Previously published same-cusp area-point results study the distance D_w, while Haas and other cusp-excursion work studies generic geodesic/flow observables. Identical cusp geometry and an inverse-width consequence do not imply this distinct event or its sextic coefficient.

## value

PASS

The probability of a minimizing geodesic leaving a horocyclic depth cap even though both randomly sampled endpoints lie below it is a natural geometric rare event. Its sharp exponent six and next coefficient distinguish it from distance tails; the exact beta–Dirichlet conditioned shape identifies how overshoot occurs and provides an independent inverse-width statistic. This is a motivated new path observable and a nontrivial limit theorem, not a relabelled distance distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
