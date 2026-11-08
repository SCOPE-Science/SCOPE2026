# Scientific review: externally supported independence of circular ladders

## Correctness — PASS
The admissible seven-column words encode precisely the ESI sets for cycles of length at least seven. The closed-walk transfer has a single cyclic component of 117 states and 241 arcs. An explicitly constructible integral potential makes the cost \(2-3w\) nonnegative after telescoping. Every coefficient of the degree-117 characteristic determinant is computed by exact Newton identities modulo deficit degree five. The resulting formal trace identity proves the maximizing-size and multiplicity formulas for all lengths, while independent direct graph enumeration handles lengths three through six. In `verify.py`, the final determinant support and independent graph enumerations through length eleven are compared exactly. This is a finite algebraic lemma plus a mathematical proof of its consequences, not an infinite inference from sampled sizes.

## Originality — PASS, with historical-priority limits
Božović, Peterin, Roux and Tepeh, *On externally supported independence number of graphs* (arXiv:2606.22972v1, 2026-06-22), supply the invariant and a general cubic upper bound. The inspected full manuscript also supplies other exact families but not a prism enumeration. The present theorem proves two infinitely recurrent strict-deficit classes, exact multiplicities for all six classes and the full transfer polynomial. The potential competing Cartesian-prism reference *Isolation number: Cartesian and lexicographic products and generalized Sierpiński graphs* (arXiv:2508.16338v1) studies a distinct minimum-isolation invariant; only its abstract was accessible, so broader unpublished equivalences remain a residual risk. Related circular-ladder homology and three-cut-complex records concern different mathematical objects. Searches alone cannot certify absolute priority.

## Mathematical value — PASS
Prisms are a natural connected cubic Cartesian-product family, and the sharp ESI value and counts are not implied by the paper's general cubic upper bound. The residue law exposes genuine lost attainability at \(n\equiv3,5\pmod6\), while the number of optimum sets alternates between constant, linear, quadratic and cubic growth. The complete cardinality polynomial provides an infinite-family enumerator. These are concrete motivated structural facts, not a textbook rearrangement.

## Scope and risk
All counts concern labelled vertex subsets of ordinary \(C_n\square K_2\) with \(n\ge3\). Full polynomials are represented as exact finite traces rather than simplified coefficient lists. An accessible abstract is not whole-text noncoverage; priority remains qualified. The exact finite certificate has been reproduced but no independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
