# Independent mathematical audit

## correctness

PASS

With the specified 2π modulation and L² normalization, completing the square gives overlap squared 2√(rt)/(r+t) times exp[−2π(rtx²+ξ²)/(r+t)]. The trace of the product of two rank-one projectors is the squared overlap; after expanding the incoherent mixture and using shift covariance, the two self terms are swapped anisotropic kernels and each cross term is κ_s exp(−πκ_s|z|²). The double integral on the rectangle factors, giving the stated weighted sum of J-products and evenness in u. For D=t∂_t, Q=DJ=t erf(√(πc)t)/√c and R=D²J=Q+2t²exp(−πct²), so a product contributes R_cJ_d+J_cR_d−2Q_cQ_d at the square. At small t use J_c(t)=t²−πct⁴/6+O_c(t⁶) with the corresponding derivatives from its convergent Gaussian power series, giving the claimed −π(s+s⁻¹+2κ_s²)A³/3 coefficient. At fixed s and large t, J_c(t)=t/√c−1/(πc) plus exponentially small error, including its fixed logarithmic derivatives. The leading terms of order A cancel from the Hessian, leaving −√A(√s+s⁻¹ᐟ²+2κ_s⁻¹ᐟ²)/(2π). At A=1 the large-c triple for c=s is (1,1,1)/√s+O(s⁻¹), the small-c triple for c=1/s is (1,2,4)+O(s⁻¹), and the cross term is O(κ_s²) because J R−Q² vanishes at c=0. Thus the intermediate Hessian is +1/(2√s)+O(s⁻¹). Analyticity in A>0 and the signs on both sides of A=1 give at least two distinct sign changes. For fixed s,A, the objective is positive and continuous and decays for |u|→∞ by J_small=O(width²) and J_large=O(width); it attains a maximum, and at A=1 strict local minimality excludes the square for sufficiently large s. Evenness gives a distinct reciprocal maximizer. No exact crossing count, uniqueness, or small/large-area global square optimum follows. Independent bounded replay: with mpmath at 40 decimal digits evaluate M_j(q)=∫_0^1(1−x)(qx²)^j exp(−qx²) dx for j=0,1,2, splitting at k/√q inside (0,1) for k=1,2,4,8,16. For q=πAc, w=πAd the product Hessian is 16A²[(M_2(q)−M_1(q))M_0(w)+M_0(q)(M_2(w)−M_1(w))−2M_1(q)M_1(w)]; combine the product terms with the weights in RESULT.md. For s=100 and A=0.001,1,10000 this gave −8.146393835963×10⁻⁸, 0.04065310698743, and −385.8368252347. These diagnostics are separate from the asymptotic proof. The uploaded checker was inspected, not executed.

## originality

PASS

Pass the reentrant square-aspect stability and resulting reciprocal nonsquare maximizers for the balanced reciprocal-squeeze mixed-state squared Hilbert–Schmidt functional on rectangles. The general mixed-state convolution formalism, single-window localization isoperimetry, and other shape-curvature invariants are not credited as original. The most closely matching inspected primary energy uses a radial single-window kernel; the closest distinct indexed claims differ in kernel, shape class, or observable. No inspected match covers the three-regime statement.

## value

PASS

The minimal reciprocal-squeeze mixture tests whether area and coordinate-swap symmetry enforce square stability for the natural Hilbert–Schmidt shape objective. They do not: the square is destabilized in a whole asymptotic squeezing regime, yet regains strict local stability at large area even at that squeezing. Three controlled asymptotics and existence of nonsquare global witnesses distinguish this from a single numerical symmetry-breaking instance. The conclusion is meaningful without determining the complete phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
