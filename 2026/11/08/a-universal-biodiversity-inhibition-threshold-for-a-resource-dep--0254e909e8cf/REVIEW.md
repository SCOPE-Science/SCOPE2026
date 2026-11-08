# Mathematical review

## Correctness

**PASS.** Every finite guild gives an irreducible finite continuous-time Markov chain. The stationary resource flux equation is \((c+e)p_m+kq_m=c\). Exact renewal splitting and an independent collection of single-consumer paths yield the survival integral \(L_m\). For positive \(u,k\), \(s(t)\in(0,1)\) for positive \(t\), making \(L_m\) strictly decrease and \(q_m\) strictly increase. A justified quadratic Laplace argument yields the limiting diversity and sharp approach. The independent rational solves in `verify.py` passed 66 stationary comparisons and 60 monotonicity checks. Risks: none detected under the specified model; numerical checks are supplementary, not a proof for all rates.

## Originality

**PASS on inspected evidence, with priority risk.** The complete accessible Lafferty–Dunne 2010 paper introduces the framework and reports simulation-based biodiversity-inhibitor classifications, but the relevant model, methods, results and discussion do not give the finite-specialist exact phase law or many-guild limit. Historical population-dependent-catastrophe theories are close mathematical precursors, not claimed as new methods; Brockwell–Gani–Resnick 1982 was accessible as metadata and abstract but not in full text, and the associated priority risk remains. The claim is a specific implication comparison, not title matching. Search non-retrieval alone was not treated as proof of priority.

## Value

**PASS.** The model isolates a natural ecological question posed by the simulation literature: can more potential consumer species produce less long-run realized richness because they can extirpate their shared resource? The sharp rate threshold, guild-size-independent neutral line and universal many-consumer ceiling give a substantive benchmark that cannot be read from individual species survival alone. The assumptions are restrictive and the result is not empirical policy advice.

Self-review: passed. Independent audit: not yet performed.
