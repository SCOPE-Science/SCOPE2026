# Independent mathematical audit — SCOPE-20260920-beb90a3a9bef

Final disposition: **FAILED**.

## Correctness
**PASS** — The explicit family is correct. With \(r=8/3\), \(x_1=1/4\) and \(x_2=\cdots=x_n=1/16\), exact exponent arithmetic gives \(Q=2^{-(2n+2)/3}\) and the normalized right side \(4^{1-n}+2(n-1)\), while the normalized conjectured left side is \(n\). Their difference is \(4^{1-n}+n-2>0\) for every \(n\ge2\), and \(8/3<e\). The two-level reduction is obtained by direct division and is also correct.

## Originality
**FAIL** — A later September 21 published finding gives a strictly stronger diagonal-instability theorem for the same Coronel–Huancas product inequality. It proves Conjecture 3.3 false in every dimension \(n\ge2\), supplies a continuum of counterexamples across a parameter range, identifies the sharp diagonal second-variation threshold, and also disproves the paper's \(r=1\) theorem for all \(n\ge4\). The assigned fixed family is therefore scientifically superseded at the time of this audit.

### Equivalent formulations
The later diagonal-instability statement strictly dominates the assigned dimension-wise falsification.

### Broader coverage
The prior-to-audit published theorem has broader parameter coverage and stronger consequences.

### Exact database or table
Positive stronger coverage is decisive; no negative-search inference is used.

### Claim versus prior implication
The assigned headline conclusion is a direct special case of a stronger published result.

## Value
**FAIL** — The fixed family is a clean counterexample, but the currently published stronger theorem already gives the same dimension-wise falsification together with a structural instability mechanism and stronger consequences. The assigned record has no separate surviving mathematical value under the audit bar.

## Source inspections
- **A diagonal-instability mechanism for a power-exponential product inequality** (https://github.com/Resultary/2026/tree/main/2026/9/21/SCOPE-power-exponential-product-local-instability--348ea42cbf67): complete published RESULT.md Method: published-record full-text inspection. Assessment: STRICTLY_STRONGER_CURRENT_COVERAGE. Evidence: It proves failure of Conjecture 3.3 for every \(n\ge2\) and gives the threshold \(e^2/(2n)\) for diagonal instability.
- **The proof of three power-exponential inequalities** (https://doi.org/10.1186/1029-242X-2014-509): accessible primary article section containing Conjecture 3.3 Method: primary full-text inspection. Assessment: ORIGINAL_CONJECTURE_SOURCE. Evidence: The article states the universal parameterized inequality that both records refute.

## Residual risks
- No correctness defect is asserted; rejection is scientific supersession.
