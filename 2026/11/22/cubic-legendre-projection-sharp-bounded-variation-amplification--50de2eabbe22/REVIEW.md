# Scientific review: cubic Legendre BV amplification

## Correctness

PASS. Standard Legendre orthogonality gives the step derivative polynomial stated in RESULT.md. Distributional Stieltjes representation reduces the operator seminorm to projected single jumps without smoothness assumptions. The centre jump produces the stated closed radical constant. For all nearby other jumps, the two-root quadratic formula and a rational sign calculation prove strict decrease. The remaining continuum of jump locations is covered by 225 exactly bounded rational Bernstein quadratics, replayed from `checks/cubic_legendre_bv.py` using only Python's standard library. Their strict \(9/5\) ceiling implies global uniqueness. No finite sample is being used as a proof of a continuum assertion.

## Originality

PASS under checked-source, best-knowledge comparison, without an assertion of universal historical priority. Cohen–Tan (2011) studies low-degree Legendre approximation and errors but gives no sharp total-variation operator bound. Tagade–Choi (2012) concerns stochastic spectral Gibbs oscillations and Gegenbauer postprocessing. Braess–Pillwein–Schöberl studies a constructed \(L^2/H^1\)-stable polynomial projector, not this ordinary degree-three projection in \(BV\). Davis–Hagelstein's Gibbs theorem concerns large-degree pointwise overshoot, not this finite-degree BV extremizer problem. Closest database records concern other projection norms, dimensions, polynomial degrees or functions. A related full publisher text was not accessible for exhaustive inspection, and the possibility of older unindexed versions remains a specific residual risk.

## Value

PASS. The first Legendre truncation with a quadratic derivative response to a step has two internal turning points and could in principle have its worst jump away from the centre. Identifying the exact maximum and proving that the centre is the unique jump location is a natural finite-degree stability invariant relevant to Gibbs-type oscillation assessment. The result characterizes all BV extremizers and supplies a rigorous norm benchmark, rather than re-evaluating a known table or optimizing an arbitrary parameter slice. There is no claim about all-degree stability.

## Remaining scientific limits

The calculation applies to the unweighted, real, cubic Legendre projector only. The strict global comparison relies on the transparent finite exact-rational interval certificate; independent human or computer-formal examination has not occurred. Historical completeness is limited by unindexed literature and unavailable full publisher material.

Self-review: passed. Independent audit: not yet performed.
