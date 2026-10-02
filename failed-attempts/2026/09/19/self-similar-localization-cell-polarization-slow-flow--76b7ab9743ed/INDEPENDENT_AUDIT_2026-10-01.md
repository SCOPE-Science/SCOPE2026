# Independent scientific audit — SCOPE-20260919-76b7ab9743ed

Audited at: 2026-10-01T15:09:23.525185Z

Disposition: **failed**

## Correctness — PASS

The exact positive-part representation gives the two support inclusions and mass squeeze. Since the maximizing set is finite, the sublevel measure tends to zero, yielding \((t+\Phi)G(\sigma)\to1\), hence \(tG(\sigma)\to1\). Regular-variation inversion gives the stated \(\sigma,\Phi,\phi\) rates, and the local homogeneous scaling directly yields the positive-part similarity profile and support-area constants. The symbolic artifact correctly checks the exponent and coefficient identities but is only corroborative.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify_asymptotics.py
- published SCOPE Morse-localization result

### Correctness risks

- The monotone-density derivative asymptotic uses the source's monotonicity of the multiplier; without that hypothesis, differentiation of a regularly varying primitive would need extra justification.

## Originality — FAIL

A published SCOPE record dated 2026-09-18 already derives the same exact representation, introduces the same threshold variable, proves the same mass squeeze through \(G\), and obtains the \(t^{-1/4}\) Morse width, \(t^{1/2}\) peak, \(t^{-1/2}\) multiplier gap, support asymptotics, and local parabolic-cap profile. The assigned record generalizes that identical argument by replacing the quadratic law \(G(s)\sim Cs^2\) with the source paper's already-computed homogeneous law \(G(s)\sim Cs^{1+2/m}\) and then performing standard regular-variation inversion.

### Equivalent formulations

The assigned clock is the same squeeze before substituting the quadratic asymptotic; its homogeneous extension is the same proof with a different already-known power of \(G\).

### Broader coverage

Together they mechanically imply the assigned homogeneous power laws and profile, so the combination is broader in ingredients than the assigned standalone statement.

### Exact database or table

No database lookup is needed: theorem implication from the earlier record and source asymptotics is decisive.

### Claim versus prior implication

Substitution of \(G(s)\sim Cs^{1+2/m}\) and regular-variation differentiation yields every displayed exponent and coefficient.

### Sources inspected

- Morse maxima force a \(t^{-1/4}\) localization law in the slow cell-polarization limit — published SCOPE record 2026/09/18/morse-maxima-t-quarter-cell-polarization-localization--95d03c9c0771. COVERING_INGREDIENT: It contains the dynamic localization mechanism that the assigned record generalizes verbatim.
- Localization properties of a free boundary problem for cell polarization — https://arxiv.org/abs/2609.20609. COVERING_INGREDIENT: The source supplies the homogeneous sublevel asymptotic used as the only new input beyond the earlier SCOPE dynamic argument.

### Checked sources

- published SCOPE 2026/09/18/morse-maxima-t-quarter-cell-polarization-localization--95d03c9c0771
- https://arxiv.org/abs/2609.20609
- https://arxiv.org/abs/2605.03553

### Residual risks

- The primary source full text was not independently re-downloaded in this run; however, the originality failure is already decisive from the earlier published SCOPE proof combined with the source ingredient explicitly used by the assigned record.

## Value — FAIL

The formulas are useful, but once the earlier Morse proof is available the assigned theorem is a routine regular-variation abstraction using a homogeneous sublevel law already supplied by the source. It does not isolate a new mechanism or independently unknown exact invariant under the stated value standard.

### Value sources

- published SCOPE Morse-localization theorem
- https://arxiv.org/abs/2609.20609

### Value risks

- A broader exposition of the clock may still be pedagogically valuable.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The result concerns the zero-diffusion slow-time limit, not the original fixed-diffusion parabolic problem.
- Explicit power laws require finite isolated maxima with the stated homogeneous asymptotics.
