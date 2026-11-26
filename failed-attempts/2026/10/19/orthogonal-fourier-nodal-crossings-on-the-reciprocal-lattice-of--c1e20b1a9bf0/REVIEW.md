# Independent mathematical audit

## correctness

PASS

Integrating e^(−2πi(su+tv)) first over the two stated vertical sections of H₀ yields det(A) times the stated cosine quotient. The three projections q=(s−t,t,−s) sum to zero, have unit physical normals 120° apart, and give the equivalent normalized numerator form F/area(H)=−sum_i q_i cos(2πq_i)/(6π² q₁q₂q₃). The hexagon is the Voronoi tile of AM Z² (the shortest-vector half-planes give the six sides and the area agrees with the lattice covolume), so its nonzero dual points are zeros, including the axial points. At integer nodes away from the three axes the first numerator term is quadratic, proportional to sum_i q_i(δq_i)²; its Cartesian trace vanishes because the normals are unit and sum_i q_i=0. Direct substitution gives the specified nonzero complex-square jet with coefficient 3√3/[8mn(m−n)], including the sign of its mixed term. The Hessian is indefinite and nonsingular, so the real-analytic Morse lemma gives exactly two transverse arcs, with the orthogonal null lines specified by the angle law. At integer axial nodes one factor cancels analytically; the linear jets at (0,n),(m,0),(m,m), before multiplying by det(A), are (−δs+2δt)/n, (2δs−δt)/m, (δs+δt)/m. At the other dual nodes all q_i have a common nonintegral residue with nonzero sine, and the numerator derivative is a nonzero multiple of sum_i q_i δq_i. Thus every other nonzero dual zero is simple. The covolume, index three, and O(R+1) contribution of the three lines give both density constants. The statement is about reciprocal-lattice nodes, not all zeros.

## originality

FAIL

The strongest coverage is the mechanically implied classification from the published Li–Sun–Xu hexagonal kernel, not the fact that a generic Fourier integral can be differentiated. Their explicit (3.7), (3.9)–(3.10) give a direct scaling limit. In their homogeneous coordinates write x=(x₁,x₂,x₃), sum x_i=0, and q=((x₁−x₂)/3,(x₂−x₃)/3,(x₃−x₁)/3). By (3.7), Φ_n*(x/n) is a normalized Riemann sum for the Fourier transform of the regular hexagon (boundary weights have vanishing contribution); taking j=(u,v,−u−v) identifies the oblique frequencies s=(x₁−x₃)/3, t=(x₂−x₃)/3. In (3.9)–(3.10) the two Θ products have numerator sine scales 1±1/n after rescaling, and their shared denominator is asymptotic off the three lines to π³q₁q₂q₃/n³. The cosine correction is O(n⁻²). The resulting normalized continuous kernel is (1/3) times the derivative at a=1 of a³∏_i sinc(πa q_i), with sinc(z)=sin(z)/z. It is therefore G=P+(1/3)E P with P=∏_i sinc(πq_i) and E the radial Euler derivative. This published-product limit gives the claimed geometry directly, even without the frozen proof's transform formula. At integer nodes off the axes P has leading term proportional to the product of the three displacement linear forms. Their unit normals are 120° apart, so the cubic product is harmonic; the radial derivative at a nonzero node gives a nonzero harmonic quadratic, and its linear differentiation gives the displayed coefficient and half-angle law. On the integer axes P has just two simple vanishing factors and their radial derivative leaves a nonzero linear term. At the two fractional residues P≠0 and G/P=(π/3)sum_i q_i cot(πq_i). Common residues immediately give zero and derivative proportional to sum_i q_i δq_i≠0. The index and density then follow from the residue classes and removal of three lines. The inspected paper does not state the nodal theorem verbatim, but its explicit product representation, standard limit and first Taylor terms already mechanically entail it. The unavailable sinc paper is not the reason for failure.

## value

PASS

As mathematical content the complete local classification on the natural cardinal lattice distinguishes regular nodal arcs from exact right-angle crossings and explains why the latter have positive density. This is a useful geometric characterization of the interpolation kernel, not just a check that certain sampled values vanish. The value assessment does not credit incremental originality for the mechanically implied result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
