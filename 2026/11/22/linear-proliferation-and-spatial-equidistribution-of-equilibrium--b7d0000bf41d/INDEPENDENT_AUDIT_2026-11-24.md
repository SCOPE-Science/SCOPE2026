# Independent mathematical audit

## correctness

PASS

Use the explicitly defined map, agreeing with Peng et al.'s Eq. (3), not their candidate origin line. The third fixed-point equation forces x=y=p, and the common equation is cos(gamma*theta(p))=g(p) for g(p)=p*L(p)/k. The derivative k*g'=L+p*L' is positive: outside [0,1/2] the second term is nonnegative, and inside it is bounded below by -1/4 since t(1-2t)<=1/8 and the log argument is at least 2. Thus g takes both endpoint values -1,+1 uniquely, and all roots are trapped in [a,b] with b<k/log(2)<1/2 and theta'>0 there. For u=acos(g), gamma*theta-u is increasing. For the other branch, write its derivative as theta'*(gamma-R), with R=g'/(theta'*sqrt(1-g^2)). At each endpoint R is an inverse square root in the distance times a smooth positive factor; differentiation makes it strictly decreasing from the left and increasing to the right, and it is bounded away from the endpoints. For sufficiently large gamma this gives exactly two turns and endpoint turning strips of width O_mu(gamma^-2), with only O_mu(gamma^-1) phase variation. Counting lattice crossings on monotone pieces of each phase over every prefix gives gamma*(theta(t)-theta(a))/(2*pi)+O_mu(1) per branch, since u varies by at most pi. Branches can agree only at the two endpoints, including any endpoint equality; counting distinct roots uses only bounded corrections. Dividing the combined prefix count by its total gives uniform O_mu(1/gamma) CDF error. Integrating that error on the common compact support proves the W1 bound and differentiating the phase CDF gives the stated density. The Jacobian's upper block has symmetric and antisymmetric multipliers P' and P'+2h*sin(z); the third multiplier is 1. If any line fails expansion somewhere, the triangle inequality gives |P'|<=1+2|h|. At a root, the log-derivative term is bounded and the sine prefactor is bounded below by a positive constant times gamma. Hence |sin|=O_mu,h(1/gamma), so 1-|g|=O_mu,h(1/gamma^2), which forces the root into an endpoint strip of that width by the positive derivative of g. The prefix bound gives only O_mu,h(1) roots there, proving the all-z quantifier for the other lines.

## originality

PASS

The map and ordinary phase counting are not new. The inspected primary article and strongest matched catalogue findings do not contain or imply the phase-span coefficient and bounded counting discrepancy, quantitative spatial law, and uniform-over-z expansion exceptions for this fixed-parameter cosine–memristor map. The scalar-amplifier precursor remains a named partial-overlap risk; this is a best-of-knowledge decision, not a finding of historical priority.

## value

PASS

For the actual published map, determining how many stationary lines occur and how they are placed is a natural global counterpart to a local equilibrium discussion and plots. The count and W1 law replace that discussion with a quantitative census, and the stability bound shows that the exceptional lines are negligible even when the criterion must hold for every z. These are specific useful benchmarks about the stationary geometry; they do not assign dynamical frequencies to typical orbits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
