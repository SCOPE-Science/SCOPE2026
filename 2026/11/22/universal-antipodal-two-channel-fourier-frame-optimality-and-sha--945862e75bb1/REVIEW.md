# Independent mathematical audit

## correctness

PASS

Summing over all translations kills the off-diagonals by discrete character orthogonality, with the factor N from the number of translates. The spectrum is w a[d(k)]+(2-w)a[d(k-r)], so it is positive. Averaging the entries at k and r-k recovers the balanced spectrum, bounding both weighted extrema in the required directions. For r<R, decrease the coordinates of an antipodal maximizing distance pair until their sum is r: both remain in [0,R], so they are realized on the short arc and at least one coordinate strictly decreases. For the minimum, increase the coordinates of an antipodal minimizing pair until their sum is N-r; the two remaining capacities sum to R and suffice, and both distances at the corresponding long-arc point are still at most R, so there is no distance wrap. This makes both comparisons strict. At the antipodal gap an off-midpoint extremizing pair exists even for a constant balanced spectrum; its two entries split under unequal power. One bound therefore worsens strictly and neither improves. For heat the unit impulse gives energy exp(-8t sin²(πk/N)); antipodal opposition makes the sum a cosh with maximum at the centers and minimum at the closest grid indices to a quarter turn. It yields the claimed parity formulas, including the doubled-neighbor N=2 case (no alternate gap), and the two margins follow respectively by evaluating at one balanced center and the two unequal-power antipodal centers. As a finite exact sanity check, N=4 with radial energies (4,3,2) gives a constant antipodal spectrum 6, versus gap-one extrema 5 and 7. I inspected CHECK.py, not executed; VERIFICATION.md's recorded 161085 assertions are supplementary and not evidence for the universal strictness or sharp comparisons. No formal verification is claimed.

## originality

PASS

Best-of-knowledge pass for the strict separation of both spectral edges across gaps for every strictly decreasing radial energy profile, joint uniqueness across powers, and the sharp heat specialization with margins. Full-translation diagonalization is prior. Weak balanced antipodal optimality also follows from reverse pairing: antipodes order the two copies of the radial vector oppositely, and choosing an opposite-rank pair for either extremum gives a pigeonhole bound on that extremum for any permutation. This weak bound does not supply strictness against every shorter cyclic gap (or power rigidity). The strongest same-setting catalogue comparison is for a non-strict profile with zeros and even gives nonantipodal optimizers; same-day dating is not taken as ordering evidence.

## value

PASS

The strict ordering settles both worst-case energy bounds at once, regardless of the shape of the strictly decreasing Fourier profile, and controls whether compensating with unequal channel powers can recover a worse spacing. The heat formulas quantify conditioning and separation penalties with an actual parity effect. This makes the result a reusable design benchmark, beyond the prior diagonalization or the weak sorting bound. It does not establish a rule for more channels, odd orders, truncated translations, or Fourier profiles with plateaux or zeros.

The dated certificate retains the supplied scientific assessment, sources and limitations.
