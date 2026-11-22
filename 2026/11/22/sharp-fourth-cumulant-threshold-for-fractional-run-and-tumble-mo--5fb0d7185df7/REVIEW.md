# Scientific review

## Correctness — PASS

The ordered-time four-point cumulant of the symmetric telegraph process equals \(-2e^{-2\gamma[(u_3-u_1)+(u_4-u_2)]}\); permutation symmetry gives the exact factor \(-48v_0^4/\Gamma(n)^4\). In gap coordinates the exponential factor is \(e^{-2\gamma(x+2y+z)}\), whose total mass is \(1/(16\gamma^3)\). Local integrability is guaranteed by \(n>0\). The large-base-point integrand is \(s^{4n-4}/(16\gamma^3)\), with a controlled \(O(s^{-1})\) relative remainder. Integrability changes precisely at \(n=3/4\), giving the finite, logarithmic, and power regimes with exact coefficients. The variance calculation independently gives the stated standardized rates. The numerical checker passed 156 deterministic assertions, supplementary to the proof.

## Originality — PASS (best-knowledge literature comparison)

The principal exact-family paper (Dean–Majumdar–Schawe, arXiv:2009.01487, full text examined) covers the \(n=1/2\) variance threshold, general distribution tails and special-order generating functions, not the all-order fourth-cumulant transition at \(n=3/4\). Santra–Ajgaonkar–Basu, arXiv:2304.11378, examines the integer acceleration case; it neither states nor subsumes this fractional-index transition. Existing positive-filter telegraph cumulant literature already implies strict negativity; the result **does not** claim that sign as new. The distinct object of originality is the sharp bounded/logarithmic/divergent absolute fourth-cumulant classification and its universal amplitudes, which is not an immediate stated consequence of the previously published variance result. Risk: equivalent unindexed applications of connected-correlation expansions may exist; no exhaustive publication-priority assertion is made.

## Value — PASS

The source identifies a localization threshold via second moments. Here the fourth cumulant remains finite through a strictly larger index interval and develops a second exact singular boundary at \(n=3/4\). This makes a physically motivated distinction between width growth and non-Gaussian fluctuation-amplitude growth; the critical logarithm and universal kurtosis coefficients give measurable diagnostics beyond an isolated numerical evaluation or restatement of general cumulant negativity.

## Scope and verification limits

All claims concern fixed positive \(n\), \(\gamma\), and \(v_0\) with a symmetric stationary telegraph sign. The finite tests cannot certify statements at infinitely many times. Inaccessible or unindexed literature remains a possible priority risk.

Self-review: passed. Independent audit: not yet performed.
