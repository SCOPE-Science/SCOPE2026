# Independent mathematical audit

## correctness

PASS

For fixed k≥2 a labeled tree can be injected into the host in n d_n^(k−1)(1+O_k(1/d_n)) ways by choosing a root and then fresh neighbors; excluding a fixed number of vertices changes the count only relatively o(1). Dividing the summed Cayley count by k! counts distinct edge-trees. For a tree with h extra possible internal host edges, exactly kd_n−2(k−1)−h edges must be closed and its k−1 edges retained. Thus the first moment is asymptotic to (k^(k−2)/k!) n (d_np_n)^(k−1) exp(−L_n), yielding e^(−c)/(k k!). Exact events for different trees on overlapping vertex sets are incompatible; every fixed ordered disjoint tuple contributes the product times q_n^(−b), where b≤k² binom(r,2) counts double-closed cross-edges. This factor tends to one uniformly, and all factorial moments tend to the corresponding Poisson moments. A cyclic component has a spanning-tree witness with closed boundary and at least one additional open internal edge; the mean number of boundary-only witnesses is bounded, and the extra independent-edge factor is O_k(p_n). Cyclic components hence vanish in probability. At k=1, the joint isolation probability is q_n^(rd_n−b), giving the same moments directly. The k=2-window isolate count has mean e^(−c/2) sqrt(n/log n), and summing covariances only over adjacent vertex pairs gives relative variance at most 1/mean+d_np_n/(nq_n)→0. Weak convergence on integer counts gives the stated zero-count probability. The window concerns marginal counts at fixed c and k; it does not assert a connectivity threshold, a monotone last-occurrence event, or growing-k uniformity.

## originality

PASS

Pass for the fixed-order finite-mean windows over all prescribed high-degree regular hosts, with no expansion, connectivity or codegree requirement. The complete-host case already follows from fixed-component Poisson theory, and the k=1 cycle-power case is directly covered. The known finite covariance formula and indexed shape-marked cycle-power specialization do not give all factorial moments on arbitrary hosts. The checked nearby random-position models and graph-expansion regimes do not supply the claimed host-independent centering and constants under these assumptions.

## value

PASS

At the same explicit centering the component-order count has the same nondegenerate Poisson law on complete, disconnected and otherwise arbitrary growing regular hosts. This identifies separate observable windows and quantifies the coexistence of two-vertex-component extinction with a diverging isolate population. Exact q-centering matters because replacing it by a linear approximation can shift the exponent by order (log n)²/d_n, not necessarily o(1). The result gives a usable extinction probability without claiming anything about overall connectivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
