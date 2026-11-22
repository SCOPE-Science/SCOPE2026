# Scientific review: individual equation essentiality at the first three-color Schur obstruction

## Correctness — PASS

The domain consists of all 49 unordered-summand positive additive equations with sum at most 14. The incrementally checked enumeration safely discards partial colorings only after two monochromatic equations, while the bitmask enumeration independently visits every one of the 1,594,323 normalized colorings. Both check 49/49 per-equation counts against a fully embedded CSV. They find no defect-free coloring, exactly 1350 normalized one-defect colorings and 29 individually essential equations. A separate verifier enumerates the six normalized valid colorings of [1,13] and checks the fixed classes and two sum-14 violations for each color choice. Count normalization and repeated-summand conventions are explicit.

## Originality — PASS, with identified uncertainty

The known Schur threshold and the [1,13] color-class rigidity are credited. Thanatipanonda's arXiv:0801.0798, Section 4, is a close primary source on monochromatic triples but proves asymptotic bounds and does not present the 14-integer per-equation deletion table. Kisner 2013 classifies the defect-free [1,13] states and thereby motivates the seven-new-equation observation; the 29/49 quantitative essentiality census and 4050 named near-defect states do not follow from that classification alone. Chappelon et al. 2013 address modular Schur numbers. Indexed findings on rainbow Schur fractions, developed group sum-free families and other three-color systems were compared by their mathematical statements. An unindexed SAT benchmark or other unpublished exhaustive table remains a residual priority risk.

## Value — PASS

The first three-color Schur obstruction is a canonical finite Ramsey instance. Exact deletion sensitivity is a natural minimal-unsatisfiability invariant: it distinguishes 29 equations whose individual removal is decisive from 20 whose removal leaves the instance unsatisfiable. The separate redundancy of all seven new endpoint equations, proved through rigid color classes, is a structural contrast not conveyed by the classical threshold alone. The exact 49-row multiplicity census can benchmark constraint minimization and robustness studies without requiring any conjectural infinite extension.

## Limits

Three named colors, integers 1 through 14, and deletion of one equation only. Computational exhaustion is finite, explicit and independently rerunnable; no claim about larger instances or certified publication priority is made.

Self-review: passed. Independent audit: not yet performed.
