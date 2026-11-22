# Independent mathematical audit

## correctness

PASS

Explicit exponential formulas yield trPhi=e^(sigma t)g(t)+e^(mu t)h(t), D=e^(2(a-d)t); the quadratic Jury criterion reduces stability to |trPhi|<1+D. In the stated parameter wedge, kappa>d-a>0, hence sigma>0, while mu<0. Uniform simple zeros of g(t)=R cos(omega t-theta) localize all late stable times; |H'| dominates |D'| in fixed small zero-neighborhoods, so the two Jury crossings bound a unique component. Uniform scaled Taylor expansions yield boundary displacement exp(-sigma*t_n)/(omega R); geometric domination yields the exact tail measure. Independent SciPy exponentials agreed with derived trace and showed stable centers at (a,d)=(0.1,11), (0.4,3). This verifies the claimed reduced ODE; finite checks do not establish the asymptotic theorem.

## originality

PASS

The closest earlier paper proves precisely the matrices and their all-dwell Floquet membership inequality, and illustrates recurrent finite windows. This is acknowledged as foundational, not claimed new. The surviving theorem proves unboundedly many connected components with rigorous uniqueness, a uniform sharp exponential endpoint/width law and a tail-measure limit, none of which follows as an explicitly stated earlier theorem; proving uniform late geometry needs a separate asymptotic argument. Best-of-knowledge novelty qualified by potentially implicit use of the same exact Floquet formula.

## value

PASS

A natural control question in focus/saddle antiresonance is whether exceptionally slow schedules continue to stabilize despite both frozen and averaged instability. Infinite components, the exact exponential tuning precision and finite total stable-time measure quantify a structurally meaningful dynamical phenomenon that the published finite-window diagrams do not characterize.

The dated certificate retains the supplied scientific assessment, sources and limitations.
