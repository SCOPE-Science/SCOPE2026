# Independent audit — 2026-10-01

## Final claim

For the two non-autonomous Moose-Wolf equations with unrestricted time-varying growth and death rates, the displayed three-constant gauge preserves the full observed trajectory, so the constant interaction parameters are structurally nonidentifiable without additional restrictions.

## Correctness — PASS

The primary source full text was inspected: it defines exactly the two non-autonomous equations with time-varying growth and death rates, then replaces those functions by constants for its structural-identifiability calculation and transfers the conclusion back by freezing one time. Direct substitution of the assigned transformed functions cancels the change in each constant interaction term identically in both models. Continuity gives the stated local ambiguity under interior parameter bounds and a positive mortality margin. The symbolic artifact independently simplifies all residuals to zero.

Checked sources: Singh and Kumari, A physics-informed inverse modeling framework for Moose-Wolf dynamics from limited and noisy data in Isle Royale National Park, arXiv:2609.20793v1; Martinelli, Identifiability of nonlinear ODE Models with Time-Varying Parameters, arXiv:2211.13507; Published finding dated 2026-09-18: Exact gauge family defeats structural identifiability in the time-varying Moose-Wolf models; Published finding dated 2026-09-19: Time-varying rates gauge away constant parameters in the Moose-Wolf inverse model; Assigned Git package and fresh direct algebraic substitution of both gauges

Residual risks: No correctness risk remains for the generic regular regime stated; architecture-restricted neural-network identifiability is a separate problem.; The exact same source-specific correction was already published before this record.

## Originality — FAIL

Originality fails decisively because an earlier published finding dated 2026-09-18 states the same source-specific three-parameter gauge for both the Holling and ratio-dependent Moose--Wolf equations, with essentially the same reconstruction formulas and conclusion. A second published finding dated 2026-09-19 also repeats the same correction. The assigned final claim is therefore covered even though it is correct.

### Equivalent formulations

Searches: Resultary semantic search for Moose-Wolf time-varying rate gauge and structural nonidentifiability; full-text inspection of the 2026-09-18 and 2026-09-19 published findings

Evidence: The 2026-09-18 result gives the same formulas for reconstructed growth and death rates for arbitrary alternative constants in both response models.; The assigned record's formulas are algebraically the same gauge written relative to an existing representation.

Reasoning: These are equivalent formulations of the same trajectory-preserving parameter-function symmetry.

### Broader coverage

Searches: general unknown-input identifiability literature; earlier 2026-09-18 source-specific published finding

Evidence: General theory is broader conceptually; the earlier source-specific finding is already exactly on the same equations and parameters.

Reasoning: The earlier result strictly covers the core source-specific nonidentifiability statement.

### Exact database or table

Searches: exact source title and arXiv identifier with `gauge`, `time-varying rates`, and `structural identifiability`

Evidence: Two independent published-finding entries were located, including one dated the day before the assigned record.

Reasoning: This is direct coverage, not merely an unsuccessful or approximate search.

### Claim versus prior implication

Searches: statement-by-statement comparison with the 2026-09-18 published RESULT.md

Evidence: Both state arbitrary changes in the three constants, exact compensating functions, perfect full-state nonidentifiability, failure of autonomous-to-nonautonomous transfer, positivity robustness and the need for extra rate information.

Reasoning: The earlier statement mechanically implies the assigned final claim.

### Source inspections

- **A physics-informed inverse modeling framework for Moose-Wolf dynamics from limited & noisy data in Isle Royale National Park** — https://arxiv.org/html/2609.20793v1
  Trigger: Exact target paper and equations being corrected
  Material read: Full HTML sections defining both models, structural-identifiability section, parameter constraints and training architecture
  Method: Primary full-text HTML inspection
  Assessment: Confirms the exact equations and the autonomous-freezing inference targeted by the correction.
  Evidence: Section 3.3 explicitly replaces the two time-dependent rates by scalars, reports autonomous identifiability, and then infers no redundancy by fixing one time.
- **Exact gauge family defeats structural identifiability in the time-varying Moose-Wolf models** — https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-time-varying-rates-destroy-moose-wolf-structural-identifiability--2c50538f59a6
  Trigger: Earlier source-specific result with same equations and conclusion
  Material read: Complete RESULT.md
  Method: Primary published-finding full-text inspection
  Assessment: Decisively covering.
  Evidence: It gives the same arbitrary-constant reconstruction formulas for both models and the same nonidentifiability conclusion.

Checked sources: Singh and Kumari, A physics-informed inverse modeling framework for Moose-Wolf dynamics from limited and noisy data in Isle Royale National Park, arXiv:2609.20793v1; Martinelli, Identifiability of nonlinear ODE Models with Time-Varying Parameters, arXiv:2211.13507; Published finding dated 2026-09-18: Exact gauge family defeats structural identifiability in the time-varying Moose-Wolf models; Published finding dated 2026-09-19: Time-varying rates gauge away constant parameters in the Moose-Wolf inverse model; Assigned Git package and fresh direct algebraic substitution of both gauges

Residual risks: No correctness risk remains for the generic regular regime stated; architecture-restricted neural-network identifiability is a separate problem.; The exact same source-specific correction was already published before this record.

## Scientific value — PASS

The source-specific correction is scientifically material: it distinguishes structural nonidentifiability from numerical fitting and identifies what extra information can break the gauge. Its value survives even though this particular record is not original because an earlier published finding already made the correction.

Checked sources: Singh and Kumari, A physics-informed inverse modeling framework for Moose-Wolf dynamics from limited and noisy data in Isle Royale National Park, arXiv:2609.20793v1; Martinelli, Identifiability of nonlinear ODE Models with Time-Varying Parameters, arXiv:2211.13507; Published finding dated 2026-09-18: Exact gauge family defeats structural identifiability in the time-varying Moose-Wolf models; Published finding dated 2026-09-19: Time-varying rates gauge away constant parameters in the Moose-Wolf inverse model; Assigned Git package and fresh direct algebraic substitution of both gauges

Residual risks: No correctness risk remains for the generic regular regime stated; architecture-restricted neural-network identifiability is a separate problem.; The exact same source-specific correction was already published before this record.

## Limitations

- The statement concerns unrestricted time-dependent functions in the ODE model, not a fixed finite neural architecture.
- Regularity/positivity conditions and nonzero denominators are required as stated.
- Scientific rejection is solely because an earlier published result already contains the same correction.

## Conclusion

Disposition: **failed**. Acceptance requires PASS on all three axes.
