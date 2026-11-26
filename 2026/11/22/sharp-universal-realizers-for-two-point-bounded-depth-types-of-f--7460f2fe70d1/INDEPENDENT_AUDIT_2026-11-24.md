# Independent mathematical audit

## correctness

PASS

For each point, the least visible return is its exact cycle length if at most d; otherwise its d+1 terms are all distinct. In the absence of cross equalities, the ordered pair of these visible periods determines the type, yielding (d+1)^2 choices. A short common cycle of length L contributes its L distinct offsets. On a common cycle of length L>d, the set of true cross differences is one residue class intersected with [-d,d]. It has at most two entries since 2L>2d; a doubleton recovers its exact separation L and has 2d+1-L possibilities for d<L<=2d. Singletons give 2d+1 distinct types, all realized at L=2d+1. This gives 2d^2+5d+2 and includes coincident points. Two copies of every short period are forced by the equal-period no-cross requirement. Each intermediate cycle is forced by its doubleton, and the singleton {d} forces L>=2d+1 or else d-L is visible as well. Adding forced sizes gives (d+1)(5d+2)/2. The proposed cycle union realizes every cross type and has two distinct long cycles for the long/long no-cross type (also when d=1); at equality no other cycle is possible. Independently ran `python audit_checks/independent_replays.py 2`, evaluating literal iterates as ordered equality partitions. Counts 9,20,35,54,77 and sizes 7,18,34,55,81 matched at depths 1–5; exhaustive integer partitions through the proposed minimum gave exactly one universal cycle profile at depths 1 and 2. This bounded test is not the all-depth proof. The submitted verifier was inspected, not executed.

## originality

PASS

The distinct claim is the exact bounded-term two-point repertoire together with its smallest simultaneous realizer and rigidity. Unrestricted cycle decomposition and algorithms for logic on permutations are not new here. The strongest retrieved neighboring statements differ in arity, logical depth, or objective. No exact or dominating match was established; the conclusion is best-of-knowledge, not a historical priority guarantee.

## value

PASS

An exact all-depth finite test structure is useful when testing equivalence of Boolean combinations of the allowed equality atoms over all finite permutations: the proposed one structure detects every distinction. The signed two-point offset forces lengths not forced by visible one-point periods. Counting all profiles and establishing the unique minimum test structure solve a natural saturation question rather than merely computing a small instance or renaming cycle decomposition. This does not assert optimality for other vocabularies, more marks, or quantified formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
