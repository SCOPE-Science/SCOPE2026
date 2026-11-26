# Independent mathematical audit

## correctness

PASS

There are n deletion sites. Adjacent equals collide; a nontrivial period likewise identifies deletion sites. The unique marker distinguishes its own deletion and roots all other outputs, reducing to different linear deletions of an alternating tail. In a collision the deleted letters agree by comparing output histograms. Closing a cyclic alignment by i→j then gives a permutation on whose cycles the source letters are constant. A fixed retained site would root both outputs at the same original position; distinct linear deletions of a proper source are different at the earlier deleted index, a contradiction. Thus there are at most floor(n/2) cycles; the n−1 rotations per pair give the claimed union bound. The adjacency matrix J−I gives the stated exact cycle coloring count and makes the ratio sqrt(q)/(q−1)<1 for q≥3. I independently enumerated direct deletion/rotation classes for ternary n=3–8 and quaternary n=3–7, reproducing the maxima and full-shadow counts. Replay with python3 /workspace/branches/independent-check/word_checks.py. The universal proof does not rely on these finite tests.

## originality

FAIL

The principal novelty claim, exponential full-shadow genericity among proper circles, is already implied with the same base and a smaller fixed-q polynomial prefactor by the distinct indexed run-exact theorem eef1c8604afc. Its shared-root argument is also the key obstruction behind the frozen uniform bound: any fixed start of an alignment puts the deletions in one run, and properness makes runs singletons, so the derangement union bound is a short corollary of this proof. The other distinct result f0f036e50847 has precisely the marker-and-periodic-data construction at t=1, though its formal theorem excludes t=1. This is a decision about demonstrated coverage, not which same-day record was first. No substantive uncovered claim in the frozen formulation is established by its alternative count.

## value

PASS

Quantifying whether every distinct site of a proper circular source is distinguishable after one deletion is a natural exact and asymptotic problem; the proper-source conditioning is essential, and the alignment count supplies a transparent all-length estimate. This value assessment does not confer originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
