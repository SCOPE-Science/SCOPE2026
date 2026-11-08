# Review of the modal cycle-spectrum theorem

## Correctness — PASS

The proof is a direct finite-depth unrolling argument followed by bounded-morphism closure, an explicit defining formula with independent letters, the standard labelled-permutation exponential formula, and matching coefficient bounds. The quantifiers range over all ordinary basic modal formulas, all positive cycle lengths and all uniform labelled permutation sizes. The critical condition for the lower bound is \(1\in A\), which follows from nonempty divisor closure. The independent-letter disjunction is valid on a length-\(k\) cycle exactly if \(k\) divides at least one selected length. The checker gives finite corroboration, not an infinite proof.

## Originality — PASS within available evidence

The 2026 cyclic-program literature uses a more expressive loop language to study finite satisfiability, not spectra of ordinary one-modality formulas on bijections. Published probability literature already studies restricted permutations and supplies strong asymptotics, but does not connect their allowable lengths to exact basic modal frame-validity spectra and optimal modal depth in the inspected passages. Literature on all-relation random frames, transitive frames and general zero-one laws does not subsume the new one-successor bijective statement. In the same uniform-permutation model, Müller–Skerman–Verstraaten (2023) review Compton's first-order convergence-but-not-zero-one theorem for one bijection; our zero-one claim concerns a different and strictly specified class of universal-valuation modal frame-validity assertions. No directly covering result appeared in the actual topical searches and accessible own claims. Remaining risk: an older modal-logical characterization of valid finite-cycle spectra, or an equivalent finite-algebraic formulation, may have been missed. No claim of priority certainty is made.

## Value — PASS

Cycles are the elementary obstruction behind many finite modal-model arguments, and this result states precisely which cycle restrictions the basic modality can enforce by **frame validity** without a loop operator. It establishes the exact optimal depth required to define each allowable spectrum and a complete sharp family of asymptotic decay exponents for the corresponding uniform finite frames. This is a natural complete classification, not an arbitrary numerical slice; its probability formulas are transparently identified as classical enumerative consequences rather than independent combinatorial inventions.

## Scope and reproducibility

The theorem concerns basic modal frame validity, not validity with a fixed valuation or arbitrary relational frames. The code performs finite checks through eight permutation points. The asymptotic coefficient error follows from positive-coefficient bounds and Stirling, not experiments. The strongest related literature remains the general restricted-cycle results of Benaych-Georges and bounded-morphism methods. An accessible full-text search was conducted for the motivating 2026 loop-PDL work, whereas the 2026 finite-model-property paper was inspected only at its abstract; an attempt to retrieve a historical PDF page image was unsuccessful. These access limits are residual originality risks, not inferred disproof.

Self-review: passed. Independent audit: not yet performed.
