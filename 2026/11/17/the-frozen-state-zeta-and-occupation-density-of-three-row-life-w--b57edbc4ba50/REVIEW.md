# Scientific review: three-row Life without Death fixed-state law

## Correctness — PASS

The local reduction is exact because a vacant site on a three-row Moore torus sees the populations of all three columns in its neighborhood, including the other two cells in its own column. This yields the precise condition that either the middle column is full or the triple total differs from three. The weighted closed-walk trace counts every indexed configuration once, including its binomial multiplicity and exact number of occupied sites. Integer symbolic determinant computation establishes the eleven-degree denominator. Explicit sixteen-state communication paths and a self-loop prove primitivity, while a positive integer Collatz–Wielandt vector gives an exact enclosing interval for the Perron root. Standard analytic perturbation then justifies the occupation-density limit.

The symbolic checker and a separately structured brute-force implementation of the original Moore update agree on every occupied-site histogram for circumferences three through seven. Brute force is a finite cross-check, not the source of the theorem for unbounded circumference. The exact polynomial and eigenvalue interval are calculated by self-contained source files included with the finding (SymPy is the declared library dependency).

## Originality — PASS, qualified

The 1987 Toffoli–Margolus book identifies the rule under its earlier name Inkspot, but its relevant pages were not available for direct inspection. The complete inspected Griffeath–Moore 1996 treatment develops circuit simulation and planar ladder dynamics, not the finite three-row weighted fixed-state zeta. The original Gravner–Griffeath 1998 survey's relevant section addresses finite-seed growth and fixation, with no corresponding three-row population formula in the inspected material. Eppstein's 2009 account gives a faster ladder, not stationary-state enumeration. Published research on fixed states of three-row majority, cyclic, Conway Life and HighLife models addresses different update rules; a subset relation for Life fixed states cannot give the full Life without Death count.

Literature searches included the full rule name, Inkspot alias, birth/survival code, three-row torus, frozen/still-life terms, transfer matrix, the first three computed counts, and equivalent growth entropy descriptions. No source with an equivalent or stronger exact statement was identified. This is evidence of noncoverage among the consulted sources, not proof of global priority. The unread original book pages and unindexed historical computations remain material residual risks.

## Mathematical value — PASS

The frozen-state ensemble is the natural terminal-state object of a monotone but computationally complex planar rule. The result classifies all finite-width stationary configurations by total occupancy for **every circumference**, rather than sampling small strips, and evaluates both its exponential entropy and its typical occupation density. A three-row neighborhood simplification exposes a non-obvious sixteen-state exact model and eleven-degree spectral law. Its conclusions are not implied by the standard observation that a finite monotone automaton eventually freezes, nor by the existing stationary spectrum of Conway Life.

## Scope and limitations

The claim does not concern infinite-plane growth, arbitrary strip height, entrance basins, or precise maximum stabilization times. The asymptotic numerical figures approximate exact algebraic expressions. First supporting public exposition of the rule is traced to the MIT Press 1987 edition; the complete text of the cited original pages could not be inspected. No external independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
