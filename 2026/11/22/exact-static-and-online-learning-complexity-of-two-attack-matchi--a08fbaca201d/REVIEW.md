# Scientific review

## Correctness: PASS

The proof establishes the stable-set/transversal equivalence exactly, classifies all jointly positive supports, supplies eight explicitly checked realizers for every three-query Boolean labeling, counts labeled paths, and excludes four-query shattering. The online upper bound analyzes every root-positive fiber and every potentially splitting second query. The direct-semantics enumerator independently confirms all cases through eight arguments (`VERIFY_OK 8`). This is a complete mathematical proof for arbitrary finite size, not an extrapolation from finite enumeration. Main boundary conditions: matching may be empty; two-edge pairs are disjoint and symmetric; the small orders require separate counts.

## Originality: PASS within inspected evidence

The closest 2026 paper of Malmqvist (https://doi.org/10.1093/logcom/exag049) is the directly motivating inverse learning problem and supplies general and sparse VC bounds rather than the complete two-edge matching shattering polynomial or the adaptive dimension in its accessible abstract. The 2019 full text of Niskanen, Wallner and Järvisalo (https://doi.org/10.1613/jair.1.11758) studies synthesis and stable consistency, not this hypothesis-class invariant. Mathematical-record searches also surfaced results on **fixed** degree-one graphs' maximal-independent-set membership classes, which swap the variable framework with the fixed graph and do not entail the current theorem. A primary full-text comparison of Malmqvist's 2026 paper was blocked by access restrictions, and historical novelty is therefore provisional; no independence or exhaustive historical exclusion is asserted.

## Value: PASS

The first nontrivial two-conflict model for learning sparse symmetric attack relations permits a complete enumeration of shatterable query sets, not just a VC upper bound. The surprising four-vertex-path characterization and static/adaptive equality quantify precisely how much adaptivity helps in this natural restricted inference model (namely, not at all). The sharp five-argument threshold and all-size polynomial provide reproducible baselines for denser and asymmetric generalizations, without claiming those generalizations are established.

## Residual scientific limits

The model varies the attack graph on a fixed labeled argument universe; it does not describe VC dimension of extensions in one fixed graph. Full 2026 motivating article was not obtained lawfully. Other synonymous formulations in prior publications might cover the exact classification.

Self-review: passed. Independent audit: not yet performed.
