# Independent mathematical audit

## correctness

PASS

An independent exhaustive replay tested all permutations through order seven against every factor inequality at every flip, kept exactly the legal neighboring-entry edges, and compared all BFS distances with the number of discordant label pairs. It recovered vertex counts 1,1,2,4,14,44,220, no discrepancy through six, and the six exceptional bins (4,6):4, (5,7):6, (6,8):4, (7,9):3, (8,10):2, (9,11):1. The frozen replay paths are check_a.py, check_b.py and their .out files; uploaded scripts were not executed in review. The infinite portion follows separately. In the displayed seven-permutation route, the three-flip one-position sets are {1,2,5,7}, {1,2,3,5}, {1,3,5,7}, and the four-flip sets are {1,2,5}, {1,3,5}, {1,3,7}; each satisfies the prefix bounds. Earlier states are common and legal, and from five flips onward at most two ones remain, with any nonempty word retaining position 1. The four discordant pairs are precisely the cross pairs between (3,7) and (2,5); only 7,2 can be swapped first in a path that changes just these four orders. This gives the forbidden prefix-normality defect 1000101, whose prefix 100 loses to factor 101. A swap changes parity, ruling out length five. Appending a trailing zero preserves all inequalities: a newly included suffix can be shortened by removing the final zero, and the full-length inequality is vacuous. Inserting each new largest label at the front implements this append operation and preserves the six-swap path. The common leading block creates no discordant pairs and a Kendall geodesic cannot swap any pair not discordant initially, so the same first move remains forced and forbidden. This proves the all-n existence claim without extrapolation and says nothing about the largest detours above seven.

## originality

PASS

The supported distinct claim is the sharp failure of isometry of the natural inclusion into the adjacent-transposition permutahedron, its exact first-failure census, and persistence of a fixed detour. The strongest inspected same-object prior gives the generator construction and directed swap criteria, not a metric equality or obstruction. The exact Resultary hit is the subject record; distinct nearby findings use other permutation classes and do not imply the result.

## value

PASS

Connectivity by sorting toward a common extremum leaves open whether shortest unrestricted paths can stay admissible. A sharp counterexample to that natural metric property is useful, especially with a classified first failure and a simple obstruction that persists in the entire family. The census identifies just how the property breaks at its first order, rather than reporting an arbitrary small-order graph statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
