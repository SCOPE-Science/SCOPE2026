# Review of the circular full-shadow threshold theorem

## Correctness (C): PASS

The indexed-deletion definition and oriented necklace quotient are explicit. The upper bound is the number of masks. Every repeated symbol at cyclic distance at most \(t\) produces two different deletion masks with identical output by deleting the intervening arc and exchanging its equal endpoints; the extension of these masks is valid whenever \(n\ge t+1\). At lengths \(n\le2t+1\), every equal pair has such an arc. Sufficiency uses unique markers to orient each output and a period-\(t+1\) data block to rule out any two linear \(r\)-deletion embeddings for \(r\le t\). The decoded package contains an executable independent exhaustive check, and finite tests do not replace the proof.

## Originality (O): PASS against inspected evidence

The closest cyclic source reconstruction study [1] distinguishes binary sources from collections of scattered cyclic subwords; it does not enumerate **indexed deletion-mask** fibers for a fixed source. Circular trace statistics [2] concern sample complexity under random deletions and shifts; they do not imply full support of cardinality \(\binom nt\) or the sharp uniform alphabet. The nonbinary linear deletion-ball theorem [3] lacks quotient-by-rotation and unique-marker anchoring. The published permutation-power calculation [4] treats deletion-mask orbits in periodic sources and explicitly has additional orbit identifications, whereas the new proof realizes all original masks. The binary one-deletion theorem [5] neither covers \(t\ge2\) nor nonbinary source threshold; the separate one-deletion case is not claimed here.

Residual risks: a previously unindexed equivalent general marker construction or a stronger all-mask theorem elsewhere could subsume this result. The available published text and relevant searchable records do not reveal such coverage; this search is not a proof of universal priority.

## Mathematical value (V): PASS

The problem measures whether the origin-free circular deletion readout loses any information about **which subset of positions was deleted**, a natural extreme of channel ambiguity. A sharp and uniform alphabet threshold across all deletion counts is a structural invariant of this channel, and the first length at which a repeated-symbol source can nevertheless attain the full information-theoretic mask count is determined exactly. This extends beyond the known linear sphere count and treats a genuine obstacle from cyclic rotation; no downstream coding-capacity claim is inferred.

## Limitations

The theorem proves existence and short-length rigidity. It does not determine all optimizers or pointwise minimum alphabets for arbitrary longer lengths, nor code size and sample complexity. Computational checks cover only their stated ranges. Literature comparison has residual priority risk.

Self-review: passed. Independent audit: not yet performed.
