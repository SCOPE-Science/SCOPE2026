# Independent mathematical audit

## correctness

PASS

For a real BV equivalence class, f is a constant plus the integral of h_s=1_(s,1) against Df, whose total variation is the seminorm on the open interval. The two averaging kernels preserve constants and monotonicity (write their arguments as xU and 1−(1−x)U with power-distributed U), so each composed step gain is its output endpoint difference. Fubini and the triangle inequality bound the seminorm by the integral of these gains against |Df|; a step realizes the gain, giving equality for the supremum. For right after left, the endpoints are 1−s^α and β∫_s^1(1−u)^(β−1)[1−(s/u)^α]du. Their difference has derivative αs^(α−1)[β∫_s^1(1−u)^(β−1)u^(−α)du−1]. The bracket is strictly decreasing from a positive limit (the full probability average of u^(−α) exceeds 1, possibly infinitely) to −1. For left after right, the endpoints are 1−s^α+α(1−s)^β∫_0^s u^(α−1)(1−u)^(−β)du and (1−s)^β. The derivative is β(1−s)^(β−1) times 1 minus the corresponding truncated integral with its α factor; this bracket strictly decreases from 1 to a negative limit. Both stationarity equations give the stated interior norm values, strictly between zero and one. A norming |Df| must concentrate at the unique maximizer, yielding exactly the stated single jumps modulo constants. Separately, the one-sided step gains 1−s^α and 1−(1−s)^β approach 1 at their respective maximizing endpoints. For β=1 direct integration gives s=α^(1/(1−α)) or e^(−1). At (1,2), the left-after-right profile is 2s(1−s); the opposite profile at 1/3 is (2/3)log 3−2/9>1/2 by the positive log series. Bisection of 2s−3−2log(s)=0 gave s≈0.301709562684336 and the opposite norm ≈0.512390465153499. Analytic replay: RESULT.md lines 39–71; the bundled checker was inspected, not executed.

## originality

PASS

The distinct contribution supported by the comparisons is the exact real BV-seminorm contraction for both orders for general positive power parameters, together with the unique interior jump normers and explicit order asymmetry. General Hardy norm theory and the positive-measure reduction are not claimed as new. The closest indexed two-order Hardy–Copson result concerns an identity error in a different output norm.

## value

PASS

The one-sided normalized averages individually have no strict margin in variation, yet composition in either opposite order does. Exact norms give both the worst jumps and the magnitude of the margin for all positive parameters, and distinguish the two orders even for simple powers. Neither the product of the separate norm bounds nor a qualitative smoothing result gives this information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
