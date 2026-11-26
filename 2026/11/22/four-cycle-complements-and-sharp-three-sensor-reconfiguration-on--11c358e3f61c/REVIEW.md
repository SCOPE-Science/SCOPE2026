# Independent mathematical audit

## correctness

PASS

For closed-neighborhood signatures, survival of every one-detector deletion is equivalent to double coverage of each N[v] and double hitting of every N[u] symmetric difference N[v]. Necessity follows by removing the lone witness when there is one, and a set with zero witnesses already fails identification. Sufficiency follows since one deletion reduces any witness count by at most one. Membership is monotone under adding detectors. Independent construction from inclusion of two- and three-subsets and enumeration of all 2^20 masks reproduced the full coefficient list (15,120,680,1824,2155,940,190,20,1) in degrees 12 through 20, zero below, and total 5945. The independently generated 15 paired-complement four-cycle masks equal exactly the twelve-element minima, and the natural S5 action is transitive since it sends any ground four-cycle to any other. BFS with all valid masks and single-bit moves reaches one minimum with budgets 12, 13 and 14, and all 15 with 15; equivariance extends the separation result to every minimum. For b<12 endpoints are absent, so the distinct-component wording applies to 12<=b<=14. Independent replay: `python3 /workspace/branches/612ca51f-d283-49fe-997b-69a441813e25/independent_check.py`; same-directory independent_check.log reports a deterministic small probe, complete census, the 180 direct deletion checks at the minima, and a concrete eight-move path at cap 15. The supplied programs were inspected, not executed.

## originality

PASS

The double-witness criterion and lower bound of 12 are prior. The Desargues-specific enumerator, complete four-cycle-complement classification of optima, and sharp TAR slack are distinct from the verified prior statements. An exact catalogue hit matching all three is the frozen record itself, not a distinct priority claim.

## value

PASS

The Desargues graph is a canonical small cubic incidence graph, and the one-erasure model and TAR cap have a clear fault-tolerance interpretation. The complete enumerator gives the sizes and multiplicities of robust placements; the four-cycle pattern organizes all exact optima, and the sharp extra-capacity requirement answers a different question from minimum size. The result is more than verifying a known cubic bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
