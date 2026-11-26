# Independent mathematical audit

## correctness

PASS

For standard Brownian motion, one fixed normalized boxcar exposure of width 0<h<1, start t in [0,1-h], and independent Gaussian variance η>0, conditioning subtracts C(s)^2/D from the prior variance, with D=t+h/3+η. Integrating the squared covariance on the three regions gives t^3/3 + ht^2 + (2/3)h^2t + (2/15)h^3 + (1-t-h)(t+h/2)^2, which simplifies to the stated N_h. The derivative numerator P=N_h'D−N_h starts strictly positive, increases until (1-h)/2 and then decreases strictly since P'=2(1-h-2t)D. In particular the sign of 180P(1-h)=F(h)+15h(12-7h)η decides the unique optimum; equality still gives strictly increasing gain before the endpoint. F'(h) changes sign once from positive to negative in (0,1), and F(0)<0<F(1), so the single critical width is valid. The interior derivative in η is positive because N_h'>0 and P'<0 there; expanding at the simple terminal root at threshold gives the stated first-order arrival coefficient. Expansion of the threshold gives 1/(3h)−29/36+O(h). For fixed η the gains converge uniformly using the polynomial expressions on [0,1], and the unique interior maximizer of the limit is eventually feasible; its derivative gives the stated quadratic and root.

## originality

PASS

The decisive overlap is in Gaussian linear-observation conditioning, not in the optimizer under the same kernel, sensor constraint and loss. The closest distinct indexed transition was read at its theorem: it has a different prior and scalar target with reflection symmetry, and is not a covering design theorem. This assessment concerns the finite-width phase diagram, not Gaussian conditioning or the general observation framework.

## value

PASS

Fixed-duration exposure is a natural scalar observation constraint. The theorem gives the entire width/noise boundary, including uniqueness at equality, and distinguishes finite exposures from point observations: for each fixed finite noise there is no terminal phase in the zero-width limit, but at positive width a terminal optimum can be forced by noise. The explicit rule resolves where to place a constrained sensor, not merely how to calculate its posterior risk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
