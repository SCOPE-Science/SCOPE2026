# Review of the first path failure for three-stage Radau IIA

## Correctness

**PASS.** The exact polynomial identity follows from the stability function, the positive spectral determinant and a terminating coefficient recurrence. For every path through thirteen vertices the standalone verifier checks nonnegative coefficients of a nonzero positive multiplier of each entry numerator; this is an all-positive-real-step argument. A strictly negative exact rational value for the endpoints of the fourteen-vertex path is obtained both from the polynomial identity and an independent exact Gaussian-elimination calculation. The claim carefully makes no assertion about all larger paths or internal stages.

## Originality

**PASS, with an identified access limitation.** Horváth's general step-size-threshold theory and the available complete text of Zappavigna–Colaneri–Kirkland–Shorten study classical positivity mechanisms but not the full-graph path order thirteen/fourteen for the three-stage \([2/3]\) completed map. Wade–Khaliq–Siddique–Yousuf discuss related Padé smoothing methods; an abstract and publication record were accessible, but the full historical article could not be inspected, leaving a stated publication-priority risk. Separately known lower-stage Radau and Gauss path results concern different rational maps and do not imply this numerical cutoff.

## Value

**PASS.** The smallest graph order permitting a negative state from nonnegative data at an arbitrary timestep is a natural sharp structural boundary for an established fifth-order stiff integrator. Its thirteen/fourteen transition distinguishes completed positivity from stability, and the exact finite-polynomial certificate avoids extrapolating numerical experiments to infinitely many real steps. This is a self-contained exact cutoff, not an arbitrary timestep sample.

## Closest literature and limits

References: Horváth (2005), DOI 10.1016/j.apnum.2004.08.026; Wade et al. (first online 2004-09-29), DOI 10.1002/num.20039; Zappavigna et al. (2010), https://www.hamilton.ie/shravan/pade_MTNS10_long.pdf. The inaccessible Wade full text creates a residual novelty risk. The theorem is limited to unweighted paths and completed steps and does not establish a property for all larger path orders.

Self-review: passed. Independent audit: not yet performed.
