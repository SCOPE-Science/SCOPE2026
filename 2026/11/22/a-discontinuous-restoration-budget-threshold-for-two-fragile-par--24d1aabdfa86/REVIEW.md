# Independent mathematical audit

## correctness

PASS

For fixed route budget b, the sum of its two edge-failure factors is minimized uniquely at equal efforts by AM–GM. Connectivity is strictly increasing in either route probability given the other (each is <1). After this reduction, write u=exp(−b/2), v=exp(−(B−b)/2), p=uv=exp(−B/2), and w=u+v. The product of failure probabilities is [(1−s)+2su−su²][(1−s)+2sv−sv²]. At fixed p its terms depending on w are −s(1−s)w²+[2s(1−s)−2s²p]w; thus success is a strictly convex quadratic of w when 0<s<1. The achievable w interval is [2√p,1+p], with only the midpoint of the route-budget split mapping to its lower end and only the two concentrated choices to its upper end. Strict convexity excludes every intermediate point even when the endpoints tie. For x=exp(−B/4), the endpoint difference is s(1−x)²[(1−s)(1−x)²−2x²]. The bracket has a unique zero in (0,1) at x=1/(1+√(2/(1−s))). The ordering, unique threshold, all three tie allocations and 32/81 at s=1/2 follow. At s=1 success is strictly increasing in w (linear coefficient 2p), and at s=0 every plan gives zero. For one investable edge per route the joint failure is (1−s)²+s(1−s)(exp(−b)+exp(−(B−b)))+s²exp(−B), uniquely minimized at b=B/2 by AM–GM. This checks all nonnegative allocations, not merely symmetric ones. The frozen symbolic and finite-grid checker was inspected, not executed. The proof applies only to equal costs/efficiencies, independent gates and links, and static two-terminal connectivity; the minimality is in the specified identical two-route family.

## originality

PASS

Best-of-knowledge pass on the closed viability-dependent threshold, all optimizers, and shortest-route contrast. The closest published comparator shares the same two-route reliability architecture and the same qualitative switch, not the effort law or gate parameter; no novelty is credited to the qualitative switch by itself or to the elementary optimization methods. The empirical source and classical allocation searches do not imply the exact parameter family identified here.

## value

PASS

The exact dependence on site viability is useful: it shows when independent backup beats further investment in the first serial route, how the switch moves to infinity as the gates become perfectly viable, and why no asymmetric compromise can be globally optimal. The single-edge comparator separates the effect of serial complementarity from gate fragility alone. This is an exact reliability benchmark under specified response and independence laws, not evidence for a field budget.

The dated certificate retains the supplied scientific assessment, sources and limitations.
