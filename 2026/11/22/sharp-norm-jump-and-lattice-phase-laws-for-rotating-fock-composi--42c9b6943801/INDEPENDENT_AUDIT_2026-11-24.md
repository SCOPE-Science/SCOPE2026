# Independent mathematical audit

## correctness

PASS

Checked RESULT.md lines 48–114. On monomials the diagonal multipliers give the stated product trace norm and contractivity; strong continuity follows by density, and the positive damping margin on compact subsectors gives locally uniform operator-norm convergence of finite diagonal truncations. With decay U and phase V, |V|≤ρU. If the distance exceeds one, increasing the radius from e^{−U} to e^{−|V|/ρ} increases the squared distance at fixed phase; a coordinate maximizing the ratio supplies the approximating lattice and hence the reverse bound as t↓0. The squared-profile derivative has sign h with h′=(1+ρ²)e^u cos(ρu), giving exactly one interior maximum before the half-turn; the tail bound rules out every later lobe. The root equation is only used on the stated first-lobe interval. For small ρ, the phase differs from π/2+arctan ρ by O(exp(−π/(2ρ))), giving the prefactor ρ/e. For large ρ, the root forces sin(ρu)=O(1/ρ) on the second quadrant, then π−ρu=2/ρ+O(ρ⁻²), yielding the asserted large-angle law. The strict maximum gives a fixed gap outside a neighborhood, and monotonicity on either side reduces the local grid comparison to floor and ceiling. Taylor expansion with curvature −Dρ gives a uniform O(t³) even at a nearest-grid tie. The specified real times realize every phase distance in [0,1/2]. The nonrotating case gives norm one for every positive time. Inspected check.py without executing it.

## originality

PASS

The supported distinction is the quantitative initial norm of the difference from identity, including the scalar lattice correction. The closest indexed angular-overshoot result concerns a transient peak of an affine composition operator's norm, and does not supply the same spectral norm problem or discrete sampling correction. The claim is not that Fock diagonalization, semigroup classification, or the small-rotation exponential scale in all contexts is new.

## value

PASS

The result identifies exactly how a compact analytic semigroup can be discontinuous in operator norm at time zero. The maximal rotation-to-damping ratio alone determines the jump in every finite diagonal dimension, and the exponentially small rise above one distinguishes weak rotation quantitatively. The scalar lattice law proves a sharp leading error with no single limiting second-order coefficient, an informative boundary that is missed by a plain O(t²) estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
