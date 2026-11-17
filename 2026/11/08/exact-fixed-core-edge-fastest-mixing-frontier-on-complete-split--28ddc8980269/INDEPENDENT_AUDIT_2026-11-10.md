# Independent mathematical audit

## correctness

PASS

Group averaging over S_s x S_m preserves every fixed clique transition and cannot increase ||P-J||_op. At invariant cross-edge probability a, the eigenvalues on leaf differences, clique differences and partwise contrasts are 1-sa, 1-ma-st and 1-(s+m)a. Nonnegative diagonal constraints restrict a to 0..min(1/s,[1-(s-1)t]/m). Simultaneously requiring all three absolute values <=r gives exact pairwise lower/upper a bounds; checking their feasibility yields seven and only seven necessary affine lower bounds. The constructed lower endpoint attains the max. At maximal t cross edges vanish and SLEM=1; no irreducible mixing is asserted. Independent rational vertex minimax checked 891 instances, s,m=2..10, 11 rational t-grid values per pair.

## originality

PASS

The full constrained fixed-internal-edge Pareto frontier is not implied by the closest inspected unconstrained optimizer-face or clique-lift results: fixing all core edges at a prescribed t removes previously used feasible optimizers, e.g. s=5,m=2,t=0 gives 3/5 versus unconstrained 1/6. Exact formula is not merely the generic SDP definition.

## value

PASS

Prescribing every peer-to-peer core transition weight while optimizing all other symmetric Markov couplings is a motivated and structurally natural constrained mixing problem. Its exact infinite-family seven-plane frontier and rational four-phase example with plateau give nontrivial behavior absent from an unconstrained SDP optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
