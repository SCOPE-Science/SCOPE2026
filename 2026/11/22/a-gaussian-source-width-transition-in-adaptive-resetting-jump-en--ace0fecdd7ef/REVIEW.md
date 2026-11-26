# Independent mathematical audit

## correctness

PASS

The frozen uniqueness claim is false if read pointwise for arbitrary rate functions: changing r_R at x=0, for example adding one there, preserves the integrated hazard along every OU excursion almost surely (the transition distribution has a density at each positive time). The normalized flux, invariant law and J are unchanged. The corrected RESULT states uniqueness a.e., with exactly one continuous version. Checked the repair: the weak stationary forward equation with integrable r_R rho_v forces the rate a.e.; optimizing the negative part of f_z over the Gamma-half variable gives Y_*=(1−3z)/(2z(1−z)) for z<1/3, otherwise zero, with the stated sharp threshold. For R>R_* the rate has a positive lower bound and quadratic growth. The repaired killed-OU resolvent on L² of the free invariant Gaussian is valid by symmetry and Gaussian cutoff approximation, and identifies the stationary density as the normalized regenerative occupation measure. The stationary jump rate is covariance of h and log h with h=R+f_z; positivity and the derivative −E[f_z²/(R+f_z)]/R follow using the bounded negative part and integrable positive tail. Free diffusion gives a²v/D. For T=R/a, inversion of F=f_z/a~2z^(3/2)Y exp((1−z)Y) and Gamma-half survival give K(z)T^(−p)(log T)^(p−1/2); Potter bounds control the entropy-tail integral for 1<p<2, and integration by parts plus the beta integral give pπ/[(p−1)sin(π(p−1))]. For z>1/2, Gamma-half moments of orders 0,1,2 give the stated second moment, which is the limit of RJ. For z=1/2+lambda/L the normalized square-integrand density on 0<t<2 is z(2zt−1/L)² t^(−1/2) exp(−2 lambda t)/sqrt(π); the log factor divided by its argument tends to one uniformly in compact lambda for each such t. The negative part is O(a²/R) before normalization and the tail above 2L is O((a²/R)L^(3/2)) uniformly, giving the crossover and in particular Phi(0)=0.6383076486. Independently recomputed the second moment numerically at z=.54,.6,.9 and integrated the rescaled log integrand for lambda=−1,0,1 at L=80,320,1280; final ratios to Phi were 0.956420, 0.986075, 1.000479. These are finite checks only; the frozen checker was read, not executed. The fixed-width limits, flux normalization and compact-uniform quantifier all hold for the corrected rate class.

## originality

PASS

Best-of-knowledge pass for the explicit Gaussian high-flux entropy trichotomy and its compact-uniform logarithmic crossover in the repaired record. The inverse hazard, generic feasibility formula and entropy covariance are prior results and the elementary Gaussian threshold is retained as input rather than a standalone novelty claim.

## value

PASS

The half-width boundary and its compact-uniform logarithmic crossover explain when increasing flux suppresses stationary jump entropy at an ordinary inverse-rate scale and when the Gaussian tail prevents that rate. This supplies a nontrivial, quantitative design distinction while keeping the positive diffusive contribution and any device work separate. Correcting equivalence of rate versions leaves the genuine high-flux result intact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
