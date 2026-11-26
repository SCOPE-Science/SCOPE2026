# Independent mathematical audit

## correctness

PASS

The folded coordinate Y=b+|X| has generator D∂² with Neumann boundary at b and killing a/y². Recurrence gives infinite occupation near b and a finite first reset almost surely. For the zero resolvent one may first absorb at M>b: the right solution v_M(y)=y^(-eta)-M^(-2eta-1)y^(eta+1) vanishes at M and the endpoint kernel is v_M(y)/(-D v'_M(b)). Monotone exhaustion gives the stated G(b,y). The killed Markov property and Tonelli give the Kac recursion, also for infinite moments. From any y, Brownian scaling and the Lipschitz fold give a fixed positive probability of staying within y/2 of y for a time proportional to y²/D with bounded integrated hazard. Thus the recursion dominates the integral of y^(2m-2-eta) and diverges even at equality. Conversely, positive Neumann supersolutions B_k control the killed occupation of y^(2k-2) via stopped Feynman–Kac, and Kac induction bounds M_k by a constant times y^(2k). For eta>1, the growth bound removes the Neumann homogeneous solution growing as y^(eta+1) from M_1. Its explicit Neumann solution and the two elementary integrals for M_2 give the printed moments, CV²=1+4eta/((eta-3)(2eta-1)), and its strictly negative derivative for eta>3. The counting limit follows from the finite-variance renewal asymptotic: for the first renewal beyond t, Wald's stopped centered sum has variance σ² E(N(t)+1); the overshoot second moment is o(t), since for any C its bound is C²+E(N(t)+1) E[R² 1_{R>C}]. With E N(t)~t/μ this gives Var N(t)~t σ²/μ³. Hence the Fano limit equals CV² exactly in the stated finite-variance regime.

## originality

PASS

The supported distinction is the sharp hierarchy for moments of the time between resets (with divergence at equality), the specialized raw second moment and the strict decreasing excess-noise classification for this rate. The finite-mean threshold, stationary spatial power law and moment hierarchy, general killed-resolvent methods, and general renewal Fano identity are not new. The stationary result gives closely related thresholds, even exact equality of the corresponding integrability tests after comparing remaining lifetimes, but it does not by itself establish those comparisons or give the temporal second moment and noise law.

## value

PASS

Stationary spatial localization, finite mean waiting time, and finite clock noise answer different questions about the same natural resetting model. The sharp temporal hierarchy clarifies when higher moments fail, including equality; the exact decreasing excess-noise law distinguishes the process from a Poisson clock and controls the asymptotic count dispersion where it is finite. These are useful dynamical quantities beyond recomputing a stationary tail exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
