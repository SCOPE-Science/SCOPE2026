# Scientific review

## Correctness

**PASS.** Every point query divides the full family into exactly \(\ell\) and \(n-\ell\) hypotheses; the full-binary-tree leaf-count upper bound is exact because consecutive start blocks admit arbitrary prefix cuts. The constructive tree covers both answer branches and all edge cases \(1\le\ell<n\). Finite first-order expressibility of a fixed tree and Łoś's theorem prove the ultraproduct boundary; the general stability/2-rank equivalence is from Chase and Freitag (2018). An independent exhaustive recursive checker of small finite cases and constructive witnesses for larger cases corroborates the proof; it is not substituted for it.

## Originality

**PASS, qualified by historical-priority risk.** The exact all-width online-rank equation and its bounded-width ultraproduct stability transition were not found in the inspected primary texts or semantic comparison results. Chase and Freitag (2018) give the general model-theoretic equivalence; Filmus et al. (2023) give broad prediction results; Chase, Freitag and Reyzin (2023/2024) discuss general query/compression results and a distinct disjoint-interval example. A pre-existing four-point translate theorem includes the special case \(\ell=4\) in sufficiently large cycles. A general translate-family pair-count formula already implies the static degree-two coefficient. These covered parts are contextual, not the proposed new result. The main remaining originality risk is an unindexed exact sliding-window rank theorem under alternative terminology.

## Value

**PASS.** Fixed-cardinality cyclic window systems are canonical finite interpretable incidence families. The theorem computes their sharp deterministic online mistake bound for every cycle length and width and identifies an exact finite-to-infinite stability transition. It quantifies a genuine static/adaptive separation: VC dimension stays at most two while online dimension can grow arbitrarily; fixed minority width also keeps the online dimension bounded even as the hypothesis population grows without bound. The result is a complete natural two-parameter classification, not a computation of an arbitrary isolated instance.

## Scope and remaining checks

This review concerns the deterministic realizable membership setting and stability of the window-incidence formula only. It does not certify priority against every historical terminology variant or derive randomized dimensions. Computational checks are finite corroboration; the universal argument is in the proof. No external scientific review or independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
