# Independent mathematical audit

## correctness

PASS

A length-m zero window is unique, rooting every cycle once; an Euler-circuit enumerator and exhaustive invertible-feedback enumeration yield identical canonical-cycle sets (2048 at m5). The arch-count characterization follows by constructing a shortest absent scattered subsequence; all 2^m cuts of each root and an independent next-occurrence DP are evaluated. Independent Python feedback/arch reimplementation reproduces (2,2):1, (3,4):2, m4 (5,7):8 and (6,7):8, and m5 (10,12):512,(11,13):1536. Independent orbit normalization reproduces the 528 reversal/complementation orbit classes and their 16/120/16/376 breakdown. The full saved CSV was not byte-recomputed; verify.py source and original Git blob were inspected. Finite proof only through m5.

## originality

PASS

Critical correction: earlier 2026 Oct18/Oct26 publications already cover the unpadded class split and exactly the same orbit numbers, contra overly strong self-review. The surviving distinct result is the paired best/worst subsequence indices for the natural padded 2^m+m-1 cut (m<=5); no earlier inspected statement establishes this exact new statistic. Acceptance is only for that tightly scoped claim and must not imply the prior numbers themselves are novel.

## value

PASS

The standard linearization of a de Bruijn cycle of order m has 2^m+m-1 letters to cover all m-factors once as a linear word. Its scattered-subsequence universality under all cuts is a separately motivated exact invariant; a complete census at first differing best-cut order is a useful finite boundary, even though the unpadded 512/1536 classification and symmetry orbits were known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
