# Independent mathematical audit

## correctness

PASS

Let p count marked vertices with at least two marked neighbours, let e be the number of marked–marked edges, and let Q be the q unmarked vertices with at least two marked neighbours. Handshaking gives p<=e. The induced graph J on A union Q has at least e+2q edges (counting each marked–unmarked edge once); it is nonempty and its cycle space embeds into that of G. Hence e+2q<=m+q-1+beta(G), and p+q<=m-1+beta(G). At most p+q distinct traces have size at least two; there are at most m singleton and one empty trace, and all traces are subsets of A. For sharpness use c marked disjoint triangles and m-3c marked singleton components, then connect representatives with subdivided bridges, add a private leaf to each marked vertex and one pendant beyond a private leaf. The result is connected with no additional cycles and cycle rank c. The distinct traces are the 3c internal triangular pairs, m-2c-1 intercomponent pairs, m singletons, and the empty trace. Bridge pairs connect different marked components and are distinct; the added terminal pendant is unmarked and has no marked neighbour. This proves equality even in the c=0, m=1 boundary, and never for an empty A. The referenced artifacts/verify.py is present under its exact path despite the abbreviated inventory. It was read, not executed. Independent replay python3 -B /workspace/reproductions/2.py used Gray-code edge updates and bitmask components for all 2097151 graph/mark pairs through six vertices and tested 65 exact cactus witnesses joined via a subdivided star; the finite test confirms the computation, not the universal bound.

## originality

PASS

The forest case is background. For open traces witnessed anywhere, the exact additive cycle-rank dependence on all finite simple graphs and the stable sharpness construction are not covered by the broader asymptotic or closed-neighbourhood results inspected, nor by the exact block-graph class extremum. The latter is a meaningful same-day comparison but provides no chronology and uses a different optimization domain. This is a bounded best-of-knowledge judgment.

## value

PASS

Cycle rank measures how far an arbitrary graph is from a forest. The exact charge of one extra realizable open trace per unit of cycle rank, with simultaneous equality throughout a stated range and attained by sparse connected cacti, sharpens qualitative neighbourhood-complexity bounds. This also explains how marked witnesses and unmarked witnesses share one cycle budget; it is not a mere renamed forest result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
