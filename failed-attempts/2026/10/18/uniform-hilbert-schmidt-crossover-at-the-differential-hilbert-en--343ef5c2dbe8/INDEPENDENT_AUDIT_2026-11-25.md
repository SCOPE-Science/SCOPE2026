# Independent mathematical audit

## correctness

PASS

With probability-normalized area, the squared monomial norm is w_n(γ)=B(n+1,γ+1)(γ+1). Expanding the kernel and integrating t^(n+k) gives exactly the rectangular-basis entry in RESULT.md:38–43. Independently, the full squared row is (n+1)^2 w_n(α+2+δ) times the integral of t^n(-log t)(1−t)^(−α−2) from 0 to 1: use the binomial series for 1/w_k(α) and the integral of t^(n+k)(−log t). For n≥1 the integral is B(n+1,−α)+O(B(n,1−α)), by 0≤−log t−(1−t)≤(1−t)^2/(2t). This verifies the coefficient Γ(α+4+δ)Γ(−α) and the uniform summable row error O_α(n^(−2−δ)); the zero row is finite. The entire missing column tail is O_α(N^α times the sum of (n+1)^(−α−1−δ) for n<N), which is O_α(N^(−δ)) because δ≤−α/2. Row summation and integral comparison give the fixed-interval bound, window and pole, and the endpoint divergence. Polynomial matrix calculations do represent the integral operator: radial evaluation is dominated by ||f|| times (1−t²)^(−(α+2)/2), integrable for α<0, so extension from polynomials agrees locally with the integral. The endpoint boundedness is also supplied by Li–Zhou. No finite numerical test is required for the proof; the frozen matrix checks were inspected, not rerun.

## originality

FAIL

The assigned quantitative claim is covered by another indexed finding, not just similar to one. The 2026/10/25 beta-prime energy record explicitly gives the additive-error square-section crossover in a signed window and the full pole. More decisively, its uniform row formula (9) and its displayed omitted-column bound directly yield the same fixed one-sided interval formula by summation, not just convergence along bounded δ log N. The 2026/10/18 root-exponential record separately states the identical full residue. These are coverage comparisons; neither dating nor the comparison proves who first obtained the result.

## value

PASS

As a mathematical statement the bounded-error interpolation is useful: it says how much squared Hilbert–Schmidt energy a finite section captures when both the cutoff and weight approach their limits, with the exact normalization. This is more informative than knowing Schatten membership. That intrinsic value does not give independent credit for a covered result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
