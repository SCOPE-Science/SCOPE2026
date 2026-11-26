---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For the exact locally Lipschitz field and a>0, b<=0, the shear w=z+cx²/2 gives w'=b|y|-x² and E' = zy² for E=(ax²+y²)/2. If c>=0, z<=w(0) makes Gronwall control x,y on each bounded forward interval, then integration controls w and hence z, giving continuation including c=0. For c=-k, set g=y-kx³/24 and h=z-kx²/4. On x=R, x'>0; on h=0 the lower margin is -x²+k²x⁴/96; on g=0 it is -ax+k²x⁵/192. The specified R makes all these strict, including at intersections, so the open sector is invariant. Inside, (x^-2)'<-k/12. A strictly positive integral margin on any initial compact time segment makes the stated lifetime bound strict, not merely non-strict as the displayed weak estimate alone would give. A bounded subsequence near finite maximal time would allow local continuation, so the norm tends to infinity. Off the equilibrium line, ∫(x²-b|y|)dt is strictly positive on any nonzero flow interval (even if b=0, by x'=y and uniqueness). This rules out return near the initial state. Equivalently invariance of the expectation of bounded arctan(w) forces stationary support. The algebra in the supplied checker was inspected, not executed; the argument does not need it. No backward-completeness or full escape-basin assertion is inferred.

## originality

PASS

The vector field and earlier studies of its dynamics are prior. The sharp universal-forward-existence split on b<=0, with a constructive open escape sector on the negative side and stationary-probability classification, was not covered by the strongest inspected claims. The exact indexed hit is the frozen record, not independent coverage. This is a bounded comparison, particularly because the 2019 same-field conference paper was not available for full-text comparison.

## value

PASS

For a studied nonlinear flow, a sharp sign boundary distinguishes parameters permitting a global forward phase space from those for which a robust nonempty set terminates in finite physical time. The explicit basin witness and usable time bound support analysis and simulations. The invariant-probability result identifies which stationary statistics are possible on the dissipative sign regime without implying that every complete trajectory converges or that compact heteroclinic sets cannot occur.

The dated certificate retains the supplied scientific assessment, sources and limitations.
