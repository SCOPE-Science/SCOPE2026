# Independent mathematical audit

## correctness

PASS

For b≥2,c≥0, sum-incidence edges have weights s_j=b^j+c; unions of two weight matchings are forests, and s_j>2s_{j-1} excludes any higher-weight edge on a cycle below first threshold. At c≥b(b-2), explicit 2b+2 cycle uses the first three levels. In intermediate band b≥3, the highest-weight obstruction excludes j≥3; eligible s_2 edges have distinct left residues modulo d=b-1, so a component has at most one, and its two-matching endpoint path has precisely 2b+1 edges. At c≥b²-b-1 explicit six-cycle exists; pair-sum uniqueness for b powers forbids 4-cycles. b=2 intermediate singleton checked separately. Independent BFS computed three-level graph girth for 63 (b,c) pairs b=2..6 and c<min(17,b²): every case matched ∞/2b+2/6. The infinite result rests on highest-edge proof; binary-word corollary uses published forest characterization.

## originality

PASS

The forest criterion and the sharp shifted-geometric support forest boundary c<b(b-2), including existence of a 2b+2 obstruction, were already published October 25; these portions are NOT new. The full graph girth trichotomy, including the second sharp boundary c=b²-b-1, absence of shorter cycles in the intermediate band, and the six-cycle regime, is not entailed by having *some* 2b+2 cycle or by forestness. A November 8 generic three-spike cycle rank formula gives independent-cycle counts, not an exact all-support shortest cycle without added analysis. Material full text of Zeng–Xue–Zeng's examples was not accessible and remains priority risk, not a default fail.

## value

PASS

Exact girth is a natural structural invariant of a sparse incidence graph, measuring the shortest obstruction beyond the known forest threshold. The nonmonotone finite-girth transition from 2b+2 to 6, with a separate sharp translation boundary, is a substantive classification across all b,c rather than a known-threshold restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
