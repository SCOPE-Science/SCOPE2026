# Scientific review: sharp target-sensitive antichain bounds for Heyting-valued modal certificates

## Correctness

PASS. The main local lemma uses Birkhoff's downset representation: the complement of a target downset is an upset, hence its minimal elements each require at most one witness. Choosing the complement of the principal upset at every such minimal element makes all those witnesses indispensable. The coordinatewise union and the depth-induction constructions preserve the claimed exact values, and the sharp star tests use the source language's crisp \(T_m\) connective. The stand-alone checker verifies local inequalities and sharp families, including all two-coordinate star profiles over generated four-element posets. Finite tests support but do not replace the unrestricted mathematical proof.

## Originality

PASS on inspected evidence with residual historical risk. The closest direct source is Das, Ray and Mali, arXiv:2608.05550v1, Section 5. It proves a height-based upper bound and a certificate construction, but does not state the exact target-dependent number or the simultaneous sharp lower-bound star construction. Birkhoff representation and general meet breadth are classical: neither is presented as a standalone novel discovery. The contribution is the exact target profile and its logical optimality in the modal certificate setting. Searches of published mathematical findings and targeted literature found no equivalent or stronger full statement, but a search is not proof of novelty; older technical literature may contain an equivalent adaptation.

## Value

PASS. The result replaces a uniform height bound by a provably optimal local invariant, quantifies the jointly required successor information for multiple boxes, and yields an unbounded improvement on high finite chains. The one-step lower bound demonstrates that this invariant is a necessary certificate resource, not merely a convenient estimate. These statements are useful for constructing and sizing exact-value model-checking certificates.

## Boundaries and closest work

The sharpness pertains to pruning a pointed model while retaining valuations. The work does not claim minimal arbitrary model sizes or extend to fuzzy accessibility. Relevant literature includes Das–Ray–Mali (2026), Fitting (1991), classical finite distributive-lattice representation, and Kurz–Poiger–Teheux (2024). An independent historical-priority review has not been performed.

Self-review: passed. Independent audit: not yet performed.
