# Self-review

## Correctness — PASS

The claim fixes the full index set \(K=\{0,s,2s\}\), \(L=2\mathbb Z_N\), normalized flat-amplitude windows and a nondegenerate step of order at least three. Direct summation of the subgroup characters gives exactly \(p\) two-by-two Hermitian blocks; their eigenvalues yield all frame bounds, including the boundary case of singular systems. A three-term vanishing relation along every step orbit forces period three and two equilateral orientations. For even step order, the half-period involution lies inside each orbit and contradicts the nonreal equilateral triple. For odd step order divisible by three, antipodal coset pairing supplies every solution. The exact \(q\)-phase count follows from independent root-of-unity orientations and \(p\) independent phase lifts. No finite enumeration is used as proof of a universal statement. `CHECK.py` independently constructs the full frame matrix and verifies representative cases and small exact counts.

## Originality — PASS relative to inspected evidence

The closest paper, Asipchuk–De Carli–Rodriguez (arXiv:2605.16139v2), proves broad block-equivalence and provides the general matrix factorization in Lemma 3.1. Its Theorems 1.1 and 1.3 and the inspected structural/cyclotomic sections do not give the phase-only three-translation step-order classification or \(q\)-alphabet counts. Magsino (arXiv:1611.00818) develops general subgroup ambiguity-function tightness criteria and examples from CAZAC sequences, but the sections inspected do not state the order-three orbit/antipodal obstruction or its complete enumeration. The abstract general tests are acknowledged as prior; only the explicit arithmetic existence, full phase classification, discrete count and associated specialized spectrum are asserted here. Searches for equivalent names, stronger coverage and tables were made; a negative search is not a uniqueness certificate. Residual risk includes specialized older filter-bank and polyphase literature under a different parametrization.

## Mathematical value — PASS

The first strictly redundant case beyond two-translation critical systems, three translations with half of the modulation characters, has density \(3/2\). Exact tightness matters because the canonical reconstruction then has a scalar frame operator. The finding identifies the precise allowable translation arithmetic, shows binary phases are intrinsically insufficient regardless of dimension, proves ternary phases are enough whenever tightness is possible, and counts all indexed alphabet-constrained designs. The full block spectrum also gives exact stability information outside the tight case. This is a complete classification of a natural design problem, not a single parameter experiment.

## Closest literature and limitations

The cited 2026 block-equivalence work treats arbitrary windows and subgroups structurally; the 2016 ambiguity-function paper provides general tightness tests. The present complete phase-only classification does not extend to nonconstant window amplitudes or other modulation subgroups. Generic filter-bank results and unexamined alternate terminology remain originality risks. The numerical checker corroborates the algebra but is not an infinite proof, and no independent mathematical review has been carried out.

Self-review: passed. Independent audit: not yet performed.
