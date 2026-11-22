# Mathematical review

## Correctness — PASS
The exact four-dimensional elimination gives a third-order multiplicative recurrence with a memory-dependent coefficient. For the interior region the coefficient stays bounded away from zero, so positive Perron projection gives the rate \(\rho\). For the constructed endpoint, a monotone operator on an explicitly bounded sequence product produces an actual strictly positive four-dimensional trajectory. Its memory tail is asymptotic to its leading population term, changing the logarithmic recurrence from coefficients \((1,2)\) to \((2,2)\), and its stable complementary roots yield the constant prefactor. The standalone exact reduction and finite diagnostic checks passed. Infinite existence and asymptotics follow from the proof, not numerical experiments.

## Originality — PASS within inspected evidence
The full Wang–Tong–Li–Zhang–Iu–Li (2023) source states its four-dimensional map and fixed-point line but does not provide the zero-memristance endpoint trajectory or its sharp attraction clock. An existing three-dimensional \(c=1\) mathematical result already derives the interior Perron root \(\rho\) without memory; this is explicitly excluded from the novelty claim. Its autonomous scalar reduction does not contain the memory-induced factor that yields \(\beta\) at \(w_\infty=\sqrt2\). Searches of indexed work on discrete memristors, parabolic maps, superexponential attraction, and the numerical root found no directly dominating published statement. An equivalent unindexed proof remains possible.

## Value — PASS
At a natural zero of the model's square-charge memristance, the memory variable and population vanish together. This changes the exponent in a double-exponential law from \(\rho\approx1.6956\) to \(\beta\approx2.3593\), and makes the first multiplicative prefactor exact and parameter-only. The endpoint is actually populated by positive initial states, not just a formal asymptotic balance. This differentiates two stability mechanisms in a previously studied four-dimensional map.

## Scope and limitations
The construction fixes \(c=1\), with a positive interior open set and a separate nonempty endpoint family; it makes no global basin, uniqueness, or smooth-separatrix claim. The originating source was read in full HTML. Related published memristor maps use different equations; their available abstracts do not resolve the exact same-map comparison. Priority over inaccessible or unindexed work is not guaranteed.

Self-review: passed. Independent audit: not yet performed.
