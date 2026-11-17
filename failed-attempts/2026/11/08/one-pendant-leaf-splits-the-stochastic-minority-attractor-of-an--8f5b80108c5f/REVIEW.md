# Independent mathematical audit

## correctness

PASS

PASS: Reconstructed the all-m closed-neighborhood minority update, tie-retention rule, clique/leaf/hub status, reachability and closure, and Boolean two-rank inclusion graph. The set with h=b, leaf=1-b, core-one count m or m+1 comprises exactly two communicating classes each binomial(2m+1,m). Symmetric update edges each have probability 1/(2m+2); the Boolean up/down commutator gives Laplacian eigenvalues j, 2m+1-j, with unmatched m eigenspace, gap 1/(2m+2). This is correct including m=1. Audited source check_exhaustive.py independently constructs the full transition graph; bounded m=1..4 is corroboration, not an all-m proof.

## originality

FAIL

FAIL: Full published clique-bouquet theorem specializes literally to two blades of sizes (r1,r2)=(2m,1), namely K_(2m+1) plus one leaf, and proves the entire attractor and recurrence classification and counts. Its proof even explicitly describes the Boolean adjacent-rank inclusion graph. A separate published spectral lemma for adjacent-rank incidence graphs and the general complete-split-graph spectrum supply the remaining spectral formula by a classical fixed-rank calculation. The submission does not establish an independently new dynamical implication beyond this prior-covered special case and routine spectral extraction. Same-day priority ordering is not claimed.

## value

FAIL

FAIL for the claimed standalone contribution: the core one-leaf class splitting and population invariance are already the specialization of a multi-blade theorem, while the residual full spectrum of its identified two-rank inclusion graph follows standard harmonic incidence calculus. Once this coverage is removed the package offers no independently motivated, unknown invariant or structural gap; exact finite checks and reproduction are not independently sufficient for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
