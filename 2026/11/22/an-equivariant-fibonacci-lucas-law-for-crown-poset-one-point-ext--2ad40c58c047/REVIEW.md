# Review of the dihedral crown-poset one-point-type character

## Correctness — PASS

The proof correctly separates one-sided ideal/filter patterns from exactly \(4n\) mixed types, then computes the fixed ideals under rotations and reflections with the explicit transfer matrix \(T\). A reflection fixes precisely two mixed types, so the character is \(2F_{n+3}+1\) for every reflection. The divisor expression follows from the exact group action by Burnside's lemma. Every quantified assertion is for \(n\ge5\), and the generic-stabilizer asymptotic is bounded using all nonidentity group elements. Reproduction instructions and a standard-library checker are supplied; exhaustive tests for five through nine crown indices support but do not replace the proof.

## Originality — PASS within inspected literature

The closest fully read source, *Uniform cyclic-incidence one-type spectra and a sharp algebraic growth law* (2026), supplies the unquotiented type count but explicitly does not quotient under rotations. The classic Munarini–Zagaglia Salvi crown-ideal work supplies the Lucas count and rank polynomials, not an inspected equivariant character. A published incidence-algebra crown rotation result concerns commuting idempotents and cannot be substituted for the type action. The accessible earlier standard-example-poset orbit result concerns a different comparability pattern and larger symmetric group. The new claim is the complete fixed-point character and base-automorphism orbit classification, not the prior scalar type count or ideal recurrence. Search terms, source comparisons, exact prior IDs and remaining historical uncertainties appear in `AUDIT.json`.

## Value — PASS

Classifying one-point extensions modulo the finite base's automorphism group is a natural complement to labelled one-type counting. The uniform reflection phenomenon, exact totient–Lucas/Fibonacci orbit expression, and exponentially generic trivial stabilizer are structural facts not provided by a scalar type total. Together they give a complete symmetry-sensitive answer for the cyclic crown family.

## Closest literature and limits

The motivating first-public source is Kwiatkowska–Sullivan–Winkel, arXiv:2502.16695 (23 February 2025). The 2002 crown rank-polynomial article was reviewed through its abstract and detailed published summary, not its full inaccessible text; this remains a specific historical-priority risk. No external mathematical audit or independent priority certification has been performed. The claim is limited to nonalgebraic unary extensions for \(n\ge5\).

Self-review: passed. Independent audit: not yet performed.
