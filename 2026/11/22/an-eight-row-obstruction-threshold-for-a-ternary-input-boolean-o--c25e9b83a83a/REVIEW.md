# Scientific review

## Correctness

PASS. The exact two-function normal form follows by moving all tuples selected by the first functional dependency to one side, leaving a single-output-per-intermediate-value requirement on the other side. Every mixed intermediate fibre forces one of the three input values to select it; four mixed fibres therefore give a universal failing eight-row subteam. In minimal failures there are no nonmixed fibres and no more than four mixed fibres. The complete remaining two- and three-fibre problem has 49 local states per fibre and is decided by the exhaustive `verify.py` certificate. It checks 292824 canonical configurations, gives a 4/6/7/8-size census, and independently checks 400 bounded direct partitions. The argument relies on exact finite reduction, not extrapolation from random tests.

## Originality

PASS within the checked record. The closest published paper (Fröhlich, Kolaitis and Meier, Theorem 25 of the 2026 CSL paper / arXiv:2508.16146) proves *unrestricted* incoherence and gives no sharp bound for three input values and two output values. Barlag et al. (arXiv:2605.31269, Sections 3 and 5) study general coherence, rewritability and decision complexity, not this finite-domain spectrum. The closest published restricted-alphabet research record handles only two first-coordinate values with arbitrary output values and proves sizes 4 and 6 with a six-row cutoff; that theorem does not imply the ternary-input Boolean-output 4/6/7/8 spectrum. Searches for chained dependencies, finite-domain coherence, ternary determinants and eight-tuple obstructions did not identify an equivalent or stronger result. The remaining risk is older literature on database repair or forbidden-subteam patterns using different terminology.

## Value

PASS. This supplies a sharp non-binary determinant case for a natural chained dependence split despite the unrestricted formula being incoherent. The exact threshold eight is a data-validation certificate size, the missing size five and present size seven distinguish the three-input case from the known two-input theorem, and the 306 canonical forbidden patterns furnish a finite obstruction basis for bounded-domain checking. The conclusion is a natural complete finite classification, not a routine numerical increment.

## Limitations

The result applies only to finite sets of distinct triples with at most three first-coordinate values and two output values, under ordinary lax team disjunction. Exhaustive state enumeration is computer-assisted and has not received independent verification. The record comparison cannot exclude uncatalogued older equivalent results.

Self-review: passed. Independent audit: not yet performed.
