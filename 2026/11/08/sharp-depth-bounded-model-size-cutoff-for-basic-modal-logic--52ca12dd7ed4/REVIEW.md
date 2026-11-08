# Scientific review

## Correctness — PASS

For every target complete depth-\(d\) type, the construction places all depth-\((d-1)\) types as labelled nodes, chooses the root by truncation of the target, and gives nonroot nodes successor sections realizing their own labels. The depth-induction verifies the labels while the root sees precisely its target successor set. Pairwise incompatible characteristic formulas force at least one world for each requested predecessor type, proving optimality. A stand-alone semantic checker verifies all 66,142 types of seven small parameter settings and an additional 200 sampled high-depth instances, totaling 66,342. The finite observations are corroboration, not an infinite certificate.

## Originality — PASS within inspected evidence

Lück (2019), Section 4 (primary full text inspected), gives **exactly the same recurrence** for the count of modal depth types (Proposition 4.7) and a canonical model realizing every rank-\(d\) type at once (Lemma 4.8). This is a particularly close precursor. It does not state the sharp **per-formula** model-size optimum one level below the type count; the proof here supplies a compatible single-carrier section construction and matching lower bound. An unindexed corollary or independently-known optimization remains an explicit priority risk. The inspected 2007 shallow-model full text has a formula-subexpression-dependent bound, not the exact uniform cutoff as a function of letters and depth. The inspected full open-access 2025 article uses standard finite-depth Hintikka formulas but does not give the proved sharp world count. The 2026 motivating study is a finite-corpus computation, not a claim of the uniform theorem, according to the available dated abstract and technical overview. Searches for exact bounds, cyclic reuse, and n-type model compression did not find the statement. An old unindexed equivalent or the inaccessible recent full text is a residual priority risk.

## Value — PASS

The theorem identifies the least world budget that suffices for **every** satisfiable formula at fixed modal depth and vocabulary, independent of length. Its optimal tower-height cutoff and reuse construction reveal a meaningful distinction between formula-dependent filtration / finite-tree bounds and fixed-resource model synthesis. It immediately determines a stopping size for exhaustive finite-frame tests of this natural fragment. These exact cutoffs are not presented as a general algorithmic speedup.

## Scope and caveats

Arbitrary Boolean unimodal Kripke frames only, including cycles and self-loops; no transfer to transitive or irreflexive frame classes. No assertion that the priority check exhausts specialist literature, and no independent expert verification.

Self-review: passed. Independent audit: not yet performed.
