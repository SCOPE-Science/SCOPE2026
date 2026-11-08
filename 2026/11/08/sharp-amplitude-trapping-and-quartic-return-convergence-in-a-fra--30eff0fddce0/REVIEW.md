# Review of the fractional kinetic amplitude-trapping theorem

## Correctness
The claim is established by exact differentiation and an elementary but global radius comparison. The derivative \(g_a'>0\) proves uniqueness of any prime-two orbit; the strict concavity \(g_a''<0\) makes the endpoint slope condition both necessary and sufficient for invariant trapping on \([0,R]\). All trajectories within the trapped interval increase toward \(R\), and the amplitude of an exterior trajectory decreases until it either enters the trapped interval or converges to the same boundary; at the critical parameter an exterior trajectory necessarily crosses below it. The vanishing derivative and nonzero second derivative at the boundary yield a nonzero quartic coefficient for the two-step return. Finite exception sets at each depth are accounted for. The companion checker passed and does not replace the infinite proof.

## Originality
The source arXiv:2610.27321 proves a general local period-two stability criterion and reports empirical attraction. The older arXiv:2204.11326 already establishes almost-everywhere convergence of scalar gradient descent for symmetric strictly subquadratic losses. Thus **neither the mere existence of a stable cycle nor generic global convergence is claimed as original**. The result instead supplies a precise two-parameter **one-step amplitude-trapping if-and-only-if**, its global monotone capture at the sharp boundary, the threshold exponent \(1/4\), and a computed nonzero order-four return law. No covering statement was found in the inspected full texts or targeted searches. Priority outside that inspected literature remains a risk.

## Mathematical value
The no-overshoot region is a natural global basin-geometry property not determined by local Floquet stability; a locally stable two-cycle exists on both sides of the frontier. The exponent criterion identifies which regularized kinetic maps retain monotone-amplitude capture at every stepsize. At a nontrivial finite tuning the same barrier becomes an exact globally accessible fourth-order return, supplying both a structural boundary and a mathematically motivated fast-convergence regime. The claim is deliberately restricted to this dynamical invariant and does not extrapolate to realistic momentum optimizers.

## Remaining scientific limits
No statement of basin geometry outside the trapping regime beyond local oscillatory approach; no multidimensional coupling; no independence or final historical priority certificate.

Self-review: passed. Independent audit: not yet performed.
