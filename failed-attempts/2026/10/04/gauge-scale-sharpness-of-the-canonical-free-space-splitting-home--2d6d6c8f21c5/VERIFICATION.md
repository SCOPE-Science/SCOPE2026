---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Kalton's Proposition 5.1 gives the exact canonical homeomorphism \(\phi(\gamma,x)=\gamma+\delta_\omega(x)\), its inverse, and the upper bounds \(\omega_\phi(t)\le 2\omega(t)\) and \(\omega_{\phi^{-1}}(t)\le 3\omega(t)\). The submitted lower bound for \(\phi\) follows by comparing \((0,tu)\) with \((0,0)\), since \(\|\delta_\omega(tu)-\delta_\omega(0)\|=\omega(t)\). For the inverse, using \(\eta_t=t\delta_\omega(u)\) with \(\|\eta_t\|=t\), the published inverse formula and the reverse triangle inequality give a coordinate difference at least \(\omega(t)\). Thus both two-sided modulus estimates and the failure of every smaller logarithmic exponent are correct.

## originality

FAIL

The final claim is directly implied by published formulas. Kalton's Proposition 5.1 already prints the canonical map, its inverse, the free-space section identity, and both upper modulus bounds. Cheng--He--Xiang reproduce the same canonical map and upper bounds for the exact logarithmic gauge used here. The two lower bounds are immediate test-pair calculations from those displayed formulas and the defining isometry of \(\delta_\omega\); no additional nonstandard lemma or unresolved comparison is needed. Under the audit rule that direct corollaries and mechanically implied special cases are covered even when the sharpness sentence is not printed verbatim, originality fails.

## value

FAIL

Showing that the exponent in a current construction is sharp is a motivated question, but here the sharpness proof is a routine test-vector exercise once the published explicit homeomorphism, inverse, and free-space norm identity are written down. It does not isolate a new structural obstruction, boundary phenomenon, or difficult exact invariant under the common value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
