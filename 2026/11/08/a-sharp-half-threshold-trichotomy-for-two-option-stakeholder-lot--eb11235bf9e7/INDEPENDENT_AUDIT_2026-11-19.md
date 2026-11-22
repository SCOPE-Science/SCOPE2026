# Independent mathematical audit

## correctness

PASS

The frozen source concerns only n>=1, 0<=K<=n, public 0<a<=b<=1 and a finite known rational grid with both endpoints, normalized binary utilities (1,0)/(0,1), deterministic finite membership queries and at most K DISTINCT contacted agents. At t=1/2 all accept for b<=1/2. For a>1/2 the right and left closed acceptance intervals are disjoint; OPT is the size of the minority orientation. A query at t=1 identifies every contacted orientation, so pure majority among K queried has regret at most max(0,U-(K mod 2)), U=n-K. The lower adaptive transcript assigns alternating orientations on first contacts (q<=K), consistently answering any repeated queries using threshold a; its imbalance is d=q mod 2 and completing all U=n-q unknown agents against the output yields >=max(0,n-q-d) regret, which bounds below the target. Gap output only worsens the regret. For a<=1/2<b, all K contacted intervals can be learned exactly by finite-grid bisection, and optimizing queried overlap yields <=n-K extra rejections. For the lower bound, respond to all queries as right orientation threshold a, then choose untouched types based on output t: right threshold b if t<b (global comparator t*=1), left threshold a if t>=b>1-a (global comparator t*=a), otherwise left threshold b if b<=t<=1-a (comparator t*=a). In every case untouched agents reject output and all agents accept comparator; a<=1/2,b>1/2 make the cases exhaustive, including equality. When K=n regret=0; when K=0 the constructions still apply; a=b=1/2 is common-feasibility, a=b>1/2 is strict. Independent exact rational exhaustive full-observation minimax over 70 cases (5 endpoint subfamilies, n=1..4, K=0..n) matched the formula. This check is NOT a proof over all grids, n or adaptive policies; the preceding transcript arguments are the uniform proof.

## originality

PASS

Best-of-knowledge novelty is the full deterministic two-option, public-threshold-range, distinct-contact-budget phase diagram, not the known full-information interval sweep or the generic n-K upper bound. Teh and Goldberg arXiv:2610.37828 Sections 6 and Appendix H prove a matching lower bound only for m>=3: the construction requires a third alternative to let contacted agents accept both pure options while remaining nondegenerate. Their Appendix E.1 solves fully elicited m=2 interval overlap, and Appendix I Theorem I.3 exactly expresses the worst gap after a fixed history, but it does not evaluate the minimax over all adaptive-contact policies for public a,b or the odd-K correction. Choo–Goldberg–Teh studies unanimity, and the related stochastic threshold law studies fully observed random profiles, not deterministic worst-case partial-contact regret. Searches did not establish an earlier all-parameter equivalent; an inaccessible same-authors 2026 distance-loss NeurIPS paper is a documented risk, not represented as read. Novelty is qualified and not independently certified.

## value

PASS

This resolves the first genuinely excluded alternative count in a central recent membership-query minimization problem. With two alternatives, normalized utilities force interval acceptance, and public threshold bounds create three mathematically different information regimes: universal center feasibility, mutually exclusive orientation majorities with an odd-contact parity gain, and an adversarial mixed-threshold regime restoring the full n-K obstruction. The complete finite-grid all-n,K classification is an interpretable natural minimax invariant needed to know when deterministic stakeholder elicitation can or cannot improve worst-case outcomes. It is more than a numeric curiosity or routine re-labeling of the m>=3 proof, whose nondegenerate lower construction is impossible in dimension one; the mixed case needs a new exact adversarial completion. It makes no claim on randomized algorithms, total number of queries, real continuum thresholds, m>=3, or average-case performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
