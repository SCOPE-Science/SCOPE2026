# Independent mathematical audit

## correctness

PASS

The census follows directly from the three-candidate tournament. With a Condorcet winner the tournament is transitive; the linear order matching every majority edge is uniquely Kemeny-optimal and its top is also the sole Copeland winner. On a directed triangle, Copeland ties all three and Kemeny orders minimize the margin weight of reversed arcs. Disagreeing with any single arc is possible, so only orders disagreeing with a single minimum-weight arc are optimal; their top candidates are the heads of those arcs. Each voter contributes +1 or -1 to the sum of cyclic margins. Positive odd margins cannot cycle for one voter, are forced to (1,1,1) for three voters, and are (1,1,1) or (3,1,1) for five. Only the latter diverges. Its sum saturates the five-voter bound, so every ballot disagrees with exactly one majority arc. For fixed orientation and margin triple, the number of ballots disagreeing with an arc of margin m is (5-m)/2, and there is exactly one ranking disagreeing with just that arc. This forces multiplicities 2,2,1. There are two orientations and three choices for the margin-3 arc, acted on transitively and freely by candidate relabeling, giving six anonymous profiles, each with 5!/(2!2!)=30 labeled profiles. The representative has margins A>B=1, B>C=3, C>A=1; reversing a light edge yields tops A or B, whereas Copeland returns all three. Consequently the exact fractions are 5/216 and 1/42. This is a direct proof; the supplied verifier was inspected, not executed.

## originality

FAIL

Shown already covered: the earlier Resultary Kemeny–Slater record gives the exact same census and orbit classification on precisely the same profiles. Slater and Copeland are pointwise identical as winner correspondences on three-candidate tie-free tournaments. Substituting this equality yields the exact frozen claim, including the denominators and both incidences, the nested winner sets, the canonical profile, and minimality. There is no distinct remainder in the frozen scope.

## value

FAIL

Exact IC/IAC frequencies at the first disagreement are a natural object, but these frequencies, their unique ballot-multiset orbit and their winner-set relation are already available by the pointwise equivalence to the previously counted case. Recounting the identical event gives no additional invariant, boundary hypothesis, or reusable classification beyond that result. The scope has no supported new smaller remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
