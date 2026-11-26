# Independent mathematical audit

## correctness

PASS

For X=q−a and Y=1+dq, the characteristic polynomial is (lambda+X)(lambda+Y)^2+zeta. The first two nonleading coefficients are positive and the Routh–Hurwitz margin is 2Y(X+Y)^2−zeta>0. The constant term is −Y² ell_d(q); a negative value yields a positive real root and a zero value yields one simple neutral root with two strictly stable roots. Thus the equivalence uses absence of a growing mode, not strict exponential stability at a neutral length or diffusivity. Neumann inversion gives v=B_d^(-1)u and w=B_d^(-2)u. Testing the stationary equation against u gives sum_j ell_d(q_j)|u_j|²=∫u⁴, excluding every nonzero stationary state when all modal signs are nonpositive. Conversely the coercive quadratic-plus-quartic energy achieves its minimum by compact H¹ embedding into L² and L⁴, and a positive mode gives strictly negative energy at small amplitude; elliptic bootstrapping and odd symmetry yield the opposite pair of smooth patterns. For q≥a and q=0 no mode can be positive. For each 0<q<a solving for d gives the printed threshold function D(q), which diverges at both ends. Maximizing (a−q)(1+dq)^2 gives the unique continuum tangency. Implicit differentiation at the tangency gives D''(q*)=3d*²/[q*(1+d*q*)], where d*q* denotes the product of the starred quantities. A rounded mode first gives excess O(L^−2); strict nondegeneracy then forces every discrete minimizer to satisfy |q_j−q*|=O(L^−1). Expansion on this bounded set of offsets and comparison with the rounded mode give the stated squared distance with a uniform O(L^−3) error, even near half-integer ties. These checks can be replayed from RESULT.md, Proof §§1–5. The supplied NumPy checker and VERIFICATION.md were inspected, not run; the theorem is analytic. It concerns signed fields, identical inhibitor diffusivities, the prescribed cubic and parameter region, and stationary existence, not stability of the patterned states or exclusion of nonstationary attractors.

## originality

PASS

The distinct supported result is the strict global stationary-state criterion including neutral exclusion for this serial-inhibitor cubic system, together with its explicit domain-length obstruction and quantitative commensurability shift. Generic linear-instability criteria, equality of two diffusivities in threshold problems, and discrete dispersion modes are prior; no novelty is claimed for those ingredients.

## value

PASS

In a diffusion-driven pattern model, a linear threshold ordinarily does not decide whether finite-amplitude stationary patterns already exist. The global exclusion identity answers precisely that question, including equality, for a nontrivial feedback cascade. The finite-length obstruction and the size and phase of the domain mismatch quantify when the continuum prediction applies. These conclusions need no claim about dynamical stabilization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
