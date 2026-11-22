# Review: sharp first \(3/2\)-barrier crossing in binary four-mer Greedy assembly

## Correctness

PASS. The path-endpoint lemma is established from the impossibility of four-symbol overlaps between chains of disjoint distinct original four-mers. The exact Greedy and optimal length recurrences have correct base cases and enumerate all legal transitions. Two independent implementations—the first operating on endpoint chain pairs and the second on literal full merged strings—both exhausted all 39,202 input subsets of cardinality at most eight. Both returned the same eight maxima, equality counts and exactly four threshold-crossing masks. A length-eleven host and a seven-step legal Greedy trace independently demonstrate the sharp \(17/11\) witness. This is not extrapolation from sampled states.

## Originality

PASS on inspected evidence, with residual priority risk. The primary recent Greedy superstring preprint of Chukhin et al. (arXiv:2608.20018, first posted 20 August 2026) treats unrestricted alphabets, proves the exact three-mer ratio and constructs longer-width lower bounds; its text does not supply the binary four-mer cardinality threshold. A public binary three-mer exact census is narrower in width, while a known complete sixteen-four-mer computation concerns a single input set rather than all at-most-eight-word sets. General 2018 Cazaux–Rivals ratio bounds do not imply the exact finite classification. Searches for word-width, binary-alphabet, cardinality, approximation-ratio, reverse/complement and exact-table equivalents found no decisive covering source. An unindexed earlier computation remains possible.

## Value

PASS. Fixed-width Greedy approximation guarantees remain a motivated string-algorithm problem, and the binary four-mer universe is the first canonical fixed-width case beyond the exactly understood binary three-mer census. The result finds the minimum number of distinct reads required to breach the natural \(3/2\) benchmark and classifies every smallest counterexample, distinguishing tie-breaking obstructions from the full-universe behavior. The exact cutoff and complete equality orbit are useful as small reproducible adversarial assembly instances. This is a bounded natural classification, not a general approximation guarantee for arbitrary binary read sets.

## Limitations and status

No claim is made for input sets larger than eight or for nonbinary words. Unindexed earlier equivalents have not been excluded. The computations support a self-contained finite proof but have not been independently audited by external experts.

Self-review: passed. Independent audit: not yet performed.
