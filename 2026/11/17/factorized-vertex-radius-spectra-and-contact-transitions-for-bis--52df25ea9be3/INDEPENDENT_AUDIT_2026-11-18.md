# Independent mathematical audit

## correctness

PASS

PASS: For a generic exposing functional on a tree-edge diamond sum, each summand chooses the endpoint with larger coordinate absolute value and its sign, inducing an acyclic orientation. Conversely any tree orientation is realizable by increasing positive weights along its directed edges, and its signed positive-indegree vector is uniquely exposed. Leaf peeling recovers the orientation from its unsigned indegrees, so the enumeration is bijective, without overcounting. Splitting by the bridge direction and t,s incoming leaf edges gives squared norm p+q−t−s+(t+epsilon)^2+(s+1−epsilon)^2, sign multiplicity 2^(p+q−t−s+1_{t+epsilon>0}+1_{s+1−epsilon>0}), producing F=A_p,1 A_q,0+A_p,0 A_q,1. At z=1 counts yield 8·3^(p+q)−2^(q+1)3^p−2^(p+1)3^q. Strict convexity of m−t+(t+delta)^2 locates outer endpoints; the ties at m=1 and p=q give contact counts 16,8,4 in their stated cases and R²=p²+q²+2max(p,q)+1. Central symmetry guarantees unique origin minimum ball and opposite-contact diameters. Independent finite direct orientation/endpoint sums for (1,1),(2,2),(2,3) reproduce 48/504/1584 vertices, R²=5/13/20 and contacts16/8/4.

## originality

PASS

PASS (qualified): Dai et al introduce the general diamond Minkowski-sum object and enumerate different invariants; prior cycle and complete multipartite special families have Euclidean shell/contact theorems but neither contains a bistar with two nonempty leaf classes. This specific factorized signed-indegree count and sharp bistar contact transitions were not found. Full primary Dai text was not recovered and is a documented residual risk.

## value

PASS

PASS: A complete vertex-radius spectrum and contact transition for the smallest nonstar tree class are natural exact convex-geometric invariants, answering a basic face-number question while revealing balance/singleton changes in outer contacts. Its two-parameter factorization is useful without needing a downstream general-tree theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
