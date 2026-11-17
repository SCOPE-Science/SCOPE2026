# Independent mathematical audit

## correctness

PASS

For the exact quadratic map x_{j+1}=−(1+μ)x_j+Qx_j² and fixed 0<Qx0<1/4, even-time u=Qx has exact two-step polynomial u↦u[(1+μ)²+μ(1+μ)u−2(1+μ)u²+u³]. The inverse-square coordinate obeys a nonautonomous nearly affine recurrence; its differentiated recurrence is controlled with summed O(sqrt N) remainder for μ=z/N and z in compacts. Thus both H(t)=(1−exp(−2zt))/z and ∂_z H converge away from the initial layer; the latter contributes O(δ²) after χ_N/N² normalization. The integral S(z) follows; independent SymPy expansion verifies its V(z,t) coefficients 1,zt/2,z²t²/24 giving S(0)=1/16,S'(0)=1/72. Fresh 25000-step sensitivity trajectories at z=-1,0,1 agree with the numerical integral within 1.9×10^-4; these finite values do not prove compact-uniform convergence. At μ=0, v_m^-2=4m+O(sqrt m) and two-step derivative 1−6v²+4v³ yields the log coefficient −3/2. No global peak uniqueness or nonhyperbolic broad-model extension claimed.

## originality

PASS

Martin–Tang–Chialvo 2025 use this identical canonical quadratic flip map and introduce finite-time susceptibility, demonstrate χ_N~N² and numerical collapse, and give state finite-time scaling. Those foundational objects, exponent and generic crossover are credited. The submitted additional claim is an actual parameter-differentiated all-z integral profile with rigorously justified normalization, positive-side derivative 1/72, and exact Lyapunov log coefficient −3/2; the 2025 Appendix gives state scaling, qualitative exponents and plots, not these exact sensitivity quantities in the inspected primary pages. Corral 2024 addresses +1 multiplier bifurcations. Best-of-knowledge PASS with risk an alternative differentiated state formula could already yield the same profile in uninspected later works.

## value

PASS

Exact finite-time response profile and its critical normalized amplitude distinguish observables sharing the same known exponent, while a nonzero slope quantifies the displaced finite-size peak. The signed −3/2 Lyapunov logarithmic correction is a natural critical-dynamics invariant rather than a restated scaling exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
