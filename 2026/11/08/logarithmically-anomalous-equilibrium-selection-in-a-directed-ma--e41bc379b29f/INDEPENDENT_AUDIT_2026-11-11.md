# Independent mathematical audit

## correctness

PASS

For m≥3 with all c_i>0 the exact ratio recurrence is q_i'= (1-c_{i+1})q_i+c_{i+1}q_{i+1}; this primitive cyclic stochastic matrix has invariant weights proportional to 1/c_{i+1}, proving consensus at the claimed beta_m. Gamma–Dirichlet representation supplies independent U_i~Beta(a,a) and G_i~Gamma(2a,1), so the numerator is a sum of iid centered (U_i-1/2)/G_{i+1}, independent across shifted indices. For a>1 its variance gives (2a-1)/[4(2a+1)(2a-2)]. For a=1 exact tail expansion is Pr(|Y|>t)=1/(24t²)+O(t^-3), hence truncated variance (log t)/12+O(1), Lindeberg–Feller with b_m²=m log(m)/24 yields the critical N(0,1/24) for sqrt(m/log m)(beta_m-1/2). The denominator obeys the strong law, and the complete-mixing ratio is exactly Beta(ma,ma). Independently confirmed the tail series symbolically; these asymptotics are established by the proof, not a finite simulation.

## originality

PASS

Best-of-knowledge original fixed-shape Dirichlet equilibrium selection fluctuation transition for the directed cyclic specialization. The defining many-loci paper covers the deterministic operator, invariant fibers and orbit convergence, not a growing-loci random-selection central limit theorem with inverse-gamma criticality. A published two-locus exact equilibrium law has fixed dimension and does not dominate the m→∞ transition.

## value

PASS

Exact random equilibrium selection is a natural question for this nonlinear recombination model, and the logarithmic critical fluctuation scale at uniform simplex initialization identifies a genuine heavy-tail boundary, contrasting sharply with the all-to-all beta law; not merely a numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
