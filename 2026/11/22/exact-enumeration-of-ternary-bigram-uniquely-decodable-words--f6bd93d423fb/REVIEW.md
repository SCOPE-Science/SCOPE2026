# Mathematical review

## Correctness — PASS

The exact observation is fixed: both endpoints and all nine oriented pair frequencies. Theorem 2 of Kontorovich–Trachtenberg (2011) converts failure of uniqueness into simultaneous occurrence of two precisely specified pattern families over twelve triples. The standalone automaton implements these conditions, enumerates all 247 nonreject reachable product states, and checks the 247-component integer vector identity \(M^6(M-I)^3\boldsymbol1=\boldsymbol0\). This identity, by commutation of powers of \(M\), proves the infinite quadratic recurrence. Initial terms determine every coefficient and exceptional initial value. An independent exhaustive profile enumerator confirms the first ten lengths. No extrapolation from finite lengths is used.

## Originality — PASS (historically qualified)

Earlier results establish regularity of uniquely reconstructible \(n\)-gram observations (Kontorovich 2004), and the exact regular-language obstruction and small deterministic automaton framework (Kontorovich–Trachtenberg 2011). They are credited as essential prior tools and not presented as new. Targeted comparisons against published results on *all attainable* ternary linear bigram profiles, cyclic singleton Markov types, homopolymer-free ternary profiles, and 3-Abelian singleton words concern different enumerands and do not imply the explicit \(3n^2+27n-63\) all-length linear singleton count. The 2011 original preprint was inspected substantively. The 2004 journal article could only be checked by its abstract and bibliography, so an unindexed equivalent formula in that article or elsewhere remains a genuine risk.

## Value — PASS

Exact singleton-fiber counts are a natural information-recovery invariant: they measure how often a complete dinucleotide histogram plus boundary symbols uniquely reconstructs the source. The precise degree-two law and exceptional lengths establish a sharp, quantitative rigidity collapse between exponential source space and polynomially many uniquely recoverable strings. This is neither an arbitrary finite slice nor merely a formal rewrite of regularity: the coefficient law requires an exact finite-state calculation and yields the explicit reconstruction probability asymptotic.

## Limits and sources

The result concerns only labeled three-letter linear words with known endpoints; it neither classifies all alphabet sizes nor resolves longer-read reconstruction. See Kontorovich (2004), DOI 10.1016/j.tcs.2004.10.010 (abstract and bibliography read), and Kontorovich–Trachtenberg (2011), https://arxiv.org/abs/1111.6431 (full preprint, particularly the obstruction theorem). The closest indexed comparisons concerned feasible profile totals rather than singleton fibers, or periodic rather than linear words. Residual historical-priority uncertainty is retained without treating a failed search as a uniqueness certificate.

Self-review: passed. Independent audit: not yet performed.
