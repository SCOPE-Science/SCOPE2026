# Scientific assessment: cyclic Rule 110 worst-case inverse branching

## Correctness — PASS

The claim has a complete all-length proof, not just an extrapolated enumeration. The four-pair-state labeled adjacency matrices implement the exact local rule, and cyclic closed walks count indexed predecessors. The all-one count is the Perrin trace. For outputs containing zero, the derived two-state transfer matrices have a three-term recurrence. A finite collection of 19 exact integer matrix comparisons, combined with a bivariate recurrence, proves the transfer-merging inequality for every pair of positive gaps except one oriented pair; cyclic factor order always admits a nonexceptional merger. The resulting bound is strictly below the all-one trace for all sizes at least five. The explicit exceptional small rings are checked independently. Reproduction programs use exact integers; one constructs the certificate and the other directly enumerates all inputs through length eighteen. Risk: the all-length conclusion depends on correct cyclic-edge labeling and the stated positive-gap reduction, both reconstructed in the proof and replayed against direct enumeration.

## Originality — PASS, with historical risk

Powley's 2009 thesis, Chapter 9, Theorem 9.5 and Example 9.2, treats homogeneous Rule 110 predecessors and gives the standard trace calculation. The exact Perrin recurrence for the all-one output is therefore an implication of established methods and is not the novelty claim. The inspected Wikibooks Rule 110 article explicitly lists the same two labeled preimage matrices and examples of periodic outputs. The new claim is their global comparison: among *every* indexed cyclic output, the all-one output uniquely maximizes one-step inverse degree for every size at least five, proved by the exceptional-pair merging lemma. Searches for maximal preimage degree, in-degree, Perrin recurrence, homogeneous-vs-heterogeneous comparisons and cyclic Rule 110 uncovered no statement settling this all-output equality case. Limitation: obscure archived computations and unindexed literature could have anticipated the theorem; no independent priority audit has been performed.

## Value — PASS

Worst-case inverse branching is a natural invariant for reconstructing an earlier configuration of a deterministic cellular automaton from one observed time slice. Rule 110 is the canonical computationally universal elementary rule, so its sharp, all-length inverse ambiguity and unique extremizing output are substantively motivated. The theorem provides an exact Perrin growth law plus a global equality classification, strengthening available homogeneous-output counts rather than merely applying the same transfer formula to a special sample. It also introduces an explicit small-state inequality that can be checked and potentially adapted to constrained inverse-branching questions. Limitation: this is a one-step finite-ring result and makes no multistep or universal dynamics claim.

## Closest literature and limitations

- Edward J. Powley, *Global properties of cellular automata*, 2009, Chapter 9, sections 9.1–9.3: exact homogeneous and periodic preimage methods, without the inspected all-output maximum theorem.
- *Cellular Automata/Examples on Rule 110*, Wikibooks: the same de Bruijn matrices, concrete background preimage counts and cyclic examples, but no global maximizer theorem in the inspected text.
- Harold V. McIntosh, *A Concordance for Rule 110*, June 4, 2000: periodic motif/glider context, not the inverse-degree comparison.

Self-review: passed. Independent audit: not yet performed.
