# Scientific review: Five-vertex positivity boundary

**Correctness — PASS.** The finding is a quantified exact theorem for every unweighted simple cycle and every nonnegative timestep. Small positive cycles are certified by closed rational formulas and an independent exact-rational interpolation verifier; all larger cycles are obstructed by an explicit Green-kernel asymptotic. The stronger uniform \(h=8\) statement uses an exact six-cycle calculation and rationally certified Fourier-tail bounds for every larger cycle. The script performs checks; it is not a substitute for the symbolic arguments in the proof.

**Originality — PASS, with priority caveat.** The 2013 Lóczi–Ketcheson [2/2] Padé zero absolute-monotonicity radius does not determine positivity of a fixed cycle family. The 2016 Fekete–Ketcheson–Lóczi work on periodic heat uses explicit methods rather than this implicit endpoint map. Existing multipartite filter coverage includes \(C_3\) and \(C_4\), but does not subsume the \(C_5\) and all-\(n\ge6\) assertions. Summaries of two related published records could be reviewed, but their full texts were unavailable, and unindexed priority remains a risk.

**Value — PASS.** The result gives a sharp all-orders-of-resolution boundary for a standard fourth-order implicit time integrator on periodic uniform diffusion grids. Its single universal failure timestep and Green-function explanation identify a structural sign-loss mechanism, not a numerical anecdote.

**Limitations.** No claim of nonuniform-weight robustness, stagewise positivity, a smallest failing timestep, or independent external mathematical audit is made. The theorem concerns endpoint sign preservation only.

Self-review: passed. Independent audit: not yet performed.
