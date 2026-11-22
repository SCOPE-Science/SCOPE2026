# Independent mathematical audit

## correctness

PASS

For a full-support mu_6 phase word f on Z7, Q(zeta_6) and Q(zeta_7) are disjoint, so an off-axis frequency zero at k!=0 forces the seven coefficients h_x(t)=f(t)conj(f(t-x)) all equal. For x!=0 the product gives c^7=1 and c in mu_6, hence c=1 and f is constant. Nonconstant words thus have 36 nonzero off-axis values; A(0,0)=7 and A(0,k!=0)=0, while shift-axis zeros occur only in three conjugate pairs. Integer coordinates of zeta_6 yield exact zero tests. Independently enumerated every one of the 6^6=46656 normalized exponent words, recovering masks 0:41868, single masks 1/2/4:1512 each, double masks 3/5/6:84 each, triple mask7:0; hence support distribution 7:1,39:252,41:4536,43:41867. Independently reconstructed the affine-index/conjugation orbits of the four provided representatives, sizes 84,42,84,42, pairwise disjoint, exactly union of all 252 double-mask words. Inspected RESULT.md, verify_support.py and independent verify_increments.py at exact frozen blobs; this is a complete finite enumeration, not extrapolation to other lengths.

## originality

PASS

Nicola provides unrestricted finite cyclic STFT minimum equality classification, which covers the constant support-seven case but not the restricted-alphabet nonconstant strata and exact simultaneous autocorrelation masks/orbits. Other Resultary small-cycle cross-STFT studies concern separate signal pairs/alphabets/lengths. An older specialist waveform table for 7-site sixth-phase autocorrelations remains a risk; Lam--Leung abstract alone is not enough to exclude it.

## value

PASS

For the natural 7-cycle and sixth-root phase alphabet, exact self-ambiguity support is a meaningful finite phase-code diagnostic. The four-level possible support set, sharp nonconstant gap, complete mask histogram and four symmetry orbits describe all admissible words, not an arbitrary sample or an isolated checksum. This precise finite classification could be used in waveform/phase-coded ambiguity design even without a general-n theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
