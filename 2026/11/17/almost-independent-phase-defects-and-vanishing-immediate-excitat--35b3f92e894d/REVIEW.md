# Independent mathematical audit

## correctness

PASS

For synchronous threshold-one 3-state Greenberg–Hastings dynamics on connected Q_d (d≥1), a period-three trajectory either rotates all vertices through 0→1→2 or is all-zero fixed: any persistently resting zero adjacent to a rotating vertex would be excited, and connectivity propagates this. Thus primitive immediate period three is equivalent to X=0 defects, where each Y_v indicates no neighbor with color C_v+1. Conditioning on initial color gives p=(2/3)^d; two centers at distance one have joint probability (3/4)p², distance two (9/8)p², and distance at least three independent because closed one-neighborhoods are disjoint. Summing covariances across d+binom(d,2) neighbors gives Var X=µ+Np²(d²−5d−16)/16, µ=(4/3)^d, switching sign precisely between d7 and d8. Dependence ball at Hamming distance ≤2 has M_d=1+d+C(d,2); Arratia–Goldstein–Gordon 1989 Theorem1 with its norm 2TV and b1=N M_d p²,b2=Np²(3d/4+9C(d,2)/8),b3=0 gives standard count TV ≤pB_d(1−e^{-µ}); Theorem3 gives vector-TV ≤2Np²(B_d+1). These tend to zero since Np²=(8/9)^d. Greedy packing of disjoint closed neighborhoods selects at least ceil(N/M_d) independent defect indicators and bounds P(X=0)≤(1−p)^ceil(N/M_d)≤e^{-µ/M_d}→0. Independent reimplementation enumerated all 9,81,6561 initial configurations for d=1,2,3 obtaining (waves,E,Var) respectively (0,4/3,2/9),(0,16/9,56/81),(252,64/27,1024/729), agreeing with published formula. Frozen tools/defect_check.py source checked for direct 3-step dynamics and exact pairs. Finite enumeration is only corroboration of all-d analytic theorem.

## originality

PASS

Best-of-knowledge PASS for the exact hypercube color-defect covariance sign reversal, growing-intensity full-vector independent-site approximation and initial period-three rarity. Chen–Stein theorem, GH dynamics and random-graph Poisson windows are prior and explicitly acknowledged. The earlier rarest-color Erdős–Rényi result has random edges and mean approaching a constant, so it does not directly imply hypercube local pair correlations with µ diverging.

## value

PASS

An exact dimension-eight crossover from underdispersion to overdispersion, combined with asymptotic independence of the entire rare spatial defect pattern while mean defect count diverges, is a motivated fine-scale stochastic-dynamical phenomenon on a canonical graph family. It separates local rarity from global immediate-cycle rarity; the exact local correlation coefficients would be useful in testing random excitation approximations. Standard Chen–Stein technology is not claimed new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
