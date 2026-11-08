# Scientific review

## Correctness — PASS

The generator is explicitly specified for all eight occupancy states; strict irreducibility holds for every positive colonization rate. Exact symbolic stationary-vector calculations yield four explicit probability rational functions. The full-occupancy difference has a strictly positive denominator and numerator proportional to a polynomial with exactly one positive root by Descartes' rule and endpoint signs. The regional-empty-state difference has a strictly positive numerator for every positive rate. The embedded checker reconstructs the matrices, verifies stationarity and the polynomial identities, and independently checks 112 cofactor stationary weights. These are exact rather than Monte Carlo checks. There is no claim at \(c=0\), nor for arbitrary rates or networks.

## Originality — PASS, provisional within inspected evidence

Foxall (2014) contains the general site-dependent spontaneous contact-process model, irreducibility criteria, and monotonicity when one model's rate parameters dominate another's coordinatewise. Endpoint-only versus center-only immigration vectors are incomparable, so those monotonicity results cannot give this comparison. His §8 star example uses positive spontaneous rates at every site and reduced approximations, not an exact three-site one-gateway optimum. Economou, Gómez-Corral, and López-García (2015) give finite SIS generator algorithms, not the precise sign reversal in examined material. Hanski–Gyllenberg (1993) and Freckleton–Watkinson (2002) give ecological context, not this stationary polynomial. Dedicated exact three-site, equivalent-parameter, and alias searches yielded no dominating statement. The generic ability to solve a finite chain is not the same mathematical assertion as a unique sign-changing optimal source-location theorem. A later full-text comparison with the remaining Economou material and any overlooked specialized older finite-contact-process tables would be prudent.

## Value — PASS

Three sites is the smallest connected path having distinct endpoint and interior single-gateway placements. The completed classification reveals a meaningful tradeoff between avoiding regional emptiness and ensuring simultaneous occupation under precisely the same rate constraints. The sign change is a nontrivial boundary between two natural infrastructure choices rather than a numerical sensitivity of an arbitrarily chosen probability. Its real-world interpretation is deliberately limited to the idealized model.

## Remaining limitations

Only stationary probabilities with equal external immigration and extinction rates are classified, with neighbor-to-neighbor rescue rate \(c>0\). No causal field recommendation, larger-network theorem, independent proof audit, or historical uniqueness certificate is claimed.

Self-review: passed. Independent audit: not yet performed.
