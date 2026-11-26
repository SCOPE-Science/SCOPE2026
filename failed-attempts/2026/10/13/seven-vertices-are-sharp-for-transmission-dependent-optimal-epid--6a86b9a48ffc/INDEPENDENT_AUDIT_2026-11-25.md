# Independent mathematical audit

## correctness

PASS

With a single seed u the sole path to v must transmit in order. Each next-edge race uses a fresh path vertex's clocks and succeeds with probability p=β/(β+γ); off-path transmissions do not change the race or create alternate routes. Thus marginal detection is the uniformly averaged p^distance score, without asserting independence of siblings' transmissions. I inspected the frozen proof, verification and checker. Independently I generated unlabeled shapes by leaf attachment and canonical rooted tuples minimized over possible roots, then used all independent bond-edge states as an algebraic representation of the distance polynomial (not as a joint Markov SIR model). For each v, expected retained-component size is the sum of p^distance over u; grouping by retained edge count gives an exact Bernstein basis. Direct integer coefficient comparisons for shapes counted 1,1,2,3,6,11 show fixed full argmax in 22 classes, with any unequal dominated score strictly smaller in the interior. For the two remaining shapes I reproduced the candidate scores and strict noncandidate exclusions. The broom gap is p(1−p)(1−p−p²), so the only interior root is (sqrt(5)−1)/2 and β/γ is the golden ratio there. The two-claw gap is p(1−p)(1−2p), with both hub scores identical and the bridge joining their tie exactly at 1/2. The order-one case is immediate. Replay: python3 -I /workspace/review_math.py 2.

## originality

FAIL

Verified prior coverage, not an access-based rejection. Coroničová Hurajová, Gago and Madaras (2018), On decay centrality in graphs, use exactly the equivalent score (nP_v−1), including full tie blocks. Their Table 1 establishes stability of the full ranking for all trees of orders 4–6 and for 9 of the 11 seven-vertex trees. Their Figure 1 and accompanying ranking give the same two-claw and its complete maximizing phases, including the three-way tie at 1/2. The stronger full-ranking census therefore already gives the lower bound and excludes any further shapes after the broom is checked. The only needed supplement is the direct small broom distance-polynomial comparison; the epidemic connection is a normalization of a unique-path marginal, not another optimization problem.

## value

FAIL

The detection objective is meaningful, but the frozen contribution as a new sharp theorem mostly reproduces an existing stronger stability census and one of its exact worked examples. The remaining broom threshold is a direct comparison of distance shells at two vertices; relabeling decay centrality as a unique-path detection marginal gives no additional independent invariant, classification, or model-level phenomenon. No standalone repair of adequate scientific substance was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
