# Self-review

## Correctness
PASS. The complete claim was checked from the explicit generator, Cayley–Hamilton reduction, entry formulas, positive two-jump coefficient, sharp rate ordering, elimination resultant, positive/negative Bernstein certificates, and the monotonicity/concavity inequalities. `verify.py` was run on the supplied source, returning 1,728 exact general triple comparisons, 30 family cases and symbolic identities. Finite checks support the analytic proof, not replace it.

## Originality
PASS, subject to specialist historical priority risk. Full published-finding corpus published claims for the homogeneous three-cycle and heterogeneous cycles of size at least five were inspected. The former only gives the equal-rate case, the latter needs the n≥5 no-wrap argument. Horváth–Song–Terlaky gives root algorithms and valid general sufficiency bounds, not this two-inequality reduction and sextic rate-bias mechanism switch. Nüßlein–Ranocha–Ketcheson considers adaptive weights; Blanes–Iserles–Macnamara develops alternative positivity methods. The published equal-rate cutoff is credited, not reclamed. A previously overlooked exact three-state formula remains a risk.

## Value
PASS. Under heterogeneous reaction rates, the completed RK4 step can lose validity through either a negative fast-state staying probability or a negative direct jump. Identifying which happens first using a single algebraic crossover is an actionable, sharp positive-step selection rule for a minimal cyclic CTMC. The more general rate-order reduction gives a direct necessary-and-sufficient test without searching nine matrix entries.

## Scope and limitations
The closed horizon is for rates proportional to `(1,1,r)` with `0<r<=1`; outside this subfamily an exact two-inequality membership test is established but a globally connected positivity interval is not claimed. No claims are made for internal stages, time-varying rates, larger cycles or external audit.

Self-review: passed. Independent audit: not yet performed.
