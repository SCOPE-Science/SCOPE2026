# Independent mathematical audit

## correctness

PASS

The real unsigned incidence matrix satisfies B^*B=H₀+2I even when amplitudes are complex. Alternation at the degree-two vertices forces a single scalar per petal, with hub constraint that the odd-petal scalars sum to zero. On F the shifted eigenvalue equation is simply (d_e−z)x_e=0. A nonzero petal scalar uses the entire petal, and the restricted scalars on eligible petals therefore give e_z+(o_z−1)_+ dimensions. A diagonal matrix preserves F precisely when it maps each supported even-petal vector and each odd-pair difference back into that parametrization: each active petal must be constant, and the two values on an odd pair must coincide. With a single odd petal there is no odd support. For absorption the imaginary part of x^*Hx is −Σ_e γ_e|x_e|², so an undamped eigenvector has support only at zero rates. The necessary and sufficient placement is one hit per even petal and all but at most one odd petal, including the cases dim F=0. With equal-length odd petals the dimension across energies is Σ_z(X_z−1)_+, where X_z is binomial with success probability q^(−ℓ). Hence E R_k=kq^(1−ℓ)−q[1−(1−q^(−ℓ))^k] and the strong law gives the stated limit; normalization by dim F=k−1 leaves the same limit. Nonatomic independent values are almost surely not constant on any of the finitely many petals. The proof needs no numerical certificate; checker.py and its output were inspected, not run.

## originality

FAIL

No inspected indexed flower result gave the identical combined display, but the deterministic dimension is an immediate specialization of the published general signless line-graph multiplicity theorem, applied to the subgraph of the selected onsite level. The entire-space invariance and absorber count are direct consequences of those dimensions. The iid part then uses ordinary occupancy of nontypical monochromatic petals, with no additional spectral or probability result beyond evaluating the binomial zero-count. The exact special-case numbers are not independent of the known broader coverage.

## value

FAIL

The original-band retention fraction can be useful for this graph, but this submission supplies a direct graph specialization of the general rank formula and an elementary finite-level occupancy evaluation. After accounting for that implication, no independent obstruction, spectral invariant, or nonmechanical statistical calculation remains. The distinction from complete dark-state capture is correctly observed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
