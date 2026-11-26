# Independent mathematical audit

## correctness

PASS

Let the rows of a change-of-natural-basis matrix be the coordinates of the new basis vectors. Pairwise zero products and independence of the old squares imply the supports of distinct rows are disjoint. Five nonzero disjoint supports on five columns are singletons, and the only nonzero scalar is 1. This verifies the permutation-similarity and full-stabilizer reduction. The source's orbital assignments enumerate all fixed matrices, and descending subgroup inversion subtracts exactly the strictly larger stabilizer fibers. I reproduced the census by a different method: in consecutive chunks of 2^20, rank-test all 2^25 binary matrix masks; for each invertible mask not seen before, mark its images under all 120 permutations and histogram the orders of the permutations fixing that representative. The orbit-size sum and invertible-mask count both equal 9,999,360, and every orbit satisfies orbit size times stabilizer size = 120. All 13 nonzero rows match, the total is 85,411, and the only S5-fixed representative has rows encoded by [1,2,4,8,16]. The other three listed subgroup types do not occur. The conclusion is for algebra maps over F2, not after scalar extension.

## originality

FAIL

A distinct indexed Resultary record gives the same complete census over F2 in dimension five. The 13 nonzero rows coincide, including D12 = S3 x C2; its completeness statement is equivalent to the three explicit zero rows. This is equivalent coverage of the frozen claim, not a priority determination based on dates. A different enumeration method does not distinguish the asserted table.

## value

FAIL

The exact full-group distribution is a natural benchmark beyond a Burnside total and would be useful if uncovered. As submitted it reproduces an available complete table; subgroup-poset inversion is a standard alternative computation here, with no distinct scientific result established by it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
