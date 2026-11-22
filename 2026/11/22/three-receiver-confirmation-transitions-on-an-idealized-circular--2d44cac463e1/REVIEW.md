# Review of the circular three-receiver confirmation theorem

## Correctness — PASS

The binomial conditional success probabilities \(f_1,f_2,f_3\) are exact for \(0<p<1\). The covered-multiplicity identity and equal-interval middle-coverage lemma establish the global constraint \(m_2+m_3\le\ell\), including the wraparound and full-circle boundary cases. All three extremal multiplicity vertices are feasible when \(3\ell\le C\); a linear objective therefore yields a sharp global maximum and complete equality classifications. Explicit subtraction proves both transition fractions. The independently constructed endpoint-integrating checker passes 18,000 random geometry tests and 14 analytical boundary cases. Finite tests are not substitutes for this proof.

## Originality — PASS on inspected evidence; priority provisional

The motivating 2023 full-text seismic paper establishes station-density/alert-mode tradeoffs, not the stated mixed three-receiver optimization. Litvak et al. explicitly analyze two overlapping sensors and grouped co-located sensors; the novelty is neither binomial counting nor the two-sensor nonoverlap principle. Asano–Brass–Sasahara optimize exactly-one interval coverage from a prescribed family; Shan–Xu–Cheng handle probabilistic target coverage and minimum sensor counts; Ammari gives general planar multi-coverage density constructions. All are relevant precedents but do not directly state or dominate the sharp three-arc mixed-confirmation phase diagram with its intermediate regime and all equality cases. A broad field of classical interval-covering and reliability optimization remains a historical-priority risk; exhaustive priority cannot be certified.

## Value — PASS

The source literature identifies a concrete tension between single-station fast alerts and network-confirmed alerts. The result fully classifies the smallest receiver count that allows a strictly optimal *intermediate* amount of redundancy, including a constructive non-colocated design, and identifies a sharp threshold depending only on receiver reliability. This is more informative than a routine numerical station-search or an arbitrary parameter slice, yet deliberately an idealized benchmark rather than field guidance. Independent instrument failures at one site, perfectly uniform events, hard detection footprints and exclusion of false alarms are strong restrictions; empirical calibration would be necessary for application.

Self-review: passed. Independent audit: not yet performed.
