# Independent mathematical audit

## correctness

PASS

The m-th monomial alone has changed squared norm m!(1+τm!), giving e^t−qt^m for t=z conjugate(w), q=τ/(1+τm!). At a fixed radius s the real phase function mθ−s sin θ has largest attained admissible multiple of 2π equal to (m−1)π in the upper half-plane: it is strictly convex, its endpoint values are 0 and mπ, and it increases after the unique crossing in ((m−1)π/m,π). This crossing maximizes the angle among phase candidates and minimizes s^(−m) exp(s cos θ). Since cos θ_m<0 and θ_m increases, C_m decreases strictly from infinity to zero. The scalar modulus equation then excludes every s<r_* and allows exactly the phase-extremal pair at r_*; a multiple scalar root would have to be t=m. Realizability of products precisely for |t|<R² gives the inclusive threshold R²≤r_* for the open bidisk. The strict radial gap follows from C_m(r)>r^(−m) exp(−r). Writing δ=π−θ_m gives mδ+r sin δ=π, so δ=O(r^(−1)) and δ=π/(r+m)+O_m(r^(−3)). Thus log C_m(r)=−r−m log r+π²/(2r)+O_m(r^(−2)). Both defining radii are L−m log L+O_m(log L/L); the mean-value theorem on r+m log r gives the coefficient and stated remainder for their difference. The independent finite bisection/Lambert-W diagnostic at m=3,5,7,9 and τ=10^(−6),0.03,1,200 confirmed the pair and gap in a branch window −8 to 8 (replay: /workspace/branches/695fcd85-98e9-4b08-b4ec-f88e3deb2a28/independent_check.py; output independent_check_results.txt alongside it). It does not establish the all-branch cutoff; the phase comparison does. The frozen script was inspected, not executed.

## originality

PASS

The kernel modification and Lambert-W parametrization are established methods. The even-jet result addresses a closely related but parity-distinct extremum. General W branch geometry gives phase equations and branchwise uniqueness, but the assessed distinct claim is the sharp comparison across the phase candidates for every admissible penalty and its quantified improvement over the radial bound. No inspected source states or directly supplies the combined global selection and sharp gap. This is not historical priority certification.

## value

PASS

The exact first-zero bidisk is a natural observation-domain invariant for this deformation of the Gaussian kernel. The result shows why the radial estimate is not attained at odd orders, locates the actual critical pair without an arbitrary branch cutoff, and quantifies the leading loss in that estimate as the penalty vanishes. This is a sharp parity-sensitive boundary, not just another Lambert-W notation for the roots.

The dated certificate retains the supplied scientific assessment, sources and limitations.
