# Scientific review

## Correctness — PASS

The proof treats all finite simple graphs of maximum degree two, including isolates and the empty graph, and fixes the unnormalized Boolean Fourier convention. A leaf-edge reversal pairs acyclic orientations with opposite singleton-leaf signs. For cycles, a two-state transfer trace counts all edge words, and subtracting the two constant directed cycles gives the exact signed measure. Rank-one factorization of unselected blocks produces the three-case multiplier formula; the integer recurrence bounds every nonzero trace away from the exceptional value two and exhibits a coefficient of \(-2\). Tensor products give exact extremal magnitudes and Hilbert condition numbers. `verify.py` passes 166855 assertions from direct graph orientations and Walsh transforms, supplementing rather than replacing the proof. Risk: no error identified in the examined transfer normalization, though the result has not received independent audit.

## Originality — PASS (bounded search)

Gebhard–Sagan (1999, arXiv:math/9907078) discuss sink enumeration and the unique-sink chromatic coefficient, not Boolean convolution conditioning. Hwang and collaborators (2019, arXiv:1910.10920) do give the complete multivariate sink polynomial for any graph, so all signed frequencies are in principle obtainable by substitution; this is the strongest overlapping source. Their general subgraph and bond-lattice formulas do not establish a zero-free theorem or an exact arithmetic gap for every cycle, nor the resulting sharp classification for all maximum-degree-two graphs. The alternate exact reduction to the independence polynomial at fugacity minus one half was checked against Radchenko (2021), whose general cycle transfer trace is credited; the all-character two-unit separation and graph-family condition number are not explicitly supplied there. Targeted searches did not locate an equivalent all-size Fourier spectral theorem. Residual priority risk: a special case might be worked out in an unindexed source or obtained from earlier multivariate enumerators; the searches do not prove uniqueness.

## Value — PASS

The natural inverse problem is to recover an arbitrary function on the Boolean vertex group from its convolution with sink-set counts. The result exactly distinguishes recoverable cycle/isolate graph geometries from leaf-bearing paths, proving a sharp positive Fourier margin and optimal Hilbert condition number rather than merely listing unsigned sink counts. This is an infinite, structurally complete natural graph class, not an arbitrary finite slice. It does not establish general graph recoverability or all higher-degree statistics.

Self-review: passed. Independent audit: not yet performed.
