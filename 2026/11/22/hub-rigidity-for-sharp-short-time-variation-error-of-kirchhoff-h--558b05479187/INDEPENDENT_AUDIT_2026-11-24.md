# Independent mathematical audit

## correctness

PASS

With a hub median subtracted, each arm is the signed superposition of its tail indicators with measure Df_j plus its adjusted trace as an atom at zero. The sum of total variations is exactly V_star. Each nontrivial tail has cost one, so the operator norm reduces exactly to the largest tail residual. Projection of an arm vector onto the common-arm line and the sum-zero space gives squared weights 1/m and 1−1/m; these spaces impose NN and DN respectively. The normalized coefficients of the hub cut in the DN sine basis yield the stated series, while its NN residual vanishes. For the model half-line NN cut, one may use its square-integrable complementary indicator [0,s] to differentiate the quadratic form. The integral P_t 1_[0,s](s)=erf(s/√t)/2 yields L′(z)=2 erfc(z)−erfc(z/√2). For the NN and DN residuals, reflection contributes opposite tails; summing the two squared norms cancels the cross terms and recovers twice the whole-line squared norm because the missing negative half of that line error is exactly the squared reflected tail. The whole-line constant is the integral of erfc(u)^2 over u≥0, equal to (2−√2)/√π by integration by parts. This gives J_m=2(1−1/m)L_∞−(1−2/m)L. The Gaussian tail hazard is strictly increasing (erfc(z)<exp(−z²)/(√π z) for z>0), so the erfc ratio in L′ increases from one to infinity, giving a unique peak. Independently reproduced rational enclosures using the Taylor series with alternating remainders, Machin’s π bounds and rational square-root bounds give L′(.99)>0, L′(1)<0, L(1)<.396617 and L_∞>.3304946. With |L′|≤2 these imply sup L<.42<4L_∞/3. For the compact transfer, use even reflections at Neumann ends and odd reflection at the Dirichlet end in the whole-line heat convolution. In the hub zone these extensions agree with the half-line extensions within a fixed radius for x≤1/2; for x>1/2 they are constant locally. The discarded tails are exponentially small in L², with the unbounded half-line tail integrated using Gaussian decay. In the interior zone and the leaf zone the same local comparisons give the free-line and NN profiles, respectively. The quadratic form derivative at the moving cut uses only P_t g_s(s) and P_2t g_s(s), so its hub comparison also has exponentially small error uniformly. Since L′(0)=1, the derivative is strictly negative for s≤ε√t when m≥3 and t is small. Outside this strip the positive lower bound of L(z) on z≥ε and the strict leaf and bulk gaps separate every other tail from s=0. A Hilbert-space norm equality for the superposition requires all signed maximizing residuals to lie on the same positive ray. Injectivity modulo constants, and the presence of a third arm, exclude this for distinct whole-arm cuts. This gives the exact extremizers and the displayed coefficient. The checker was inspected, not executed; the profile sign checks and the analytic localization support the eventual-time claim, not any explicit threshold or all-time rigidity.

## originality

PASS

Pass for the eventual exact norm and whole-arm classification for the specified star variation and heat boundary conditions. The heat kernel, separated star modes, and jump/cut reduction have precedents; the decisive comparison of the branching hub, bulk, and leaf cases and its compact-time equality conclusion are not supplied by the inspected precedents.

## value

PASS

The compact metric star is the basic local model for a branching Kirchhoff vertex. The sharp norm detects branching at the level of the leading coefficient and of equality, rather than only giving an O(t^(1/4)) L² approximation bound. In particular the result distinguishes true hub concentration from cuts within a shrinking boundary layer and proves the exact optimizer for a nonempty range of times. This resolves a natural comparison between three possible local geometries; it does not require an all-graph extension to be useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
