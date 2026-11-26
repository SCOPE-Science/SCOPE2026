# Independent mathematical audit

## correctness

PASS

Root circular spacings at a specified sampled vertex (not at the first vertex after a fixed coordinate angle); then the uniform simplex density is valid. On the exclusion event the unique long gap is greater than π; disjointness and Dirichlet slicing give probability n/2^(n-1), independent T=δ/π with survival (1-t)^(n-1), and V of dimension m=n-1, uniform on its simplex. The closing chord and its oriented area contribution are 2cos(δ/2) and -sin(δ)/2. For Q=sum V_j³, the Dirichlet moment formula gives mean 6/[(m+1)(m+2)]; its second moment is [720+36(m-1)]/[(m+1)...(m+5)], which yields the frozen variance. With G_j=L V_j, the remainder in the cubic expansions is bounded by a constant times sum G_j⁵, with expectation O(n^-4) uniformly in L. Thus ΔP=δ+δ²/4+L³Q/24 up to O(δ⁴) and the fifth-power error; ΔA=δ+L³Q/12 up to O(δ³) and the fifth-power error. This verifies the shared exponential leading term and the quadratic difference. For W unit-exponential, the delta-method influence for the cube sum normalized by the cubed sample mean is W³-18W+12 of variance 360, giving variance 360π⁶/24²=5π⁶/8. Its normalized spacing vector is exactly independent of the endpoint gap and L tends to π, which proves the joint independence in the limit. The centering in the formula is the exact conditional mean of the cubic proxy, not of the nonlinear D_n; Scope states this correctly and the nonlinear conditional mean differs uniformly by O(n^-4). I inspected VERIFICATION.md and verify.py without running the frozen script. The finite arithmetic and simulation are diagnostic, not a proof or historical attestation.

## originality

FAIL

The full vector is not quoted verbatim in the inspected sources, but it is mechanically implied by two specifically matching earlier results, not merely by a generic CLT. The marked Wendel result gives exactly the conditional endpoint and uniform sample representation. The earlier cyclic-polygon result proves exactly the same normalized cubic spacing CLT with the same centering and Taylor control. Applying it to the independent normalized spacings and expanding the area and closing chord gives the entire vector, including its apparently distinct second-order difference and fifth-coordinate variance. This is a concrete coverage finding; it does not rely on inferring anything from an inaccessible paper.

## value

FAIL

The conditioned geometry and second-order cancellation are natural, and this is a clear exposition of what happens. But for this particular result the rare-event law, normalized spacing fluctuation and independence mechanism are already supplied. The additional coordinates consist of elementary chord/area Taylor conversions of those same two variables, with no new limit mechanism or surviving independent invariant needing separate determination. The notation suggesting exact nonlinear centering would not change that judgment even if clarified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
