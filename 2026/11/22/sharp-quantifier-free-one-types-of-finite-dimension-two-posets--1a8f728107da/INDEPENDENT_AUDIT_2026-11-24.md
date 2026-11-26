# Independent mathematical audit

## correctness

PASS

For each unmarked realization the two linear orders give prefix masks A,B of U; below/above sets are A∩B and U\(A∪B). For marked rank pair (i,p_i), opposite cuts (i−1,p_i) and (i,p_i−1) make i incomparable, and every other parameter's two-cut change leaves its type unchanged since both ranks are distinct. Each edge is the unique one crossing its own first-coordinate threshold, so every edge is a bridge. Contracting these m equal-signature edges gives the upper bound (m+1)^2−m. For reverse ranks the possible nonempty below or above sets are intervals and cannot occur simultaneously; every interval is obtained with the indicated cuts, and (0,m) realizes the empty comparison. One rational point in each chosen open cut rectangle, with all coordinates distinct, realizes the entire witness in a single poset whose coordinate orders are linear. Adding the m equality types gives (m+1)^2, which is also a lower bound for the size of any witness by counting vertices. The empty marking is witnessed by one vertex. Replay: python3 /workspace/review_evidence.py, posets section, independently enumerates m=0 through 6 with bitmasks; it does not prove the arbitrary-m result. The frozen supporting review's phrase ‘all-arity’ is not the audited statement: the theorem has one free variable and unbounded parameter count.

## originality

PASS

Best-of-knowledge pass for the joint named predecessor/successor signature count in the pure finite poset reduct. The closest named-order and permutation-graph statements count different data, and the general type bounds do not supply the loss of exactly m at the optimum or its simultaneous antichain realization. No claim of historical priority is made.

## value

PASS

An exact one-variable type-growth invariant for a standard finite order class, with a proof of the precise penalty from forgetting the named orders and a simultaneous minimum-size antichain realization. Neither the general growth order nor an arbitrary small-size census explains that penalty or witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
