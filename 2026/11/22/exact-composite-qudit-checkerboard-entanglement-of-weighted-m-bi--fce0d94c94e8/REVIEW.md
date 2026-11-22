# Self-review

## Correctness — PASS
The graph is bipartite precisely in the stated odd half-circumference regime. Multiplying the explicit physical cross-cut matrix by an integral cyclic shift reduces it to the quadratic circulant \(T^2+wT+I\). Because the quadratic is monic, the cyclic cokernel reduces over the **integers** to the rank-two companion power \(C_w^n-I\); taking its entry gcd and determinant yields the complete Smith invariants, including zero factors. Additive-character orthogonality then gives \(d^n/[\gcd(d,g)\gcd(d,h)]\) equal positive reduced-density eigenvalues for **all** integer \(d\ge2\). No step assumes that \(d\) is a field. The independently constructed exact Smith test runs 104 parameters; a second program checks modular images and direct reduced-density spectra, with all tests passing. Finite checks are not the infinite proof.

## Originality — PASS on examined evidence, with residual historical uncertainty
Hein–Eisert–Briegel (2003) give general graph-state entanglement tools; Looi–Yu–Gheorghiu–Griffiths (2007) introduce general-dimension qudit graph-state constructions; Helwig (2013) develops qudit cut-entanglement techniques; Telloni–Williams (2014) study a different class of polynomial circulant Smith calculations. These are credited rather than claimed as new. The nearest checked research record concerns prime-qudit **generalized Petersen** graphs and a different alternating-layer cut; its full text was not accessible, so the evidence consists of its publicly available detailed summary and an explicit graph-family implication comparison. A general Smith-method reference need not imply that this family has already been computed. No inspected work states the all-odd-length weighted Möbius-ladder integer recurrence and composite-qudit Schmidt formula. Unindexed equivalent prior calculations remain possible.

## Mathematical value — PASS
The exact natural invariant is the bipartite entanglement spectrum, not an arbitrary tabulation. The theorem replaces a growing integral Smith problem with one fixed two-dimensional recurrence, covers every composite local dimension, and produces sharp physically interpretable phase-weight resonances, including exceptional unit-weight divisibility by three and the unipotent rung-weight boundary. The exact whole-family formula is substantively more informative than computing a few small graph-state instances.

## Scientific limitations
Only odd half-circumference, the parity bipartition, pure weighted graph states, and integer-controlled-phase interactions are covered. The result does not show all-cut AME, noise robustness, or dynamic transfer. Independent scientific audit and definitive historical-priority confirmation are not asserted. The nearest neighboring published record was available only at the detailed-summary level.

Self-review: passed. Independent audit: not yet performed.
