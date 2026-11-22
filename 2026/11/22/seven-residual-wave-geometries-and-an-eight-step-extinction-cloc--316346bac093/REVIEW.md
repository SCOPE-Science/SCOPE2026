# Scientific review: near-majority icosahedral excitation

## Correctness — PASS

The graph is given by twelve explicit five-neighbor lists. An exhaustive C++17 functional-graph traversal classifies every integer code in the \(3^{12}\)-state range. Independently, a vectorized Python implementation checks the all-state identity \(F^{11}=F^8\), reconstructs each first-entry time and ultimate period, and compares every individual three-cycle basin to the C++ results. Both yield the identical thirteen nonzero depth–period cells, \(200\) three-cycles, \(1260\) oscillatory-basin configurations, and a sharp eight-step bound. A third verifier checks the entire graph automorphism group, the seven geometric classes and basin multiplicities. The code \(2824\) explicitly witnesses the maximal extinction time. The result is a finite exact classification, not an analytic bound for all graphs.

## Originality — PASS, with historical-priority limits

The closest complete icosahedral census uses a single required contact, while the present result uses two. Its complete list of phase-class representatives could permit post-filtering to recover the *recurrent configuration set*, so the static count alone is not the originality justification. The sharp two-contact iterate identity, the full transient-period histogram, individual two-contact basins and the eight-versus-six delay reversal are not consequences of that single-contact census. A separate four-state icosahedral census uses four local phases rather than three. The 2016 and 2018 arbitrary-graph theorems use single-contact excitation; a published induced-density extinction criterion is inapplicable because the graph's induced edge density exceeds two. Adamatzky's threshold-two experiments concern random Delaunay triangulations, not an exact icosahedral classification. Multiple exact and alias searches found no covering published result. There remains a risk of an unindexed equivalent enumeration.

## Mathematical value — PASS

The icosahedron is the canonical twelve-site five-regular triangular spherical network. Two contacts is the largest threshold below strict majority on that graph. Its complete transient/recurrent partition shows survival collapse from \(48400\) to \(200\) three-cycle orbits, while the sharp periodic-entry clock counterintuitively grows from six to eight updates. The seven surviving spatial wave types and basin sizes \(3,6,12\) provide a natural reproducible threshold-response benchmark, not an arbitrary subgraph or sampling exercise. The claim is deliberately limited to that exact finite system; no wider theorem is inferred.

## Sources and limitations

The closest direct comparison is *Icosahedral excitation: exact three-cycle, geometric-orbit, and six-step entrance census* (2026), with the 2016 full text of Gravner–Lyu–Sivakoff and the 2018 full text of Doba supplying the single-contact general theory. Adamatzky (2011) discusses threshold-two excitation in noncrystalline triangulations. The 2026 induced-density criterion concerns a different sufficient condition. Detailed comparison and material inspected appear in `AUDIT.json`. External historical coverage is incomplete, and independent external validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
