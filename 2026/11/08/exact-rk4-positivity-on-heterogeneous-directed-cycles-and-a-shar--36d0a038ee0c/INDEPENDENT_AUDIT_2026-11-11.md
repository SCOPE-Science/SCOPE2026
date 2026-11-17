# Independent mathematical audit

## correctness

PASS

For n>=5 with strictly positive vertex-specific one-way rates, the RK4 polynomial has no wrapped walks of <=4 jumps. Exact path expansion using complete homogeneous symmetric polynomials yields five entry types by forward distance. Distance 0,2,4 stay strictly positive (Taylor remainder/discriminant), while distance-one entry is hr_iF_{r_i,r_{i+1}}(h) and distance-three is h³Πr(4-hΣ_4r)/24. The negative discriminant for F' makes F strictly decreasing with one root and proves a single sharp intersection cutoff. Independently computed exact rational RK4 matrix powers for three heterogeneous/homogeneous n=5,6,7 examples and checked every entry against the symbolic formulas, all row sums one. Symbolically checked F(2/(a+b))=1/3 and the single-defect cubic substitution; these support the analytic no-reentry proof. The four-maximum plateau criterion follows because each one-jump root is >1/M and 4/W is =1/M iff W=4M. Diagonal <=1 in a nonnegative stochastic matrix gives Mh*<α, while the single-high-rate defect yields sharp supremum α; the changeover R_c is the unique root >1 of 3R³-9R²-15R-43. No correctness defect found.

## originality

PASS

The distinct final claim is the uniform-in-cycle-length heterogeneous positive-rate sharp local formula, all-step no-reentry, four-maximal plateau iff, optimal global gain and exact single-defect transition. The earlier unit-rate case is credited and not new, while the inspected general primary theorem gives a method but no such parametric identity. Best-of-knowledge originality passes with residual unindexed-source risk.

## value

PASS

Unmodified RK4 on finite nonreversible Markov cycles is a natural numerical diffusion problem. An exact timestep law valid for arbitrary heterogeneous rates, using only adjacent pairs and four consecutive rates rather than a full matrix positivity test, directly characterizes a meaningful CFL frontier. The exact plateau criterion explains when RK4 genuinely outperforms forward Euler; the sharp universal gain and one-defect phase switch reveal nontrivial structure. These are motivated complete family-level invariants, not arbitrary isolated calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
