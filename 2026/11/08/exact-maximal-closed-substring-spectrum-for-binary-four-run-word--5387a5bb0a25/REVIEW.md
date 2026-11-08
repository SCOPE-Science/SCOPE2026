# Scientific review

## Correctness — PASS

The claimed classification is proved by an exhaustive partition according to the number of letter transitions in a factor (zero through three), with border existence, uniqueness, and both one-letter maximality conditions checked in each class. The two endpoint deletions are forced by closed extensions that cross an adjacent run boundary. The resulting disjoint endpoint families imply the exact count; a two-variable floor bound gives the sharp maximum, and explicit positive compositions give every intermediate count. The independent literal-factor checker passed 4,096 parameter quadruples with all four run lengths at most eight and checked lengthwise attainable spectra through 32. Finite computation is corroborative, not the proof of unbounded claims.

## Originality — PASS, with residual priority risk

The closest general source is Umezaki et al. (arXiv:2607.02838), whose run-length encoded framework includes unary-border interval families and a valid-pair classification. These broader lemmas cover the structural *method* for individual MCSs, but the inspected text does not state or directly evaluate the exact four-run endpoint list or the sharp attainable spectrum at fixed total length; deriving those requires specializing the endpoint cases and a separate extremal argument. Fischer–Köppl (arXiv:2610.38114) treats output-sensitive enumeration for arbitrary strings with its output count left instance-dependent. Jain–Mhaskar (arXiv:2506.06452) discusses exact counting for Fibonacci words instead. Search-index and locally available prior-claim comparisons found no explicitly equivalent symbolic four-run result. An unindexed earlier specialization, or an interpretation of the broader run-length lemmas as making this a routine corollary, remains a priority/value risk.

## Value — PASS

The four-run family is the first binary run composition admitting both two-transition unary-border and three-transition mixed-border MCS occurrences. It gives a natural boundary case for output-sensitive compressed enumeration. Beyond a closed form, the exact all-length interval spectrum shows how much the occurrence output can vary with fixed input length and fixed number of runs, with witnesses for all attainable values. This is a complete motivated structural classification rather than a recomputation of a short table.

## Limitations and closest evidence

The theorem applies to occurrence counts for exactly four positive runs, not general RLE strings or circular words. There has been no independent audit. Most important sources: https://arxiv.org/abs/2607.02838 (general RLE structure, especially Lemma 4), https://arxiv.org/abs/2610.38114 (new output-sensitive framing), https://arxiv.org/abs/2506.06452 (distinct family), and https://arxiv.org/abs/2209.00271 (original MCS definition).

Self-review: passed. Independent audit: not yet performed.
