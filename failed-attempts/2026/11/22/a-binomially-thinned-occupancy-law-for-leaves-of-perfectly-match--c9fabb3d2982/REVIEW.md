# Independent mathematical audit

## correctness

PASS

The union of two perfect matchings would have an alternating cycle in their symmetric difference, so conditioning on existence is equivalent, for the leaf law, to fixing a matching by label symmetry. Each quotient tree on m pairs has 4^(m-1) lifts; opposite endpoints of a quotient edge are independent bits. Conditional on the quotient, pair i gives one leaf with probability 2^(1-d_i), independently across pairs. The quotient Pruefer occurrences are iid, d_i=1+K_i, and occurrence-wise independent fair thinning consequently reproduces the joint pair flags. For k boxes the joint vacancy probability is (1-k/(2m))^(m-2), giving the pgf, extreme probabilities and moments. Expanding log b_m and log a_m^2 gives a difference -1/(4m)+O(1/m^2), hence m(b_m-a_m^2)->-e^(-1)/4. The limit variance and normalized L2 concentration are consistent. The two-vertex case has both partners as leaves and is correctly excluded. An independent finite reproduction agreed for all labeled trees at orders 2,4,6,8 (the first by its separate trivial law). At order 10 with a fixed matching it gave counts (1920,11520,14560,4000) for leaves (2,3,4,5), over 32000 trees. Neither finite experiment establishes the unrestricted result.

## originality

FAIL

The full conditional distribution, not just the unmarked matched-tree count, follows routinely from the classical fixed-forest extension formula: delete any prescribed leaf endpoints and apply the same formula to a forest of singleton and two-vertex components. This gives the entire joint marked leaf law in one specialization, and the claimed occupancy law is precisely the same joint vacancy law under iid draws into boxes with a null outcome. The inspected tables and other adjacent papers do not themselves contain the occupancy statement; the reason for failure is the exact implication from the stronger classical counting tool, not those tables or a negative search.

## value

FAIL

The conditioning and leaf statistic are both natural, and the example is a useful illustration of forest completion. But the exact invariant as submitted is mechanically recovered by deleting designated pendant vertices and substituting component sizes 1 and 2 into the standard completion formula. The vacancy interpretation is an equality of the resulting joint probabilities, without an extra distributional or structural theorem beyond that calculation. Its useful explanatory presentation does not supply a scientifically distinct narrow result under the standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
