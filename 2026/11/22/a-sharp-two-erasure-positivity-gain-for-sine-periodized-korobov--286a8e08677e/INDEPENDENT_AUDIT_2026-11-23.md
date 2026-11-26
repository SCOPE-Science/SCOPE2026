# Independent mathematical audit

## correctness

PASS

For variations vanishing at all nodes, the mean term and derivative term in the norm give S''=4π²γ∫S on each gap. The linear interpolant minus 2π²γ(∫S)Q is exactly that solution; solving for its mean using ∫Q=T/6 and integrating against the density yields the rank-one correction to the hat masses. The sign threshold is therefore a unique scalar crossing for this design once its denominator is positive. Independently, setting h=1/N and x=2πh, integration of the nearest hat on [−h,h] and [h,2h] gives the exact ratio [1+(sin x−sin 2x)/x]/(6h)=(7/9)π²h+O(h³). Ordinary hats have the sine value at the node times sinc²(πh), with smallest ratio 2π²h+O(h³), so exactly the four symmetric nearest sites minimize eventually. Two doubled gaps give T=h²+12h³. On each ordinary gap, the ratio of bubble mass to density mass is exactly (2/k²)(1−(kh/2)cot(kh/2)), k=2π, by integrating the cosine about the midpoint; this is h²/6+O(h⁴). Both doubled gaps carry only O(h²) density mass with an O(h²) bubble. Hence B=h²/6+O(h⁴), and the denominator is π²h²/3−7π⁴h³/27+O(h⁴). Its reciprocal gives the displayed (7/3)N+49π²/27+O(1/N). The strict minimum gap and monotonicity in γ check all three sign cases. The same calculation for the intact even grid has minimum [1−sin x/x]/(2h)=π²h/3+O(h³), giving the stated comparison. For a general density with minimum hat ratio zero, the exact criterion permits no positive γ; the scalar crossing is then at the endpoint γ=0 of the extended correction function, not a positive threshold.

## originality

PASS

The kernel, unconstrained optimization and subsampling prescription are known; the intact-grid threshold is also prior coverage. The supported distinction is the quantitative classification of this specific nonuniform two-erasure design, including the two coefficients and four minimizing sites, derived via the local formula.

## value

PASS

The two sites are distinguished by exact density zeros before computation. Erasing them changes both the minimum normalized hat mass and the allowable scale of γ by an exact factor greater than two, and identifies which retained weights lose positivity. This is a quantitative robustness fact about the unmodified quadrature weights, not a recomputation of the intact case or a postprocessed improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
