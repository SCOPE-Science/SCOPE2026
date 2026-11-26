# Independent mathematical audit

## correctness

PASS

For fixed a,b>0, let v tend to zero with u=v/2 and h=4(a+1)^2 v^2. Then the rectangle conditions hold, the two row-sum Lipschitz bounds tend to zero, and the number of integers between a/v+1 and 2a/v-1 diverges. For each such k the denominator of the inverse is strictly between a pi/v and 2a pi/v by the margins in k and bh<pi/4, so the inverse takes values in (u,v). The phase interval is a k-pi translate of [arcsin sqrt(u)-bh,arcsin sqrt(v)], of width less than pi; the reciprocal images for different k are separated. Differentiating the inverse gives the stated row-sum bound via x<=v and w in [u,v]; differentiating the second coordinate uses |sin(2t)|<=2|t|. The transverse update stays in [0,h/4]. In the sup metric on rectangle-valued one-sided sequences with y_0 reset to eta, the simultaneous backward x and forward y update is a strict contraction of a complete space. Its fixed points are genuine orbits in the chosen branches. Every fixed-point coordinate depends continuously on the code in the product topology and on eta, since finite Picard iterates only use finitely many symbols for that coordinate and convergence is uniform. The initial-state image is therefore compact, and shifting a fixed orbit exhibits forward invariance. The branch intervals are compact and pairwise separated; each code coordinate is recovered continuously from the corresponding iterate, so the itinerary map is continuous and onto, giving the entropy lower bound. A periodically repeated p-word yields a continuous self-map eta to y_p of [0,h]. A fixed eta and uniqueness of the coded orbit imply F^p fixes its starting state; distinct p-words give disjoint itineraries. These are fixed points of the iterate, not all necessarily of least period p. If invariant is taken to mean onto, the nested compact sets F^j(K_N) all retain onto coding and contain the constructed periodic points, and their intersection does too. The theorem does not extend the map continuously to the singular line or claim infinite entropy on a single compact subsystem. RESULT.md lines 18–59 are the analytic replay path; VERIFICATION.md and the finite mpmath checker were inspected, not executed.

## originality

PASS

Best-of-knowledge pass for the exact Zhu planar recurrence at every positive parameter pair, with compact factors onto arbitrary finite one-sided full shifts and exponential iterate-fixed-point lower bounds. The same-day Resultary near-match proves full shifts for Chebyshev-deformed orders of a different symmetric recurrence; the exact equation comparison rules out direct coverage by that result.

## value

PASS

The proof gives rigorous recurrent symbolic complexity at every positive parameter pair of a specific singular dynamical system. It goes beyond numerical entropy, one-step branch multiplicity and saddle counts: arbitrary words can be followed indefinitely on compact nonsingular sets, and periodic words lift to actual periodic trajectories. The separation between compact-subsystem entropy and undefined global compact dynamics is scientifically meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
