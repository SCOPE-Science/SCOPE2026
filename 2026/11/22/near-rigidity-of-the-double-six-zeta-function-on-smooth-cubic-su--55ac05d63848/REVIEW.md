# Scientific review: double-six Frobenius near-rigidity

## Correctness
**PASS.** The statement concerns the full finite Galois set of 36 geometric unordered double-sixes on each smooth cubic surface, not the possibility of a particular ordered sixer descent. The standard 27-line divisor-class model and six simple root reflections reduce all characteristics to a fixed finite W(E6)-action. The standalone exact checker constructs all 72 sixers by zero intersections and validates their unique complementary partners, independently constructs the 36 double-sixes by a Weyl orbit, enumerates all 51,840 elements and 25 conjugacy classes, and checks the 24 distinct double-six orbit spectra and the unique collision. It independently computes the traces and invariant Picard ranks of that pair. The all-field theorem follows from the classical geometric identification; the finite computation is exhaustive in the relevant finite universe.

## Originality
**PASS, qualified.** Das (arXiv:2002.11183, Sections 1–3 and Tables 1, 3, 5) classifies Weyl types and obtains statistical distributions for markings but does not display the double-six cycle-spectrum inverse, its unique collision, or the extra one-rational-line resolution. Loughran–Trepalin (arXiv:1811.06785, Theorem 1.1) establishes occurrence of all relevant types. Elsenhans–Jahnel (2010, introduction and constructions) studies Galois-invariant double-sixes but not the 25-type finite-field spectral comparison. Complete accessible accounts of the Fermat-cubic sixer descent and of the integral double-six incidence lattice concern narrower or different claims. No equivalent result was found in the available research-record and literature searches. Residual risk: an older character/permutation table might encode the same collision implicitly.

## Mathematical value
**PASS.** Whether arithmetic splitting of a natural 36-point marking scheme detects the surface's full Weyl Frobenius type is a motivated geometric question, because invariant double-sixes encode descent data of blow-down structures and are central to cubic-surface arithmetic. The answer is an exact 24/25 near-rigidity theorem with a sharp, geometric obstruction: both exceptional types exist over all finite fields of order at least seven, yet differ in arithmetic Picard rank and rational-point count despite identical double-six zeta functions. The one-number repair is intrinsically informative, not an arbitrary field slice or a known table reproduction.

## Scope and residual risks
The result is a statement about the class of Frobenius in W(E6), not a classification of surface isomorphism types. Existing character-theory tables could contain an implicit equivalent statement. The authorship or independent external verification of the finite calculation is not asserted. The accompanying proof checker and certificate are part of the evidence; neither requires a computational algebra system.

Self-review: passed. Independent audit: not yet performed.
