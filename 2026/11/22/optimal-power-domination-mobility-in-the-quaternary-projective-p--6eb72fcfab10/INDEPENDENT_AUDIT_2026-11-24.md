# Independent mathematical audit

## correctness

PASS

Independently built the incidence graph from the 21 cyclic translates of {0,1,4,14,16} modulo 21. Its ordered nonzero differences cover all 20 residues once, hence it is a projective plane of order four and isomorphic to PG(2,4) by uniqueness at that order. The independent vectorized computation takes the closed neighborhood at time 1 and uses only observed sources and the previous observation mask for all later forces. It exhausts 850668 five-sets with zero successes; monotonicity rules out all smaller sets because a force either remains available or its target is already observed in a superset. Exhausting 5245786 six-sets gave 566160 successes, with (point count,time) frequencies (2,3):65520, (3,2):52080, (3,3):383040, (4,3):65520. Each unordered jump pair has a unique common five-core. Summing binomial(f,2) by core frequency f gives 19706400 and replacing each core clique by a spanning path preserves precisely the one connected component. For slides, deleting a point and inserting an incident line counts each edge once; exact sparse connectivity gives 2257920 edges, component sizes 535920 once and 1 exactly 30240 times, with frozen frequencies (3,2):10080 and (3,3):20160. The script /workspace/reviews/evidence/pg24.py replayed with Python 3, NumPy and SciPy: first run 'seeds OUTDIR' (full, no limit) and then 'exchanges OUTDIR' on the same fresh directory. This resolves the finite claim without relying on the author's programs.

## originality

PASS

The checked exact counts and mobility classification concern a distinct finite plane instance; formulations and prior bounds are not credited as new. The closest related record has the same invariant on the same family, but covers only the two-sensor boundary and the q=2 optimum census.

## value

PASS

Order four is the first extension-field projective plane and a canonical finite test for the propagation/reconfiguration problem. The time-and-shore census and contrast between jumping connectivity and sliding with a giant component plus immobilized states provide an exact benchmark for both predicates, beyond a minimum-size computation or a count alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
