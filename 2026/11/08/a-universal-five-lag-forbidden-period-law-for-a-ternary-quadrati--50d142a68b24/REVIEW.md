# Self-review

## Correctness — PASS

The state map is bijective and admits a two-sided cyclic-word representation. A sum of the five row differences forces each five-row column to contain either zero or three nonzero symbols. A zero column forces the all-zero word. For nonzero columns, the five-step lemma exhausts all two-zero masks: a source must have separated zero positions while every target has adjacent zero positions. This contradiction is invariant under the single cyclic row rotation at the column seam. It proves the statement for every integer \(k\ge2\), including the \(k=2\) boundary. `verify.py` independently enumerates ten masks and all states for nine sample memory lengths.

## Originality — PASS, with residual historical uncertainty

The nearest primary source is Finch, arXiv:2610.34300v1, Proposition 7 and Theorem 8: the same permutation, but the exact fixed-point count there is at \(4k\), not \(5k\). Earlier related \(4d\)-period counts, for \(d\mid k\), also do not cover \(5k\). Three semantic searches and targeted literature searches located no direct equivalent. This does not establish uniqueness; an implicit earlier forbidden-period lemma is a real priority risk. The 1995 Cassaigne–Finch paper treats a ternary recurrence in an additive-sequence setting, but its accessible publisher abstract and partially garbled PDF did not permit a complete comparison.

## Value — PASS

The theorem completes a natural fixed-point count \(\#\operatorname{Fix}(T_k^{5k})\) uniformly in the memory length, directly contrasting the large \(\operatorname{Fix}(T_k^{4k})\) classes found in recent work. The elementary cyclic-zero transition lemma gives a structural reason for the sharp period exclusion; the conclusion is not merely a bounded enumeration or a rephrased fixed-point observation.

## Scope and limitations

The proof does not classify other period multipliers, all cycles, or the special-seed period. Historical-priority comparison remains nonexhaustive. Finite computation is corroborative and not an infinite proof. No independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
