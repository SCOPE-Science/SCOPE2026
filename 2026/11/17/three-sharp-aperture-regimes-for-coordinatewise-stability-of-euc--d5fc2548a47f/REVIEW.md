# Independent mathematical audit

## correctness

PASS

Orthogonal meridian minimization gives exact projection with middle rho=(kappa*t+r)/(1+kappa^2) between polar region t<=-r/kappa and cone t>=kappa*r. Differentiation of the middle branch gives top row (kappa^2,kappa*u)/(1+kappa^2), spatial block cI+(1/(1+kappa^2)-c)uuT with c=(1+kappa*t/r)/(1+kappa^2). The induced infinity norm is max absolute row sum, convex in c, so sharp sup follows from c=0 and 1. For u unit, fix a=|u_i| and maximize other components via sum<=sqrt(d-1)sqrt(1-a^2), giving the exactly stated B-/B+ scalar maxima. Integrating derivative bound over segments gives global two-input Lipschitz; taking limiting row-sign differential perturbations gives sharpness. The maximum a*sqrt(1-a^2)=1/2 yields all three leading coefficients and open interval dominance at thresholds 1/2,2 (no tie regime asserted). Independently checked finite middle-region directional Jacobian differences for 400 random cases from several dimensions/apertures. Finite samples corroborate but do not prove the supremum/infinite-d theorem.

## originality

PASS

The previously published standard Lorentz-cone exact norm is recovered only at kappa=1, and its explicit scope excludes arbitrary apertures. Changing kappa is not an isometry of Euclidean projection, so it cannot be obtained by conjugating a coordinate norm. The other scaled-cone prior result minimizes distances in l_p, rather than Euclidean distance then measuring errors in l_infinity. No inspected primary theorem gives this variable-aperture three-branch classification.

## value

PASS

A sharp, reproducible stability constant and two meaningful aperture phase transitions answer a natural sensitivity question for second-order-cone projection. The exact dimension-dependent row types distinguish polar, axial and cone-side amplification, which general Hilbert nonexpansivity masks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
