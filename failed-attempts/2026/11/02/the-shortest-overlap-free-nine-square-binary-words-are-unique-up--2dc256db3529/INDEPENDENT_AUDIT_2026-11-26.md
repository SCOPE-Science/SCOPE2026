# Independent mathematical audit

## correctness

PASS

Every prefix of an overlap-free word is overlap-free. For each one-bit extension, a factor of length 2p+1 has period p exactly when it is axaxa with |x|=p-1; this includes p=1. The supplied recurrence removes the final nonempty square, so correctly computes maximum square count; for this theorem the exact-nine test can also be done independently without relying on the distinction between at least nine and exactly nine. The independent reproduction checked every possible start of a forbidden factor and counted factorizations at each exact depth, with the empty prefix having depth zero and only positive-length even square edges allowed. It found zero exactly-nine words at each length 1–47, then 416 overlap-free words at length 48 of which exactly the displayed complementary pair admit nine squares. Each has exactly one ordered cut, with lengths (6,4,4,4,12,4,4,4,6). Replay: python /workspace/branches/0ba74666-1385-4be6-8d72-124807c92212/independent_census.py; its output is independent_census.log in the same directory. This is a finite exact exhaustion, not a statement about longer words or other alphabets.

## originality

FAIL

A distinct indexed result, 52c025fc067a, gives the entire submitted theorem as the k=9 part of a stronger minimum-length spectrum. It uses the same definitions and states the same pair and unique cuts. The date shared by the catalogue entries does not establish which result was found or made public first; this is demonstrable statement coverage, not a claim of historical priority or derivation. No distinct substantive remainder is established by the frozen claim.

## value

PASS

In mathematical content the minimum over the maximum permitted square count, complete classification of optimizers, and rigidity of their cuts are substantive, naturally posed refinements of the ten-square theorem. This assesses the question's scientific value separately from the exact indexed coverage that defeats distinctness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
