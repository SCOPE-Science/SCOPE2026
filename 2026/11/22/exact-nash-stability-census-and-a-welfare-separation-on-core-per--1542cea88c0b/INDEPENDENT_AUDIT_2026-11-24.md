# Independent mathematical audit

## correctness

PASS

With enemy value -N, any player sharing an enemy would receive at most -2, so individually rational blocks are cliques, as are Nash-stable blocks since singleton exit is allowed. If two blocks contain core agents, one can move from the no-larger block to the larger block and strictly gain. A peripheral must join the resulting sole core block if it has none. Conversely, once there is one peripheral in the core block, a core player already earns r>=1 and can get at most one elsewhere; neither kind of peripheral can gain by any move, with outside-to-core utility r-N=-s. Thus there are exactly s labeled equilibria, including equality r=1 and the s=1 one-block case. Positive Nash product requires one distinct core per peripheral, so is feasible exactly for r>=s. At a positive optimum merging any core-only block into a mixed block strictly improves the product. For the resulting core counts k_i>=1 the log product is the sum of (k_i+1)log(k_i); strictly increasing successive differences force all surplus onto one peripheral. This gives product (r-s+1)^(r-s+2), whose (r+s)-th root is the stated welfare, and the labeling counts s! binom(r,s-1) for r>s and r! for equality. For r>=s>=2 all equilibria have a zero-utility singleton despite a positive optimum.

## originality

PASS

The supported contribution is the joint exact optimum and ordinary Nash census on the full complete-split family, including the zero-welfare separation at every equilibrium throughout the positive-optimum regime s>=2. The clique lemma, a small welfare/stability conflict, and low-core welfare and optimizer counts have existing coverage and are not credited separately.

## value

PASS

This is a natural complete classification in a standard core–periphery family. It gives exact welfare and optimizer statistics and shows that even choosing the best ordinary Nash equilibrium cannot achieve positive welfare in arbitrarily large instances where full positive welfare is feasible. This is stronger than exhibiting a bad equilibrium or one unstable optimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
