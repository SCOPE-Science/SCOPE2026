# Independent mathematical audit

## correctness

PASS

For an admissible error e, cancellation of the projected row norm against its sampling probability gives the exact decrease ||AP_I e||²/F(I); a least-eigenvalue vector proves sharpness. The four classes have multiplicities 4, 8, 2, 1 and positive spectra respectively (2c²,2s²), (2,4c²s²), (2,2c²,2s²), and (2,2). This gives exactly the stated score minimizers and unique rate maximizer throughout 0<s<1/√2. For the specified common x*, optimal-rate constraints leave error −e2 and each raw draw hits it with probability 1/2; ID constraints leave −e4, have first squared norm c², and from then on a switch of the row multiplies squared norm by (c²−s²)² with conditional probability 1/2. Rejection enforces switching once a row has been used; the optimal-rate system instead stops at the first accepted update. These are different clocks. Independently reproduced 60 projected spectra and 112 exact moment identities using rational projections and branching, with zero projected rows removed before division; replay `python3 /workspace/branches/independent_reproduce.py` (section 5). The packaged verifier was inspected, not executed; it constructs an update operator even at zero projected norm, so filtering is advisable. The finite replay corroborates rather than proves the full parameter and time laws.

## originality

PASS

The substantive unpreempted claim is the unit-normalized rank-two exact optimizer separation plus realized trajectory separation, not the general rate formula, the row-ID surrogate, or the general possibility of Frobenius selection regret. The prior singleton rejection-overhead example is real conceptual overlap but measures a different phenomenon.

## value

PASS

The family tests a practically motivated surrogate at its global optimum. Unit rows remove trivial rescaling, and the exact expected errors demonstrate a genuine convergence penalty, not just a worse guarantee. The duplicated strong rows and nearly parallel weak-direction pair isolate what a rate-aware selector should detect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
