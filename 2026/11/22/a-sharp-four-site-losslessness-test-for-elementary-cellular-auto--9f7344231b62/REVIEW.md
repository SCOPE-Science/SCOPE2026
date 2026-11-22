# Review of the four-site losslessness classification

## Correctness

**PASS.** The map is defined at all indices on bi-infinite inputs and on cyclic rings, including the one- and two-site cases. Only five out of the eight elementary neighborhoods can occur when `11` is forbidden. Among 32 five-bit masks, an explicit two-, three- or four-site collision eliminates 22; thirteen local five-site cases give an inverse of radius at most one for the other ten. These are exhaustive finite identity and witness arguments, not an extrapolation from sampled lengths. The packaged checker also verifies direct ring maps through length 12. The count of 80 rules uses eight inactive rule-table choices per effective mask.

## Originality

**PASS, subject to residual literature uncertainty.** Relevant full text on generalized inverses [1] and shift dynamics [2] does not give the complete 80-rule restricted injectivity classification or the sharp four-site test. A checked published Rule-28 predecessor theorem treats unrestricted inputs and a maximum inverse fiber for a single rule; a checked all-rule finite-block identifiability theorem asks for the existence of at least one unique unrestricted finite predecessor, not injectivity for every allowed input. Their statements do not imply the present characterization. An equivalent older table of reversible restricted-source elementary rules may exist under other terms; searches and full-text inspections are not exhaustive.

## Value

**PASS.** Losslessness on the golden-mean shift is a natural exact decoding question for constrained symbolic sources. The result is a complete classification across the canonical 256 local rules, provides uniform radius-one reconstruction when possible, and gives a sharp finite diagnostic for impossibility. The distinction from unrestricted reversibility is mathematically substantive. No downstream result or optimal capacity claim is asserted.

## Limitations

The conclusion concerns one synchronous elementary update from a source forbidding `11`; it does not describe images of longer updates or broader exclusion constraints. The scientific priority assessment is provisional, and there has been no independent proof audit.

Self-review: passed. Independent audit: not yet performed.
