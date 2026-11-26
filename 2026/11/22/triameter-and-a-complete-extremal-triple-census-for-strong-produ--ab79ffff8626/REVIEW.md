# Independent mathematical audit

## correctness

PASS

For coordinate ranges A≥B≥…, assign each pair one coordinate attaining its Chebyshev distance. A single witness for all three gives at most 2A by the line perimeter identity; multiplicity 2+1 gives at most 2A+B; three distinct witnesses give at most A+B+C≤2A+B. Three corners in the largest two coordinates attain the bound. If A>B, equality forces two diametral edges with a common outlier in the unique longest coordinate and distance B between the remaining pair. This gives exactly R times the number R²−S²(b²−2)^r of ordered pairs at distance B in the transverse box, because the three outlier choices and two endpoint orientations cancel the factor six for vertex labels. If A=B, all three pairs must attain A. In one leading coordinate a given label-pair event has 2a outcomes, each pairwise intersection has 2, and the triple intersection is empty. Inclusion–exclusion across the k independent coordinates gives the stated count with the unconstrained R³ factor and division by six. On a square board this counts 4a side-based constructions minus the four double-counted corner triples; on a nonsquare board the unique-longest formula gives 2n. For j specified failed pairs, the joint probability is [1−2j/q²+O(q⁻³)]^d, so their joint moments converge to e^(−2jλ), giving the binomial law by finite inversion. The collision bound 3/q^d controls conditioning on distinctness, and a union bound gives the infinite-ratio limit. A separate direct enumeration matched six boxes, including tied largest and tied second-largest sides. Replay: python3 /workspace/branches/498f0eb4-3154-491f-b4b6-81542ff7f3b8/small_box_check.py. The frozen 676,739-triple run is reported corroboration; the supplied verifier was inspected, not executed.

## originality

PASS

The invariant and the strong-product maximum metric are known. The supported distinct claim is the sharp two-range value together with the full equality census in both multiplicity regimes and the joint diameter-pair transition. The inspected graph-wide packing/connectivity bounds, product metric identity, and king-board results do not supply that census or its asymptotics. This is a bounded best-of-knowledge decision, not priority certification.

## value

PASS

Perimeter maximizers are a natural test of the graph distance invariant. The result describes how a second maximal coordinate changes their geometry and multiplicity, including the fixed 2n count despite arbitrary lengthening of a nonsquare board. The full formulas also identify the scale d≈q² at which a typical triple becomes extremal and distinguish the failures of all three pairs, rather than only bounding the triameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
