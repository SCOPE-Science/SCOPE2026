# Scientific review

## Correctness

PASS. The matrix has determinant \(1/2\), hence is perfect over the stated fields. The first two idempotent equations have precisely the pairs \((0,0)\) and \((1,1)\). The remaining equations form an explicit two-state scalar recursion: zero gives roots zero or one, while the state \(1/4\) gives the unique root \(1/2\). This proves the complete list in every dimension, not merely in tested cases. The standard-library checker confirms the formulas by exact rational arithmetic and independent finite-field exhaustive searches.

## Originality

PASS, with residual priority risk. The motivating 2026 survey explicitly calls the cardinality problem open and says its known complex triangular constructions give at least \(n+1\) distinct idempotents. The present explicit family has exactly \(n\) for every \(n\ge3\). A separate 2026 paper proving existence of idempotents in perfect complex evolution algebras does not determine exact counts; a three-dimensional study concerns full support rather than the family of cardinalities. Searches for this count, its quadratic degeneracy mechanism, and the corresponding three-dimensional example found no equivalent assertion. The 2019 classification of three-dimensional evolution algebras could implicitly include an isomorphic instance, but does not imply the all-dimensions construction. Older quadratic-map or idempotent-scheme literature could still cover the fact implicitly; searches are not a proof of priority.

## Mathematical value

PASS. A natural, explicit count immediately below the \(n+1\) threshold of previously described triangular constructions is realized in **every** dimension. This fills an infinite family of instances of a current conjectural idempotent-cardinality spectrum, not an arbitrary one-off enumerative slice. The characteristic-independent formula and finite-field interpretation strengthen the result. It does not settle the unknown count two in dimensions above two.

## Closest work and limits

Kaygorodov--Martín González--Viruel, arXiv:2610.22248v1, Section 2.3, Conjecture 6, is the nearest explicit formulation. García-Martínez--Pérez-Rodríguez (2026), Section 3.3, establishes weaker existence. Hu (2026), Introduction and Corollary 3, addresses full support, not exact counts in arbitrary dimensions. The result assumes characteristic different from two and counts distinct elements, not scheme multiplicities. Historical priority and the proof merit independent assessment.

Self-review: passed. Independent audit: not yet performed.
