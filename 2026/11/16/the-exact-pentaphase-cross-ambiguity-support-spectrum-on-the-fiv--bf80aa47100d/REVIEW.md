# Scientific review of the exact pentaphase five-cycle cross-ambiguity spectrum

## Correctness
**PASS.** The exact Fourier-zero test follows from irreducibility of the fifth cyclotomic polynomial: a five-term sum of fifth roots is zero exactly when the five exponent residues are a permutation. Independent standard-library Python and C++ implementations enumerate all 390625 normalized ordered pairs, testing every time and frequency shift with integer arithmetic. Both give the identical five support multiplicities and six sorted row-zero profiles. The normalization removes precisely two independent global phases, not any cyclic symmetries. The displayed matched-chirp minimum family contains exactly 125 normalized pairs. The finite loop is exhaustive for the stated finite domain; it makes no extrapolation to other lengths or alphabets.

## Originality
**PASS, subject to historical-priority uncertainty.** Nicola (2022) proves an uncertainty lower bound and minimum-support equality classification, not the new five-value spectrum and its pair counts. Krahmer–Pfander–Rashkov (2006), Proposition 4.4, gives a general support bound but not alphabet-restricted counts. An earlier published constant-envelope result proves the five-or-at-least-seventeen gap for all complex phases, so that gap is expressly excluded from the new contribution. An earlier published self-ambiguity census on the same five-cycle includes only diagonal pairs \(f=g\), not all independent ordered pairs. The fixed-five matched-prime alphabet, multiplicities and two distinct support-21 profiles are non-implied by these inspected claims. Specialized pentaphase radar or finite combinatorial catalogues may exist outside indexed sources.

## Mathematical value
**PASS.** Full-support fifth-root phase coding on a five-site prime cycle is a natural discrete phase-coded radar/Gabor model at the first size where phase-alphabet order equals the ambient prime. The complete spectrum identifies which nonminimal exact ambiguity-support sizes are realizable and gives their prevalence, refining known qualitative uncertainty bounds. Distinguishing two support-21 row patterns describes substantively different time-shift cancellation layouts. The result is confined to this natural small case, has no stability or magnitude implications, and no generalization is claimed.

## Closest sources and limitations
F. Nicola, arXiv:2204.14176v1 (2022); Krahmer, Pfander, Rashkov, arXiv:math/0611493v1 (2006); Somlai, arXiv:2212.12823v1 (2022); and published studies of constant-envelope support gaps and the five-cycle self-ambiguity subclass. The finite-field direction theorem explains the allowed per-row zero counts but does not imply their coupled cross-shift census. Originality is a best-knowledge statement, not proof of priority. Independent assessment is still outstanding.

Self-review: passed. Independent audit: not yet performed.
