# Scientific review: exact infinite-temperature fluctuations in the \(N\)-queens lattice gas

## Correctness — PASS

The domain is the uniformly sampled size-\(N\) subset of an open \(N\times N\) board, with physical Hamiltonian \(JH_N\). The proof first evaluates the attack graph's incidence count \(W_N=\sum_v\binom{d_v}{2}\), including its parity-sensitive mixed-diagonal term, and then exactly separates ordered pairs of attack edges by whether their endpoints use two, three or four sites. Uniform fixed-cardinality hypergeometric probabilities give the claimed rational variance. The thermodynamic statement follows at each **fixed** board size from \(C_N(T)=\operatorname{Var}_T(E_N)/T^2\), before the board-size limit; no exchange of limits is presumed. The standalone `check.py` directly counts all configurations for \(N=2,3,4,5\), checks exact finite formulas through \(N=80\), and passes 491 equalities. The infinite proof is not based on the finite checks.

## Originality — PASS, with residual publication risk

The closely matching Liu–Liao–Wang paper, arXiv:2605.10326 (first public 2026-05-11), defines the **same unrestricted fixed-cardinality model** and derives its infinite-temperature mean energy, while its specific heat is obtained from Monte Carlo. Its full relevant model, analytical and specific-heat sections and conclusion do not give the exact variance or the asymptotic coefficient \(31/18\). The 2009 Zhang–Ma approach uses a different constrained permutation model and diagonal energy. Polson–Sokolov 2024 addresses counting and sampling, without the claimed second-moment invariant. Searches for exact quantum/queen-lattice analogues, queen-graph edge-count variance and the proposed coefficient yielded no stronger published statement in the checked sources. The generic edge-indicator covariance identity is explicitly credited as standard and is not the asserted novelty. An unindexed evaluation of attack-graph degree moments remains a genuine residual risk; absence from search indexes is not a proof of priority.

## Value — PASS

The recent physical study makes the high-temperature energy and the specific-heat curve central quantities but has no exact heat-capacity coefficient at the infinite-temperature endpoint. The result supplies a parameter-free benchmark \(31/18\) and the complete finite-size parity correction, enabling exact calibration of high-temperature sampling and derivatives of thermodynamic integration. The structural source of the number is a delicate positive/negative cancellation of three edge-interaction covariance classes with respective limits \(5/3\), \(67/6\), and \(-100/9\); it is not an arbitrary small-board enumeration, a renaming, or an unsupported extrapolation. No finite-temperature phase assertion is included.

## Scope and unresolved risks

A general graph-variance identity reduces the calculation to attack-graph incidence sums; a separately published explicit identity for those sums, if found, could weaken priority. The paper's finite-temperature heat capacity is empirical and is not promoted here to a theorem. The high-temperature and large-board limits are ordered, not interchanged. This review is not independent validation.

Self-review: passed. Independent audit: not yet performed.
