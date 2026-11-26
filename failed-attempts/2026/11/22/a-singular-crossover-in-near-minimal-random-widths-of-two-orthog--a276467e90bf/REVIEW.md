# Independent mathematical audit

## correctness

PASS

The two opposing support maxima give W=A+B+max(|A−B|,t|v|). Because W≥2 max(A,B) and A²+B²=1+v², equality at √2 forces v=0 and equal transverse squared coordinates, giving precisely four oriented minima. In fact 4 max(A,B)²=2[1+v²+(1−v²)|cos(2φ)|]; this uniformly localizes the event to v=O(√ε) and longitude offsets s=O(ε). Taylor expansion near a chart yields A+B=√2+v²/√2+O(s²+v⁴) and |A−B|=(1−v²)|cos(2φ)|/(A+B)=√2|s|+O(s²+|s|v²). The exact term t|v| in the maximum strengthens localization to v=O_t(ε) for fixed t>0. Haar probability is dφ dv/(4π). The fixed-t limiting rectangle has area 2√2/t; at finite t/√ε→τ the limiting section at each y is |x|≤(1−y²/√2)/√2 with |y|≤y_τ. These bounded sublevel sets have null boundaries and convergence gives both the probability and uniform conditional law, with four equal charts. Integrating yields F and the τ=0 constant; rationalization gives y_τ∼1/τ. Replay: frozen RESULT.md from the exact support identity through its local rescaling; VERIFICATION.md and verify_width.py were inspected, not executed. The stated finite-τ limit and the fixed-positive-t limit are not a uniform arbitrary-path claim.

## originality

FAIL

A distinct indexed result, 478c8834f500, covers the actual lower-endpoint theorem, not just mean width or a special case. Its body, Haar sampling, four minimizers, all fixed-positive-separation coefficients, coincident-center coefficient, and locally uniform critical-window profile coincide with or imply the frozen statements. Its folded angular law recovers the frozen four-chart law by reflection symmetry and a constant linear coordinate change in the limit. Both catalogue dates are 2026-11-22; this establishes substantive equivalent coverage, not who proved or published it first. No materially new frozen remainder survives the comparison.

## value

PASS

The mathematical result is useful in its own right: an established body has a lower-tail exponent change when a linear angular constraint disappears, and the limiting conditional shape resolves how directions concentrate across the singular scale. This is a structural endpoint calculation, not just a mean or a sampled numerical value. That merit does not make this frozen formulation a distinct contribution in light of the equivalent catalogue law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
