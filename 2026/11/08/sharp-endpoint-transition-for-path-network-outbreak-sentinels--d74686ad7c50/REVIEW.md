# Self-review: sharp endpoint transition for path-network outbreak sentinels

## Correctness — PASS

The result concerns uniform-source eventual detection on an undirected homogeneous open-edge path with exactly \(2\le k<n\) error-free monitors. Conditioning on all possible source locations gives the exact objective in terms of two outer and \(k-1\) inner gap rewards. Their first differences, \(b_t=p^t\) and \(h_t=p^t[1+t(1-p)]\), decrease strictly. Therefore selecting the greatest feasible marginal rewards is necessary and sufficient for the global optimum, including ties; the gap exchange arguments prove the balancing inequalities. Restricting both endpoints to be monitored leaves \(N=n-k\) gap units distributed evenly among \(m=k-1\) interior gaps. The global test is exactly \(h_{\lceil N/m\rceil}\ge b_1\). Differentiating its one-variable polynomial establishes the single interior threshold for \(q\ge2\); its fixed-\(c\) logarithmic expansion proves \(1-p_q\sim2/q^2\). All domain restrictions and the separate \(q=1\) case are explicit.

A source-enumeration and independent-percolation checker performs 6,546 assertions/diagnostics on finite paths, exact rational parameters, optimization ties, and threshold examples. These checks are supporting evidence, not universal proof. There is no claim of empirical validation.

## Originality — PASS within evidence, with residual priority risk

The 2007 Leskovec–Krause–Guestrin–Faloutsos–VanBriesen–Glance paper sets up general outbreak-detection optimization and submodularity but the inspected technical report does not state this all-size exact path-gap solution. The 2013/2014 Khanna–Lucier influence-maximization setting **does cover the entire model by an exact undirected-connectivity equivalence**: our objective is the expected independent-cascade spread of sentinels divided by \(n\). That broader framing and generic approximation guarantees do not, in the inspected material, imply the precise path gap allocation, endpoint threshold, uniqueness-or-tie regimes, or the sharp \(q^{-2}\) asymptotic. The comparison is of implications, not titles or application fields.

The 2017 Holme source considers epidemiological node importance/detection time on small graphs, and the 2019 Colman–Holme–Sayama–Gershenson source evaluates heuristic sentinel placements with distinct time-sensitive objectives. Semantic index queries for path sensors, homogeneous independent cascade, margin/gap laws and critical endpoints returned no matching claim. The closest indexed normalized-path endpoint-sampling result concerns a spectral observability Gramian, not epidemic reachability; the closest discounted hitting result concerns a complete bipartite graph and a different objective. This is not a proof that no earlier equivalent result exists. In particular, historical influence-maximization, stochastic covering, and facility-location specializations remain a realistic risk.

## Value — PASS

An exact all-size placement rule and nontrivial critical transmission probability resolve a genuine network-surveillance design issue that heuristic or submodular approximation guarantees do not resolve: when does monitoring both path endpoints become optimal rather than interior-only placements? A sharp switch and the \(1-p_q\sim2/q^2\) scale exhibit a structural relationship between path length, fixed monitor budget and transmission reliability. The exact \(n=10,k=3\) reversal is not an arbitrary isolated witness: it illustrates the proved family. Although the idealized eventual-detection model does not prescribe practical surveillance schedules, the result is a reusable analytic benchmark.

## Closest literature and limitations

- Leskovec et al. (2007), *Cost-effective outbreak detection in networks*, doi:10.1145/1281192.1281239; technical report https://www-cs.stanford.edu/~jure/pubs/detect-techRept.pdf. The report specifies June 2007 without a day; the August 12, 2007 conference date is the earliest public day verified for this cited work.
- Khanna and Lucier (2013/2014), *Influence maximization in undirected networks*, doi:10.1137/1.9781611973402.109; public manuscript https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/Influence-Maximization-in-Undirected-Networks.pdf. The exact model reduction is acknowledged; the specific optimum is not derived in the inspected sections.
- Holme (2017), arXiv:1708.06456; Colman et al. (2019), doi:10.1371/journal.pcbi.1007517. Their epidemiological sensor objectives differ materially.
- Only paths, homogeneous independent undirected transmission, uniform initial-source selection, perfect eventual detection and a fixed monitor budget are proved. Independent scientific audit and field validation are absent.

Self-review: passed. Independent audit: not yet performed.
