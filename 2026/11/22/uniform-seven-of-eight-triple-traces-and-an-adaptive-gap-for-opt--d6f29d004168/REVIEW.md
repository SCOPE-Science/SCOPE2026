# Scientific review: seven-of-eight triple traces for four-cube minimum domination

## Correctness (PASS)

The statement quantifies over every unordered triple of the 16 vertices, not an unverified random sample. A direct counting proof first forces minimum dominating cardinality four and two selected vertices of each parity, and then classifies all 40 minimum sets into the 16 antipodal-pair type and 24 distance-two type. Four pair-distance cases and six triple-distance cases are exhaustively characterized with explicit trace counts. The maximum shattered support has size two. The adaptive upper bound uses the exact pair co-occurrence counts and the disjoint-remainders property of all four-concept positive-positive branches; the lower bound is an eight-leaf tree with explicit minimum dominating witnesses. Both independent implementations reproduce the complete finite result, including all 560 triples. Nothing about other cube dimensions is inferred.

## Originality (PASS, subject to historical priority limitation)

The 2020 primary source on VC dimension and density of Hamming graphs (arXiv:2007.16042v1) was read through its relevant Hamming theorems. It studies open-neighborhood concepts, whereas the present concept class consists of minimum dominating vertex sets. The 2019 hypercube domination paper arXiv:1905.13292v1 studies small connected dominating sets and bounds, not the complete membership-trace or adaptive rank of the optimum family. The closest earlier code-classification paper (Östergård and Weakley, 2000) covers structural classification of short optimal covering codes, so the 40-set census and its orbit types are credited as background rather than claimed as independently novel. Its accessible abstract does not state the triple-trace law or Littlestone dimension, but its full text could not be read and is an explicit priority risk. Published mathematical research searches, including published research-record searches under equivalences and parameters, did not identify a direct statement or dominating known trace/online theorem. This is conditional scholarly originality, not proof of first discovery.

## Value (PASS)

The precise seven-of-eight boundary is uniform over **all** 560 triples of a canonical radius-one optimal covering-code family. It supplies a complete static-shattering complex despite 40 different hypotheses, and the sharp three-round online decision tree shows a strict adaptive advantage over the two-query static limit. This sharp comparison is a motivated learning-theoretic invariant of optimal domination, not an arbitrary choice of one triple or an unexplained isolated count. The ordinary optimizer census is prior context and does not itself constitute the mathematical contribution.

## Scope, related literature and unresolved risks

The theorem is specific to the binary four-cube and only membership queries. The 2000 covering-code paper's full text was inaccessible; the exact strength of any pre-existing derived triple-trace tables or online decision-tree statements remains unknown. No independent expert audit or mathematical certification was performed.

Self-review: passed. Independent audit: not yet performed.
