# Scientific assessment

## Correctness — PASS

The proof establishes a necessary-and-sufficient encoding condition for any two *distinct* one-deletion outputs. The main nonstandard step, that two distinct deletion outputs of one word jointly retain its complete symbol support, follows from the uniqueness of a deleted occurrence of a missing symbol. Consequently, all conflicts are confined to exact support classes. Every one of the seven finite support-class graphs has both a concrete independent set of size \(a\) and a vertex-disjoint matching of size \(v-a\). Matching upper bounds are valid even when the graph has additional edges: at most one endpoint of each matched edge may belong to an independent set. Exhaustive standalone verification reconstructs the graphs from deletion sets, checks both certificates, and tests the resulting polynomial identities. This gives a rigorous proof for every integer alphabet size rather than an extrapolation from tested values.

## Originality — PASS, with residual historical risk

The 2016 coded multiread reconstruction framework and the 2020 works on explicit two-read deletion codes and asymptotic optimality are acknowledged as prior art. A particularly close published record determines the number of forbidden pairs of the same \(q\)-ary single-deletion two-read graph, but does not state the independent-set optima at lengths three and four; edge count by itself cannot determine these optima. Published-record semantic queries for the two all-alphabet polynomial formulas, support-class components and short reconstruction codes, as well as comparison against accessible historical claim summaries, found no equivalent or stronger theorem. However, unindexed exact finite-length coding results or a previously unnoticed deduction from a more general theorem could preempt priority. This qualification is not a claim of exhaustive worldwide novelty certification.

## Value — PASS

The model asks for the largest message set recoverable when two *different* one-deletion traces are available: a practical adversarial multiread alternative to classic single-trace correction. Exact capacities for the first two nontrivial lengths, for arbitrary alphabet size, characterize a concrete coding-theoretic limit. The support-separation principle and complementary matching/independent certificates explain why the answer is a uniform polynomial in alphabet size rather than an arbitrary extrapolated table. Neither correctness nor novelty alone is used as the value rationale.

## Relevant sources and limitations

- Sala, Gabrys, Schoeny and Dolecek, arXiv:1604.03000 (first posted 2016-04-11), coded trace reconstruction, principally insertions.
- Cai, Kiah, Nguyen and Yaakobi, arXiv:2001.01376, definitions and explicit \(q\)-ary two-read single-deletion codes.
- Chrisnata, Kiah and Yaakobi, arXiv:2004.06032, asymptotic optimality for binary two-read deletion reconstruction.
- Related published record: *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph* (record `737fed325e91`), same conflict graph but different invariant.

The result is confined to lengths three and four; no general-all-length optimum or performance for identical reads is claimed. The independent verification status remains unperformed.

Self-review: passed. Independent audit: not yet performed.
