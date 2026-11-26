# Independent mathematical audit

## correctness

PASS

A failing set is contained in a bisector of an unresolved pair, so a maximum failure must fill a largest bisector. On the set of differing axes, normalized bisector size is the zero atom of an independent sum, with masses 1/q_i at each sign and (q_i−2)/q_i at zero. For q_i>=4, its unique maximum atom bounds the convolution, and equality requires the remaining sum to vanish surely, impossible with any other active axis (all remaining signs can be positive). For q_i=3, the bound is 1/3 with equality exactly when the remaining sum is supported on −1,0,1, i.e. at most one other active axis. Binary-only even supports of size 2s yield binom(2s,s)/4^s, strictly decreasing for s>=1, and odd supports give zero. These observations give each of the five rows and all maximizing supports. Each bisector depends essentially on exactly its listed support, so distinct supports cannot collide. Within a pair of ternary axes every permutation projection is realized by assigning one matched row/column zero and opposite signs on the other rows/columns. The binary–ternary case allows any ordered distinct ternary values in its two binary rows. The singleton and binary-pair counts follow by excluded letters and parity, respectively. Thus the table counts distinct sets, not vertex pairs. Independent enumeration over symbol pairs and relative orientations verified each regime, e.g. (2,2,3,5,5) gives max size 180 and 20 sets, (2,2,4,4) gives 32 and 14 and (2,3,3) gives 6 and 24. Replay: python3 /workspace/review-evidence/replay.py 4. The recorded 61-profile run is separate evidence.

## originality

PASS

The graph-general maximum-bisector identity is prior, and a criterion for testing individual landmark sets in uniform Hamming graphs is also prior. The distinct content is the sharp mixed-alphabet evaluation, with its exact equality supports and deduplication into a count of distinct critical failures. In particular the binary/ternary competition and the four-symbol versus two-binary tie are not ordinary metric-dimension facts or direct evaluations of a uniform-alphabet theorem.

## value

PASS

The exact worst-case guarantee makes a different prediction than ordinary metric dimension. Its dependence on the alphabet mix is structural: two binary axes can dominate ternary axes, and they can tie four-symbol axes. The additional characterization and count specify which landmark choices attain failure at the sharp boundary, not just the existence of such failures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
