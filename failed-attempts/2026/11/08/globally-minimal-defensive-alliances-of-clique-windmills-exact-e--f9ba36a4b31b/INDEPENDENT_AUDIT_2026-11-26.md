# Independent mathematical audit

## correctness

PASS

A selected outer vertex in petal i requires k_i >= floor(m_i/2)+1-h, where h indicates the hub; the selected hub requires sum k_i >= floor(N/2). Without the hub, any occupied petal supplies a minimal subset of exactly b_i+1 vertices. With it, global minimality forces k_i <= b_i, since otherwise the petal supplies a proper alliance. The sum of these caps is (N-q)/2 and reaches the hub threshold exactly for q <= 1, forcing saturation of every cap. Deleting any vertex other than the hub now fails the hub threshold, and any nonempty hub-free subset fails a petal threshold. This applies also to singleton petals and equal powers in the counting polynomial. For m_i=2 the two counts are r and 2^r, with missing sizes 3 through r for r>=3. The proof is unrestricted; the frozen verification and verify_alliance.py were inspected but their finite execution was not rerun. The code enumerates proper submasks until a witness is found or all have been ruled out.

## originality

FAIL

The two earlier findings give the full classification, parity cutoff, polynomial and friendship gap on m_i>=2. Leaves are outside their stated domain but do not yield a distinct substantial result: each singleton is an alliance, so can never occur in any other global minimum. With L leaves removed and nonleaf total N0, all nonhub thresholds are unchanged. If floor((N0+L)/2) rises above floor(N0/2), no hub minimum can survive, since its cap was at most floor(N0/2); otherwise every nonleaf alliance has unchanged feasibility. Add Lz for the leaves. If only one petal remains, the pruned graph is a clique with a single elementary size threshold; if none remain there can be no hub minimum for r>=2. This recovers the exact extension without a new mechanism.

## value

FAIL

A structural parity cutoff and arbitrarily long gaps would be useful for this natural family, but these are already present in the matching findings. The only remaining change, admitting pendant singletons, contributes their singleton terms and a direct threshold suppression; it does not give an independently substantial classification or new phenomenon warranting repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
