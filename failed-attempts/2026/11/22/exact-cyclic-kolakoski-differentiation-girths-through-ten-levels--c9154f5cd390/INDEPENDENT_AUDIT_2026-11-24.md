# Independent mathematical audit

## correctness

FAIL

The frozen exact-height census is false. With the frozen definition, [1112] is a primitive height-zero class because one of its cyclic runs has length three. [12122] has lengths (1,1,1,2), so has exact height one but is absent from the two-class census. In fact the primitive terminal words [1^j2] for every j>=3 have undefined derivative; the valid inverse lemma gives a primitive k-fold inverse of each, distinct because the k-th derivatives differ and of unbounded periods by strict period descent. Therefore all exact-height sets are infinite and neither L6 nor L7 is the full exact-height spectrum. The supplied sources implement only the recurrence rooted at the constants. Their restricted numbers and the unrestricted girth/minimizer numbers were independently reproduced, but they establish different claims. In particular, one replay exhausts all one-step-valid bases through period 20 and prunes by the proved >=4/3 growth in period per inverse; /workspace/branches/b52f4bc0-9387-44df-8a87-e41770379869/independent_replay.py and full_run.txt. A separate replay starts at every eligible terminal class (including nonconstant invalid-run classes) using descending integer caps, then applies the exact inverse lemma; /workspace/branches/replay-2/verify_full_girths.py and level_statistics.csv. Both agree on the actual minimum lengths and minimizer counts through ten; small direct forward enumeration cross-checks the lower levels. Those accurate numbers do not repair the false complete census.

## originality

FAIL

The valid substantive girths and all extremal orbit counts through depth ten exactly match the earlier 2026-11-17 Resultary record under the same definitions. The other advertised novelty, a finite full exact-height census and full height-six/seven spectra, is false; the recovered numbers enumerate a restricted descendant sector by direct iteration of the same published inverse lemma.

## value

FAIL

Finite-stage periodic girth and sharp minimizer counts are useful dynamical invariants, but their asserted exact values are already known. The genuinely broader full-height classification offered by the frozen record is false. Reinterpreting the numerical spectra as the descendants of just two seeds gives an accurate restricted census, but that slice and the height-ten cutoff have no separate mathematical motivation in the record beyond the precovered girth question; the small restricted table is an immediate application of the existing inverse lemma. The one-line correction that every exact-height inventory is infinite also follows from the existing all-fibers lemma and does not leave the claimed new spectral classification. No genuinely distinct valuable repair is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
