# Independent mathematical audit

## correctness

PASS

For an ordered k-monitor set in an n-vertex path, the unmonitored vertices split into outer lengths L,R and k−1 interior lengths g_i with total N=n−k. Conditioning on the uniform source and open edge path yields the exact nD=k+B(L)+B(R)+sum G(g_i), B(g)=sum_(t=1)^g p^t and G(g)=2B(g)−g p^(g+1). Differencing produces strictly declining outer marginal b_t=p^t and inner marginal h_t=p^t[1+t(1−p)]; their discrete concavity proves the exact N-largest-marginals selection rule with all ties, gap balancing and dominance of interior gaps. Monitoring both endpoints corresponds to allocating all N slots among m=k−1 interior sequences with longest gap q=ceil(N/m), and is optimal iff h_q≥b_1=p. For q≥2, F_q(p)=p^(q−1)(q+1−qp) has a single interior maximum at p=1−1/q², unique nontrivial crossing, strict phases and increasing roots; Taylor expansion logF_q(1−c/q²)=(c−c²/2)/q²+O(q^(−3)) proves 1−p_q~2/q². q=1 follows directly. Independently enumerated all percolation patterns, sources and sentinel sets for n≤7 at three rational probabilities, 639 cases; small checks corroborate the all-n proof.

## originality

PASS

The epidemic detection functional is exactly equivalent to expected influence of the chosen monitors by undirected live-edge symmetry: no novelty claimed for the model or generic submodular framework. The strongest earlier specific two-sentinel path theorems already cover the k=2 threshold/phase diagram. The surviving original all-k contribution is a complete arbitrary-k top-N interior/boundary marginal characterization, all ties, and exact cutoff q=ceil((n−k)/(k−1)) for k≥3, with phase monotonicity. A 2011 thesis gives polynomial-time optimal path influence selection but the available abstract does not imply this explicit symbolic optimizer classification; its inaccessible full text is a material originality risk.

## value

PASS

All-k exact selection of perfect monitors on a natural path network and the onset of forced endpoint monitoring are interpretable optimization invariants, beyond known generic approximation and two-sentinel cases. The strictly diminishing marginal merge rule classifies all optimal placements and ties for every n,k,p, and the q-dependent threshold answers a natural design transition that a polynomial instance solver alone does not articulate. It is a substantive structural classification for k≥3, not an assertion that the independent-cascade model or k=2 threshold is new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
