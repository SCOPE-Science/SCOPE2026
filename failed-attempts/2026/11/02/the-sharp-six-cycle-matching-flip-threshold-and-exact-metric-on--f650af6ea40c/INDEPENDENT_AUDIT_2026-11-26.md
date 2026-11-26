# Independent mathematical audit

## correctness

PASS

In a simple graph the symmetric difference of two perfect matchings decomposes into even alternating cycles, each of length at least four. Total sizes four and six therefore identify a single cycle of the prescribed length, not a simultaneous flip. I independently generated all matchings by choosing disjoint graph edges in increasing index order until all vertices were covered, tested the size predicate on every unordered pair, and ran BFS from all 125 vertices. The 300 four-flip edges give components 120,1,1,1,1 and the stated degree distribution; each of the 30 graph edges lies in exactly one of the five isolated matchings. The 580 additional exact-six flips produce 880 union edges. All union eccentricities are three; unordered pair counts are 880,4250,2620, the degree counts are 5,20,30,60,10 at 8,11,14,15,18, and all ten pairs of frozen states are at distance two. Separate traversal of simple cycles, rooted at their least vertex and removing reversal, confirms 30 and 240 cycles of lengths four and six, as distinct from exchanges. Thus all numeric claims and the sharp cutoff of six are verified.

## originality

FAIL

Resultary 98a001e14839 is an earlier distinct record that already gives the matching count, four-flip component census, 580 exact-six flips and connectivity, hence the same sharp cutoff. Its prose metric is for EXACTLY six, not AT MOST six; however the published package contains the actual complete, compatibly labelled flip4.tsv and flip6.tsv tables and matchings.tsv. I read those tables and computed their union and BFS, reproducing the full submitted combined metric, including the degree polynomial and frozen-pair distances. The census not explicitly printed in the earlier prose is thus mechanically implied by exact released tables, not new on the basis of different graph notation.

## value

FAIL

The graph and exact transition invariants are natural, but the cutoff is already proved and the full union census is a routine combination and traversal of the existing complete exact-length edge tables. There is no new structural theorem or surviving exact invariant beyond that readout. Independent re-enumeration is useful corroboration, not a distinct scientific finding to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
