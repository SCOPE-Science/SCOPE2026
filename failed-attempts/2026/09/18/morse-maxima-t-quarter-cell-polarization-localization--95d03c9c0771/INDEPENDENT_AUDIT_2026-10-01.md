# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-95d03c9c0771`

## Correctness — PASS

From the exact representation \(u=[u_0+A-(t+A)h]_+\), mass conservation squeezes \((t+A)G(q)\) to one, with \(G(s)=Cs^2+o(s^2)\) for isolated Morse minima. This yields \(q\sim(Ct)^{-1/2}\), \(A\sim\sqrt{t/C}\), the support scale \(t^{-1/4}\), and the parabolic-cap profile after Hessian rescaling. The multiplier asymptotic follows from the support sublevel asymptotics rather than differentiating an equivalence. The inspected quadratic-model script checks only constants and agrees with the analytic derivation.

### Correctness sources

- assigned RESULT.md and artifacts/verify_quadratic_cap.py
- Niethammer–Röger–Velázquez, arXiv:2609.20609

### Correctness risks

- The theorem is only for the zero-diffusion slow-limit dynamics with isolated nondegenerate maxima.

## Originality — FAIL

A later published SCOPE result gives a strictly broader localization-clock theorem for the same slow flow and explicitly specializes it to Morse maxima with the same \(t^{-1/4}\) width, \(t^{1/2}\) height, \(t^{-1/2}\) multiplier gap, Hessian constants, and positive-part local profile. The audited claim is therefore currently covered, even though the covering record postdates it.

### equivalent_formulations

Searches:
- Resultary semantic search for cell-polarization slow-flow Morse localization rates
- full comparison with the 2026-09-19 localization-clock result

Evidence:
- The later result contains a dedicated 'Generic Morse maxima' specialization with the same exponents and formulas.

Reasoning:
The later threshold variable \(\sigma\) is the audited \(q=A/(t+A)\); its Morse specialization is the same claim after notation change.

### broader_coverage

Searches:
- 2026-09-19 SCOPE localization-clock theorem
- Niethammer–Röger–Velázquez source paper

Evidence:
- The later theorem handles arbitrary power-law sublevel geometry and homogeneous maxima, so it strictly dominates the audited Morse-only case.

Reasoning:
A general theorem covering all homogeneous maxima is broader than the audited nondegenerate-quadratic case.

### exact_database_or_table

Searches:
- Resultary exact and semantic searches

Evidence:
- No database lookup is needed once theorem-level coverage is located.

Reasoning:
This originality check is theorem-implication based, not table based.

### claim_vs_prior_implication

Searches:
- statement-by-statement implication comparison

Evidence:
- The later result states the same Morse asymptotics and profile as an explicit corollary.

Reasoning:
Current published coverage is decisive under the special-case/corollary rule.

### source_inspections
- **A localization clock and self-similar rates for the cell-polarization slow flow** — https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-self-similar-localization-cell-polarization-slow-flow--76b7ab9743ed. Trigger: Highest relevant Resultary hit and same model. Material read: Complete RESULT.md including proof and the Generic Morse maxima section. Method: Full statement-and-proof implication comparison. Assessment: DECISIVE CURRENT COVERAGE; strictly broader than the audited theorem. Evidence: It gives the localization clock and then the same Morse exponents, constants and rescaled positive-part profile.
- **Localization properties of a free boundary problem for cell polarization** — https://arxiv.org/abs/2609.20609. Trigger: Primary source model. Material read: Abstract and public metadata; direct arXiv full-text retrieval failed in this run. Method: Primary-source scope comparison. Assessment: Supplies the underlying slow-flow model and qualitative localization; not needed for the decisive current-coverage finding. Evidence: The abstract states slow-time localization and characterization of concentration.

### checked_sources

- later published localization-clock SCOPE result
- arXiv:2609.20609
- arXiv:2605.03553
- assigned package

### residual_risks

- The covering theorem was published one day later, so this audit does not determine historical priority on 2026-09-18.
- Primary arXiv full text was not retrievable through the available web route in this run.

## Scientific value — PASS

The Morse-rate theorem is a natural and useful sharp asymptotic boundary result for a cell-polarization free-boundary flow. Current coverage defeats originality, not mathematical significance.

### Value sources

- later general localization-clock theorem
- assigned self-contained proof

### Value risks

- Value does not restore acceptance when originality fails.

## Limitations

- Current scientific rejection is originality-only; correctness and value pass.
- The decisive covering result postdates the audited record, so historical first-discovery priority is not adjudicated.
- The result does not address finite diffusion or degenerate maxima.

## Disposition

**FAILED**
