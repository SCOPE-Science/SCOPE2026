# Scientific review: exact pure-branch limit retractions

## Correctness — PASS

The shape domain, both child maps, sorting walls and tie conventions are explicit. The argument gives a finite partition of the entire positive shape triangle and proves that all left paths enter the stable left chamber in no more than two steps and all right paths enter the stable right chamber in no more than one step. Within each chamber, one *physical angle* is invariant, the other two retain a constant sum, and the largest angle obeys the exact affine recurrence \(a_{n+1}=S-a_n/2\). Its solution yields the claimed coordinates, retraction formulas and oscillatory \((-1/2)^n\) error. Both finite-entry bounds and the geometric rate have explicit positive-angle witnesses; no limit argument requires a degenerate triangle. The independent sorted-triple implementation in `verify.py` passed 743 exact-rational starting shapes and iterates up to depth 12. These finite checks support but do not substitute for the algebraic proof.

## Originality — PASS within examined evidence

J. Michaud, arXiv:2611.06492v1 (November 4, 2026), Proposition 1 gives the same piecewise maps, Proposition 3 gives their fixed segments, and Proposition 7 proves convergence in *distance to the segment*. It does not identify the exact point of convergence, show finite-time stable-chamber entry, give four- and two-chamber piecewise-rational limit retractions, or the \(1/2\) oscillatory rate. This result is a strict pointwise and quantitative strengthening, rather than a restatement of segment attraction. The full relevant sections of the primary paper were inspected. Ismailescu et al., arXiv:1908.02749, treat geometric regularity, while Michaud–Korotov, arXiv:2607.25457, analyze largest-angle \(n\)-section regularity. The closest public related mathematical result, *Sharp mixed-child contraction and exponential shape concentration for largest-angle bisection* (November 8, 2026), was examined in full: it proves a sharp \(3/4\) bound for mixed \(LR/RL\) blocks and random-tree shape concentration, not the pure-branch projection or rate. published-finding corpus semantic searches for pure-branch limits, projections and exact rates found no stronger coverage. Residual priority risk: other historical treatments of projective angle-refinement maps not indexed in those sources.

## Mathematical value — PASS

Exceptional eventually pure branches are exactly the obstruction to universal right-isosceles convergence in the motivating dynamical classification. Their limiting geometry is therefore an intrinsic invariant, not an arbitrary parameter slice: the theorem gives the complete exact endpoint from *every* initial similarity class, a finite symbolic chamber classification, and the sharp rate with alternating sign. It turns qualitative attraction to a one-dimensional continuum into a computable point-selection mechanism, and determines every eventually constant itinerary by evaluating its finite prefix. This is a natural complete classification of an outstanding exceptional dynamical regime, rather than a routine special numerical example.

## Closest results and scientific limits

No novel assertion is made about mixed itineraries, random-tree convergence or geometric mesh diameter shrinkage. The sharp factor holds after the specified finite transients, not as a global one-step contraction. All literature coverage is subject to residual historical-priority uncertainty, and no independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
