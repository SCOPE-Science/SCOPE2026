---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Gaussian integration gives the exact Z_T. Ground-state conjugation gives a confining Schrödinger operator with locally bounded potential (V′ is continuous, so there is no interface delta) and the usual one-node characterization of the gap. On each exterior half-line the weighted square-integrable solution is the recessive parabolic-cylinder branch; its origin ratio is −√2 Γ((1−ν)/2)/Γ(−ν/2), which reduces to the stated positive gamma quotient. For 0<ν<1 the recurrence in terms of the two lower, negative-order cylinder functions makes it positive throughout the outward half-line. Left and right logarithmic derivatives have opposite signs in the global coordinate. The interior cosine starts at phase arctan r_- and ends at π−arctan r_+, with exactly one interior zero. With u=√T the implicit equation is smooth near (k,u)=(π/L,0) and its k derivative tends to L>0. The tail gamma expansion contributes log 2 and the cubic arctangent subtracts (π/2)/3, giving the stated B; B>0. With k0=π/Z_T the shift is −B k0³ T^(3/2)/Z_T+O(T^(5/2)), so expanding T k² and replacing Z_T by L in the correction gives the stated O(T³) error. As a separate finite check, solved the half-interval odd-state condition for L=κ_-=κ_+=1 using a midpoint Dirichlet condition and a Tricomi U tail evaluated near the interface. The measured/predicted correction ratios at T=10⁻³,10⁻⁴,10⁻⁵,10⁻⁶ were approximately 0.684567, 0.883831, 0.961323, 0.987564. These values test sign and coefficient, not the asymptotic proof. Replay RESULT.md:35–72. Frozen check_spectrum.py was inspected, not executed; its recorded PASS counts are finite evidence only.

## originality

FAIL

The Nov. 2 published Resultary expansion gives the same beyond-mass coefficient for the exact symmetric subcase, more strongly for every fixed mode with an unexpanded effective denominator and a sharper remainder. It also supplies the complete one-wall impedance and its cubic phase coefficient. Equal nonunit stiffness amounts to rescaling; at unequal stiffnesses the very same two single-wall phases merely add in the flat interval, as shown below. No distinct dispersive coefficient or new mechanism survives narrowing to unequal walls. This is verified prior coverage and a routine extension, not a verdict based on a missing article.

## value

FAIL

The negative beyond-mass term is a scientifically natural invariant, but it is not newly obtained in this record. After excluding the earlier all-fixed-mode result, the change is just substituting the two stiffnesses in a known local boundary formula and adding phases. There is no new, nonmechanical remainder to preserve by narrowing the result or by adding numerical corroboration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
