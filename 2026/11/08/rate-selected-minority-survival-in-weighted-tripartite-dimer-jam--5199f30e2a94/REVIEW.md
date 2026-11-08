# Scientific review: rate-selected minority survival in weighted tripartite adsorption

## Correctness

**PASS.** Edge counts produce the stated exact finite Markov transition probabilities. Independent exponential clocks of weights divided by system size have precisely the same ordered deposition law. Their bounded-jump martingale decomposition and a locally Lipschitz drift justify a finite-time fluid limit. The symmetry reduction, integrating-factor identity, three positive-root cases and threshold equality establish the closed formula. A pathwise future-consumption bound controls the infinite-time/large-size interchange, without relying on numerical experiments. The two separate reproducibility scripts passed exact labeled-state comparisons, symbolic invariant differentiation, deterministic integrations and finite stochastic checks. The result explicitly excludes vanishing reaction rates and does not claim a critical-window law.

## Originality

**PASS on examined evidence, with historical-priority risk.** The rate-symmetric three-species mean-field law was treated by ben-Avraham and Redner (1986), so that known \(\rho=1\) case is not treated as independently new. Hilhorst, Washenberger and Täuber (arXiv:cond-mat/0409079, Sections 2–3 and conclusion) supply the general annihilation master equation and discuss equal-density decay; Section 3.1 explicitly excludes analysis of the unequal-density surviving states. Their symmetry-normalized rate setting does not evaluate the asymmetric \(AB=AC\ne BC\) terminal-density function for arbitrary initial \(a,b\). Pippenger's foundational graph RSA results do not identify this precise high-degree weighted tripartite law. Comparisons checked random greedy matching, equivalent three-species annihilation vocabulary, master-equation parameter reduction, source- and claim-based record searches, and the accessible historical claims for related graph adsorption. No source examined gives this exact weighted threshold and the finite stochastic terminal LLN. Full text of the closely relevant 1986 work remained inaccessible; it is a stated risk, not a claim of having ruled out all equivalent results.

## Mathematical value

**PASS.** A fixed positive rate change produces a sharp, continuously tunable jamming transition in a natural three-color adsorption network that can admit perfect matchings. The nontrivial surviving-density expression and onset exponent \(2b/a\) quantify how irreversible kinetics selects one part even when that part initially contains fewer sites than either competing part. The exact finite-size recurrence links the macroscopic transition with reproducible finite systems. This is more than static matching feasibility, a renamed master equation or a small finite calculation.

## Closest literature and remaining limits

- D. ben-Avraham and S. Redner (1986), https://doi.org/10.1103/PhysRevA.34.501: equal-rate three-species kinetic precursor, with abstract but not full text examined.
- N. Pippenger (1989), https://doi.org/10.1137/0402034: general irreversible graph adsorption precursor, with abstract and publication details examined.
- H. J. Hilhorst, M. J. Washenberger and U. C. Täuber (2004), https://arxiv.org/abs/cond-mat/0409079: original full text examined in relevant sections, including the explicit decision not to analyze unequal-density terminal states.

Priority is provisional pending broader expert literature comparison; the theorem is limited to positive fixed edge rates and the specified symmetric two-part initial populations. Simulations are supporting checks, not infinite-size proof. No external or independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
